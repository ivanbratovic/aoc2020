import re

def passports_from_file(filepath : str):
    """
    Reads input and returns a list of all passports
    represented as python dictionaries.
    """
    passports = []
    with open(filepath, "r") as file:
        d = {}
        lines = file.readlines()
        for line in lines:
            if line.strip() == "":
                passports.append(d)
                d = {}
                continue
            for keyval in line.strip().split():
                k, v = tuple(keyval.split(":"))
                d[k] = v
        passports.append(d)
    print("Read {} passports.".format(len(passports)))
    return passports

def str_num_between(num : str, low : int, high : int):
    """
    Checks if a given number is between the values
    low and high. Boundaries are included.
    """
    val = int(num)
    if val < low or val > high:
        return False
    return True

def valid(key : str, passport : dict):
    """
    Checks for the validity of the key inside a dict.

    Also is a mess.
    """
    val = passport[key]
    if key == "byr": # Birth year
        if not str_num_between(val, 1920, 2002):
            return False
    if key == "iyr": # Issue year
        if not str_num_between(val, 2010, 2020):
            return False
    if key == "eyr": # Expiration year
        if not str_num_between(val, 2020, 2030):
            return False
    if key == "hgt": # Height
        number, unit = val[:-2], val[-2:]
        if unit != "in" and unit != "cm":
            return False
        if unit == "in":
            if not str_num_between(number, 59, 76):
                return False
        elif unit == "cm":
            if not str_num_between(number, 150, 193):
                return False
    if key == "hcl": # Hair colour
        if not re.match(r"#[0-9a-f]{6}", val):
            return False
    if key == "ecl": # Eye colour
        if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
    if key == "pid": # Passport ID
        if len(val) != 9:
            return False
    if key == "cid": # Country ID
        return True
    # print("valid")
    return True

def main():
    """
    Main function. Contains primary logic.
    """
    passports =  passports_from_file("input.txt")
    count = len(passports)
    invalid = 0
    for i, passport in enumerate(passports):
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]:
            if (key == "cid"):
                continue # Ignore the cid key
            if key not in passport.keys() or not valid(key, passport):
                invalid += 1
                break
    print("  Valid: ",count-invalid,"\nInvalid: ",count, sep="")

main()
