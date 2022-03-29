import datetime


class Note:
    id = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = datetime.datetime.now()
        __class__.id += 1
        self.id = __class__.id

    def match(self, str) -> bool:
        return self.tag.find(str) != -1 or self.text.find(str) != -1


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, notatnik):
        self.notes.append(notatnik)

    def modify_note(self, id):
        if id is None or id > len(self.notes):
            raise ValueError("Nie ma takiej notatki")
        for note in self.notes:
            if note.id == id:
                note.text = input("Podaj nowy tekst: ")

    def search(self, str):
        found = []
        for note in self.notes:
            if note.match(str):
                found.append(note)

        return found
