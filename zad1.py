from zad1_klasy import Note, Notebook


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def showMenu(self):
        print("""
        1. Pokaz notatki
        2. Szukaj notatki
        3. Dodaj notatke
        4. Modyfikuj notatke
        5. Wyjdz
        """)

    def run(self):
        while True:
            self.showMenu()
            choice = input("Wybierz opcje: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Nie ma takiej opcji")

    def show_notes(self, notes=None):
        if notes is None:
            notes = self.notebook.notes

            print("="*20)
        if not len(notes) > 1:
            print("Nie znaleziono notatek")
            print("="*20)

        for note in notes:
            print(f"[Id {note.id}] Tagi : {note.tag} \nTreść :\n{note.text}")
            print("="*20)
            print("="*20)

    def search_notes(self):
        found = self.notebook.search(input("Podaj tekst: "))
        self.show_notes(found)

    def add_note(self):
        text = input("Podaj tekst: ")
        tag = input("Podaj tag: ")
        self.notebook.new_note(Note(text, tag))

    def modify_note(self):
        note_id = input("Podaj id notatki do edycji ")
        self.notebook.modify_note(note_id)

    def quit(self):
        exit()


def main():
    menu = Menu()
    menu.run()


if __name__ == '__main__':
    main()
