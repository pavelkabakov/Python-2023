def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить все заметки\n"
          "2. Найти заметку по заголовку\n"
          "3. Найти заметку по идентификатору\n"
          "4. Добавить заметку в справочник\n"
          "5. Удалить заметку из справочника\n"
          "6. Сохранить заметки в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def work_with_notebook():
    choice = show_menu()
    note_book = read_csv('notebook.csv')

    while choice != 7:
        if choice == 1:  # 1. Отобразить весь справочник
            print_result(note_book)
        elif choice == 2:  # 2. Найти заметку по фамилии
            name = get_search_header()
            print_result(find_by_header(note_book, name))
        elif choice == 3:  # 3. Найти заметку по номеру телефона
            id_note = get_search_number()
            print_result(find_by_id(note_book, id_note))
        elif choice == 4:  # 4. Добавить заметку в справочник
            user_data = get_new_user()
            add_user(note_book, user_data)
            write_csv('notebook.csv', note_book)
        elif choice == 5:  # 5. Удалить заметку из справочника
            name = get_search_header()
            print_result(find_by_header(note_book, name))
            delete_user(note_book, find_by_header(note_book, name))
            write_csv('notebook.csv', note_book)
        elif choice == 6:  # Сохранить заметки в текстовом формате
            file_name = get_file_name()
            write_txt(file_name, note_book)
        choice = show_menu()


def read_csv(filename: str) -> list:
    data = []
    fields = ["Заголовок", "Содержание", "Идентификатор", "Дата"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def write_txt(filename: str, data: list):
    txt_filename = filename + '.txt'
    print(txt_filename)
    with open(txt_filename, 'w', encoding='utf-8') as fout:
        s = '│'
        fout.write('┌' + '─' * 10 + '┬' + '─' * 40 + '┬' + '─' * 10 + '┬' + '─' * 10 + '┐' + '\n')
        fields = ["Заголовок", "Содержание", "Идентификатор", "Дата"]
        for v in fields:
            s += v.center(20) + "│"
        fout.write(f'{s}\n')
        fout.write('├' + '─' * 10 + '┼' + '─' * 40 + '┼' + '─' * 10 + '┼' + '─' * 10 + '┤' + '\n')

        for i in range(len(data)):
            s = '│'
            for v in data[i].values():
                s += v.center(20) + "│"
            fout.write(f'{s}\n')
            fout.write('├' + '─' * 10 + '┼' + '─' * 40 + '┼' + '─' * 10 + '┼' + '─' * 10 + '┤' + '\n')
        fout.write(f'Всего сохранено {len(data)} записей')


def print_result(data: list):
    s = "│"
    print('┌' + '─' * 10 + '┬' + '─' * 40 + '┬' + '─' * 10 + '┬' + '─' * 10 + '┐')
    fields = ["Заголовок", "Содержание", "Ид.", "Дата"]
    tabs = [10, 40, 10, 10]

    # for v in fields:
    s += fields[0].center(10) + "│" + fields[1].center(40) + "│" + fields[2].center(10) + "│" + fields[3].center(
        10) + "│"
    print(f'{s}')
    print('├' + '─' * 10 + '┼' + '─' * 40 + '┼' + '─' * 10 + '┼' + '─' * 10 + '┤')

    for i in range(len(data)):
        s = '│'
        t1 = 0
        for v in data[i].values():
            s += v.center(tabs[t1]) + "│"
            t1 += 1
        print(f'{s}')
        print('├' + '─' * 10 + '┼' + '─' * 40 + '┼' + '─' * 10 + '┼' + '─' * 10 + '┤')
    print(f'Всего найдено {len(data)} записей')


def find_by_header(data: list, first_name):
    search_by_name = []
    for line in data:
        index = line['Заголовок'].lower()
        if index.find(first_name.lower()) == 0:
            search_by_name.append(dict(line))
    return search_by_name


def find_by_id(data: list, number):
    search_by_number = []
    for line in data:
        index = line['Идентификатор']
        if index.find(number) == 0:
            search_by_number.append(dict(line))
    return search_by_number


def get_new_user():
    line = {}
    fields = ["Заголовок", "Содержание", "Идентификатор", "Дата"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line


def delete_user(data: list, name):
    # print(f'name:{name}')
    tmp = []
    for record in name:
        if record in data:
            print('Найдена запись для удаления:')
            tmp.append(record)
            print_result(tmp)
            confirmation = input('Для подтверждения удаления записи введите ""yes"",\n'
                                 'для отмены операции удаления введите ""no"":')
            if confirmation == 'yes':
                data.remove(record)
            elif confirmation == 'no':
                return
            tmp.clear()


def add_user(data: list, user_data: dict):
    data.append(dict(user_data))
    return data


def get_search_header():
    first_name = input("Введите заголовок: ")
    return first_name


def get_search_number():
    name = input("Введите идентификатор: ")
    return name


def get_file_name():
    name = input("Введите имя файла: ")
    return name


# import os
# path = os.getcwd()
# print(path + '\sem_8')
# os.chdir(path+ '\sem_8') # устанавливаем рабочую директорию
# print(os.getcwd()) # вывести рабочую директорию

work_with_notebook()
