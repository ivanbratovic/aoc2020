import re

def passports_from_file(filepath : str):
    """
    Reads input and returns a list of all passports
    represented as python dictionaries.
    """
    passports = []
    with open(filepath, "r") as file:
        d = {}
        for line in file.readlines():
            line = line.strip()
            if line == "":
                passports.append(d)
                d = {}
                continue
            for keyval in line.split():
                k, v = tuple(keyval.split(":"))
                d[k] = v
        passports.append(d)
    #print(f"Read {len(passports)} passports.")
    return passports

def str_num_between(num : str, low : int, high : int):
    return int(num) in range(low, high+1)

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

def main(file: str):
    """
    Main function. Contains primary logic.
    """
    passports =  passports_from_file(file)
    count = len(passports)
    invalid = 0
    invalid_part1 = 0
    for i, passport in enumerate(passports):
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in passport:
                invalid_part1 += 1
                break
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in passport or not valid(key, passport):
                invalid += 1
                break
    print("Part 1:", count-invalid_part1)
    print("Part 2:", count-invalid)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

