"""Berry-Sauer / Coifman-Lafon symmetric Laplacian (Theorem 4.7)."""
import numpy as np


def berry_sauer_general(X=None, eps=None, alpha=1.0, dist_sq=None):
    """
    Right-normalised symmetric graph Laplacian, Berry-Sauer Theorem 4.7.
    """
    if dist_sq is None:
        if X is None:
            raise ValueError("Need X or dist_sq")
        dist_sq = np.sum((X[:, None] - X[None]) ** 2, axis=-1)
    K = np.exp(-dist_sq / eps)
    q = K.sum(axis=1) ** alpha
    K_a = K / np.outer(q, q)
    d = K_a.sum(axis=1)
    d_inv_sqrt = 1.0 / np.sqrt(d)
    K_norm = K_a * np.outer(d_inv_sqrt, d_inv_sqrt)
    n = dist_sq.shape[0]
    L_sym = (np.eye(n) - K_norm) / eps
    return 0.5 * (L_sym + L_sym.T)
