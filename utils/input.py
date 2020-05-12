def inputWPM():
    wpm = 60
    print("Enter a target WPM: ")

    while(True):
        wpm = int(input())
        if (wpm > 0) :
            break;
        else :
            print("Please enter a value greater than 0:")
    return wpm;