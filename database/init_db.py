import sqlite3

is_sure = input("The database will be reset and his data will be lost, are you sure (yes/no)?  ")

if is_sure.lower() in ['yes', 'y']:
    conn = sqlite3.connect('mattiabtech.db')

    with open('schema.sql') as f:
        conn.executescript(f.read())

    conn.execute(
        "INSERT INTO content (page_name, content_name, content) VALUES (?, ?, ?)",
        ('about', 'title', 'About me')
    )

    conn.execute(
        "INSERT INTO content (page_name, content_name, content, is_multipara) VALUES (?, ?, ?, ?)",
        ('about', 'biography', 'Some amazing biography', 1)
    )

    conn.commit()
    conn.close()

    print("Database succesfully reset")