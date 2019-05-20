import numpy as np


def ient_dft(s, fs, NFFT=0):
    """
    Calculate discrete Fourier transform of vector s
    Sampling frequency fs is used to calculate frequency vector f
    Number of frequency coefficients can be specified as well
    """
    if NFFT==0: 
        NFFT = len(s); # int(2**np.ceil(np.log2(len(bla))))
    
    S = np.fft.fftshift(np.fft.fft(s, NFFT))/NFFT
    f = np.linspace(-fs/2,fs/2, NFFT)
    
    return (S, f)

def ient_idft(S, Ntime=0, NFFT=0):
    """
    Calculate discrete inverse Fourier transform of vector S
    Number of time bins is used to crop the output of NumPy's ifft function
    Number of frequency coefficients can be specified as well
    """
    if NFFT==0: NFFT = len(S)
    
    s = np.fft.ifft(np.fft.ifftshift(S*NFFT), NFFT)
    
    if not Ntime==0:
        s = s[0:Ntime]
    
    return s