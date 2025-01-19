def charCount(t):
    """
    Retrieves data from a text file and returns a dictionary where the keys are unique characters
    (excluding whitespace) and the values are the counts of occurrences of each character.

    :param t: Path to the text file
    :return: Dictionary with characters as keys and their counts as values
    """
    char_dict = {}

    try:
        with open(t, 'r') as file:
            for line in file:
                for char in line.strip():
                    # Skip whitespace characters
                    if char.isspace():
                        continue

                    # Increment the count for the character in the dictionary
                    if char in char_dict:
                        char_dict[char] += 1
                    else:
                        char_dict[char] = 1
    except FileNotFoundError:
        print(f"Error: The file '{t}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return char_dict

# Example usage:
# Create a text file 'example.txt' with some content to test this function.
# print(charCount('example.txt'))

