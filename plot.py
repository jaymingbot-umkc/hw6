
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file = '/home/zhimbot/ros2_ws/src/unmanned_systems_ros2_pkg/unmanned_systems_ros2_pkg/log/Nov_17_17_12.csv'
data = pd.read_csv(csv_file)

# Extract columns
time = data['time'].to_numpy()
x_position = data['x'].to_numpy()
y_position = data['y'].to_numpy()
evader_x = data['evader_x'].to_numpy()
evader_y = data['evader_y'].to_numpy()

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Data of x vs y')

# Subplot 1: X Position vs. Time
axs[0, 0].plot(x_position, y_position)
axs[0, 0].set_title('pursuer x vs y')
axs[0, 0].set_xlabel('X position')
axs[0, 0].set_ylabel('Y Position')

# Subplot 2: Y Position vs. Time
axs[0, 1].plot(evader_x, evader_y)
axs[0, 1].set_title('evader x vs y')
axs[0, 1].set_xlabel('X position')
axs[0, 1].set_ylabel('Y Position')

# Subplot 3: Velocity vs. Time
axs[1, 0].plot(x_position, y_position)
axs[1, 0].plot(evader_x, evader_y)
axs[1, 0].set_title('both together')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Velocity')

#Subplot 4: Angular Velocity vs. Time
axs[1, 1].plot(time, x_position)
axs[1, 1].set_title('time used')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('x_position of pursuer')

# Adjust layout for better visualization
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plots
plt.show()

