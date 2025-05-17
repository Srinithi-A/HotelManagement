import mysql.connector
from mysql.connector import Error

# Initialize global variables
myconnection = None
cursor = None
username = "root"
password = ""  # XAMPP default is empty password
roomrent = 0
restaurantbill = 0
totalamount = 0
cid = ""

def MYSQLconnectioncheck():
    global myconnection
    try:
        myconnection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="MYHOTEL"
        )
        if myconnection.is_connected():
            print("\nCONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
            return myconnection
    except Error as e:
        print(f"\nERROR ESTABLISHING MYSQL CONNECTION: {e}")
        return None

def MYSQLconnectionisconnector():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="MYHOTEL"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"\nERROR ESTABLISHING MYSQL CONNECTION: {e}")
        return None

def userentry():
    global cid
    conn = MYSQLconnectionisconnector()
    if conn:
        try:
            cid = input("Enter customer identification number: ")
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            age = input("Enter customer age: ")
            nationality = input("Enter customer country: ")
            phoneno = input("Enter customer contact number: ")
            email = input("Enter customer email: ")
            
            cursor = conn.cursor()
            sql = 'INSERT INTO C_DETAILS (cid, name, address, age, nationality, phoneno, email) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            values = (cid, name, address, age, nationality, phoneno, email)
            cursor.execute(sql, values)
            conn.commit()
            print("\nNEW CUSTOMER ENTERED IN THE SYSTEM SUCCESSFULLY!")
        except Error as e:
            print(f"\nERROR: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def searchcustomer():
    conn = MYSQLconnectionisconnector()
    if conn:
        try:
            cid = input("Enter customer identification number to search: ")
            cursor = conn.cursor()
            sql = "SELECT * FROM C_DETAILS WHERE cid = %s"
            cursor.execute(sql, (cid,))
            result = cursor.fetchone()
            if result:
                print("\nCUSTOMER DETAILS:")
                print(f"CID: {result[0]}, Name: {result[1]}, Address: {result[2]}, Age: {result[3]}, "
                      f"Nationality: {result[4]}, Phone: {result[5]}, Email: {result[6]}")
            else:
                print("\nCUSTOMER NOT FOUND!")
        except Error as e:
            print(f"\nERROR: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def bookingrecord():
    global cid, roomrent
    conn = MYSQLconnectionisconnector()
    if conn:
        try:
            checkin = input("\nEnter customer checkin date [yyyy-mm-dd]: ")
            checkout = input("\nEnter customer checkout date [yyyy-mm-dd]: ")
            
            cursor = conn.cursor()
            sql = "INSERT INTO BOOKING_RECORD (cid, checkin_date, checkout_date) VALUES (%s,%s,%s)"
            values = (cid, checkin, checkout)
            cursor.execute(sql, values)
            conn.commit()
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY!")  
            
            print("\n#### ROOM OPTIONS ####")
            print("1. ULTRA ROYAL - Rs.10,000") 
            print("2. ROYAL - Rs.5,000")
            print("3. ELITE - Rs.3,500")
            print("4. BUDGET - Rs.2,500")
            
            roomchoice = int(input("Enter your option: "))
            roomno = int(input("Enter customer room no: "))
            noofdays = int(input("Enter number of days: "))
            
            if roomchoice == 1:
                roomrent = noofdays * 10000
            elif roomchoice == 2:
                roomrent = noofdays * 5000
            elif roomchoice == 3:
                roomrent = noofdays * 3500
            elif roomchoice == 4:
                roomrent = noofdays * 2500
            else:
                print("INVALID ROOM CHOICE!")
                return
            
            print(f"\nROOM RENT: Rs.{roomrent}")
            
            sql = "INSERT INTO ROOM_RENT (cid, room_type, room_no, days, rent) VALUES (%s,%s,%s,%s,%s)"
            values = (cid, roomchoice, roomno, noofdays, roomrent)
            cursor.execute(sql, values)
            conn.commit()
            print(f"ROOM BOOKED FOR {noofdays} DAYS SUCCESSFULLY!")
            
        except Error as e:
            print(f"\nERROR: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def restaurant():
    global cid, restaurantbill
    conn = MYSQLconnectionisconnector()
    if conn:
        try:
            print("\n=== RESTAURANT MENU ===")
            print("1. VEG COMBO Rs.300")
            print("2. NONVEG COMBO Rs.500")
            print("3. VEG AND NONVEG COMBO Rs.750")
            
            choice_dish = int(input("Enter your choice: "))
            quantity = int(input("Enter quantity: "))
            
            if choice_dish == 1:
                restaurantbill = quantity * 300
            elif choice_dish == 2:
                restaurantbill = quantity * 500
            elif choice_dish == 3:
                restaurantbill = quantity * 750
            else:
                print("INVALID CHOICE!")
                return
            
            sql = "INSERT INTO RESTAURANT (cid, item_type, quantity, amount) VALUES (%s,%s,%s,%s)"
            values = (cid, choice_dish, quantity, restaurantbill)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            print(f"\nTOTAL BILL AMOUNT: Rs.{restaurantbill}")
        except Error as e:
            print(f"\nERROR: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def totalamount():
    global cid, roomrent, restaurantbill, totalamount
    conn = MYSQLconnectionisconnector()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT name FROM C_DETAILS WHERE cid = %s"
            cursor.execute(sql, (cid,))
            customer = cursor.fetchone()
            
            if customer:
                name = customer[0]
                totalamount = roomrent + restaurantbill
                
                sql = "INSERT INTO TOTAL (cid, customer_name, room_rent, restaurant_bill, grand_total) VALUES (%s,%s,%s,%s,%s)"
                values = (cid, name, roomrent, restaurantbill, totalamount)
                cursor.execute(sql, values)
                conn.commit()
                
                print("\n" + "*" * 50)
                print("CUSTOMER BILL")
                print("*" * 50)
                print(f"NAME: {name}")
                print(f"ROOM RENT: Rs.{roomrent}")
                print(f"RESTAURANT BILL: Rs.{restaurantbill}")
                print(f"TOTAL AMOUNT: Rs.{totalamount}")
                print("*" * 50)
            else:
                print("\nCUSTOMER NOT FOUND!")
                
        except Error as e:
            print(f"\nERROR: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def main_menu():
    print("\n" + "*" * 50)
    print("HOTEL MANAGEMENT SYSTEM".center(50))
    print("*" * 50)
    
    if MYSQLconnectioncheck():
        while True:
            print("\nMAIN MENU")
            print("1. ENTER CUSTOMER DETAILS")
            print("2. BOOKING RECORD")
            print("3. RESTAURANT BILL")
            print("4. TOTAL BILL")
            print("5. SEARCH CUSTOMER")
            print("6. EXIT")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                userentry()
            elif choice == '2':
                bookingrecord()
            elif choice == '3':
                restaurant()
            elif choice == '4':
                totalamount()
            elif choice == '5':
                searchcustomer()
            elif choice == '6':
                print("\nThank you for using the system!")
                break
            else:
                print("INVALID CHOICE!")
                
if __name__ == "__main__":
    main_menu()
