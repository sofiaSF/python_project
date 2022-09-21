class PersonService:
    def __init__(self, repository):
        self.repository = repository

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def add(self, person):
        self.repository.add(person)

    def update(self, old_person, new_person):
        self.repository.update(old_person, new_person)

    def delete(self, id):
        self.repository.delete(id)

    # OTHER BUSINESS LOGIC CAN BE ADDED HERE
    def get_by_name(self, name):
        for person in self.repository.get_all():
            if person.name == name:
                return person
        return None
    
    # FILTER PERSON BY AGE
    def filter_by_age(self, age):
        persons = []
        for person in self.repository.get_all():
            if person.age == age:
                persons.append(person)
        return persons