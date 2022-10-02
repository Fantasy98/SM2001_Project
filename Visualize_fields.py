#%%
import Velocity_Reconst as v
import numpy as np 
from matplotlib import pyplot as plt

#%%

#%%
def visualize_fields(a_,start_t,end_t):
    ZP1,YP1 = np.meshgrid(v.zp,v.yp)
    XP2,ZP2 = np.meshgrid(v.xp,v.zp)
    print(ZP1.shape)
    for t in np.arange(start_t,end_t):
        a = a_[t,:]

        # velocity compoments
        ux = a[0]*v.u1x + a[1]*v.u2x + a[5]*v.u6x + a[6]*v.u7x + a[7]*v.u8x + a[8]*v.u9x
        uy = a[2]*v.u3y + a[7]*v.u8y
        uz = a[2]*v.u3z + a[3]*v.u4z + a[4]*v.u5z + a[5]*v.u6z + a[6]*v.u7z + a[7]*v.u8z
       

        # Average velocity in x-direction (down stream)
        ux_avg = np.reshape(np.mean(ux,axis=0),(v.ny,v.nz))
        uy_avg = np.reshape(np.mean(uy,axis=0),(v.ny,v.nz))
        uz_avg = np.reshape(np.mean(uz,axis=0),(v.ny,v.nz))
       
        # velocities at mid plane
        ce = np.ceil(v.ny//2)
        ce = np.int64(ce)
   
        ux_mid = np.reshape( ux[:,ce,:],(v.nx,v.nz) )
        uy_mid = np.reshape( uy[:,ce,:],(v.nx,v.nz) )
        uz_mid = np.reshape( uz[:,ce,:],(v.nx,v.nz) )

        
        ## plot 1 Mean Profile 
        f=plt.figure(0+t)
        plt.plot(np.mean(ux_avg,axis=1),v.yp,lw=5)
        plt.xticks(range(-1,2))
        plt.yticks(range(-1,2))
        plt.xlabel("${u_x}$")
        plt.ylabel("${u_y}$")
        f.savefig(r"/Users/wangyuning/Desktop/Data-driven Methods in Engineering Mechanics/SM2001_Project/Visualizing Data/Mean Profile@{}".format(t))

        f=plt.figure(1+t)
        cont=plt.contourf(ZP1,YP1,ux_avg,cmap="jet")
        plt.colorbar(cont)
        # plt.xticks(np.arange(-0.5,0.5,0.1))
        plt.quiver(ZP1,YP1,uz_avg,uy_avg)
        # plt.quiver(YP1,uy_avg,"k")
        plt.close(f)

        plt.xticks(np.arange(0,v.Lz))
        plt.yticks(range(-1,2))
        plt.ylabel("y")
        plt.xlabel("z")
        f.savefig(r"/Users/wangyuning/Desktop/Data-driven Methods in Engineering Mechanics/SM2001_Project/Visualizing Data/Down_Stream_contour@t={}".format(t))
        plt.close(f)
        
        f=plt.figure(2+t)
        cont2=plt.contourf(XP2,ZP2,uy_mid.T,cmap="jet")
        plt.colorbar(cont2)
        plt.quiver(XP2,ZP2,ux_mid.T,uz_mid.T)
        plt.xlabel("x")
        plt.ylabel("z")
        plt.xticks(np.arange(0,v.Lx))
        plt.yticks(np.arange(0,v.Lz))
        f.savefig(r"/Users/wangyuning/Desktop/Data-driven Methods in Engineering Mechanics/SM2001_Project/Visualizing Data/Mid_Line_contour@t={}".format(t))

        plt.close(f)
# %%
