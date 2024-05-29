import random

print('Добро пожаловать в числовую угадайку!')
print()

def guess_the_number():
    limit = int(input('В каком диапазоне мне загадать число? От 1 до '))
    print()

    print('Хм... Значит от 1 до', str(limit) + '? Что ж, давай попробуем')
    print()

    hidden_number = random.randint(1, limit)

    try_count = 0

    while 1 == 1:
        answer = input('Какое число я загадал? ')
        if answer.isdigit():
            try_count += 1
            answer = int(answer)
            if answer < hidden_number:
                print('Маловато. Думай дальше!')
                print()
            elif answer> hidden_number:
                print('Слишком много! Еще подумай')
                print()
            elif answer == hidden_number:
                print()
                print('Ты угадал, поздавляю!')
                print()
                print('Тебе для этого потребовалось', try_count, 'попыток')
                print()
                break
        else:
            print('А может все-таки введешь именно ЧИСЛО?')
            print()

guess_the_number()

while 1 == 1:
    purpose = input('Ну что, сыграешь еще раз? ')
    print()
    if purpose == 'да':
        guess_the_number()
    else:
        print('Салага...')
        break