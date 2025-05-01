import sqlite3

# connect to SQLite database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT                                            
         )
""")

# function to add a contact
def add_contact(name, phone, email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?,?,?)", (name, phone, email))
    conn.commit()
    print("Contact added successfully")


# function to view all contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        print(row)


# function to update a contact
def update_contact(contact_id, name, phone, email):
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? where id = ?", (name,phone,email,contact_id))
    conn.commit()
    print("Contact Updated")


# function to delete a contact
def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id))
    conn.commit()
    print("Contact deleted")


# function to close connection
def close_connection():
    conn.close()



