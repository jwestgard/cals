#!/usr/bin/env python3

import csv
import sqlite3
import sys

DB_PATH    = "data/example.sqlite"
INPUT_PATH = sys.argv[1]
INSERT_CMD = '''INSERT INTO foods (name, serving, cals) 
                VALUES ("{food.name}", "{food.serving}", {food.cals})'''
CREATE_CMD = '''CREATE TABLE foods(id INTEGER PRIMARY KEY,
                    name TEXT, serving TEXT, cals INTEGER)'''
DROP_CMD   = '''DROP TABLE IF EXISTS foods'''


class Food:
    def __init__(self, name, serving, grams, cals, fat, carbs, protein):
        self.name    = name
        self.serving = serving
        self.grams   = grams
        self.cals    = cals
        self.fat     = fat
        self.carbs   = carbs
        self.protein = protein


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(DROP_CMD)
    cursor.execute(CREATE_CMD)
    with open(INPUT_PATH) as inputfile:
        reader = csv.DictReader(inputfile, delimiter='\t')
        for d in reader:
            f = Food(**d)
            cursor.execute(INSERT_CMD.format(food=f))
    cursor.execute('SELECT * FROM foods')
    print("Loaded {} rows into foods table".format(len(cursor.fetchall())))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
