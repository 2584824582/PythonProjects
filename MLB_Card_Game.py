import random, time, os
from datetime import datetime
#Array of teams
Teams = [
    "Arizona Diamondbacks",
    "Atlanta Braves",
    "Baltimore Orioles",
    "Boston Red Sox",
    "Chicago Cubs",
    "Chicago White Sox",
    "Cincinnati Reds",
    "Cleveland Guardians",
    "Colorado Rockies",
    "Detroit Tigers",
    "Houston Astros",
    "Kansas City Royals",
    "Los Angeles Angels",
    "Los Angeles Dodgers",
    "Miami Marlins",
    "Milwaukee Brewers",
    "Minnesota Twins",
    "New York Mets",
    "New York Yankees",
    "Oakland Athletics",
    "Philadelphia Phillies",
    "Pittsburgh Pirates",
    "San Diego Padres",
    "San Francisco Giants",
    "Seattle Mariners",
    "St. Louis Cardinals",
    "Tampa Bay Rays",
    "Texas Rangers",
    "Toronto Blue Jays",
    "Washington Nationals"
]
#Array of used teams
Players = []
#Write Score to file
def writeScore(score):
    # score should be an integer
    with open('score.txt', 'w') as file:
        file.write(str(score))

#Read Score from file
def readScore():
    if not os.path.exists('score.txt'):
        return 0
    with open('score.txt', 'r') as file:
        text = file.read().strip()
        try:
            return int(text)
        except ValueError:
            return 0

#Write Currency to file
def writeCurrency(amount):
    # amount should be an integer
    with open('money.txt', 'w') as file:
        file.write(str(amount))

#Read Currency from file
def readCurrency():
    if not os.path.exists('money.txt'):
        return 0
    with open('money.txt', 'r') as file:
        text = file.read().strip()
        try:
            return int(text)
        except ValueError:
            return 0

#Bet Menu
def bet():
    global betAmount, multiplier, current, starting
    # start with current currency from file
    current = readCurrency()
    starting = current

    betAmount = int(input("How much currency would you like to bet? "))
    if betAmount > current:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        menu()
    else:
        current -= betAmount
        writeCurrency(current)
        time.sleep(1)

    odds = input("What are the odds for your team to win? (e.g. +150, -200) ")
    if odds.startswith('+'):
        multiplier = int(odds[1:]) / 100
    elif odds.startswith('-'):
        multiplier = 100 / int(odds[1:])
    else:
        print("Invalid odds format. Please try again.")
        time.sleep(2)
        menu()

    time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

#Check Bet Menu
def checkBets():
    global betAmount, multiplier, current, starting
    winorloss = int(input("Did your team win?\nType '1' for yes and '0' for no. "))
    if winorloss == 1:
        winnings = int(betAmount * multiplier)
        current += winnings
        writeCurrency(current)
        print(f"You won {winnings} currency from your bet!\n")
    elif winorloss == 0:
        print(f"You lost {betAmount} currency from your bet.\n")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        menu()
    menu()

#Points Menu
def points():
    # start with current score from file
    current = readScore()
    starting = current

    HomeRuns = int(input("How many Home Runs did your players hit today? "))
    current += HomeRuns
    writeScore(current)
    time.sleep(1)

    RBIs = int(input("How many RBIs did your players have today? "))
    current += RBIs
    writeScore(current)
    time.sleep(1)

    Hits = int(input("How many Hits did your players have today? "))
    current += Hits
    writeScore(current)
    time.sleep(1)

    Runs = int(input("How many Runs did your players have today? "))
    current += Runs
    writeScore(current)
    time.sleep(1)

    winorloss = int(input("Did your team win?\nType '1' for yes and '0' for no. "))
    if winorloss == 1:
        current += 10
        writeScore(current)
    elif winorloss == 0:
        current -= 5
        writeScore(current)
    time.sleep(1)

    earned = current - starting
    print(f"You have earned {earned} points today from stats!\n")
    time.sleep(1)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

#Player Input Menu
def playerInput():
    print("Please enter your starting lineup as prompted.\nIf you are missing a player, then type 'N' or 'n'.\nYou will earn points based on the stats of your players in their game today and if your team wins.")
    time.sleep(2)
    catcher = input("Enter your starting Catcher: ")
    Players.append(catcher)
    time.sleep(1)
    firstBase = input("Enter your starting First Baseman: ")
    Players.append(firstBase)
    time.sleep(1)
    secondBase = input("Enter your starting Second Baseman: ")
    Players.append(secondBase)
    time.sleep(1)
    thirdBase = input("Enter your starting Third Baseman: ")
    Players.append(thirdBase)
    time.sleep(1)
    shortStop = input("Enter your starting Short Stop: ")
    Players.append(shortStop)
    time.sleep(1)
    leftField = input("Enter your starting Left Fielder: ")
    Players.append(leftField)
    time.sleep(1)
    centerField = input("Enter your starting Center Fielder: ")
    Players.append(centerField)
    time.sleep(1)
    rightField = input("Enter your starting Right Fielder: ")
    Players.append(rightField)
    time.sleep(1)
    startingPitcher = input("Enter your starting Pitcher: ")
    Players.append(startingPitcher)
    time.sleep(1)
    DesignatedHitter = input("Enter your starting Designated Hitter: ")
    Players.append(DesignatedHitter)
    time.sleep(1)
    while "N" in Players:
        Players.remove("N")
    while "n" in Players:
        Players.remove("n")
    time.sleep(3)
    writeScore(str(len(Players)))
    print("\nGoing back to the main menu...\n")
    time.sleep(2)
    menu()

