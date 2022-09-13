
def index_finder(letter):
    index = int(ord(letter)) - 96
    return index

def numeric_position(index):
    if index == 1:
        position = str(index) + "st"
    elif index == 2:
        position = str(index) + "nd"
    elif index == 3:
        position = str(index) + "rd"
    else:
        position = str(index) + "th"
    return position

letter = input("Enter a letter: ")
print(f"\nthe numeric position of the letter {letter} is {numeric_position(index_finder(letter))}")
