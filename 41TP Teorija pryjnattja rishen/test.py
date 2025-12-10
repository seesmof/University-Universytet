import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable as PT

VARIANT = 19
NUM_INTERVALS = 15
OUTPUT_FILENAME = "classification_analysis.txt"


def get_raw_data():
    x_values = [
        2.5,
        3.8,
        3.8,
        3.8,
        6.3,
        6.3,
        4.6,
        8.6,
        4.6,
        7.7,
        6.5,
        10.2,
        4.6,
        8.4,
        8.5,
        8.4,
        3.7,
        8.5,
        5.5,
        4.3,
        11.1,
        5.3,
        5.5,
        10.1,
        5.7,
        4.9,
        10.3,
        7.9,
        2.7,
        2.3,
        6.5,
        5.7,
        4.7,
        8.5,
        5.5,
        4.6,
        8.8,
        8.5,
        5.8,
        7.6,
        3.7,
        6.5,
        6.7,
        11.3,
        10.3,
        6.3,
        8.6,
        13,
        10.2,
        12,
        5.7,
        10.3,
        5.5,
        3.4,
        7.9,
        4.9,
        10.3,
        4.6,
        8.4,
        8.5,
    ]
    y_values = [
        0.07,
        0.07,
        0.09,
        0.15,
        0.15,
        0.18,
        0.10,
        0.28,
        0.15,
        0.23,
        0.22,
        0.27,
        0.18,
        0.26,
        0.27,
        0.18,
        0.05,
        0.28,
        0.10,
        0.08,
        0.30,
        0.08,
        0.15,
        0.24,
        0.15,
        0.17,
        0.27,
        0.24,
        0.06,
        0.05,
        0.17,
        0.31,
        0.20,
        0.22,
        0.11,
        0.11,
        0.30,
        0.27,
        0.16,
        0.22,
        0.04,
        0.17,
        0.18,
        0.31,
        0.29,
        0.16,
        0.31,
        0.34,
        0.26,
        0.35,
        0.17,
        0.30,
        0.10,
        0.03,
        0.24,
        0.18,
        0.28,
        0.09,
        0.27,
        0.29,
    ]
    return x_values, y_values


def preprocess_data(x_raw, y_raw, multiplier):
    x_data = np.array([round(x * multiplier, 2) for x in x_raw])
    y_data = np.array(y_raw)

    y_mean_threshold = y_data.mean()
    actual_classes = np.where(y_data <= y_mean_threshold, "K1", "K2")

    class_counts = {
        "K1": np.sum(actual_classes == "K1"),
        "K2": np.sum(actual_classes == "K2"),
    }

    print(f"Середнє значення α (поріг для Y) = {y_mean_threshold:.3f}")
    return x_data, y_data, actual_classes, y_mean_threshold, class_counts


def evaluate_thresholds(x_data, actual_classes, class_counts, num_intervals):
    threshold_range = np.linspace(x_data.min(), x_data.max(), num_intervals)
    all_metrics = []
    total_samples = len(x_data)
    actual_k1_count = class_counts["K1"]
    actual_k2_count = class_counts["K2"]

    best_accuracy = -1.0
    best_threshold_value = None

    for t in threshold_range:
        predicted = np.where(x_data <= t, "K1", "K2")

        metrics = {"threshold": t}

        metrics["n_pred_k1_actual_k1"] = np.sum(
            (predicted == "K1") & (actual_classes == "K1")
        )
        metrics["n_pred_k1_actual_k2"] = np.sum(
            (predicted == "K1") & (actual_classes == "K2")
        )
        metrics["n_pred_k2_actual_k1"] = np.sum(
            (predicted == "K2") & (actual_classes == "K1")
        )
        metrics["n_pred_k2_actual_k2"] = np.sum(
            (predicted == "K2") & (actual_classes == "K2")
        )

        metrics["n_decision_k1"] = (
            metrics["n_pred_k1_actual_k1"] + metrics["n_pred_k1_actual_k2"]
        )
        metrics["n_decision_k2"] = (
            metrics["n_pred_k2_actual_k1"] + metrics["n_pred_k2_actual_k2"]
        )

        metrics["p_correct"] = (
            metrics["n_pred_k1_actual_k1"] + metrics["n_pred_k2_actual_k2"]
        ) / total_samples
        metrics["p_error"] = (
            metrics["n_pred_k1_actual_k2"] + metrics["n_pred_k2_actual_k1"]
        ) / total_samples

        metrics["p_k1_given_dec_k2"] = (
            (metrics["n_pred_k2_actual_k1"] / metrics["n_decision_k2"])
            if metrics["n_decision_k2"] > 0
            else 0
        )
        metrics["p_k2_given_dec_k1"] = (
            (metrics["n_pred_k1_actual_k2"] / metrics["n_decision_k1"])
            if metrics["n_decision_k1"] > 0
            else 0
        )

        metrics["p_dec_k1_given_k2"] = (
            (metrics["n_pred_k1_actual_k2"] / actual_k2_count)
            if actual_k2_count > 0
            else 0
        )
        metrics["p_dec_k2_given_k1"] = (
            (metrics["n_pred_k2_actual_k1"] / actual_k1_count)
            if actual_k1_count > 0
            else 0
        )

        metrics["p_decision_k1"] = metrics["n_decision_k1"] / total_samples
        metrics["p_decision_k2"] = metrics["n_decision_k2"] / total_samples

        all_metrics.append(metrics)

        if metrics["p_correct"] > best_accuracy:
            best_accuracy = metrics["p_correct"]
            best_threshold_value = t

    print(
        f"Оптимальний поріг: {best_threshold_value:.2f}, точність: {best_accuracy:.2f}"
    )
    return all_metrics, best_threshold_value, threshold_range


