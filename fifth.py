import csv
def fifth(batsman):

    with open('deliveries.csv', newline ='') as deliveries_csv:
        deliveries_reader = csv.DictReader(deliveries_csv)
        six = 0
        four = 0
        for i in deliveries_reader:
            if i['batsman'] == batsman:
                if i['batsman_runs'] == '6':
                    six+=1
                if i['batsman_runs'] == '4':
                    four+=1
        print("player name: "+batsman)
        print("Total boundries: "+str(six+four))
        print("sixes: "+str(six))
        print("fours "+str(four))
fifth("V Kohli")





