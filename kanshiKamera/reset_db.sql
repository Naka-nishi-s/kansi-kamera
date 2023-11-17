DROP TABLE IF EXISTS watch_room_video;
CREATE TABLE watch_room_video(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path VARCHAR(100) NOT NULL,
    created_at DATE DEFAULT (date('now'))
);