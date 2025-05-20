class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._orders = []
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
    
    @property
    def name(self):
        return self._name