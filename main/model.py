import os
import json

path = '/Users/aleksr/PycharmProjects/notesApp/main/notes/'


def show_notes():
    with os.scandir(path) as files:
        for file in files:
            print(file.name)


def open_note():
    with open('test_json_file.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    print(templates)

    for section, commands in templates.items():
        print(section)
        print('\n'.join(commands))


def add_note():
    one_two = [
        'раз', 'два'
    ]

    two_three = [
        'три', 'четыре'
    ]

    to_json = {'Раз-Два': one_two, 'Три-Четыре': two_three}

    with open('test_json_file.json', 'w') as f:
        f.write(json.dumps(to_json, ensure_ascii=False, indent=4))
        f.close()

    # with open('test_json_file') as f:
    #     print(f.read())


def change_note():
    with open('test_json_file.json') as f:
        data = json.load(f)
    data['Раз-Два'] = ['замена1', 'замена2']
    with open('test_json_file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
