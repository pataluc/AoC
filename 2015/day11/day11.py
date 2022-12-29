def valid_password(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    if not any(map(lambda t: ord(t[0]) + 1 == ord(t[1]) and ord(t[1]) +1 == ord(t[2]), [ password[i:i+3] for i in range(len(password)-2)])):
        return False
    if len(set([ password[i:i+2] for i in range(len(password)-1) if password[i] == password[i+1] ])) < 2:
        return False
    return True

assert not valid_password("hijklmmn")
assert not valid_password("abbceffg")
assert not valid_password("abbcegjk")
assert valid_password("abcdffaa")
assert valid_password("ghjaabcc")

def inc_password(password):
    i = len(password) - 1
    while True:
        password = password[:i] + chr((((ord(password[i]) + 1) - ord('a')) % 26) + ord('a')) + password[i + 1:] if i < len(password) else ''
        if password[i] != 'a':
            break
        else:
            i -= 1
    return password

def get_next_password(password):
    while True:
        password = inc_password(password)
        if valid_password(password):
            return password

password = "cqjxjnds"
password = get_next_password(password)

print("ex1 : %s" % password)
print("ex2 : %s" % get_next_password(password))