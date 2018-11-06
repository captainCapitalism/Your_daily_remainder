def import_file(day):
    day_string = day + ".txt"
    with open("TextFiles/" + day_string, "r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()
    return lines
