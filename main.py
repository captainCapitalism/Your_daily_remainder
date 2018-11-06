#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
import atexit
from Scripts.WhatDayOfTheWeekIsIt import what_day_of_the_week_is_it
from Scripts.ImportFile import import_file
from Scripts.ExitHandler import exit_handler
from Scripts.CheckIfToday import check_if_today
from Scripts.CheckWhatIsDone import check_what_is_done
from Scripts.SetupUI import setup_root
from Scripts.SetupUI import setup_frame
from Scripts.GetMotivator import get_motivator
from Scripts.RewardHandler import check_if_reward_is_deserved

root = setup_root()
window_frame = setup_frame(master=root)
today_day_number = datetime.datetime.today().weekday()
today_is = what_day_of_the_week_is_it(today_day_number)
file_is_from_today = check_if_today(today_day_number)
task_list = import_file(today_is[0])
tasks_done = []
task_label_list = []
task_checkbox_list = []

if file_is_from_today:
    tasks_done = check_what_is_done(tasks_done)
else:
    for x in range(task_list.__len__()):
        tasks_done.append(tk.BooleanVar())
        tasks_done[x].set(False)

welcome_message = tk.Label(master=window_frame,
                           text="Dzisiaj jest "
                                + today_is[1]
                                + ". Twoje zadania na dziś:").grid(row=0,
                                                                   column=0,
                                                                   columnspan=3,
                                                                   pady = 10)
for x in range(task_list.__len__()):
    task_label_list.append(
        tk.Label(master=window_frame,
                 text=task_list[x]))
    task_label_list[x].grid(row=x + 1,
                            column=1,
                            sticky="news")
    task_checkbox_list.append(
        tk.Checkbutton(master=window_frame,
                       variable=tasks_done[x],
                       command=lambda: check_if_reward_is_deserved(tasks_done,root)))
    task_checkbox_list[x].grid(row=x + 1,
                               column=2,
                               sticky="news")

motivating_message = tk.Message(window_frame,
                                text=get_motivator(),
                                width = 350,
                                anchor = 'center')
motivating_message.grid(row=1 + task_checkbox_list[-1].grid_info()["row"],
                        column=0,
                        columnspan=3)
atexit.register(exit_handler, today_day_number, tasks_done, task_list)
root.mainloop()
