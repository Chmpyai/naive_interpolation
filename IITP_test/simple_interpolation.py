import matplotlib.pyplot as plt


def sim_sim_interpolate(donor_values, donor_coords, target_coords):

    interpolated_values = []
    for target_x in target_coords:

        lower_index = 0
        while lower_index < len(donor_coords) - 1 and donor_coords[lower_index + 1] < target_x:
            lower_index += 1

        upper_index = lower_index + 1

        # Boundary points
        if target_x < donor_coords[0]:
            interpolated_values.append(donor_values[0])
            continue
        if target_x > donor_coords[-1]:
            interpolated_values.append(donor_values[-1])
            continue

        x1, x2 = donor_coords[lower_index], donor_coords[upper_index]
        y1, y2 = donor_values[lower_index], donor_values[upper_index]

        interpolated_y = y1 + (target_x - x1) * (y2 - y1) / (x2 - x1)
        interpolated_values.append(interpolated_y)

    return interpolated_values


# Test

X_c = [1, 2, 3, 4, 7, 9]
X_v = [10, 20, 30, 40, 50, 60]
Y_c = [1.5, 2.5, 3.5, 5.5, 8]

Y_v = sim_sim_interpolate(X_v, X_c, Y_c)

plt.figure(figsize=(8, 5))
plt.scatter(X_c, X_v, color='blue', label='Donor points (X_c, X_v)', marker='o')
plt.plot(X_c, X_v, linestyle='dashed', color='blue', alpha=0.5)
plt.scatter(Y_c, Y_v, color='red', label='Target points (Y_c, Y_v)', marker='x')
plt.xlabel('Coordinates')
plt.ylabel('Values')
plt.title('Linear interpolation')
plt.legend()
plt.grid(True)

plt.show()