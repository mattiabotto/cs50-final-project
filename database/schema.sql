DROP TABLE IF EXISTS content; 

CREATE TABLE content (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    page_name TEXT NOT NULL,
    content_name TEXT NOT NULL,
    content TEXT,
    is_multipara INTEGER DEFAULT 0
);
CREATE UNIQUE INDEX id ON content(id);


DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    img TEXT,
    repo_link TEXT,
    preview_link TEXT,
    display_order INTEGER DEFAULT 0
);