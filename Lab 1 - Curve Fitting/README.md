# Numerical Method Lab Work: Curve Fitting in Python

This repository contains Python implementations of data-driven curve fitting techniques using the **Method of Least Squares**. These scripts take a set of discrete data points and find the best-fit curves for **Linear**, **Exponential**, and **Power** relationships, plotting the results using `matplotlib`.

---

## 📈 Covered Curve Fitting Models

### 1. Linear Curve Fitting
Fits data to the standard straight-line equation:
$$y = a + bx$$
* **Best used for:** Data showing a constant rate of change.

### 2. Exponential Curve Fitting
Fits data to the exponential growth/decay equation:
$$y = a e^{bx}$$
* **Process:** Linearized using natural logarithms: $\ln(y) = \ln(a) + bx$.
* **Best used for:** Rapidly accelerating or decaying data (e.g., population growth, radioactive decay).

### 3. Power Curve Fitting
Fits data to a power equation:
$$y = a x^b$$
* **Process:** Linearized using log-log transformation: $\ln(y) = \ln(a) + b\ln(x)$.
* **Best used for:** Physics laws or relationships scaling geometrically.

---

## 🚀 Getting Started (For Beginners)

If you are new to running Python scripts locally, follow these steps to get everything running on your machine.

### Prerequisites
Make sure you have Python installed on your system. You will also need two external packages:
* **NumPy:** Used for fast mathematical matrix/array calculations.
* **Matplotlib:** Used to generate visual graphs.

You can install both dependencies at once via your terminal or command prompt by running:
```bash
pip install numpy matplotlib
