from bd.Connection import Connection
from choices import ACTIONS
from utils.cleanTerminal import cleanTerminal
from views.drawPrincipalMenu import drawPrincipalMenu

db = Connection()
db.createDatabaseStructure()
db.getConnection().close()

def run():
    cleanTerminal()
    while True:
        choice = drawPrincipalMenu()
        ACTIONS.get(str(choice))()
        break;
run()