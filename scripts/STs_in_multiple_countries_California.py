#!/usr/bin/env python3
import os
import sys
import argparse
from collections import Counter
from collections import defaultdict
from datetime import date
PARSER = argparse.ArgumentParser(
    prog="STs_in_multiple_countries.py",
    description="Prepare summary for STs in multiple countries")
PARSER.add_argument("Novel_STs", type=str, help="Novel STs list")
PARSER.add_argument("GNUVID_report", type=str, help="GNUVID strain report")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
#############################
INPUT_GNUVID_report2 = open(ARGS.Novel_STs,'r')
INPUT_GNUVID_report2.readline()
period_dict = {}
Novel_STs_list = []
for line in INPUT_GNUVID_report2:
    line = line.rstrip()
    line_list = line.split('\t')
    Novel_STs = line_list[4:]
    for i in Novel_STs:
        period_dict[i[2:]] = line_list[0]
        Novel_STs_list.append(i[2:])
#############################
INPUT_GNUVID_report = open(ARGS.GNUVID_report,'r')
header_line = INPUT_GNUVID_report.readline().rstrip()
Output_obj = open('STs_multiple_countries_ordered_CA_2_countries.txt', "w")
Output_obj2 = open('STs_multiple_countries_ordered_CA_all.txt', "w")
#Output_obj = open('STs_multiple_regions_ordered.txt', "w")
ST_country_dict = defaultdict(list)
ST_CC = {}
ST_dates = defaultdict(list)
CA_ST_dates = defaultdict(list)
for line in INPUT_GNUVID_report:
    line = line.rstrip()
    line_list = line.split('\t')
    country = line_list[2]
    row_date = line_list[1]
    #country = line_list[3]#region
    Strain_ST = line_list[-2]
    ST_CC[Strain_ST] = line_list[-1]
    ST_country_dict[Strain_ST].append(country)
    ST_dates[Strain_ST].append(row_date)
    if '/USA/CA' in line_list[0]:
        CA_ST_dates[Strain_ST].append(row_date)
print(len(CA_ST_dates))
counter = 0
STs_successful = []
for record in Novel_STs_list:
    countries_list = ST_country_dict[record]
    countries_count = len(set(ST_country_dict[record]))
    if countries_count >= 2:
        STs_successful.append(record)
#STs_successful_sorted = sorted(STs_successful, key = lambda x: x[1],reverse=True)
#print(STs_successful_sorted)
header = 'ST\tCC\tPeriod\tNumber of countries\tNumber of isolates\tNumber of isolates CA\tFirst_seen\tCA_date\tOrigin\tdays\tCountries\n'
Output_obj.write(header)
Output_obj2.write(header)
for j in STs_successful:
    new_list = []
    countries_list = ST_country_dict[j]
    isolates_count = len(countries_list)
    countries_count = len(set(countries_list))
    CC = ST_CC[j]
    ST_date = ST_dates[j]
    CA_date = CA_ST_dates[j]
    ST_period = period_dict[j]
    isolates_count_CA = len(CA_date)
    dates = [ST_date[0], CA_date[0]]
    sorted_dates = sorted(dates)
    if len(set(dates)) == 1:
        origin = 'CA'
        days = '0'
    elif sorted_dates.index(CA_date[0]) == 0:
        origin = 'CA'
        CA_date_l = [int(x) for x in sorted_dates[0].split('-')]
        other_date_l = [int(x) for x in sorted_dates[1].split('-')]
        days = str((date(CA_date_l[0],CA_date_l[1],CA_date_l[2])
                    - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
    else:
        origin = 'other'
        CA_date_l = [int(x) for x in sorted_dates[1].split('-')]
        other_date_l = [int(x) for x in sorted_dates[0].split('-')]
        days = str((date(CA_date_l[0],CA_date_l[1],CA_date_l[2])
                    - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
    for i in countries_list:
        if i not in new_list:
            new_list.append(i)
    Output_obj.write(j+'\t'+CC+'\t'+ST_period+'\t'+str(countries_count)+'\t'
    +str(isolates_count) +'\t'+str(isolates_count_CA)+'\t' +ST_date[0]+'\t'+CA_date[0]+'\t'
    +origin+'\t'+days+'\t'+'\t'.join(new_list)+'\n')
    counter +=1
    #print(record)
    #print(record,'\t',set(ST_country_dict[record]))
print(counter)
for nov_ST in Novel_STs_list:
    new_list = []
    countries_list = ST_country_dict[nov_ST]
    isolates_count = len(countries_list)
    countries_count = len(set(countries_list))
    CC = ST_CC[nov_ST]
    ST_date = ST_dates[nov_ST]
    CA_date = CA_ST_dates[nov_ST]
    ST_period = period_dict[nov_ST]
    isolates_count_CA = len(CA_date)
    dates = [ST_date[0], CA_date[0]]
    sorted_dates = sorted(dates)
    if len(set(dates)) == 1:
        origin = 'CA'
        days = '0'
    elif sorted_dates.index(CA_date[0]) == 0:
        origin = 'CA'
        CA_date_l = [int(x) for x in sorted_dates[0].split('-')]
        other_date_l = [int(x) for x in sorted_dates[1].split('-')]
        days = str((date(CA_date_l[0],CA_date_l[1],CA_date_l[2])
                    - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
    else:
        origin = 'other'
        CA_date_l = [int(x) for x in sorted_dates[1].split('-')]
        other_date_l = [int(x) for x in sorted_dates[0].split('-')]
        days = str((date(CA_date_l[0],CA_date_l[1],CA_date_l[2])
                    - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
    for i in countries_list:
        if i not in new_list:
            new_list.append(i)
    Output_obj2.write(nov_ST+'\t'+CC+'\t'+ST_period+'\t'+str(countries_count)+'\t'
    +str(isolates_count) +'\t'+str(isolates_count_CA)+'\t' +ST_date[0]+'\t'+CA_date[0]+'\t'
    +origin+'\t'+days+'\t'+'\t'.join(new_list)+'\n')
