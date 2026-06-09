
# Newton's Forward and Backward Interpolation in Python

This repository contains a Python implementation of **Newton's Forward and Backward Interpolation** methods. These techniques are used to approximate the value of a dependent variable $y$ for a given independent variable $x$ from a set of equally spaced data points.

---

## Features
* **Forward Interpolation:** Optimized for approximating values near the **beginning** of the data set.
* **Backward Interpolation:** Optimized for approximating values near the **end** of the data set.
* **Difference Tables:** Automatically calculates and prints the respective forward and backward difference matrices.

---

## Getting Started

### Prerequisites
You only need standard Python 3.x installed. No external libraries (like NumPy or SciPy) are required.

### Code Structure & Usage

The script is split into two independent blocks: the first block runs the **Backward** method, and the second runs the **Forward** method.

To adapt the script for your own dataset or target values, locate and modify the following variables in the code:

```python
# 1. Define your data points (Ensure x-values are equally spaced)
x = [0, 1, 2, 3, 4] 
y = [-9, -8, 11, 66, 175] 

# 2. Set the target x-value you want to interpolate
xval = 3.6  # For Backward Interpolation (near the end)
xval = 0.7  # For Forward Interpolation (near the start)
