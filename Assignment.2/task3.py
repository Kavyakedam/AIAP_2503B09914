"""
Task 3: Python Functions to Calculate Area of Various Shapes
This module demonstrates how to build area calculation functions line by line
with detailed explanations and examples for different geometric shapes.
"""

# ============================================================================
# LINE 1-2: Import necessary modules and define the main module docstring
# ============================================================================
import math
from typing import Union, Dict, Tuple


# ============================================================================
# SECTION 1: BASIC SHAPE AREA CALCULATIONS (Line by Line)
# ============================================================================

# LINE 3-10: Rectangle Area Calculation
# ─────────────────────────────────────────
# A rectangle has:
# - Length (l) and Width (w)
# - Area = length × width
# - Formula: A = l × w

def calculate_rectangle_area(length: float, width: float) -> float:
    """
    LINE 1: Define function with parameters
    - length: float - the length of the rectangle
    - width: float - the width of the rectangle
    
    LINE 2: Return type annotation -> float
    
    LINE 3: Multiply length and width to get area
    """
    # LINE 4: Validate input (defensive programming)
    if length <= 0 or width <= 0:
        # LINE 5: Raise error for invalid dimensions
        raise ValueError("Length and width must be positive numbers")
    
    # LINE 6: Calculate area by multiplying length and width
    area = length * width
    
    # LINE 7: Return the calculated area
    return area


# LINE 11-18: Circle Area Calculation
# ─────────────────────────────────────────
# A circle has:
# - Radius (r)
# - Area = π × r²
# - Formula: A = πr²

def calculate_circle_area(radius: float) -> float:
    """
    LINE 1: Define function with radius parameter
    
    LINE 2: Calculate area of circle
    """
    # LINE 3: Validate radius is positive
    if radius <= 0:
        # LINE 4: Raise error for invalid radius
        raise ValueError("Radius must be a positive number")
    
    # LINE 5: Calculate area using π × r²
    # - Use math.pi for accurate value of π
    # - radius ** 2 means radius squared
    area = math.pi * (radius ** 2)
    
    # LINE 6: Return the calculated area
    return area


# LINE 19-26: Triangle Area Calculation
# ─────────────────────────────────────────
# A triangle has:
# - Base (b) and Height (h)
# - Area = (base × height) / 2
# - Formula: A = (b × h) / 2

def calculate_triangle_area(base: float, height: float) -> float:
    """
    LINE 1: Define function with base and height parameters
    
    LINE 2: Calculate area of triangle
    """
    # LINE 3: Validate inputs are positive
    if base <= 0 or height <= 0:
        # LINE 4: Raise error for invalid dimensions
        raise ValueError("Base and height must be positive numbers")
    
    # LINE 5: Calculate area using (base × height) / 2
    area = (base * height) / 2
    
    # LINE 6: Return the calculated area
    return area


# LINE 27-36: Square Area Calculation
# ─────────────────────────────────────────
# A square has:
# - Side (s) - all sides are equal
# - Area = side²
# - Formula: A = s²

def calculate_square_area(side: float) -> float:
    """
    LINE 1: Define function with side parameter
    
    LINE 2: Calculate area of square
    """
    # LINE 3: Validate side is positive
    if side <= 0:
        # LINE 4: Raise error for invalid side
        raise ValueError("Side length must be a positive number")
    
    # LINE 5: Calculate area using side²
    area = side ** 2
    
    # LINE 6: Return the calculated area
    return area


# LINE 37-50: Ellipse Area Calculation
# ─────────────────────────────────────────
# An ellipse has:
# - Semi-major axis (a) and Semi-minor axis (b)
# - Area = π × a × b
# - Formula: A = πab

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    """
    LINE 1: Define function with two semi-axes parameters
    
    LINE 2: Calculate area of ellipse
    """
    # LINE 3: Validate both axes are positive
    if semi_major <= 0 or semi_minor <= 0:
        # LINE 4: Raise error for invalid axes
        raise ValueError("Semi-major and semi-minor axes must be positive numbers")
    
    # LINE 5: Calculate area using π × a × b
    area = math.pi * semi_major * semi_minor
    
    # LINE 6: Return the calculated area
    return area


