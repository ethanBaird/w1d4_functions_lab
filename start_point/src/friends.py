def get_name(person):
    person_name = person["name"]
    return person_name

def get_favourite_tv_show(person):
    person_tv_show = person["favourites"]["tv_show"]
    return person_tv_show

def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    person_likes_to_eat = False
    for snack in snacks:
        if snack == food:
            person_likes_to_eat = True
    return person_likes_to_eat
 
    # return food in snacks

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends"].remove(old_friend)

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]
    return total
    
def lend_money(lender, borrower, amount):
    borrower["monies"] += amount
    lender["monies"] -= amount

def all_favourite_foods(people):
    list_all_favourite_foods = []
    for person in people:
        persons_favourite_foods = person["favourites"]["snacks"]
        for food in persons_favourite_foods:
            list_all_favourite_foods.append(food)
    return list_all_favourite_foods
        
def find_no_friends(people):
    people_with_no_friends = []
    for person in people:
        if person["friends"] == []:
            people_with_no_friends.append(person)
    return people_with_no_friends

def unique_favourite_tv_shows(people):
    list_favourite_tv_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in list_favourite_tv_shows:
            list_favourite_tv_shows.append(person["favourites"]["tv_show"])
    return list_favourite_tv_shows