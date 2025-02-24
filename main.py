import telebot
from dotenv import load_dotenv
import os
import datetime
load_dotenv()


bot = telebot.TeleBot(token=os.getenv("TOKEN"), parse_mode=None)

@bot.message_handler(["start"])
def send_messege(message):
    bot.reply_to(message, """Ат2 бот, это бот посвящённой комьюнити Рисуем мультфильмы 2, или иначе, At2. Этот бот, предназначен рассказать больше а известных креаторах в нашем комьюнити и их особенностях!
Что бы вывести список Аниматоров о которых вы хотите узнать введите << /creator_list >>
Так же, если вы напишите боту "Запиши мой айди", то, возможно, автор заметит вас и сделает для вас особенное сообщение. 

Уникальное сообщение, доступно только, в раз, один день.""")


@bot.message_handler(["creator_list"])
def send_list(message):
    bot.reply_to(message, """
SN_Nervel |
----------------- 
Tortell |
----------- 
Ranimek |
---------------
Nekto777 |
---------------- 
Infario_Cabu |
-------------------- 
Mr.Vladislav |
------------------------
""")

animators = [
    {
        "name": "Sn_Nervel",
        "keywords": ["nervel", "sn", "сн", "нервел"],
        "description": """SN Nervel — Самый уникальный аниматор среди топов. Все спрайты он делает сам: эффекты, персонажи, ракурсы — всё с нуля. Его работа над освещением, камерой и эффектами действительно впечатляет. SN Nervel всегда стремится выделяться и не боится экспериментировать с новыми техниками. Он работает на высокой скорости анимации, а его сцены могут содержать сотни или даже тысячи кадров, что требует огромного терпения и внимания к деталям. Каждая его работа — это шаг вперёд, и он постоянно ищет новые способы улучшить свои навыки.



    Chanell link: https://www.youtube.com/@Sn_Nervel"""
    },
    {
        "name": "Tortell",
        "keywords": ["tortell", "tort", "тортелл", "торт"],
        "description": """Tortell — Крутой аниматор, который отлично чувствует баланс между плавностью и динамикой. Его RHG-битвы насыщены сюжетом и эпичными сценами, а каждая новая работа — это проработка деталей и улучшение техники. Он умело сочетает стиль и техническую сложность, создавая действительно зрелищные анимации. Видно, что он вкладывает душу в каждую сцену, делая их запоминающимися.



    Chanell link: https://www.youtube.com/@Tortell3211"""
    },
    {
        "name": "Ranimek",
        "keywords": ["rani", "рани"],
        "description": """Ranimek — Хотя он не считает себя самым крутым аниматором, его стремление к самосовершенствованию заслуживает уважения. Он тщательно анализирует ошибки, прорабатывает детали и с каждой новой анимацией становится лучше. Даже если что-то не выходит идеально, он не сдаётся и продолжает двигаться вперёд. Именно это упорство делает его уникальным. Можно сказать, что у него есть потенциал, который с каждым проектом раскрывается всё больше.



    Chanell link: https://www.youtube.com/@ran1m3k"""
    },
    {
        "name": "Nekto777",
        "keywords": ["nekto", "некто"],
        "description": """Nekto777 — Аниматор, который принимал участие во множестве турниров и коллабов RHG-комьюнити. С каждой новой анимацией он старается исправить прошлые ошибки и прокачать свои навыки. Видно, что он постоянно учится и ищет новые приёмы, чтобы сделать свои работы ещё лучше. У него хорошо получается совмещать динамику и проработку сцен, а в его проектах всегда есть чёткий стиль и идея.



    Chanell link: https://www.youtube.com/@nkt_777"""
    },
    {
        "name": "Infario_Cabu",
        "keywords": ["infar", "инфар"],
        "description": """Infario Cabu — Аниматор с уникальной стилистикой движений. Его «зажим» и нестандартный подход к анимации выделяют его среди других. Он не боится экспериментировать, пробуя разные техники, даже если это что-то новое и рискованное. Его подход к анимации делает его работы узнаваемыми, и каждая новая работа — это ещё один шаг вперёд. Благодаря экспериментам и поиску новых решений он развивается и постоянно удивляет зрителей.



    Chanell link: https://www.youtube.com/@infariocabu2801"""
    },
    {
        "name": "Mr.Vladislav",
        "keywords": ["vlad", "влад"],
        "description": """Mr. Vladislav — Аниматор, известный своими масштабными проектами и вниманием к деталям. Он создаёт плавные и детализированные анимации, которые впечатляют зрителей. Его проекты, такие как «Оружейный беспредел», «Читеры» и «Киборг Владислав против Киборг Боди». Владислав часто сам создаёт спрайты и фоны, тщательно прорабатывает ракурсы. Хотя он не слишком активен, каждая его работа стоит ожидания. Он аниматор, который не просто делает анимации, а создаёт полноценные истории, вложенные в визуал.



    Chanell link: https://www.youtube.com/@Mr-bd7do"""
    }
]

# Особенные пользователи (ID -> персональные сообщения)
special_users = {
    5465611423: "Привет, Создатель! Рад тебя видеть!",
    1989427956: "О, это же ты, хороший 3д артист! Привет кикер.",
    771529762: "Неверятно, это же визео! Здраствуй!",
    7000190934: "Привет blood moon!"
}

# Словарь для хранения последнего времени ответа VIP-пользователям
special_users_last_used = {}

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    chat_type = message.chat.type  # Личный чат или группа?
    text = message.text.lower()
    today = datetime.date.today()

    if chat_type == "private":

    # --- ЛОГИКА ДЛЯ ОСОБЕННЫХ ПОЛЬЗОВАТЕЛЕЙ ---
        if user_id in special_users:
            last_used = special_users_last_used.get(user_id)

            if last_used is None or last_used < today:
                # Если бот еще не отвечал сегодня, обновляем дату и отправляем сообщение
                special_users_last_used[user_id] = today
                bot.reply_to(message, special_users[user_id])
                return

    # Если пользователь хочет записать свой ID
        if "запиши мой айди" in text:
            print(f"User ID: {message.from_user.id} | Username: @{message.from_user.username}")
            bot.reply_to(message, "Я записал твой ID!")
            return

    # Проверяем ключевые слова для аниматоров
        for animator in animators:
            if any(keyword in text for keyword in animator["keywords"]):
                bot.reply_to(message, animator["description"])
                return


        # Если сообщение не попало ни под одно условие
        bot.reply_to(message, "Я не понял, попробуй сформулировать иначе.")

    elif chat_type == "supergroup" or chat_type == "group":
        if bot.get_me().username in message.text:
            print(f"Упоминание бота в сообщении: {message.text}")

        # --- ЛОГИКА ДЛЯ ОСОБЕННЫХ ПОЛЬЗОВАТЕЛЕЙ ---
        if user_id in special_users:
            last_used = special_users_last_used.get(user_id)

            if last_used is None or last_used < today:
                # Если бот еще не отвечал сегодня, обновляем дату и отправляем сообщение
                special_users_last_used[user_id] = today
                bot.reply_to(message, special_users[user_id])
                return

        # Если пользователь хочет записать свой ID
        if "запиши мой айди" in text:
            print(f"User ID: {message.from_user.id} | Username: @{message.from_user.username}")
            bot.reply_to(message, "Я записал твой ID!")
            return

        # Проверяем ключевые слова для аниматоров
        for animator in animators:
            if any(keyword in text for keyword in animator["keywords"]):
                bot.reply_to(message, animator["description"])
                return


bot.infinity_polling()