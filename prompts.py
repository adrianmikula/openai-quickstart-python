


def generate_rooms(animal):
    return """Suggest a room name for an animal that is a superhero.

Animal: Cat
Names: Sharpclaw Suite, Fluffball Room, Queen Feline
Animal: Dog
Names: Hound Hut, Canine Cabin, Dog Den
Animal: {}
Names:""".format(
        animal.capitalize()
    )


def generate_amenities(animal):
    return """Suggest amenities for an animal that is a superhero.

Animal: Cat
Amenities: Climbing Tree, Litter Box, Scratch Post, Catnip, Cat Bed, Cat Toys
Animal: Dog
Amenities: Dog Kennel, Dog Bed, Dog Toys, Dog Leash, Dog Collar
Animal: {}
Amenities:""".format(
        animal.capitalize()
    )


def generate_prices(days):
    return """Suggest hotel room prices when staying for a certain number of days.

Days: 1
Prices: 90, 110, 150
Days: 7
Prices: 80, 100, 140
Days: {}
Prices:""".format(
        days.capitalize()
    )