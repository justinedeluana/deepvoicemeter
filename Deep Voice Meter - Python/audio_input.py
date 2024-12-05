import pyaudio
import numpy as np

class AudioInput:
    def __init__(self, rate=44100, chunk=1024):
        self.rate = rate
        self.chunk = chunk
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_stream(self):
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)
    
    def read_chunk(self):
        data = self.stream.read(self.chunk, exception_on_overflow=False)
        return np.frombuffer(data, dtype=np.int16)
    
    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def terminate(self):
        self.audio.terminate()
