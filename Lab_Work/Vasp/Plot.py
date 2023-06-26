import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



plt.style.use("ggplot")

def Ehh(E_vide,type):
    """
    Calculate the Ehh value based on the given parameters.

    Args:
        E_vide (float): The E_vide value.
        material_type (str): The type of material ("sI" or "sII").

    Returns:
        float: The calculated Ehh value.
    """
    if type =="sI":
        nb_H20=46
    else:
        nb_H20=136
    return (E_vide - nb_H20*E_REF_H20)/(nb_H20)

def Egh(E_DFT,E_vide,l,type):
    """
    Calculate the Egh value based on the given parameters.

    Args:
        E_DFT (float): The E_DFT value.
        E_vide (float): The E_vide value.
        l (float): The l value.
        material_type (str): The type of material ("sI" or "sII").

    Returns:
        float: The calculated Egh value.
    """
    if type =="sI":
        nb_SC=2
    else:
        nb_SC=16
    return (E_DFT - E_vide - (l+nb_SC)*E_REF_C0)/(l+nb_SC)



# Reference energy values
E_REF_H20 = -13.12345414
E_REF_C0 = -11.88607971

data_sI=np.loadtxt("dataConvex/data_convex1.txt")
data_sII=np.loadtxt("dataConvex/data_convex2.txt")

E_DFT_sI= data_sI[:,1]
E_DFT_sII= data_sII[:,1]
Vmin_sI = data_sI[:,2]
Vmin_sII = data_sII[:,2]
dV_sI = data_sI[:,3]
dV_sII = data_sII[:,3]
B0_sI = data_sI[:,4]
B0_sII = data_sII[:,4]
dB0_sI = data_sI[:,5]
dB0_sII = data_sII[:,5]

HostEnergy_sI=pd.read_table("dataConvex/HostEnergy_sI.txt",sep=" ",skiprows=0,header=None)
HostEnergy_sI = HostEnergy_sI.to_numpy()
E_vide_sI = HostEnergy_sI[:,6]

HostEnergy_sII=pd.read_table("dataConvex/HostEnergy_sII.txt",sep=" ",skiprows=0,header=None)
HostEnergy_sII= HostEnergy_sII.to_numpy()
E_vide_sII = HostEnergy_sII[:,6]
E_vide_sII_Trunc = np.delete(HostEnergy_sII[:,6],1)

Theta_sI=np.array([float(i[2:]) for i in HostEnergy_sI[:,0]])
Theta_sII =np.array([float(i[2:]) for i in HostEnergy_sII[:,0]])




# Plot amin along the Composition for sI and sII
fig, ((ax1, ax2)) = plt.subplots(1, 2)

ax1.plot(Theta_sI, Vmin_sI)
ax1.errorbar(Theta_sI, Vmin_sI, yerr=dV_sI,label="Error bar",capsize=5)
ax1.set_xlabel(r"$\theta_{LC}$ ")
ax1.set_ylabel("unit cell parameter" + r"$ \ (\AA)$")
ax1.set_title("unit cell parameter along  Composition (sI)")
ax1.legend()
ax2.plot(Theta_sII, Vmin_sII)
ax2.errorbar(Theta_sII, Vmin_sII, yerr=dV_sII,label="Error bar",capsize=5)
ax2.set_xlabel(r"$\theta_{LC}$ ")
ax2.set_ylabel("unit cell parameter" + r"$ \ (\AA)$")
ax2.set_title("unit cell parameter along Composition (sII)")
ax2.legend()
plt.show()

# Plot B0 along the Composition for sI and sII
fig, ((ax1, ax2)) = plt.subplots(1, 2)

