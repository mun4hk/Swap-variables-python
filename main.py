#Ввод данных
something_1 = input("Введите что-нибудь: ")
something_2 = input("Введите ещё что-нибудь: ")

#Проверка ввода
print(f"Вы ввели это: '{something_1}' и это: '{something_2}'\n")


#Сохранение в новых переменных
safe_something_1 = something_1
safe_something_2 = something_2

#Проверка сохранения данных
print(f"В переменной <safe_something_1> сохранено это: '{safe_something_1}'")
print(f"В переменной <safe_something_2> сохранено это: '{safe_something_2}'\n")


#Обмен значениями
something_1 = safe_something_2
something_2 = safe_something_1

#Проверка обмена значениями
print(f"Переменная <something_1> содержит: '{something_1}'")
print(f"Переменная <something_2> содержит: '{something_2}'\n")

