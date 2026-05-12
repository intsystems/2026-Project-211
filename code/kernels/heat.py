"""Discrete heat kernel and pointwise normalisation."""
import numpy as np


def discrete_heat_kernel(L_sym, t):
    """H_t = exp(-t L_sym) via dense eigendecomposition."""
    w, V = np.linalg.eigh(L_sym)
    return (V * np.exp(-t * w)) @ V.T


def normalise_pointwise(K):
    """normalisation"""
    d = np.sqrt(np.clip(np.diag(K), 1e-15, None))
    return K / np.outer(d, d)
