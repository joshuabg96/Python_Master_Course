# Create a program that follows the following isntructions
# Create a Set called users with the users Marta, David, Elvira, Juan and Marcos
# Create a Set called admin with the Administrators Juan and Marta
# Delete the Administrator Juan from admin arran
# Add Marcos as new administrator but do not delete it from users
# Show all the users dinamically and show if it is admin or not

# A set can not have a value dupplicated.
users = {"Marta", "David", "Elvira", "Juan", "Marcos"}
admin = {"Juan", "Marta"}

admin.discard("Juan")
admin.add("Marcos")

for member in users:
    if member in admin:
        print(member, " is Administrator")
    else:
        print(member, " Is not Administrator")