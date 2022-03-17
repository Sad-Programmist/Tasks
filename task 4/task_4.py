def correction(text, words):
    for word in text.split():
        for correct_word in words.split():
            if len(word) > 2 and comparison(word, correct_word):
                new_word = correct_word + "".join(word[len(correct_word):])
                if word[0].isupper():
                    new_word = new_word.capitalize()
                text = text.replace(word, new_word)
                break
    return text


def comparison(word, correct_word):
    result = 0
    for correct_letter, letter in zip(word.lower(), correct_word.lower()):
        if letter != correct_letter:
            result += 1
        if result > 1:
            return False
    return True


def read(name):
    with open(name, "r", encoding='utf-8') as f:
        return f.readline().replace("\n", ""), f.readline()


if __name__ == '__main__':
    name = "input files/input5.txt"
    text, words = read(name)
    print("Input text: " + text)
    print("Correct words: " + words)
    print("Output text: " + correction(text, words))
