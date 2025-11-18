import pandas as pd
from faker import Faker
import sqlite3
from datetime import datetime
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

def generate_users(n=1000):
    data = []
    for _ in range(n):
        data.append({
            "user_id": fake.uuid4(),
            "name": fake.name(),
            "age": random.randint(16, 60),
            "country": fake.country(),
        })
    return pd.DataFrame(data)

def generate_purchases(users, n=5000):
    data = []
    for _ in range(n):
        user = users.sample(1).iloc[0]
        data.append({
            "purchase_id": fake.uuid4(),
            "user_id": user["user_id"],
            "item": random.choice(["Gold Pack", "Skins", "Boost", "Loot Box"]),
            "amount": round(random.uniform(1.0, 99.0), 2),
            "timestamp": fake.date_time_this_year()
        })
    return pd.DataFrame(data)

def save_to_sqlite(users, purchases, db_path="output/database.db"):
    conn = sqlite3.connect(db_path)
    users.to_sql("users", conn, if_exists="replace", index=False)
    purchases.to_sql("purchases", conn, if_exists="replace", index=False)
    conn.close()

def main():
    users = generate_users()
    purchases = generate_purchases(users)
    
    users.to_csv("data/users.csv", index=False)
    purchases.to_csv("data/purchases.csv", index=False)
    
    save_to_sqlite(users, purchases)
    print("Data generated.")

if __name__ == "__main__":
    main()
