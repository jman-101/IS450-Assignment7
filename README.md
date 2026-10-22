# IS450-Assignment7: Make a GitHub Commit

## Project Information
* **Project Name:** Wolf Pack Café Order Calculator
* **Student Name:** Joe Camarillo
* **GitHub Username:** jman-101

## Program Description
`myProgram.py` is a console-based transaction processor for a café. It stores menu items and pricing inside a dictionary, accepts user selections in a dynamic loop, computes order subtotal, conditionally calculates bulk discounts, applies sales tax, and prints an itemized receipt.

## Course Concepts Demonstrated
1. **Functions:** Modular design with `display_menu()`, `calculate_discount()`, and `process_order()`.
2. **Dictionaries & Loops:** Key-value traversal of menu items and prices using `.items()`.
3. **Conditionals:** Threshold checks to determine order eligibility for bulk discounts.
4. **Data Aggregation & Lists:** Tracking user choices in a list and summing prices via generator expressions.
5. **Formatted Output:** F-strings displaying aligned columns and monetary values rounded to two decimal places.

## Input & Output
* **Input Accepted:** Item names typed as text strings by the user, followed by the keyword `done`.
* **Output Produced:** Formatted console display of the café menu, immediate feedback confirming added items, and a structured final receipt showing subtotal, discount, tax, and final amount.

## How to Run the Program
1. Open a terminal or command prompt inside the project directory.
2. Run the script using Python 3:
   ```bash
   python myProgram.py