# LINE 51-64: Trapezoid Area Calculation
# ─────────────────────────────────────────
# A trapezoid has:
# - Two parallel sides (base1, base2) and height (h)
# - Area = ((base1 + base2) / 2) × height
# - Formula: A = ((b₁ + b₂) / 2) × h

def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    """
    LINE 1: Define function with three parameters
    - base1: first parallel side
    - base2: second parallel side
    - height: perpendicular distance between bases
    
    LINE 2: Calculate area of trapezoid
    """
    # LINE 3: Validate all inputs are positive
    if base1 <= 0 or base2 <= 0 or height <= 0:
        # LINE 4: Raise error for invalid dimensions
        raise ValueError("Bases and height must be positive numbers")
    
    # LINE 5: Calculate average of the two bases
    average_base = (base1 + base2) / 2
    
    # LINE 6: Multiply average base by height
    area = average_base * height
    
    # LINE 7: Return the calculated area
    return area


# LINE 65-78: Polygon Area Calculation (Regular Polygon)
# ─────────────────────────────────────────────────────────
# A regular polygon has:
# - n sides (number of sides)
# - side length (s)
# - Formula: A = (n × s² × cot(π/n)) / 4
# - Where cot(π/n) = 1 / tan(π/n)

def calculate_regular_polygon_area(num_sides: int, side_length: float) -> float:
    """
    LINE 1: Define function with number of sides and side length
    
    LINE 2: Calculate area of regular polygon
    """
    # LINE 3: Validate number of sides (must be at least 3)
    if num_sides < 3:
        # LINE 4: Raise error for invalid polygon
        raise ValueError("Polygon must have at least 3 sides")
    
    # LINE 5: Validate side length is positive
    if side_length <= 0:
        # LINE 6: Raise error for invalid side
        raise ValueError("Side length must be a positive number")
    
    # LINE 7: Calculate angle in radians: π / number of sides
    angle = math.pi / num_sides
    
    # LINE 8: Calculate cotangent: 1 / tan(angle)
    cot_angle = 1 / math.tan(angle)
    
    # LINE 9: Calculate area using formula: (n × s² × cot(π/n)) / 4
    area = (num_sides * (side_length ** 2) * cot_angle) / 4
    
    # LINE 10: Return the calculated area
    return area


# ============================================================================
# SECTION 2: UNIFIED AREA CALCULATOR FUNCTION
# ============================================================================

