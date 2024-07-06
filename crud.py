# CREATE DATABASE address_book_db;
# USE address_book_db;

# CREATE TABLE contacts (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     no VARCHAR(255) NOT NULL,
#     address VARCHAR(255) NOT NULL,
#     no_telp VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL
# );


import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='address_book_db'
)
cursor = conn.cursor()

def insert_contacts(no, address, no_telp, email):
    cursor.execute('''
    INSERT INTO contacts (no, address, no_telp, email)
    VALUES (%s, %s, %s, %s)
    ''', (no, address, no_telp, email))
    conn.commit()

def select_all_contacts():
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()

def update_contact(id, no=None, address=None, no_telp=None, email=None):
    query = 'UPDATE contacts SET '
    params = []
    
    if no is not None:
        query += 'no = %s, '
        params.append(no)
    if address is not None:
        query += 'address = %s, '
        params.append(address)
    if no_telp is not None:
        query += 'no_telp = %s, '
        params.append(no_telp)
    if email is not None:
        query += 'email = %s, '
        params.append(email)
        
    query = query.rstrip(', ')
    query += ' WHERE id = %s'
    params.append(id)
    
    cursor.execute(query, params)
    conn.commit()

def delete_contact(id):
    cursor.execute('DELETE FROM contacts WHERE id = %s', (id,))
    conn.commit()

if __name__ == '__main__':
    insert_contacts('0001', 'Green Cove', '021-123-456', 'yeppie@gmail.com')
    
    contacts = select_all_contacts()
    print('All Contacts:')
    for contact in contacts:
        print(contact)
    
    update_contact(1, address='kost zoe')
    
    contacts = select_all_contacts()
    print('All Contacts after update:')
    for contact in contacts:
        print(contact)
    
    delete_contact(1)
    
    contacts = select_all_contacts()
    print('All Contacts after delete:')
    for contact in contacts:
        print(contact)

conn.close()