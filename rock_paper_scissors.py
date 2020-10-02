#!/usr/bin/env python3
import random
moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        play = input("Rock, paper, scissors?\n").lower()
        if play == "rock":
            print("You played rock.")
        elif play == "paper":
            print("You played paper.")
        elif play == "scissors":
            print("You played scissors.")
        else:
            print("Invalid input! Try again!")
            # Calling the function again in case of wrong input
            self.move()
        return play

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    # Calling the constructor with superpowers
    def __init__(self):
        super().__init__()
        self.moves_size = len(moves)
        self.my_next_move_index = random.randrange(self.moves_size)

    def move(self):
        my_next_move = moves[self.my_next_move_index]
        self.my_next_move_index = (
            self.my_next_move_index + 1) % self.moves_size
        return my_next_move

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def results(self):
        if self.p1.score > self.p2.score:
            print("\n\n*** PLAYER ONE WON THE GAME!! *** ")
        elif self.p2.score > self.p1.score:
            print("\n\n*** PLAYER TWO WON THE GAME!! *** ")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        # Results
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("*** PLAYER ONE WINS! ***")
            self.p1.score += 1
        elif beats(move2, move1):
            print("*** PLAYER TWO WINS! ***")
            self.p2.score += 1
        else:
            print("*** TIE! ***")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player one {self.p1.score}, Player Two {self.p2.score}")

    def play_game(self):
        print("*** Game start! ***")
        for round in range(3):
            print(f"\n\nRound {round}:")
            self.play_round()
        self.results()
        # I created another loop in case
        # there was a tie in the first three rounds.
        for round in range(3, 9):
            if self.p1.score == self.p2.score:
                print(f"\n\nRound {round}:")
                self.play_round()
                self.results()
        print("Game over!\n\n")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
