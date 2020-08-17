from datetime import datetime, date, time
import matplotlib.pyplot as plt
import numpy as np 
'''
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()'''

#plt.hist([1,3,5,9, 3], bins=[1,3,5,9], weights=[1,5,10,9, 6])
plt.hist([0, 24000.376, 219454.24, 219481.131], bins=[0, 24000.376, 219454.24, 219481.131], weights=[1000,0,1000,0])
plt.show()

with open('contact.txt') as f:
    start_end_times = []
    durations = []
    lines = f.readlines()
    observer_names = [lines[2][10:]] 

    #print(observer_1)   
    currline = 4 
    observeri_start_end = []
    while (currline < len(lines)):
        #print(currline)
        if (lines[currline] == '\n'):
            currline += 7
            start_end_times.append(observeri_start_end)
            if (currline < len(lines)): observer_names.append(lines[currline-2][10:])
            observeri_start_end = []
            continue
        line = lines[currline].strip()
        lineinfo = line.split("    ")

        #print(lineinfo)
        st1 = lineinfo[0]
        st2 = lineinfo[1]
        dt1 = datetime.strptime(st1, "%d %b %Y %H:%M:%S.%f")
        dt2 = datetime.strptime(st2, "%d %b %Y %H:%M:%S.%f")
        observeri_start_end.append((dt1, dt2))
        currline+=1

    with open('check_dates.txt', 'w') as fw:
        for i in range (len(start_end_times)):
            for j in range(len(start_end_times[i])):
                fw.write(str(start_end_times[i][j]) + '\n')

    for i in range(1):
        transition_times = []
        start = start_end_times[i][0][0]    
        end = start_end_times[i][-1][1]
        dt_tot = end - start
        print(dt_tot.total_seconds())
        for j in range(len(start_end_times[i])):
            transition_times.append((start_end_times[i][j][0] - start).total_seconds())
            transition_times.append((start_end_times[i][j][1] - start).total_seconds())
        

    