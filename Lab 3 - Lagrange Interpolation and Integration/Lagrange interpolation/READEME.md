# Lagrange Interpolation in Python

This repository contains a simple implementation of **Lagrange Polynomial Interpolation** using Python, NumPy, and Matplotlib. 

The script fits a polynomial through a given set of data points $(x, y)$, calculates the interpolated value at a specific target point ($x_p = 5$), and plots the resulting polynomial curve alongside the original data points.

## Features
- **Custom Interpolation Function**: Implements the mathematical formula for Lagrange Interpolation from scratch using nested loops.
- **Data Validation**: Checks that the input arrays are of equal length and contain at least two data points.
- **Visualization**: Generates a clean plot showing the original data points, the interpolated point, and the continuous polynomial curve.

## Mathematical Overview
Lagrange interpolation finds a polynomial $P(x)$ of degree $n-1$ that passes through $n$ distinct points $(x_i, y_i)$. The polynomial is defined as:

$$P(x) = \sum_{i=1}^{n} y_i \cdot L_i(x)$$

where $L_i(x)$ represents the Lagrange basis polynomials:

$$L_i(x) = \prod_{j=1, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

## Requirements
To run this script, you need Python installed along with the following packages:
- `numpy`
- `matplotlib`

You can install the dependencies via pip:
```bash
pip install numpy matplotlib


## Sample Output

![Sample Output](sample%20output.png)

---

## Visualization

The graph displays:

- Green dots → Original data points
- Black curve → Lagrange interpolation polynomial
- Red cross → Interpolated value at `x = 5`

---

## Project Structure

```text
.
├── lagrange_interpolation.py
├── sample output.png
└── README.md
```

---

## Features

- Pure implementation of Lagrange interpolation
- Works with any valid dataset containing at least two points
- Automatic plotting using Matplotlib
- Interpolated value visualization
- Easy to modify for different datasets

---

## Author

Created using Python, NumPy, and Matplotlib for numerical analysis and interpolation visualization.
