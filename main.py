import time
from essential_generators import DocumentGenerator

def typing_speed():
    
    # Generate random sentence
    gen = DocumentGenerator()
    String = gen.sentence()
    wordcount = len(String.split())
    
    # Typing speed calculation
    print(String)
    print("----------------------------------------")
    start_time = time.time()
    textInput = str(input("Type the sentence: "))
    endTime = time.time()
    acc = len(set(textInput.split()) & set(String.split()))
    acc = acc / wordcount*100
    timeTaken = round(endTime - start_time, 2)
    wpm = round((wordcount / timeTaken)* 60)
    print("----------------------------------------")
    
    # show the result 
    print("Your accuracy is: ", acc)
    print("Time Taken: ", timeTaken, "s")
    print("Your typing speed is: ", wpm, "wpm")

    if acc < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif acc < 80 or wpm < 60:
        print("You're doing great")
    elif acc <= 100 or wpm <= 100:
        print("You're pro in typing!")
    else:
        "You're typing machine"

if __name__ == "__main__":
    print("Let's start")
    typing_speed()

    while True:
        if input("Do you want to try again? (y/n): ") == "y":
            print('\n')
            typing_speed()
        else:
            print("Typing has been ended")
            break