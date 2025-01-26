'''
play this game tan play mobile game
'''

import requests
import random
import os
import time

'''const'''
URL_REQUEST_NGL_API = "https://ngl.link/api/submit"
NGL_ACCOUNT_ID = "apiphon.exe2"
URL_REQUEST_LINE_API = 'https://notify-api.line.me/api/notify'
TOKEN_LINE_API = '*******************************************' #warning api end 1 april 2025
CURRENT_DIR = os.getcwd()
CREDIT_NAME = "made by Apiphol Suwanchaisakul. full stack dev See https://github.com/apiphon for more information. "
COPYRIGHT_NAME = "Copyright (c) 20xx ApiphonTutor00.org."
VER_NAME = "1.4.1"
DATE_LAST_EDIT = "24-01-2025"

def base64_encoder(plain_txt):
    '''input text output base64'''
    os.system("title base64_encoder")
    enc_txt = ""
    base64_char = {
      '000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D',
      '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H',
      '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L',
      '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P',
      '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T',
      '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X',
      '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b',
      '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f',
      '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j',
      '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n',
      '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r',
      '101100': 's', '101101': 't', '101110': 'u', '101111': 'v',
      '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z',
      '110100': '0', '110101': '1', '110110': '2', '110111': '3',
      '111000': '4', '111001': '5', '111010': '6', '111011': '7',
      '111100': '8', '111101': '9', '111110': '+', '111111': '/'
    }
    bin_txt = ''.join(format(ord(i), '08b') for i in plain_txt)
    if (len(bin_txt))%6:
        bin_txt += "0"*(6-(len(bin_txt) % 6))
    for i in range(0,len(bin_txt),6):
        enc_txt += (base64_char[bin_txt[i:i+6]])
    if len(enc_txt) %4:
        enc_txt += "="*(4-(len(enc_txt)%4))
    return enc_txt

def base64_decoder(plain_txt):
    '''input base64 output text'''
    os.system("title base64_decoder")
    plain_txt = plain_txt.strip('=')
    dec_txt = ""
    dec_bin = ""
    base64_char = {
      'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
      'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
      'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
      'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
      'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
      'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
      'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
      'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
      'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
      'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
      'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
      's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
      'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
      '0': '110100', '1': '110101', '2': '110110', '3': '110111',
      '4': '111000', '5': '111001', '6': '111010', '7': '111011',
      '8': '111100', '9': '111101', '+': '111110', '/': '111111'
    }
    for i in plain_txt:
        dec_bin += base64_char[i]
    dec_len = len(dec_bin)
    for i in range(int(dec_len/8)):
        dec_txt += (chr(int(dec_bin[i*8:((i+1)*8)], 2)))
    return dec_txt

