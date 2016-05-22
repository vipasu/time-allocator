import sys
from collections import defaultdict
import numpy as np



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
    for subj in tasks.keys():
        timed_tasks = [item for item in tasks[subj].items() if item[1] < m]
        num_tasks = len(timed_tasks)
        if num_tasks == 0:
            print "loljk"
        else:
            print "Here is a task you could do in this topic"
            print '\t ', subj
            index = np.random.choice(num_tasks)
            task = timed_tasks[index]
            print "\tYou should do this: ", task[0]
            print "\tIt will take you", task[1], "minutes."

if __name__ == '__main__':
    minutes = sys.argv[1]
    main(minutes)
