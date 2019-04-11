import numpy as np

def rsquare(x, y, popt, f):
    residuals = y - f(x, *popt)
    #Sum of the residuals squared
    ss_res = np.sum(residuals**2)
    #Total sum of squares
    ss_tot = np.sum((y-np.mean(y))**2)
    #R-Squared
    Rsq = 1.0 - ss_res/ss_tot
    return Rsq