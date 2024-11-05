import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('videos_yt.db')
cursor = conn.cursor()

# Create videos table if it doesn't exist
cursor.execute("""
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   video_name TEXT NOT NULL,
                   description TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               """)

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(video_name, video_description, time):
    cursor.execute("""
                    INSERT INTO videos (video_name, description, time) VALUES(?, ?, ?)
                    """, (video_name, video_description, time))
    conn.commit()

def update_video(video_id, video_name, video_description, time):
    cursor.execute("""
                   UPDATE videos SET video_name = ?, description = ?, time = ? WHERE id = ?
                   """, (video_name, video_description, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("""
                   DELETE FROM videos WHERE id = ?
                   """, (video_id,))
    conn.commit()

def show_choices():
    print("1. List all videos")
    print("2. Add video")
    print("3. Update video")
    print("4. Delete video")
    print("5. Exit app")

def main():
    while True:
        print("\nYOUTUBE MANAGER APP")
        show_choices()
        
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                video_name = input("Enter the name for the video: ")
                video_description = input("Enter the description: ")
                time = input("Enter the time: ")
                add_video(video_name, video_description, time)
            case "3":
                video_id = input("Enter the ID to be updated: ")
                video_name = input("Enter the new name for the video: ")
                video_description = input("Enter the new description: ")
                time = input("Enter the new time: ")
                update_video(video_id, video_name, video_description, time)
            case "4":
                video_id = input("Enter the ID to delete: ")
                delete_video(video_id)
            case "5":
                print("Exiting...")
                break
            case _:
                print("Please enter a valid choice between 1-5")

    conn.close()

if __name__ == "__main__":
    main()