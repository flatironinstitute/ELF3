import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

q0=np.loadtxt('0q/290K/sasa.dat')
q7=np.loadtxt('7q/290K/sasa.dat')
q13=np.loadtxt('13q/290K/sasa.dat')
q19=np.loadtxt('19q/290K/sasa.dat')

fig, axs = plt.subplots(4,figsize=(9,6.5), dpi=300)
axs[0].plot(q0,color='limegreen')
axs[1].plot(q7,color='limegreen')
axs[2].plot(q13,color='limegreen')
axs[3].plot(q19,color='limegreen')
axs[0].set_xlim([0,186])
axs[0].set_ylim([0.001,3])
axs[1].set_xlim([0,186])
axs[1].set_ylim([0.001,3])
axs[2].set_xlim([0,186])
axs[2].set_ylim([0.001,3])
axs[3].set_xlim([0,186])
axs[3].set_ylim([0.001,3])

axs[0].text(s='0Q',x=170,y=.22,fontsize=20)
axs[1].text(s='7Q',x=170,y=.22,fontsize=20)
axs[2].text(s='13Q',x=170,y=.22,fontsize=20)
axs[3].text(s='19Q',x=170,y=.22,fontsize=20)


x=range(186)
axs[0].tick_params(axis='x',labelsize=0)
axs[0].tick_params(axis='y',labelsize=18)
axs[1].tick_params(axis='x',labelsize=0)
axs[1].tick_params(axis='y',labelsize=18)
axs[2].tick_params(axis='x',labelsize=0)
axs[2].tick_params(axis='y',labelsize=18)
axs[3].tick_params(axis='x',labelsize=18)
axs[3].tick_params(axis='y',labelsize=18)

axs[0].set_xticks(x[::20])
axs[1].set_xticks(x[::20])
axs[2].set_xticks(x[::20])
axs[3].set_xticks(x[::20])
axs[3].set_xticklabels(x[::20])

plt.xlabel('Residue Index',fontsize=24)
plt.ylabel('Surface Area (nm$^2$)',fontsize=24,loc='top')
axs[3].yaxis.set_label_coords(-.05,3.5)
plt.subplots_adjust(hspace=0)

axs[1].axvspan(112,118,color='deepskyblue',alpha=0.5, lw=0)
axs[2].axvspan(112,124,color='deepskyblue',alpha=0.5, lw=0)
axs[3].axvspan(112,131,color='deepskyblue',alpha=0.5, lw=0)


plt.savefig('fig.png')
