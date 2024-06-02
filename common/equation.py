import numpy as np

def R(alpha, U_m, W):
    alpha = float(alpha)
    U_m = float(U_m)
    W = float(W)

    result = alpha * np.square(U_m) / (3600 * W)

    return result

def u(t, U_m):
    p = np.pi
    f = 50.0

    result = U_m * np.abs(2 * p * f * t)

    return result