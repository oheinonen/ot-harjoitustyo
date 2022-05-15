class Category:
    """ Class that expresses Categories
    """

    def __init__(self, category_id, name, owner):
        """Constructor for the class that creates new category

        Args:
            category_id (Int): primary key
            name (String): name of the category
            owner (String): username of the user who creates category
        """

        self.name = name
        self.owner = owner
        self.category_id = category_id
