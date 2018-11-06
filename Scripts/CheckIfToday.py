from os import remove

def check_if_today(today):
    try:
        with open('TextFiles/DoneTasks.txt', "r", encoding="utf-8") as f:
            day = f.readline()
            if int(today) == int(day[0]):
                return True
                f.close()
            else:
                print('T\'was yesterday')
                f.close()
                remove("TextFiles/DoneTasks.txt")
                with open('TextFiles/DoneTasks.txt', "w", encoding="utf-8") as g:
                    g.write(today + "\n")
                g.close()
                return False
    except:
        print('No FILE')
        return False
