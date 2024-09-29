def send_email ( message , recipient , sender = "university.help@gmail.com"):
    if (email_false ( sender ) or email_false ( recipient )) :
        print ('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if sender == recipient :
        print ("Нельзя отправить письмо самому себе")
        return
    if sender == "university.help@gmail.com" :
        print ("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        return

def email_false(email):
    result = True
    if "@" in email and ((len(email) - email.find(".com") -4) == 0 or (len(email) - email.find(".net") -4) == 0 or (len(email) - email.find(".ru") -3) == 0):
        result = False
    return result

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')