# A simple greeting script to test Python
def main():
    print("--- Welcome to your Git-cloned Project! ---")
    
    # Get user input
    name = input("What is your name? ")
    
    # Print a formatted greeting
    if name:
        print(f"Hello, {name}! Your Python file is running perfectly.")
    else:
        print("Hello, Stranger! Everything looks good.")

if __name__ == "__main__":
    main()
