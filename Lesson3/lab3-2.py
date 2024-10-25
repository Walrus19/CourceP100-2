# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, razd =','):
    words1 = str1.split(sep=razd)
    words2 = str2.split(sep=razd)
    words3 = []
    for word1 in words1:
        for word2 in words2:
            if word1 == word2:
                words3.append(word1)
    words3.sort()
    return words3
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,'|'))