def calculate_area(shape: str, **kwargs) -> float:
    """
    LINE 1: Define unified function to calculate area of any shape
    
    LINE 2: Parameters:
    - shape: str - name of the shape ('rectangle', 'circle', 'triangle', etc.)
    - **kwargs: variable keyword arguments containing shape dimensions
    
    LINE 3: Returns:
    - float: The calculated area
    
    LINE 4: Usage examples:
    - calculate_area('rectangle', length=5, width=3)
    - calculate_area('circle', radius=4)
    - calculate_area('triangle', base=6, height=4)
    """
    
    # LINE 5: Convert shape name to lowercase for case-insensitive comparison
    shape = shape.lower().strip()
    
    # LINE 6: Use if-elif-else structure to handle different shapes
    
    # LINE 7: If shape is rectangle
    if shape == 'rectangle':
        # LINE 8: Check if required parameters are present
        if 'length' in kwargs and 'width' in kwargs:
            # LINE 9: Call rectangle area function
            return calculate_rectangle_area(kwargs['length'], kwargs['width'])
        else:
            # LINE 10: Raise error if parameters are missing
            raise ValueError("Rectangle requires 'length' and 'width' parameters")
    
    # LINE 11: Elif shape is circle
    elif shape == 'circle':
        # LINE 12: Check if radius parameter is present
        if 'radius' in kwargs:
            # LINE 13: Call circle area function
            return calculate_circle_area(kwargs['radius'])
        else:
            # LINE 14: Raise error if parameter is missing
            raise ValueError("Circle requires 'radius' parameter")
    
    # LINE 15: Elif shape is triangle
    elif shape == 'triangle':
        # LINE 16: Check if base and height parameters are present
        if 'base' in kwargs and 'height' in kwargs:
            # LINE 17: Call triangle area function
            return calculate_triangle_area(kwargs['base'], kwargs['height'])
        else:
            # LINE 18: Raise error if parameters are missing
            raise ValueError("Triangle requires 'base' and 'height' parameters")
    
    # LINE 19: Elif shape is square
    elif shape == 'square':
        # LINE 20: Check if side parameter is present
        if 'side' in kwargs:
            # LINE 21: Call square area function
            return calculate_square_area(kwargs['side'])
        else:
            # LINE 22: Raise error if parameter is missing
            raise ValueError("Square requires 'side' parameter")
    
    # LINE 23: Elif shape is ellipse
    elif shape == 'ellipse':
        # LINE 24: Check if both semi-axes parameters are present
        if 'semi_major' in kwargs and 'semi_minor' in kwargs:
            # LINE 25: Call ellipse area function
            return calculate_ellipse_area(kwargs['semi_major'], kwargs['semi_minor'])
        else:
            # LINE 26: Raise error if parameters are missing
            raise ValueError("Ellipse requires 'semi_major' and 'semi_minor' parameters")
    
    # LINE 27: Elif shape is trapezoid
    elif shape == 'trapezoid':
        # LINE 28: Check if all three parameters are present
        if 'base1' in kwargs and 'base2' in kwargs and 'height' in kwargs:
            # LINE 29: Call trapezoid area function
            return calculate_trapezoid_area(kwargs['base1'], kwargs['base2'], kwargs['height'])
        else:
            # LINE 30: Raise error if parameters are missing
            raise ValueError("Trapezoid requires 'base1', 'base2', and 'height' parameters")
    
    # LINE 31: Elif shape is regular polygon
    elif shape == 'polygon' or shape == 'regular_polygon':
        # LINE 32: Check if required parameters are present
        if 'num_sides' in kwargs and 'side_length' in kwargs:
            # LINE 33: Call polygon area function
            return calculate_regular_polygon_area(kwargs['num_sides'], kwargs['side_length'])
        else:
            # LINE 34: Raise error if parameters are missing
            raise ValueError("Polygon requires 'num_sides' and 'side_length' parameters")
    
    # LINE 35: Else - shape not recognized
    else:
        # LINE 36: Raise error for unknown shape
        raise ValueError(
            f"Unknown shape: {shape}. "
            f"Supported shapes: rectangle, circle, triangle, square, ellipse, trapezoid, polygon"
        )


# ============================================================================
# SECTION 3: DEMONSTRATION AND TEST CASES
# ============================================================================

def print_header(title: str) -> None:
    """LINE 1: Helper function to print formatted headers"""
    # LINE 2: Print title centered with decoration
    print(f"\n{'=' * 70}")
    print(f"{title.center(70)}")
    print(f"{'=' * 70}\n")


