import pprint
import csv
from matplotlib import pyplot as plt
import numpy as np
def fourth_task(year):
    match_id = []
    runs = []
    deliverise = {}
    total_run= {}
    with open('matches.csv', newline ='') as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        with open('deliveries.csv', newline ='') as deliveries_csv:
            deliveries_reader = csv.DictReader(deliveries_csv)

            for row in matches_reader:
                if row['season'] == year:
                    match_id.append(row['id'])
                else:
                    continue
            total_ball = {}

            for i in deliveries_reader:
                temp = i["match_id"]
                if match_id.__contains__(temp):
                    temp2 = i['bowler']

                    if not temp2 in total_run:
                        total_ball[temp2] = 1
                        total_run[temp2] = int(i["total_runs"])
                    elif temp2 in total_run:
                        total_run[temp2] += int(i["total_runs"])
                        total_ball[temp2] = str(int(total_ball[temp2]) + 1)

            print(total_ball)
            print(total_run)
            economy = {}
            top_economy = {}

            for j in total_ball:
                economy[j] = float("{0:.2f}".format((total_run[j]/int(total_ball[j]))*6))
            print(economy)
            economy = sorted(economy.items(), key=lambda x: x[1])
            print(economy)
            top_economy =dict(economy[0:10])

            x = [i for i in top_economy.keys()]
            y = [i for i in top_economy.values()]
            plt.xlabel('bowler')
            plt.ylabel('economy')
            plt.xticks(rotation=90)
            plt.plot(x, y)
            plt.show()


fourth_task('2015')
