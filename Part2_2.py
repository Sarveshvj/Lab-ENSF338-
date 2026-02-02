vowels = 0
words = 0
start = False
lines = []

def read_into_list():
    with open('pg2701.txt', 'r', encoding='utf-8') as File:
        for line in File:
            lines.append(line)

def count():
    global vowels, words, start
    for line in lines:
        if line == "CHAPTER 1. Loomings.\n":
            start = True
        if start:
            for word in line.split():
                for char in word:
                    if char in "aeiouyAEIOUY":
                        vowels += 1
                words += 1

def compute_average():
    return vowels / words

def main():
    read_into_list()
    count()
    average_vowels = compute_average()
    print(average_vowels)

main()