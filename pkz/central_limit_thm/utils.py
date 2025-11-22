from typing import Callable
from typing import Dict
from typing import List
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def get_sample_mean(
    sampler: Callable,
    params: Dict,
    n_samples: int,
) -> float:
    """
    Sample data from a cetrain distribution and find its mean.

    Args:
        sampler (Callable): distribution to sample some data.
        params (Dict): dictionary containing all parameters of a specific distribution.
        n_samples (int): sampling size.

    Returns:
        mean of the sampled data.
    """
    samples = sampler(size=n_samples, **params)
    sample_mean = samples.mean()
    return sample_mean

def plot_histogram(samples_of_mean: List[float]) -> Figure:
    """
    Plot a histogram of samples of mean.

    Args:
        samples_of_mean (List): list of samples of the mean.

    Returns:
        a histogram of the mean.
    """
    fig, ax = plt.subplots()
    ax.hist(
        samples_of_mean, 
        bins="auto", 
        color="#EC5A53", 
        edgecolor="black",
    )
    ax.set_title("Distribution of the sample mean")
    return fig
