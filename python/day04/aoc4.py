import numpy as np  

with open("/Users/christopherauld/Desktop/AOC2018/data/day4/input.txt", "r") as file:
    s = [line.strip("\n") for line in file]

s = [[t.split("]")[0].replace("[", ""), t.split("]")[1].replace(" ", "", 1)] for t in s]

class GuardData:
    def __init__(self, number):
        self.number = number
        self.days = []
        self.minutes = []
        self.events = []
        self.total_sleep = 0

    def update_total_sleep(self):
        self.total_sleep += self.minutes[-1] - self.minutes[-2]


def get_event_type(d):
    return True if "falls" in d else False


def get_day_and_minute(d):
    return np.array( [ int(d[0][8:10]), (int(d[1][0:2]) * 60) + int(d[1][3:5]) ] ) 


guards = {}
previous_state = None

for e in s:
    # change guards if it's a new one
    if "Guard" in e[1]:
        guard_num = int(e[1].split(" ")[1].replace("#", ""))
        if guard_num in guards:
            current = guard 
        elif guard_num not in guards:
            guards[guard_num] = Guard(number = guard_num)
            current = guard_num
    else:
        time = get_day_and_minute(e[0])
        guards[current].days.append(time[0])
        guards[current].minutes.append(time[1])
        sleep_state = get_event_type(e[1])
        guards[current].events.append(sleep_state)
        if not sleep_state and guards[current].events[-2] :
