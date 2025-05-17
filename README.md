Hotel Management System
Welcome to the Hotel Management System, a console-based application designed to efficiently manage hotel bookings, restaurant services, and billing.
This project provides an interactive system for handling customer details, reservations, and payments, all integrated with MySQL for data storage.

📌 Technology Used:
Python: Core programming language for system functionalities.
MySQL: Database management for storing customer and booking records.
MySQL Connector: Establishing connection between Python and MySQL database using xampp

📌 Features:
This system is designed to streamline hotel management operations, including:
Customer Management: Store and retrieve customer details efficiently.
Room Booking: Book rooms with predefined options and automated rent calculations.
Restaurant Services: Maintain restaurant order records and billing.
Billing System: Generate total payment summary, including room rent and food expenses.
Search Functionality: Look up customer records using their identification number.

📌 Project Structure:
root/  
├── database/  
│   ├── hms.sql  # MySQL database schema for hotel management system  
├── python/  
│   ├── hotel_management.py  # Main Python script for hotel operations  
└── README.md  # Documentation for setup and usage  
 
📌 How to Run the Project with XAMPP:
1️⃣ Install Python 3.x if not already installed.
2️⃣ Install MySQL Connector using: pip install mysql-connector-python
3️⃣ Set up MySQL using XAMPP:
Download and install XAMPP.
Start Apache and MySQL services from the XAMPP control panel.
Open phpMyAdmin (http://localhost/phpmyadmin).
Create a new database named MYHOTEL.
4️⃣ Update MySQL connection details in your Python script (hotel_management.py): myconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Default XAMPP password is empty
    database="MYHOTEL"
)
5️⃣ Run the program

📌 Contact:
Hey, I am always open to feedback, suggestions, collaborations, and improvements!
GitHub: https://github.com/Srinithi-A
LinkedIn: https://www.linkedin.com/in/srinithia?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
