import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^((?:(?:[1][0-2])|[0-9])(?:\:[0-5][0-9])? (?:AM|PM)) to ((?:(?:[1][0-2])|[0-9])(?:\:[0-5][0-9])? (?:AM|PM))$", s)
    if match:

        if match.group(1).find("AM") != -1:
            start = match.group(1).strip("AM").strip()
            if len(start) <= 2:
                if int(start) == 12:
                    start = "00:00"
                else:
                    start = f"{int(start):02}:00"
            elif len(start) > 2:
                hr, min = start.split(":")
                if int(hr) == 12:
                    hr = "00"
                else:
                    hr = f"{int(hr):02}"
                start = f"{hr}:{min}"

        elif match.group(1).find("PM") != -1:
            start = match.group(1).strip("PM").strip()
            if len(start) <= 2:
                if int(start) == 12:
                    start = "12:00"
                else:
                    start = f"{int(start) + 12}:00"
            elif len(start) > 2:
                hr, min = start.split(":")
                if int(hr) == 12:
                    hr = 12
                else:
                    hr = int(hr) + 12
                start = f"{hr}:{min}"

        if match.group(2).find("AM") != -1:
            end = match.group(2).strip("AM").strip()
            if len(end) <= 2:
                if int(end) == 12:
                    end = "00:00"
                else:
                    end = f"{int(end):02}:00"
            elif len(end) > 2:
                hr, min = end.split(":")
                if int(hr) == 12:
                    hr = "00"
                else:
                    hr = f"{int(hr):02}"
                end = f"{hr}:{min}"

        elif match.group(2).find("PM") != -1:
            end = match.group(2).strip("PM").strip()
            if len(end) <= 2:
                if int(end) == 12:
                    end = "12:00"
                else:
                    end = f"{int(end) + 12}:00"
            elif len(end) > 2:
                hr, min = end.split(":")
                if int(hr) == 12:
                    hr = 12
                else:
                    hr = int(hr) + 12
                end = f"{hr}:{min}"

        return f"{start} to {end}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
