"""Description:
Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

Examples
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance" """

def balance(left, right):
    if (right=="" and left==""):return "Balance"

    elif (left=="" or left.count("!")*2 + left.count("?")*3 < right.count("!")*2 + right.count("?")*3):return "Right"
    elif right=="" or left.count("!")*2 + left.count("?")*3 > right.count("!")*2 + right.count("?")*3:return "Left"
    elif left.count("!")*2 + left.count("?")*3 == right.count("!")*2 + right.count("?")*3:return "Balance"
    else: return "Balance"

    # lc=left.count("!")*2 + left.count("?")*3
    # rc=right.count("!")*2 + right.count("?")*3
    #
    # return "Elft" if lc>rc else  "Right"