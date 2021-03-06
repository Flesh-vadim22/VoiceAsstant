import json
import random
import app.Models.ComputerModel
import app.Models.BrowserModel


class DataModel():
    # основная функция получения ответа и действия пользователя
    def __init__(self):
        # super().__init__(parent)
        self.computer = app.Models.ComputerModel.ComputerModel()
        self.browser = app.Models.BrowserModel.BrowserModel()

    def get_answer(self, text):
        filname = r'app/Controllers/data/commands.json'
        with open(filname, 'r', encoding='utf-8') as f:
            data = json.load(f)
        key_text = self.get_key_request(text, data)
        # print(key_text)#ключевые слова, запаисанные в commands2.json
        if key_text != None:
            value_text = self.get_request(text, data)  # значения от пользователя
            class_command = self.classify_text(self.clear_phrase(key_text), data)  # класс ключевого слова
            if class_command:
                answer = self.get_answer_by_intent(class_command, data)
                action = self.performing_action(class_command, key_text, value_text)
                return (answer, action)
        stub = self.get_failure_phrase(data)
        return (stub, False)

    # получение ключевого слова от пользователя
    def get_key_request(self, text, data):
        text = text.split()
        for key, value in data['intents'].items():
            for example in value['examples']:
                if text[0] == example: return text[0]

        # получение вторичного значения из фразы пользователя
    def get_request(self, text, data):
        arr_text = text.split(maxsplit=1)
        if len(arr_text) == 1:
            val = str(arr_text[0])
        else:
            val = str(arr_text[1])
        for key, value in data['intents'].items():
            for example in value['examples']:
                val = val.replace(example, '')
        val = val.strip()
        return val

    # классификация текста и получения от него ключа
    def classify_text(self, text, data):
        for key, value in data['intents'].items():
            for example in value['examples']:
                example = self.clear_phrase(example)
                # distance = nltk.edit_distance(text, example)
                # if example and distance / len(example) < 0.4:
                #     return key
                example = self.clear_phrase(example)
                if example == text:
                    return key

    # очистка фразы от ненужных символов
    def clear_phrase(self, phrase):
        phrase = phrase.lower()
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
        result = ''.join(symbol for symbol in phrase if symbol in alphabet)
        return result


    # выбор рандомного значения, зависящее от ключа пользователя
    def get_answer_by_intent(self, intent, data):
        if intent in data['intents']:
            responses = data['intents'][intent]['responses']
            return random.choice(responses)

    # получение фразы-заглушки, если команды не существует
    def get_failure_phrase(self, data):
        failure_phrases = data['failure_phrases']
        return (random.choice(failure_phrases))

    # Основная функция для выполнения определенных команд
    def performing_action(self, key_action='', key_text='', value_text=''):
        main_text = value_text.replace(' ', '')
        if key_action == "bye":
            return True
        elif key_action == "open_programm":
            if ('калькулятор' in main_text) or ('calculator' in main_text):
                self.computer.openApp('calc')
            elif ('блокнот' in main_text) or ('notepad' in main_text):
                self.computer.openApp('notepad')
            elif ('паинт' in main_text) or ('пэинт' in main_text) or ('paint' in main_text):
                self.computer.openApp('mspaint')
            elif ('блокнот' in main_text) or ('notepad' in main_text):
                self.computer.openApp('notepad')
            elif ('браузер' in main_text) or ('browser' in main_text):
                self.browser.openUrl('https://yandex.ru/')
            elif ('ютуб' in main_text) or ('youtube' in main_text):
                self.browser.openUrl('https://www.youtube.com/')
            elif ('вконтакте' in main_text) or ('vkontakte' in main_text):
                self.browser.openUrl('https://vk.com/')
            elif ('почту' in main_text) or ('почтовую' in main_text):
                self.browser.openUrl('https://e.mail.ru/inbox/?')
            elif ('твиттер' in value_text) or ('twitter' in main_text):
                self.browser.openUrl('https://twitter.com/')
            elif ('фейсбук' in main_text) or ('facebook' in main_text):
                self.browser.openUrl('https://www.facebook.com/')
        elif key_action == "action_browser":
            if ('открой' in key_text) or ('поиск' in key_text) or ('найти' in key_text) or ('найди' in key_text):
                rezult = self.browser.filter_internet(self.browser.search_in_google(main_text))
                if self.browser.definition_of_plural(value_text) == False:
                    self.browser.openUrl(rezult[0])
                else:
                    self.browser.openUrl(random.choice(rezult))
        elif key_action == "humor":
            return self.browser.tell_anecdote()
        elif key_action == "weather":
            return self.browser.weather()
        elif key_action == "music":
            url = 'https://my.mail.ru/music/search/' + str(value_text)
            self.browser.openUrl(url)
        elif key_action == 'movie':
            rezult = self.browser.filter_internet(self.browser.search_in_google('смотреть онлайн ' +  main_text))
            self.browser.openUrl(random.choice(rezult))
        elif key_action == 'shutdown':
            self.computer.Computeroff()
