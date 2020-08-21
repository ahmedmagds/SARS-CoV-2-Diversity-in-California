#!/usr/bin/env python3
import os
import sys
import argparse
from collections import Counter
from collections import defaultdict
PARSER = argparse.ArgumentParser(
    prog="stacked_area_graph.py",
    description="extract the top number of STs and CCs as percentanges",
)
PARSER.add_argument(
    "-t",
    "--top", type=int, help="top STs and CCs in a dataset, others is the last group [Default: 10]"
)
PARSER.add_argument(
    "output", type=str, help="output prefix name"
)
PARSER.add_argument(
    "ST_GNUVID_report", type=str, help="ST GNUVID tab report"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
##########################
GNUVID_obj = open(ARGS.ST_GNUVID_report, 'r')
output_obj = open(ARGS.output, 'w')
if ARGS.top:
    top_cutoff = ARGS.top
else:
    top_cutoff = 10
##################################
counter = 0
GNUVID_obj.readline()
ST_list = []
CC_list = []
for line in GNUVID_obj:
    counter += 1
    line = line.rstrip()
    line_list = line.split('\t')
    Strain_CC = line_list[-1]
    Strain_ST = line_list[-2]
    ST_list.append(Strain_ST)
    CC_list.append(Strain_CC)

ST_C = Counter(ST_list)
most_occur_ST = ST_C.most_common()
CC_C = Counter(CC_list)
most_occur_CC = CC_C.most_common()
print(CC_C)
output_obj.write('CC\tCount\n')
output_obj.write(
    "\n".join("{}\t{}".format(x[0], x[1]) for x in most_occur_CC)
)
output_obj.write('\n#################\n')
output_obj.write('ST\tCount\n')
output_obj.write(
    "\n".join("{}\t{}".format(x[0], x[1]) for x in most_occur_ST)
)
################################
'''continents = ['Europe','North America', 'South America', 'Africa', 'Oceania','Asia', 'Middle East']
CCs = ['277', '323', '274', '275', '4', '76', '863', '403', '324', '552', '900', '843']
Continents_Counts = defaultdict(list)
for CC in CCs:
    GNUVID_obj.seek(0)
    GNUVID_obj.readline()
    for line in GNUVID_obj:
        line = line.rstrip()
        line_list = line.split('\t')
        Strain_CC = line_list[-1]
        Continent = line_list[3]
        if Strain_CC == CC:
            Continents_Counts[Strain_CC].append(Continent)
for CC in CCs:
    output_obj.write('\tCC{}\n'.format(CC))
    for continent in continents:
        output_obj.write('{}\t{}\n'.format(continent,Continents_Counts[CC].count(continent)))
'''
