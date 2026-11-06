class Transaction:
    def __init__(self, user_id, amount, status):
        self.user_id = user_id
        self.amount = amount
        self.status = status


def filter_completed_transactions(transactions, min_amount):
    filtered_list = []
    for txn in transactions:
        if txn.status == "completed" and txn.amount >= min_amount:
            filtered_list.append(txn)
    return filtered_list


data = [
    Transaction(101, 150.50, "completed"),
    Transaction(102, 45.00, "pending"),
    Transaction(103, 320.00, "completed"),
    Transaction(104, 80.00, "cancelled"),
    Transaction(105, 500.00, "completed"),
]

if __name__ == "__main__":
    threshold = 100.0
    high_value_sales = filter_completed_transactions(data, threshold)

    print(f"Transactions above ${threshold}:")
    for item in high_value_sales:
        print(f"User {item.user_id}: ${item.amount:.2f}")
