from src.signal_generator import SignalGenerator

generator = SignalGenerator()

spectrum = generator.generate()

print("Spectrum Size :", len(spectrum))
print("Maximum Power :", max(spectrum))
print("Minimum Power :", min(spectrum))