ax1.plot(Theta_sI, B0_sI)
ax1.errorbar(Theta_sI, B0_sI, yerr=dB0_sI,label="Error bar",capsize=5)
ax1.set_xlabel(r"$\theta_{LC}$ ")
ax1.set_ylabel("B0 (GPa)")
ax1.set_title("B0 along  Composition (sI)")
ax1.legend()
ax2.plot(Theta_sII, B0_sII)
ax2.errorbar(Theta_sII, B0_sII, yerr=dB0_sII,label="Error bar",capsize=5)
ax2.set_xlabel(r"$\theta_{LC}$ ")
ax2.set_ylabel("B0 (GPa)")
ax2.set_title("B0 along Composition (sII)")
ax2.legend()
plt.show()


# Plot Ehh along Composition for sI and sII

plt.plot(Theta_sI, Ehh(E_vide_sI, "sI"),marker='.',label="sI")

plt.plot(Theta_sII, Ehh(E_vide_sII, "sII"),marker='.',label="sII")
plt.legend()
plt.xlabel(r"$\theta_{LC}$ ")
plt.ylabel(r"$E_{hh}$ (eV/molecule)")
plt.title(r"$E_{hh}$ along Composition")
plt.show()


# Plot Egh along Composition for sI and sII
plt.plot(Theta_sI, Egh(E_DFT_sI, E_vide_sI, Theta_sI*6, "sI"),marker='.',label="sI")


plt.plot(Theta_sII, Egh(E_DFT_sII, E_vide_sII, Theta_sII*8, "sII"),marker='.',label="sII")
plt.xlabel(r"$\theta_{LC}$ ")
plt.ylabel(r"$E_{gh}$ (eV/molecule)")
plt.title(r"$E_{gh}$ along  Composition ")
plt.legend()
plt.show()



# Load the data for Enthalpy Diagram
diagram_ice_H = np.loadtxt("dataIce/EnthalpyRel_vdWDF2-PAW.dat")
P_1 = diagram_ice_H[:, 0]
H_1 = diagram_ice_H[:, 1]
P_2 = diagram_ice_H[:, 2]
H_2 = diagram_ice_H[:, 3]
P_3 = diagram_ice_H[:, 4]
H_3 = diagram_ice_H[:, 5]
P_4 = diagram_ice_H[:, 6]
H_4 = diagram_ice_H[:, 7]


# Plot the Enthalpy Diagram
plt.semilogx(P_1, H_1, label="xI")
plt.semilogx(P_2, H_2, label="II")
plt.semilogx(P_3, H_3, label="XV")
plt.semilogx(P_4, H_4, label="VIII")

# Labels and title
plt.xlabel('Pressure (GPa)')
plt.ylabel('Relative Enthalpy')
plt.title('Relative Enthalpy Diagram per Pressure')

# Find the pressure points where phase transitions occur
transitions = []
phases = ['xI', 'II', 'XV', 'VIII']
for i in range(len(phases) - 1):
    p_transition = np.where(H_1 < H_2)[0]
    transitions.append(p_transition)
    H_1 = H_2
    P_1 = P_2
    H_2 = H_3
    P_2 = P_3
    H_3 = H_4
    P_3 = P_4

# Text indicating the phase transitions
y_offset =  [-0.04,-0.08,-0.12,-0.18]  # Vertical offset to avoid overlapping texts
for i, transition in enumerate(transitions):
    if len(transition) > 0:
        p_min = P_1[transition[0]]
        p_max = P_1[transition[-1]]
        plt.text(0.020, y_offset[i], f"Transition: {phases[i]} to {phases[i + 1]}", ha='center', va='bottom')

# Axes limits
plt.ylim([-0.5, 0.25])
plt.xlim([0, 9])

# Legend
plt.legend()

# Display the graph
plt.show()


# Read data from file
data = pd.read_table("dataConvex/Encut.dat", sep=" ", skiprows=0, header=None)
data = data.to_numpy()
encut = list(data[:, 0])
E = list(data[:, 3])

# Create plot
plt.plot(encut,E)
plt.ylabel('E (eV)')
plt.xlabel('Encut')
plt.title('Plot of Encut versus E')

# Display the plot
plt.show()