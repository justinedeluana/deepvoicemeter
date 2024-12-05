import numpy as np

class VoiceAnalyzer:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

    def analyze_frequency(self, data):
        fft_data = np.fft.fft(data)
        frequencies = np.fft.fftfreq(len(fft_data), 1/self.sample_rate)
        magnitudes = np.abs(fft_data)
        peak_index = np.argmax(magnitudes)
        peak_frequency = abs(frequencies[peak_index])

        return peak_frequency

    def is_deep_voice(self, frequency, threshold=150):
        return frequency < threshold
