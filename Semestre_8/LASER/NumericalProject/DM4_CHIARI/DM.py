import numpy as np 
import matplotlib.pyplot as plt
import mpmath as mp

plt.style.use("ggplot")
# def sech(x):
#     l=np.zeros(len(x))
#     for i in range(len(x)):
#         l[i] = mp.sech(x[i])
#     return l

# def asech(x):
#     l=np.zeros(len(x))
#     for i in range(len(x)):
#         l[i] = mp.asech(x[i])
#     return l
def find_nearest(X,Y, value):
    return abs(Y[np.unravel_index(np.argmin(np.abs(X - value)), X.shape)])*2

# def fftsech(x):
#     return np.sqrt(np.pi/(2*alpha**2)) * sech(np.pi/(2*alpha) *x)



# def gaussian(x,sigma):
#     return np.exp(- t**2 /(2*sigma**2))

# def solitons_molecules(x,phase,delay,sigma):
#     return gaussian(x,sigma) + gaussian(x - delay,sigma)*np.exp(1j*phase)

# def solitons_spec(x,phase,delay,sigma):
#     return 4*abs(np.fft.fftshift(np.fft.fft(gaussian(nu,sigma)))**2)*np.cos(np.pi*delay*x-phase/2)**2

# def spectrum(t,f,sigma,T,phi):
#     # Compute the soliton molecule in the frequency domain
#     soliton_spectrum = np.fft.fftshift(np.fft.fft(gaussian(t, sigma) + gaussian(t-T, sigma) * np.exp(1j * phi)))
#     return np.abs(soliton_spectrum)**2
# def gaussian_pulse(t, FWHM):
#     sigma = FWHM / (2 * np.sqrt(2 * np.log(2)))
#     return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-t**2 / (2 * sigma**2))
# def spectrum(t,FWHM,T,phi):
#     # Compute the soliton molecule in the frequency domain
#     soliton_spectrum = np.fft.fftshift(np.fft.fft(gaussian_pulse(t, FWHM) + gaussian_pulse(t-T, FWHM) * np.exp(1j * phi)))
#     return np.abs(soliton_spectrum)**2



def T(q0,Isat,I_t):
    return 1-q0/(1+I_t/Isat)
# # ---------------Question 2--------------
# FWHM = 10
# Tmax = 500  # Maximum time
# delay= 100
# Npts=10000

# # alpha=1/FWHM
# # Time and frequency grids
# dT = 2 * Tmax / (Npts - 1)
# t = np.linspace(-Tmax,Tmax,Npts)
# # nu = np.arange(-Npts / 2, Npts / 2) / (8 * Tmax)
# nu = np.fft.fftshift(np.fft.fftfreq(len(t), d=(t[1] - t[0])))
# sigma=FWHM/(2*np.sqrt(2*np.log(2)))

# phi_values=[0,np.pi/2,np.pi]
# # plt.plot(t,gaussian(t,sigma))
# for i in phi_values:
#     plt.plot(t,abs(solitons_molecules(t,delay,i,sigma))**2,label=f'phi={i}')

# plt.legend()
# plt.show()
# fig, axs = plt.subplots(3, 2, figsize=(17, 9))
# for i in range(len(phi_values)):
    
#     axs[i, 0].plot(nu,abs(solitons_spec(nu,phi_values[i],delay,sigma)),label=f'phi={round(phi_values[i],2)}')
#     axs[i, 0].set_title(f"Spectral soliton molecules for phi = {round(phi_values[i],2)}")
#     axs[i, 1].plot(nu,abs(spectrum(t,FWHM,delay,phi_values[i])),label=f'phi_th={round(phi_values[i],2)}',linestyle='--')
#     axs[i, 1].set_title(f"np.fft of the temporal soliton molecules for phi = {round(phi_values[i],2)}")
#     axs[i, 0].legend()
#     axs[i, 1].legend()

#     axs[i, 0].set_xlim((-0.10,0.10))
#     axs[i, 1].set_xlim((-0.10,0.10))
# plt.tight_layout(h_pad=2, w_pad=0.5)
# plt.show()

