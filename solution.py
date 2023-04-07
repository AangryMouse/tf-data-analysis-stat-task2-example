import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 396317433

def solution(p: float, x: np.array) -> tuple:
    n = x.shape[0]
    alpha = 1 - p
    loc = x.mах()
    scale = (loc - 0.038) / np.sqrt(2*n)
    return loc - norm.ppf(1 - alpha / 2) * scale, \
           loc + norm.ppf(1 - alpha / 2) * scale


