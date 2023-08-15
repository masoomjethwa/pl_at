import numpy as np
import matplotlib.pyplot as plt

def planetary_atmosphere(R, M, T, g, p0, z0):
  """
  This function models the atmosphere of a planet with radius R, mass M,
  temperature T, gravity g, surface pressure p0, and surface altitude z0.

  Args:
    R: The radius of the planet (in meters).
    M: The mass of the planet (in kg).
    T: The temperature of the planet (in Kelvin).
    g: The gravity of the planet (in m/s^2).
    p0: The surface pressure of the planet (in Pa).
    z0: The surface altitude of the planet (in meters).

  Returns:
    A NumPy array containing the pressure, temperature, and density of the
    atmosphere as a function of altitude.
  """

  # Initialize the pressure, temperature, and density arrays.
  p = np.zeros(z0 + 1)
  T = np.zeros(z0 + 1)
  rho = np.zeros(z0 + 1)

  # Set the initial conditions.
  p[0] = p0
  T[0] = T
  rho[0] = rho0

  # Loop over the altitudes.
  for i in range(1, z0 + 1):
    # Calculate the pressure at this altitude.
    p[i] = p[i - 1] * np.exp(-g * (i - z0) / R / T[i - 1])

    # Calculate the temperature at this altitude.
    T[i] = T[i - 1] * (p[i] / p[i - 1]) ** (R / g)

    # Calculate the density at this altitude.
    rho[i] = p[i] / (R * T[i])

  return p, T, rho

if __name__ == "__main__":
  # Set the planetary parameters.
  R = 6371000  # meters
  M = 5.972e24  # kg
  T = 288  # Kelvin
  g = 9.807  # m/s^2
  p0 = 101325  # Pa
  z0 = 0  # meters

  # Calculate the pressure, temperature, and density of the atmosphere.
  p, T, rho = planetary_atmosphere(R, M, T, g, p0, z0)

  # Plot the pressure, temperature, and density of the atmosphere.
  plt.plot(p, T, label="Pressure")
  plt.plot(p, rho, label="Density")
  plt.xlabel("Pressure (Pa)")
  plt.ylabel("Temperature (Kelvin)")
  plt.legend()
  plt.show()
