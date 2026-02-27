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
CombinedPitchersAndFielders = []
Pitcher = []

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

#Bet Home Menus
def bet():
    betInput = input("What would you like to bet on?\nType 'Outcome' to bet on the outcome of the game.\nType 'Runs' to bet on the total runs scored in the game.\nType 'Props' to bet on player props.\nType 'Back' to go back to the main menu.\n")
    if betInput == "Outcome" or betInput == "outcome":
        checkDailyInputBetCheckOutcome()
        if checkDailyInputBetCheckOutcome() == True:
            print("\nYou have chosen to bet on the outcome of the game!\n")
            time.sleep(2)
            recordRunDateBetCheckOutcome()
            betGameOutcome()
        elif checkDailyInputBetCheckOutcome() == False:
            print("\nYou have already made a bet on the outcome of the game for the day! Please come back tomorrow to make a new bet.\n")
        time.sleep(2)
    elif betInput == "Runs" or betInput == "runs":
        checkDailyInputBetRunTotals()
        if checkDailyInputBetRunTotals() == True:
            recordRunDateBetRunTotals()
            betRunTotals()
        elif checkDailyInputBetRunTotals() == False:
            print("\nYou have already made a bet on the total runs scored in the game for the day! Please come back tomorrow to make a new bet.\n")
        time.sleep(2)
    elif betInput == "Props" or betInput == "props":
        betPlayerPropsHomeMenu()
    elif betInput == "Back" or betInput == "back":
        print("Going back to the main menu...\n")
        time.sleep(2)
        menu()
    else:
        print("Invalid input, please try again.")
        time.sleep(2)
        bet()

def betPlayerPropsHomeMenu():
    input2 = input("Would you like to bet on pitcher's performance or fielder's performance, or both?\nType 'Pitcher' to bet on the pitcher's performance, 'Fielder' to bet on the fielder's performance, and 'Both' to bet on both the pitcher's and fielder's performance. ")
    if input2 == "Pitcher" or input2 == "pitcher":
        checkDailyInputBetPlayerPropsPitcher()
        if checkDailyInputBetPlayerPropsPitcher() == True:
            print("You have chosen to bet on the pitcher's performance!\n")
            recordRunDateBetPlayerPropsPitcher()
            betPlayerPropsPitcherOnly()
            time.sleep(2)
            #add code for betting on pitcher's performance here
        elif checkDailyInputBetPlayerPropsPitcher() == False:
            print("You have already made a bet on the pitcher's performance for the day! Please come back tomorrow to make a new bet.\n")
            time.sleep(2)
            menu()
        time.sleep(2)
    elif input2 == "Fielder" or input2 == "fielder":
        checkDailyInputBetPlayerPropsFielder()
        if checkDailyInputBetPlayerPropsFielder() == True:
            print("You have chosen to bet on the fielder's performance!\n")
            recordRunDateBetPlayerPropsFielder()
            betPlayerPropsFielderOnly()
            time.sleep(2)
        elif checkDailyInputBetPlayerPropsFielder() == False:
            print("You have already made a bet on the fielder's performance for the day! Please come back tomorrow to make a new bet.\n")
            time.sleep(2)
            menu()
        #add code for betting on fielder's performance here
    elif input2 == "Both" or input2 == "both":
        checkDailyInputBetPlayerPropsBoth()
        if checkDailyInputBetPlayerPropsBoth() == True:
            print("You have chosen to bet on both the pitcher's and fielder's performance!\n")
            recordRunDateBetPlayerPropsBoth()
            betPlayerPropsPitcher()
            time.sleep(2)
        elif checkDailyInputBetPlayerPropsBoth() == False:
            print("You have already made a bet on both the pitcher's and fielder's performance for the day! Please come back tomorrow to make a new bet.\n")
            time.sleep(2)
            menu()

