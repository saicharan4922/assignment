class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        
class Admin:
    def __init__(self):
        self.food_items = []
        
    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)
        print("Food item added successfully!")
        
    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found.")
        
    def view_food_items(self):
        for food_item in self.food_items:
            print(f"ID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
            
    def remove_food_item(self, food_id):
        for index, food_item in enumerate(self.food_items):
            if food_item.food_id == food_id:
                self.food_items.pop(index)
                print("Food item removed successfully!")
                return
        print("Food item not found.")

admin = Admin()

# Adding a food item
admin.add_food_item("Pizza", "Large", 12.99, 0.1, 50)

# Editing a food item
admin.edit_food_item(1, "Pizza", "Medium", 9.99, 0.05, 75)

# Viewing all food items
admin.view_food_items()

# Removing a food item
admin.remove_food_item(1)
