import numpy as np

def alpha(T):
    p = np.pi

    f = 50

    integrand = lambda t: np.square(2 * p * f * t)

    integral = integrate(integrand, 0, T)

    result = integral

    return result

def integrate(function, a, b):
    integral = 0
    x = a
    h = np.power(10.0, -6)

    while x < b:
        integral += function(x) * h
        x += h

    return integral