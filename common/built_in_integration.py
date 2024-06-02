import numpy as np
from scipy import integrate

def alpha(T):
    p = np.pi

    f = 50

    integrand = lambda t: np.square(2 * p * f * t)

    integral = integrate.quad(integrand, 0, T)

    result = integral[0]

    return result