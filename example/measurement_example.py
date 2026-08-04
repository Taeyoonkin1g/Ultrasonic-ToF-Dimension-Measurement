"""
Example implementation for the Ultrasonic ToF Dimension Measurement project.

This file is NOT the original competition source code.
It is a simplified example created to demonstrate the basic
measurement concept of the project.
"""

import time


class UltrasonicSensor:

    def measure_distance(self):
        """
        Example distance measurement (cm)
        """
        return 25.4


def calculate_dimension(distance):
    """
    Example dimension calculation.
    """
    return round(distance, 2)


def main():

    sensor = UltrasonicSensor()

    while True:

        distance = sensor.measure_distance()

        dimension = calculate_dimension(distance)

        print(f"Measured Distance : {distance:.2f} cm")
        print(f"Estimated Dimension : {dimension:.2f} cm")

        time.sleep(1)


if __name__ == "__main__":
    main()
