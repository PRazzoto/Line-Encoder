def stringToBin(string):
    binary_result = ""

    for char in string:
        # Pega o Unicode e converte para binário, removendo o 0b
        string_binary = bin(ord(char))[2:].zfill(8)

        binary_result += string_binary

    return binary_result


def binToString(binary_string):
    # Dividindo a string em chunks de 8 bits
    chunks = [binary_string[i : i + 8] for i in range(0, len(binary_string), 8)]

    # Converte para decimal cada chunk de 8 bits
    decimal = [int(chunk, 2) for chunk in chunks]

    # Converte cada int para o seu correspondente em ASCII
    letters = [chr(value) for value in decimal]

    final_string = "".join(letters)

    return final_string


def binToHex(binary_string):
    decimal = int(binary_string, 2)
    hexadecimal = hex(decimal)

    return hexadecimal


def hexToBin(hexadecimal_str):
    decimal = int(hexadecimal_str, 16)
    binary_str = bin(decimal)[2:]

    return binary_str.zfill(len(hexadecimal_str) * 4)


def encode8b6t(hexadecimal_str):
    hexadecimal = hex(int(hexadecimal_str, base=16))

    result = []
    array00 = [-1, 1, 0, 0, -1, 1]
    array01 = [0, -1, 1, -1, 1, 0]
    array02 = [0, -1, 1, 0, -1, 1]
    array03 = [0, -1, 1, 1, 0, -1]
    array04 = [-1, 1, 0, 1, 0, -1]
    array05 = [1, 0, -1, -1, 1, 0]
    array06 = [1, 0, -1, 0, -1, 1]
    array07 = [1, 0, -1, 1, 0, -1]
    array08 = [-1, 1, 0, 0, 1, -1]
    array09 = [0, -1, 1, 1, -1, 0]
    array0A = [0, -1, 1, 0, 1, -1]
    array0B = [0, -1, 1, -1, 0, 1]
    array0C = [-1, 1, 0, -1, 0, 1]
    array0D = [1, 0, -1, 1, -1, 0]
    array0E = [1, 0, -1, 0, 1, -1]
    array0F = [1, 0, -1, -1, 0, 1]
    array10 = [0, -1, -1, 1, 0, 1]
    array11 = [-1, 0, -1, 0, 1, 1]
    array12 = [-1, 0, -1, 1, 0, 1]
    array13 = [-1, 0, -1, 1, 1, 0]
    array14 = [0, -1, -1, 1, 1, 0]
    array15 = [-1, -1, 0, 0, 1, 1]
    array16 = [-1, -1, 0, 1, 0, 1]
    array17 = [-1, -1, 0, 1, 1, 0]
    array18 = [-1, 1, 0, -1, 1, 0]
    array19 = [1, -1, 0, -1, 1, 0]
    array1A = [-1, 1, 1, -1, 1, 0]
    array1B = [1, 0, 0, -1, 1, 0]
    array1C = [1, 0, 0, 1, -1, 0]
    array1D = [-1, 1, 1, 1, -1, 0]
    array1E = [1, -1, 0, 1, -1, 0]
    array1F = [-1, 1, 0, 1, -1, 0]
    array20 = [-1, 1, 1, -1, 0, 0]
    array21 = [1, 0, 0, 1, -1, -1]
    array22 = [-1, 1, 0, -1, 1, 1]
    array23 = [1, -1, 0, -1, 1, 1]
    array24 = [1, -1, 0, 1, 0, 0]
    array25 = [-1, 1, 0, 1, 0, 0]
    array26 = [1, 0, 0, -1, 0, 0]
    array27 = [-1, 1, 1, 1, -1, -1]
    array28 = [0, 1, 1, -1, 0, -1]
    array29 = [1, 0, 1, 0, -1, -1]
    array2A = [1, 0, 1, -1, 0, -1]
    array2B = [1, 0, 1, -1, -1, 0]
    array2C = [0, 1, 1, -1, -1, 0]
    array2D = [1, 1, 0, 0, -1, -1]
    array2E = [1, 1, 0, -1, 0, -1]
    array2F = [1, 1, 0, -1, -1, 0]
    array30 = [1, -1, 0, 0, -1, 1]
    array31 = [0, 1, -1, -1, 1, 0]
    array32 = [0, 1, -1, 0, -1, 1]
    array33 = [0, 1, -1, 1, 0, -1]
    array34 = [1, -1, 0, 1, 0, -1]
    array35 = [-1, 0, 1, -1, 1, 0]
    array36 = [-1, 0, 1, 0, -1, 1]
    array37 = [-1, 0, 1, 1, 0, -1]
    array38 = [1, -1, 0, 0, 1, -1]
    array39 = [0, 1, -1, 1, -1, 0]
    array3A = [0, 1, -1, 0, 1, -1]
    array3B = [0, 1, -1, -1, 0, 1]
    array3C = [1, -1, 0, -1, 0, 1]
    array3D = [-1, 0, 1, 1, -1, 0]
    array3E = [-1, 0, 1, 0, 1, -1]
    array3F = [-1, 0, 1, -1, 0, 1]
    array40 = [-1, 0, 0, 1, 0, 1]
    array41 = [0, -1, 0, 0, 1, 1]
    array42 = [0, -1, 0, 1, 0, 1]
    array43 = [0, -1, 0, 1, 1, 0]
    array44 = [-1, 0, 0, 1, 1, 0]
    array45 = [0, 0, -1, 0, 1, 1]
    array46 = [0, 0, -1, 1, 0, 1]
    array47 = [0, 0, -1, 1, 1, 0]
    array48 = [0, 0, 1, 0, 0, 0]
    array49 = [1, 1, -1, 0, 0, 0]
    array4A = [1, -1, 1, 0, 0, 0]
    array4B = [-1, 1, 1, 0, 0, 0]
    array4C = [0, 1, -1, 0, 0, 0]
    array4D = [1, 0, -1, 0, 0, 0]
    array4E = [0, -1, 1, 0, 0, 0]
    array4F = [-1, 0, 1, 0, 0, 0]
    array50 = [1, -1, -1, 1, 0, 1]
    array51 = [-1, 1, -1, 0, 1, 1]
    array52 = [-1, 1, -1, 1, 0, 1]
    array53 = [-1, 1, -1, 1, 1, 0]
    array54 = [1, -1, -1, 1, 1, 0]
    array55 = [-1, -1, 1, 0, 1, 1]
    array56 = [-1, -1, 1, 1, 0, 1]
    array57 = [-1, -1, 1, 1, 1, 0]
    array58 = [-1, -1, 0, 1, 1, 1]
    array59 = [-1, 0, -1, 1, 1, 1]
    array5A = [0, -1, -1, 1, 1, 1]
    array5B = [0, -1, -1, 0, 1, 1]
    array5C = [1, -1, -1, 0, 1, 1]
    array5D = [-1, 0, 0, 0, 1, 1]
    array5E = [0, 1, 1, 1, -1, -1]
    array5F = [0, 1, 1, 1, -1, -1]
    array60 = [0, 1, 1, 0, -1, 0]
    array61 = [1, 0, 1, -1, 0, 0]
    array62 = [1, 0, 1, 0, -1, 0]
    array63 = [1, 0, 1, 0, 0, -1]
    array64 = [0, 1, 1, 0, 0, -1]
    array65 = [1, 1, 0, -1, 0, 0]
    array66 = [1, 1, 0, 0, -1, 0]
    array67 = [1, 1, 0, 0, 0, -1]
    array68 = [0, 1, 1, -1, 1, -1]
    array69 = [1, 0, 1, 1, -1, -1]
    array6A = [1, 0, 1, -1, 1, -1]
    array6B = [1, 0, 1, -1, -1, 1]
    array6C = [0, 1, 1, -1, -1, 1]
    array6D = [1, 1, 0, 1, -1, -1]
    array6E = [1, 1, 0, -1, 1, -1]
    array6F = [1, 1, 0, -1, -1, 1]
    array70 = [0, 0, 0, 1, 1, -1]
    array71 = [0, 0, 0, 1, -1, 1]
    array72 = [0, 0, 0, -1, 1, 1]
    array73 = [0, 0, 0, 1, 0, 0]
    array74 = [0, 0, 0, 1, 0, -1]
    array75 = [0, 0, 0, 1, -1, 0]
    array76 = [0, 0, 0, -1, 0, 1]
    array77 = [0, 0, 0, -1, 1, 0]
    array78 = [1, 1, 1, -1, -1, 0]
    array79 = [1, 1, 1, -1, 0, -1]
    array7A = [1, 1, 1, 0, -1, -1]
    array7B = [0, 1, 1, 0, -1, -1]
    array7C = [-1, 0, 0, -1, 1, 1]
    array7D = [-1, 0, 0, 1, 0, 0]
    array7E = [1, -1, -1, -1, 1, 1]
    array7F = [1, -1, -1, 1, 0, 0]
    array80 = [-1, 0, 0, 1, -1, 1]
    array81 = [0, -1, 0, -1, 1, 1]
    array82 = [0, -1, 0, 1, -1, 1]
    array83 = [0, -1, 0, 1, 1, -1]
    array84 = [-1, 0, 0, 1, 1, -1]
    array85 = [0, 0, -1, -1, 1, 1]
    array86 = [0, 0, -1, 1, -1, 1]
    array87 = [0, 0, -1, 1, 1, -1]
    array88 = [-1, 0, 0, 0, 1, 0]
    array89 = [0, -1, 0, 1, 0, 0]
    array8A = [0, -1, 0, 0, 1, 0]
    array8B = [0, -1, 0, 0, 0, 1]
    array8C = [-1, 0, 0, 0, 0, 1]
    array8D = [0, 0, -1, 1, 0, 0]
    array8E = [0, 0, -1, 0, 1, 0]
    array8F = [0, 0, -1, 0, 0, 1]
    array90 = [1, -1, -1, 1, -1, 1]
    array91 = [-1, 1, -1, -1, 1, 1]
    array92 = [-1, 1, -1, 1, -1, 1]
    array93 = [-1, 1, -1, 1, 1, -1]
    array94 = [1, -1, -1, 1, 1, -1]
    array95 = [-1, -1, 1, -1, 1, 1]
    array96 = [-1, -1, 1, 1, -1, 1]
    array97 = [-1, -1, 1, 1, 1, -1]
    array98 = [1, -1, -1, 0, 1, 0]
    array99 = [-1, 1, -1, 1, 0, 0]
    array9A = [-1, 1, -1, 0, 1, 0]
    array9B = [-1, 1, -1, 0, 0, 1]
    array9C = [1, -1, -1, 0, 0, 1]
    array9D = [-1, -1, 1, 1, 0, 0]
    array9E = [-1, -1, 1, 0, 1, 0]
    array9F = [-1, -1, 1, 0, 0, 1]
    arrayA0 = [-1, 1, 1, 0, -1, 0]
    arrayA1 = [1, -1, 1, -1, 0, 0]
    arrayA2 = [1, -1, 1, 0, -1, 0]
    arrayA3 = [1, -1, 1, 0, 0, -1]
    arrayA4 = [-1, 1, 1, 0, -1]
    arrayA5 = [1, 1, -1, -1, 0, 0]
    arrayA6 = [1, 1, -1, 0, -1, 0]
    arrayA7 = [1, 1, -1, 0, 0, -1]
    arrayA8 = [-1, 1, 1, -1, 1, -1]
    arrayA9 = [1, -1, 1, 1, -1, -1]
    arrayAA = [1, -1, 1, -1, 1, -1]
    arrayAB = [1, -1, 1, -1, -1, 1]
    arrayAC = [-1, 1, 1, -1, -1, 1]
    arrayAD = [1, 1, -1, 1, -1, -1]
    arrayAE = [1, 1, -1, -1, 1, -1]
    arrayAF = [1, 1, -1, -1, -1, 1]
    arrayB0 = [1, 0, 0, 0, -1, 0]
    arrayB1 = [0, 1, 0, -1, 0, 0]
    arrayB2 = [0, 1, 0, 0, -1, 0]
    arrayB3 = [0, 1, 0, 0, 0, -1]
    arrayB4 = [1, 0, 0, 0, 0, -1]
    arrayB5 = [0, 0, 1, -1, 0, 0]
    arrayB6 = [0, 0, 1, 0, -1, 0]
    arrayB7 = [0, 0, 1, 0, 0, -1]
    arrayB8 = [1, 0, 0, -1, 1, -1]
    arrayB9 = [0, 1, 0, 1, -1, -1]
    arrayBA = [0, 1, 0, -1, 1, -1]
    arrayBB = [0, 1, 0, -1, -1, 1]
    arrayBC = [1, 0, 0, -1, -1, 1]
    arrayBD = [0, 0, 1, 1, -1, -1]
    arrayBE = [0, 0, 1, -1, 1, -1]
    arrayBF = [0, 0, 1, -1, -1, 1]
    arrayC0 = [-1, 1, 0, 1, -1, 1]
    arrayC1 = [0, -1, 1, -1, 1, 1]
    arrayC2 = [0, -1, 1, 1, -1, 1]
    arrayC3 = [0, -1, 1, 1, 1, -1]
    arrayC4 = [-1, 1, 0, 1, 1, -1]
    arrayC5 = [1, 0, -1, -1, 1, 1]
    arrayC6 = [1, 0, -1, 1, -1, 1]
    arrayC7 = [1, 0, -1, 1, 1, -1]
    arrayC8 = [-1, 1, 0, 0, 1, 0]
    arrayC9 = [0, -1, 1, 1, 0, 0]
    arrayCA = [0, -1, 1, 1, 0, 0]
    arrayCB = [0, -1, 1, 0, 0, 1]
    arrayCC = [-1, 1, 0, 0, 0, 1]
    arrayCD = [1, 0, -1, 1, 0, 0]
    arrayCE = [1, 0, -1, 0, 1, 0]
    arrayCF = [1, 0, -1, 0, 0, 1]
    arrayD0 = [1, -1, 0, 1, -1, 1]
    arrayD1 = [0, 1, -1, -1, 1, 1]
    arrayD2 = [0, 1, -1, 1, -1, 1]
    arrayD3 = [0, 1, -1, 1, 1, -1]
    arrayD4 = [1, -1, 0, 1, 1, -1]
    arrayD5 = [-1, 0, 1, -1, 1, 1]
    arrayD6 = [-1, 0, 1, 1, -1, 1]
    arrayD7 = [-1, 0, 1, 1, 1, -1]
    arrayD8 = [1, -1, 0, 0, 1, 0]
    arrayD9 = [0, 1, -1, 1, 0, 0]
    arrayDA = [0, 1, -1, 0, 1, 0]
    arrayDB = [0, 1, -1, 0, 0, 1]
    arrayDC = [1, -1, 0, 0, 0, 1]
    arrayDD = [-1, 0, 1, 1, 0, 0]
    arrayDE = [-1, 0, 1, 0, 1, 0]
    arrayDF = [-1, 0, 1, 0, 0, 1]
    arrayE0 = [-1, 1, 1, 0, -1, 1]
    arrayE1 = [1, -1, 1, -1, 1, 0]
    arrayE2 = [1, -1, 1, 0, -1, 1]
    arrayE3 = [1, -1, 1, 1, 0, -1]
    arrayE4 = [-1, 1, 1, 1, 0, -1]
    arrayE5 = [1, 1, -1, -1, 1, 0]
    arrayE6 = [1, 1, -1, 0, -1, 1]
    arrayE7 = [1, 1, -1, 1, 0, -1]
    arrayE8 = [-1, 1, 1, 0, 1, -1]
    arrayE9 = [1, -1, 1, 1, -1, 0]
    arrayEA = [1, -1, 1, 0, 1, -1]
    arrayEB = [1, -1, 1, -1, 0, 1]
    arrayEC = [-1, 1, 1, -1, 0, 1]
    arrayED = [1, 1, -1, 1, -1, 0]
    arrayEE = [1, 1, -1, 0, 1, -1]
    arrayEF = [1, 1, -1, -1, 0, 1]
    arrayF0 = [1, 0, 0, 0, -1, 1]
    arrayF1 = [0, 1, 0, -1, 1, 0]
    arrayF2 = [0, 1, 0, 0, -1, 1]
    arrayF3 = [0, 1, 0, 1, 0, -1]
    arrayF4 = [1, 0, 0, 1, 0, -1]
    arrayF5 = [0, 0, 1, -1, 1, 0]
    arrayF6 = [0, 0, 1, 0, -1, 1]
    arrayF7 = [0, 0, 1, 1, 0, -1]
    arrayF8 = [1, 0, 0, 0, 1, -1]
    arrayF9 = [0, 1, 0, 1, -1, 0]
    arrayFA = [0, 1, 0, 0, 1, -1]
    arrayFB = [0, 1, 0, -1, 0, 1]
    arrayFC = [1, 0, 0, -1, 0, 1]
    arrayFD = [0, 0, 1, 1, -1, 0]
    arrayFE = [0, 0, 1, 0, 1, -1]
    arrayFF = [0, 0, 1, -1, 0, 1]

    if hexadecimal == hex(0):
        result.append(array00)
    if hexadecimal == hex(1):
        result.append(array01)
    if hexadecimal == hex(2):
        result.append(array02)
    if hexadecimal == hex(3):
        result.append(array03)
    if hexadecimal == hex(4):
        result.append(array04)
    if hexadecimal == hex(5):
        result.append(array05)
    if hexadecimal == hex(6):
        result.append(array06)
    if hexadecimal == hex(7):
        result.append(array07)
    if hexadecimal == hex(8):
        result.append(array08)
    if hexadecimal == hex(9):
        result.append(array09)
    if hexadecimal == hex(10):
        result.append(array0A)
    if hexadecimal == hex(11):
        result.append(array0B)
    if hexadecimal == hex(12):
        result.append(array0C)
    if hexadecimal == hex(13):
        result.append(array0D)
    if hexadecimal == hex(14):
        result.append(array0E)
    if hexadecimal == hex(15):
        result.append(array0F)
    if hexadecimal == hex(16):
        result.append(array10)
    if hexadecimal == hex(17):
        result.append(array11)
    if hexadecimal == hex(18):
        result.append(array12)
    if hexadecimal == hex(19):
        result.append(array13)
    if hexadecimal == hex(20):
        result.append(array14)
    if hexadecimal == hex(21):
        result.append(array15)
    if hexadecimal == hex(22):
        result.append(array16)
    if hexadecimal == hex(23):
        result.append(array17)
    if hexadecimal == hex(24):
        result.append(array18)
    if hexadecimal == hex(25):
        result.append(array19)
    if hexadecimal == hex(26):
        result.append(array1A)
    if hexadecimal == hex(27):
        result.append(array1B)
    if hexadecimal == hex(28):
        result.append(array1C)
    if hexadecimal == hex(29):
        result.append(array1D)
    if hexadecimal == hex(30):
        result.append(array1E)
    if hexadecimal == hex(31):
        result.append(array1F)
    if hexadecimal == hex(32):
        result.append(array20)
    if hexadecimal == hex(33):
        result.append(array21)
    if hexadecimal == hex(34):
        result.append(array22)
    if hexadecimal == hex(35):
        result.append(array23)
    if hexadecimal == hex(36):
        result.append(array24)
    if hexadecimal == hex(37):
        result.append(array25)
    if hexadecimal == hex(38):
        result.append(array26)
    if hexadecimal == hex(39):
        result.append(array27)
    if hexadecimal == hex(40):
        result.append(array28)
    if hexadecimal == hex(41):
        result.append(array29)
    if hexadecimal == hex(42):
        result.append(array2A)
    if hexadecimal == hex(43):
        result.append(array2B)
    if hexadecimal == hex(44):
        result.append(array2C)
    if hexadecimal == hex(45):
        result.append(array2D)
    if hexadecimal == hex(46):
        result.append(array2E)
    if hexadecimal == hex(47):
        result.append(array2F)
    if hexadecimal == hex(48):
        result.append(array30)
    if hexadecimal == hex(49):
        result.append(array31)
    if hexadecimal == hex(50):
        result.append(array32)
    if hexadecimal == hex(51):
        result.append(array33)
    if hexadecimal == hex(52):
        result.append(array34)
    if hexadecimal == hex(53):
        result.append(array35)
    if hexadecimal == hex(54):
        result.append(array36)
    if hexadecimal == hex(55):
        result.append(array37)
    if hexadecimal == hex(56):
        result.append(array38)
    if hexadecimal == hex(57):
        result.append(array39)
    if hexadecimal == hex(58):
        result.append(array3A)
    if hexadecimal == hex(59):
        result.append(array3B)
    if hexadecimal == hex(60):
        result.append(array3C)
    if hexadecimal == hex(61):
        result.append(array3D)
    if hexadecimal == hex(62):
        result.append(array3E)
    if hexadecimal == hex(63):
        result.append(array3F)
    if hexadecimal == hex(64):
        result.append(array40)
    if hexadecimal == hex(65):
        result.append(array41)
    if hexadecimal == hex(66):
        result.append(array42)
    if hexadecimal == hex(67):
        result.append(array43)
    if hexadecimal == hex(68):
        result.append(array44)
    if hexadecimal == hex(69):
        result.append(array45)
    if hexadecimal == hex(70):
        result.append(array46)
    if hexadecimal == hex(71):
        result.append(array47)
    if hexadecimal == hex(72):
        result.append(array48)
    if hexadecimal == hex(73):
        result.append(array49)
    if hexadecimal == hex(74):
        result.append(array4A)
    if hexadecimal == hex(75):
        result.append(array4B)
    if hexadecimal == hex(76):
        result.append(array4C)
    if hexadecimal == hex(77):
        result.append(array4D)
    if hexadecimal == hex(78):
        result.append(array4E)
    if hexadecimal == hex(79):
        result.append(array4F)
    if hexadecimal == hex(80):
        result.append(array50)
    if hexadecimal == hex(81):
        result.append(array51)
    if hexadecimal == hex(82):
        result.append(array52)
    if hexadecimal == hex(83):
        result.append(array53)
    if hexadecimal == hex(84):
        result.append(array54)
    if hexadecimal == hex(85):
        result.append(array55)
    if hexadecimal == hex(86):
        result.append(array56)
    if hexadecimal == hex(87):
        result.append(array57)
    if hexadecimal == hex(88):
        result.append(array58)
    if hexadecimal == hex(89):
        result.append(array59)
    if hexadecimal == hex(90):
        result.append(array5A)
    if hexadecimal == hex(91):
        result.append(array5B)
    if hexadecimal == hex(92):
        result.append(array5C)
    if hexadecimal == hex(93):
        result.append(array5D)
    if hexadecimal == hex(94):
        result.append(array5E)
    if hexadecimal == hex(95):
        result.append(array5F)
    if hexadecimal == hex(96):
        result.append(array60)
    if hexadecimal == hex(97):
        result.append(array61)
    if hexadecimal == hex(98):
        result.append(array62)
    if hexadecimal == hex(99):
        result.append(array63)
    if hexadecimal == hex(100):
        result.append(array64)
    if hexadecimal == hex(101):
        result.append(array65)
    if hexadecimal == hex(102):
        result.append(array66)
    if hexadecimal == hex(103):
        result.append(array67)
    if hexadecimal == hex(104):
        result.append(array68)
    if hexadecimal == hex(105):
        result.append(array69)
    if hexadecimal == hex(106):
        result.append(array6A)
    if hexadecimal == hex(107):
        result.append(array6B)
    if hexadecimal == hex(108):
        result.append(array6C)
    if hexadecimal == hex(109):
        result.append(array6D)
    if hexadecimal == hex(110):
        result.append(array6E)
    if hexadecimal == hex(111):
        result.append(array6F)
    if hexadecimal == hex(112):
        result.append(array70)
    if hexadecimal == hex(113):
        result.append(array71)
    if hexadecimal == hex(114):
        result.append(array72)
    if hexadecimal == hex(115):
        result.append(array73)
    if hexadecimal == hex(116):
        result.append(array74)
    if hexadecimal == hex(117):
        result.append(array75)
    if hexadecimal == hex(118):
        result.append(array76)
    if hexadecimal == hex(119):
        result.append(array77)
    if hexadecimal == hex(120):
        result.append(array78)
    if hexadecimal == hex(121):
        result.append(array79)
    if hexadecimal == hex(122):
        result.append(array7A)
    if hexadecimal == hex(123):
        result.append(array7B)
    if hexadecimal == hex(124):
        result.append(array7C)
    if hexadecimal == hex(125):
        result.append(array7D)
    if hexadecimal == hex(126):
        result.append(array7E)
    if hexadecimal == hex(127):
        result.append(array7F)
    if hexadecimal == hex(128):
        result.append(array80)
    if hexadecimal == hex(129):
        result.append(array81)
    if hexadecimal == hex(130):
        result.append(array82)
    if hexadecimal == hex(131):
        result.append(array83)
    if hexadecimal == hex(132):
        result.append(array84)
    if hexadecimal == hex(133):
        result.append(array85)
    if hexadecimal == hex(134):
        result.append(array86)
    if hexadecimal == hex(135):
        result.append(array87)
    if hexadecimal == hex(136):
        result.append(array88)
    if hexadecimal == hex(137):
        result.append(array89)
    if hexadecimal == hex(138):
        result.append(array8A)
    if hexadecimal == hex(139):
        result.append(array8B)
    if hexadecimal == hex(140):
        result.append(array8C)
    if hexadecimal == hex(141):
        result.append(array8D)
    if hexadecimal == hex(142):
        result.append(array8E)
    if hexadecimal == hex(143):
        result.append(array8F)
    if hexadecimal == hex(144):
        result.append(array90)
    if hexadecimal == hex(145):
        result.append(array91)
    if hexadecimal == hex(146):
        result.append(array92)
    if hexadecimal == hex(147):
        result.append(array93)
    if hexadecimal == hex(148):
        result.append(array94)
    if hexadecimal == hex(149):
        result.append(array95)
    if hexadecimal == hex(150):
        result.append(array96)
    if hexadecimal == hex(151):
        result.append(array97)
    if hexadecimal == hex(152):
        result.append(array98)
    if hexadecimal == hex(153):
        result.append(array99)
    if hexadecimal == hex(154):
        result.append(array9A)
    if hexadecimal == hex(155):
        result.append(array9B)
    if hexadecimal == hex(156):
        result.append(array9C)
    if hexadecimal == hex(157):
        result.append(array9D)
    if hexadecimal == hex(158):
        result.append(array9E)
    if hexadecimal == hex(159):
        result.append(array9F)
    if hexadecimal == hex(160):
        result.append(arrayA0)
    if hexadecimal == hex(161):
        result.append(arrayA1)
    if hexadecimal == hex(162):
        result.append(arrayA2)
    if hexadecimal == hex(163):
        result.append(arrayA3)
    if hexadecimal == hex(164):
        result.append(arrayA4)
    if hexadecimal == hex(165):
        result.append(arrayA5)
    if hexadecimal == hex(166):
        result.append(arrayA6)
    if hexadecimal == hex(167):
        result.append(arrayA7)
    if hexadecimal == hex(168):
        result.append(arrayA8)
    if hexadecimal == hex(169):
        result.append(arrayA9)
    if hexadecimal == hex(170):
        result.append(arrayAA)
    if hexadecimal == hex(171):
        result.append(arrayAB)
    if hexadecimal == hex(172):
        result.append(arrayAC)
    if hexadecimal == hex(173):
        result.append(arrayAD)
    if hexadecimal == hex(174):
        result.append(arrayAE)
    if hexadecimal == hex(175):
        result.append(arrayAF)
    if hexadecimal == hex(176):
        result.append(arrayB0)
    if hexadecimal == hex(177):
        result.append(arrayB1)
    if hexadecimal == hex(178):
        result.append(arrayB2)
    if hexadecimal == hex(179):
        result.append(arrayB3)
    if hexadecimal == hex(180):
        result.append(arrayB4)
    if hexadecimal == hex(181):
        result.append(arrayB5)
    if hexadecimal == hex(182):
        result.append(arrayB6)
    if hexadecimal == hex(183):
        result.append(arrayB7)
    if hexadecimal == hex(184):
        result.append(arrayB8)
    if hexadecimal == hex(185):
        result.append(arrayB9)
    if hexadecimal == hex(186):
        result.append(arrayBA)
    if hexadecimal == hex(187):
        result.append(arrayBB)
    if hexadecimal == hex(188):
        result.append(arrayBC)
    if hexadecimal == hex(189):
        result.append(arrayBD)
    if hexadecimal == hex(190):
        result.append(arrayBE)
    if hexadecimal == hex(191):
        result.append(arrayBF)
    if hexadecimal == hex(192):
        result.append(arrayC0)
    if hexadecimal == hex(193):
        result.append(arrayC1)
    if hexadecimal == hex(194):
        result.append(arrayC2)
    if hexadecimal == hex(195):
        result.append(arrayC3)
    if hexadecimal == hex(196):
        result.append(arrayC4)
    if hexadecimal == hex(197):
        result.append(arrayC5)
    if hexadecimal == hex(198):
        result.append(arrayC6)
    if hexadecimal == hex(199):
        result.append(arrayC7)
    if hexadecimal == hex(200):
        result.append(arrayC8)
    if hexadecimal == hex(201):
        result.append(arrayC9)
    if hexadecimal == hex(202):
        result.append(arrayCA)
    if hexadecimal == hex(203):
        result.append(arrayCB)
    if hexadecimal == hex(204):
        result.append(arrayCC)
    if hexadecimal == hex(205):
        result.append(arrayCD)
    if hexadecimal == hex(206):
        result.append(arrayCE)
    if hexadecimal == hex(207):
        result.append(arrayCF)
    if hexadecimal == hex(208):
        result.append(arrayD0)
    if hexadecimal == hex(209):
        result.append(arrayD1)
    if hexadecimal == hex(210):
        result.append(arrayD2)
    if hexadecimal == hex(211):
        result.append(arrayD3)
    if hexadecimal == hex(212):
        result.append(arrayD4)
    if hexadecimal == hex(213):
        result.append(arrayD5)
    if hexadecimal == hex(214):
        result.append(arrayD6)
    if hexadecimal == hex(215):
        result.append(arrayD7)
    if hexadecimal == hex(216):
        result.append(arrayD8)
    if hexadecimal == hex(217):
        result.append(arrayD9)
    if hexadecimal == hex(218):
        result.append(arrayDA)
    if hexadecimal == hex(219):
        result.append(arrayDB)
    if hexadecimal == hex(220):
        result.append(arrayDC)
    if hexadecimal == hex(221):
        result.append(arrayDD)
    if hexadecimal == hex(222):
        result.append(arrayDE)
    if hexadecimal == hex(223):
        result.append(arrayDF)
    if hexadecimal == hex(224):
        result.append(arrayE0)
    if hexadecimal == hex(225):
        result.append(arrayE1)
    if hexadecimal == hex(226):
        result.append(arrayE2)
    if hexadecimal == hex(227):
        result.append(arrayE3)
    if hexadecimal == hex(228):
        result.append(arrayE4)
    if hexadecimal == hex(229):
        result.append(arrayE5)
    if hexadecimal == hex(230):
        result.append(arrayE6)
    if hexadecimal == hex(231):
        result.append(arrayE7)
    if hexadecimal == hex(232):
        result.append(arrayE8)
    if hexadecimal == hex(233):
        result.append(arrayE9)
    if hexadecimal == hex(234):
        result.append(arrayEA)
    if hexadecimal == hex(235):
        result.append(arrayEB)
    if hexadecimal == hex(236):
        result.append(arrayEC)
    if hexadecimal == hex(237):
        result.append(arrayED)
    if hexadecimal == hex(238):
        result.append(arrayEE)
    if hexadecimal == hex(239):
        result.append(arrayEF)
    if hexadecimal == hex(240):
        result.append(arrayF0)
    if hexadecimal == hex(241):
        result.append(arrayF1)
    if hexadecimal == hex(242):
        result.append(arrayF2)
    if hexadecimal == hex(243):
        result.append(arrayF3)
    if hexadecimal == hex(244):
        result.append(arrayF4)
    if hexadecimal == hex(245):
        result.append(arrayF5)
    if hexadecimal == hex(246):
        result.append(arrayF6)
    if hexadecimal == hex(247):
        result.append(arrayF7)
    if hexadecimal == hex(248):
        result.append(arrayF8)
    if hexadecimal == hex(249):
        result.append(arrayF9)
    if hexadecimal == hex(250):
        result.append(arrayFA)
    if hexadecimal == hex(251):
        result.append(arrayFB)
    if hexadecimal == hex(252):
        result.append(arrayFC)
    if hexadecimal == hex(253):
        result.append(arrayFD)
    if hexadecimal == hex(254):
        result.append(arrayFE)
    if hexadecimal == hex(255):
        result.append(arrayFF)
    return result


