def send_email(message, recipient, sender='university.help@gmail.com'):
    def is_correct(email):
        # return '@' in email or any(ext in email for ext in ['.com', '.ru', '.net'])
        return '@' in email and email.endswith(('.com', '.ru', '.net'))

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif not is_correct(recipient) or not is_correct(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо: {message} успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо: {message} отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')