def demonstrate_all_shapes() -> None:
    """
    LINE 1: Main demonstration function showing all shape calculations
    """
    
    # LINE 2: Print main header
    print_header("AREA CALCULATION - ALL SHAPES")
    
    # LINE 3: List to store results
    results = []
    
    # LINE 4: Dictionary with shape test cases
    # LINE 5: Each entry contains shape name and parameters
    test_cases = {
        'rectangle': {'length': 5, 'width': 3},
        'circle': {'radius': 4},
        'triangle': {'base': 6, 'height': 4},
        'square': {'side': 5},
        'ellipse': {'semi_major': 5, 'semi_minor': 3},
        'trapezoid': {'base1': 4, 'base2': 6, 'height': 3},
        'polygon': {'num_sides': 6, 'side_length': 4},
    }
    
    # LINE 6: Iterate through each test case
    for shape_name, params in test_cases.items():
        try:
            # LINE 7: Calculate area using unified function
            area = calculate_area(shape_name, **params)
            
            # LINE 8: Format parameters for display
            param_str = ", ".join([f"{k}={v}" for k, v in params.items()])
            
            # LINE 9: Store result
            results.append((shape_name.upper(), param_str, area))
            
            # LINE 10: Print result
            print(f"✓ {shape_name.upper()}")
            print(f"  Parameters: {param_str}")
            print(f"  Area: {area:.4f} square units\n")
        
        # LINE 11: Catch any errors during calculation
        except Exception as e:
            # LINE 12: Print error message
            print(f"✗ Error calculating {shape_name}: {str(e)}\n")
    
    # LINE 13: Print summary table
    print_header("SUMMARY TABLE")
    
    # LINE 14: Print table header
    print(f"{'Shape':<20} {'Parameters':<40} {'Area':<15}")
    print("-" * 75)
    
    # LINE 15: Print each result row
    for shape, params, area in results:
        # LINE 16: Format and print the row
        print(f"{shape:<20} {params:<40} {area:>14.4f}")
    
    # LINE 17: Print footer
    print()


