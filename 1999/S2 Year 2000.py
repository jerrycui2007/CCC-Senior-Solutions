import re

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Regex
patterns = [
    (r'\b(\d{2})/(\d{2})/(\d{2})\b', 'dmY'),  # dd/mm/yy
    (r'\b(\d{2})\.(\d{2})\.(\d{2})\b', 'Ymd'),  # yy.mm.dd
    (rf'\b({"|".join(months)}) (\d{{2}}), (\d{{2}})\b', 'Month_d_Y')  # Month dd, yy
]


def replace_year(match, format_type):
    if format_type == 'dmY':
        day, month, year = match.groups()
    elif format_type == 'Ymd':
        year, month, day = match.groups()
    elif format_type == 'Month_d_Y':
        month_name, day, year = match.groups()
        month = None  # Not needed for validation in this case

    # Convert to integer for validation
    day, year = int(day), int(year)
    month = int(month) if month else None

    if not (1 <= day <= 31):
        return match.group(0)
    if month and not (1 <= month <= 12):
        return match.group(0)

    new_year = 2000 + year if year <= 24 else 1900 + year

    if format_type == 'dmY':
        return f"{day:02}/{month:02}/{new_year}"
    elif format_type == 'Ymd':
        return f"{new_year}.{month:02}.{day:02}"
    elif format_type == 'Month_d_Y':
        return f"{month_name} {day:02}, {new_year}"


lines = int(input())
for _ in range(lines):
    line = input()

    for pattern, format_type in patterns:
        line = re.sub(pattern, lambda match: replace_year(match, format_type), line)

    print(line)

"""
4
Before 02/03/04, but not after December 19, 99,
there was a rehash of the 55.34.02 meeting. A date, like November 15,
95 cannot traverse two lines, nor can it be surrounded by alphabetics
or numerics like this: 78November 01, 88, or 6801/12/03, or 02/03/04x.
"""