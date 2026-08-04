"""
Example implementation for the Ultrasonic ToF Dimension Measurement project.

This file is NOT the original competition source code.
It is a simple reference implementation demonstrating
the basic measurement concept.
"""

import time

def measure_distance():
    # Example distance value (cm)
    distance = 25.4
    return distance

while True:
    d = measure_distance()
    print(f"Measured Distance : {d:.2f} cm")
    time.sleep(1)
