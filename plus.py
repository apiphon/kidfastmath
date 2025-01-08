'''
play this game tan play mobile game
algo = readfiles get in vari and del files when answer write in files.
'''
import random
import os
'''const'''
CURRENT_DIR = os.getcwd()
CREDIT_NAME = "Apiphol Suwanchaisakul"
VER_NAME = "1.0.2"
DATE_LAST_EDIT = "07-01-2025"

def base64_encoder(plain_txt):
    '''input text output base64'''
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

#def game(allPlay)
def game(correctAnswer):
    '''input score'''
    #inCorrectAnswer = allPlay - correctAnswer
    os.system('cls')
    while True:
        fristPara = random.randint(10,99)
        secPara = random.randint(10,99)
        answerPara = fristPara + secPara
        print("Your Score Is : ",correctAnswer)
        print(fristPara,"+",secPara,"=",sep = " ", end = "")
        try:
            answerInput = float(input())
            if answerInput == answerPara:
                correctAnswer += 1
                ff = open("__pcf.conf", "w")
                ff.write(base64_encoder(str(correctAnswer)))
                ff.close()
                print("Correct Answer!!!", end ="")
            elif answerInput == -1:
                ff = open("__pcf.conf", "w")
                ff.write(base64_encoder(str(correctAnswer)))
                ff.close()
                return "blabbbbb"
            else:
                print("Wrong Answer!!!  Correct Answer Is : ",answerPara)
                ff = open("__pcf.conf", "w")
                ff.write(base64_encoder(str(correctAnswer)))
                ff.close()
        except:
            print("Wrong Answer!!!  Correct Answer Is : ",answerPara)
            ff = open("__pcf.conf", "w")
            ff.write(base64_encoder(str(correctAnswer)))
            ff.close()
        print("\n*****************************************************************\n\n")

def setting():
    os.system('cls')
    '''now clearScore del files'''
    print("\npress 1 to clear score()\n\npress 0 to back to main menu")
    settingInput = str(input())
    if settingInput == "1":
        clearScore()
    else:
        main()

def clearScore():
    '''clear score to 0'''
    ff = open("__pcf.conf", "w")
    ff.write(base64_encoder("0"))
    ff.close()
    print("Reset Score!!!")
    main()


def main():
    '''main'''
    os.system('cls')
    if not "__pcf.conf" in os.listdir(CURRENT_DIR):
        print("Create files completely.")
        f = open("__pcf.conf", "a")
        f.write(base64_encoder("0"))
        f.close()
    fo = open("__pcf.conf", "r")
    DATA_LAST_RAW_FLIE_BASE64 = fo.read()
    try:
        DATA_LAST_RAW_FLIE = base64_decoder(DATA_LAST_RAW_FLIE_BASE64)
        fo.close()
    except:
        print("Warning do not cheat to add score by your self.")
        clearScore()
    try:
        saveScore = int(DATA_LAST_RAW_FLIE)
    except:
        print("Warning do not cheat to add score by your self.")
        clearScore()
    print("Last score is : ",saveScore)
    print("Welcome to program add math.")
    print("\n\n press 1 = playgame\n\n press 2 = setup\n\n press 3 = credit\n\n press 0 = exit\n\n Sel : ",end = "")
    modeInput = str(input())
    try:
        if modeInput == "1":
            game(saveScore)
            #game(timeOfPlay)
        elif modeInput == "2":
            setting()
        elif modeInput == "3":
            print(CREDIT_NAME, VER_NAME)
            main()
        elif modeInput == "0":
            print("bye see u again")
        else:
            os.system('cls')
            main()
    except:
        print("invalid key")
        main()
main()
