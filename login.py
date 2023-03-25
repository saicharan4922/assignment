import sqlite3


conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL);''')

def register():
    name = input("Enter Full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")
    cursor.execute("INSERT INTO users (name, phone, email, address, password) VALUES (?, ?, ?, ?, ?)", 
                   (name, phone, email, address, password))
    conn.commit()
    print("Registration Successful!")


register()

cursor.close()
conn.close()





import sqlite3


conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()


def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        print("Login Successful!")
    else:
        print("Invalid Email or Password. Please try again.")


login()


cursor.close()
conn.close()






def display_options():
    print("Please choose an option:")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")


display_options()







food_menu = {
    1: {"name": "Tandoori Chicken", "quantity": 4, "price": 240},
    2: {"name": "Vegan Burger", "quantity": 1, "price": 320},
    3: {"name": "Truffle Cake", "quantity": "500gm", "price": 900}
}

user_data = {}

order_history = []
def place_order():
    selected_items = []
    print("Please select the items you want to order by entering the corresponding numbers separated by commas:")
    for item in food_menu:
        print(f"{item}. {food_menu[item]['name']} ({food_menu[item]['quantity']}) [INR {food_menu[item]['price']}]")
    item_numbers = input().split(",")
    for number in item_numbers:
        selected_items.append(food_menu[int(number)])
    print("You have selected the following items:")
    for item in selected_items:
        print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
    confirm_order = input("Do you want to place the order? (Y/N)").upper()
    if confirm_order == "Y":
        order_history.append(selected_items)
        print("Order placed successfully!")
    else:
        print("Order cancelled.")


def show_order_history():
    print("Your previous orders:")
    for order in order_history:
        print("Items:")
        for item in order:
            print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
        print("----------")


def update_profile():
    print("Update your profile:")
    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    user_data["full_name"] = full_name
    user_data["phone_number"] = phone_number
    user_data["email"] = email
    user_data["address"] = address
    user_data["password"] = password
    print("Profile updated successfully!")



def main():
    print("Welcome to the restaurant app!")
    while True:
        print("Please select an option:")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        option = input()
        if option == "1":
            place_order()
        elif option == "2":
            show_order_history()
        elif option == "3":
            update_profile()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

