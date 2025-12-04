import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email_login = os.getenv("EMAIL_LOGIN")
email_pass = os.getenv("EMAIL_PASS")

email_to = email_login

letter_template = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

ref_link = "https://dvmn.org/profession-ref-program/dhgg7012/rhcHx/"
friend_name = "Дмитрий"
sender_name = "Aron"
letter_template = letter_template.replace("%friend_name%", friend_name)
letter_template = letter_template.replace("%my_name%", sender_name)
letter_template = letter_template.replace("%website%", ref_link)

letter = """From: {email_from}
To: {email_to}
Subject: {letter_subject}
Content-Type: text/plain; charset="UTF-8";

{letter_template}

""".format(email_from=email_login, email_to=email_to, letter_subject="Приглашение!", letter_template=letter_template)

letter = letter.encode("UTF-8")

ya_port = 465
ya_host = 'smtp.yandex.ru'
gmail_port = 465
gmail_host = 'smtp.yandex.ru'
mailru_port = 465
mailru_host = 'smtp.mail.ru'

server = smtplib.SMTP_SSL(ya_host, ya_port)
server.login(email_login, email_pass)
server.sendmail(email_login, email_to, letter)

server.quit()
