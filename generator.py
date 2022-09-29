import random


# Слоги
syllables = ['ma', 'pa', 'ka', 'te', 'so']


rulles = {
    'nc1': [1, 'ka']
}

# Получение правила
rule_prefix = input('Правило: ')
rule = rulles[rule_prefix]

# Получение количества слов
count_of_words = int(input('Количество слов: '))


for i in range(count_of_words):
    # Длина слова
    word_length = random.randint(1, 5)
    word = rule[1]
    for j in range(word_length - rule[0]):
        word += random.choice(syllables)
    print(word)
