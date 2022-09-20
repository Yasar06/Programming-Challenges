

            

import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0]
        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0]
        #[points,wins,draws,losses,goal difference]
        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
            dictionary[home][2] += 1
            dictionary[away][2] += 1
            
        if winner == "H":
            dictionary[home][0] += 3
            dictionary[home][1] += 1
            dictionary[away][3] += 1

            
        if winner == "A":
            dictionary[away][0] += 3
            dictionary[away][1] += 1
            dictionary[home][3] += 1

        
        #goal difference also needs to be calculated
        dictionary[home][4] = dictionary[home][4] + int(homegoals) - int(awaygoals)
        #goal difference for away team here
        dictionary[away][4] = dictionary[away][4] + int(awaygoals) - int(homegoals)
        #after this is done, you'll have all of the points and goal differences for each team
    dictionary = sorted(dictionary.items(), key=lambda e: e[1][0])
    dictionary.reverse()

    return dictionary


 
def table(rows):
    print("Name:\t\t\tPoints:\t\t\tWins:\t\t\tDraws:\t\t\tLosses:\t\t\tGoal Difference:")
    for row in rows:
        print(f"{row[0]:<25}{row[1][0]:<25}{row[1][1]:<23}{row[1][2]:<25}{row[1][3]:<25}{row[1][4]}")
    


if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    table(results)
    

    
    #instead of printing, you'll need to sort function to sort...the league - this should help - https://stackoverflow.com/questions/1217251/sorting-a-dictionary-with-lists-as-values-according-to-an-element-from-the-list
    #then print the league table in a pretty output function
