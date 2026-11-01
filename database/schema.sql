DROP TABLE IF EXISTS content;

CREATE TABLE content (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    page_name TEXT NOT NULL,
    content_name TEXT NOT NULL,
    content TEXT
);

CREATE UNIQUE INDEX id ON content(id);