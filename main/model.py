import os
import json

path = '/Users/aleksr/PycharmProjects/notesApp/main/notes/'


def open_note(note_id: int, notes: dict[int, str]):
    with open('notes/' + dict.get(notes, note_id), 'r') as fh:
        file_content = fh.read()
        print('\n' + json.loads(file_content))


def add_note():
    name = input('Введите название заметки: ')
    text = input('Введите текст заметки: ')

    with open('notes/' + name + '.json', 'w') as f:
        f.write(json.dumps(text, ensure_ascii=False, indent=4))

    # with open('test_json_file') as f:
    #     print(f.read())


def get_notes_dict():
    note_list = os.listdir(path)
    keys = []
    for i in range(len(note_list)):
        keys.append(i + 1)

    new_dict = {k: v for k, v in zip(keys, note_list)}

    return new_dict


def search(word, notes: dict[int, str]):
    result = {}
    for i, text in notes.items():
        splitted = text.split()
        for field in splitted:
            if word.lower() in field.lower():
                result[i] = text
                break
    return result


def change_note():
    with open('notes/test_json_file.json') as f:
        data = json.load(f)
    data = 'замена1'
    with open('notes/test_json_file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
