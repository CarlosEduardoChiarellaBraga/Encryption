#letter that will be recognized by the encrypt algorithm
alf = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', ':', '!', '.', '(', ')', '*', '/', '+', '-', '@', '?', '#']

#Function to track the current index of the key on the encryption or decryption
def AddCurrent(key, current):
    if current+1 < len(key):
        return current+1
    return 0

def Encrypt(txt: str, key: int):
    key = PutKeyInPairs(key)
    current = 0
    txt_ret = ''
    txt = txt.upper()
    for n in range(0, len(txt)):
        index = alf.index(txt[n])
        final_value = index + key[current]
        current = AddCurrent(key, current)
        while final_value >= len(alf):
            final_value -= len(alf) #49 --> 0, #50 --> 1, #51 --> 2, for an alf of len 49

        txt_ret += alf[final_value]
    return txt_ret

def Decrypt(txt: str, key: int):
    key = PutKeyInPairs(key)
    current = 0
    decripted_txt = ''
    txt = txt.upper()
    for n in range(0, len(txt)):
        index = alf.index(txt[n])
        while key[current] > index:
            index += len(alf)
        index = index - key[current]
        decripted_txt += alf[index]
        current = AddCurrent(key, current)
    return decripted_txt

#IsOdd will be user on PutKeyInPairs()
def IsOdd(num):
    if num % 2 == 1:
        return True
    return False

#function to put an int (the key) in pairs on a list
def PutKeyInPairs(key: int):
    key = str(key)
    if IsOdd(len(key)):
        key += "0"
    lst = []
    for n in range(1, len(key), 2):
        lst.append(int(key[n-1]+key[n]))
    return lst


text = input('Text: ')
key = int(input('Key: '))

txt = Encrypt(text, key)
print(txt)
txt = Decrypt(txt, key)
print(txt)
