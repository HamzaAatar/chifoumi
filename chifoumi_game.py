# ATTAR HAMZA MPSI-1 16/06/2020

from random import randint
from time import time


class Chifoumi:

    scores = {}
    options = ['Rock', 'Paper', 'Scissors']

    # prepare file to save sessions & scores
    f = open('chifoumi_scores.txt', 'a+')

    with open('chifoumi_scores.txt') as my_file:
        my_file.seek(0)
        first_char = my_file.read(1)
        if not first_char:
            # the file is empty
            f.write('<Player> <Score> <Time in seconds>\n')
            f.write('Standard 0 0\n')
        else:
            my_file.seek(0)
            next(my_file)
            for line in my_file:
                (name, score, time) = line.split(" ")
                time = time.replace('\n', '')
                scores[name] = list((int(score), float(time)))

    def __init__(self, player_name, num_rounds):
        self.name = player_name
        self.n = num_rounds
        if self.name not in self.scores:
            self.scores[self.name] = [0, 0]

    def start_game(self):
        ''' start the game '''

        start = time()
        conteur = 0
        i = 0
        while i < self.n:

            while True:
                try:
                    choice = int(input("\nRock: 0, Papre: 1, Scissors: 2 ==> "))
                    break
                except ValueError:
                    print("\nPlease Choose 0, 1 or 2... Play Again!!")

            if choice in [0, 1, 2]:
                player_1 = self.options[choice]
                computer = self.options[randint(0, 2)]

                if player_1 == computer:
                    print('\n*** Tie!! ***')
                elif player_1 == "Rock":
                    if computer == "Paper":
                        print("\n*** You lose!", computer, "covers", player_1, "***")
                    else:
                        print("\n*** You win!", player_1, "smashes", computer, "***")
                        conteur += 1
                elif player_1 == "Paper":
                    if computer == "Scissors":
                        print("\n*** You lose!", computer, "cut", player_1, "***")

                    else:
                        print("\n*** You win!", player_1, "covers", computer, "***")
                        conteur += 1
                elif player_1 == "Scissors":
                    if computer == "Rock":
                        print("\n*** You lose...", computer, "smashes", player_1, "***")

                    else:
                        print("\n*** You win!", player_1, "cut", computer, "***")
                        conteur += 1
                else:
                    print("\nThat's not a valid play. Check your spelling!  ")
                i += 1

            else:
                print("\nPlease Choose 0, 1 or 2... Play Again!!")

        self.duree = float(time() - start)
        self.score = conteur

        # to save the highest score
        if conteur > self.scores[self.name][0]:
            self.scores[self.name][0] = conteur
            self.scores[self.name][1] = self.duree

    @classmethod
    def save_score(cls):
        ''' saving score to the file '''

        cls.f.seek(0)
        cls.f.truncate()
        cls.f.write('<Player> <Score> <Time in seconds>\n')
        for i in cls.scores.keys():
            cls.f.write("{} {} {}\n".format(i, cls.scores[i][0], cls.scores[i][1]))

    @classmethod
    def rankOfPlayers(cls):
        ''' Ranking players by score '''

        listofTuples = sorted(cls.scores.items(),  key=lambda x: x[1], reverse=True)
        print("\n*************")
        print("\nRanking:\n")
        for elem in listofTuples:
            print(elem[0], " ==> ", elem[1][0])


def main():
    print("\n*****************************************\n")
    print("""Welcome to Rock, Paper, Scissors game,\n
    In this game You face the computer in a RPS match with several rounds.\n
    it's simple:\n
    1) save your player's name.\n
    2) choose the number of rounds you want to play.\n
    the game will save your highest score and the time of your match.\n
    you can create as many player as you want,\n
    invite your friends and challenge them to find out who is the best player.\n\n
    Options:\n
        Y: Play, n: Exit, r: Ranking
     """)

    choix = str(input("Do You Want To Start (Y/n/r)?"))
    choix = choix.replace(' ', '')

    while choix not in ['n', 'N', 'no', 'NO', 'No']:
        if choix == 'r':
            Chifoumi.save_score()
            Chifoumi.rankOfPlayers()
            print("\n*************\n")
            choix = str(input("""Y: Play again.\nn: Exit.\nr: Ranking."""))
            choix = choix.replace(' ', '')
        else:
            p_name = str(input("You're name is: "))
            p_name = p_name.replace(' ', '')
            while True:
                try:
                    rounds = int(input("How many rounds do you wanna play? "))
                    break
                except ValueError:
                    print('The number of rounds is an integer !!')

            player = Chifoumi(p_name, rounds)
            player.start_game()
            Chifoumi.save_score()
            print("\n*****************************************************************************")
            print(" \nYour score is: {}, and your game lasted for {} seconds\n ".format(
                player.score, player.duree))
            print("*****************************************************************************\n")
            choix = str(input("""Y: Play again.\nn: Exit.\nr: Ranking."""))
            choix = choix.replace(' ', '')

    print("\n**For More Information About The Players Check chifoumi_scores.txt**")
    print("\n*****************************************")
    print("\nMade By ==> Hamza ATTAR MPSI-1\n \n** As A Homework**\n")


if __name__ == "__main__":
    main()
