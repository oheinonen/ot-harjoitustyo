class Expense:

    def __init__(self, expense_id, name, value, category, date, owner):
        self.name = name
        self.value = value
        self.expense_id = expense_id
        self.category = category
        self.date = date
        self.owner = owner
