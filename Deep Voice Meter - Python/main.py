import tkinter as tk
from audio_input import AudioInput
from voice_analyzer import VoiceAnalyzer
from ui import DeepVoiceMeterUI
import threading
import time

class DeepVoiceMeterApp:
    def __init__(self, root):
        self.ui = DeepVoiceMeterUI(root)
        self.rate = 44100
        self.chunk = 1024
        self.audio_input = AudioInput(rate=self.rate, chunk=self.chunk)
        self.voice_analyzer = VoiceAnalyzer(sample_rate=self.rate)
        self.audio_input.start_stream()
        self.running = True
        self.thread = threading.Thread(target=self.update_audio)
        self.thread.start()

    def update_audio(self):
        while self.running:
            data = self.audio_input.read_chunk()
            frequency = self.voice_analyzer.analyze_frequency(data)
            self.ui.update_frequency(frequency)
            is_deep_voice = self.voice_analyzer.is_deep_voice(frequency)
            self.ui.update_voice_type(is_deep_voice)
            time.sleep(0.1)

    def stop(self):
        self.running = False
        self.audio_input.stop_stream()
        self.audio_input.terminate()
        self.thread.join()


root = tk.Tk()
app = DeepVoiceMeterApp(root)
def on_closing():
    app.stop()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

