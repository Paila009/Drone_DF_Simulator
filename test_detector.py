from src.core.detector import AIDetector

detector = AIDetector()

print("=" * 60)

for signal in [

    "noise",

    "wifi",

    "bluetooth",

    "drone"

]:

    result = detector.detect(signal)

    print()

    print("Signal :", signal)

    print("Prediction :", result["prediction"])

    print("Confidence :", round(result["confidence"] * 100, 2), "%")