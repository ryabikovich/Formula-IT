
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



# TODO  Напишите функцию count_letters
# def count_letters(text):
#     text = list(text.lower())
#     alphabet = [chr(i) for i in range(1072, 1104)]
#     alphabet.insert(6, chr(ord("ё"))) # почему то через range 1105 выдает  символ ѐ
#     letters = dict.fromkeys(alphabet, 0)
#     for i in text:
#         if i.isalpha():
#             letters[i] = letters[i] + 1
#     return (letters)

def count_letters(text):
    text = list(text.lower())
    letters = {}
    for i in text:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return (letters)



def calculate_frequency(letters):
    all_letters = sum(letters.values())
    for i in letters:
        letters[i] = letters[i]/all_letters
    return ((letters))


# TODO Распечатайте в столбик букву и её частоту в тексте

# print(count_letters(main_str))
freq = calculate_frequency(count_letters(main_str))
for i in freq:
    print(f"{i}: {(freq[i]):.2f}")
