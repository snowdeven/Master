import numpy as np
import matplotlib.pyplot as plt


def propagator(N, Npts, Nz, nb):
    """
    This function contains all the parameters used in the propagation
    of solitons in fiber optics and the integrator called split step method.

    Args:
        N (int): The order of solitons
        Npts (int): The number of points on the time and frequency axis
        Nz (int): The number of points on the propagation Z-axis
        nb (int): The number of zsol, the spatial period the soliton should propagate exactly 

    Returns:
        Ip (array): Values of intensity
        Ip_TF (array): Values of spectral intensity
        FF (list): Frequency values
        TT (list): Time values
        ZZ (list): Propagation values of the Z-axis
    """

    # Constants and parameters
    lambda0 = 850e-9  # Wavelength
    c = 299792458  # Speed of light
    F0 = c / lambda0  # Central frequency

    Tmax = 0.5e-12  # Maximum time
    T0 = 28e-15  # Pulse duration

    beta2 = -13e-27  # Dispersion coefficient
    gamma = 0.10  # Nonlinear coefficient

    L_D = T0 ** 2 / abs(beta2)  # Characteristic length scale

    # Time and frequency grids
    dT = 2 * Tmax / (Npts - 1)
    TT = np.arange(-Npts / 2, Npts / 2) * dT
    FF = np.arange(-Npts / 2, Npts / 2) / (2 * Tmax)

    WW = 2 * np.pi * FF
    lambda_ = c / (FF + F0)

    # Initial condition peak power
    P0 = N ** 2 * abs(beta2) / (T0 ** 2 * gamma)
    A = np.sqrt(P0) * 1 / np.cosh(TT / T0)

    # Characteristic length scales
    zsol = np.pi / 2 * L_D
    Lz = nb * zsol
    dz = Lz / Nz
    ZZ = np.linspace(0, Lz, Nz)

    # Initialization
    Ip = np.zeros((Nz, Npts))
    Ip_TF = np.zeros((Nz, Npts))
    Ip[0, :] = np.abs(A) ** 2
    Ip_TF[0, :] = np.abs(np.fft.fftshift(np.fft.ifft(np.fft.fftshift(A)))) ** 2
    S_norm = np.max(Ip_TF[0, :])
    Ip_TF[0, :] = Ip_TF[0, :] / S_norm

    # Soliton propagation using split step method
    for i in range(1, Nz):
        A_TF = np.fft.fftshift(np.fft.ifft(A)) * np.exp(1j * beta2 / 2 * WW ** 2 * dz)
        A = np.fft.fft(np.fft.fftshift(A_TF))
        A = A * np.exp(1j * gamma * dz * np.abs(A) ** 2)

        
        Ip[i, :] = np.abs(A)**2
        Ip_TF[i, :] = np.abs(A_TF)**2 / S_norm
    
    Ip , Ip_TF = Ip/np.amax(Ip) , Ip_TF/np.amax(Ip_TF)
    ZZ = ZZ/zsol
    return Ip,Ip_TF,FF,TT,ZZ
    
def Norm(vector):
    """
    Calculates the Euclidean norm (magnitude) of a given vector.

    Args:
        vector (array-like): The input vector.

    Returns:
        float: The magnitude of the vector.

    """
    return np.linalg.norm(vector)


