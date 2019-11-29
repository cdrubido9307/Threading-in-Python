import time
import concurrent.futures

class Account:
    def __init__(self):
        # Shered Data
        self.balance = 100
    def update(self, transaction, amount):
        print(f'{transaction} thread updating...')
        local_copy = self.balance
        local_copy += amount
        time.sleep(1)
        self.balance = local_copy
        print(f'{transaction} thread finishing...')

if __name__ == '__main__':
        account = Account()
        print(f'Starting account balance: {account.balance}')
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as trans_ex:
            for transaction, amount in [('deposit', 50), ('withdrawal', -150)]:
                trans_ex.submit(account.update, transaction, amount)
        print(f'Ending balance of {account.balance}')