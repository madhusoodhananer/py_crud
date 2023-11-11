import mysql.connector

# Database connection settings
db = mysql.connector.connect(
    host="localhost", 
    user="root", #change this to your username
    password="123456", #change this to your password
    database="python" #change this to your database
)

cursor = db.cursor()


def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    values = (name, price, quantity)

    cursor.execute(sql, values)
    db.commit()

    print("Product created successfully!")


def read_products():
    sql = "SELECT id, name, price, quantity FROM products"
    cursor.execute(sql)

    products = cursor.fetchall()

    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")


def update_product():

    
        id = int(input("Enter product ID: "))
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        quantity = int(input("Enter new product quantity: "))

        sql = "UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s"
        values = (name, price, quantity, id)

        cursor.execute(sql, values)
        db.commit()

        print("Product updated successfully!")


def delete_product():
    id = int(input("Enter product ID: "))

    sql = "DELETE FROM products WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)
    db.commit()

    print("Product deleted successfully!")


def main_menu():
    print("Welcome to the product CRUD application!")
    print("------------------------------------")

    while True:
        print("Please select an option:")
        print("1. Create Product")
        print("2. Read Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            create_product()
        elif option == 2:
            read_products()
        elif option == 3:
            update_product()
        elif option == 4:
            delete_product()
        elif option == 5:
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main_menu()