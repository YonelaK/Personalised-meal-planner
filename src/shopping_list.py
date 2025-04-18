class ShoppingList:
    def __init__(self, id):
        self._id = id
        self._items = []

    def view_items(self):
        return self._items
