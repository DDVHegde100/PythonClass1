import random

friend_groups_valid = 1

while friend_groups_valid == 1:
    friend_groups = input("Do you want friend groups to be accounted for(Yes or No)? ")
    friend_groups = friend_groups.lower()
    friend_groups = friend_groups.strip( )
    if friend_groups == "yes" or friend_groups == "no":
        friend_groups_valid = 0
        do_friend_groups = True
    else:
        print("Invalid Choice \n")
    
def normal_pick():
    people = input("List the people who will be choosing books: ")
    books = input("List the books: ")
    people = people.strip( )
    books = books.strip( )
    people_list = people.split(",")
    book_list = books.split(",")
    


def friend_groups_pick():
 