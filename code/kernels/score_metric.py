"""Score-induced Riemannian metric utilities."""
import numpy as np


def metric_from_score(s_vec):
    """g(x) = (I + s s^T)^{-1} applied to every row of ``s_vec``."""
    n, d = s_vec.shape
    I = np.eye(d)
    G = I[None] + s_vec[:, :, None] * s_vec[:, None, :]
    return np.linalg.inv(G)


def metric_distances_sq(X, g):
    """Squared distance matrix under the symmetrised score metric.

    d_g^2(x_i, x_j) = (x_i-x_j)^\\top \\bar g_{ij}\\,(x_i-x_j)
    with g_{ij} = (g_i+g_j)/2
    """
    g_avg = 0.5 * (g[:, None] + g[None, :])
    diff = X[:, None] - X[None, :]
    return np.einsum("ijk, ijkl, ijl -> ij", diff, g_avg, diff)
