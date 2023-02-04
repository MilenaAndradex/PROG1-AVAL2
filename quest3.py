# Antonio Guilherme de Brito
# Milena Andrade da Costa
from sys import stdin


def main():
    while (True):
        word = stdin.readline().strip().replace('\n', '')
        if word == "None" or word == "":
            break
        table = {
            "aist": ["futuro", "5a"],
            "est": ["pretérito", "5a"],
            "ais": ["futuro", "2a"],
            "aem": ["futuro", "4a"],
            "aim": ["futuro", "6a"],
            "ons": ["presente", "5a"],
            "om": ["presente", "4a"],
            "am": ["presente", "6a"],
            "ei": ["pretérito", "1a"],
            "es": ["pretérito", "2a"],
            "em": ["pretérito", "4a"],
            "im": ["pretérito", "6a"],
            "os": ["presente", "2a"],
            "ai": ["futuro", "1a"],
            "o": ["presente", "1a"],
            "a": ["presente", "3a"],
            "e": ["pretérito", "3a"],
            "i": ["futuro", "3a"]
        }
        for conjunction, [time, person] in table.items():
            if word[-len(conjunction):] == conjunction:
                verb = word[:-len(conjunction)] + "en"
                print("%s - verb %s, %s %s pessoa" %
                      (word, verb, time, person))
                break
        else:
            print('%s - não é um tempo verbal' % (word))


if __name__ == "__main__":
    main()
