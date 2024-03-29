# Словарь для вопросов
LEXICON_QUE: dict[str, str] = {'first': "Кто сыграл Нео в 'Матрице'?",
                               'second': "У какого млекопитающего нет голосовых связок?",
                               'third': "Как называется крупнейшая технологическая компания Южной Кореи?",
                               'fourth': "Сколько зубов должно быть во рту взрослого человека?",
                               'fifth': "Какая социальная сеть появилась в 2003 году?",
                               'end': "Отлично, ты прошёл тест, твои ответы: "}
# Словарь для ответов
LEXICON_ANS: dict[str, str] = {"first_question_answer_one": "a) Бред Питт",
                               "first_question_answer_two": "b) Том Круз",
                               "first_question_answer_three": "c) Киану Ривз",
                               "first_question_answer_four": "d) Мэттью Макконахи",
                               "second_question_answer_one": "a) Бегемот",
                               "second_question_answer_two": "b) Жираф",
                               "second_question_answer_three": "c) Пантера",
                               "second_question_answer_four": "d) Крот",
                               "third_question_answer_one": "a) Samsung",
                               "third_question_answer_two": "b) Hyundai",
                               "third_question_answer_three": "c) LG Electronics",
                               "third_question_answer_four": "d) Korea Electric Power Corporation",
                               "fourth_question_answer_one": "a) 35",
                               "fourth_question_answer_two": "b) 32",
                               "fourth_question_answer_three": "c) 30",
                               "fourth_question_answer_four": "d) 42",
                               "fifth_question_answer_one": "a) Myspace",
                               "fifth_question_answer_two": "b) Twitter",
                               "fifth_question_answer_three": "c) Facebook",
                               "fifth_question_answer_four": "d) ВКонтакте",
                               "start": "Начать✅",
                               "cancel": "Отмена❌"
                               }
# Словарь для команд
LEXICON_CMD: dict[str, str] = {
    '/start': "Привет, я бот для проведения учебного тестирования,"
              " ваши ответы я сохраняю в google sheets\n"
              "Для помощи напишу команду /help",
    '/help': "Список команд:\n"
             "/start - начало работы бота\n"
             "/help - вызов списка команд\n"
             "/test - начать тест",
    '/test': "Тест будет состоять из 5 вопросов, время прохождения не ограниченно"}
