from src.core.virtual_receiver import VirtualReceiver

rx = VirtualReceiver()

rx.set_signal("drone")

signal = rx.receive()

print(signal)

print()

print("Samples :", len(signal))

print("Mean :", signal.mean())

print("Std :", signal.std())