import Note


def create_note(number):
    title = check_len_text_input(input("Укажите заголовок заметки: "), number)
    body = check_len_text_input(input("Введите содержание заметки: "), number)
    return Note.Note(title=title, body=body)


def menu():
    print(
        "\nПеред вами приложение 'Заметки'. Выберите операцию:\n\n1 - вывести все заметки\n2 - добавить новую заметку\n3 - удалить заметку\n4 - редактировать заметку\n5 - выборать заметки по дате\n6 - выбрать заметку по id\n7 - выход\n\nВведите номер операции: "
    )


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f"Текст должен содержать больше {n} символов\n")
        text = input("Введите текст: ")
    else:
        return text


def goodbuy():
    print("Спасибо, что воспользовались нашим сервисом!")
