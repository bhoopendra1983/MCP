
import sqlite3

conn = sqlite3.connect("countries.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS countries (
    name TEXT PRIMARY KEY,
    capital TEXT NOT NULL,
    continent TEXT NOT NULL,
    population INTEGER NOT NULL
)
""")

countries = [
    ("India", "New Delhi", "Asia", 1428600000),
    ("Japan", "Tokyo", "Asia", 124500000),
    ("France", "Paris", "Europe", 68000000),
]

conn.executemany("""
INSERT OR REPLACE INTO countries
(name, capital, continent, population)
VALUES (?, ?, ?, ?)
""", countries)

conn.commit()
conn.close()

print("Country database created.")
