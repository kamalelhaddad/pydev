def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string

def mutate_string2(string, position, character):
    result = list(string)
    result[position] = character
    return ''.join(result)

if __name__ == '__main__':
    mutate_string2("abracadabra", 5, "k")