#Bet Menus
def betGameOutcome():
    global betAmountOutcome, multiplier1, current1, starting1
    # start with current currency from file
    current1 = readCurrency()
    starting1 = current1

    betAmountOutcome = int(input("How much currency would you like to bet? "))
    if betAmountOutcome > current1:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        menu()
    else:
        current1 -= betAmountOutcome
        writeCurrency(current1)
        time.sleep(1)

    odds = input("What are the odds for your team to win? (e.g. +150, -200) ")
    if odds.startswith('+'):
        multiplier1 = int(odds[1:]) / 100
    elif odds.startswith('-'):
        multiplier1 = 100 / int(odds[1:])
    else:
        print("Invalid odds format. Please try again.")
        time.sleep(2)
        menu()
    pick = input("Do you pick your team to win or lose?\nType 'Win' to pick your team to win and 'Lose' to pick your team to lose. ")
    if pick == "Win" or pick == "win":
        multiplier1 = multiplier1  
    elif pick == "Lose" or pick == "lose":
        multiplier1 = -multiplier1
    time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

def betRunTotals():
    global betAmountRuns, multiplier2, current2, starting2, underTotal, overTotal
    # start with current currency from file
    current2 = readCurrency()
    starting2 = current2

    betAmountRuns = int(input("How much currency would you like to bet? "))
    if betAmountRuns > current2:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        bet()
    else:
        current2 -= betAmountRuns
        writeCurrency(current2)
        time.sleep(1)

    overTotal = input("What is the over run total? (e.g. 8.5, 5.5) ")
    if overTotal.endswith('.5'):
        multiplier2 = 1.9
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    underTotal = input("What is the under run total? (e.g. 8.5, 5.5) ")
    if underTotal.endswith('.5'):
        multiplier2 = 1.9
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    pick2 = input("Do you pick the over or under?\nType 'Over' to pick the over and 'Under' to pick the under. ")
    if pick2 == "Over" or pick2 == "over":
        multiplier2 = multiplier2
    elif pick2 == "Under" or pick2 == "under":
        multiplier2 = -multiplier2
    time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

def betPlayerPropsPitcherOnly():
    global betAmountPitcher, multiplier3, current3, starting3, StrikeoutsOverTotal, StrikeoutsUnderTotal
    # start with current currency from file
    current3 = readCurrency()
    starting3 = current3

    betAmountPitcher = int(input("How much currency would you like to bet?\n"))
    if betAmountPitcher > current3:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        bet()
    else:
        current3 -= betAmountPitcher
        writeCurrency(current3)
        time.sleep(1)
    dailyPitcher = Pitcher[0]
    print(f"Your pitcher to bet on today is: {dailyPitcher}\n")
    time.sleep(2)

    StrikeoutsOverTotal = input("What is the over for strikeouts for your pitcher? (e.g. 8.5, 5.5)\n")
    if StrikeoutsOverTotal.endswith('.5'):
        multiplier3 = 1.9
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    StrikeoutsUnderTotal = input("What is the under for strikeouts for your pitcher? (e.g. 8.5, 5.5)\n")
    if StrikeoutsUnderTotal.endswith('.5'):
        multiplier3 = 1.9
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    pick3 = input("Do you pick the over or under for strikeouts?\nType 'Over' to pick the over and 'Under' to pick the under.\n")
    if pick3 == "Over" or pick3 == "over":
        multiplier3 = multiplier3
    elif pick3 == "Under" or pick3 == "under":
        multiplier3 = -multiplier3
    time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

