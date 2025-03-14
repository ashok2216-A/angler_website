from supabase import create_client, Client
import getpass

# Initialize Supabase client
SUPABASE_URL = 'https://nlseukvysoshudzdvfzu.supabase.co'  # Replace with your Supabase URL
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sc2V1a3Z5c29zaHVkemR2Znp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE4NDg0NjAsImV4cCI6MjA1NzQyNDQ2MH0.JlfPqzxbH2lHXqT3rARjN0YAvqUOHF2oGdvdsXfT_VY'  # Replace with your Supabase API key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def signup():
    print("=== Sign Up ===")
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")

    try:
        # Sign up the user
        user = supabase.auth.sign_up({"email": email, "password": password})
        print("Signup successful! Check your email for confirmation.")
        print("User:", user)
    except Exception as e:
        print(f"Error during signup: {e}")

def login():
    print("=== Login ===")
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")

    try:
        # Log in the user
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        print("Login successful!")
        print("User:", user)
    except Exception as e:
        print(f"Error during login: {e}")

def main():
    while True:
        print("\n1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()