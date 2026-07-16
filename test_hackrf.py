from src.hackrf_interface import VirtualHackRF

radio = VirtualHackRF()

print(radio.info())

for i in range(5):

    freq = radio.hop()

    print(

        "Hop",

        i+1,

        round(freq/1e6,2),

        "MHz"

    )