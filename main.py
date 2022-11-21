from translate import Translator

translator = Translator(from_lang='English', to_lang='Russian')
print(translator.translate(str(input('Введите данные: '))))

