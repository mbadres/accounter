from models.record import Record


class Daybook:

    def __init__(self):
        self.records = []

    def add(self, record: Record):
        self.records.append(record)


daybook = Daybook()
