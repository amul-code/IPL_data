import csv
import time
import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def third_task(year):
    match_id = []
    with open('matches.csv', newline='') as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        season_list = []
        for season in matches_reader:
            if season['season'] == year:
                match_id.append(season['id'])
            else:
                continue
        #print(list(list_of_id))

    extra_run_dic={}
    tmp_row=[]
    with open('deliveries.csv', newline='') as delivery_csv:
        delivery_reader = csv.reader(delivery_csv)
        list_of_csv_rows = list(delivery_reader)
#        print(list_of_csv_rows)
        for row in list_of_csv_rows:
            if row[0] in match_id:
                extra_run_dic.setdefault(row[2], 0)
                extra_run_dic[row[2]] = extra_run_dic[row[2]] + int(row[16])

            else:
                continue

        x = [i for i in list(extra_run_dic.keys())]
        y = [int(i) for i in list(extra_run_dic.values())]
        plt.xlabel('teams')
        plt.ylabel('matches won')
        pprint.pprint(extra_run_dic)
        plt.xticks(rotation=90)
        plt.plot(x, y)
        plt.show()

third_task('2016')
