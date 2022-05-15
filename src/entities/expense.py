class Expense:
    """ Class that expresses Expenses
    """

    def __init__(self, expense_id, name, value, category, date, owner):
        """Constructor for the class that creates new expense

        Args:
            expense_id (Int): primary key
            name (String): name of the expense
            value (String): value of the expense
            category (String): user's existing category
            date (Date): date when the expense is created
            owner (String): username of the user who creates expense
        """

        self.name = name
        self.value = value
        self.expense_id = expense_id
        self.category = category
        self.date = date
        self.owner = owner
