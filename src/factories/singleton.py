# singleton.py

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new DatabaseConnection instance...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = "Connected"
        return cls._instance

    def get_connection(self):
        return self.connection
