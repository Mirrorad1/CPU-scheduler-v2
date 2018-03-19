#Process object
#Gantt gchart
#shift Circular left
#Round Robin RR



class Process:                             #Class for the process 
    def __init__(self, pid, arrival_time, burst_time):		#pid: Process id, arrival_time: Arrival time, burst_time: Burst time
        self.pid = pid 
        self.arrival = arrival_time 
        self.burst = burst_time 
        

def shiftCL(alist):             #alist is queue list 1,2,3=> 3,2,1 => 2,1,3
    temp = alist[0]             #first process in the list 
    for i in range(len(alist)-1):   # -1 
        alist[i] = alist[i+1]       # any shft will add +1 
    alist[len(alist)-1]=temp        #-1 is the last place in the list ex. 0-4 =>5 elements -1 = 4
    return alist

def RR(tq,plist,n):				#Round Robin(RR) (plist: process list, tq: Quantum time)
    global gchart
    queue=[]
    time = 0						#we start arrival_time time 0
    ap= 0							#arrived processes
    done=0							#done processes, to count the number of processes finished 
    q=tq							#time quantum
    start=0 
    rp=0 
    while (done<n):					#still more processes 
        for i in range(ap, n):		#process next in line 
            if time >= plist[i].arrival: #to check for a new arrivil process with out checking P1
                queue.append(plist[i])  
                ap+=1
                rp+=1
        if rp<1:                    #in case of there is no arrival 
            gchart.append(0)
            time+=1
            continue

        if start:
            queue = shiftCL(queue) 

            if queue[0].burst>0:
                if queue[0].burst>q:
                    for j in range(time, time+q):
                        gchart.append(queue[0].pid)
                    time+=q
                    queue[0].burst-=q
                else:
                    for j in range(time, time+queue[0].burst):
                        gchart.append(queue[0].pid)
                    time+=queue[0].burst
                    queue[0].burst=0
                    done+=1
                    rp-=1
                start=1 

plist =[]
plist.append(Process(1,0,5))
plist.append(Process(2,1,3))
plist.append(Process(3,3,6))
plist.append(Process(4,5,1))
plist.append(Process(5,6,4))

RR(3,plist, len(plist))
print(gchart) 




