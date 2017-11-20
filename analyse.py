from statistics import mean
import numpy as np

avxs = np.array([1,2,3,4,5], dtype=np.float64)
avys = np.array([2,3,6,7,11], dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(avxs)*mean(avys)) - mean(avxs*avys)) /
         ((mean(avxs)**2) - mean(avxs**2)))
    return m

m = best_fit_slope(avxs,avys)
print(m)