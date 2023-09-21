import numpy as np
import matplotlib.pyplot as plt

# Generate normally distributed data
data = np.random.normal(size=(8, 8))

# Create a heatmap
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='coolwarm')

# Add a colorbar
cbar = ax.figure.colorbar(im, ax=ax)

# Add labels and title
ax.set_xticks(np.arange(8))
ax.set_yticks(np.arange(8))
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
ax.set_yticklabels(['1', '2', '3', '4', '5', '6', '7', '8' ])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Normal Distribution Heatmap')


# Rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')


# Display the plot
plt.show()
