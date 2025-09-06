# A simple crop rotation planner
# This is a starting point for the community to build upon.

CROP_FAMILIES = {
    "legumes": ["Beans", "Peas", "Lentils"],
    "brassicas": ["Broccoli", "Cabbage", "Kale"],
    "nightshades": ["Tomatoes", "Potatoes", "Peppers"],
    "alliums": ["Onions", "Garlic", "Leeks"]
}

def suggest_rotation(previous_crop):
    """
    Suggests a crop family to plant after the previous crop.
    A very simple rule: Don't plant the same family twice.
    """
    print(f"After {previous_crop}, consider planting a crop from a different family.")
    print("For example, after a nightshade like tomatoes, plant a legume like beans to fix nitrogen.")

if __name__ == "__main__":
    suggest_rotation("Tomatoes")
