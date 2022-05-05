from colorama import Fore
import layout 
from pymongo import MongoClient
client = MongoClient()

# Setting db_games to our trivia db on MongoDB
db_trivia = client.trivia

games = db_trivia.games


def main():
# Main Menu    
    print(Fore.LIGHTMAGENTA_EX + "Hello and welcome to the Trivia Game\n")
    print(Fore.LIGHTMAGENTA_EX + "Here you have a choice of three categories for questions. Please select 1-5 to start\n" + "         -----------------------------") 
    print(Fore.LIGHTMAGENTA_EX + "\t | 1) Monuments Geography    |\n" + "\t | 2) Wars                   |\n" + "\t | 3) Historical Leaders     |\n" + "\t | 4) See all previous Games |\n" + "         -----------------------------")
    
# Sees if users enteres 1-4      
    while True:
        try:
            print("Enter 5 to exit \n")
            category = (input(">>> "))
            break  
        except ValueError:
            print("Oh no! You must enter a valid number! Try again!")

# loads object 
    if category == "1":
        Ge0()
    elif category == "2":
        Warz()
    elif category == "3":
        Leadz()    
    elif category == "4":
        ck_savez()
    elif category == "5":      
        exit()
    else:
        main()

#saves
def ck_savez():
    results = str(games.find_one())
    lst_gmz = []
    gm_data = games.find()
    for line in gm_data:
        lst_gmz.append(line)
    print("\u0332".join("SavedGames""\n"))    
    for x in lst_gmz:   
        print("\u0332".join(" GameType:"),x["type"],"\n","\u0332".join("Username:"),x["user"],"\n", "\u0332".join("Score:"),x["score"],"\n","\u0332".join("Game:"),x["games"],"\n",) 
    print("\nIf you want to change your username or delete a game enter 1 or 2 and/or 3 to exit: ")
    us_input = input(">>> ")
    while True:
        try:
            if us_input == "1":
                old_user = input("Enter your old username >>> ")
                new_user = input("Enter a new username >>> ")
                if results == "None": 
                    raise ValueError
                elif not old_user == x["user"]: 
                    raise ValueError   
                else:     
                    for x in lst_gmz:
                        games.update_one({"user": old_user}, {"$set": {"user" : new_user}})   
                        print("\u0332".join(" GameType:"),x["type"],"\n","\u0332".join("Username:"),x["user"],"\n", "\u0332".join("Score:"),x["score"],"\n","\u0332".join("Game:"),x["games"],"\n",) 
                        print("Update Successfully")
                        main()
            elif us_input == "2":    
                    game_num = int(input("\nTo delete a game, please enter a game number:\n>>> "))
                    if results == "None": 
                        raise ValueError
                    else:    
                        games.delete_one({"games" : game_num})  
                        print("\u0332".join(" GameType:"),x["type"],"\n","\u0332".join("Username:"),x["user"],"\n", "\u0332".join("Score:"),x["score"],"\n","\u0332".join("Game:"),x["games"],"\n",) 
                        print("\nGame Successfully deleted!")  
                        main()     
            elif us_input == "3":
                main()
            else: 
                raise ValueError 
        except ValueError: 
            print("Invalid Input")  
            ck_savez()      


# Starts Game under first category 
def Ge0():
    gm_type = layout.Geo().Game_type 
    score = layout.Geo().score
    cat1 = layout.Geo().lst1  
    i = 0    
    for q in cat1: 
        while True:
            try:
                while i < len(cat1):    
                    print(cat1[i][0], "\n", cat1[i][1], "\n", cat1[i][2], "\n", cat1[i][3], "\n", cat1[i][4], "\n")
                    answer = input(">>> ")
                    if not answer == "a" and not answer == "b" and not answer == "c" and not answer == "d": 
                        raise ValueError("Please enter a correct letter depending on your answer (a,b,c or d)")    
                    else: 
                        if not answer == cat1[i][5]:
                            score = score - 10 
                    i += 1            
                    if i == len(cat1):
                        print(" You Finished The Trivia Game!!! \n", "Your Score in ", gm_type , " is ", score) 
                        geo_gm(score) 
                        exit()                                                 
            except ValueError:
                print("Please enter a correct letter depending on your answer (a,b,c or d)")   

