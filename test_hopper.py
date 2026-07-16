from src.frequency_hopper import FrequencyHopper

hopper = FrequencyHopper()

for i in range(10):

    freq = hopper.next_frequency()

    print(
        f"Hop {i+1}: "
        f"{hopper.get_frequency_mhz():.2f} MHz "
        f"({hopper.get_band()})"
    )