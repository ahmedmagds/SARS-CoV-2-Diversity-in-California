# SARS-CoV-2-Diversity-in-California

**Ahmed M. Moustafa** and **Paul J. Planet**

---

This repository contains the data files, scripts and workflows necessary to reproduce the analyses and figures presented in Moustafa AM and Planet PJ (TBD). Some of the scripts may need some adjustment depending on the local setup. The analysis is based on using the 940 Californian high coverage genomes included in the recent database release (07/17/2020)  from the [GNUVID v1.3](https://github.com/ahmedmagds/GNUVID) tool.

Because of the GISAID [terms of use](https://www.gisaid.org/registration/terms-of-use/), genomic sequences will not be shared in this repository. However, we make the GISAID accessions available along with all associated results.

A table of acknowledgements for the 25594 GISAID SARS-CoV-2 sequences used is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_06_17_00.xls
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_07_21_17.pdf

## Dependencies
Python3

## Definitions
- Relative Abundance: In Figure 1A, Relative abundance is the ratio is the number of genomes belonging a certain CC (lineage) divided by the total number of genomes in a certain time window (e.g. January). For better visualization, We only included the top 10 abundant CCs (more than 10 genomes) in Figure 1A which represent 92% of the Californian genomes that were assigned a CC.
- Novel ST: a virus sequence type (a haplotype that differ by at least one nucleotide in any of the 10 ORFs of SARS-CoV-2) that is seen for the first time in a certain geographical region (e.g. California). This could be a result of new introduction or a local emerging ST.
- Introduced ST: A novel ST that is introduced from outside the geographical region (e.g. California). In this case, other US State or from another country. Our rule is appearing in another region before California by 10 days.
- Introduced USA: A special case of Introduced ST that focus on the STs that were introduced from other US States and are not present anywhere else except USA.

## Data

- [`California_Allelic_diversity/`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/California_Allelic_diversity/): A folder having nine GNUVID reports for the genomes sequenced in nine intervals (January, February, mid-March, end-March, mid-April, end-April, mid-May, end-May to mid June, end-June). Mid and end means genomes sequenced 1st-15th and 16th-last day of the month, respectively. These 9 files have 940 Californian high coverage genomes. The 9 files will be used for producing Figure 1A and 1B.
- [`California_Allelic_diversity_order_list.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/California_Allelic_diversity_order_list.txt): A text file ordering the inputs by month.
- [`GNUVID_07172020_DB_isolates_report_raw.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/GNUVID_07172020_DB_isolates_report_raw.txt): GNUVID DB typing report for 25,594 genomes included in the recent database release (07/17/2020)  from the [GNUVID v1.3](https://github.com/ahmedmagds/GNUVID) tool.
- [`Novel_STs_California_results.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/Novel_STs_California_results.txt): This file is an output of Alleles_collectors_curve.py and has the novel STs (virus haplotyopes) at each of the nine time intervals. The fourth column in this file is the Novel STs/Circulating STs ratio used in Figure 1B. The second column is used a denominator for the Introduced STs/Novel STs. It is also used as an input for STs_in_multiple_countries_California.py.
- [`Allelic_diversity_California_results.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/Allelic_diversity_California_results.txt): This file is an output of Alleles_collectors_curve.py and the second to last column in the ratios is the Circulating STs/Genomes ratio used in Figure 1B.
- [`California_isolates_stack_area.xlsx`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/California_isolates_stack_area.xlsx):
An excel file combining all the results from stacked_area_graph.py. The relative abundance for the selected 10 CCs for Figure 1A are in sheet all in red.
- [`STs_multiple_countries_ordered_CA_all.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/STs_multiple_countries_ordered_CA_all.txt): An output file from STs_in_multiple_countries_California.py script.
- [`STs_multiple_countries_ordered_CA_2_countries.txt`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/STs_multiple_countries_ordered_CA_2_countries.txt): An output file from STs_in_multiple_countries_California.py script.
- [`STs_multiple_countries_ordered_CA_2_countries_USA.xlsx`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/STs_multiple_countries_ordered_CA_2_countries_USA.xlsx): Filtering this file in excel will show the 26 ST introductions for all time period.

## Commands (Figure 1A)

**Use the following command with each file in the [`California_Allelic_diversity/`](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/California_Allelic_diversity/) folder by just replacing the file name and change the output name**

```
stacked_area_graph.py California_end_jan_report.txt California_end_jan.txt
```

## Commands (Figure 1B)

```
Alleles_collectors_curve.py -l California_Allelic_diversity_order_list.txt California_Allelic_diversity/
STs_in_multiple_countries_California.py Novel_STs_California_results.txt GNUVID_07172020_DB_isolates_report_raw.txt
```

## Figures

Figures were produced in the Graphpad Prism 7 using these two files:

- Figure 1A: [Figure_1A.txt](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/Figure_1A.txt).
- Figure 1B: [Figure_1B.txt](https://github.com/ahmedmagds/SARS-CoV-2-Diversity-in-California/blob/master/data/Figure_1B.txt).