def geo_gm(score):
    user_name = input("Input your username to save the game >>> ")
    results = str(games.find_one())
    if results == "None":
        new_game = {
            "type" : "Monument Geography",
            "user" : user_name,
            "score" : score,
            "games" : 1 
        }
        games.insert_one(new_game)
        main()
    else:
        gm = games.aggregate([{"$group" : { "_id" : "null", "games" : {"$max": "$games"}}}]) 
        num_games = gm.next()["games"] 
        new_game = {
            "type" : "Monument Geography",
            "user" : user_name,
            "score" : score,
            "games" : num_games + 1 
        }
        games.insert_one(new_game)
        main()                 

                 
# Starts Game under second category 
def Warz():
    gm_type = layout.War().Game_type
    score = layout.War().score
    cat2 = layout.War().lst2   
    i = 0     
    for q in cat2: 
        while True:
            try:  
               while i < len(cat2):    
                    print(cat2[i][0], "\n", cat2[i][1], "\n", cat2[i][2], "\n", cat2[i][3], "\n", cat2[i][4], "\n")
                    answer = input(">>> ")
                    if not answer == "a" and not answer == "b" and not answer == "c" and not answer == "d": 
                        raise ValueError("Please enter a correct letter depending on your answer (a,b,c or d)")    
                    else: 
                        if not answer == cat2[i][5]:
                            score = score - 10 
                    i += 1            
                    if i == len(cat2):
                        print(" You Finished The Trivia Game!!! \n", "Your Score in ", gm_type , " is ", score) 
                        warz_gm(score) 
                        exit() 
                    else:
                        pass         
            except ValueError:
                print("Please enter a correct letter depending on your answer (a,b,c or d)")  

def warz_gm(score):
    user_name = input("Input your username to save the game >>> ")
    results = str(games.find_one())
    if results == "None":
        new_game = {
            "type" : "Wars",
            "user" : user_name,
            "score" : score,
            "games" : 1 
        }
        games.insert_one(new_game)
        main()
    else: 
        gm = games.aggregate([{"$group" : { "_id" : "null", "games" : {"$max": "$games"}}}])      
        num_games = gm.next()["games"]
        new_game = {
            "type" : "Wars",
            "user" : user_name,
            "score" : score,
            "games" : num_games + 1 
        }
        games.insert_one(new_game)
        main()
                    

# Starts Game under third category 
def Leadz():
    gm_type = layout.Lead().Game_type
    score = layout.Lead().score
    cat3 = layout.Lead().lst3
    i = 0     
    for q in cat3: 
        while True:
            try:    
                print(cat3[i][0], "\n", cat3[i][1], "\n", cat3[i][2], "\n", cat3[i][3], "\n", cat3[i][4], "\n")
                answer = input(">>> ")
                if not answer == "a" and not answer == "b" and not answer == "c" and not answer == "d": 
                    raise ValueError("Please enter a correct letter depending on your answer (a,b,c or d)")    
                else: 
                    if not answer == cat3[i][5]:
                        score = score - 10 
                    else:
                        pass
                    i += 1 
                    if  i == len(cat3):
                        print("You Finished The Trivia Game!!! \n", "Your Score in ", gm_type , " is ", score) 
                        leads_gm(score)  
                    else:
                        pass         
            except ValueError:
                print("Please enter a correct letter depending on your answer (a,b,c or d)")    

def leads_gm(score):
    user_name = input("Input your username to save the game >>> ")
    results = str(games.find_one())
    if results == "None":
        new_game = {
            "type" : "Historical Leaders",
            "user" : user_name,
            "score" : score,
            "games" : 1 
        }
        games.insert_one(new_game)
        main()
    else: 
        gm = games.aggregate([{"$group" : { "_id" : "null", "games" : {"$max": "$games"}}}])      
        num_games = gm.next()["games"]
        new_game = {
            "type" : "Historical Leaders",
            "user" : user_name,
            "score" : score,
            "games" : num_games + 1 
        }
        games.insert_one(new_game)
        main()                



if __name__ == '__main__':
    main()