def gamePlus():
    '''input score'''
    os.system('cls')
    answerInput = 2
    while answerInput != -1:
        allPlay,correctAnswer,minRan,maxRan = getDataFile()
        inCorrectAnswer = (allPlay - correctAnswer)
        fristPara = random.randint(minRan,maxRan)
        secPara = random.randint(minRan,maxRan)
        answerPara = fristPara + secPara
        stringMinRan = str(minRan)
        stringMaxRan = str(maxRan)
        STRING_FOR_TITLE = "title Plus : min = "+stringMinRan+", max = "+stringMaxRan
        os.system(STRING_FOR_TITLE)
        print(" You have played", allPlay, "times.", sep = " ")
        print(" Your Score Is : ",correctAnswer)
        print(" You have answered incorrectly", inCorrectAnswer, "times")
        print("\n ")
        print(" ",fristPara,"+",secPara,"=",sep = " ", end = " ")
        try:
            answerInput = float(input())
            if answerInput == answerPara:
                allPlay += 1
                correctAnswer += 1
                print(" Correct Answer!!!", end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
            elif answerInput == -1:
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
                os.system('cls')
                main()
            else:
                allPlay += 1
                print(" Wrong Answer!!!  Correct Answer Is : ",answerPara, end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
        except:
            allPlay += 1
            print(" Wrong Answer!!!  Correct Answer Is : ",answerPara)
            setDataFile(allPlay, correctAnswer, minRan, maxRan)
        print("\n *****************************************************************\n\n")

def gameMinus():
    '''minus use abs'''
    os.system('cls')
    answerInput = 2
    while answerInput != -1:
        allPlay,correctAnswer,minRan,maxRan = getDataFile()
        inCorrectAnswer = (allPlay - correctAnswer)
        fristPara = random.randint(minRan,maxRan)
        secPara = random.randint(minRan,maxRan)
        if fristPara > secPara:
            maxPara = fristPara
            minPara = secPara
        else:
            maxPara = secPara
            minPara = fristPara
        answerPara = abs(maxPara - minPara)
        stringMinRan = str(minRan)
        stringMaxRan = str(maxRan)
        STRING_FOR_TITLE = "title Minus : min = "+stringMinRan+", max = "+stringMaxRan
        os.system(STRING_FOR_TITLE)
        print(" You have played", allPlay, "times.", sep = " ")
        print(" Your Score Is : ",correctAnswer)
        print(" You have answered incorrectly", inCorrectAnswer, "times")
        print("\n ")
        print(" ",maxPara,"-",minPara,"=",sep = " ", end = " ")
        try:
            answerInput = float(input())
            if answerInput == answerPara:
                allPlay += 1
                correctAnswer += 1
                print(" Correct Answer!!!", end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
            elif answerInput == -1:
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
                os.system('cls')
                main()
            else:
                allPlay += 1
                print(" Wrong Answer!!!  Correct Answer Is : ",answerPara, end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
        except:
            allPlay += 1
            print(" Wrong Answer!!!  Correct Answer Is : ",answerPara)
            setDataFile(allPlay, correctAnswer, minRan, maxRan)
        print("\n *****************************************************************\n\n")

def gameMultiply():
    '''input score'''
    os.system('cls')
    answerInput = 2
    while answerInput != -1:
        allPlay,correctAnswer,minRan,maxRan = getDataFile()
        inCorrectAnswer = (allPlay - correctAnswer)
        fristPara = random.randint(minRan,maxRan)
        secPara = random.randint(minRan,maxRan)
        answerPara = fristPara * secPara
        stringMinRan = str(minRan)
        stringMaxRan = str(maxRan)
        STRING_FOR_TITLE = "title Plus : min = "+stringMinRan+", max = "+stringMaxRan
        os.system(STRING_FOR_TITLE)
        print(" You have played", allPlay, "times.", sep = " ")
        print(" Your Score Is : ",correctAnswer)
        print(" You have answered incorrectly", inCorrectAnswer, "times")
        print("\n ")
        print(" ",fristPara,"*",secPara,"=",sep = " ", end = " ")
        try:
            answerInput = float(input())
            if answerInput == answerPara:
                allPlay += 1
                correctAnswer += 1
                print(" Correct Answer!!!", end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
            elif answerInput == -1:
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
                os.system('cls')
                main()
            else:
                allPlay += 1
                print(" Wrong Answer!!!  Correct Answer Is : ",answerPara, end ="")
                setDataFile(allPlay, correctAnswer, minRan, maxRan)
        except:
            allPlay += 1
            print(" Wrong Answer!!!  Correct Answer Is : ",answerPara)
            setDataFile(allPlay, correctAnswer, minRan, maxRan)
        print("\n *****************************************************************\n\n")

def setting():
    '''now clearScore del files'''
    os.system('cls')
    os.system("title Setup")
    print("\n press 1 to clear score\n\n press 2 to set diff min number\n\n press 3 to set diff max number \n\n press 4 to sent score to p'Tee\n\n press 0 to back to main menu")
    print("\n\n Sel : ", end ="")
    settingInput = str(input())
    if settingInput == "1":
        clearScore()
    elif settingInput == "2":
        setMinNumber()
    elif settingInput == "3":
        setMaxNumber()
    elif settingInput == "4":
        sentConfDataDeveoper()
    else:
        main()

def clearScore():
    '''clear score to 0'''
    os.system("title clearScore")
    ff = open("__pcf.conf", "w")
    ff.write(base64_encoder("0,0,10,99"))
    ff.close()
    print(" Reset Score!!!")
    main()

def setMinNumber():
    '''set min number random'''
    os.system('cls')
    os.system("title setMinNumber")
    tim, scr, mii, mxx = getDataFile()
    os.system("title setMinNumber")
    print("\n ** Set min number **\n")
    print(" current min number is", mii)
    print(" current max number is", mxx)
    print(" Enter value -1 to back")
    print("\n Enter value for min number : ", end = "")
    try:
        RAW_NEW_MIN_RANDOM = int(input())
        if RAW_NEW_MIN_RANDOM > mxx or RAW_NEW_MIN_RANDOM < -1:
            print(" min number cannot larger than max number\n enter value again")
            setMinNumber()
        elif RAW_NEW_MIN_RANDOM == -1:
            setting()
        else:
            newMinRandom = str(RAW_NEW_MIN_RANDOM)
            setDataFile(tim, scr, newMinRandom, mxx)
            setMinNumber()
    except:
        print("invalid key")
        setMinNumber()

def setMaxNumber():
    '''set max number random'''
    os.system('cls')
    os.system("title setMaxNumber")
    tim, scr, mii, mxx = getDataFile()
    os.system("title setMaxNumber")
    print("\n ** Set max number **\n")
    print(" current min number is", mii)
    print(" current max number is", mxx)
    print(" Enter value -1 to back")
    print("\n Enter value for max number : ", end = "")
    try:
        RAW_NEW_MAX_RANDOM = int(input())
        if RAW_NEW_MAX_RANDOM < mii and RAW_NEW_MAX_RANDOM != -1:
            print(" min number cannot larger than max number\n enter value again")
            setMaxNumber()
        elif RAW_NEW_MAX_RANDOM == -1:
            setting()
        else:
            newMaxRandom = str(RAW_NEW_MAX_RANDOM)
            setDataFile(tim, scr, mii, newMaxRandom)
            setMaxNumber()
    except:
        print(" invalid key")
        setMaxNumber()

def getDataFile():
    '''get data files return n of time to play, score, min random number, max random number'''
    os.system("title getDataFile")
    if not "__pcf.conf" in os.listdir(CURRENT_DIR):
        print("Please enter your name : ", end = "")
        nameUser = str(input())
        print(" Create files completely.")
        f = open("__pcf.conf", "a")
        f.write(base64_encoder("0,0,10,99,"))
        f.close()
    fo = open("__pcf.conf", "r")
    DATA_LAST_RAW_FILE_BASE64 = fo.read()
    try:
        DATA_LAST_RAW_FILE = base64_decoder(DATA_LAST_RAW_FILE_BASE64)
        DATA_LAST_FILE = DATA_LAST_RAW_FILE.split(",")
        fo.close()
    except:
        print(" Warning do not cheat to add score by your self.")
        clearScore()
    try:
        DATA_ALL_TIME_PLAY = int(DATA_LAST_FILE[0])
        DATA_MY_SCORE = int(DATA_LAST_FILE[1])
        DATA_MIN_RANDOM_NUMBER = int(DATA_LAST_FILE[2])
        DATA_MAX_RANDOM_NUMBER = int(DATA_LAST_FILE[3])
        return DATA_ALL_TIME_PLAY, DATA_MY_SCORE, DATA_MIN_RANDOM_NUMBER, DATA_MAX_RANDOM_NUMBER
    except:
        print(" Warning do not cheat to add score by your self.")
        clearScore()

def setDataFile(newTimePlay, newScore, newMinRandomNumber, newMaxRandomNumber):
    '''sent any type and convert to string to write files'''
    os.system("title setDataFile")
    ff = open("__pcf.conf", "w")
    stringNewTimePlay = str(newTimePlay)
    stringNewScore = str(newScore)
    stringNewMinRandomNumber = str(newMinRandomNumber)
    stringNewMaxRandomNumber = str(newMaxRandomNumber)
    DATA_WRITE_TO_FLIE = stringNewTimePlay + "," + stringNewScore + "," + stringNewMinRandomNumber + "," + stringNewMaxRandomNumber
    ff.write(base64_encoder(DATA_WRITE_TO_FLIE))
    ff.close()

def getCredit():
    '''print credit name'''
    os.system('cls')
    os.system("title getCredit")
    print("\n ** credit and copyright **")
    print(" ",CREDIT_NAME,"\n")
    print(" ",COPYRIGHT_NAME, "\n All Rights Reserved.\n\n")
    print(" Press ENTER key to continue . . .")
    _ = str(input())
    main()

def sentConfDataDeveoper():
    '''sent data to me line and ngl'''
    os.system('cls')
    os.system("title sentDataToLine")
    print("Enter your name : ",end = "")
    nameStd = str(input())
    #LINE notify
    HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+TOKEN_LINE_API}
    P_DATA_ALL_TIME_PLAY, P_DATA_MY_SCORE, P_DATA_MIN_RANDOM_NUMBER, P_DATA_MAX_RANDOM_NUMBER = getDataFile()
    incorrectAnswer = P_DATA_ALL_TIME_PLAY - P_DATA_MY_SCORE
    stringReportNameHeader = "  Data of player name : " + nameStd + "\n"
    stringReportTotalPlay = "  player play game : " + str(P_DATA_ALL_TIME_PLAY) + " times\n"
    stringReportTotalScore = "  Score : "+ str(P_DATA_MY_SCORE) + "\n"
    stringReportTotalIncorrect = "  Player answer Incorrect : " + str(incorrectAnswer) + "\n" #2
    stringReportMinMax = "  diff : min = " + str(P_DATA_MIN_RANDOM_NUMBER) + ", max = " + str(P_DATA_MAX_RANDOM_NUMBER) +"\n\n"
    stringReportPlayerData = "form kidfast ver " + VER_NAME + "\npath user save is : " + CURRENT_DIR + "\n"
    #TEXT_SENT_TO_LINE = "** Report **\n\ndata of player " +nameStd + " \n\n player 'XXX' play : " + str(P_DATA_ALL_TIME_PLAY) + " times \n Score of player 'XXX' is : "+ str(P_DATA_MY_SCORE) + "\n inCorrect of player 'XXX' is : " + str(incorrectAnswer) + "\n\nconf : min = " + str(P_DATA_MIN_RANDOM_NUMBER) + ", max = " + str(P_DATA_MAX_RANDOM_NUMBER)
    TEXT_SENT_DATA = "** Report **\n\n" + stringReportNameHeader + stringReportTotalPlay + stringReportTotalScore + stringReportTotalIncorrect + stringReportMinMax + stringReportPlayerData
    _ = requests.post(URL_REQUEST_LINE_API, headers=HEADERS, data = {'message':TEXT_SENT_DATA})
    #NGL
    NGL_DATA_CONF = {'username': NGL_ACCOUNT_ID,'question': TEXT_SENT_DATA,'deviceId': '','gameSlug': '','referrer': '',}
    _ = requests.post(URL_REQUEST_NGL_API, data=NGL_DATA_CONF)
    setting()

def main():
    '''main'''
    os.system('cls')
    os.system("title Welcome")
    allPlay, saveScore, minRandomNumber, maxRandomNumber = getDataFile()
    print(" You play thime game",allPlay,"Times")
    print(" Last score is : ",saveScore)
    print(" diff min number is", minRandomNumber,"and max number is", maxRandomNumber)
    print("\n Welcome to program kid fast ( VER",VER_NAME,")")
    print("\n ** main menu **\n")
    print("\n press 1 = Game Plus Number\n\n press 2 = Game Minus Number\n\n press 3 = Game Multiply\n\n press 4 = Setup\n\n press 5 = Credit\n\n press 0 = exit\n\n Sel : ",end = "")
    os.system("title Welcome")
    modeInput = str(input())
    try:
        if modeInput == "1":
            gamePlus()
        elif modeInput == "2":
            gameMinus()
        elif modeInput == "3":
            gameMultiply()
        elif modeInput == "4":
            setting()
        elif modeInput == "5":
            getCredit()
        elif modeInput == '0':
            print("bye see u again")
            return 0
        else:
            os.system('cls')
            main()
    except:
        print("invalid key")
        main()
main()
