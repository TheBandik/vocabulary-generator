import random


# Гласные
vowels = ['a', 'i', 'e', 'u', 'o']

# Согласные
consonants = ['t', 'd', 'r', 'n', 'm', 'p', 'b', 'f', 'v', 's', 'z', 'k', 'h', 'l', 'j']

# Слоги CV
syllables_cv = [
    'ta', 'ti', 'te', 'tu', 'to',
    'da', 'di', 'de', 'du', 'do',
    'ra', 'ri', 're', 'ru', 'ro',
    'na', 'ni', 'ne', 'nu', 'no',
    'ma', 'mi', 'me', 'mu', 'mo',
    'pa', 'pi', 'pe', 'pu', 'po',
    'ba', 'bi', 'be', 'bu', 'bo',
    'fa', 'fi', 'fe', 'fu', 'fo',
    'va', 'vi', 've', 'vu', 'vo',
    'sa', 'si', 'se', 'su', 'so',
    'za', 'zi', 'ze', 'zu', 'zo',
    'tsa', 'tsi', 'tse', 'tsu', 'tso',
    'dza', 'dzi', 'dze', 'dzu', 'dzo',
    'cha', 'chi', 'che', 'chu', 'cho',
    'ka', 'ki', 'ke', 'ku', 'ko',
    'ha', 'hi', 'he', 'hu', 'ho',
    'la', 'li', 'le', 'lu', 'lo',
    'ja', 'ji', 'je', 'ju', 'jo',
    'sha', 'shi', 'she', 'shu', 'sho',
    'mpa', 'mpi', 'mpe', 'mpu', 'mpo',
    'mba', 'mbi', 'mbe', 'mbu', 'mbo',
]

# Слоги VC
syllables_vc = [
    'at', 'it', 'et', 'ut', 'ot',
    'ad', 'id', 'ed', 'ud', 'od',
    'ar', 'ir', 'er', 'ur', 'or',
    'an', 'in', 'en', 'un', 'on',
    'am', 'im', 'em', 'um', 'om',
    'ap', 'ip', 'ep', 'up', 'op',
    'ab', 'ib', 'eb', 'ub', 'ob',
    'af', 'if', 'ef', 'uf', 'of',
    'av', 'iv', 'ev', 'uv', 'ov',
    'as', 'is', 'es', 'us', 'os',
    'az', 'iz', 'ez', 'uz', 'oz',
    'ats', 'its', 'ets', 'uts', 'ots',
    'adz', 'idz', 'edz', 'udz', 'odz',
    'ach', 'ich', 'ech', 'uch', 'och',
    'ak', 'ik', 'ek', 'uk', 'ok',
    'ah', 'ih', 'eh', 'uh', 'oh',
    'al', 'il', 'el', 'ul', 'ol',
    'aj', 'ij', 'ej', 'uj', 'oj',
    'ash', 'ish', 'esh', 'ush', 'osh',
    'amp', 'imp', 'emp', 'ump', 'omp',
    'amb', 'imb', 'emb', 'umb', 'omb',
]

# Правила
rulles = {
    'nc1': {
        'c': 'u',
        'v': 'um'
    },

    'nc2': {
        'c': 'sa', 
        'v': 's'
    },

    'nc3': {

    }, 

    'nc4': {

    },

    'nc5': {
        'c': 'za',
        'v': 'd'
    },

    'nc6': {},

    'nc7': {
        'c': 'a', 
        'v': 'ar'
    },

    'ad': {}
}

# Получение правила
rule_prefix = input('Правило: ')
rule = rulles[rule_prefix]

# Получение количества слов
count_of_words = int(input('Количество слов: '))


for i in range(count_of_words):
    # Длина слова
    word_length = random.randint(1, 5)

    # Если существительное
    if 'nc' in rule_prefix:
        if rule_prefix != 'nc6':
            word = random.choice((rulles[rule_prefix]['c'], rulles[rule_prefix]['v']))
        else:
            word = random.choice(syllables_cv + syllables_vc)

        for j in range(word_length):
            if word[-1] in vowels:
                word += random.choice(syllables_cv)
            elif word[-1] in consonants:
                word += random.choice(syllables_vc)

        if word[-1] in vowels:
            word = word[:-1]
    

    print(word)
