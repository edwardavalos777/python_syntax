def print_upper_words(words, must_start_with=None):
    """
    Given a list of words, print each word on a separate line in all uppercase,
    but only if the word starts with one of the letters in the `must_start_with`
    set (if provided).

    Args:
    - words (list): a list of strings
    - must_start_with (set): a set of letters that the word must start with

    Returns:
    - None
    """
    for word in words:
        if must_start_with is None or word.startswith(tuple(must_start_with)):
            print(word.upper())
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

