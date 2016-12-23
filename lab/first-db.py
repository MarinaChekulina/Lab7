# import MySQLdb
#
# # Открываем соединение
# db = MySQLdb.connect(
#     host='localhost',
#     user='Marina27',
#     passwd='luck27',
#     db='cars_db',
# )
#
# # без utf-8 не работает, что-то с кодировкой не то
# db.set_character_set('utf8')
# # Получаем курсор для работы с БД
# c = db.cursor()
# print("Вставить описание акции:")
# # Выполняем вставку
# c.execute('INSERT INTO lab_Sales(id, name, date, text) VALUES (%s, %s, %s, %s);',
#         (4, 'Новая акция', 'с 15 декабря по 25 декабря', 'С наступающим Новым Годом!'))
#
# # Фиксируем изменения
# db.commit()
#
# # Выполняем выборку
# c.execute("SELECT * FROM lab_Sales;")
#
# #Забираем все полученные записи
# sales = c.fetchall()
#
# #Печатаем их
# for item in sales:
#     print(item)
#
# c.execute('DELETE FROM lab_Sales where id=4;')
# db.commit()
#
# c.execute("SELECT id, name, date, text FROM lab_Sales;")
# print()
# print("Результат после удаления акции с id=4:")
# sales = c.fetchall()
#
# #Печатаем их
# for item in sales:
#     print(item)
#
# c.close() #Закрываем курсор
#
# db.close() #Закрываем соединение