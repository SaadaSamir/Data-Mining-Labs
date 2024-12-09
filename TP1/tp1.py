import pandas as pd

def load_dataset(file_path):
    """
    Load the dataset from the specified file path.
    Handles decimal formatting issues and missing values.
    """
    try:
        # Attempt to read the dataset with the specified options
        data = pd.read_csv(file_path, 
                           delimiter=';',  # Use semicolon as delimiter
                           decimal='.',  # Use dot for decimal points
                           na_values=['NaN', 'NA', '', ' '],  # Specify NaN values
                           on_bad_lines='warn',  # Warn about bad lines
                           low_memory=False)  # Avoid Dtype warning
        
        # Convert relevant columns to numeric
        numeric_columns = ['Acc_x', 'Acc_y', 'Acc_z', 'Gyro_x', 'Gyro_y', 'Gyro_z', 'Set']
        for column in numeric_columns:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def display_basic_info(data):
    """Display basic information about the dataset."""
    print("Basic Info:")
    print(data.info())
    print("\nFirst 5 Rows:")
    print(data.head())

def calculate_central_tendencies(data, attribute):
    """Calculate and display the central tendencies for the specified attribute manually."""
    if attribute in data.columns:
        # Get the values for the attribute and drop NaN values
        values = data[attribute].dropna().values
        
        # Mean
        total_sum = sum(values)
        count = len(values)
        mean = total_sum / count if count > 0 else None
        
        # Median
        sorted_values = sorted(values)
        mid_index = count // 2
        
        if count % 2 == 0:  # even number of elements
            median = (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
        else:  # odd number of elements
            median = sorted_values[mid_index]
        
        # Mode
        frequency = {}
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        
        max_count = max(frequency.values())
        mode = [key for key, value in frequency.items() if value == max_count]
        mode = mode[0] if len(mode) == 1 else mode  # Handle multiple modes or no mode
        
        print(f"Central Tendencies for {attribute}:")
        print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
    else:
        print(f"Attribute '{attribute}' not found in the dataset.")


def calculate_quartiles(data, attribute):
    """Calculate and display the quartiles (Q0, Q1, Q2, Q3, Q4) for the specified attribute manually."""
    if attribute in data.columns:
        values = data[attribute].dropna().values
        sorted_values = sorted(values)
        count = len(sorted_values)
        
        q0 = sorted_values[0]  # Minimum
        q1 = sorted_values[int(count * 0.25)]  # First quartile
        q2 = sorted_values[int(count * 0.5)]  # Median (second quartile)
        q3 = sorted_values[int(count * 0.75)]  # Third quartile
        q4 = sorted_values[-1]  # Maximum
        
        quartiles = {
            0: q0,
            1: q1,
            2: q2,
            3: q3,
            4: q4
        }
        
        print(f"Quartiles for {attribute}: {quartiles}")
    else:
        print(f"Attribute '{attribute}' not found in the dataset.")


def display_missing_values(data, attribute):
    """Display the number and percentage of missing values for the specified attribute."""
    if attribute in data.columns:
        missing_count = data[attribute].isnull().sum()
        missing_percentage = (missing_count / len(data)) * 100
        print(f"Missing Values for {attribute}: Count = {missing_count}, Percentage = {missing_percentage:.2f}%")
    else:
        print(f"Attribute '{attribute}' not found in the dataset.")

def display_unique_values(data, attribute):
    """Display the number of unique values for the specified attribute."""
    if attribute in data.columns:
        unique_values = data[attribute].nunique()
        print(f"Unique Values for {attribute}: {unique_values}")
    else:
        print(f"Attribute '{attribute}' not found in the dataset.")

def main():
    """Main function to execute the data analysis."""
    file_path = 'DatasetExos.csv'
    data = load_dataset(file_path)
    
    if data is not None:
        display_basic_info(data)
        
        # Example usage of functions
        calculate_central_tendencies(data, 'Acc_x')
        calculate_quartiles(data, 'Acc_x')
        display_missing_values(data, 'Acc_x')
        display_unique_values(data, 'ID')

if __name__ == "__main__":
    main()
