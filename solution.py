import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 396317433

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean() * 2
    scale = loc / np.sqrt(3*n)
    return loc - norm.ppf((1 + alpha) / 2) * scale, \
           loc + norm.ppf((1 + alpha) / 2) * scale

