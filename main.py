import pyperclip
import pyautogui
import time

begrepp_lista = []
forklaring_lista = []

# Specify the path to your text file
file_path = "load_begrepp_forklaring.txt"

# Open and read the file
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

# Check if there's an even number of lines (begrepp and forklaring)
if len(lines) % 2 == 0:
    for i in range(0, len(lines), 2):
        begrepp = lines[i].strip()
        forklaring = lines[i + 1].strip()

        # Cut forklaring at 60 characters
        forklaring = forklaring[:60]

        # Check if both begrepp and forklaring are not empty before appending
        if begrepp and forklaring:
            begrepp_lista.append(begrepp)
            forklaring_lista.append(forklaring)
else:
    print("Uneven number of lines in the input file. Each begrepp should have a forklaring.")

print(begrepp_lista)
print(forklaring_lista)
print("  ")
print("  ")
print("  ")

card_positions = {
        0: (360, 300),  # Coordinates for card 0
        1: (760, 300),  # Coordinates for card 1
        2: (1160, 300),# Add coordinates for all cards
        3: (1560, 300),
        4: (360, 600),
        5: (760, 600),
        6: (1160, 600),
        7: (1560, 600),
        8: (360, 900),
        9: (760, 900),
        10: (1160, 900),
        11: (1560, 900),
    }

def find_input(text_input):
    lines_to_skip = 8
    text_lines = text_input.split('\n')[lines_to_skip:]

    # Join the remaining lines to form the options text
    options_text = '\n'.join(text_lines)

    # Split the text into lines and cut off any explanation that is longer than 15 characters
    options_lines = [line.strip() for line in options_text.split('\n') if line.strip()]
    options_lista = [line[:60] for line in options_lines]

    print("options_lista =", options_lista)
    return options_lista


def hitta_kort_index(kort_texter, kort_lista, kort_forklaring_lista):
    kort_index_lista = []
    for kort_text in kort_texter:
        # Använd hela korttexten (inte bara hälften) för att matcha exakt
        index_i_kort = kort_lista.index(kort_text) if kort_text in kort_lista else -1
        index_i_forklaring = kort_forklaring_lista.index(kort_text) if kort_text in kort_forklaring_lista else -1
        
        # Only include indexes where a match is found
        kort_indexes = [index_i_kort, index_i_forklaring]
        kort_indexes = [index for index in kort_indexes if index != -1]
        
        kort_index_lista.extend(kort_indexes)  # Extend the list to add duplicates
    print(kort_index_lista)
    return kort_index_lista




def click_card(index):
        if index in card_positions:
            x, y = card_positions[index]
            pyautogui.click(x, y)


def setup_click(kort_indexs):
    # List of card indexes
    card_indexes = kort_indexs

    matching_indexes = []

    for index, card_index in enumerate(card_indexes):
        # Find the matching card with the same index
        matching_index = None
        for other_index, other_card_index in enumerate(card_indexes):
            if other_index != index and other_card_index == card_index:
                matching_index = other_index
                break

        if matching_index is not None and matching_index > index:
            matching_indexes.append((index, matching_index))

    print(matching_indexes)
    # Function to click a card at the specified index
    

    # Click the matching pairs of cards
    for pair in matching_indexes:
        click_card(pair[0])
           # Click the first card in the pair
        #time.sleep(0.1)  # Adjust the delay as needed between clicks
        click_card(pair[1])
        
        click_card(pair[0])
        click_card(pair[1])   # Click the second card in the pair
        #time.sleep(0.1)  # Adjust the delay as needed between clicks



# Main loop to run in the background
current_clipboard = pyperclip.paste()
last_clipboard = current_clipboard
while True:
    # Check clipboard every second
    current_clipboard = pyperclip.paste()
    time.sleep(0.05)
    if current_clipboard != last_clipboard:
        setup_click(hitta_kort_index(find_input(current_clipboard), begrepp_lista, forklaring_lista))
        break

    last_clipboard = current_clipboard

