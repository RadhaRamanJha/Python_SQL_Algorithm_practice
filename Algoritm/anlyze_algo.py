# modeling the data based on input and output values
import numpy as np
from scipy.optimize import curve_fit

def liner_model(n,a,b):
    return a*n+b

def quadratic_model(n, a, b):
    return a*n*n + b*n

# Sample data

xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

# cofficients are returned as first argument
[(a,b),_] = curve_fit(liner_model,np.array(xs),np.array(ys))
print("linear model = {}*n{}".format(a,b))

[(c,d),_] = curve_fit(quadratic_model,np.array(xs),np.array(ys))
print("Quadratic model is {}*n**2 + {}".format(c,d))