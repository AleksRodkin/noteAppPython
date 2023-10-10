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


def input_number(msg: int, result: dict[int, str]) -> int:
    check_list = list(result.keys())
    while True:
        number = int(input(msg))
        if 0 < number <= len(check_list):
            return int(number)


def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')
