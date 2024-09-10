import numpy as np
import matplotlib.pyplot as plt

# Generate values for x
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # 1000 points between -2π and 2π

# Compute the cosine of x
y = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='cos(x)', color='blue')

# Add titles and labels
plt.title('Graph of cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()