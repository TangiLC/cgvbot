CREATE TABLE IF NOT EXISTS Logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation FOREIGN KEY id.Conversations,
    date DATETIME NOT NULL,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL,
    statut FOREIGN KEY,
);