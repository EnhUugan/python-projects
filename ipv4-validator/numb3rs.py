import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        c = 0
        for i in range(1, 5):
            if int(matches.group(i)) > 255:
                return False
            if matches.group(i).startswith("0") and len(matches.group(i)) > 1:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
