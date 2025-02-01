import json

# Functions to save data
DATA_FILE = "data.json"

def save_data(products, basket, budget):
    data = {
        "products": products,
        "basket": basket,
        "budget": budget
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    

# Function to load data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data["products"], data["basket"], data["budget"]
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or error in reading, return default values
        return [], [], 0.0  
    

# Display all products
def display_products(products):
        print("Available products : ")
        for i, product in enumerate(products):
            print(f"\n{i}: {product} ")
        
        if not products:
            print("\nNo available products.")
            
        return products
    

# Function to buy products
def buy_products(products, basket, budget):
        # Display products function
        display_products(products)
        
        if not products:
            print("\nNo products available.")
            return
        
        try:         
            num_of_items_to_buy = int(input("\nPlease enter how many products to buy : "))
            
            for i in range(num_of_items_to_buy):
                product_to_buy = input("\nItem name : ")
                quantity_to_buy = int(input("Enter how many to buy : "))
                
                # Assuming no products is found
                found = False
                
                # Else if product is found
                for product in products:
                    if product["Name"] == product_to_buy:
                        found = True
                        
                        # Multiply the product price to the quantity to calculate the total price                       
                        total_price = product["Price"] * quantity_to_buy
                         
                        if product["Quantity"] >= quantity_to_buy:
                            # If the user has enough budget
                            if budget >= total_price:  
                                product["Quantity"] -= quantity_to_buy  
                                basket.append({"Name": product_to_buy, "Quantity": quantity_to_buy})
                                
                                # Subtract the budget to the total price
                                budget -= total_price  
                                print(f"\nSuccessfully added to basket! Remaining budget: {budget:.2f}")
                            else:
                                 print("\nNot enough budget.")
                        else:
                            print("\nNot enough stock available.")
                        break 
            
                # Just to check if the product is not available
                if not found:
                    print("\nItem not available.")
            
        except ValueError:
            print("\nPlease enter a valid input.")
            
        return products, basket, budget
            

# Function to add some products
def add_products(products):
        try:
            num_of_products = int(input("\nPlease enter how many items to sell : "))
            
            for i in range(num_of_products):
                product_name = input("\nProduct name :")
                quantity = int(input("Enter the quantity : "))
                price = float(input("Enter the price : "))
                    
                # Store it in a dictionary and append it to the list
                added_items = {"Name": product_name, "Quantity": quantity, "Price": price}
                
                products.append(added_items)
                print("\nItems successfully added!")
                
        except ValueError:
                print("\nPlease input a valid input!")
                
        return products
   

# Function to remove some products
def remove_product_in_products(products):
    # Just to check if there are any existing products
    if not products:
        print("\nNo items to remove.")
        return products
    
    # Display function
    display_products(products)
    
    try:      
        choose = int(input("\nSelect an item to remove : "))
            
        # If the product is not in the list
        if choose < 0 or choose >=len(products):
            print("\nProduct to remove not found. Please try again.")
            return products   
       
        # If the product exist then remove
        products.pop(choose)
        print("\nSuccessfully removed!")
           
    except ValueError:
        print("\nPlease enter a valid input!")
        
    return products
            

# Function to display your bought products
def view_products_bought(basket, budget):
    # Display basket list
    for i, item in enumerate(basket):
        print(f"{i} : {item}")
        
    # Check if the basket is empty
    if not basket:
        print("\nYou have no items bought.")
    
    # Print budget
    print("\nRemaining budget : ", budget)
    
    while True:
       try:
           print("\n1. Remove an item")
           print("2. Remove all items")
           print("0. Exit")
        
           choice = int(input("\nSelect a choice : "))
        
           if choice == 1:
               # Check if you have bought any products if none it will return to menu
                if not basket:
                    print("\nYou have no items bought.")
                    continue
                
                delete = int(input("\nSelect the item to delete : "))
             
                # If the item is found then delete or if not return to menu
                if 0 <= delete < len(basket):
                    basket.pop(delete)
                    print("\nSuccessfully removed!")
                else:
                    print("\nItem to remove not in the basket!")
           elif choice == 2:
                # Check if there are any items
                if not basket:
                    print("\nYou have no items bought.")
                    continue
                
                clarify = input("\nAre you sure you want to delete all items? (yes/no): ")
            
                if clarify.lower() == "yes":
                    basket.clear()
                    print("\nAll items deleted!")
                elif clarify.lower() == "no":
                    print("\nNo items deleted!")
                else:
                    print("\nPlease type yes or no only")
           elif choice == 0:
               break
           else:
               print("\nInput not in the menu!")
           
       except ValueError:
           print("\nInput invalid!")
           continue
           
    return basket, budget
       
    
print("Welcome to the product selling store.")

products = []
basket = []
budget = 0.00

# Load your saved data
products, basket, budget = load_data()

while True:
        try:
            print("\n[1] View products")
            print("[2] Add products")
            print("[3] Buy products")
            print("[4] Remove products")
            print("[5] View bought products")
            print("[0] Exit")
        
            choice = int(input("\nPlease select from the options :"))
        
            if choice == 1:
                products = display_products(products)
            elif choice == 2:
                products = add_products(products)
            elif choice == 3:
                budget = float(input("\nEnter your budget: "))
                products, basket, budget = buy_products(products, basket, budget)
            elif choice == 4:
                products = remove_product_in_products(products)
            elif choice == 5:
                basket, budget = view_products_bought(basket, budget)
            elif choice == 0:
                print("\nProgram exiting...")
                # Save all data before exiting
                save_data(products, basket, budget)
                break
        except ValueError:
            print("\nPlease enter a valid input!")
            continue
