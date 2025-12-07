import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "marketbasket.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
df = df.fillna(0)
for column in df.columns:
    df[column] = df[column].astype("bool")
print(df.head())

# --- Apriori ---
apriori_result = apriori(df, min_support=0.01, use_colnames=True)
print(apriori_result)

RULES_COUNT = 3
rules = association_rules(apriori_result, metric="confidence", min_threshold=0.1)
sorted_rules = rules.sort_values("confidence", ascending=False)
results_matrix = rules[["antecedents", "consequents", "confidence"]]
print(results_matrix.head(RULES_COUNT))

# --- FP-Growth ---
fpgrowth_result = fpgrowth(df, min_support=0.01, use_colnames=True)
rules = association_rules(fpgrowth_result, metric="confidence", min_threshold=0.1)
sorted_rules = rules.sort_values("confidence", ascending=False)
results_matrix = rules[["antecedents", "consequents", "confidence"]]
print(results_matrix.head(7))
