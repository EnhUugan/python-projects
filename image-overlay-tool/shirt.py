from PIL import Image, ImageOps
import sys

def check_inp(input):
    if len(input) == 2:
        a = sys.argv[1].lower()
        b = sys.argv[2].lower()
        ends = (".jpg", ".jpeg", ".png")
        if a.endswith(ends) and b.endswith(ends):
            a = a.split(".")
            b = b.split(".")
            if a[-1] == b[-1]:
                return True
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")
    elif len(input) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if check_inp(sys.argv[1:]):
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(f"{sys.argv[1]}")
        fitted = ImageOps.fit(photo, shirt.size)
        fitted.paste(shirt, shirt)
        fitted.save(f"{sys.argv[2]}")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
