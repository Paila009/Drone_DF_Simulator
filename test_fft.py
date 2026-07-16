from src.signal_generator import SignalGenerator
from src.fft_processor import FFTProcessor

generator = SignalGenerator()

processor = FFTProcessor()

signal = generator.generate()

fft = processor.process(signal)

print("FFT Length :", len(fft))
print("Maximum FFT :", max(fft))
print("Minimum FFT :", min(fft))