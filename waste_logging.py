"""
EcoTrack — Waste Logging Module
Handles collecting a new waste entry from the user, validating it,
and appending it to the shared waste_log list.
"""

from datetime import date

# The categories the app accepts. "landfill" means it was NOT recycled.
VALID_CATEGORIES = ["plastic", "paper", "glass", "metal", "organic", "landfill"]


def log_waste_entry(waste_log):
    """
    Prompts the user for a waste category and weight, validates both,
    and appends a new entry (as a dictionary) to waste_log.

    Parameters:
        waste_log (list): the shared list of waste entry dictionaries

    Returns:
        None — modifies waste_log in place
    """

    print("\n♻️  --- Log a Waste Entry ---")
    print("Valid categories:", ", ".join(VALID_CATEGORIES))

    category = get_valid_category()
    weight_kg = get_valid_weight()

    # Only "landfill" counts as NOT recycled — every other category does
    recycled = category != "landfill"

    new_entry = {
        "date": str(date.today()),
        "category": category,
        "weight_kg": weight_kg,
        "recycled": recycled
    }

    waste_log.append(new_entry)

    print(f"\n✅ Entry saved: {weight_kg} kg of {category} logged on {new_entry['date']}.\n")


def get_valid_category():
    """
    Repeatedly asks the user for a category until a valid one is entered.
    Returns the category as a lowercase string.
    """

    while True:
        category = input("Enter waste category: ").strip().lower()

        if category in VALID_CATEGORIES:
            return category

        print(f"\n⚠️  Invalid category. Please choose from: {', '.join(VALID_CATEGORIES)}\n")


def get_valid_weight():
    """
    Repeatedly asks the user for a weight until a valid positive number is entered.
    Returns the weight as a float.
    """

    while True:
        weight_input = input("Enter weight in kg: ").strip()

        try:
            weight = float(weight_input)

            if weight <= 0:
                print("\n⚠️  Weight must be greater than 0. Please try again.\n")
                continue

            return weight

        except ValueError:
            print("\n⚠️  Invalid input. Please enter a numeric value (e.g., 2.5).\n")


