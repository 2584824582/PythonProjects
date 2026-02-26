import random, time, os
#Scores
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
UsedTeams = []
Players = []
#Write Score to file
def writeScore(score):
    # score should be an integer
    with open('score.txt', 'w') as file:
        file.write(str(score))

#Read Score from file
#returns an int, defaults to 0 if file missing or invalid

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
#returns an int, defaults to 0 if missing or invalid

def readCurrency():
    if not os.path.exists('money.txt'):
        return 0
    with open('money.txt', 'r') as file:
        text = file.read().strip()
        try:
            return int(text)
        except ValueError:
            return 0

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
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

#Menu
def menu():
    input1 = input("Type 'Points' to start entering stats and earning points.\nType 'Bet' to use your currency to bet on odds for the game.\nType 'Score' to see your current score.\nType 'Money' to see your current currency.\nType 'Players' to start entering your players for the day.\nType 'List' to see your players that you entered.\nType 'Team' to see your selected team.\n")
    if input1 == "Points" or input1 == "points":
        print("You have chosen to enter stats and earn points!")
        time.sleep(2)
        points()
    elif input1 == "Bet" or input1 == "bet":
        print("You have chosen to bet your currency on the game!")
        #Put bet function here
    elif input1 == "Score" or input1 == "score":
        print("Your current score is: " + str(readScore()) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Money" or input1 == "money":
        print("Your current currency is: " + str(readCurrency()) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Players" or input1 == "players":
        print("You have chosen to enter your players for the day!")
        time.sleep(2)
        playerInput()
    elif input1 == "List" or input1 == "list":
        print("Your current players are: " + str(Players) + "\n")
        time.sleep(2)
        menu()
    elif input1 == "Team" or input1 == "team":
        print(teamSelection + " is your current team for the day!\n")
        time.sleep(2)
        menu()
    else:
        print("Invalid input, please try again.\n")
        menu()
#Team Selection
def selectTeam():
    global teamSelection
    teamSelection = random.choice(Teams)
    print("\nYour team for today is: " + teamSelection + "\n")
    UsedTeams.append(teamSelection)
    Teams.remove(teamSelection)
    time.sleep(2)
    menu()
#Start of the game
print("Welcome to the MLB Schedule Points Game!")
time.sleep(2)
print("You will be given a random team and you will earn points based on your starting lineup cards, stats and win/loss record.")
time.sleep(2)
print("Let's get started!")
time.sleep(2)
selectTeam()
