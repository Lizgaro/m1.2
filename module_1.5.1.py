# module_1_5.py

# 2. Создаём переменную immutable_var (неизменяемый кортеж)
immutable_var = (1, 2, 'a', 'b')

# 3. Выводим кортеж на экран
print("Immutable tuple:", immutable_var)

# 4. Попытка изменить элемент кортежа
try:
    immutable_var[0] = 87  # Попытка изменить первый элемент кортежа
except TypeError as e:
    print(f"Ошибка: {e} - Кортежи неизменяемы, и их элементы нельзя изменять.")

# 5. Создаём изменяемую структуру данных - список
mutable_list = [1, 2, 'a', 'b']

# 6. Изменяем элементы списка
mutable_list[0] = 87  # Изменение первого элемента
mutable_list.append('lion')  # Добавляем новый элемент в конец списка

# 7. Выводим изменённый список
print("Mutable list:", mutable_list)
# module_1_5.py
