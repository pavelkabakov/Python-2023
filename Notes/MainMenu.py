# import Note
# import FileWriter
import csv
from datetime import date





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


class FileWriter:
    __filename = "Notes.csv"

    def file_write(note: Note, filename: str):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            row = str(note.get_id()) + str(note.get_date()) + str(note.get_head()) + str(note.get_body())
            writer.writerow(row)

    def file_read(date: [], filename: str):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], "-", row[1], "-", row[2], "-", row[3])


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить все заметки\n"
          "2. Создать новую заметку\n"
          "3. Редактировать заметку\n"
          "4. Удалить заметку\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def work_with_notes():
    choice = show_menu()
    # phone_book = read_csv('phonebook.csv')

    while choice != 5:
        if choice == 1:  # 1. Отобразить все заметки
            print("1")
        elif choice == 2:  # 2. Создать новую заметку
            print("2")
            create_note()
        elif choice == 3:  # 3. Редактировать заметку
            print("3")
        elif choice == 4:  # 4. Удалить заметку
            print("4")

        choice = show_menu()


def create_note() -> Note:
    note = Note("1")
    filename = "notes.csv"
    filewrite = FileWriter
    today = date.today()
    print("Введите имя заметки:\n")
    choice = str(input())
    note.set_head(choice)
    print("Введите текст заметки:\n")
    choice = str(input())
    note.set_body(choice)
    note.set_id(1)
    note.set_date(today)
    filewrite.file_write(note, filename)
    return note


work_with_notes()