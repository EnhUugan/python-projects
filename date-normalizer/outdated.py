def main():
    date()

def month_conv(month):

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if month.isalpha():
        if month in month_list:
            num = 1
            for i, lmonth in enumerate(month_list):
                if lmonth == month:
                    num += i
            if num < 10:
                return f"0{num}"
            else:
                return num
        else:
            raise KeyError

    elif month.isdigit():
        month = int(month)
        if 0 < month < 13:
            if month < 10:
                return f"0{month}"
            else:
                return month
        else:
            raise KeyError
    else:
        raise ValueError


def date():

    while True:

        user = input("Date: ")
        user = user.strip()

        try:
            if "/" in user:
                user = user.split("/")
                year = int(user[2])
                if user[0].isdigit():
                    month = user[0]
                else:
                    raise ValueError
                day = int(user[1])
                if day < 1 or 31 < day:
                    raise ValueError
                if day < 10:
                    day = f"0{day}"

                print(f"{year}-{month_conv(month)}-{day}")
                break
            elif "," in user:
                user = user.split(",")
                m_d = user[0]
                year = user[1].strip()
                month, day = m_d.split(" ")
                month = str(month).strip()
                day = int(day)
                if day < 1 or 31 < day:
                    raise ValueError
                if day < 10:
                    day = f"0{day}"

                print(f"{year}-{month_conv(month)}-{day}")
                break
            else:
                continue
        except ValueError:
            pass
        except KeyError:
            pass
main()
