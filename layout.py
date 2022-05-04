# Parent class
import csv

with open('Trivia Questions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    counter = 0
    lst_questions = [[],[],[]]
    for line in csv_reader:
        lst_questions[counter // 10].append((line[0], line[1], line[2], line[3], line[4], line[5]))
        counter += 1

class Game:    
    score = 100 
    answer = str
    Game_type = str  

# child class (category one)
class Geo(Game): 
    Game_type = "Monument Geography"
    lst1 = lst_questions[0]

# child class (category two)    
class War(Game): 
    Game_type = "Wars"
    lst2 = lst_questions[1]
    
    
# child class (category third)    
class Lead(Game): 
    Game_type = "Historical Leaders"
    lst3 = lst_questions[2]