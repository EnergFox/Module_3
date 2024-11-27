calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(st):
    string = len(st), st.upper(), st.lower()
    tuple(string)
    count_calls()
    return string
def is_contains(a, b):
    a = a.upper()
    count_calls()
    b = [x.upper() for x in b]
    if a in b:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'UrbAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)