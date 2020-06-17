# ATTAR HAMZA MPSI-1 16/06/2020

from random import randint
from time import time


class Chifoumi:

    scores = {}
    options = ['Rock', 'Paper', 'Scissors']

    f = open('chifoumi_scores.txt', 'a+')

    with open('chifoumi_scores.txt') as my_file:

        my_file.seek(0)
        first_char = my_file.read(1)
        if not first_char:
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

        start = time()
        c = 0
        for i in range(self.n):

            choice = int(input("\nRock: 0, Papre: 1, Scissors: 2 ==> "))
            assert choice in [0, 1, 2], "Choose 0, 1, 2... Play Again!!"
            player_1 = self.options[choice]
            computer = self.options[randint(0, 2)]

            if player_1 == computer:
                print('\n*** Tie!! ***')
            elif player_1 == "Rock":
                if computer == "Paper":
                    print("\n*** You lose!", computer, "covers", player_1, "***")
                else:
                    print("\n*** You win!", player_1, "smashes", computer, "***")
                    c += 1
            elif player_1 == "Paper":
                if computer == "Scissors":
                    print("\n*** You lose!", computer, "cut", player_1, "***")

                else:
                    print("\n*** You win!", player_1, "covers", computer, "***")
                    c += 1
            elif player_1 == "Scissors":
                if computer == "Rock":
                    print("\n*** You lose...", computer, "smashes", player_1, "***")

                else:
                    print("\n*** You win!", player_1, "cut", computer, "***")
                    c += 1
            else:
                print("\nThat's not a valid play. Check your spelling!  ")

            computer = self.options[randint(0, 2)]

        self.duree = float(time() - start)
        self.score = c
        if c > self.scores[self.name][0]:
            self.scores[self.name][0] = c
            self.scores[self.name][1] = self.duree

    @staticmethod
    def deletecontent(pfile):
        pfile.seek(0)
        pfile.truncate()

    @classmethod
    def save_score(cls):
        cls.deletecontent(cls.f)
        cls.f.write('<Player> <Score> <Time in seconds>\n')
        for i in cls.scores.keys():
            cls.f.write("{} {} {}\n".format(i, cls.scores[i][0], cls.scores[i][1]))

    @classmethod
    def rankOfPlayers(cls):
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
    while choix not in ['n', 'N', 'no', 'NO', 'No']:
        if choix == 'r':
            Chifoumi.save_score()
            Chifoumi.rankOfPlayers()
            print("\n*************\n")
            choix = str(input("""Y: Play again.\nn: Exit.\nr: Ranking."""))
        else:
            p_name = str(input("You're name is: "))
            rounds = int(input("How many rounds do you wanna play? "))

            assert (int(rounds) - rounds) == 0, 'The number of rounds is an integer!!'

            player = Chifoumi(p_name, rounds)
            player.start_game()
            Chifoumi.save_score()
            print("\n*****************************************************************************")
            print(" \nYour score is: {}, and your game lasted for {} seconds\n ".format(
                player.score, player.duree))
            print("*****************************************************************************\n")
            choix = str(input("""Y: Play again.\nn: Exit.\nr: Ranking."""))

    print("\n**For More Information About The Players Check chifoumi_scores.txt**")
    print("\n*****************************************")
    print("\nMade By ==> Hamza ATTAR MPSI-1\n \n** As A Homework**\n")


if __name__ == "__main__":
    main()
