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

    conn.execute(
        "INSERT INTO projects (title, content, img, repo_link, preview_link, display_order) VALUES (?, ?, ?, ?, ?, ?)",
        ("Nail salone website", "A static website for a nail salon, using MDB, an enhanced version of bootstrap",
        'nails-salon.jpg', 'https://github.com/mattiabotto/nails-salon-website', 'https://nailsbyalice.cz/', 1)
    )

    conn.execute(
        "INSERT INTO projects (title, content, img, repo_link, preview_link, display_order) VALUES (?, ?, ?, ?, ?, ?)",
        ("Calculator", "Final project for the fundamentals course of The Odin Project, a simple calculator build using" +
        " HTML, CSS and Javascript", "calculator.jpg", "https://github.com/mattiabotto/calculator", 
        "https://mattiabotto.github.io/calculator/", 2)
    )

    conn.commit()
    conn.close()

    print("Database succesfully reset")