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

