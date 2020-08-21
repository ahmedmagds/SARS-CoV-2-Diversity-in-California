#!/usr/bin/env python3
import os
import sys
import argparse
from collections import Counter
from collections import defaultdict
PARSER = argparse.ArgumentParser(
    prog="Alleles_collectors_curve.py",
    description="Prepare summary for collector's curve")
PARSER.add_argument(
    "-l",
    "--list",
    type=str,
    help="Files List to process in a specific date order",
)
PARSER.add_argument(
    "directory", type=str, help="Directory having the multiple GNUVID reports (time organized) files to analyze"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
############################
QUERY = ARGS.directory
QUERY_LIST = []
for file in os.listdir(QUERY):
    if file.endswith(".txt"):
        QUERY_LIST.append(QUERY + file)
print("You provided folder of {} GNUVID report files".format(len(QUERY_LIST)))
input_file_object = open(QUERY_LIST[0], 'r')
Genes = input_file_object.readline().split('\t')[4:15]
indices = [4,5,6,7,8,9,10,11,12,13,14]
input_file_object.close()
if ARGS.list:
    QUERY_LIST = []
    list_file_object = open(ARGS.list, 'r')
    for line in list_file_object:
        line = line.rstrip()
        QUERY_LIST.append(QUERY + line)
#Times = ['mid_Jan','end_Jan','mid_Feb','end_Feb','mid_Mar','end_Mar','mid_Apr',
#'end_Apr','mid_May','end_May','mid_June','end_June','mid_July']
Times = ['end_jan','Feb','mid_Mar','end_Mar','mid_Apr',
'end_Apr','mid_May','end_May_mid_June','end_June']
#####################
time_dict_raw = defaultdict(list)
time_dict_percent = defaultdict(list)
Output_obj = open('Allelic_diversity_California_results.txt', "w")
Output_obj2 = open('Novel_STs_California_results.txt', "w")
Output_obj2.write('Time_period\tNumber_of_Novel_STs\tNumber of circulating STs\tNovel_STs_percentage\tSTs\n')
All_STs = set()
for QUERYFILE in QUERY_LIST:
    counter = 0
    QUERYFILE_OBJECT = open(QUERYFILE, "r")
    QUERYFILE_OBJECT.readline()
    time_period = QUERYFILE.rsplit('/',1)[-1].split('California_')[-1].split('.txt')[0]
    Alleles_ST_numbers_dict = defaultdict(list)
    for Gene in Genes:
        Alleles_ST_numbers_dict[Gene]
    for line in QUERYFILE_OBJECT:
        counter += 1
        line = line.rstrip()
        line_list = line.split('\t')
        for Gene,Index in zip(Genes,indices):
            Alleles_ST_numbers_dict[Gene].append(int(line_list[Index]))
    #########Reporting############
    #print(time_period, '\t', counter)
    for record in Genes:
        period_alleles = Alleles_ST_numbers_dict[record]
        #time_dict_set[time_period].extend(period_alleles)
        time_dict_raw[time_period].append(str(len(set(period_alleles))))
        time_dict_percent[time_period].append('{:.2f}'.format(len(set(period_alleles))/counter))
    time_dict_raw[time_period].append(str(counter))
    time_dict_percent[time_period].append(str(counter))
    #capturing novel STs in each period
    period_STs = set(Alleles_ST_numbers_dict['ST'])
    Novel_STs = period_STs - All_STs
    Novel_STs_list = [('ST'+str(x)) for x in Novel_STs]
    All_STs = All_STs.union(period_STs)
    Novel_STs_percent = '{:.2f}'.format(len(Novel_STs)/len(period_STs))
    Output_obj2.write('{}\t{}\t{}\t{}\t{}\n'.format(time_period,len(Novel_STs),len(period_STs),Novel_STs_percent,'\t'.join(Novel_STs_list)))
print('\t','\t'.join(Genes),'\tTotal')
Output_obj.write('\t'+'\t'.join(Genes)+'\tTotal\n')
for period in Times:
    print(period,'\t','\t'.join(time_dict_raw[period]))
    Output_obj.write(period+'\t'+'\t'.join(time_dict_raw[period])+'\n')
print('########################')
Output_obj.write('########################\n')
print('\t','\t'.join(Genes),'\tTotal')
Output_obj.write('\t'+'\t'.join(Genes)+'\tTotal\n')
for period in Times:
    print(period,'\t','\t'.join(time_dict_percent[period]))
    Output_obj.write(period+'\t'+'\t'.join(time_dict_percent[period])+'\n')
#print(record,'\t',len(set(Alleles_ST_numbers_dict[record])))
