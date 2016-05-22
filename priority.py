import sys
from collections import defaultdict
from random import choice



def load_priorities():
    tasks = defaultdict(dict)
    with open('input.txt') as f:
        for l in f.readlines():
            if l[0] == '#':
                continue
            topic, name, time = l.strip().split(', ')
            tasks[topic][name] = time
    return tasks



def main(m):
    tasks = load_priorities()
    choices = []
    for subj in tasks.keys():
        timed_tasks = [item for item in tasks[subj].items() if item[1] < m]
        if len(timed_tasks) == 0:
            continue
        else:
            task = choice(timed_tasks)
            choices.append((subj, task[0], task[1]))

    if len(choices) > 0:
        suggestion = choice(choices)
        print "Here is a task you could do in this topic: ",  suggestion[0]
        print "\tYou should do this: ", suggestion[1]
        print "\tIt will take you", suggestion[2], "minutes."

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage error: Please specify a time interval"
    else:
        minutes = sys.argv[1]
        main(minutes)
