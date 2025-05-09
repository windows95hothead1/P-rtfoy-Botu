import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database  # Name of the database

    def create_tables(self):
        """Creates the necessary tables in the database."""
        try:
            with sqlite3.connect(self.database) as con:
                # Create projects table
                con.execute("""
                    CREATE TABLE IF NOT EXISTS projects(
                        project_id INTEGER PRIMARY KEY,
                        user_id INTEGER,        
                        project_name TEXT,
                        url TEXT,        
                        description TEXT,
                        status_id INTEGER,
                        FOREIGN KEY(status_id) REFERENCES status(status_id)
                    )
                """)
                # Create status table
                con.execute("""
                    CREATE TABLE IF NOT EXISTS status(
                        status_id INTEGER PRIMARY KEY,
                        status_name TEXT
                    )
                """)
                # Create skills table
                con.execute("""
                    CREATE TABLE IF NOT EXISTS skills(
                        skill_id INTEGER PRIMARY KEY,
                        skill_name TEXT
                    )
                """)
                # Insert default data into status table
                status_data = [
                    (1, 'Prototip Oluşturma'),
                    (2, 'Geliştirme Aşamasında'),
                    (3, 'Tamamlanmış'),
                    (4, 'Güncelleme'),
                    (5, 'Terk edilmiş/Desteklenmiyor')
                ]
                con.executemany("INSERT OR IGNORE INTO status VALUES (?, ?)", status_data)

                # Insert default data into skills table
                skills_data = [
                    (1, 'Python'),
                    (2, 'Discord bot geliştirme'),
                    (3, 'SQL'),
                    (4, 'API'),
                    (5, 'HTML'),
                    (6, 'CSS'),
                    (7, 'FLASK'),
                    (8, 'AI')
                ]
                con.executemany("INSERT OR IGNORE INTO skills VALUES (?, ?)", skills_data)
 
                print("Tables created and default data inserted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            con.commit()
            con.close()  # Commit changes within the 'with' block

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()