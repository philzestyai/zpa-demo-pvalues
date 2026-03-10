from dataclasses import dataclass

import numpy as np


@dataclass
class TestResult:
    """Result of a statistical test on A/B data."""

    test_name: str
    effect_name: str
    effect_size: float
    statistic_name: str
    statistic: float
    p_value: float
    alpha: float

    def __repr__(self) -> str:
        return (
            f"{self.test_name} test: {self.effect_name} = {self.effect_size:.4f}, "
            f"{self.statistic_name} = {self.statistic:.4f}, p-value = {self.p_value:.4g}, "
            f"alpha = {self.alpha:.2f}, significant = {self.p_value < self.alpha}"
        )


@dataclass
class SimulationResult:
    """Result of a single simulation run, including the test result and observed effect."""

    p_values: np.ndarray
    observed_effects: np.ndarray