def betPlayerPropsPitcher():
    global betAmountPitcher2, multiplier4, current4, starting4
    # start with current currency from file
    current4 = readCurrency()
    starting4 = current4

    betAmountPitcher2 = int(input("How much currency would you like to bet? "))
    if betAmountPitcher2 > current4:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        bet()
    else:
        current4 -= betAmountPitcher2
        writeCurrency(current4)
        time.sleep(1)
    dailyPitcher = Pitcher[0]
    print(f"Your pitcher to bet on today is: {dailyPitcher}\n")
    time.sleep(2)

    StrikeoutsOverTotal = input("What is the over for strikeouts for your pitcher? (e.g. 8.5, 5.5)\n Type 'No Bet' to not bet on this prop. ")
    if StrikeoutsOverTotal.endswith('.5'):
        multiplier4 = 1.9
    elif StrikeoutsOverTotal == "No Bet" or StrikeoutsOverTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    StrikeoutsUnderTotal = input("What is the under for strikeouts for your pitcher? (e.g. 8.5, 5.5)\nType 'No Bet' to not bet on this prop. ")
    if StrikeoutsUnderTotal.endswith('.5'):
        multiplier4 = 1.9
    elif StrikeoutsUnderTotal == "No Bet" or StrikeoutsUnderTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    pick3 = input("Do you pick the over or under for strikeouts?\nType 'Over' to pick the over and 'Under' to pick the under.\n Tpye 'No Bet' to not bet on this prop. ")
    if pick3 == "Over" or pick3 == "over":
        multiplier4 = multiplier4
    elif pick3 == "Under" or pick3 == "under":
        multiplier4 = -multiplier4
    elif pick3 == "No Bet" or pick3 == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    time.sleep(2)
    print("Going to the fielder props menu...\n")
    time.sleep(2)
    betPlayerPropsFielder()

def betPlayerPropsFielderOnly():
    global betAmountFielder, multiplier5, current5, starting5
    # start with current currency from file
    current5 = readCurrency()
    starting5 = current5
    betAmountFielder = int(input("How much currency would you like to bet?\n"))
    if betAmountFielder > current5:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        bet()
    else:
        current5 -= betAmountFielder
        writeCurrency(current5)
        time.sleep(1)
    RandomPlayer = random.choice(Players)
    print("Your randomly selected fielder/DH to bet on today is: " + RandomPlayer + "\n")
    HomeRun = input(f"Do you bet on {RandomPlayer} to hit a home run?\nType 'Yes' to bet on a home run and 'No' to not bet on a home run.\n")
    if HomeRun == "Yes" or HomeRun == "yes":
        multiplier5 = 3
    elif HomeRun == "No" or HomeRun == "no":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        bet()
    overHitsTotal = input(f"What is the over for hits for {RandomPlayer}? (e.g. 1.5, 2.5)\nType 'No Bet' to not bet on this prop.\n")
    if overHitsTotal.endswith('.5'):
        multiplier5 = 1.9
    elif overHitsTotal == "No Bet" or overHitsTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    underHitsTotal = input(f"What is the under for hits for {RandomPlayer}? (e.g. 1.5, 2.5)\nType 'No Bet' to not bet on this prop.\n")
    if underHitsTotal.endswith('.5'):
        multiplier5 = 1.9
    elif underHitsTotal == "No Bet" or underHitsTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    pick4 = input("Do you pick the over or under for hits?\nType 'Over' to pick the over and 'Under' to pick the under.\nType 'No Bet' to not bet on this prop.\n")
    if pick4 == "Over" or pick4 == "over":
        multiplier5 = multiplier5
    elif pick4 == "Under" or pick4 == "under":
        multiplier5 = -multiplier5
    elif pick4 == "No Bet" or pick4 == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()

def betPlayerPropsFielder():
    global betAmountFielder2, multiplier6, current6, starting6, HomeRun, overHitsTotal, underHitsTotal
    # start with current currency from file
    current6 = readCurrency()
    starting6 = current6
    betAmountFielder2 = int(input("How much currency would you like to bet? "))
    if betAmountFielder2 > current6:
        print("You do not have enough currency to make that bet. Please try again.")
        time.sleep(2)
        bet()
    else:
        current6 -= betAmountFielder2
        writeCurrency(current6)
        time.sleep(1)
    HomeRun = input("Do you bet on a randomly selected fielder/DH to hit a home run?\nType 'Yes' to bet on a home run and 'No' to not bet on a home run. ")
    if HomeRun == "Yes" or HomeRun == "yes":
        multiplier6 = 3
    elif HomeRun == "No" or HomeRun == "no":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        bet()
    overHitsTotal = input("What is the over for hits for your randomly selected fielder/DH? (e.g. 1.5, 2.5)\nType 'No Bet' to not bet on this prop. ")
    if overHitsTotal.endswith('.5'):
        multiplier6 = 1.9
    elif overHitsTotal == "No Bet" or overHitsTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    underHitsTotal = input("What is the under for hits for your randomly selected fielder/DH? (e.g. 1.5, 2.5)\nType 'No Bet' to not bet on this prop. ")
    if underHitsTotal.endswith('.5'):
        multiplier6 = 1.9
    elif underHitsTotal == "No Bet" or underHitsTotal == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    else:
        print("Invalid total format. Please try again.")
        time.sleep(2)
        bet()
    pick4 = input("Do you pick the over or under for hits?\nType 'Over' to pick the over and 'Under' to pick the under.\nType 'No Bet' to not bet on this prop. ")
    if pick4 == "Over" or pick4 == "over":
        multiplier6 = multiplier6
    elif pick4 == "Under" or pick4 == "under":
        multiplier6 = -multiplier6
    elif pick4 == "No Bet" or pick4 == "no bet":
        print("You have chosen not to bet on this prop.")
        time.sleep(2)
    print("Going back to the main menu...\n")
    time.sleep(2)
    menu()
