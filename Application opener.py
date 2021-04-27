from os import*
from pyttsx3 import*
speak("Hello and Welcome")
speak('This program can do the following things')
print('This program allows you to open the applications mentioned below. If u face any error then it maybe because the file was not installed in your system')
print()
print("\t 1)MSWORD \t 2)POWERPOINT\n \t 3)CHROME \t 4)MSEDGE \n \t 5)QUIT")
print()
speak('these are the rules ')
print('Rules:You can enter the first three words or the full file name or the number beside it ')

speak("please enter you input as per the rules mentioned above")
while True:
    b=input("enter the name of the application u want to open: ").strip()
    a=b.upper()
    try:
        if (a=='MSWORD') or (a=='1') or (a=='MSW'):
            speak("Opening MICROSOFT WORD")
            print('opening.............')
            startfile('WINWORD.EXE')

        elif (a=='POWERPOINT') or (a=='2') or (a=='POW'):
            speak("Opening POWERPOINT")
            print('opening.............')
            startfile("POWERPNT.EXE")
        elif (a=='CHROME') or (a=='3') or (a=='CHR'):
            speak("Opening Google chrome")
            print('opening.............')
            startfile("chrome.exe")
        elif (a=='MSEDGE') or (a=='4') or (a=='MSE'):
            speak("Opening MICROSOFT EDGE")
            print('opening.............')
            startfile("msedge.exe")
        elif (a=='QUIT') or (a=='5') or (a=='QUI'):
            speak('Thank You for using')
            break
        else:
            speak('please enter input from the rules as mentioned ')
            print('Go through the rules')
    except:
        print()
        print('Error:File maybe not be present in your system')
