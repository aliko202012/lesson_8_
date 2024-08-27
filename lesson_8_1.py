import sqlite3

class BankAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts 
                               (id INTEGER PRIMARY KEY, balance REAL)''')
        self.conn.commit()
        if not self._account_exists():
            self._create_account()

    def _account_exists(self):
        self.cursor.execute('SELECT * FROM accounts WHERE id=?', (self.account_id,))
        return self.cursor.fetchone() is not None

    def _create_account(self):
        self.cursor.execute('INSERT INTO accounts (id, balance) VALUES (?, ?)', 
                            (self.account_id, self.balance))
        self.conn.commit()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._update_balance()
        else:
            print("Сумма для пополнения должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._update_balance()
        elif amount > self.balance:
            print("Недостаточно средств для снятия")
        else:
            print("Сумма для снятия должна быть положительной")

    def get_balance(self):
        self.cursor.execute('SELECT balance FROM accounts WHERE id=?', (self.account_id,))
        return self.cursor.fetchone()[0]

    def _update_balance(self):
        self.cursor.execute('UPDATE accounts SET balance=? WHERE id=?', 
                            (self.balance, self.account_id))
        self.conn.commit()

    def close(self):
        self.conn.close()


account1 = BankAccount(1, 500)
account2 = BankAccount(2, 750)


account1.deposit(50)
account1.withdraw(30)
print(f"Баланс account1: {account1.get_balance()}") 


account2.deposit(200)
account2.withdraw(250)
print(f"Баланс account2: {account2.get_balance()}")


account1.close()
account2.close()