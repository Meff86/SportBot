import telebot


token = "5300200188:AAF8A92QfL77an5yJCUi2caOj8GNqIqVHyQ"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}\nЭтот бот поможет тебе подобрать идеальную тренировку только для тебя".format(
            message.from_user
        ),
    )
    msg = bot.send_message(message.chat.id, "Введите вашу цель(похудение, или масса): ")
    bot.register_next_step_handler(msg, start_2)


def start_2(message):
    lock = str(message.text)
    if (
        lock == "похудение"
        or lock == "Похудение"
        or lock == "Похудеть"
        or lock == "похудеть"
    ):
        age = bot.send_message(message.chat.id, "Введите ваш возраст: ")
        bot.register_next_step_handler(age, start_3)
    elif lock == "масса" or lock == "Масса":
        age = bot.send_message(message.chat.id, "Введите ваш возраст: ")
        bot.register_next_step_handler(age, start_3_1)
    else:
        bot.send_message(
            message.chat.id, "Некорректный ввод, начните заново с команды /start"
        )


def start_3(message):
    age = int(message.text)
    if age >= 60 or age <= 16:
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        weight = bot.send_message(message.chat.id, "Введите ваш вес в кг: ")
        bot.register_next_step_handler(weight, start_4)


def start_3_1(message):
    age = int(message.text)
    if age >= 60 or age <= 16:
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        weight = bot.send_message(message.chat.id, "Введите ваш вес в кг: ")
        bot.register_next_step_handler(weight, start_4_1)


def start_4(message):
    weight = int(message.text)
    if weight >= 90 or weight <= 40:
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        contraindications = bot.send_message(
            message.chat.id,
            "Есть ли у вас противопоказания к занятию фитнесом(Да,Нет): ",
        )
        bot.register_next_step_handler(contraindications, start_5)


def start_4_1(message):
    weight = int(message.text)
    if weight >= 90 or weight <= 40:
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        contraindications = bot.send_message(
            message.chat.id,
            "Есть ли у вас противопоказания к занятию фитнесом(Да,Нет): ",
        )
        bot.register_next_step_handler(contraindications, start_5_1)


def start_5(message):
    contraindications = str(message.text)
    if contraindications == "Да" or contraindications == "да":
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        bot.send_message(
            message.chat.id,
            "https://disk.yandex.ru/d/7qyoil6QDNJTKA\nПриятных тренировок!",
        )
        bot.send_message(
            message.chat.id,
            "А за любыми консультациями и дальнейшими тренировками, а так же питанием обращайтесь к\n"
            "https://taplink.cc/fito_nadya ",
        )


def start_5_1(message):
    contraindications = str(message.text)
    if contraindications == "Да" or contraindications == "да":
        bot.send_message(
            message.chat.id,
            "Перед тренировками необходима консультация у квалифицированного тренера\n"
            "https://taplink.cc/fito_nadya",
        )
    else:
        bot.send_message(
            message.chat.id,
            "https://disk.yandex.ru/d/3-xtAs6UuZ2rGA\nПриятных тренировок!",
        )
        bot.send_message(
            message.chat.id,
            "А за любыми консультациями и дальнейшими тренировками, а так же питанием обращайтесь к\n"
            "https://taplink.cc/fito_nadya ",
        )


bot.polling(none_stop=True)
