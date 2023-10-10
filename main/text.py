main_menu = ['Главное меню',
             'Показать заметки',
             'Найти и открыть заметку для чтения',
             'Добавить заметку',
             'Изменить заметку',
             'Удалить заметку',
             'Выход']

main_menu_input = 'Выберите пункт меню: '

main_menu_input_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu) - 1}: '

empty_folder = 'Папка пуста'

input_search_word = 'Введите название заметки для поиска: '


def empty_search(word: str) -> str:
    return f'Заметки содержащие "{word}" не найдены'


input_open_file = 'Введите номер файла для открытия: '

input_change_file = 'Введите номер файла для изменения: '

input_delete_file = 'Введите номер файла для удаления: '

change_success = 'Текст файла успешно изменён'


def note_deleted(name: str) -> str:
    return f'Заметка {name} успешно удалена'


wrong_type_error = 'Введите номер существующих заметок: '
