import sqlite3
import os


SOURCE_DB = "db/source.db"
TARGET_DB = "db/target.db"


def create_source_database():

    connection = sqlite3.connect(SOURCE_DB)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS patient")

    cursor.execute("""
        CREATE TABLE patient (
            patient_id TEXT PRIMARY KEY,
            name TEXT,
            city TEXT
        )
    """)

    patients = [
        ("P101", "Amit", "Pune"),
        ("P102", "Rahul", "Mumbai"),
        ("P103", "Neha", "Delhi"),
        ("P104", "Priya", "Pune"),
        ("P105", "Kiran", "Bangalore")
    ]

    cursor.executemany("""
        INSERT INTO patient
        (patient_id, name, city)
        VALUES (?, ?, ?)
    """, patients)

    connection.commit()
    connection.close()


def create_target_database():

    connection = sqlite3.connect(TARGET_DB)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS patient")
    cursor.execute("DROP TABLE IF EXISTS claims")

    cursor.execute("""
        CREATE TABLE patient (
            patient_id TEXT PRIMARY KEY,
            name TEXT,
            city TEXT
        )
    """)

    patients = [
        ("P101", "Amit", "Pune"),
        ("P102", "Rahul", "Mumbai"),
        ("P103", "Neha", "Delhi"),
        ("P104", "Priya", "Pune"),
        ("P105", "Kiran", "Bangalore")
    ]

    cursor.executemany("""
        INSERT INTO patient
        (patient_id, name, city)
        VALUES (?, ?, ?)
    """, patients)

    cursor.execute("""
        CREATE TABLE claims (
            claim_id TEXT PRIMARY KEY,
            quantity INTEGER,
            unit_price REAL,
            total_amount REAL
        )
    """)

    claims = [
        ("C101", 2, 500, 1000),
        ("C102", 3, 200, 600),
        ("C103", 5, 100, 500)
    ]

    cursor.executemany("""
        INSERT INTO claims
        (claim_id, quantity, unit_price, total_amount)
        VALUES (?, ?, ?, ?)
    """, claims)

    connection.commit()
    connection.close()


if __name__ == "__main__":

    os.makedirs("db", exist_ok=True)

    create_source_database()
    create_target_database()

    print("Source and Target databases created successfully.")