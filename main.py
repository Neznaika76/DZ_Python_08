# from translate import Translator
#
# translator = Translator(from_lang='English', to_lang='Russian')
# print(translator.translate(str(input('Введите данные: '))))
#
# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в
# которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна
# Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?
s = []
print('Введите данные в формате «Имя Фамилия» или 0 для выхода из режима ввода данных ')
while True:
    fio = []
    info = str(input())
    print(info[0])
    if info == '0':
        break
    else:
        fio.append(info)
        fio.append(info[0])
    s.append(fio)
print('Введенные данные')
fio = []
fio = list(map(tuple, s))
dicts = {}
for elem in fio:
    try:
        dicts[elem[1]].append(elem[0])
    except KeyError:
        dicts[elem[1]] = [elem[0],]
print(dicts)
