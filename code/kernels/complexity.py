"""Data complexity functional and natural diffusion timescales."""
import numpy as np


def complexity(K, jitter=1e-10):
    """C(X) = log det(I + K)"""
    n = K.shape[0]
    M = np.eye(n) + K + jitter * np.eye(n)
    L = np.linalg.cholesky(M)
    return float(2.0 * np.sum(np.log(np.diag(L))))


def t_spectral(L_sym):
    """1 / lambda_2(L_sym) - diffusion timescale"""
    w = np.sort(np.linalg.eigvalsh(L_sym))
    nz = w[w > 1e-9]
    return float(1.0 / nz[0]) if len(nz) else float("inf")


def t_median(d2):
    """Median of off-diagonal squared distances."""
    n = d2.shape[0]
    mask = ~np.eye(n, dtype=bool)
    return float(np.median(d2[mask]))
