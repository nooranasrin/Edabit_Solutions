def encrypt(string):
    reverse = string[::-1]
    new_string = reverse.maketrans('aeou', '0123')
    return reverse.translate(new_string) + 'aca'


def main():
    print(encrypt('apple'))
    print(encrypt('banana'))
    print(encrypt('karaca'))


main()

