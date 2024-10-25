def count_letters(text: str) -> dict:
    """
    Функция возвращает словарь котором ключи это буквы нижнего регистра полученные из text,
    а значение это сколько раз эта буква встретилась в text.

    пример:
        text = 'У лукоморья дуб зелёный;'
        result = count_letters(text)
        print(result)  # {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
    """
    text = ''.join(text.lower().split())
    # print(text)
    str_d = {}
    for let in text:
        if str_d.get(let) is None and let.isalpha():
            c = 0
            for letter in text:
                if letter == let:
                                c += 1
            str_d[let] = c

    return str_d

def calculate_frequency(letter_count: dict) -> dict:
    """
    Функция возвращает словарь, где буква используется как ключ, а ее частота как значение.

    пример:
        letter_count = {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
        result = calculate_frequency(letter_count)
        print(result)  # {'у': 0.15, 'л': 0.1, 'к': 0.05, 'о': 0.1, 'м': 0.05, 'р': 0.05, 'ь': 0.05, 'я': 0.05,
        'д': 0.05, 'б': 0.05, 'з': 0.05, 'е': 0.05, 'ё': 0.05, 'н': 0.05, 'ы': 0.05, 'й': 0.05}
    """
      # TODO Реализуйте функцию
    str_dict ={}
    sum_ = sum(letter_count.values())
    # print(sum_)
    for letter in letter_count:
        str_dict[letter] = round((letter_count.get(letter)) / sum_, 2)

    return str_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
# text1 = main_str
# text1 = ''.join(text1.lower().split())
# i = 0
# ch = text1[0].lower()
# for k in text1:
#     if k == ch:
#         i += 1
# print(i)

# print(count_letters(main_str))
# print(calculate_frequency(count_letters(main_str)))
count_dict = count_letters(main_str)
# print(count_dict)
frequency_dict = calculate_frequency(count_dict)
# print(frequency_dict)

# TODO Распечатайте в столбик букву и её частоту в тексте
for key, item in frequency_dict.items():
    print(f"{key}: {item:.2f}")
