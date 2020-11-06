class Dna:
    def __init__(self, word):
        self.word = word
        self.letters = [i for i in self.word]
        self.unique = self.create_unique(self.letters)

    def create_unique(self, letters):
        unique_dict = {}
        for i in letters:
            unique_dict[i] = 0

        return unique_dict

    @property
    def count_unique(self):
        unique_table = self.unique
        for i in self.letters:
            unique_table[i] += 1

        return " ".join(str(x) for x in unique_table.values())


def main():
    wordset = input("Please input your word for counting\n=> ")

    game = Dna(wordset)
    print(game.count_unique)


if __name__ == "__main__":
    main()