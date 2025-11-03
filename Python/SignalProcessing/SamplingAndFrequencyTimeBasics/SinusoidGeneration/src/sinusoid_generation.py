import numpy as np
import matplotlib.pyplot as plt

def generate_signal(sampling_rate, amplitude, frequency, duration, phase, oversampling_original):
    # Number of samples
    N = int(sampling_rate*duration)
    N_original = int(oversampling_original*frequency*duration)

    # Time vector
    t = np.linspace(0, duration, N, endpoint=False)
    t_original = np.linspace(0,duration, N_original, endpoint=False)

    # Generate sinusoid with phase
    signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    signal_original = amplitude * np.sin(2 * np.pi * frequency * t_original + phase)

    return signal, signal_original ,t, t_original

def generate_fft(signal,sampling_rate):
    # Compute FFT (discrete)
    fft_vals = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
    return fft_vals,fft_freqs

def plot_time_domain(signal,signal_original,t,t_original,f,phi):
    # Plot time-domain signal
    plt.figure(figsize=(10, 6))
    plt.subplot(4, 1, 1)
    plt.plot(t_original, signal_original)
    plt.title(f'Time Domain (original): Sinusoid (f={f} Hz, phase={phi} rad)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.subplot(4, 1, 2)
    plt.plot(t,signal)
    plt.title(f'Time Domain (sampled): Sinusoid (f={f} Hz, phase={phi} rad)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

def plot_freq_domain(fft_freqs, fft_freqs_original, fft_vals, fft_vals_original, signal, signal_original):
    # Plot frequency-domain magnitude
    plt.subplot(4, 1, 3)
    plt.stem(fft_freqs_original[:len(fft_freqs_original)//2], np.abs(fft_vals_original[:len(fft_vals_original)//2]) / len(signal_original))
    plt.title('Frequency Domain (original): FFT')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.subplot(4, 1, 4)
    plt.stem(fft_freqs[:len(fft_freqs)//2], np.abs(fft_vals[:len(fft_vals)//2]) / len(signal))
    plt.title('Frequency Domain (sampled): FFT')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.tight_layout()

def main():
    # Parameters
    sampling_rate = 1000          # Sampling frequency (Hz) Original 1000
    duration = 1              # Duration (seconds)
    frequency = 50             # Frequency of sinusoid (Hz)
    amplitude = 1              # Amplitude
    phase = 0            # Phase (radians)
    oversampling_original = 4
    
    # Your existing logic here
    print("Generating a signal with the following attributes:"
    " frequency: ",frequency, " amplitude: ", amplitude, " phase: ", phase, " and duration: ",duration)
    signal, signal_original, t, t_original = generate_signal(sampling_rate, amplitude, frequency, duration, phase, oversampling_original)
    fft_vals, fft_freqs = generate_fft(signal,sampling_rate)
    plot_time_domain(signal,signal_original,t,t_original,frequency,phase)
    plot_freq_domain(fft_freqs, fft_vals, signal)
    print("Sampling the original signal with a sampling frequency of :",sampling_rate)

if __name__ == "__main__":
    main()