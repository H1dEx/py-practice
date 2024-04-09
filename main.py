import random

class Game:
    maxErrors = 5

    def __init__(self):
        self.errors = 0
        f = open('./words.txt', 'r', encoding='utf')
        # print(f.read())
        words = []

        for line in f:
            words.append(line.strip())

        f.close()

        self.secret_word = words[random.randint(0, len(words) - 1)]
        self.current_word = '_' * len(self.secret_word)
        print(f'Game starts!')

        while self.errors < self.maxErrors and self.current_word != self.secret_word:
            self.step()
        else:
            print(
                f'Game over! Answer is {self.secret_word}.',
                f'{'You won!' if self.current_word == self.secret_word else 'You lost!'}')

    def step(self):
        print(f'{self.get_status()}')
        char = ''
        while len(char) != 1:
            temp = input('Enter a letter\n').strip()
            if temp.isalpha() and len(temp) == 1:
                char = temp
            else:
                print(f'Incorrect value, your prompt is "{temp}"')

        if char.lower() in self.secret_word.lower():
            print('Write letter!')
            self.current_word = self.change_current_word(char)
        else:
            print('Wrong letter :(')
            self.errors += 1

    def change_current_word(self, char):
        temp = ''
        for i in range(len(self.secret_word)):
            if self.secret_word[i].lower() == char.lower():
                temp += self.secret_word[i]
            else:
                temp += self.current_word[i]
        return temp

    def get_status(self):
        return f'Your word is: {self.current_word}'


Game()
