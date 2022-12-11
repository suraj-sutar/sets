# sets do not contains duplicates values it will print duplicate value one time 
# if you want to add some data in the set you can add using add()
# you can add any data in set it can store the any of the positon in the set

# list is dinoted as as "[]"
# tuple is dinated as a "()"
# sets is dinoted as a "{}"




# first_set = {"suraj","kashinath","chetan"}

# first_set.add("prayag")
# print(first_set)

# art_friends = {"prathmeshg","gaurav","mangesh"}

# science_friends = {"prathmeshg","sanket","chetan"}

# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science)

# in above example some friends are in arts but it does not contain in science that is the meaning of difference keyword

# art_friends = {"prathmeshg","gaurav","mangesh"}

# science_friends = {"prathmeshg","sanket","chetan"}

# not_in_both = art_friends.symmetric_difference(science_friends)
# print(not_in_both)
# in above example you can find how donot do both using symmetric_difference


# than you can find how can do both using intersecton
# art_friends = {"prathmeshg","gaurav","mangesh"}

# science_friends = {"prathmeshg","sanket","chetan"}

# arts_and_science = art_friends.intersection(science_friends)
# print(arts_and_science)
# print(type(arts_and_science))


nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()

name = input("enter name: ")

new_set = set()
new_set.add(name)

print(new_set)

intersectionss = new_set.intersection(nearby_people)
print(intersectionss)







# user_friends_name = input("Enter user name: ")
# user_friends.add(user_friends_name)

# nearby_and_user_frineds = user_friends.intersection(nearby_people)
# print(nearby_and_user_frineds)
