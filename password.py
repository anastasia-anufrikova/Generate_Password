import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def generate_password(length, chars):
    for i in range(how_much):
        print('Включать ли цифры?')
        numbers = input().lower()
        if numbers == 'да':
            chars += digits
        print('Включать ли прописные буквы?')
        big_letters = input().lower()
        if big_letters == 'да':
            chars += uppercase_letters
        print('Включать ли строчные буквы?')
        small_letters = input().lower()
        if small_letters == 'да':
            chars += lowercase_letters
        print('Включать ли символы?')
        symbols = input().lower()
        if symbols == 'да':
            chars += punctuation
        password = random.sample(chars, length)
        return password
        
        
print('Сколько паролей нужно сгенерировать?')
how_much = int(input())
print('Введите длину пароля:')
length = int(input())
for j in range(how_much):
    print(*(generate_password(length, chars)), sep='')
