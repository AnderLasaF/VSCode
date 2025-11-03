import pytest
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for tests
import matplotlib.pyplot as plt
from src.sinusoid_generation import generate_signal, generate_fft, plot_time_domain, plot_freq_domain

@pytest.mark.parametrize("frequency,sampling_rate,amplitude,duration,phase,oversampling_original", [
    (10, 1000,1,1,0,20),
    (50, 2000,1,1,0,20),
    (100, 5000,1,1,0,20)
])
def test_fft_has_single_component(frequency, sampling_rate,amplitude,duration,phase,oversampling_original):
    # Check that a right sampling_rate has been chosen
    assert sampling_rate/frequency >= oversampling_original, \
        f"Sampling frequency {sampling_rate} is <{oversampling_original} times bigger than the original frequency {frequency}"
    # Generate signal
    signal, signal_original, t, t_original = generate_signal(sampling_rate, amplitude, frequency, duration, phase, oversampling_original)

    # Compute FFT for the sampled signal
    fft_values, freqs = generate_fft(signal, sampling_rate)

    # Compute FFT for the original signal
    fft_values_original, freqs_original = generate_fft(signal_original, frequency*oversampling_original)

    # ---- Plotting using original functions ----
    plot_time_domain(signal, signal_original, t, t_original, frequency, phase)  # Pass frequency and phase
    plot_freq_domain(freqs, freqs_original, fft_values, fft_values_original, signal, signal_original)

    # Save plot in the test folder
    output_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(output_dir, exist_ok=True)
    filename = f"signal_fft_f{frequency}_fs{sampling_rate}.png"
    plt.savefig(os.path.join(output_dir, filename))
    # ---- End Plotting ----
    
    # Compute magnitudes
    magnitudes = np.abs(fft_values)

    # Consider only positive frequencies: sin(2pift) contains two complex exponential members. One of them contains negative freqs
    half = len(magnitudes) // 2
    magnitudes = magnitudes[:half]

    # Define threshold (e.g., 1% of max)
    threshold = max(magnitudes) * 0.01

    # Count significant components
    significant_components = np.sum(magnitudes > threshold)

    # Assert only one significant component
    assert significant_components == 1, \
        f"Expected 1 component in frequency greater than {threshold}, found {significant_components}"
    