from typing import Optional

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.container import BarContainer

from zpa_demo.types import SimulationResult


def plot_conversion_rates(df: pd.DataFrame) -> None:
    """Plot the conversion rates for control and treatment groups.

    Args:
        df: DataFrame containing 'group' and 'converted' columns.
    """

    _, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x="group", y="converted", data=df, ax=ax)
    bar_container = ax.containers[0]
    if isinstance(bar_container, BarContainer):
        ax.bar_label(bar_container, fmt="{:.1%}", padding=4)
    ax.set_title("Conversion Rates by Group")
    ax.set_ylabel("Conversion Rate")
    ax.set_xlabel("Group")
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.show()

    return None


def plot_simulation_results(
    results: SimulationResult, lift: float, alpha: float
) -> None:
    """Plot simulation results.

    Args:
        results: SimulationResult containing p-values and observed effects from multiple runs.
        lift: True effect size (lift) used in the simulation.
        alpha: Significance level for hypothesis testing.
    """

    _, axes = plt.subplots(1, 2, figsize=(15, 5))

    # observed effects
    ax = axes[0]
    ax.hist(
        results.observed_effects,
        bins=50,
        color="#3498db",
        alpha=0.7,
        edgecolor="black",
    )
    ax.set_xlabel("Observed effect size", fontsize=12, fontweight="bold")
    ax.set_ylabel("Count", fontsize=12, fontweight="bold")
    ax.set_title(
        f"Distribution of Observed Effect Sizes Under Null Hypothesis (true lift = {lift})",
        fontsize=13,
        fontweight="bold",
    )
    ax.axvline(
        lift,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"True effect size (lift = {lift})",
    )
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    # histogram of p-values
    ax = axes[1]
    ax.hist(results.p_values, bins=100, color="#9b59b6", alpha=0.7, edgecolor="black")
    ax.set_xlabel("P-value", fontsize=12, fontweight="bold")
    ax.set_ylabel("Count", fontsize=12, fontweight="bold")
    ax.set_title(
        f"Distribution of P-values Under Null Hypothesis (true lift = {lift})",
        fontsize=13,
        fontweight="bold",
    )
    ax.axvline(
        alpha,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"alpha = {alpha}",
    )
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return None


def plot_p_value_histogram(
    results: SimulationResult,
    alpha: float,
    title: Optional[str] = None,
    base_color: str = "#9b59b6",
    below_alpha_color: str = "#e74c3c",
) -> None:
    # Calculate the number and percentage of p-values below alpha
    n_below_alpha = (results.p_values < alpha).sum()
    percent_below_alpha = n_below_alpha / len(results.p_values) * 100

    # histogram of p-values
    _, ax = plt.subplots(figsize=(8, 4))
    counts, bins, patches = ax.hist(
        results.p_values, bins=100, color=base_color, alpha=0.7, edgecolor="black"
    )

    # Color the tail red
    for i, patch in enumerate(patches):  # type: ignore
        if bins[i] < alpha:
            patch.set_facecolor(below_alpha_color)

    ax.set_xlabel("P-value", fontsize=12, fontweight="bold")
    ax.set_ylabel("Count", fontsize=12, fontweight="bold")
    ax.set_title(
        (
            title
            if title is not None
            else "Distribution of P-values Under Null Hypothesis (true lift = 0)"
        ),
        fontsize=13,
        fontweight="bold",
    )
    ax.axvline(
        alpha,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"alpha = {alpha}",
    )
    ax.annotate(
        f"{n_below_alpha} experiments\n({percent_below_alpha:.1f}%)",
        xy=(0.02, counts.max() * 0.8),  # type: ignore
        fontsize=12,
        fontweight="bold",
        bbox=dict(
            boxstyle="round", facecolor=below_alpha_color, alpha=0.8, edgecolor="black"
        ),
        color="white",
    )

    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return None
