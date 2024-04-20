import sys
import Webfinder

def main():
    print("Welcome to the Information System CLI!")
    while True:
        print("\nSelect an option:")
        print("1. View personal information")
        print("2. View educational information")
        print("3. View professional information")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                view_personal_info()
            case "2":
                view_educational_info()
            case "3":
                view_professional_info()
            case "4":
                print("Exiting the Information System CLI. Goodbye!")
                sys.exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

def view_personal_info():
    print("\nPersonal Information:")
    print("Name: John Doe")
    print("Age: 30")
    print("Address: 123 Main Street, Anytown, USA")
    # Add more personal information as needed

def view_educational_info():
    print("\nEducational Information:")
    print("Degree: Bachelor of Science in Computer Science")
    print("University: University of Example")
    print("Year of Graduation: 2015")
    # Add more educational information as needed

def view_professional_info():
    print("\nProfessional Information:")
    print("Position: Software Engineer")
    print("Company: Tech Corp")
    print("Years of Experience: 5")
    # Add more professional information as needed

if __name__ == "__main__":
    main()
