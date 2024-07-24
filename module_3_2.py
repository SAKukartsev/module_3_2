def send_email(massage, recipient, *, sender='university.help@gmail.com'):

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    if ((recipient.find('@') == recipient.rfind('@') and
         sender.find('@') == sender.rfind('@')) and
            recipient.find('@') > 0 and
            sender.find('@') > 0):
        find = True

    else:
        find = False

    list1 = ('.com', '.ru', '.net')

    for i in list1:
        find_and = recipient.endswith(str(i))

        if find_and:

            for i in list1:
                find_and = sender.endswith(str(i))

                if find_and and find:

                    if find_and and find and sender != 'university.help@gmail.com':
                        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

                    else: print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                    break

                else:
                    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                    break

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')