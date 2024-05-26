# try:
#     file = open("100 Days code/Day 30 Exception Error/a_file.txt")
#     # a_dictionary = {"key": "value"}
#     # print(a_dictionary["qwert"])
# except FileNotFoundError:
#     file = open("100 Days code/Day 30 Exception Error/a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was Closed!")
#     raise TypeError("This is a Test Error Message!")


# Raising errors
height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
    
bmi = weight / height ** 2
print(bmi)