#Check Bet Home Menu
def checkBet():
    checkInput = input("What bet would you like to check on?\nType 'Outcome' to check on the outcome of the game.\nType 'Runs' to check on the total runs scored in the game.\nType 'Back' to go back to the main menu.")
    if checkInput == "Outcome" or checkInput == "outcome":
        checkDailyInputBetCheckOutcome()
        if checkDailyInputBetCheckOutcome() == True:
            print("\nYou have chosen to check your bet on the outcome of the game!\n")
            time.sleep(2)
            recordRunDateBetCheckOutcome()
            checkBetGameOutcome()
        elif checkDailyInputBetCheckOutcome() == False:
            print("\nYou have already checked your bet on the outcome of the game for the day! Please come back tomorrow to check new bets.\n")
        time.sleep(2)
    elif checkInput == "Runs" or checkInput == "runs":
        checkDailyInputBetRunTotals()
        if checkDailyInputBetRunTotals() == True:
            print("\nYou have chosen to check your bet on the total runs scored in the game!\n")
            time.sleep(2)
            recordRunDateBetRunTotals()
            checkBetRunTotals()
        elif checkDailyInputBetRunTotals() == False:
            print("\nYou have already checked your bet on the total runs scored in the game for the day! Please come back tomorrow to check new bets.\n")
        time.sleep(2)
    #elif checkInput == "Props" or checkInput == "props":
    elif checkInput == "Back" or checkInput == "back":
        print("Going back to the main menu...\n")
        time.sleep(2)
        menu()
    else:
        print("Invalid input, please try again.\n")
        time.sleep(2)
        checkBet()

#Check Bet Menus
def checkBetGameOutcome():
    global betAmountOutcome, multiplier1, current1, starting1
    winorloss = int(input("Did your team win?\nType '1' for yes and '0' for no. "))
    if winorloss == 1:
        winnings = int(betAmountOutcome * multiplier1)
        current1 += winnings
        writeCurrency(current1)
        print(f"You won {winnings} currency from your bet!\n")
    elif winorloss == 0:
        print(f"You lost {betAmountOutcome} currency from your bet.\n")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        menu()
    menu()

def checkBetRunTotals():
    global betAmountRuns, multiplier2, current2, starting2, underTotal, overTotal
    winorloss = int(input("How many total runs were scored?\nType a number."))
    if winorloss < int(overTotal) and winorloss > int(underTotal):
        winnings = int(betAmountRuns * multiplier2)
        current2 += winnings
        writeCurrency(current2)
        print(f"You won {winnings} currency from your bet!\n")
    elif winorloss == 0:
        print(f"You lost {betAmountRuns} currency from your bet.\n")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        menu()
    menu()

