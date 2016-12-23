# import MySQLdb
#
#
# class Connection:
#     def __init__(self, user, password, db, host="localhost", charset="utf8"):
#         self.user = user
#         self.host = host
#         self.password = password
#         self.db = db
#         self.charset = charset
#         self._connection = None
#
#     @property
#     def connection(self):
#         return self._connection
#
#     def __enter__(self):
#         self.connect()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.disconnect()
#
#     def connect(self):
#         #открытие соединения
#         if not self._connection:
#             self._connection = MySQLdb.connect(
#                 host=self.host,
#                 user=self.user,
#                 passwd=self.password,
#                 db=self.db,
#                 charset=self.charset
#             )
#
#     def disconnect(self):
#         #закрытие соединения
#         if self._connection:
#             self._connection.close()
#
#
# class SalesClass:
#     def __init__(self, db_connection, id, name, date, text):
#         self.db_connection = db_connection.connection
#         self.id = id
#         self.name = name
#         self.date = date
#         self.text = text
#
#
#     def save(self):
#         c = self.db_connection.cursor()
#         c.execute("INSERT INTO lab_Sales(id, name, date, text) VALUES (%s, %s, %s, %s);", (self.id, self.name, self.date, self.text))
#         self.db_connection.commit()
#         c.close()
#
#     def print_all(self):
#         c = self.db_connection.cursor()
#         c.execute('SELECT id, name, date, text FROM lab_Sales;')
#         items = c.fetchall()
#         for item in items:
#             print(item)
#         c.close()
#         return items
#
#     def del_str(self):
#         c = self.db_connection.cursor()
#         c.execute("DELETE FROM lab_Sales where id=5;")
#         self.db_connection.commit()
#         c.close()
#
#
# con = Connection('Marina27', 'luck27', 'cars_db')
#
# with con:
#     new_sale = SalesClass(con, 5, 'Вторая новая акция', 'с 17 декабря по 25 декабря', 'С наступающим Новым Годом 2017!')
#     new_sale.save()
#     print("Добавили предложение:")
#     list(new_sale.print_all())
#     print()
#     print("После удаления добавленного предложения:")
#     new_sale.del_str()
#     list(new_sale.print_all())
