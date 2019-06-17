import random
import keyboard
import os
import copy
from TambolaGameOOPS.Player import Player


class TambolaGame:
    # set player name having length 10 and return that name
    def getValidPlayerName(self, nameOfPlayer):
        validPlayerName = ""
        if len(nameOfPlayer) > 10:
            validPlayerName = nameOfPlayer[0:10]

        elif len(nameOfPlayer) == 10:
            validPlayerName = nameOfPlayer
        else:
            validPlayerName = nameOfPlayer.ljust(10 - len(nameOfPlayer))
        return validPlayerName.upper()

    # Print mainScore and currentScore of each player in tabular format
    def displayScore(self, playerList, scoreType):
        '''playerNameList = []
        for playerObject in playerList:
            playerNameList.append(playerObject.getPlayerName())'''

        rows = self.TotalNumber + 1
        for rows in range(rows):
            print("+-----------------------------------------------+")
            for playerObj in playerList:
                playername = self.getValidPlayerName(playerObj.getPlayerName())
                if rows == 0:
                    print("|", playername, "\t", end="")
                else:
                    if scoreType == "mainScore":
                        print("|  ", playerObj.getPlayerValues()[rows - 1], "\t\t", end="")
                    if scoreType == "currentScore":
                        print("|  ", playerObj.getPlayerCurrentScore()[rows - 1], "\t\t", end="")
            print("|")
        print("+-----------------------------------------------+")

    # create method to clear colsole
    def clearConsole(self):
        os.system('cls')

    # Create method using recursive  function to generate new unique token number and return thar token
    def generateNumber(self, listOfNumbers):
        newRandomNo = random.randint(0, self.maxRange)
        if newRandomNo not in listOfNumbers:
            return newRandomNo
        else:
            return self.generateNumber(listOfNumbers)

    # create method to check token number is available in player current score or not.. If number is available then edit that number to 'X'
    def checkNumIsAvailableInPlayerList(self, newNumber, playerObjectList):
        for playerobj in playerObjectList:
            if newNumber in playerobj.getPlayerCurrentScore():
                score = playerobj.getPlayerCurrentScore()
                score[score.index(newNumber)] = 'X'
                playerobj.setPlayerCurrentScore(score)

    # create method for play game
    def playGame(self, playerObjectList):
        chkFlag = True
        listOfNumbers = []  # create that list to store all token numbers for user reference
        winnerName = ""
        # originalValuesInPlayerDict = copy.deepcopy(playersDictionary)
        while chkFlag:
            enterKeyFlag = input("\nPress ENTER button for next Token Number :")
            if keyboard.is_pressed("enter"):  # on click of 'enter'  button new token no is genrated

                self.clearConsole()
                newNumber = self.generateNumber(listOfNumbers)
                listOfNumbers.append(newNumber)
                print("Main Values in player chart are below :\n")
                self.displayScore(playerObjectList, "mainScore")
                print("\nLucky Numbers are :", listOfNumbers)
                print("\nNext Number is :", newNumber)

                self.checkNumIsAvailableInPlayerList(newNumber, playerObjectList)
                for playerobj in playerObjectList:
                    l1 = [ele for ele in playerobj.getPlayerCurrentScore() if isinstance(ele, str)]
                    if len(playerobj.getPlayerCurrentScore()) == len(
                            l1):  # check this condition for player  check all current values of sheet are match or not
                        winnerName = playerobj.getPlayerName()
                        chkFlag = False

                self.displayScore(playerObjectList, "currentScore")  # display player score in proper format.

            # time.sleep(.3)

        print("\ncongratulations", winnerName.upper(), "You are the winner !!!!\n\n")

    # return  list of unique random values for each player
    def getRandomValues(self):
        listOfNumbersForPlayer = []
        while len(listOfNumbersForPlayer) < self.TotalNumber:
            r = random.randint(0, self.maxRange + 1)
            if r not in listOfNumbersForPlayer:  # chaeck r is unique or not
                listOfNumbersForPlayer.append(r)
        return listOfNumbersForPlayer

    # create player class reference and store name of player , player main score and player currentScore score  and return that player reference object
    def getPlayer(self, playerName):
        player = Player()
        player.setPlayerName(playerName)
        currentScore = self.getRandomValues()  # create list of unique random values for each player
        mainScore = copy.deepcopy(
            currentScore)  # using deepcopy mainScore list are not change while editing on current score List
        player.setPlayerValues(mainScore)  # mainScore values are constant till end of the game
        player.setPlayerCurrentScore(currentScore)  # currentScore values are changed after matching token number
        return player

    # Take informetion from user like number of players, max number range and numbers for digits for each player and play game
    def getUserInputValues(self):

        self.noOfPlayer = int(input("Enter Number of Players :"))
        self.maxRange = int(input("Enter maximum Number :"))
        self.TotalNumber = int(input("Enter max number in sheet for player :"))

        playerObjectList = []  # Store all player object reference in this list
        for player in range(self.noOfPlayer):
            playerName = input("Enter name of player :")
            playerObjectList.append(self.getPlayer(
                playerName))  # call getPlayer method to store name of player and player score in player reference object

        '''Show player name with its sheet'''
        self.displayScore(playerObjectList, "mainScore")  # Call displayScore method to display score in proper format

        '''Main game start from here'''
        self.playGame(playerObjectList)  # call playGame function to play Tambola game....

    # Call main function of the game
    def mainMethod(self):
        self.getUserInputValues()  # take input from user for to start the game.


tambolagame = TambolaGame()
tambolagame.mainMethod()  # Call main method to execute the game
