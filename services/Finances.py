from bd.Connection import Connection

class Finances:
    def __init__(self):
        instaConnection = Connection()
        self.connection = instaConnection.getConnection()
        self.cursor = instaConnection.getCursor()