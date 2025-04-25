def sameChars(s1, s2):
    def char_in_string(s, c):
        for chr in s:
            if chr == c:
                return True
        return False

    def all_chars_match(s1, s2):
        for chr in s1:
            if not char_in_string(s2, chr):
                return False
        for chr in s2:
            if not char_in_string(s1, chr):
                return False
        return True

    return all_chars_match(s1, s2)

print(sameChars(input(),input()))


