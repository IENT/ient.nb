import numpy as np

# t axis in seconds
(t, deltat) = np.linspace(-10, 10, 5001, retstep=True)  

# Elementary signals
gauss     = lambda t: np.exp(-(t)**2)
unitstep  = lambda t: np.where(t>=0, 1, 0)
rect      = lambda t: np.where(np.abs(t) <= 0.5, 1, 0)
tri       = lambda t: rect(t/2)*(1-abs(t))
si        = lambda t: np.sinc(t/np.pi) # English notation sinc(t) = sin(pi t)/(pi t)

eps = np.finfo(float).eps # floating point accuracy