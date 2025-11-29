import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE, SelectKBest, VarianceThreshold, f_classif

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# 1. Variance Threshold
vt = VarianceThreshold(threshold=0.3)
X_vt = vt.fit_transform(X, y)
vt_features = [f for f, keep in zip(feature_names, vt.get_support()) if keep]

# 2. Univariative Selection (SelectKBest with f_classif)
skb = SelectKBest(score_func=f_classif, k=3)
X_skb = skb.fit_transform(X, y)
skb_features = [f for f, keep in zip(feature_names, skb.get_support()) if keep]

# 3. Recursive Feature Elimination (RFE with Logistic Regression)
log_reg = LogisticRegression()
rfe = RFE(estimator=log_reg, n_features_to_select=3)
X_rfe = rfe.fit_transform(X, y)
rfe_features = [f for f, keep in zip(feature_names, rfe.support_) if keep]

# 4. L1-based feature selectin (Logistic Regression with L1 penalty)
l1_log_reg = LogisticRegression(penalty="l1", solver="liblinear", max_iter=200)
l1_log_reg.fit(X, y)
l1_support = np.abs(l1_log_reg.coef_).sum(axis=0) > 0
l1_features = [f for f, keep in zip(feature_names, l1_support) if keep]

# 5. Tree-based feature selection (Random Forest)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)
rf_importances = rf.feature_importances_
rf_features = [f for f, imp in zip(feature_names, rf_importances) if imp > 0.03]

# Results
results = DataFrame(
    {
        "Features": feature_names,
        "VarianceThreshold": [f in vt_features for f in feature_names],
        "SelectKBest": [f in skb_features for f in feature_names],
        "RFE": [f in rfe_features for f in feature_names],
        "L1-based": [f in l1_features for f in feature_names],
        "Tree-based": [f in rf_features for f in feature_names],
    }
)
print(results)


# --- Visualization ---


# Create figure and axis
plt.figure(figsize=(12, 6))

# Set up bar positions
x = np.arange(len(feature_names))
width = 0.15

# Plot coefficients for each method
plt.bar(
    x - 2 * width,
    [l1_log_reg.coef_[0][i] for i in range(len(feature_names))],
    width,
    label="L1-based",
    color="skyblue",
)
plt.bar(
    x - width,
    [rf.feature_importances_[i] for i in range(len(feature_names))],
    width,
    label="Tree-based",
    color="lightgreen",
)
plt.bar(
    x,
    [
        np.mean([vt.get_support()[i], skb.get_support()[i], rfe.support_[i]])
        for i in range(len(feature_names))
    ],
    width,
    label="Other Methods (Mean)",
    color="salmon",
)

# Customize the plot
plt.xlabel("Features")
plt.ylabel("Coefficient/Importance Score")
plt.title("Feature Selection Coefficients Comparison")
plt.xticks(x, feature_names, rotation=45)
plt.legend()

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
