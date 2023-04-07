import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 396317433

def solution(p: float, x: np.array) -> tuple:
    n = x.shape[0]
    alpha = p
    loc = x.mean() * 2
    scale = loc / np.sqrt(3*n)
    return loc + 0.038 - norm.ppf((1 + alpha) / 2) * scale, \
           loc + 0.038 + norm.ppf((1 + alpha) / 2) * scale

