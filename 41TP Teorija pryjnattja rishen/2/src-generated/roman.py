import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from scipy.optimize import minimize, minimize_scalar


class BivariateNormalAnalysis:
    def init(self, mean_x, mean_y, var_x, var_y):
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.var_x = var_x
        self.var_y = var_y
        self.std_x = np.sqrt(var_x)
        self.std_y = np.sqrt(var_y)

        # Вихідні дані для розрахунків
        self.R_values = [-0.6, -0.7]
        self.X_observations = [11.8, 11.2, 10.0, 8.8]
        self.k_factors = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3]

    def get_conditional_mean(self, x, r):
        return self.mean_y + r * (self.std_y / self.std_x) * (x - self.mean_x)

    def get_conditional_variance(self, r, base_variance=None):
        if base_variance is None:
            base_variance = self.var_y
        return base_variance * (1 - r**2)

    def univariate_pdf(self, val, mean, var):
        std = np.sqrt(var)
        if std == 0:
            return float("inf") if val == mean else 0
        exponent = -((val - mean) ** 2) / (2 * var)
        return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(exponent)

    def bivariate_pdf(self, x, y, r):
        if abs(r) == 1.0:
            return None

        denom = 2 * np.pi * self.std_x * self.std_y * np.sqrt(1 - r**2)

        norm_x = (x - self.mean_x) / self.std_x
        norm_y = (y - self.mean_y) / self.std_y

        exponent = (
            -1 / (2 * (1 - r**2)) * (norm_x**2 - 2 * r * norm_x * norm_y + norm_y**2)
        )

        return (1 / denom) * np.exp(exponent)

    @staticmethod
    def _calculate_error(value, optimal):
        abs_err = np.abs(value - optimal)
        rel_err = (abs_err / np.abs(optimal)) * 100 if optimal != 0 else 0
        return abs_err, rel_err

    def run_error_variance_analysis(self):
        print("\n--- 1. Аналіз дисперсії похибки D[Δy~] ---")
        r_range = np.linspace(0.0, 1.0, 11)
        var_multipliers = [self.var_y, 2 * self.var_y, 4 * self.var_y]

        plt.figure(figsize=(8, 5))

        table = PrettyTable()
        table.field_names = ["r"] + [f"d_y = {dy:.2f}" for dy in var_multipliers]

        for dy in var_multipliers:
            error_dispersions = [
                self.get_conditional_variance(r, base_variance=dy) for r in r_range
            ]
            plt.plot(
                r_range,
                error_dispersions,
                label=f"d_y = {dy:.2f}",
                marker="s",
                linestyle="--",
            )

        for r in r_range:
            row = [f"{r:.1f}"]
            for dy in var_multipliers:
                disp = self.get_conditional_variance(r, base_variance=dy)
                row.append(f"{disp:.4f}")
            table.add_row(row)

        print("\nТаблиця значень дисперсії похибки D[Δy~]:")
        print(table)

        plt.xticks(r_range)
        plt.title("Залежність дисперсії D[Δy~] від коефіцієнта кореляції r")
        plt.xlabel("Коефіцієнт кореляції r")
        plt.ylabel("Дисперсія похибки D[Δy~]")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def run_unconditional_density_table(self):
        print("\n--- 2. Таблиця безумовної густини W(y) ---")
        table = PrettyTable()
        table.field_names = ["y (точка)", "W(y) (густина)"]

        for k in self.k_factors:
            y_pos = self.mean_y + k * self.std_y
            y_neg = self.mean_y - k * self.std_y

            W_pos = self.univariate_pdf(y_pos, self.mean_y, self.var_y)
            W_neg = self.univariate_pdf(y_neg, self.mean_y, self.var_y)

            table.add_row([f"{y_pos:.3f}", f"{W_pos:.6f}"])
            table.add_row([f"{y_neg:.3f}", f"{W_neg:.6f}"])

        print("\nЗначення кривої безумовної густини W(y):")
        print(table)


