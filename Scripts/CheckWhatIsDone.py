from tkinter import BooleanVar


def check_what_is_done(done):
    f = open('TextFiles/DoneTasks.txt', 'r')
    lines = f.read().split("\n")
    lines = lines[1:-1]

    for x in range(len(lines)):
        done.append(BooleanVar())

        if lines[x] == 'True':
            done[x].set(True)
        else:
            done[x].set(False)
    return done
