createTableProductsSql = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXTO NOT NULL,
        almount INTEGER NOT NULL,
        cost_price INTEGER NOT NULL,
        public_cost INTEGER NOT NULL
    )
'''
createTableFinancesSql = '''
    CREATE TABLE IF NOT EXISTS finances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bills INTEGER NOT NULL,
        sold INTEGER NOT NULL,
        profits INTEGER NOT NULL
    )
'''