def run_optimization_comparison(self):
    print("\n--- 3. Порівняння методів оптимізації ---")

    target_x = self.X_observations[1]
    target_r = self.R_values[0]

    analytical_y_opt = self.get_conditional_mean(target_x, target_r)
    print(f"Аналітична оптимальна оцінка Y* = {analytical_y_opt:.10f}")

    objective_function = lambda y: -self.bivariate_pdf(target_x, y, target_r)

    def objective_gradient(y):
        h = 1e-6
        y_val = y[0] if isinstance(y, (list, np.ndarray)) else y
        grad = (objective_function(y_val + h) - objective_function(y_val - h)) / (2 * h)
        return np.array([grad])

    y_start = self.mean_y
    search_bounds = (self.mean_y - 5 * self.std_y, self.mean_y + 5 * self.std_y)

    res_bounded = minimize_scalar(
        objective_function, bounds=search_bounds, method="bounded"
    )
    res_newton = minimize(
        objective_function, x0=[y_start], method="Newton-CG", jac=objective_gradient
    )
    res_powell = minimize(objective_function, x0=y_start, method="Powell")

    methods_results = {
        "Інтервальний (bounded)": res_bounded.x,
        "Ньютон-CG (jac)": res_newton.x[0],
        "Powell": res_powell.x.item(),
    }

    table = PrettyTable()
    table.field_names = [
        "Метод",
        "y_opt (чисельний)",
        "Абс. похибка",
        "Відн. похибка (%)",
    ]

    for method_name, y_numerical in methods_results.items():
        abs_e, rel_e = self._calculate_error(y_numerical, analytical_y_opt)
        table.add_row(
            [method_name, f"{y_numerical:.10f}", f"{abs_e:.10f}", f"{rel_e:.8f}"]
        )

    print("\nОцінка точності методів оптимізації:")
    print(table)


def run_conditional_density_analysis(self):
    print("\n--- 4. Аналіз та візуалізація умовних густин W(y|x_j) ---")

    table = PrettyTable()
    table.field_names = ["X_j", "R", "Y", "W(Y|X_j)"]

    plt.figure(figsize=(12, 7))

    plot_styles = [
        {"color": "orange", "linestyle": "-"},
        {"color": "orange", "linestyle": "--"},
        {"color": "green", "linestyle": "-"},
        {"color": "green", "linestyle": "--"},
        {"color": "red", "linestyle": "-"},
        {"color": "red", "linestyle": "--"},
        {"color": "purple", "linestyle": "-"},
        {"color": "purple", "linestyle": "--"},
    ]
    style_index = 0

    for i, x_val in enumerate(self.X_observations):
        for j, r_val in enumerate(self.R_values):
            cond_mean = self.get_conditional_mean(x_val, r_val)
            cond_var = self.get_conditional_variance(r_val)
            cond_std = np.sqrt(cond_var)

            for k in self.k_factors:
                for sign in [-1, 1]:
                    y_point = cond_mean + sign * k * cond_std
                    w_val = self.univariate_pdf(y_point, cond_mean, cond_var)
                    table.add_row(
                        [
                            f"{x_val:.2f}",
                            f"{r_val:.2f}",
                            f"{y_point:.3f}",
                            f"{w_val:.6f}",
                        ]
                    )

            y_plot_range = np.linspace(
                cond_mean - 4 * cond_std, cond_mean + 4 * cond_std, 50
            )
            w_plot_values = [
                self.univariate_pdf(y, cond_mean, cond_var) for y in y_plot_range
            ]

            label = f"W(y|X{i + 1}={x_val}, R{j + 1}={r_val})"
            style = plot_styles[style_index]
            plt.plot(y_plot_range, w_plot_values, label=label, **style, linewidth=1.5)
            style_index += 1

    print("\nЗначення умовної щільності W(y|x_j):")
    print(table)

    y_base_range = np.linspace(
        self.mean_y - 4 * self.std_y, self.mean_y + 4 * self.std_y, 50
    )
    w_base_values = [
        self.univariate_pdf(y, self.mean_y, self.var_y) for y in y_base_range
    ]

    plt.plot(
        y_base_range,
        w_base_values,
        label="Безумовна W(y)",
        color="blue",
        linestyle=":",
        marker="x",
        markersize=4,
    )
    plt.title("Графіки умовних W(y|x_j) та безумовної W(y) густин")
    plt.xlabel("Значення параметра y")
    plt.ylabel("Густина ймовірності W(...)")
    plt.grid(True)
    plt.legend(fontsize="small", loc="upper right")
    plt.tight_layout()
    plt.show()


def main():
    # Вихідні параметри розподілу
    base_parameters = {"mean_x": 10.0, "mean_y": 20.0, "var_x": 0.6, "var_y": 0.8}

    # Створюємо екземпляр класу
    analyzer = BivariateNormalAnalysis(**base_parameters)

    # Виконуємо всі частини аналізу
    analyzer.run_error_variance_analysis()
    analyzer.run_unconditional_density_table()
    analyzer.run_optimization_comparison()
    analyzer.run_conditional_density_analysis()


if __name__ == "main":
    main()
