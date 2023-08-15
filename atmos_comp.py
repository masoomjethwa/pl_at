import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def atmospheric_composition(planet):
    """
    This function displays the atmospheric composition of the given planet.

    Args:
      planet: The name of the planet.

    Returns:
      None.
    """
    # Get the atmospheric composition data for the planet.
    gas_concentrations, gas_labels = get_atmospheric_composition_data(planet)

    # Plot the atmospheric composition.
    altitude_km = gas_concentrations[:, 0]  # Altitude in kilometers
    gas_concentrations = gas_concentrations[:, 1:]  # Remove altitude column
    for i in range(len(gas_labels)):
        plt.plot(altitude_km, gas_concentrations[:, i], label=gas_labels[i])
    plt.xlabel("Altitude (km)")
    plt.ylabel("Gas Concentration (mol/mol)")
    plt.legend()
    plt.title(f"Atmospheric Composition of {planet}")
    plt.show()

def get_atmospheric_composition_data(planet):
    """
    This function gets the atmospheric composition data for the given planet.

    Args:
      planet: The name of the planet.

    Returns:
      A tuple of NumPy arrays containing the gas concentrations and gas labels for
      the planet.
    """
    # Simulate fetching data from NASA database or any other source
    # For demonstration purposes, let's use mock data
    gas_concentrations = np.random.rand(10, 8)  # 10 altitudes, 8 gases
    gas_labels = ["Gas 1", "Gas 2", "Gas 3", "Gas 4", "Gas 5", "Gas 6", "Gas 7", "Gas 8"]

    return gas_concentrations, gas_labels

if __name__ == "__main__":
    # Display the atmospheric composition of each planet.
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        atmospheric_composition(planet)
