'''Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.'''

phone_book = {"0568323222":"Amal", "0522222232":"Mohammed", "0532335983":"Khadijah", "0545341144":"Abdullah",
 "0545534556":"Rawan", "0560664566":"Faisal", "0567917077":"Layla"}

phone_number = input("Enter the number: ")
if phone_number.isnumeric():
    if len(phone_number) == 10:
        print(phone_book.get(phone_number, "Sorry, the number is not found\n"))
    else:
        print("\nThis is invalid number\n")     
else:
    print("\nThis is invalid number\n")
        

    
'''Q2:Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.'''

def sorting(numbers_list :list):
    new_numbers_list = []
    for number in numbers_list:
        if number == 0:
            new_numbers_list.append(0)
        else:
            new_numbers_list.insert(0, number)
    return new_numbers_list

unsorted_list = [5, 0, 34, 9, 0, 13, 8]
print(f"The list after arrangment: {sorting(unsorted_list)}\n")