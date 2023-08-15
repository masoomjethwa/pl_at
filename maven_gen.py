import numpy as np
import matplotlib.pyplot as plt

def read_maven_data(filename):
  """
  This function reads the data from the given NASA MAVEN file.

  Args:
    filename: The name of the NASA MAVEN file.

  Returns:
    A NumPy array containing the data from the file.
  """

  # Read the data from the file.
  with open(filename, "r") as f:
    data = f.readlines()

  # Convert the data to a NumPy array.
  data = np.array([float(line.strip()) for line in data])

  # Return the data.
  return data

def plot_maven_data(data):
  """
  This function plots the data from the given NASA MAVEN file.

  Args:
    data: The data from the NASA MAVEN file.

  Returns:
    None.
  """

  # Plot the data.
  plt.plot(data)
  plt.xlabel("Time (seconds)")
  plt.ylabel("Data")
  plt.show()

if __name__ == "__main__":
  # Read the data from the file.
  data = read_maven_data("maven_data.txt")

  # Plot the data.
  plot_maven_data(data)
