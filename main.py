import random

koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)

print("Поиграем в блэк джек?")
count = 0
botCount = 0

while True:
    language = input('English или Русский язык? en/ru\n')
    if language == 'en':
        count = 0
        botCount = 0
        while True:
            choice = input('Will you take a card? y/n\n')

            if choice == 'y':
                current = koloda.pop()
                print('You got a face value card %d' % current)
                count += current

                if count > 21:
                    print('Sorry, your score is over 21, you lost!')
                    print('Your score: %d points' % count)
                    break

                elif count == 21:
                    print('Congratulations, you scored 21 points!')
                    print('Your opponent automatically lost!')
                    print('The game is over!')
                    break

                else:
                    print('Your score: %d points' % count)

            elif choice == 'n' and count < 21:
                botCount = random.randint(1, 21)
                print('Game over, your have score: %d points!' % count)
                print('Your opponent score: %d points' % botCount)
                if count > botCount:
                    print('Your opponent lost!')
                elif count < botCount:
                    print('Your opponent win!')
                count = 0
                botCount = 0
                break

    if language == 'ru':
        count = 0
        botCount = 0
        while True:
            choice = input('Будете брать карту? да/нет\n')

            if choice == 'да':
                current = koloda.pop()
                print('Вам выпала карта номиналом: %d' % current)
                count += current

                if count > 21:
                    print('Извините, вы набрали больше 21 очка, вы проиграли!')
                    print('Ваш счёт: %d очков' % count)
                    break

                elif count == 21:
                    print('Поздравляем, вы набрали 21 очко!')
                    print('Ваш противник автоматически проиграл!')
                    print('Игра окончена')
                    break

                else:
                    print('Твой счёт: %d очков' % count)

            elif choice == 'нет' and count < 21:
                botCount = random.randint(1, 21)
                print('Игра окончена, ваш счёт: %d очков!' % count)
                print('Счёт вашего противника: %d очков' % botCount)
                if count > botCount:
                    print('Ваш противник проиграл вам')
                elif count < botCount:
                    print('Ваш противник выиграл!')
                count = 0
                botCount = 0
                break