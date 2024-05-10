def solve(s: str):
    arr = s.split(" ")
    corrected_arr = []

    for word in arr:
        # Capitalize the first character of each word
        corrected_word = word.capitalize()

        # Preserve any non-alphabetic characters at the start of the word
        for i in range(len(word)):
            if not word[i].isalpha():
                corrected_word = corrected_word[:i] + word[i] + corrected_word[i+1:]
            else:
                break

        corrected_arr.append(corrected_word)

    corrected_s = " ".join(corrected_arr)
    return corrected_s
