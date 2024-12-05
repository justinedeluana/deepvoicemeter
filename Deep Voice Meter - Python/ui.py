import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class DeepVoiceMeterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deep Voice Meter")
        self.frequency_label = tk.Label(root, text="Frequency: 0 Hz", font=("Arial", 16))
        self.frequency_label.pack(pady=10)
        self.voice_type_label = tk.Label(root, text="Voice Type: Normal", font=("Arial", 16))
        self.voice_type_label.pack(pady=10)
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim(0, 500)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Frequency (Hz)')
        self.line, = self.ax.plot([], [])
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
        self.data_points = []

    def update_frequency(self, frequency):
        self.frequency_label.config(text=f"Frequency: {frequency:.2f} Hz")
        self.data_points.append(frequency)
        if len(self.data_points) > 50:
            self.data_points.pop(0)
        self.line.set_ydata(self.data_points)
        self.line.set_xdata(range(len(self.data_points)))
        self.ax.set_xlim(0, len(self.data_points))
        self.canvas.draw()

    def update_voice_type(self, is_deep_voice):
        if is_deep_voice:
            self.voice_type_label.config(text="Voice Type: Deep", fg="green")
        else:
            self.voice_type_label.config(text="Voice Type: Normal", fg="black")
