def stringToBin(string):
    binary_result = ""

    for char in string:
        # Pega o Unicode e converte para binário, removendo o 0b
        string_binary = bin(ord(char))[2:].zfill(8)

        binary_result += string_binary

    return binary_result


input_string = "Café"
# print(stringToBin(input_string))


def binToString(binary_string):
    # Dividindo a string em chunks de 8 bits
    chunks = [binary_string[i : i + 8] for i in range(0, len(binary_string), 8)]

    # Converte para decimal cada chunk de 8 bits
    decimal = [int(chunk, 2) for chunk in chunks]

    # Converte cada int para o seu correspondente em ASCII
    letters = [chr(value) for value in decimal]

    final_string = "".join(letters)

    return final_string


bin_string = "01100011011000010110011011101001"
# print(binToString(bin_string))


def binToHex(binary_string):
    decimal = int(binary_string, 2)
    hexadecimal = hex(decimal)

    return hexadecimal
