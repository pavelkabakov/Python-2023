""""
Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки.
"""


class Note:
    def __init__(self, head):
        self.__note_id = "None"
        self.__date = "00.00.0000"
        self.__body = "telo"
        self.__head = head

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_id(self, note_id):
        self.__note_id = note_id

    def get_id(self):
        return self.__note_id

    def set_head(self, head):
        self.__head = head

    def get_head(self):
        return self.__head


