class PersonRepository:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def get(self, id):
        for person in self.persons:
            if person.id == id:
                return person
        return None

    def get_all(self):
        return self.persons

    def update(self, old_person, new_person):
        self.delete(old_person.id)
        self.add(new_person)
        raise Exception("Person not found")

    def delete(self, id):
        for p in self.persons:
            if p.id == id:
                self.persons.remove(p)
                return
        raise Exception("Person not found")
