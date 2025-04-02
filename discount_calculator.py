# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): Original price of the item.
    discount_percent (float): Discount percentage.

    Returns:
    float: Final price after applying the discount if discount is 20% or higher,
           otherwise returns the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Main program to prompt user input and display the final price
def main():
    try:
        # Prompt user for original price and discount percentage
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price using the function
        final_price = calculate_discount(price, discount_percent)
        
        # Display the result
        if final_price == price:
            print(f"No discount applied. The original price is: ${price:.2f}")
        else:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
