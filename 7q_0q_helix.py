import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

q0_290=np.loadtxt('0q_HG290_norm')
q0_300=np.loadtxt('0q_HG300_norm')
q0_320=np.loadtxt('0q_HG320_norm')
q0_415=np.loadtxt('0q_HG415_norm')

q7_290=np.loadtxt('7q_HG290_norm')
q7_300=np.loadtxt('7q_HG300_norm')
q7_320=np.loadtxt('7q_HG320_norm')
q7_415=np.loadtxt('7q_HG415_norm')

#plt.plot(q0_290)
#plt.plot(q0_300)
fig, axs = plt.subplots(2,figsize=(9,6.5), dpi=300)
#fig = plt.figure(figsize=(8.5,6), dpi=300)
axs[0].plot(q7_290)
axs[0].plot(q7_300)
axs[0].plot(q7_320)
axs[0].plot(q7_415)
axs[1].plot(q0_290)
axs[1].plot(q0_300)
axs[1].plot(q0_320)
axs[1].plot(q0_415)
axs[0].set_xlim([0,173])
axs[1].set_xlim([0,173])
axs[0].set_ylim([0.001,0.34])
axs[1].set_ylim([0.001,0.34])
axs[0].text(s='7Q',x=148,y=.22,fontsize=24)
axs[1].text(s='0Q',x=148,y=.22,fontsize=24)

axs[0].text(s='H1',x=90,y=.08,fontsize=16,color='red')
axs[0].text(s='H2',x=95,y=.15,fontsize=16,color='green')
axs[0].text(s='H3',x=100,y=.25,fontsize=16,color='blue')

x=range(173)
axs[0].set_xticks(x[::20])
axs[0].tick_params(axis='x',labelsize=0)
axs[0].tick_params(axis='y',labelsize=18)
axs[1].tick_params(axis='both',labelsize=18)

axs[0].set_xticklabels(x[::20])
axs[1].set_xticks(x[::20])
axs[1].set_xticklabels(x[::20])
axs[0].legend(['290K','300K','320K','415K'],loc='upper left',fontsize=14)
plt.xlabel('Residue Index',fontsize=24)
plt.ylabel('Ratio',fontsize=24,loc='top')
plt.subplots_adjust(hspace=0)

plt.savefig('fig.png')