def demonstrate_individual_shapes() -> None:
    """
    LINE 1: Demonstrate each shape calculation individually
    """
    
    # LINE 2: Print main header
    print_header("INDIVIDUAL SHAPE DEMONSTRATIONS")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 3-5: Rectangle Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("1. RECTANGLE AREA CALCULATION")
    print("-" * 70)
    # LINE 6: Define rectangle parameters
    rect_length, rect_width = 5, 3
    # LINE 7: Calculate area
    rect_area = calculate_rectangle_area(rect_length, rect_width)
    # LINE 8: Display formula and result
    print(f"Formula: A = length × width")
    print(f"Parameters: length = {rect_length}, width = {rect_width}")
    print(f"Calculation: {rect_length} × {rect_width} = {rect_area}")
    print(f"Result: {rect_area} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 9-11: Circle Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("2. CIRCLE AREA CALCULATION")
    print("-" * 70)
    # LINE 12: Define circle parameters
    circle_radius = 4
    # LINE 13: Calculate area
    circle_area = calculate_circle_area(circle_radius)
    # LINE 14: Display formula and result
    print(f"Formula: A = π × r²")
    print(f"Parameters: radius = {circle_radius}")
    print(f"Calculation: π × {circle_radius}² = π × {circle_radius**2} = {circle_area:.4f}")
    print(f"Result: {circle_area:.4f} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 15-17: Triangle Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("3. TRIANGLE AREA CALCULATION")
    print("-" * 70)
    # LINE 18: Define triangle parameters
    tri_base, tri_height = 6, 4
    # LINE 19: Calculate area
    tri_area = calculate_triangle_area(tri_base, tri_height)
    # LINE 20: Display formula and result
    print(f"Formula: A = (base × height) / 2")
    print(f"Parameters: base = {tri_base}, height = {tri_height}")
    print(f"Calculation: ({tri_base} × {tri_height}) / 2 = {tri_base * tri_height} / 2 = {tri_area}")
    print(f"Result: {tri_area} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 21-23: Square Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("4. SQUARE AREA CALCULATION")
    print("-" * 70)
    # LINE 24: Define square parameters
    sq_side = 5
    # LINE 25: Calculate area
    sq_area = calculate_square_area(sq_side)
    # LINE 26: Display formula and result
    print(f"Formula: A = side²")
    print(f"Parameters: side = {sq_side}")
    print(f"Calculation: {sq_side}² = {sq_area}")
    print(f"Result: {sq_area} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 27-29: Ellipse Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("5. ELLIPSE AREA CALCULATION")
    print("-" * 70)
    # LINE 30: Define ellipse parameters
    ell_major, ell_minor = 5, 3
    # LINE 31: Calculate area
    ell_area = calculate_ellipse_area(ell_major, ell_minor)
    # LINE 32: Display formula and result
    print(f"Formula: A = π × a × b")
    print(f"Parameters: semi_major = {ell_major}, semi_minor = {ell_minor}")
    print(f"Calculation: π × {ell_major} × {ell_minor} = {ell_area:.4f}")
    print(f"Result: {ell_area:.4f} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 33-35: Trapezoid Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("6. TRAPEZOID AREA CALCULATION")
    print("-" * 70)
    # LINE 36: Define trapezoid parameters
    trap_base1, trap_base2, trap_height = 4, 6, 3
    # LINE 37: Calculate area
    trap_area = calculate_trapezoid_area(trap_base1, trap_base2, trap_height)
    # LINE 38: Display formula and result
    print(f"Formula: A = ((base1 + base2) / 2) × height")
    print(f"Parameters: base1 = {trap_base1}, base2 = {trap_base2}, height = {trap_height}")
    avg = (trap_base1 + trap_base2) / 2
    print(f"Calculation: (({trap_base1} + {trap_base2}) / 2) × {trap_height} = {avg} × {trap_height} = {trap_area}")
    print(f"Result: {trap_area} square units\n")
    
    # ─────────────────────────────────────────────────────────────────
    # LINE 39-41: Regular Polygon Demonstration
    # ─────────────────────────────────────────────────────────────────
    print("7. REGULAR POLYGON (HEXAGON) AREA CALCULATION")
    print("-" * 70)
    # LINE 42: Define polygon parameters
    poly_sides, poly_side_length = 6, 4
    # LINE 43: Calculate area
    poly_area = calculate_regular_polygon_area(poly_sides, poly_side_length)
    # LINE 44: Display formula and result
    print(f"Formula: A = (n × s² × cot(π/n)) / 4")
    print(f"Parameters: num_sides = {poly_sides}, side_length = {poly_side_length}")
    print(f"Calculation: (6 × 4² × cot(π/6)) / 4 = {poly_area:.4f}")
    print(f"Result: {poly_area:.4f} square units\n")


def demonstrate_error_handling() -> None:
    """
    LINE 1: Demonstrate error handling for invalid inputs
    """
    
    # LINE 2: Print main header
    print_header("ERROR HANDLING DEMONSTRATION")
    
    # LINE 3: List of invalid test cases
    invalid_cases = [
        ('rectangle', {'length': -5, 'width': 3}, "Negative dimension"),
        ('circle', {'radius': 0}, "Zero radius"),
        ('triangle', {'base': 5}, "Missing parameter"),
        ('square', {'side': 'abc'}, "Invalid parameter type"),
        ('unknown_shape', {}, "Unknown shape"),
    ]
    
    # LINE 4: Iterate through invalid cases
    for i, (shape, params, description) in enumerate(invalid_cases, 1):
        # LINE 5: Print test case description
        print(f"{i}. {description}")
        print(f"   Shape: {shape}")
        print(f"   Parameters: {params}")
        try:
            # LINE 6: Attempt calculation
            area = calculate_area(shape, **params)
            # LINE 7: This shouldn't be reached
            print(f"   Result: {area}")
        
        # LINE 8: Catch errors
        except (ValueError, TypeError) as e:
            # LINE 9: Print error message
            print(f"   ✓ Error caught: {str(e)}")
        
        # LINE 10: Print separator
    print()


# ============================================================================
# SECTION 4: MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    """
    LINE 1: Main execution block
    """
    
    # LINE 2: Print title
    print("\n" + "=" * 70)
    print("AREA CALCULATION FUNCTIONS - COMPREHENSIVE DEMONSTRATION".center(70))
    print("=" * 70)
    
    # LINE 3: Run individual shape demonstrations
    demonstrate_individual_shapes()
    
    # LINE 4: Run all shapes summary
    demonstrate_all_shapes()
    
    # LINE 5: Run error handling demonstration
    demonstrate_error_handling()
    
    # LINE 6: Print final message
    print_header("DEMONSTRATION COMPLETE")
    print("All area calculation functions executed successfully!")
    print()
