#!/usr/bin/python3
"""Function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """Checks if text is a string and prints its content
    skipping the spaces after ".", "?", ":"."""
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        result = ""
        i = 0
        while i < len(text):
            if text[i] in (".", "?", ":"):
                result += text[i]
                if i < len(text) - 1 and text[i+1] == " ":
                    i += 1
                result += "\n\n"
            else:
                result += text[i]
            i += 1
        print(result)
