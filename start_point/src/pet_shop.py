def get_pet_shop_name(petshop):
    return petshop["name"]


def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]


def add_or_remove_cash(petshop, num):
    petshop["admin"]["total_cash"] += num


def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]


def increase_pets_sold(petshop, num):
    petshop["admin"]["pets_sold"] += num


def get_stock_count(petshop):
    return (len(petshop["pets"]))


def get_pets_by_breed(petshop, breed_type):
    found_breeds = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed_type:
            found_breeds.append(breed_type)
    return found_breeds
