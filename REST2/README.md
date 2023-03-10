# REST2 Figures
## Fig 2:
## wt_mut_helix_per_res.py
Plot of 7Q and 0Q helicity, including all temperatures. Creates two subplots vertically stacked and includes 'H1', 'H2', & 'H3' labels on helices of interest. Highlights Haro, HN1, HN2, HN3, F96 and 3 polyQ tracts.

## rg_split.py
Plots the RG of the first 100 residues and athe last 73 residues as histograms. Top panel is WT REST, bottom panel is F96A.

## Fig 3:
## dist_f96_haro.py
Histograms of F96-Haro minimum distance for each temperature condition. WT REST2.

## kde_plot_haro_rg.py
Script used to create Figs 3B and 3C. This script only creates one plot and must be modified and rerun to create the whole figure.

## 1stpeak.py
Plots the max value of the first peak of the rdf curve for each residue. 7Q REST2 at 290K is blue and 405K is red. 
Haro highlighted in yellow, polyQ in blue. Does not calculate peak heights, those must be provided as input data.

## Fig. 5:
## ss_0Q_helix_per_res.py
Helix propensity for 0Q REST2 trajectories at 4 temperatures. Haro is highlighted in yellow, polyQs in blue and deleted polyQ represented by a dashed blue line.
