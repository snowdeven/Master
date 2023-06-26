from mayavi import mlab

from function import *
import numpy


# Create a new Mayavi figure
mlab.figure(1, fgcolor=(1, 1, 1), size=(1024, 1024), bgcolor=(0.5, 0.5, 0.5))
mlab.clf()

# Set the main parameters
Nz = 10000
Npts = 2000
nb = 1

# Set the initial x-axis bounds
borne_x_inf = 0
borne_x_sup = 7

# Iterate over soliton orders
for i in range(1, 7, 1):
    borne_x_sup += 3
    borne_x_inf += 3
    
    # Compute the soliton profiles using the propagator function
    Ip, Ip_TF, FF, TT, ZZ = propagator(i, Npts, Nz, nb)
    
    # Rescale the profiles for better visualization
    Ip, Ip_TF, TT, FF = rescale(Ip, Ip_TF, TT, FF, Npts, threshold=0.1, threshold_TF=0.01)
    
    # Set the extent for the 2D surface plot
    _extent = (borne_x_inf, borne_x_sup, 0, 10, 0, 5)
    
    # Transpose and flip the array for correct orientation
    Ip = numpy.transpose(Ip)
    Ip = Ip[::-1, :]
    
    # Plot the 2D surface plot for the soliton intensity
    surf_ = mlab.surf(Ip, colormap='Spectral', extent=_extent)
    mlab.outline(surf_, color=(0, 0, 0), extent=_extent)

    if i == 1:
        # Customize the axes and add a colorbar for the first soliton order
        mlab.axes(surf_, color=(0, 0, 0), extent=_extent, ranges=(min(TT*1e12), max(TT*1e12), min(ZZ), max(ZZ), 0, 1), xlabel='Time in ps', ylabel='Propagation', zlabel='Intensity', x_axis_visibility=True, z_axis_visibility=True)
        ax = mlab.axes()
        ax.axes.font_factor = 0.5
        ax.title_text_property.font_size = 10
        ax.label_text_property.font_size = 1
        cb = mlab.colorbar(title="Intensity and spectral intensity")
        cb.scalar_bar.unconstrained_font_size = True
        cb.scalar_bar_representation.proportional_resize = True
        cb.label_text_property.font_size = 14

    # Set the extent for the 3D surface plot
    _extent = (borne_x_inf, borne_x_sup, 20, 30, 0, 5)
    
    # Transpose and flip the array for correct orientation
    Ip_TF = numpy.transpose(Ip_TF)
    Ip_TF = Ip_TF[::-1, :]
    
    # Plot the 3D surface plot for the transformed soliton intensity
    surf_ = mlab.surf(Ip_TF, colormap='Spectral', extent=_extent)
    mlab.outline(surf_, color=(0, 0, 0), extent=_extent)
    
    # Update the x-axis bounds for the next iteration
    borne_x_sup += 7
    borne_x_inf += 7


    if i == 1:
        # Customize the axes and add a colorbar for the first soliton order
        mlab.axes(surf_, color=(0, 0, 0), extent=_extent, ranges=(min(FF*1e-12), max(TT*1e-12), min(ZZ), max(ZZ), 0, 1), xlabel='Frequency in Thz', ylabel='Propagation', zlabel='Intensity', x_axis_visibility=True, z_axis_visibility=True)
        ax = mlab.axes()
        ax.axes.font_factor = 0.5
        ax.title_text_property.font_size = 10
        ax.label_text_property.font_size = 1
        cb = mlab.colorbar(title="Intensity and spectral intensity")
        cb.scalar_bar.unconstrained_font_size = True
        cb.scalar_bar_representation.proportional_resize = True
        cb.label_text_property.font_size = 14



# Display the Mayavi plot

mlab.show()