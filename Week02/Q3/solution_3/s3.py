def charCount(t):

    char_dictionary = {}

    try:
        with open(t, 'r') as file:
            for line in file:
                for char in line:
                    # Skipping th whitespace characters
                    if char.isspace():
                        continue
                    char_dictionary[char] = char_dictionary.get(char, 0) + 1
    except FileNotFoundError:
        print(f"Error: The file {t} was not found!")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    return char_dictionary


print(charCount('note.txt'))        