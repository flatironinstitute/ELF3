# ELF3 Python Scripts
A place to store code used to generate figures.

## Fig 1:
## ss_7q_0q_helix.py
Plots helix propensity of HCG 7Q ensembles at all 4 temperatures. Haro is shaded yellow, polyQ tracts are shaded blue, F96 is marked with a dashed red line, and HN1, HN2, HN3, and HC1 are labeled.

## hcg_pc1_2col.py
Plots E-PC1 of HCG 0Q/7Q/13Q/19Q at 290K (left) and 415K (right). Code does not align data, data files must be pre-processed to achieve this.  

## Fig 2:
## wt_mut_helix_per_res.py
Plot of 7Q and 0Q helicity, including all temperatures. Creates two subplots vertically stacked and includes 'H1', 'H2', & 'H3' labels on helices of interest. Highlights Haro, HN1, HN2, HN3, F96 and 3 polyQ tracts.

## rg_split.py
Plots the RG of the first 100 residues and athe last 73 residues as histograms. Top panel is WT REST, bottom panel is F96A.

## Fig 3:
## dist_f96_haro.py
Histograms of F96-Haro minimum distance for each temperature condition. WT REST2.

## hcg_ipca.py
I-PCA PC1 and PC2 plots of all HCG ensmbles. 8 subplots in a 2 column x 4 row configuration.

## hcg_sasa.py
Solvent accessible surface area for all polyQ lengths. 4 row x 1 column, only 290K plotted because all temperatures are essentially identical. 
PolyQ region is shaded blue.

## polyq_dist.py
Plot of 7Q HCG Ca-Ca distance as a function of temperature. Four histograms on one plot.

## rg.py
The gyradius of REST2 WT and F96A mutant as a histogram on one plot. Alpha set at 0.5 for readability.

## rg_hcg.py
Histogram of 7Q temperature-dependent gyradius. 
