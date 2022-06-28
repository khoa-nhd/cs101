def check_valid_parentheses(text):
    valid_opening = {')': '(', ']': '[', '}': '{'}
    lastOpen = []
    for c in text:
        if c == "(" or c == "[" or c == "{":
            lastOpen.append(c)
        elif c == ")" or c == "]" or c == "}":
            if len(lastOpen) == 0:
                return False
            opening = lastOpen.pop()
            if opening != valid_opening[c]:
                return False
    if len(lastOpen) == 0 :
        return True
    else:
        return False
    
text = '{{}}({})'
ketQua = check_valid_parentheses(text)
print(ketQua)