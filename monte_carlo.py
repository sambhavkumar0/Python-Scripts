import random
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

def plot_points_in_circle(num_samples):
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    plt.scatter(x_inside, y_inside, color='blue', marker='.')
    plt.scatter(x_outside, y_outside, color='red', marker='.')
    plt.title(f'Monte Carlo Simulation: {num_samples} Samples')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

num_samples = 10000
pi_estimate = estimate_pi(num_samples)
print(f"Estimated value of pi using {num_samples} samples: {pi_estimate}")

plot_points_in_circle(num_samples)
