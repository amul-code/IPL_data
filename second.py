import time
import csv
import time
import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict
def second_task():
    start_time = time.time()
    list_of_matches_won = []
    list_of_season = []
    list_of_winner = []
    season_list = []
    with open('matches.csv', newline='') as matches_csv:

        matches_reader = csv.DictReader(matches_csv)
        for row in matches_reader:
            list_of_season.append(row['season'])
            list_of_winner.append(row['winner'])
            if not row['season'] in season_list:
              season_list.append(row['season'])
              season_list.sort()
        res = defaultdict(list)
        for season, winner in zip(list_of_season,list_of_winner):
            res[season].append(winner)
        new_dict = {}
        for i in  res:
            temp = {}
            for j in res[i]:
                temp[j] = res[i].count(j)
            new_dict[i] = temp


        unique_list_of_winner = []
        for i in list_of_winner:
            if not i in unique_list_of_winner:
                unique_list_of_winner.append(i)
        #print(unique_list_of_winner)

        X_AXIS = (unique_list_of_winner)
        #print(X_AXIS)
        index = pd.Index(X_AXIS, name='team')
        data = new_dict
        print(data)
        print(type(data))
        df = pd.DataFrame(data, index=index)
        ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
        ax.set_ylabel('years')
        plt.xticks(rotation = 90)
        plt.savefig('stacked.png')
        print("timetaken:"+str((time.time()-start_time)*1000))
        plt.show()



second_task()
