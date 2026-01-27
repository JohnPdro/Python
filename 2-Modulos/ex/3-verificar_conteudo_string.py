import re

def check_character(string) :
    rule = re.compile(r'[^a-zA-Z0-9]')
    checked_string = rule.search(string)
    return not bool(checked_string)

print(check_character("ADSSDSFDSgsfkjaajdhf2224123412"))
print(check_character("#@^`:.,.#$%@%"))