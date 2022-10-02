import numpy as np
# def visualize_fields(a_):
# % Plot function for velocity fields
# % The function reconstructs the velocity fields using the 9 chosen Fourier
# % modes and their corresponding amplitudes
# %
# % Input:
# %   a - A matrix of size (nTP, 9), where nTP is the number of time points
# %
# % The code has been used for the results in:
# % "Predictions of turbulent shear flows using deep neural networks"
# % P.A. Srinivasan, L. Guastoni, H. Azizpour, P. Schlatter, R. Vinuesa
# % Physical Review Fluids (accepted)
# % Visualization start and end time
start_t = 404
end_t = start_t

    # Size of the domain
Lx = 4*np.pi
Lz = 2*np.pi

A = 2*np.pi/Lx
B = np.pi/2
C = 2*np.pi/Lz

    # Velocity fields
    # Number of gridpoints in each direction
nx = 21
ny = nx
nz = nx

    # The gridpoints
xp = np.linspace(0,Lx,nx)
yp = np.linspace(-1,1,ny)
zp = np.linspace(0,Lz,nz)

    # % Initialize arrays for each component of the 9 modes
u1x = np.zeros(shape=(nx,ny,nz))
u2x = np.zeros(shape=(nx,ny,nz))
u6x = np.zeros(shape=(nx,ny,nz))
u7x = np.zeros(shape=(nx,ny,nz))
u8x = np.zeros(shape=(nx,ny,nz))
u9x = np.zeros(shape=(nx,ny,nz))
u3y = np.zeros(shape=(nx,ny,nz))
u8y = np.zeros(shape=(nx,ny,nz))
u3z = np.zeros(shape=(nx,ny,nz))
u4z = np.zeros(shape=(nx,ny,nz))
u5z = np.zeros(shape=(nx,ny,nz))
u6z = np.zeros(shape=(nx,ny,nz))
u7z = np.zeros(shape=(nx,ny,nz))
u8z = np.zeros(shape=(nx,ny,nz))

    # The velocity components of the chosen Fourier modes
for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                u1x[i,j,k] = 2**0.5*np.sin(B*yp[j])
                u2x[i,j,k] = (4/3)**0.5*(np.cos(B*yp[j]))**2 * np.cos(C*zp[k])
                u6x[i,j,k] = 4*np.sqrt(2/3/(A**2 + C**2))*(-C)*np.cos(A*xp[i])*(np.cos(B*yp[j]))**2*np.sin(C*zp[k]) 
                # u6x[i,j,k] = 4*np.sqrt(2/3/(A**2 + C**2))*(-C)*np.cos(A*xp[i])*(np.cos(B*yp[j]))**2*np.sin(C*zp[k])
                u7x[i,j,k] = 2*np.sqrt(2/(A**2 + C**2))*C*np.sin(A*xp[i])*np.sin(B*yp[j])*np.sin(C*zp[k])
                u8x[i,j,k] = 2*np.sqrt(2/(A**2 + C**2)/(4*A**2 + 4*C**2 + np.pi**2))*(np.pi*A)*np.sin(A*xp[i])*np.sin(B*yp[j])*np.sin(C*zp[k])
                u9x[i,j,k] = 2**0.5*np.sin(3*B*yp[j])
                u3y[i,j,k] = 2/np.sqrt(4*C**2 + np.pi**2)*2*C*np.cos(B*yp[j])*np.cos(C*zp[k])
                u8y[i,j,k] = 2*np.sqrt(2/(A**2 + C**2)/(4*A**2 + 4*C**2 + np.pi**2))*2*(A**2+C**2)*np.cos(A*xp[i])*np.cos(B*yp[j])*np.sin(C*zp[k])
                u3z[i,j,k] = 2/np.sqrt(4*C**2 + np.pi**2)*np.pi*np.sin(B*yp[j])*np.sin(C*zp[k])
                u4z[i,j,k] = 4/3**0.5*np.cos(A*xp[i])*(np.cos(B*yp[j]))**2
                u5z[i,j,k] = 2*np.sin(A*xp[i])*np.sin(B*yp[j])
                u6z[i,j,k] = 4*np.sqrt(2/3/(A**2 + C**2))*A*np.sin(A*xp[i])*(np.cos(B*yp[j]))**2*np.cos(C*zp[k])
                u7z[i,j,k] = 2*np.sqrt(2/(A**2 + C**2))*A*np.cos(A*xp[i])*np.sin(B*yp[j])*np.cos(C*zp[k])
                u8z[i,j,k] = 2*np.sqrt(2/(A**2 + C**2)/(4*A**2 + 4*C**2 + np.pi**2))*(-np.pi*C)*np.cos(A*xp[i])*np.sin(B*yp[j])*np.cos(C*zp[k])

