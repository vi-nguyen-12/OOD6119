import mysql.connector
import configparser

# [tutorial] Create MySQL database in Azure and using MySQL Workbench app to connect to it
# https://www.youtube.com/watch?v=O6tlkpFmZds&t=536s
class DatabaseAccessLayer:
    def __init__(self, config_file='config.ini'):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.connection = mysql.connector.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config["Database"]['password'],
            database=config['Database']['database']
        )
        self.cursor = self.connection.cursor()
        print("Connect to the MySQL database!")

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()
            return False

    def fetch_data(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


# if __name__ == "__main__":
#     # MySQL database credentials
#     db = DatabaseAccessLayer(config_file='config.ini')

#     #print("Connected to the MySQL database!")

#     # Insert ItemType data
#     insert_query_item_type = "INSERT INTO ItemType (name, description) VALUES (%s, %s)"
#     data_item_type = ("Novel", "Fictional classic narrative")
#     db.execute_query(insert_query_item_type, data_item_type)

#     # Insert ItemType data
#     insert_query_item_type = "INSERT INTO ItemType (name, description) VALUES (%s, %s)"
#     data_item_type = ("Kids", "Fictional classic tale that embarks on a whimsical adventure.")
#     db.execute_query(insert_query_item_type, data_item_type)

#     # Insert ItemType data
#     insert_query_item_type = "INSERT INTO ItemType (name, description) VALUES (%s, %s)"
#     data_item_type = ("Biography", "Elon biography delves into his extraordinary life and visionary mind.")
#     db.execute_query(insert_query_item_type, data_item_type)

#     # Insert Adventure item type
#     insert_query_adventure = "INSERT INTO ItemType (name, description) VALUES (%s, %s)"
#     data_adventure = ("Adventure", "Exciting and often risky experiences")
#     db.execute_query(insert_query_adventure, data_adventure)

#     # Retrieve ItemType data
#     select_query_item_type = "SELECT _id FROM ItemType WHERE name = %s"
#     data_item_type_name = ("Adventure",)  # Adjust based on the ItemType
#     type_id = db.fetch_data(select_query_item_type, data_item_type_name)
    

#     # Insert The Adventure of Tom Sawyer data
#     insert_query_the_adventure_of_tom_sawyer = "INSERT INTO Book (title, author, year, `#`, availability) VALUES (%s, %s, %s, %s, %s)"
#     data_the_adventure_of_tom_sawyer = ("The Adventure of Tom Sawyer", "Mark Twain", 1876, 2, False)
#     db.execute_query(insert_query_the_adventure_of_tom_sawyer, data_the_adventure_of_tom_sawyer)

#      # Retrieve ItemType data
#     select_query_item_type = "SELECT _id FROM ItemType WHERE name = %s"
#     data_item_type_name = ("Novel",)  # Adjust based on the ItemType
#     type_id = db.fetch_data(select_query_item_type, data_item_type_name)

#     # Retrieve ItemType data
#     select_query_item_type = "SELECT _id FROM ItemType WHERE name = %s"
#     data_item_type_name = ("Kids",)  # Adjust based on the ItemType
#     type_id = db.fetch_data(select_query_item_type, data_item_type_name)

#     # Retrieve ItemType data
#     select_query_item_type = "SELECT _id FROM ItemType WHERE name = %s"
#     data_item_type_name = ("Biography",)  # Adjust based on the ItemType
#     type_id = db.fetch_data(select_query_item_type, data_item_type_name)



#     # Insert The Great Gatsby data
#     insert_query = "INSERT INTO Book (title, author, year, type_id, availability) VALUES (%s, %s, %s, %s, %s)"
#     data = ("The Great Gasby", "FScott Fitzgerald", 1925, 1, True)
#     db.execute_query(insert_query, data)
#     #success = db.execute_query(insert_query, data)
#     #print("The Great Gatsby data inserted successfully!" if success else "Failed to insert The Great Gatsby data.")


#     # Insert Little Red Riding Hood data
#     insert_query_little_red_riding_hood = "INSERT INTO Book (title, author, year, type_id, availability) VALUES (%s, %s, %s, %s, %s)"
#     data_little_red_riding_hood = ("Little Red Riding Hood", "Charles Perrault", None, 2, True)
#     db.execute_query(insert_query_little_red_riding_hood, data_little_red_riding_hood)

#     # Insert Elon Musk data
#     insert_query_elon_musk = "INSERT INTO Book (title, author, year, type_id, availability) VALUES (%s, %s, %s, %s, %s)"
#     data_elon_musk = ("Elon Musk", "Walter Isaacson", None, 3, True)
#     db.execute_query(insert_query_elon_musk, data_elon_musk) 


#     # Retrieve data
#     select_query_books = "SELECT * FROM Book"
#     books = db.fetch_data(select_query_books)

#     # Display the retrieved data
#     for book in books:
#         print(f"Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, #: {book[4]}, Availability: {book[5]}")

#     # Retrieve data from ItemType table
#     select_query_item_types = "SELECT * FROM ItemType"
#     item_types = db.fetch_data(select_query_item_types)

#     # Display the retrieved data
#     for item_type in item_types:
#         print(f"#: {item_type[0]}, Name: {item_type[1]}, Description: {item_type[2]}")

#     # Retrieve data from ReservedBook table
#     select_query_reserved_books = "SELECT * FROM ReservedBook"
#     reserved_books = db.fetch_data(select_query_reserved_books)

#     # Display the retrieved data
#     for reserved_book in reserved_books:
#         print(f"Reserved Book ID: {reserved_book[0]}, User ID: {reserved_book[1]}, Book ID: {reserved_book[2]}, Reserve Date: {reserved_book[3]}")

#     # close the connection
#     db.close_connection()
# db_connection= DatabaseAccessLayer(config_file='config.ini')
