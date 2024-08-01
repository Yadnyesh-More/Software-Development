def check_word_in_text(word, text):
    # Convert both text and word to lowercase
    text_lower = text.lower()
    word_lower = word.lower()
    # Check if the word is a substring of the text
    return word_lower in text_lower

address = "Ramabai Ambedkar Marg, Opposite Haj House, Green Stone Heritage Office No2, 3rd Floor, C Wing, MRA Marg, Fort, Mumbai South , Mumbai"

# Example usage
word_to_check = "Ramabai Ambedkar Marg, Opposite Ha"
is_present = check_word_in_text(word_to_check, address)
print(is_present)  # Output: True

word_to_check = "Delhi"
is_present = check_word_in_text(word_to_check, address)
print(is_present)  # Output: False
