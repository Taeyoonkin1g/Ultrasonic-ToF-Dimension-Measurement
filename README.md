# Ultrasonic Time-of-Flight (ToF) Dimension Measurement System

> Raspberry Pi-based embedded system for real-time object dimension measurement using ultrasonic Time-of-Flight (ToF) sensors.

![Project](images/setup.jpg)

---

# Overview

This project was developed during the **Creative Embedded System Education Program (2020)** at Gyeongsang National University.

The objective was to build a real-time embedded measurement system capable of estimating the width and height of an object using multiple ultrasonic sensors based on the **Time-of-Flight (ToF)** principle.

The system was implemented using **Python** on a **Raspberry Pi**, with multiple HC-SR04 ultrasonic sensors, an LCD display, and external circuitry for data acquisition and visualization.

---

# Objectives

- Design a real-time embedded measurement system
- Learn Raspberry Pi hardware interfacing
- Apply ultrasonic Time-of-Flight distance measurement
- Display measurement results on an LCD module
- Improve calibration accuracy through repeated testing

---

# Hardware

| Component | Description |
|-----------|-------------|
| Raspberry Pi | Main Controller |
| HC-SR04 ×4 | Ultrasonic Distance Sensors |
| 16×2 LCD | Measurement Display |
| Breadboard | Circuit Prototyping |
| Jumper Wires | Hardware Connections |
| Power Supply | Embedded System Power |

---

# Software

- Python
- Raspberry Pi GPIO
- LCD Control
- Ultrasonic Sensor Interface

---

# Measurement Principle

The system measures the propagation time of ultrasonic pulses.

1. Trigger ultrasonic pulse
2. Receive echo signal
3. Calculate distance using Time-of-Flight
4. Estimate object dimensions
5. Display results on LCD

The project combines multiple ultrasonic sensors to estimate object width and height in real time.

---

# System Architecture

```
Ultrasonic Sensors
        │
        ▼
 Raspberry Pi
        │
Python Measurement Program
        │
Distance Calculation
        │
Dimension Estimation
        │
LCD Display
```

---

# Gallery

## Prototype

![Prototype](images/prototype.jpg)

---

## Hardware Setup

![Hardware](images/hardware.jpg)

---

## Measurement System

![Measurement](images/measurement.jpg)

---

## Experimental Environment

![Experiment](images/experiment.jpg)

---

## Award

The project received the **Encouragement Award (Bronze Prize)** in the Creative Embedded System Competition.

![Award](images/award.jpg)

---

# Skills Demonstrated

- Embedded System Development
- Raspberry Pi Programming
- Python Programming
- Sensor Interfacing
- Hardware Debugging
- Embedded System Integration
- Real-time Measurement
- Time-of-Flight (ToF)
- Hardware Calibration
- Problem Solving

---

# Lessons Learned

Through this project, I gained practical experience in integrating embedded hardware and software.

The project strengthened my understanding of:

- Sensor interfacing
- Embedded Python programming
- Hardware debugging
- Measurement calibration
- Real-time data acquisition
- System integration

It also provided valuable hands-on experience in building a complete embedded system from hardware assembly to software implementation.

---

# Repository Note

This repository is intended as a portfolio summarizing the project experience.

The original educational source code has not been preserved.

Only project documentation and photographs are provided.

---
