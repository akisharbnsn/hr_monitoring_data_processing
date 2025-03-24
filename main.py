"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from pathlib import Path 
from typing import Tuple
from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    
    file_path = Path(filename) # Putting the filename in the Path package
    file_name = file_path.stem # Using Path package to extract the file name
    
    data: list = [] #empty list to store each line from "filename" (.txt file)

    # open file using file I/O and read it into the `data` list
    with open(filename, "r") as file: # Loading the "filename" as file (.txt file)
        for line in file: # For each "line" in the ".txt" file
            data.append(line) # Storing the data into the "data" list

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    filtered_data = filter_nondigits(data)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    indices = list(range(1, len(filtered_data) + 1)) # Labeling the index positions of the "filtered_data" list
    
    # Heart rate line plot
    fig, ax = plt.subplots()
    ax.plot(indices, filtered_data, marker='o', linestyle='-', color='b')
    ax.set_xlabel("Index")
    ax.set_ylabel("Heart Rate (BPM)")
    ax.set_title("Heart Rate Readings")
    ax.grid(True)
    fig.savefig(f"images/{file_name}_heart_rate_line_plot.png")
    
    # Heart rate histogram
    fig, ax = plt.subplots()
    ax.hist(filtered_data, bins=5, color='blue', edgecolor='black', alpha=0.7)
    ax.set_xlabel("Heart Rate (BPM)")
    ax.set_ylabel("Frequency")
    ax.set_title("Heart Rate Distribution")
    fig.savefig(f"images/{file_name}_heart_rate_histogram.png")
    
    # Heart rate box plot
    fig, ax = plt.subplots()
    ax.boxplot(filtered_data, vert=True, patch_artist=True)
    ax.set_ylabel("Heart Rate (BPM)")
    ax.set_title("Heart Rate Variability")
    fig.savefig(f"images/{file_name}_heart_rate_box_plot.png")
    
    # Heart rate scatter plot
    fig, ax = plt.subplots()
    ax.scatter(indices, filtered_data, color='red', marker='o')
    ax.set_xlabel("Index")
    ax.set_ylabel("Heart Rate (BPM)")
    ax.set_title("Heart Rate Scatter Plot")
    ax.grid(True)
    fig.savefig(f"images/{file_name}_heart_rate_scatter_plot.png")

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(filtered_data)
    max_hr = maximum(filtered_data)
    std_dev_hr = standard_deviation(filtered_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
