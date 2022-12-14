import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context("talk")

q0=np.loadtxt('/mnt/home/jlindsay/ceph/elf3prd/hcg/analysis/contact/0q/290K/x.pc1')
q7=np.loadtxt('/mnt/home/jlindsay/ceph/elf3prd/hcg/analysis/contact/7q/290K/x.pc1')
q13=np.loadtxt('/mnt/home/jlindsay/ceph/elf3prd/hcg/analysis/contact/13q/290K/x.pc1')
q19=np.loadtxt('/mnt/home/jlindsay/ceph/elf3prd/hcg/analysis/contact/19q/290K/x.pc1')

hq0=np.loadtxt('0q')
hq7=np.loadtxt('7q')
hq13=np.loadtxt('13q')
hq19=np.loadtxt('19q')

fig, axs = plt.subplots(1,2,figsize=(7,1.75), dpi=300)
#plt.subplots_adjust(hspace=0)
axs[0].plot(q0, color='blue')
axs[0].plot(-q7, color='cyan')
axs[0].plot(q13, color='darkblue')
axs[0].plot(q19, color='skyblue')
axs[1].plot(hq0,color='red')
axs[1].plot(hq7,color='darkred')
axs[1].plot(hq13,color='orange')
axs[1].plot(-hq19,color='magenta')
axs[1].yaxis.tick_right()

axs[0].set_ylim([-.3,.6])
axs[1].set_ylim([-.3,.6])

axs[0].text(s='290K',x=1750,y=.35,fontsize=22)
axs[1].text(s='415K',x=1750,y=.35,fontsize=22)


x=range(186)
axs[0].tick_params(axis='x')
axs[0].tick_params(axis='y')
axs[1].tick_params(axis='x')
axs[1].tick_params(axis='y')

#axs[0,0].set_xticks([0,500,1000,1500,2000,2500])
#axs[1,0].set_xticks([0,500,1000,1500,2000,2500])
#axs[2,0].set_xticks([0,500,1000,1500,2000,2500])
#axs[3,0].set_xticks([0,500,1000,1500,2000,2500])
#axs[3,0].set_xticklabels([0,500,1000,1500,2000,2500])

axs[0].set_xlim(1200,2200)
axs[1].set_xlim(1200,2200)

#axs[3,1].set_xticks([1400,1800,2200])
#axs[3,1].set_xticklabels(['1400','1800','2200'])

axs[0].set_xticks([1500,2000])
axs[1].set_xticks([1500,2000])
axs[0].set_yticks([-.3,0,0.3,0.6])
axs[1].set_yticks([-.3,0,0.3,0.6])

axs[0].set_ylabel("PC1",labelpad=.5)
axs[0].set_xlabel("Contact Index")
axs[0].xaxis.set_label_coords(.95, -.3)
axs[0].yaxis.set_label_coords(-.2,.5)
#axs[0,0].get_xaxis().set_visible(False)
#axs[1,0].get_xaxis().set_visible(False)
#axs[2,0].get_xaxis().set_visible(False)

#axs[3,0].text(2000, -.6, 'Contact Index', ha='center', va='center',fontsize=22)
#axs[2,0].text(775,.7, 'PC1', ha='center', va='center',fontsize=22,rotation=90)
#axs[3,0].yaxis.set_label_coords(-.1,2.25)
plt.subplots_adjust(hspace=0,wspace=0)

#axs[1].axvspan(112,118,color='deepskyblue',alpha=0.5, lw=0)
#axs[2].axvspan(112,124,color='deepskyblue',alpha=0.5, lw=0)
#axs[3].axvspan(112,131,color='deepskyblue',alpha=0.5, lw=0)


plt.savefig('fig.png',bbox_inches='tight')
