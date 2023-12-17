import numpy as np
from scipy.optimize import minimize


def loss_function(params, x_values, y_values):
    a, b, c, d = params
    predicted_y_values = a * np.exp(b * x_values) + c * np.exp(d * x_values)
    residuals = y_values - predicted_y_values
    return np.sum(residuals ** 2)  # Minimizing the quadratic error


# Known value of x
x_values = np.array(0.05)

# Known y values
y_values = np.array([0.428, 0.431, 0.431, 0.428, 0.435, 0.428])

# Initial conditions for parameters a, b, c, d
initial_guess = [1.0, 1.0, 1.0, 1.0]

# Customize the parameters using minimize
result = minimize(loss_function, initial_guess, args=(x_values, y_values))

a_fit, b_fit, c_fit, d_fit = result.x

print("Fitted parameters (a, b, c, d):", a_fit, b_fit, c_fit, d_fit)
