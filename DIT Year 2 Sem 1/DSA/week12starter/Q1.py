# Represents one entry of a list of high scores.
class GameEntry:
    # Create an entry with given name and score.
    def __init__(self, name, score):
        self._name = name
        self._score = score

    # Return the name of the person for this entry.
    def get_name(self):
        return self._name

    # Return the score of this entry.
    def get_score(self):
        return self._score

    # Return string representation of the entry.
    def __str__(self):
        # e.g., '(Bob, 98)'
        return '({0}, {1})'.format(self._name, self._score)

# Fixed-length sequence of high scores in ascending order.
class Scoreboard:
    # Initialise scoreboard with given maximum capacity.
    def __init__(self, capacity=10):
        # All entries are initially None.
        self._board = [None] * capacity # reserve space for future scores
        self._n = 0 # number of actual entries

    # Return entry at index k.
    def __getitem__(self, k):
        return self._board[k]

    # Return string representation of the high score list.
    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    # Consider adding entry to high scores.
    def add(self, entry):
        score = entry.get_score()
        # Does new entry qualify as a high score?
        # Yes, if board is not full or score is higher than last entry
        qualified = self._n < len(self._board) or score > self._board[-1].get_score()

        if qualified:
            if self._n < len(self._board): # no score drops from list
            # so overall number increases
                self._n += 1
            # Shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                # shift entry from j-1 to j
                # and decrement j
                self._board[j] = self._board[j-1]
                j -= 1
            # when done, add new entry
            self._board[j] = entry

# Test code
board = Scoreboard(5)
for e in (
('Rob', 750), ('Mike',1105), ('Rose', 590), ('Jill', 740),
('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400),
):
    ge = GameEntry(e[0], e[1])
    board.add(ge)
    print('After considering {0}, scoreboard is:'.format(ge))
    print(board, "\n")