# # --------------------Question 3 ----------------------
# # Constants
# c = 299792458  # Speed of light in m/s
# FWHM = 100e-15  # Pulse duration in seconds
# center_wavelength = 800e-9  # Center wavelength in meters
# Tmax = 1e-12  # Maximum time
# Npts=1000
# # alpha=1/FWHM

# # Time and frequency grids
# dT = 2 * Tmax / (Npts - 1)
# t = np.arange(-Npts / 2, Npts / 2) * dT
# nu = np.arange(-Npts / 2, Npts / 2) / (2 * Tmax)


# nu0=c/center_wavelength
# wavelength=c/(nu +nu0)
# # Gaussian pulse
# sigma=FWHM/(2*np.sqrt(2*np.log(2)))
# gaussian_temp= gaussian(t,sigma)
# gaussian_spectrum =abs(np.fft.fftshift(np.fft.fft(gaussian_temp)))

# # Sech pulse
# truc=FWHM/(2*np.log(2+np.sqrt(3)))
# alpha=np.log((np.sqrt(2)+1)/(np.sqrt(2)-1))/FWHM
# sech_pulse = sech(t*alpha)
# sech_spectrum = abs(np.fft.fftshift(np.fft.fft(sech_pulse)))

# print(r"$\Delta \tau$:",find_nearest(sech_pulse,t,max(sech_pulse)/2))
# print(r"$\Delta \tau_{th}$:",1/alpha *np.log((np.sqrt(2)+1)/(np.sqrt(2)-1)))
# print(r"$\Delta \nu $:",find_nearest(sech_spectrum**2,nu*1e-12,max(sech_spectrum**2)/2))
# print(r"$\Delta \nu_{th}$:",alpha*1e-12/np.pi**2 * np.log((np.sqrt(2)+1)/(np.sqrt(2)-1)))

# # Plotting the temporal intensity profiles
# plt.figure(figsize=(12, 6))
# plt.plot(t * 1e15, gaussian_temp**2, label="Gaussian Pulse")
# plt.plot(t * 1e15, sech_pulse**2, label="Sech Pulse")
# plt.xlabel("Time (fs)")
# plt.ylabel("Intensity")
# plt.title("Temporal Intensity Profiles")
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plotting the spectral intensity profiles
# plt.figure(figsize=(12, 6))
# plt.plot(wavelength*1e9, gaussian_spectrum**2/max(gaussian_spectrum**2), label="Gaussian Spectrum")
# plt.plot(wavelength*1e9, sech_spectrum**2/max(sech_spectrum**2), label="Sech Spectrum")
# plt.xlabel("Wavelength (nm)")
# plt.ylabel("Intensity")
# plt.title("Spectral Intensity Profiles")
# plt.legend()
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(12, 6))
# plt.plot(nu*1e-12, gaussian_spectrum, label="Gaussian Spectrum")
# plt.plot(nu*1e-12, sech_spectrum, label="Sech Spectrum")
# plt.xlabel("Wavelength (nm)")
# plt.ylabel("Intensity")
# plt.title("Spectral Intensity Profiles")
# plt.legend()
# plt.grid(True)
# plt.show()




# --------------------Question 4---------------

def gaussian_peak(P0,sigma,t):
    return (np.sqrt(P0)*np.exp(- t**2 /(2*sigma**2)))**2

def pass_trought_absorber(fct):
    return (np.sqrt(T(q0,I_sat,fct))*np.exp(- t**2 /(2*sigma**2)))**2
FWHM = 1
Tmax = 5 # Maximum time
Npts=10000
t = np.linspace(-Tmax,Tmax,Npts)
nu = np.fft.fftshift(np.fft.fftfreq(len(t), d=(t[1] - t[0])))
sigma=FWHM/(2*np.sqrt(2*np.log(2)))
q0=0.75

I_sat=500
Power_peak=[10,100,1000]
Power_noise=np.random.normal(1000,10,10000)

for i in Power_peak:
    plt.plot(t,T(q0,I_sat,gaussian_peak(i,sigma,t)),label=f'Power peak={i} W')

plt.xlabel("Time in ps")
plt.ylabel("Transmission")
plt.title("Transmission function for three gaussian pulse of different peak powers with FWHM = 1ps")

plt.legend()
plt.show()