def error(borninf, bornsup, step, sub, Npts=2000, N=1, Nz=2000, nb=1):
    """
    Calculates the errors between the initial and final states of soliton propagation for varying parameters.

    Args:
        borninf (float): Lower bound of the parameter range.
        bornsup (float): Upper bound of the parameter range.
        step (int): Number of steps between the bounds.
        sub (str): Sub-parameter to vary ("Nz", "Npts", "N", or "Zsol").
        Npts (int): Number of points on the time and frequency axis. Default is 2000.
        N (int): Order of solitons. Default is 1.
        Nz (int): Number of points on the propagation Z-axis. Default is 2000.
        nb (int): Number of zsol, the spatial period the soliton should propagate exactly. Default is 1.

    Returns:
        err (list): List of errors in intensity.
        err2 (list): List of errors in spectral intensity.
        x (list): List of varied parameter values.

    """
    err = []  # List to store errors in intensity
    err2 = []  # List to store errors in spectral intensity
    x = []  # List to store varied parameter values
    for i in range(borninf, bornsup, step):
        x.append(i)  # Append the current parameter value to the list of parameter values

        # Update the appropriate parameter based on the sub-parameter to vary
        if sub == "Nz":
            Nz = i
        elif sub == "Npts":
            Npts = i
        elif sub == "N":
            N = i
        elif sub == "Zsol":
            nb = i

        # Perform soliton propagation using the updated parameters
        Ip, Ip_TF, FF, TT, ZZ = propagator(N, Npts, Nz, nb)

        # Rescale the obtained results
        Ip, Ip_TF, TT, FF = rescale(Ip, Ip_TF, TT, FF, Npts)

        # Calculate the errors in intensity and spectral intensity
        err.append(abs((Norm(Ip[0,:]) - Norm(Ip[-1,:])))/Norm(Ip[0,:]) *100 )
        err2.append(abs((Norm(Ip_TF[0,:]) - Norm(Ip_TF[-1,:])))/Norm(Ip_TF[0,:]) *100)
        # err.append(abs((max(Ip[0,:]) - max(Ip[-1,:])))/max(Ip[0,:]) *100 )
        # err2.append(abs((max(Ip_TF[0,:]) - max(Ip_TF[-1,:])))/max(Ip_TF[0,:]) *100)
    return err, err2, x
    

def rescale(Ip, Ip_TF, TT, FF, Npts, threshold=0.1, threshold_TF=0.01):
    """
    Rescales the soliton propagation results based on threshold values.

    Args:
        Ip (array): Values of intensity.
        Ip_TF (array): Values of spectral intensity.
        TT (array): Times values.
        FF (array): Frequency values.
        Npts (int): Number of points on the time and frequency axis.
        threshold (float): Threshold value for intensity. Default is 0.001.
        threshold_TF (float): Threshold value for spectral intensity. Default is 0.001.

    Returns:
        Ip (array): Rescaled values of intensity.
        Ip_TF (array): Rescaled values of spectral intensity.
        TT (array): Rescaled times values.
        FF (array): Rescaled frequency values.

    """
    index = 0
    index_TF = 0

    # Find the index where the intensity exceeds the threshold value
    for j in range(Npts):
        if max(np.abs(Ip[:, j])) > threshold:
            index = j + 1
            break

    # Find the index where the spectral intensity exceeds the threshold value
    for j in range(Npts):
        if max(np.abs(Ip_TF[:, j])) > threshold_TF:
            index_TF = j + 1
            break

    # Rescale the soliton propagation results based on the obtained indices
    Ip = Ip[:, index:-index]
    Ip_TF = Ip_TF[:, index_TF:-index_TF]
    TT = TT[index:-index]
    FF = FF[index_TF:-index_TF]

    return Ip, Ip_TF, TT, FF


def Simple_error_plot(borninf, bornsup, step, sub):
    """
    Generate a simple error plot for the intensity error and spectral intensity error.

    Parameters:
    - borninf (float): Lower bound of the range for the parameter being studied.
    - bornsup (float): Upper bound of the range for the parameter being studied.
    - step (float): Step size between consecutive values of the parameter.
    - sub (str): Parameter being studied.

    Returns:
    None
    """

    # Initialize empty lists for storing error values and parameter values
    err = []
    err2 = []
    x = []

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    # Compute the error values and retrieve the parameter values
    err, err2, x = error(borninf, bornsup, step, sub)

    # Plot the intensity error in the first subplot
    ax1.plot(x, err)
    ax1.set_xlabel(f'{sub}')
    ax1.set_ylabel("Error in percent")
    ax1.set_title("Intensity error")

    # Plot the spectral intensity error in the second subplot
    ax2.plot(x, err2)
    ax2.set_xlabel(f'{sub}')
    ax2.set_ylabel("Error in percent")
    ax2.set_title("Spectral Intensity error")

    # Set the super title for the entire figure
    plt.suptitle(r"Absolute error $\frac{||A(z=0) - A(z)||}{||A(z=0)||}$ " + f"along {sub}", size=18)

    # Display the plot
    plt.show()