#Checking and Recording Dates for daily input functions to prevent multiple entries in one day
def checkDailyInputPlayers():
    trackingFile = "last_run_players.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(trackingFile):
        with open(trackingFile, 'r') as file:
            last_run = file.read().strip()
        if last_run == today_str:
            print("You already used this function today. Please come back tomorrow!")
            return False
        else:
            return True
    else:
        return True
    
def checkDailyInputBet():
    trackingFile = "last_run_bet.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(trackingFile):
        with open(trackingFile, 'r') as file:
            last_run = file.read().strip()
        if last_run == today_str:
            print("You already used this function today. Please come back tomorrow!")
            return False
        else:
            return True
    else:
        return True
    
def checkDailyInputPoints():
    trackingFile = "last_run_points.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(trackingFile):
        with open(trackingFile, 'r') as file:
            last_run = file.read().strip()
        if last_run == today_str:
            print("You already used this function today. Please come back tomorrow!")
            return False
        else:
            return True
    else:
        return True

def checkDailyInputBetCheck():
    trackingFile = "last_run_bet_check.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(trackingFile):
        with open(trackingFile, 'r') as file:
            last_run = file.read().strip()
        if last_run == today_str:
            print("You already used this function today. Please come back tomorrow!")
            return False
        else:
            return True
    else:
        return True

def recordRunDatePlayers():
    trackingFile = "last_run_players.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)     

def recordRunDateBet():
    trackingFile = "last_run_bet.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)     

def recordRunDatePoints():
    trackingFile = "last_run_points.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetCheck():
    trackingFile = "last_run_bet_check.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

#Daily Team Menu
def daily_team(items_array):
    today = datetime.now().date()
    day_number = today.toordinal()
    index = day_number % len(items_array)
    print(f"Today's team is: {items_array[index]}\n")
    time.sleep(2)
    menu()

#Home Menu
def menu():
    input1 = input("Type 'Points' to start entering stats and earning points.\nType 'Bet' to use your currency to bet on odds for the game.\nType 'Check' to check your bets.\nType 'Score' to see your current score.\nType 'Money' to see your current currency.\nType 'Players' to start entering your players for the day.\nType 'List' to see your players that you entered.\nType 'Team' to see your selected team.\n")
    if input1 == "Points" or input1 == "points":
        checkDailyInputPoints()
        if checkDailyInputPoints() == True:
            print("\nYou have chosen to enter stats and earn points!\n")
            time.sleep(2)
            recordRunDatePoints()
            points()
        elif checkDailyInputPoints() == False:
            print("\nYou have already entered stats for the day! Please come back tomorrow to enter new stats.\n")
        time.sleep(2)
        menu()
    elif input1 == "Bet" or input1 == "bet":
        checkDailyInputBet()
        if checkDailyInputBet() == True:
            print("\nYou have chosen to bet your currency on the game!\n")
            time.sleep(2)
            recordRunDateBet()
            bet()
        elif checkDailyInputBet() == False:
            print("\nYou have already made a bet for the day! Please come back tomorrow to make a new bet.\n")
        time.sleep(2)
        menu()
    elif input1 == "Check" or input1 == "check":
        checkDailyInputBetCheck()
        if checkDailyInputBetCheck() == True:
            print("\nYou have chosen to check your bets for the game!\n")
            time.sleep(2)
            recordRunDateBetCheck()
            checkBets()
        elif checkDailyInputBetCheck() == False:
            print("\nYou have already checked your bets for the day! Please come back tomorrow to check new bets.\n")
        time.sleep(2)
        menu()
    elif input1 == "Score" or input1 == "score":
        print("\nYour current score is: " + str(readScore()) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Money" or input1 == "money":
        print("\nYour current currency is: " + str(readCurrency()) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Players" or input1 == "players":
        checkDailyInputPlayers()
        if checkDailyInputPlayers() == True:
            print("\nYou have chosen to enter your players for the day!\n")
            time.sleep(2)
            recordRunDatePlayers()
            playerInput()
        elif checkDailyInputPlayers() == False:
            print("\nYou have already entered your players for the day! Please come back tomorrow to enter new players.\n")
            time.sleep(2)
            menu()
    elif input1 == "List" or input1 == "list":
        print("\nYour current players are: " + str(Players) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Team" or input1 == "team":
        print(f"\n{daily_team(Teams)} is your current team for the day!\n")
        time.sleep(2)
        menu()  
    else:
        print("\nInvalid input, please try again.\n")
        menu()

#Start of the game
print("Welcome to the MLB Schedule Points Game!")
time.sleep(2)
print("You will be given a random team and you will earn points based on your starting lineup cards, stats and win/loss record.")
time.sleep(2)
print("Let's get started!")
time.sleep(2)
daily_team(Teams)