def checkBetPlayerPropsPitcherOnly():
    global betAmountPitcher, multiplier3, current3, starting3, strikeouts, StrikeoutsOverTotal, StrikeoutsUnderTotal
    strikeouts = int(input("How many strikeouts did your pitcher have? Type a number. "))
    if (multiplier3 > 0 and strikeouts > int(StrikeoutsOverTotal)) or (multiplier3 < 0 and strikeouts < int(StrikeoutsUnderTotal)):
        winnings = int(betAmountPitcher * multiplier3)
        current3 += winnings
        writeCurrency(current3)
        print(f"You won {winnings} currency from your bet!\n")
    else:
        print(f"You lost {betAmountPitcher} currency from your bet.\n")
    global betAmountFielder, multiplier5, current5, starting5, HomeRun, overHitsTotal, underHitsTotal
    homeRunInput = input("Did your randomly selected fielder/DH hit a home run?\nType 'Yes' for yes and 'No' for no. ")
    if (HomeRun == "Yes" or HomeRun == "yes") and homeRunInput == "Yes":
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your home run prop bet!\n")
    elif (HomeRun == "Yes" or HomeRun == "yes") and homeRunInput == "No":
        print(f"You lost {betAmountFielder} currency from your home run prop bet.\n")
    elif (HomeRun == "No" or HomeRun == "no") and homeRunInput == "No":
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your home run prop bet!\n")
    elif (HomeRun == "No" or HomeRun == "no") and homeRunInput == "Yes":
        print(f"You lost {betAmountFielder} currency from your home run prop bet.\n")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        menu()
    hitsInput = float(input("How many hits did your randomly selected fielder/DH have? Type a number. "))
    if (overHitsTotal != "No Bet" and hitsInput > float(overHitsTotal)) or (underHitsTotal != "No Bet" and hitsInput < float(underHitsTotal)):
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your hits prop bet!\n")
    else:
        print(f"You lost {betAmountFielder} currency from your hits prop bet.\n")
    menu()

def checkBetPlayerPropsBoth():
    global betAmountPitcher, multiplier7, current7, starting7, strikeouts, StrikeoutsOverTotal, StrikeoutsUnderTotal
    strikeouts = int(input("How many strikeouts did your pitcher have? Type a number. "))
    if (multiplier7 > 0 and strikeouts > int(StrikeoutsOverTotal)) or (multiplier7 < 0 and strikeouts < int(StrikeoutsUnderTotal)):
        winnings = int(betAmountPitcher * multiplier7)
        current7 += winnings
        writeCurrency(current7)
        print(f"You won {winnings} currency from your bet!\n")
    else:
        print(f"You lost {betAmountPitcher} currency from your bet.\n")

    global betAmountFielder, multiplier5, current5, starting5, HomeRun, overHitsTotal, underHitsTotal
    homeRunInput = input("Did your randomly selected fielder/DH hit a home run?\nType 'Yes' for yes and 'No' for no. ")
    if (HomeRun == "Yes" or HomeRun == "yes") and homeRunInput == "Yes":
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your home run prop bet!\n")
    elif (HomeRun == "Yes" or HomeRun == "yes") and homeRunInput == "No":
        print(f"You lost {betAmountFielder} currency from your home run prop bet.\n")
    elif (HomeRun == "No" or HomeRun == "no") and homeRunInput == "No":
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your home run prop bet!\n")
    elif (HomeRun == "No" or HomeRun == "no") and homeRunInput == "Yes":
        print(f"You lost {betAmountFielder} currency from your home run prop bet.\n")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        menu()
    hitsInput = float(input("How many hits did your randomly selected fielder/DH have? Type a number. "))
    if (overHitsTotal != "No Bet" and hitsInput > float(overHitsTotal)) or (underHitsTotal != "No Bet" and hitsInput < float(underHitsTotal)):
        winnings = int(betAmountFielder * multiplier5)
        current5 += winnings
        writeCurrency(current5)
        print(f"You won {winnings} currency from your hits prop bet!\n")
    else:
        print(f"You lost {betAmountFielder} currency from your hits prop bet.\n")
    strikeouts = int(input("How many strikeouts did your pitcher have? Type a number. "))
    if (multiplier3 > 0 and strikeouts > int(StrikeoutsOverTotal)) or (multiplier3 < 0 and strikeouts < int(StrikeoutsUnderTotal)):
        winnings = int(betAmountPitcher * multiplier3)
        current3 += winnings
        writeCurrency(current3)
        print(f"You won {winnings} currency from your bet!\n")
    else:
        print(f"You lost {betAmountPitcher} currency from your bet.\n")
    print("Going back to the main menu...\n")
    time.sleep(2)
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
    CombinedPitchersAndFielders.append(catcher)
    time.sleep(1)
    firstBase = input("Enter your starting First Baseman: ")
    Players.append(firstBase)
    CombinedPitchersAndFielders.append(firstBase)
    time.sleep(1)
    secondBase = input("Enter your starting Second Baseman: ")
    Players.append(secondBase)
    CombinedPitchersAndFielders.append(secondBase)
    time.sleep(1)
    thirdBase = input("Enter your starting Third Baseman: ")
    Players.append(thirdBase)
    CombinedPitchersAndFielders.append(thirdBase)
    time.sleep(1)
    shortStop = input("Enter your starting Short Stop: ")
    Players.append(shortStop)
    CombinedPitchersAndFielders.append(shortStop)
    time.sleep(1)
    leftField = input("Enter your starting Left Fielder: ")
    Players.append(leftField)
    CombinedPitchersAndFielders.append(leftField)
    time.sleep(1)
    centerField = input("Enter your starting Center Fielder: ")
    Players.append(centerField)
    CombinedPitchersAndFielders.append(centerField)
    time.sleep(1)
    rightField = input("Enter your starting Right Fielder: ")
    Players.append(rightField)
    CombinedPitchersAndFielders.append(rightField)
    time.sleep(1)
    startingPitcher = input("Enter your starting Pitcher: ")
    Pitcher.append(startingPitcher)
    CombinedPitchersAndFielders.append(startingPitcher)
    time.sleep(1)
    DesignatedHitter = input("Enter your starting Designated Hitter: ")
    Players.append(DesignatedHitter)
    CombinedPitchersAndFielders.append(DesignatedHitter)
    time.sleep(1)
    while "N" in CombinedPitchersAndFielders:
        CombinedPitchersAndFielders.remove("N")
    while "n" in CombinedPitchersAndFielders:
        CombinedPitchersAndFielders.remove("n")
    time.sleep(3)
    writeScore(str(len(CombinedPitchersAndFielders)))
    if len(CombinedPitchersAndFielders) == 10:
        print("You have entered a full starting lineup! You have earned 500 currency points!\n")
        current = readCurrency()
        current += 500
        writeCurrency(current)
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

