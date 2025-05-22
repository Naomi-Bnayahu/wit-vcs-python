from datetime import date

class Commit:
    def __init__(self, creation_date, description, hashcode) :
        self.creation_date = creation_date
        self.description = description
        self.hashcode = hashcode

    def __str__(self):
        return f"hashcode: {self.hashcode} | description: {self.description} | date: {self.creation_date}"

    #ממירה את האובייט כומיט למילון
    def to_dict(self):
        return {
            'creation_date':self.creation_date.isoformat(),
            'description': self.description,
            'hashcode': self.hashcode
        }

#ממירה את המילון לכומיט
    @classmethod
    def to_commit(cls,data):
        return cls(creation_date=date.fromisoformat(data['creation_date']),description=data['description'],hashcode=data['hashcode'])



