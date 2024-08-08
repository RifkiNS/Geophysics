import numpy as np
import matplotlib.pyplot as plt
step=10

nx = 750
nz = 601
dx = 1000
dz = 1000

vp = 1500.0 * np.ones((nz, nx))         
vs = vp / 1.732
rho = 3500 * np.ones(vp.shape)
lam = rho*(vp**2 - 2*vs**2)
mu = rho*vs**2   


t_total = 2.5
dt = 0.8/(vp.max() * np.sqrt(1/dx**2 + 1/dz**2))
nt = round(t_total/dt)
t = range(0,nt)*dt

CFL = vp.max()*dt * np.sqrt(1.0/dx**2 + 1.0/dz**2)

f0 = 25.0           
t0 = 1 / f0  
factor = 10**10
angle_force = 95.0

jsrc = round(nz/8)    
isrc = round(nx/4)     

a = np.pi*np.pi*f0*f0
dt2rho_src = dt**2/rho[jsrc, isrc]
source_term = factor * np.exp(-a*(t-t0)**2)                       

force_x = np.sin(angle_force * np.pi / 180) * source_term * dt2rho_src / (dx * dz)
force_z = np.cos(angle_force * np.pi / 180) * source_term * dt2rho_src / (dx * dz)
min_wavelengh = 0.5*((vs>330).choose(a,330)).min()/f0

abs_thick = min(np.floor(0.15*nx), np.floor(0.15*nz))
abs_rate = 0.3/abs_thick

lmargin = [abs_thick, abs_thick]
rmargin = [abs_thick, abs_thick]
weights = np.ones((nz+2,nx+2))
for iz in range(nz+2):
    for ix in range(nx+2):
        i = 0
        j = 0
        k = 0
        if (ix < lmargin[0] + 1):
            i = lmargin[0] + 1 - ix
        
        if (iz < lmargin[1] + 1):
            k = lmargin[1] + 1 - iz
        
        if (nx - rmargin[0] < ix):
            i = ix - nx + rmargin[0]
        
        if (nz - rmargin[1] < iz):
            k = iz - nz + rmargin[1]
       
        if (i == 0 and j == 0 and k == 0):
            continue
        
        rr = abs_rate * abs_rate * np.double(i*i + j*j + k*k )
        weights[iz,ix] = np.exp(-rr)

ux3 = np.zeros((nz+2,nx+2))
uz3 = np.zeros((nz+2,nx+2))
ux2 = np.zeros((nz+2,nx+2))
uz2 = np.zeros((nz+2,nx+2))
ux1 = np.zeros((nz+2,nx+2))
uz1 = np.zeros((nz+2,nx+2))

co_dxx = 1/dx**2
co_dzz = 1/dz**2
co_dxz = 1/(4.0 * dx * dz)
co_dzx = 1/(4.0 * dx * dz)
dt2rho=(dt**2)/rho
lam_2mu = lam + 2 * mu

for iter in range(1,nt):
    ux3 = np.zeros(ux2.shape)
    uz3 = np.zeros(uz2.shape)


    dux_dxx = co_dxx * (ux2[1:-1,0:-2] - 2*ux2[1:-1,1:-1] + ux2[1:-1,2:])
    dux_dzz = co_dzz * (ux2[0:-2,1:-1] - 2*ux2[1:-1,1:-1] + ux2[2:,1:-1])
    dux_dxz = co_dxz * (ux2[0:-2,2:] - ux2[2:,2:]- ux2[0:-2,0:-2] + ux2[2:,0:-2])

    duz_dxx = co_dxx * (uz2[1:-1,0:-2] - 2*uz2[1:-1,1:-1] + uz2[1:-1,2:])
    duz_dzz = co_dzz * (uz2[0:-2,1:-1] - 2*uz2[1:-1,1:-1] + uz2[2:,1:-1])
    duz_dxz = co_dxz * (uz2[0:-2,2:] - uz2[2:,2:]- uz2[0:-2,0:-2] + uz2[2:,0:-2])


    sigmas_ux = lam_2mu * dux_dxx + lam * duz_dxz + mu * (dux_dzz + duz_dxz)
    sigmas_uz = mu * (dux_dxz + duz_dxx) + lam * dux_dxz + lam_2mu * duz_dzz

    ux3[1:-1,1:-1] = 2.0*ux2[1:-1,1:-1] - ux1[1:-1,1:-1] + sigmas_ux*dt2rho
    uz3[1:-1,1:-1] = 2.0*uz2[1:-1,1:-1] - uz1[1:-1,1:-1] + sigmas_uz*dt2rho

    ux3[jsrc, isrc] = ux3[jsrc, isrc] + force_x[iter]
    uz3[jsrc, isrc] = uz3[jsrc, isrc] + force_z[iter]

    ux1 = ux2 * weights
    ux2 = ux3 * weights
    uz1 = uz2 * weights
    uz2 = uz3 * weights

    if iter%step==0:
      print('Time step: %d \t %.4f s\n'%(iter,t[iter]))
      u=(ux3**2 + uz3**2)**0.5
      plt.imshow(u,cmap='rainbow',aspect='equal')
      plt.show()
