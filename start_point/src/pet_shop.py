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


def find_pet_by_name(petshop, pet_name):
    for name in petshop["pets"]:
        if name["name"] == pet_name:
            return name


def remove_pet_by_name(petshop, petname):
    for pet in petshop["pets"]:
        if pet["name"] == petname:
            petshop["pets"].remove(pet)


# def add_pet_to_stock(petshop, add_stock):
#     petshop["pets"] += add_stock

def add_pet_to_stock(petshop, add_stock):
    petshop["pets"].append(add_stock)

# # add a task to the list
# def add_to_list(list, task):
#     list.append(task)


# def test_add_or_remove_cash__add(self):
#         add_or_remove_cash(self.cc_pet_shop, 10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)

# def add_or_remove_cash(petshop, num):
#     petshop["admin"]["total_cash"] += num
