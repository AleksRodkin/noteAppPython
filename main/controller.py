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
                if model.get_notes_dict() == {}:
                    view.print_msg(text.empty_folder)
                else:
                    search_dict = search_note()
                    if search_dict:
                        note_id = view.input_number(text.input_open_file, search_dict)
                        model.open_note(note_id, model.get_notes_dict())
            case 3:
                model.add_note()
            case 4:
                if model.get_notes_dict() == {}:
                    view.print_msg(text.empty_folder)
                else:
                    search_dict = search_note()
                    if search_dict:
                        note_id = view.input_number(text.input_change_file, search_dict)
                        model.change_note(note_id, model.get_notes_dict())
                        view.print_msg(text.change_success)
            case 5:
                if model.get_notes_dict() == {}:
                    view.print_msg(text.empty_folder)
                else:
                    search_dict = search_note()
                    if search_dict:
                        note_id = view.input_number(text.input_delete_file, search_dict)
                        name = model.delete_note(note_id)
                        view.print_msg(text.note_deleted(name))
            case 6:
                break
