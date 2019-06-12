import pprint
import csv
import time
from matplotlib import pyplot as plt
import numpy as np
def first_task():
    start_time = time.time()
    with open('matches.csv', newline = '') as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        season_wins={}
        for row in matches_reader:
            season_wins.setdefault(row['season'], 0)
            season_wins[row['season']] = season_wins[row['season']] + 1
    x = [int(key) for key in list(season_wins.keys())]
    y = [int(value) for value in list(season_wins.values())]
    plt.xlabel('years')
    plt.ylabel('matches won')
    pprint.pprint(season_wins)

    plt.plot(x,y)
    plt.show()
    print("timetaken:"+str((time.time()-start_time)*1000))
first_task()
