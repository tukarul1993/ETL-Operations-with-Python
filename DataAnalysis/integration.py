import math

def integrate_sin_cos(x):
    sinx = math.sin(x)
    cosx = math.cos(x)
    integrand = (2*sinx*cosx - math.pow(cosx,2) + math.pow(sinx,2)) / (sinx * cosx)
    integral = 2*x - math.log(abs(sinx)) + math.log(abs(cosx))
    return integral

# Test the function with an example value of x
x = math.pi / 4
print(integrate_sin_cos(x))

"""
"""

'''
'''