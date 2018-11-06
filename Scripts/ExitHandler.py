def exit_handler(day, done, tasks):
    with open('TextFiles/DoneTasks.txt', "w", encoding="utf-8") as f:
        f.write(str(day) + "\n")

        for x in range(len(tasks)):
            f.write(str(done[x].get())+"\n")

    f.close()
