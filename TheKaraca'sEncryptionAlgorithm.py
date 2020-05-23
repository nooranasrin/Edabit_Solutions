def encrypt(string):
    alternatives = {'a': 0, 'e': 1, 'o': 2, 'u': 3}
    reverse = string[::-1]
    new_string = ''
    for character in reverse:
        new_string += f'{alternatives.get(character, character)}'
    return new_string + 'aca'


print(encrypt('apple'))
print(encrypt('banana'))
print(encrypt('karaca'))
