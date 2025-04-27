# Create a function called add_ones that recive a list and an element. the function
# shall add the element at the end of the list with the condition of no repeat any element
# if the element is in the list we have to call the error ValueError that have to be
# catched and show the message "Error: Imposible to add duplicated element => [element]"

element = [1,5,-2]
def add_ones(list, value):
    try:
        if value in list:
            raise ValueError
        else:
            list.append(value)
    except ValueError:
        print("Error: Imposible to add duplicated element => {}".format(value))

add_ones(element, 10)
print(element)
add_ones(element, -2)
print(element)
add_ones(element, 0)
print(element)