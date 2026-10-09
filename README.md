
# Triangle Classifier

CSC 325 - Module 6 Assignment

## Description
This Python program classifies triangles as Invalid, Equilateral, Isosceles, or Scalene. It also identifies right triangles using math.isclose() to account for floating-point calculations.

## How to Run Tests
Install pytest:

    python3 -m pip install -r requirements.txt

Run all tests:

    python3 -m pytest -v

## Equivalence Classes
- Invalid: zero or negative side
- Invalid: triangle inequality fails
- Equilateral: three equal sides
- Isosceles: exactly two equal sides
- Scalene: three different sides
- Right triangle: satisfies the Pythagorean theorem

## Boundaries
- Zero-length side
- Negative side
- Degenerate triangle: (1, 2, 3)
- Triangle inequality boundary: (2, 3, 4), (2, 3, 5), (2, 3, 6)
- Non-integer right triangle: (5, 5, 5 * sqrt(2))

## Why an Equilateral Triangle Cannot Be Right
All three angles in an equilateral triangle are 60 degrees. A right triangle must have a 90-degree angle, so an equilateral triangle cannot be right.

## Copilot Review Log

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| test_equilateral | Yes | Kept | Matches the specification for three equal sides |
| test_invalid_triangle | Yes | Kept | Checks zero, negative, and degenerate cases |
| test_isosceles | Yes | Kept | Checks exactly two equal sides |
| test_scalene | Yes | Kept | Checks scalene and right-scalene cases |
| test_right_triangle_non_integer | Yes | Kept | Checks right-angle classification using non-integer inputs |
| test_right_isosceles_non_integer | Yes | Kept | Tests a floating-point right isosceles triangle |
| test_triangle_inequality_boundary | Yes | Edited | Copilot suggested repetitive degenerate cases. I replaced them with before-boundary, at-boundary, and beyond-boundary tests |

## Customer Acceptance Criteria
1. For input (3, 4, 5), the system returns "Right Scalene" to identify a piece requiring reinforced corners.
2. For input (1, 2, 3), the system returns "Invalid" without crashing.
3. For input (5, 5, 5), the system returns "Equilateral".

## Testing Results
All 8 tests passed using pytest.

## AI-Use Disclosure
GitHub Copilot autocomplete was used to suggest unit tests. Suggestions were reviewed against the specification, and the triangle inequality boundary test was edited to improve coverage.

ChatGPT was used to help develop the triangle implementation, review the unit tests, and provide the acceptance criteria and acceptance test example. The program was executed locally and all eight tests passed.
