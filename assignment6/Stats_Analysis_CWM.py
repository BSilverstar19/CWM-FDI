import numpy as np

import os

os.chdir("/Users/bensilvesterratcliffe/Documents/Coding/CWM_Wk3")
print(os.getcwd())
# Path to your data file
filename = "time_c_pinned.txt"

# Create an empty list to store the numbers
data = []

# Open the file
with open(filename, "r") as f:

    # Read each line in the file
    for line in f:

        # Remove spaces and newline characters
        cleaned_line = line.strip()

        # Ignore blank lines
        if cleaned_line != "":

            # Convert text to a number
            value = float(cleaned_line)

            # Add the number to our list
            data.append(value)

# Convert the Python list into a NumPy array
data = np.array(data)

# Calculate statistics
minimum_value = np.min(data)
first_percentile = np.percentile(data, 1)
tenth_percentile = np.percentile(data, 10)
mean_value = np.mean(data)
median_value = np.median(data)
ninetieth_percentile = np.percentile(data, 90)
ninety_ninth_percentile = np.percentile(data, 99)
maximum_value = np.max(data)

# Display results
print()
print("Statistics")
print("----------")
print("Minimum value      =", minimum_value)
print("1st percentile     =", first_percentile)
print("10th percentile    =", tenth_percentile)
print("Mean               =", mean_value)
print("Median             =", median_value)
print("90th percentile    =", ninetieth_percentile)
print("99th percentile    =", ninety_ninth_percentile)
print("Maximum value      =", maximum_value)