import json
import os
from waste_logging import log_waste_entry

# File used to store waste records
DATA_FILE = "waste_log.json"


def display_main_menu():
    """Display the main EcoTrack menu."""

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║              🌱  E C O T R A C K  🌱            ║")
    print("║          Sustainable Waste Tracker ♻️            ║")
    print("║                                                  ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║                                                  ║")
    print("║       ♻️  1. Log Waste                           ║")
    print("║       📊  2. Recycling Summary                   ║")
    print("║       🌍  3. Environmental Impact                ║")
    print("║       📖  4. View Waste History                  ║")
    print("║       🔎  5. Search Waste History                ║")
    print("║       💡  6. Get Recommendations                 ║")
    print("║       🚪  7. Exit                                ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print("          🌿 Small actions. Greener cities. 🌿\n")


def load_data():
    """
    Load waste records from the JSON file.

    Returns an empty list if the file does not exist
    or if the stored data is invalid.
    """

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        print("\n⚠️  Unable to load previous data.")
        print("🌱 Starting with an empty waste log.\n")
        return []


def save_data(waste_log):
    """
    Save the current waste records to the JSON file.
    """

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(waste_log, file, indent=4)

    except OSError:
        print("\n⚠️  There was a problem saving your data.")


def get_menu_choice():
    """
    Get and validate the user's menu choice.

    Returns a valid number between 1 and 7.
    """

    while True:
        choice = input("🌱 Choose an option (1-7): ").strip()

        if not choice.isdigit():
            print("\n⚠️  Please enter a number from 1 to 7.")
            continue

        choice = int(choice)

        if 1 <= choice <= 7:
            return choice

        print("\n⚠️  Invalid choice. Please choose a number from 1 to 7.")


def main():
    """
    Main function that controls the EcoTrack application.
    """

    # Load previously saved waste records
    waste_log = load_data()

    # Welcome message
    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║           🌿 WELCOME TO ECOTRACK 🌿              ║")
    print("║                                                  ║")
    print("║     Your little step towards a greener city     ║")
    print("║                                                  ║")
    print("║          ♻️  Reduce • Reuse • Recycle  ♻️        ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")

    # Main program loop
    while True:

        display_main_menu()
        choice = get_menu_choice()

        if choice == 1:
            log_waste_entry(waste_log)
            save_data(waste_log)

            # Member 2's function will be connected here.

        elif choice == 2:
            print("\n📊 Opening Recycling Summary...")
            print("Please wait for the recycling summary module.\n")

            # Member 3's function will be connected here.

        elif choice == 3:
            print("\n🌍 Opening Environmental Impact...")
            print("Please wait for the environmental impact module.\n")

            # Member 4's function will be connected here.

        elif choice == 4:
            print("\n📖 Opening Waste History...")
            print("Please wait for the history module.\n")

            # Member 5's function will be connected here.

        elif choice == 5:
            print("\n🔎 Opening History Search...")
            print("Please wait for the search module.\n")

            # Member 5's function will be connected here.

        elif choice == 6:
            print("\n💡 Opening Recommendations...")
            print("Please wait for the recommendations module.\n")

            # Member 5's function will be connected here.

        elif choice == 7:
            # Save data before exiting
            save_data(waste_log)

            print("\n")
            print("╔══════════════════════════════════════════════════╗")
            print("║                                                  ║")
            print("║              🌱 GOODBYE! 🌱                     ║")
            print("║                                                  ║")
            print("║     Thank you for making sustainable choices!   ║")
            print("║                                                  ║")
            print("║        ♻️  Every small action counts! 💚        ║")
            print("║                                                  ║")
            print("╚══════════════════════════════════════════════════╝")
            print()

            break


# Start the application
if __name__ == "__main__":
    main()
