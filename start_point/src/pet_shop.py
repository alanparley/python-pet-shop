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


# def get_pets_by_breed(pet_shop, breed_type):
#     found_breeds = []
#     for breed_type in pet_shop:
#         if breed_type["pets"]["British Shorthair"] == True:
#             found_breeds.append(breed_type)
#     print(len(found_breeds))

    # def get_pets_by_breed(pet_shop, breed_type):
    #     found_breeds = []
    #     for breed_type in pet_shop:
    #         if breed_type["pets"]["breed"] == "British Shorthair":
    #             found_breeds.append(breed_type)
    #     print(len(found_breeds))

def get_pets_by_breed(pet_shop, breed_type):
    found_breeds = []
    for breed_type in pet_shop["pets"]["breed"]:
        if breed_type == "British Shorthair":
            found_breeds.append(int(breed_type))
    return found_breeds
