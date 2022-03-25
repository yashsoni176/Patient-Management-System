import sqlite3

con = sqlite3.connect("hospital.db")
cursor = con.cursor()
#
# sqlite_query = '''CREATE TABLE patient(
#                patientcode TEXT PRIMARY KEY,
#                name TEXT NOT NULL,
#                Address TEXT NOT NULL,
#               phone INTEGER NOT NULL);'''
# cursor.execute(sqlite_query)
def add():

    patientcode = input("Patient Code : ")
    name = input("Name : ")
    address = input("Address : ")
    phone = int(input("Phone number : "))

    cursor.execute("INSERT INTO patient VALUES(?,?,?,?)",(patientcode,name,address,phone))
    print("INSERTED SUCCESSFULLY!")
    con.commit()

def view():
    sql_view = "Select * FROM patient"
    cursor.execute(sql_view)

    records = cursor.fetchall()

    for item in records:
        print(item)

    con.commit()

while(True):
    print('''
          1. Add Patients
          2. View Patients
          3. EXIT ''')
    choice = int(input("Select an option : "))

    functions =[add,view]
    a = functions[choice-1]()
    ch = input("\n Press enter to continue OR press N to discontinue!")
    if (ch == "n" or ch == "N"):
        break
    else:
        pass



