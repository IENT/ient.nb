import numpy as np
if __package__ is None or __package__ == '':
    from ient_signals import eps
else:
    from ient_nb.ient_signals import eps


def ient_dft(s, fs, NFFT=0):
    """
    Calculate discrete Fourier transform of vector s
    Sampling frequency fs is used to calculate frequency vector f
    Number of frequency coefficients can be specified as well
    """
    if NFFT==0: 
        NFFT = len(s) # int(2**np.ceil(np.log2(len(bla))))
    
    S = np.fft.fftshift(np.fft.fft(s, NFFT))/NFFT
    f = np.linspace(-fs/2,fs/2, NFFT)
    
    return S, f


def ient_idft(S, Ntime=0, NFFT=0):
    """
    Calculate discrete inverse Fourier transform of vector S
    Number of time bins is used to crop the output of NumPy's ifft function
    Number of frequency coefficients can be specified as well
    """
    if NFFT == 0: NFFT = len(S)
    
    s = np.fft.ifft(np.fft.ifftshift(S*NFFT), NFFT)
    
    if not Ntime == 0:
        s = s[0:Ntime]
    
    return s


def ient_ilaplace_ht(t=np.linspace(-6, 6, num=1024), H0=1, pp=np.array([]), pz=np.array([]), ord_p=np.array([]),
                     ord_z=np.array([]), roc=[-12, 12]):
    """
    Calculate inverse Laplace Transform from s-domain to t-domain
    """

    # check for parameters
    pp = np.array(pp)
    pz = np.array(pz)
    ord_p = np.array(ord_p)
    ord_z = np.array(ord_z)

    td = sd = np.array([])

    poles = np.append(pp, np.conj(pp[np.where(pp.imag != 0)]))
    poles_order = np.append(ord_p, ord_p[np.where(pp.imag != 0)]).astype(int)

    zeroes = np.append(pz, np.conj(pz[np.where(pz.imag != 0)]))
    zeroes_order = np.append(ord_z, ord_z[np.where(pz.imag != 0)]).astype(int)

    #####
    left_border = roc[0]
    right_border = roc[1]
    pole_is_causal = np.ones(poles.shape)

    pole_is_causal[np.where(poles.real <= left_border)] = True
    pole_is_causal[np.where(poles.real >= right_border)] = False

    #####

    if np.sum(poles_order) >= np.sum(zeroes_order):

        b = np.zeros((np.sum(poles_order) + 1, 1))
        A = np.zeros((len(b), len(b)), dtype=complex)

        col = 0
        tmp = np.array([])
        for ind, pp in enumerate(poles):
            tmp = np.append(tmp, np.array(pp * np.ones(poles_order[ind])))

        p = np.poly(tmp)

        if isinstance(p, float):
            A[-int(p):, col] = p;
        else:
            A[-len(p):, col] = p;

        for ind, ppoles in enumerate(poles):
            for indd in range(1, poles_order[ind] + 1):
                tmp = ppoles * np.ones(poles_order[ind] - indd)
                for ind2, ppoles2 in enumerate(poles):
                    if ind != ind2:
                        tmp = np.append(tmp, np.array(ppoles2 * np.ones(poles_order[ind2])))
                p = np.poly(tmp)

                col = col + 1

                if isinstance(p, float):
                    A[-int(p):, col] = p;
                else:
                    A[-len(p):, col] = p;

        ####

        tmp = []
        for ind, pzeroes in enumerate(zeroes):
            tmp = np.append(tmp, np.array(pzeroes * np.ones(zeroes_order[ind])))

        p = H0 * np.poly(tmp)

        if isinstance(p, np.ndarray):
            b[-len(p):, 0] = p.transpose()
        else:
            b[-1:, 0] = p

        try:
            A_inv = np.around(np.linalg.inv(A), 8)  # precision
        except np.linalg.LinAlgError:
            # Not invertible.
            pass

        a = np.dot(A_inv, b)

        ####

        h = np.zeros(t.shape)

        row = 0

        for ind, ppoles in enumerate(poles):
            for indd in range(1, poles_order[ind] + 1):
                row = row + 1
                amplitude = a[row]
                if indd > 1:
                    amplitude = amplitude / np.prod(range(1, indd))

                tmp = amplitude * np.power(t, indd - 1) * np.exp(ppoles * t)
                if pole_is_causal[ind]:
                    tmp[np.where(t < 0)] = 0
                else:
                    tmp[np.where(t >= 0)] = 0
                    tmp = -tmp

                h = np.add(h, tmp)

        a[0] = np.real(a[0])
        if np.abs(a[0]) > eps:
            if a[0]:
                h = np.array(np.real(h), dtype=float)
                td = np.array([0])
                sd = np.array(a[0])
    else:
        # Zaehlergrad größer als Nennergrad. Keine Partialbruchzerlegung möglich
        h = np.array([np.NaN for x in t])

    return h, td, sd


def ient_ilaplace_Hf(f=np.linspace(-6, 6, num=1024), H0=1, pp=np.array([]), pz=np.array([]), ord_p=np.array([]),
                     ord_z=np.array([]), dB=False):
    numerator = H0 * np.ones(f.shape)

    for ind, ppz in enumerate(pz):
        for _ in range(1, ord_z[ind] + 1):
            numerator = numerator * (1j * f - ppz)
            if np.abs(np.imag(ppz)):
                numerator = numerator * (1j * f - np.conj(ppz))

    denominator = np.ones(f.shape)

    for ind, ppp in enumerate(pp):
        for _ in range(1, ord_p[ind] + 1):
            denominator = denominator * (1j * f - ppp)
            if np.abs(np.imag(ppp)):
                denominator = denominator * (1j * f - np.conj(ppp))
    if dB:
        return 20 * np.log10(np.maximum(eps, np.abs(numerator / denominator)))
    else:
        return np.abs(numerator / denominator)
