import text


def show_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print('\t' + f'{i}. {item}')
        else:
            print(item)
    select_option = input(text.main_menu_input)
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.main_menu):
            return int(select_option)
        select_option = input(text.main_menu_input_error)


def show_notes(notes: dict[int, str], msg: str):
    if notes:
        print("==================")
        for i, note_name in notes.items():
            print(f'{i}. {notes.get(i)}')
        print("==================")
    else:
        print_msg(msg)


def input_data(msg: str) -> str:
    return input(msg)


def input_number(msg: str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)


def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')
