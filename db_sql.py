import sqlite3


class Database:
    """
    Класс с функциями для взаимодействия с базой данных
    """
    def __init__(self):
        """
        Создание базы данных
        """
        self.con = sqlite3.connect('DBFT.db')
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tbl(
            id INTEGER PRIMARY KEY,
            name TEXT,
            value TEXT);
        """)

    def save_db(self, data):
        """
        Функция сохранения данных в базу данных
        :param data: данные из структуры
        :return: None
        """
        self.cur.execute("INSERT INTO tbl(name,value) VALUES(?,?);", data)
        self.con.commit()

    def delete_db(self, name):
        """
        Функция удаления сохранения из базы данных
        :param name: название сохранения
        :return: None
        """
        self.cur.execute(f"DELETE FROM tbl WHERE name = '{name}';")
        self.con.commit()

    def load_db(self, name):
        """
        Функция загрузки данных из базы данных
        :param name: название сохранения
        :return: results
        """
        self.cur.execute(f"SELECT value FROM tbl WHERE name = '{name}';")
        results = self.cur.fetchall()
        if results:
            return results[0]
