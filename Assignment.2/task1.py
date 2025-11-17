import csv
import os
# Absolute path for the CSV file
csv_path = os.path.join(os.path.dirname(__file__), 'sample.csv')

# Create a CSV file with numeric sample data
with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Age', 'Salary', 'Score'])
    writer.writerow([25, 50000, 85.5])
    writer.writerow([30, 60000, 92.0])
    writer.writerow([22, 45000, 78.5])
    writer.writerow([28, 55000, 88.0])
    writer.writerow([35, 75000, 95.5])

# Read the CSV file and print its contents
with open(csv_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

from typing import Dict, Union
import pandas as pd

def calculate_csv_statistics(file_path: str) -> Dict[str, Dict[str, Union[float, int]]]:
    """
    Reads a CSV file and calculates mean, min, and max for each numeric column.
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV file to read
    
    Returns:
    --------
    Dict[str, Dict[str, Union[float, int]]]
        A dictionary where keys are column names and values are dictionaries 
        containing 'mean', 'min', and 'max' for each numeric column
    
    Example:
    --------
    >>> stats = calculate_csv_statistics('data.csv')
    >>> print(stats)
    {'age': {'mean': 25.5, 'min': 18, 'max': 65},
     'salary': {'mean': 50000.0, 'min': 30000, 'max': 120000}}
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Initialize result dictionary
        statistics = {}
        
        # Calculate statistics for each numeric column
        for column in df.select_dtypes(include=['number']).columns:
            statistics[column] = {
                'mean': df[column].mean(),
                'min': df[column].min(),
                'max': df[column].max()
            }
        
        return statistics
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return {}


def read_and_calculate_statistics():
    """Read the CSV file and return statistics for numeric columns.

    Uses the global `csv_path` by default so no user input is required.
    """
    # Delegate to the pandas-based calculator to avoid manual parsing issues
    return calculate_csv_statistics(csv_path)

def prompt_and_calculate_statistics():
    numbers = [80, 23, 56, 78]
    mean_value = sum(numbers) / len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    print(f"Mean: {mean_value}, Min: {min_value}, Max: {max_value}")

# Example usage
if __name__ == "__main__":
    # Example: Create a sample CSV file for testing
    import os
    
    # Create sample data
    sample_data = """name,age,salary,score
John,25,50000,85.5
Jane,30,60000,92.0
Bob,22,45000,78.5
Alice,28,55000,88.0
Charlie,35,75000,95.5"""
    
    # Write sample data to a file
    sample_file = "sample_data.csv"
    with open(sample_file, 'w') as f:
        f.write(sample_data)
    
    # Calculate statistics
    stats = calculate_csv_statistics(sample_file)
    
    # Display results
    print("CSV Statistics:")
    print("-" * 50)
    for column, values in stats.items():
        print(f"\n{column}:")
        print(f"  Mean: {values['mean']:.2f}")
        print(f"  Min:  {values['min']:.2f}")
        print(f"  Max:  {values['max']:.2f}")
    
    # Clean up sample file
    if os.path.exists(sample_file):
        os.remove(sample_file)

    # Example of using read_and_calculate_statistics (no input required)
    print("\nExample of read_and_calculate_statistics:")
    stats = read_and_calculate_statistics()
    print(stats)

    # Example of using prompt_and_calculate_statistics
    print("\nExample of prompt_and_calculate_statistics:")
    prompt_and_calculate_statistics()
        
    import csv

    # ...existing code... (string-based sample CSV creation removed)
