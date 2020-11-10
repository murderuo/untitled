def is_isogram(string):
    if "" in string or string.isalpha():
        if len(list(string.lower()))==len(list(set(string.lower()))): return True
        else: return False
    else:return False

print(is_isogram("Dermatoglyphics"),)
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))