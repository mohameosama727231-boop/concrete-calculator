# Concrete Quantity Calculator 🏗️

## Overview
The **Concrete Quantity Calculator** is a command-line Python application designed for civil engineering estimation. It computes the wet concrete volume for critical structural elements (Beams, Columns, Slabs, and Footings) and accurately breaks down the required raw materials: **Cement, Sand, and Aggregate**.

## Engineering Background & Purpose
In real-world construction and site engineering, estimating material quantities accurately is vital for budgeting, reducing waste, and preventing structural failures. Dry materials (cement, sand, and aggregate) contain air voids. When mixed with water, these voids shrink, meaning the dry volume of materials required is significantly larger than the final wet concrete volume. 
This tool applies standard industry quantity take-off practices—specifically utilizing the **1.54 dry volume factor** and standard structural mix ratios (M15, M20, M25)—to bridge practical civil engineering methodologies with software automation.

## Features
* Supports 4 major structural elements with custom dimensional inputs.
* Implements standard concrete mix ratios:
  * **M15 (1:2:4)** for general use and footings.
  * **M20 (1:1.5:3)** for beams, columns, and slabs.
  * **M25 (1:1:2)** for heavy-duty structural work.
* Robust error handling to reject zero, negative, or non-numeric inputs without crashing.
* Automated unit testing suite using `pytest`.

## How to Run the Application
1. Ensure you have Python installed.
2. Run the main script:
   ```bash
   python main.py
