import numpy as np
from scipy import signal # butter

def ient_butter(cutoff, fs, order=5, type='Tiefpass', fdelta=0):
    """
    Design Butterworth filter
    """
    btypes = {'Tiefpass':'lowpass', 'Bandpass':'bandpass', 'Hochpass':'highpass'}
    btype = btypes[type]
    nyq = 0.5 * fs # Nyquist frequency
    if btype == 'bandpass':
        normal_min = (cutoff-fdelta/2) / nyq; normal_max = (cutoff+fdelta/2) / nyq; # normalized min and max frequency
        normal_cutoff = [normal_min, normal_max]
    else:
        normal_cutoff = cutoff / nyq # normalized cutoff-frequency
    b, a = signal.butter(order, normal_cutoff, btype=btype, analog=False) # coefficients in z-domain
    return b, a
    
# Shortcuts
def ient_butter_bandpass(f0, fdelta, fs, order=5):
    b,a = ient_butter(f0, fs, order, 'Bandpass', fdelta)
    return b, a
def ient_butter_lowpass(cutoff, fs, order=5):
    b,a = ient_butter(cutoff, fs, order, 'Tiefpass')
    return b, a
def ient_butter_highpass(cutoff, fs, order=5):
    b,a = ient_butter(cutoff, fs, order, 'Hochpass')
    return b, a

def ient_filter(s, b, a):
    """
    Filter s(n) in z-Domain with filter coefficients a and b:
                        -1              -M
            b[0] + b[1]z  + ... + b[M] z
    G(z) = -------------------------------- S(z)
                        -1              -N
            a[0] + a[1]z  + ... + a[N] z
    """
    g = signal.lfilter(b, a, s)
    return g
