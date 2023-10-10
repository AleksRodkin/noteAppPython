import view
import model

def start():
  model.show_notes()
  while True:
    user_select = view.show_menu()
    match user_select:
      case 1:
        model.show_notes()
      case 2:
        model.open_note()
      case 3:
        model.add_note()