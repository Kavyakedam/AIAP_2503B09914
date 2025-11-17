# Fibonacci Number Calculator - Documentation

## Overview

This program calculates the nth Fibonacci number using a recursive approach. The Fibonacci sequence is one of the most famous sequences in mathematics, where each number is the sum of the two preceding ones.

## Fibonacci Sequence Definition

The Fibonacci sequence is defined as:
- **F(0) = 0**
- **F(1) = 1**
- **F(n) = F(n-1) + F(n-2)** for n > 1

### Sequence Example
```
n:   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  ...
F(n): 0  1  1  2  3  5  8  13 21 34 55  89  144 233 377 610 ...
```

## Code Structure

### 1. `fibonacci_recursive(n)`

**Purpose:** Calculate the nth Fibonacci number using basic recursion.

**How it works:**
1. **Base Cases:** 
   - If `n == 0`, return `0`
   - If `n == 1`, return `1`
   
2. **Recursive Case:**
   - For `n > 1`, return `fibonacci_recursive(n-1) + fibonacci_recursive(n-2)`
   - This breaks down the problem into smaller subproblems until reaching base cases

**Example Execution for F(5):**
```
F(5) = F(4) + F(3)
     = [F(3) + F(2)] + [F(2) + F(1)]
     = [[F(2) + F(1)] + [F(1) + F(0)]] + [[F(1) + F(0)] + 1]
     = [[[F(1) + F(0)] + 1] + [1 + 0]] + [[1 + 0] + 1]
     = [[[1 + 0] + 1] + [1 + 0]] + [[1 + 0] + 1]
     = [[1 + 1] + 1] + [1 + 1]
     = [2 + 1] + 2
     = 3 + 2
     = 5
```

**Time Complexity:** O(2^n) - Exponential
- Each call generates two more calls
- Many values are recalculated multiple times

**Space Complexity:** O(n) - Linear
- Maximum depth of recursion stack is n

**Limitations:**
- Very slow for large values of n (e.g., n > 35)
- May hit Python's recursion limit for very large n

---

### 2. `fibonacci_memoized(n, memo=None)`

**Purpose:** Calculate the nth Fibonacci number using recursion with memoization (optimization).

**How it works:**
1. Uses the same base cases as the basic recursive function
2. **Memoization:** Stores previously calculated Fibonacci numbers in a dictionary
3. Before calculating, checks if the value already exists in the memo dictionary
4. If found, returns the stored value (avoids redundant calculations)
5. If not found, calculates recursively and stores the result

**Example Execution for F(5) with Memoization:**
```
F(5) = F(4) + F(3)        [memo: {}]
     = [F(3) + F(2)] + F(3)  [memo: {}]
     = [F(3) + F(2)] + F(3)  [memo: {2: 1}]
     = [F(3) + 1] + F(3)     [memo: {2: 1}]
     = [F(2) + F(1)] + 1 + F(3)  [memo: {2: 1}]
     = [1 + 1] + 1 + F(3)    [memo: {2: 1, 3: 2}]
     = 2 + 1 + 2             [memo: {2: 1, 3: 2, 4: 3}]
     = 5                     [memo: {2: 1, 3: 2, 4: 3, 5: 5}]
```

**Time Complexity:** O(n) - Linear
- Each Fibonacci number from 0 to n is calculated exactly once

**Space Complexity:** O(n) - Linear
- For the memo dictionary and recursion stack

**Advantages:**
- Much faster than basic recursion
- Can handle larger values of n efficiently

---

## Usage

### Running the Program

```bash
python task3.py
```

This will execute the `main()` function, which demonstrates both approaches with various test cases.

### Using as a Module

```python
from task3 import fibonacci_recursive, fibonacci_memoized

# Calculate F(10) using basic recursion
result1 = fibonacci_recursive(10)
print(f"F(10) = {result1}")  # Output: F(10) = 55

# Calculate F(30) using memoized recursion (faster)
result2 = fibonacci_memoized(30)
print(f"F(30) = {result2}")  # Output: F(30) = 832040
```

## Code Explanation

### Key Concepts

1. **Recursion:**
   - A function that calls itself
   - Must have base cases to prevent infinite recursion
   - Breaks complex problems into simpler subproblems

2. **Base Cases:**
   - The simplest instances of the problem that can be solved directly
   - For Fibonacci: F(0) = 0 and F(1) = 1
   - Without base cases, recursion would continue infinitely

3. **Recursive Case:**
   - The part where the function calls itself with modified parameters
   - For Fibonacci: F(n) = F(n-1) + F(n-2)
   - Each recursive call moves closer to the base cases

4. **Memoization:**
   - An optimization technique that stores results of expensive function calls
   - When the same inputs occur again, returns the cached result
   - Dramatically improves performance for recursive functions with overlapping subproblems

### Code Flow

```
User calls fibonacci_recursive(5)
    ↓
Check: n == 0? No
    ↓
Check: n == 1? No
    ↓
Check: n < 0? No
    ↓
Return fibonacci_recursive(4) + fibonacci_recursive(3)
    ↓
    ├─→ fibonacci_recursive(4)
    │       ├─→ fibonacci_recursive(3) + fibonacci_recursive(2)
    │       │       ├─→ fibonacci_recursive(2) + fibonacci_recursive(1)
    │       │       │       ├─→ fibonacci_recursive(1) + fibonacci_recursive(0)
    │       │       │       │       ├─→ Returns 1 (base case)
    │       │       │       │       └─→ Returns 0 (base case)
    │       │       │       └─→ Returns 1 + 0 = 1
    │       │       └─→ Returns 1 (base case)
    │       │       └─→ Returns 1 + 1 = 2
    │       └─→ fibonacci_recursive(2) = 1
    │       └─→ Returns 2 + 1 = 3
    │
    └─→ fibonacci_recursive(3) = 2 (already calculated above)
    ↓
Returns 3 + 2 = 5
```

## Performance Comparison

| n | Basic Recursive | Memoized Recursive |
|---|----------------|-------------------|
| 10 | ~0.0001s | ~0.0001s |
| 20 | ~0.01s | ~0.0001s |
| 30 | ~1s | ~0.0001s |
| 35 | ~10s | ~0.0001s |
| 40 | ~100s+ | ~0.0001s |

*Note: Times are approximate and may vary based on system*

## Error Handling

The code includes input validation:
- **Negative numbers:** Raises `ValueError` with a descriptive message
- **Large numbers:** May raise `RecursionError` if exceeding Python's recursion limit (typically ~1000)

## Best Practices Demonstrated

1. **Documentation:** Comprehensive docstrings following Google/NumPy style
2. **Comments:** Inline comments explaining each section
3. **Error Handling:** Input validation for edge cases
4. **Code Organization:** Clear separation of concerns
5. **Examples:** Included in docstrings and main function
6. **Optimization:** Provided both basic and optimized versions

## Alternative Approaches

While recursion is elegant, other approaches exist:

1. **Iterative Approach:** Uses a loop instead of recursion
   - Time: O(n), Space: O(1)
   - No recursion limit issues

2. **Matrix Exponentiation:** Mathematical approach
   - Time: O(log n), Space: O(1)
   - Most efficient for very large n

3. **Binet's Formula:** Direct mathematical formula
   - Time: O(1), Space: O(1)
   - May have precision issues for large n

## Conclusion

This implementation demonstrates:
- ✅ Recursive problem-solving
- ✅ Base case handling
- ✅ Code optimization with memoization
- ✅ Comprehensive documentation
- ✅ Error handling
- ✅ Practical examples

The recursive approach is excellent for learning and understanding the Fibonacci sequence, while the memoized version provides a practical, efficient solution.