def build_results_table(metrics_list, thresholds):
    metric_display_names = {
        "n_decision_k1": "n(ріш K1)",
        "n_decision_k2": "n(ріш K2)",
        "n_pred_k1_actual_k2": "n(ріш K1/K2)",
        "n_pred_k2_actual_k1": "n(ріш K2/K1)",
        "n_pred_k1_actual_k1": "n(ріш K1/K1)",
        "n_pred_k2_actual_k2": "n(ріш K2/K2)",
        "p_correct": "P(прав)",
        "p_error": "P(пом)",
        "p_k1_given_dec_k2": "P(К1/ріш K2)",
        "p_k2_given_dec_k1": "P(К2/ріш K1)",
        "p_dec_k1_given_k2": "P(ріш K1/К2)",
        "p_dec_k2_given_k1": "P(ріш K2/К1)",
        "p_decision_k1": "P(ріш K1)",
        "p_decision_k2": "P(ріш K2)",
    }

    table = PT()
    header_labels = [f"{t:.2f}" for t in thresholds]
    table.field_names = ["Метрика"] + header_labels

    for key, display_name in metric_display_names.items():
        row_data = [round(m[key], 3) for m in metrics_list]
        table.add_row([display_name] + row_data)

    return table


def visualize_results(x, y, y_mean, best_t, metrics_data, threshold_labels):
    fig, (ax_scatter, ax_probs) = plt.subplots(1, 2, figsize=(13, 6))

    ax_scatter.axvline(
        x=best_t, color="red", linestyle="--", label=f"Опт. поріг X ({best_t:.2f})"
    )
    ax_scatter.axhline(
        y=y_mean, color="green", linestyle="--", label=f"Поріг Y ({y_mean:.3f})"
    )
    ax_scatter.scatter(x, y, color="blue", alpha=0.7, edgecolors="black")
    ax_scatter.set_title("Кореляція X та Y з порогами")
    ax_scatter.set_xlabel("Шумова напруга (X)")
    ax_scatter.set_ylabel("КоефіціFєнт старіння (Y)")
    ax_scatter.grid(True)
    ax_scatter.legend()

    p_errors = [m["p_error"] for m in metrics_data]
    p_k1_given_dec_k2 = [m["p_k1_given_dec_k2"] for m in metrics_data]
    p_k2_given_dec_k1 = [m["p_k2_given_dec_k1"] for m in metrics_data]
    x_tick_labels = [f"{t:.2f}" for t in threshold_labels]

    ax_probs.plot(
        x_tick_labels,
        p_errors,
        color="blue",
        marker="o",
        linestyle="-",
        label="P(пом) - Загальна",
    )
    ax_probs.plot(
        x_tick_labels,
        p_k1_given_dec_k2,
        color="green",
        marker="s",
        linestyle="--",
        label="P(К1/ріш K2)",
    )
    ax_probs.plot(
        x_tick_labels,
        p_k2_given_dec_k1,
        color="red",
        marker="^",
        linestyle=":",
        label="P(К2/ріш K1)",
    )

    ax_probs.set_xlabel("Порогові значення (X)")
    ax_probs.set_ylabel("Ймовірності")
    ax_probs.set_title("Розподіл ймовірностей помилок")
    ax_probs.grid(True)
    ax_probs.legend()

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def main():
    x_raw, y_raw = get_raw_data()

    x_data, y_data, actual_cls, y_mean, counts = preprocess_data(x_raw, y_raw, VARIANT)

    all_metrics, best_thresh, thresholds = evaluate_thresholds(
        x_data, actual_cls, counts, NUM_INTERVALS
    )

    results_table = build_results_table(all_metrics, thresholds)

    if NUM_INTERVALS > 10:
        try:
            with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
                f.write(results_table.get_string())
            print(f"Таблицю результатів збережено у файл: {OUTPUT_FILENAME}")
        except Exception as e:
            print(f"Не вдалося зберегти таблицю: {e}")
    else:
        print(results_table)

    visualize_results(x_data, y_data, y_mean, best_thresh, all_metrics, thresholds)


if __name__ == "main":
    main()
