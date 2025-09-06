import random

CROP_FAMILIES = {
    "legumes": ["Beans", "Peas", "Lentils"],
    "brassicas": ["Broccoli", "Cabbage", "Kale"],
    "nightshades": ["Tomatoes", "Potatoes", "Peppers"],
    "alliums": ["Onions", "Garlic", "Leeks"],
    "cucurbits": ["Cucumbers", "Zucchini", "Pumpkins", "Melons"],
    "grains": ["Wheat", "Corn", "Barley", "Oats"],
    "root_vegetables": ["Carrots", "Beets", "Radishes", "Turnips"],
    "leafy_greens": ["Lettuce", "Spinach", "Chard"]
}

def find_family(crop):
    """Find the family a crop belongs to."""
    for family, crops in CROP_FAMILIES.items():
        if crop in crops:
            return family
    return None

def suggest_rotation(previous_crop):
    """
    Suggests a crop family to plant after the previous crop.
    Rule: Avoid planting the same family twice.
    """
    prev_family = find_family(previous_crop)
    other_families = [f for f in CROP_FAMILIES if f != prev_family]

    chosen_family = random.choice(other_families)
    chosen_crop = random.choice(CROP_FAMILIES[chosen_family])

    print(f"After {previous_crop}, avoid planting the same family ({prev_family}).")
    print(f"Instead, try a {chosen_family} crop, e.g., {chosen_crop}.")

if __name__ == "__main__":
    suggest_rotation("Tomatoes")