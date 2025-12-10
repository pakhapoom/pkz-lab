"""
Streamlit app for visualizing t-distribution vs standard normal distribution.

This app demonstrates how the t-distribution converges to the standard normal
distribution as the degrees of freedom (sample size) increases.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Configure page
st.set_page_config(
    page_title="t-distribution",
    page_icon="📊",
    layout="wide",
)

# Title and description
st.title("Student's t-distribution VS z-distribution")

# Sidebar controls
st.sidebar.header("Distribution Parameters")

# Initialize session state for number of samples
if 'n_samples' not in st.session_state:
    st.session_state.n_samples = 6

# Slider for number of samples (n)
# df = n - 1
# Use the session state value directly in the slider
n = st.sidebar.slider(
    "Number of Samples (n)",
    min_value=2,
    max_value=101,
    value=st.session_state.n_samples,
    step=1,
    help="Number of samples in your data. As sample size increases, the t-distribution approaches the normal distribution."
)

# Only update session state if the slider value changed
# This prevents the slider from overriding button clicks
if n != st.session_state.n_samples:
    st.session_state.n_samples = n

# Calculate degrees of freedom
df = n - 1

# Buttons to increment/decrement number of samples
col1, col2, col3 = st.sidebar.columns([1, 1, 1])

with col1:
    if st.button("➖", use_container_width=True):
        if st.session_state.n_samples > 2:
            st.session_state.n_samples -= 1
            st.rerun()

with col2:
    if st.button("➕", use_container_width=True):
        if st.session_state.n_samples < 101:
            st.session_state.n_samples += 1
            st.rerun()

with col3:
    if st.button("↻", use_container_width=True):
        st.session_state.n_samples = 6
        st.rerun()

# Display corresponding degrees of freedom
st.sidebar.info(f"Degrees of Freedom (df) = {df}")

# Range for x-axis
x_range = st.sidebar.slider(
    "X-axis Range",
    min_value=2.0,
    max_value=6.0,
    value=4.0,
    step=0.5,
    help="Adjust the range of x-values to display"
)

# Number of points for smooth curve
n_points = 1000

# Generate x values
x = np.linspace(-x_range, x_range, n_points)

# Calculate probability densities
normal_pdf = stats.norm.pdf(x, loc=0, scale=1)
t_pdf = stats.t.pdf(x, df=df)

# Calculate metrics across all sample sizes for the subplot
n_range = np.arange(2, 102)  # n from 2 to 101
df_range = n_range - 1

# Calculate variance for each n
variances = []
for df_i in df_range:
    if df_i > 2:
        variances.append(df_i / (df_i - 2))
    else:
        variances.append(np.nan)

# Calculate value at peak for each n
peaks = []
for df_i in df_range:
    t_pdf_i = stats.t.pdf(0, df=df_i)  # PDF at x=0
    normal_peak = stats.norm.pdf(0, loc=0, scale=1)
    peaks.append(abs(t_pdf_i - normal_peak))

# Calculate excess kurtosis for each n
kurtosis = []
for df_i in df_range:
    if df_i > 4:
        kurtosis.append(6 / (df_i - 4))
    else:
        kurtosis.append(np.nan)

# Create the plot with subplots
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 3, height_ratios=[1.2, 1], hspace=0.3, wspace=0.3)

# Main plot (top, spanning all columns)
ax_main = fig.add_subplot(gs[0, :])

# Plot standard normal distribution (reference - in background)
ax_main.plot(x, normal_pdf, 'b-', linewidth=2, label='z-distribution', alpha=0.7)

# Plot t-distribution
ax_main.plot(x, t_pdf, 'r-', linewidth=2.5, label=f't-distribution (df={df})')

# Fill area under t-distribution for better visualization
ax_main.fill_between(x, t_pdf, alpha=0.2, color='red')

# Styling
ax_main.set_xlabel('Value', fontsize=12)
ax_main.set_ylabel('Probability Density', fontsize=12)
ax_main.legend(loc='upper right', fontsize=11)
ax_main.grid(True, alpha=0.3, linestyle='--')
ax_main.set_ylim(0, max(max(normal_pdf), max(t_pdf)) * 1.1)

# Subplot 1: Variance
ax1 = fig.add_subplot(gs[1, 0])
ax1.plot(n_range, variances, 'g-', linewidth=2)
ax1.axhline(y=1, color='b', linestyle='--', linewidth=1, alpha=0.5, label='Normal (σ²=1)')
ax1.axvline(x=n, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Current n={n}')
ax1.scatter([n], [df / (df - 2) if df > 2 else np.nan], color='r', s=100, zorder=5)
ax1.set_xlabel('Sample Size', fontsize=10)
ax1.set_ylabel('Variance', fontsize=10)
ax1.set_title('Variance', fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(fontsize=8)

# Subplot 2: Value at Peak (Difference)
ax2 = fig.add_subplot(gs[1, 1])
ax2.plot(n_range, peaks, 'purple', linewidth=2)
ax2.axvline(x=n, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Current n={n}')
current_peak = abs(t_pdf[n_points//2] - normal_pdf[n_points//2])
ax2.scatter([n], [current_peak], color='r', s=100, zorder=5)
ax2.set_xlabel('Sample Size', fontsize=10)
ax2.set_ylabel('|Difference|', fontsize=10)
ax2.set_title('Difference at Peak', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(fontsize=8)

# Subplot 3: Excess Kurtosis
ax3 = fig.add_subplot(gs[1, 2])
ax3.plot(n_range, kurtosis, 'orange', linewidth=2)
ax3.axhline(y=0, color='b', linestyle='--', linewidth=1, alpha=0.5, label='Normal (κ=0)')
ax3.axvline(x=n, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Current n={n}')
if df > 4:
    current_kurtosis = 6 / (df - 4)
    ax3.scatter([n], [current_kurtosis], color='r', s=100, zorder=5)
ax3.set_xlabel('Sample Size', fontsize=10)
ax3.set_ylabel('Excess Kurtosis', fontsize=10)
ax3.set_title('Excess Kurtosis', fontsize=11, fontweight='bold')
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.legend(fontsize=8)

# Tracking metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Number of Samples",
        value=n,
        help=f"Sample size (n) | df = {df}"
    )

with col2:
    if df > 2:
        t_variance = df / (df - 2)
        t_variance = f"{t_variance:.4f}"
    else:
        t_variance = "Undefined"
    st.metric(
        label="Variance",
        value=t_variance,
        help="Variance of the t-distribution"         
    )

with col3:
    # Calculate the difference at x=0 (peak)
    diff_at_peak = abs(t_pdf[n_points//2] - normal_pdf[n_points//2])
    st.metric(
        label="Difference at Peak",
        value=f"{diff_at_peak:.4f}",
        help="Absolute difference between distributions at x=0"
    )

with col4:
    # Kurtosis of t-distribution (if df > 4)
    if df > 4:
        excess_kurtosis = 6 / (df - 4)
        st.metric(
            label="Excess Kurtosis",
            value=f"{excess_kurtosis:.4f}",
            help="Excess kurtosis of t-distribution (normal has 0)"
        )
    else:
        st.metric(
            label="Excess Kurtosis",
            value="Undefined",
            help="Excess kurtosis is undefined for df ≤ 4"
        )

# Display the plot
st.pyplot(fig)

