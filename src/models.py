class Expense:
    def __init__(self, title, category, amount, date):
        self.title = title
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }