def play(word, geussWord):
    geuss = str(input("Enter a letter: "))
    count = 0
    for x in word:
        if geuss == x:
            geussWord[count] = geuss
        count += 1

def main():
    randWord = "Testicals"
    geusses = 0
    maxGeusses = (len(randWord) - 1)

    #word = list(randWord)??????
    word = []
    geussWord = []
    for x in randWord:
        word.append(x)
        geussWord.append("-")

    while word != geussWord:
        if geusses < maxGeusses:
            play(word, geussWord)
            print("Good geuss....")
            print(word)
            print(geussWord)
            geusses += 1
        else:
            print("You lose!")
            break


if __name__ == "__main__":
    main()