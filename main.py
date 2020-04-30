
# СЛОВАРИ

# задание вручную (через литералы) (можно задавать как угодно)
# на примере курсов Нетологии https://netology.ru/development/programs/all
courses_dict = {"python":["Артём Черняков", "Елена Никитина", "Ринат Хабибиев", "Евгений Шмаргунов", "Олег Булыгин"], "frontend":["Татьяна Тен", "Александр Фитискин", "Алёна Батицкая"]}

# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
# разные способы задания словаря - потренироваться дома
# еще один хороший мануал https://www.ibm.com/developerworks/ru/library/l-python_part_4/index.html

#  добавить cpp, удалить cpp, получить keys, values, items
courses_dict["cpp"] = [""]
del courses_dict["cpp"]
print(courses_dict.keys())
print(courses_dict.values())
print(courses_dict.items())
# ...
# ошибка с получением несуществующего ключа - упадет
print(courses_dict["web"])
# безопасный способ проверки ключа
print(courses_dict.get("frontend"))
# setdefault - создает значение по умолчанию, если такого ключа в словаре еще нет, либо ничего не делает, если ключ уже есть
courses_dict.setdefault("frontend", [""])
print(courses_dict.get("frontend"))

# ===============
# МНОЖЕСТВА

# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html хорошее описание множеств и их функционала

# на примере курсов Нетологии https://netology.ru/development/programs/all
python_set = set(["Артём Черняков", "Елена Никитина", "Ринат Хабибиев", "Евгений Шмаргунов", "Олег Булыгин"])
bigdata_set = set(["Олег Булыгин", "Специальный тестовый"])

intersection = python_set & bigdata_set
intersection = python_set.intersection(bigdata_set)

union = python_set | bigdata_set

difference = python_set.difference(bigdata_set)
print("Разность:\n", difference)
symmetricdifference = python_set.symmetric_difference(bigdata_set)
print("Симметричная разность:\n", symmetricdifference)

python_set.discard("Олег Булыгин")
intersection = python_set & bigdata_set
print("Пересечение после удаления:\n", intersection)