def checkDailyInputBetCheckOutcome():
    trackingFile = "last_run_bet_check_outcome.txt"
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

def checkDailyInputBetRunTotals():
    trackingFile = "last_run_check_bet_runs.txt"
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

def checkDailyInputBetPlayerPropsPitcher():
    trackingFile = "last_run_bet_props_pitcher.txt"
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

def checkDailyInputBetPlayerPropsFielder():
    trackingFile = "last_run_bet_props_fielder.txt"
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
    
def checkDailyInputBetPlayerPropsBoth():
    trackingFile = "last_run_bet_props_both.txt"
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

def recordRunDatePoints():
    trackingFile = "last_run_points.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetCheckOutcome():
    trackingFile = "last_run_bet_check_bet_outcome.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetRunTotals():
    trackingFile = "last_run_check_bet_runs.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetPlayerPropsPitcher():
    trackingFile = "last_run_bet_props_pitcher.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetPlayerPropsFielder():
    trackingFile = "last_run_bet_props_fielder.txt"
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(trackingFile, 'w') as file:
        file.write(today_str)

def recordRunDateBetPlayerPropsBoth():
    trackingFile = "last_run_bet_props_both.txt"
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
    input1 = input("Type 'Points' to start entering stats and earning points.\nType 'Bet' to use your currency to bet on the game outcome, run totals and player props for the game.\nType 'Check' to check your bets.\nType 'Score' to see your current score.\nType 'Money' to see your current currency.\nType 'Players' to start entering your players for the day.\nType 'List' to see your players that you entered.\nType 'Team' to see your selected team.\n")
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
        bet()
    elif input1 == "Check" or input1 == "check":
        checkBet()
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