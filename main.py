def print_mirrored_triangle(rows):
    """Prints a mirrored right-angled triangle of stars."""
    for i in range(1, rows + 1):
        # Print spaces first to create the mirror effect
        print(" " * (rows - i) + "*" * i)

def main():
    try:
        # Take user input
        rows = int(input("Enter the number of rows: "))
        
        # Validate input
        if rows <= 0:
            print("Please enter a positive integer greater than zero.")
            return
        
        # Print the mirrored triangle
        print_mirrored_triangle(rows)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()