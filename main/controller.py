import view
import model
import text


def search_note():
    word = view.input_data(text.input_search_word)
    notes_dict = model.get_notes_dict()
    result = model.search(word, notes_dict)
    view.show_notes(result, text.empty_search(word))
    return result


def start():
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                show_dict = model.get_notes_dict()
                view.show_notes(show_dict, text.empty_folder)
            case 2:
                if search_note():
                    note_id = view.input_number(text.input_open_file)
                    model.open_note(note_id, model.get_notes_dict())
            case 3:
                model.add_note()
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