def decode8b6t(msg):
    result = ""

    if msg == [-1, 1, 0, 0, -1, 1]:
        result += hex(0)[2:]
    if msg == [0, -1, 1, -1, 1, 0]:
        result += hex(1)[2:]
    if msg == [0, -1, 1, 0, -1, 1]:
        result += hex(2)[2:]
    if msg == [0, -1, 1, 1, 0, -1]:
        result += hex(3)[2:]
    if msg == [-1, 1, 0, 1, 0, -1]:
        result += hex(4)[2:]
    if msg == [1, 0, -1, -1, 1, 0]:
        result += hex(5)[2:]
    if msg == [1, 0, -1, 0, -1, 1]:
        result += hex(6)[2:]
    if msg == [1, 0, -1, 1, 0, -1]:
        result += hex(7)[2:]
    if msg == [-1, 1, 0, 0, 1, -1]:
        result += hex(8)[2:]
    if msg == [0, -1, 1, 1, -1, 0]:
        result += hex(9)[2:]
    if msg == [0, -1, 1, 0, 1, -1]:
        result += hex(10)[2:]
    if msg == [0, -1, 1, -1, 0, 1]:
        result += hex(11)[2:]
    if msg == [-1, 1, 0, -1, 0, 1]:
        result += hex(12)[2:]
    if msg == [1, 0, -1, 1, -1, 0]:
        result += hex(13)[2:]
    if msg == [1, 0, -1, 0, 1, -1]:
        result += hex(14)[2:]
    if msg == [1, 0, -1, -1, 0, 1]:
        result += hex(15)[2:]
    if msg == [0, -1, -1, 1, 0, 1]:
        result += hex(16)[2:]
    if msg == [-1, 0, -1, 0, 1, 1]:
        result += hex(17)[2:]
    if msg == [-1, 0, -1, 1, 0, 1]:
        result += hex(18)[2:]
    if msg == [-1, 0, -1, 1, 1, 0]:
        result += hex(19)[2:]
    if msg == [0, -1, -1, 1, 1, 0]:
        result += hex(20)[2:]
    if msg == [-1, -1, 0, 0, 1, 1]:
        result += hex(21)[2:]
    if msg == [-1, -1, 0, 1, 0, 1]:
        result += hex(22)[2:]
    if msg == [-1, -1, 0, 1, 1, 0]:
        result += hex(23)[2:]
    if msg == [-1, 1, 0, -1, 1, 0]:
        result += hex(24)[2:]
    if msg == [1, -1, 0, -1, 1, 0]:
        result += hex(25)[2:]
    if msg == [-1, 1, 1, -1, 1, 0]:
        result += hex(26)[2:]
    if msg == [1, 0, 0, -1, 1, 0]:
        result += hex(27)[2:]
    if msg == [1, 0, 0, 1, -1, 0]:
        result += hex(28)[2:]
    if msg == [-1, 1, 1, 1, -1, 0]:
        result += hex(29)[2:]
    if msg == [1, -1, 0, 1, -1, 0]:
        result += hex(30)[2:]
    if msg == [-1, 1, 0, 1, -1, 0]:
        result += hex(31)[2:]
    if msg == [-1, 1, 1, -1, 0, 0]:
        result += hex(32)[2:]
    if msg == [1, 0, 0, 1, -1, -1]:
        result += hex(33)[2:]
    if msg == [-1, 1, 0, -1, 1, 1]:
        result += hex(34)[2:]
    if msg == [1, -1, 0, -1, 1, 1]:
        result += hex(35)[2:]
    if msg == [1, -1, 0, 1, 0, 0]:
        result += hex(36)[2:]
    if msg == [-1, 1, 0, 1, 0, 0]:
        result += hex(37)[2:]
    if msg == [1, 0, 0, -1, 0, 0]:
        result += hex(38)[2:]
    if msg == [-1, 1, 1, 1, -1, -1]:
        result += hex(39)[2:]
    if msg == [0, 1, 1, -1, 0, -1]:
        result += hex(40)[2:]
    if msg == [1, 0, 1, 0, -1, -1]:
        result += hex(41)[2:]
    if msg == [1, 0, 1, -1, 0, -1]:
        result += hex(42)[2:]
    if msg == [1, 0, 1, -1, -1, 0]:
        result += hex(43)[2:]
    if msg == [0, 1, 1, -1, -1, 0]:
        result += hex(44)[2:]
    if msg == [1, 1, 0, 0, -1, -1]:
        result += hex(45)[2:]
    if msg == [1, 1, 0, -1, 0, -1]:
        result += hex(46)[2:]
    if msg == [1, 1, 0, -1, -1, 0]:
        result += hex(47)[2:]
    if msg == [1, -1, 0, 0, -1, 1]:
        result += hex(48)[2:]
    if msg == [0, 1, -1, -1, 1, 0]:
        result += hex(49)[2:]
    if msg == [0, 1, -1, 0, -1, 1]:
        result += hex(50)[2:]
    if msg == [0, 1, -1, 1, 0, -1]:
        result += hex(51)[2:]
    if msg == [1, -1, 0, 1, 0, -1]:
        result += hex(52)[2:]
    if msg == [-1, 0, 1, -1, 1, 0]:
        result += hex(53)[2:]
    if msg == [-1, 0, 1, 0, -1, 1]:
        result += hex(54)[2:]
    if msg == [-1, 0, 1, 1, 0, -1]:
        result += hex(55)[2:]
    if msg == [1, -1, 0, 0, 1, -1]:
        result += hex(56)[2:]
    if msg == [0, 1, -1, 1, -1, 0]:
        result += hex(57)[2:]
    if msg == [0, 1, -1, 0, 1, -1]:
        result += hex(58)[2:]
    if msg == [0, 1, -1, -1, 0, 1]:
        result += hex(59)[2:]
    if msg == [1, -1, 0, -1, 0, 1]:
        result += hex(60)[2:]
    if msg == [-1, 0, 1, 1, -1, 0]:
        result += hex(61)[2:]
    if msg == [-1, 0, 1, 0, 1, -1]:
        result += hex(62)[2:]
    if msg == [-1, 0, 1, -1, 0, 1]:
        result += hex(63)[2:]
    if msg == [-1, 0, 0, 1, 0, 1]:
        result += hex(64)[2:]
    if msg == [0, -1, 0, 0, 1, 1]:
        result += hex(65)[2:]
    if msg == [0, -1, 0, 1, 0, 1]:
        result += hex(66)[2:]
    if msg == [0, -1, 0, 1, 1, 0]:
        result += hex(67)[2:]
    if msg == [-1, 0, 0, 1, 1, 0]:
        result += hex(68)[2:]
    if msg == [0, 0, -1, 0, 1, 1]:
        result += hex(69)[2:]
    if msg == [0, 0, -1, 1, 0, 1]:
        result += hex(70)[2:]
    if msg == [0, 0, -1, 1, 1, 0]:
        result += hex(71)[2:]
    if msg == [0, 0, 1, 0, 0, 0]:
        result += hex(72)[2:]
    if msg == [1, 1, -1, 0, 0, 0]:
        result += hex(73)[2:]
    if msg == [1, -1, 1, 0, 0, 0]:
        result += hex(74)[2:]
    if msg == [-1, 1, 1, 0, 0, 0]:
        result += hex(75)[2:]
    if msg == [0, 1, -1, 0, 0, 0]:
        result += hex(76)[2:]
    if msg == [1, 0, -1, 0, 0, 0]:
        result += hex(77)[2:]
    if msg == [0, -1, 1, 0, 0, 0]:
        result += hex(78)[2:]
    if msg == [-1, 0, 1, 0, 0, 0]:
        result += hex(79)[2:]
    if msg == [1, -1, -1, 1, 0, 1]:
        result += hex(80)[2:]
    if msg == [-1, 1, -1, 0, 1, 1]:
        result += hex(81)[2:]
    if msg == [-1, 1, -1, 1, 0, 1]:
        result += hex(82)[2:]
    if msg == [-1, 1, -1, 1, 1, 0]:
        result += hex(83)[2:]
    if msg == [1, -1, -1, 1, 1, 0]:
        result += hex(84)[2:]
    if msg == [-1, -1, 1, 0, 1, 1]:
        result += hex(85)[2:]
    if msg == [-1, -1, 1, 1, 0, 1]:
        result += hex(86)[2:]
    if msg == [-1, -1, 1, 1, 1, 0]:
        result += hex(87)[2:]
    if msg == [-1, -1, 0, 1, 1, 1]:
        result += hex(88)[2:]
    if msg == [-1, 0, -1, 1, 1, 1]:
        result += hex(89)[2:]
    if msg == [0, -1, -1, 1, 1, 1]:
        result += hex(90)[2:]
    if msg == [0, -1, -1, 0, 1, 1]:
        result += hex(91)[2:]
    if msg == [1, -1, -1, 0, 1, 1]:
        result += hex(92)[2:]
    if msg == [-1, 0, 0, 0, 1, 1]:
        result += hex(93)[2:]
    if msg == [0, 1, 1, 1, -1, -1]:
        result += hex(94)[2:]
    if msg == [0, 1, 1, 1, -1, -1]:
        result += hex(95)[2:]
    if msg == [0, 1, 1, 0, -1, 0]:
        result += hex(96)[2:]
    if msg == [1, 0, 1, -1, 0, 0]:
        result += hex(97)[2:]
    if msg == [1, 0, 1, 0, -1, 0]:
        result += hex(98)[2:]
    if msg == [1, 0, 1, 0, 0, -1]:
        result += hex(99)[2:]
    if msg == [0, 1, 1, 0, 0, -1]:
        result += hex(100)[2:]
    if msg == [1, 1, 0, -1, 0, 0]:
        result += hex(101)[2:]
    if msg == [1, 1, 0, 0, -1, 0]:
        result += hex(102)[2:]
    if msg == [1, 1, 0, 0, 0, -1]:
        result += hex(103)[2:]
    if msg == [0, 1, 1, -1, 1, -1]:
        result += hex(104)[2:]
    if msg == [1, 0, 1, 1, -1, -1]:
        result += hex(105)[2:]
    if msg == [1, 0, 1, -1, 1, -1]:
        result += hex(106)[2:]
    if msg == [1, 0, 1, -1, -1, 1]:
        result += hex(107)[2:]
    if msg == [0, 1, 1, -1, -1, 1]:
        result += hex(108)[2:]
    if msg == [1, 1, 0, 1, -1, -1]:
        result += hex(109)[2:]
    if msg == [1, 1, 0, -1, 1, -1]:
        result += hex(110)[2:]
    if msg == [1, 1, 0, -1, -1, 1]:
        result += hex(111)[2:]
    if msg == [0, 0, 0, 1, 1, -1]:
        result += hex(112)[2:]
    if msg == [0, 0, 0, 1, -1, 1]:
        result += hex(113)[2:]
    if msg == [0, 0, 0, -1, 1, 1]:
        result += hex(114)[2:]
    if msg == [0, 0, 0, 1, 0, 0]:
        result += hex(115)[2:]
    if msg == [0, 0, 0, 1, 0, -1]:
        result += hex(116)[2:]
    if msg == [0, 0, 0, 1, -1, 0]:
        result += hex(117)[2:]
    if msg == [0, 0, 0, -1, 0, 1]:
        result += hex(118)[2:]
    if msg == [0, 0, 0, -1, 1, 0]:
        result += hex(119)[2:]
    if msg == [1, 1, 1, -1, -1, 0]:
        result += hex(120)[2:]
    if msg == [1, 1, 1, -1, 0, -1]:
        result += hex(121)[2:]
    if msg == [1, 1, 1, 0, -1, -1]:
        result += hex(122)[2:]
    if msg == [0, 1, 1, 0, -1, -1]:
        result += hex(123)[2:]
    if msg == [-1, 0, 0, -1, 1, 1]:
        result += hex(124)[2:]
    if msg == [-1, 0, 0, 1, 0, 0]:
        result += hex(125)[2:]
    if msg == [1, -1, -1, -1, 1, 1]:
        result += hex(126)[2:]
    if msg == [1, -1, -1, 1, 0, 0]:
        result += hex(127)[2:]
    if msg == [-1, 0, 0, 1, -1, 1]:
        result += hex(128)[2:]
    if msg == [0, -1, 0, -1, 1, 1]:
        result += hex(129)[2:]
    if msg == [0, -1, 0, 1, -1, 1]:
        result += hex(130)[2:]
    if msg == [0, -1, 0, 1, 1, -1]:
        result += hex(131)[2:]
    if msg == [-1, 0, 0, 1, 1, -1]:
        result += hex(132)[2:]
    if msg == [0, 0, -1, -1, 1, 1]:
        result += hex(133)[2:]
    if msg == [0, 0, -1, 1, -1, 1]:
        result += hex(134)[2:]
    if msg == [0, 0, -1, 1, 1, -1]:
        result += hex(135)[2:]
    if msg == [-1, 0, 0, 0, 1, 0]:
        result += hex(136)[2:]
    if msg == [0, -1, 0, 1, 0, 0]:
        result += hex(137)[2:]
    if msg == [0, -1, 0, 0, 1, 0]:
        result += hex(138)[2:]
    if msg == [0, -1, 0, 0, 0, 1]:
        result += hex(139)[2:]
    if msg == [-1, 0, 0, 0, 0, 1]:
        result += hex(140)[2:]
    if msg == [0, 0, -1, 1, 0, 0]:
        result += hex(141)[2:]
    if msg == [0, 0, -1, 0, 1, 0]:
        result += hex(142)[2:]
    if msg == [0, 0, -1, 0, 0, 1]:
        result += hex(143)[2:]
    if msg == [1, -1, -1, 1, -1, 1]:
        result += hex(144)[2:]
    if msg == [-1, 1, -1, -1, 1, 1]:
        result += hex(145)[2:]
    if msg == [-1, 1, -1, 1, -1, 1]:
        result += hex(146)[2:]
    if msg == [-1, 1, -1, 1, 1, -1]:
        result += hex(147)[2:]
    if msg == [1, -1, -1, 1, 1, -1]:
        result += hex(148)[2:]
    if msg == [-1, -1, 1, -1, 1, 1]:
        result += hex(149)[2:]
    if msg == [-1, -1, 1, 1, -1, 1]:
        result += hex(150)[2:]
    if msg == [-1, -1, 1, 1, 1, -1]:
        result += hex(151)[2:]
    if msg == [1, -1, -1, 0, 1, 0]:
        result += hex(152)[2:]
    if msg == [-1, 1, -1, 1, 0, 0]:
        result += hex(153)[2:]
    if msg == [-1, 1, -1, 0, 1, 0]:
        result += hex(154)[2:]
    if msg == [-1, 1, -1, 0, 0, 1]:
        result += hex(155)[2:]
    if msg == [1, -1, -1, 0, 0, 1]:
        result += hex(156)[2:]
    if msg == [-1, -1, 1, 1, 0, 0]:
        result += hex(157)[2:]
    if msg == [-1, -1, 1, 0, 1, 0]:
        result += hex(158)[2:]
    if msg == [-1, -1, 1, 0, 0, 1]:
        result += hex(159)[2:]
    if msg == [-1, 1, 1, 0, -1, 0]:
        result += hex(160)[2:]
    if msg == [1, -1, 1, -1, 0, 0]:
        result += hex(161)[2:]
    if msg == [1, -1, 1, 0, -1, 0]:
        result += hex(162)[2:]
    if msg == [1, -1, 1, 0, 0, -1]:
        result += hex(163)[2:]
    if msg == [-1, 1, 1, 0, -1]:
        result += hex(164)[2:]
    if msg == [1, 1, -1, -1, 0, 0]:
        result += hex(165)[2:]
    if msg == [1, 1, -1, 0, -1, 0]:
        result += hex(166)[2:]
    if msg == [1, 1, -1, 0, 0, -1]:
        result += hex(167)[2:]
    if msg == [-1, 1, 1, -1, 1, -1]:
        result += hex(168)[2:]
    if msg == [1, -1, 1, 1, -1, -1]:
        result += hex(169)[2:]
    if msg == [1, -1, 1, -1, 1, -1]:
        result += hex(170)[2:]
    if msg == [1, -1, 1, -1, -1, 1]:
        result += hex(171)[2:]
    if msg == [-1, 1, 1, -1, -1, 1]:
        result += hex(172)[2:]
    if msg == [1, 1, -1, 1, -1, -1]:
        result += hex(173)[2:]
    if msg == [1, 1, -1, -1, 1, -1]:
        result += hex(174)[2:]
    if msg == [1, 1, -1, -1, -1, 1]:
        result += hex(175)[2:]
    if msg == [1, 0, 0, 0, -1, 0]:
        result += hex(176)[2:]
    if msg == [0, 1, 0, -1, 0, 0]:
        result += hex(177)[2:]
    if msg == [0, 1, 0, 0, -1, 0]:
        result += hex(178)[2:]
    if msg == [0, 1, 0, 0, 0, -1]:
        result += hex(179)[2:]
    if msg == [1, 0, 0, 0, 0, -1]:
        result += hex(180)[2:]
    if msg == [0, 0, 1, -1, 0, 0]:
        result += hex(181)[2:]
    if msg == [0, 0, 1, 0, -1, 0]:
        result += hex(182)[2:]
    if msg == [0, 0, 1, 0, 0, -1]:
        result += hex(183)[2:]
    if msg == [1, 0, 0, -1, 1, -1]:
        result += hex(184)[2:]
    if msg == [0, 1, 0, 1, -1, -1]:
        result += hex(185)[2:]
    if msg == [0, 1, 0, -1, 1, -1]:
        result += hex(186)[2:]
    if msg == [0, 1, 0, -1, -1, 1]:
        result += hex(187)[2:]
    if msg == [1, 0, 0, -1, -1, 1]:
        result += hex(188)[2:]
    if msg == [0, 0, 1, 1, -1, -1]:
        result += hex(189)[2:]
    if msg == [0, 0, 1, -1, 1, -1]:
        result += hex(190)[2:]
    if msg == [0, 0, 1, -1, -1, 1]:
        result += hex(191)[2:]
    if msg == [-1, 1, 0, 1, -1, 1]:
        result += hex(192)[2:]
    if msg == [0, -1, 1, -1, 1, 1]:
        result += hex(193)[2:]
    if msg == [0, -1, 1, 1, -1, 1]:
        result += hex(194)[2:]
    if msg == [0, -1, 1, 1, 1, -1]:
        result += hex(195)[2:]
    if msg == [-1, 1, 0, 1, 1, -1]:
        result += hex(196)[2:]
    if msg == [1, 0, -1, -1, 1, 1]:
        result += hex(197)[2:]
    if msg == [1, 0, -1, 1, -1, 1]:
        result += hex(198)[2:]
    if msg == [1, 0, -1, 1, 1, -1]:
        result += hex(199)[2:]
    if msg == [-1, 1, 0, 0, 1, 0]:
        result += hex(200)[2:]
    if msg == [0, -1, 1, 1, 0, 0]:
        result += hex(201)[2:]
    if msg == [0, -1, 1, 1, 0, 0]:
        result += hex(202)[2:]
    if msg == [0, -1, 1, 0, 0, 1]:
        result += hex(203)[2:]
    if msg == [-1, 1, 0, 0, 0, 1]:
        result += hex(204)[2:]
    if msg == [1, 0, -1, 1, 0, 0]:
        result += hex(205)[2:]
    if msg == [1, 0, -1, 0, 1, 0]:
        result += hex(206)[2:]
    if msg == [1, 0, -1, 0, 0, 1]:
        result += hex(207)[2:]
    if msg == [1, -1, 0, 1, -1, 1]:
        result += hex(208)[2:]
    if msg == [0, 1, -1, -1, 1, 1]:
        result += hex(209)[2:]
    if msg == [0, 1, -1, 1, -1, 1]:
        result += hex(210)[2:]
    if msg == [0, 1, -1, 1, 1, -1]:
        result += hex(211)[2:]
    if msg == [1, -1, 0, 1, 1, -1]:
        result += hex(212)[2:]
    if msg == [-1, 0, 1, -1, 1, 1]:
        result += hex(213)[2:]
    if msg == [-1, 0, 1, 1, -1, 1]:
        result += hex(214)[2:]
    if msg == [-1, 0, 1, 1, 1, -1]:
        result += hex(215)[2:]
    if msg == [1, -1, 0, 0, 1, 0]:
        result += hex(216)[2:]
    if msg == [0, 1, -1, 1, 0, 0]:
        result += hex(217)[2:]
    if msg == [0, 1, -1, 0, 1, 0]:
        result += hex(218)[2:]
    if msg == [0, 1, -1, 0, 0, 1]:
        result += hex(219)[2:]
    if msg == [1, -1, 0, 0, 0, 1]:
        result += hex(220)[2:]
    if msg == [-1, 0, 1, 1, 0, 0]:
        result += hex(221)[2:]
    if msg == [-1, 0, 1, 0, 1, 0]:
        result += hex(222)[2:]
    if msg == [-1, 0, 1, 0, 0, 1]:
        result += hex(223)[2:]
    if msg == [-1, 1, 1, 0, -1, 1]:
        result += hex(224)[2:]
    if msg == [1, -1, 1, -1, 1, 0]:
        result += hex(225)[2:]
    if msg == [1, -1, 1, 0, -1, 1]:
        result += hex(226)[2:]
    if msg == [1, -1, 1, 1, 0, -1]:
        result += hex(227)[2:]
    if msg == [-1, 1, 1, 1, 0, -1]:
        result += hex(228)[2:]
    if msg == [1, 1, -1, -1, 1, 0]:
        result += hex(229)[2:]
    if msg == [1, 1, -1, 0, -1, 1]:
        result += hex(230)[2:]
    if msg == [1, 1, -1, 1, 0, -1]:
        result += hex(231)[2:]
    if msg == [-1, 1, 1, 0, 1, -1]:
        result += hex(232)[2:]
    if msg == [1, -1, 1, 1, -1, 0]:
        result += hex(233)[2:]
    if msg == [1, -1, 1, 0, 1, -1]:
        result += hex(234)[2:]
    if msg == [1, -1, 1, -1, 0, 1]:
        result += hex(235)[2:]
    if msg == [-1, 1, 1, -1, 0, 1]:
        result += hex(236)[2:]
    if msg == [1, 1, -1, 1, -1, 0]:
        result += hex(237)[2:]
    if msg == [1, 1, -1, 0, 1, -1]:
        result += hex(238)[2:]
    if msg == [1, 1, -1, -1, 0, 1]:
        result += hex(239)[2:]
    if msg == [1, 0, 0, 0, -1, 1]:
        result += hex(240)[2:]
    if msg == [0, 1, 0, -1, 1, 0]:
        result += hex(241)[2:]
    if msg == [0, 1, 0, 0, -1, 1]:
        result += hex(242)[2:]
    if msg == [0, 1, 0, 1, 0, -1]:
        result += hex(243)[2:]
    if msg == [1, 0, 0, 1, 0, -1]:
        result += hex(244)[2:]
    if msg == [0, 0, 1, -1, 1, 0]:
        result += hex(245)[2:]
    if msg == [0, 0, 1, 0, -1, 1]:
        result += hex(246)[2:]
    if msg == [0, 0, 1, 1, 0, -1]:
        result += hex(247)[2:]
    if msg == [1, 0, 0, 0, 1, -1]:
        result += hex(248)[2:]
    if msg == [0, 1, 0, 1, -1, 0]:
        result += hex(249)[2:]
    if msg == [0, 1, 0, 0, 1, -1]:
        result += hex(250)[2:]
    if msg == [0, 1, 0, -1, 0, 1]:
        result += hex(251)[2:]
    if msg == [1, 0, 0, -1, 0, 1]:
        result += hex(252)[2:]
    if msg == [0, 0, 1, 1, -1, 0]:
        result += hex(253)[2:]
    if msg == [0, 0, 1, 0, 1, -1]:
        result += hex(254)[2:]
    if msg == [0, 0, 1, -1, 0, 1]:
        result += hex(255)[2:]

    return result
