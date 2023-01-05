    # This is a sample Python script.
import pandas as pd
import numpy as np
from datetime import datetime


readingData = r'C:\Users\oriny\Desktop\פרוייקט גמר טירוף\אלגוריתם 1\input_25_0.1.csv'##read from csv
jobsRead = pd.read_csv(readingData)

stam=np.array(jobsRead)

mainJobs=stam[1:499,]
allInputs=mainJobs.astype(int)
solIndex=0
solutions=np.empty((100,3), dtype=object)

for lk in range (0,len(allInputs),5):
    start = datetime.now()
    jobs=allInputs[lk:lk+3,]
    ##input data
    n=np.size(jobs,1)## n jobs
    print(n)
    m=3 ##m machines
    basesTime=0 ## for sigma aj

    ## sum base time calaulate sigma aj
    for x in range(n) :
        basesTime = basesTime + jobs[0][x]

    ## calculat  aj sum deltaj
    deltaAndaj=[]
    for x in range(n):
        deltaAndaj.append(jobs[0][x]+jobs[2][x])

    jobs=np.vstack([jobs,deltaAndaj ])## insert deltaj+aj to array

    ##sorting array by AJDJ
    sortJobs = jobs
    sortJobs= np.atleast_2d(sortJobs).T ## sort job table transform
    sortJobs=sortJobs[sortJobs[:, 3].argsort()] ## sorting by deltaj and aj
    sortJobs= np.atleast_2d(sortJobs).T## retern to original table

    ##check optimal solve that all jobs are early
    optimal= True
    sj=0
    for x in range(n):
        if optimal ==  True :
            if sj <= sortJobs[2][x]:
                sj = sj+sortJobs[2][x]
            else:
                optimal = False

    ## calculate aj+bj
    Lj=[]
    for x in range(n):
        Lj.append(sortJobs[0][x]+sortJobs[1][x])
    ##insert aj+bj to array
    sortJobs=np.vstack([sortJobs,Lj ])
    ## count of row needed in the worst case
    row=basesTime+1
    ##array to Z* for all lj
    allTables=[]
    bigSol=[]

    ## flage is lj can be max
    cantBeMax=False

    ##actual algorithm

    if optimal == False :
        ##for l0
        l0 = np.max(sortJobs, 1)[0] ## l0 by max from aj
        max_index = np.argmax(sortJobs[0])
        Cmax0=(m-1)*l0+basesTime ## calaulate started cmax
        table0 = np.empty((row,n+1), dtype=object)##construction table by corrent size
        table0[0][0]=[Cmax0,0, ""] ##initialization the first cell in array

        for t in range(n):##column run
            RBR= list(filter(None, table0[:, t]))##reduce array blank rows
            for k in range (len(RBR)):##row run
                    if (RBR[k])[1] <= sortJobs[2][t]: ##check if sj little than deltaj
                            target = (RBR[k])[0] ## for target function
                            earlyTime = (RBR[k])[1]+sortJobs[0][t]##for sj
                            earlyJob = str((RBR[k])[2])+str(t+1)+","##for list of early jobs
                            addJobs = False
                            if table0[earlyTime][t+1] is not None:
                                    if (table0[earlyTime][t + 1])[0] > target:
                                        table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]
                            else:
                                table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]

                    if (sortJobs[4][t])<= l0 and (max_index!= t):## check if aj+bj little then the max job now
                            target = (RBR[k])[0]+sortJobs[1][t]
                            earlyTime = (RBR[k])[1]
                            earlyJob = str((RBR[k])[2])
                            addJobs = False
                            if table0[earlyTime][t + 1] is not None:
                                if (table0[earlyTime][t + 1])[0] > target:
                                    table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]
                            else:
                                table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]

        if np.count_nonzero(table0[:, n])>0:##if the column is not empty
            targetNow=1000000 ##for lower target
            index=0 ## which index with lower target
            y = list(filter(None, table0[:, n]))
            for b in range (len(y)):## for rhe last column
                if (y[b])[0]< targetNow: ## check if targey function in this iteration is lower then the target befor
                    targetNow=(y[b])[0]
                    index=b
            allTables.append(y[index])##insert the lower solution to the final array
        else:## if the last column is empty
            allTables.append(1000000)
        bigSol.append(table0)


        for x in range(n):##for the max job by lj
            l0 = sortJobs[4][x]## who the max now
            Cmax0 = (m - 1) * l0 + basesTime ##cmax for this iteration
            table0=np.empty((row, n + 1), dtype=object)
            table0[0][0] = [Cmax0, 0, " "]
            cantBeMax=False
            for max in range(n):##check if there is job with base time bigger then the max now
                if cantBeMax==False:
                    if sortJobs[4][x] < sortJobs[0][max]:
                        cantBeMax = True
                        allTables.append(1000000)

            if cantBeMax == False:
                for t in range(n):## loop for sort job
                    RBR= list(filter(None, table0[:, t]))##reduce array blank rows
                    for k in range(len(RBR)):##for that run of column table
                         if (RBR[k])[1] <= sortJobs[2][t] and (t != x):## check if aj little then sj
                             target = (RBR[k])[0]
                             earlyTime = (RBR[k])[1] + sortJobs[0][t]
                             earlyJob = str((RBR[k])[2]) + str(t + 1)+ ","
                             if (table0[earlyTime][t+1]) is not None:
                                     if (table0[earlyTime][t+1])[0]>=target:
                                         table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]
                             else:
                                table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]


                         if (sortJobs[4][t]) <= l0 :
                             target = (RBR[k])[0] + sortJobs[1][t]
                             earlyTime = (RBR[k])[1]
                             earlyJob = str((RBR[k])[2])
                             addJobs = False
                             if (table0[earlyTime][t + 1]) is not None:
                                 if (table0[earlyTime][t + 1])[0] > target:
                                         table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]

                             else:
                                 table0[earlyTime][t + 1] = [target, earlyTime, earlyJob]

                if np.count_nonzero(table0[:, n]) > 0:
                    targetNow = 1000000
                    index = 0
                    y=list(filter(None, table0[:, n]))
                    for b in range(len(y)):
                        if (y[b])[0] < targetNow:
                            targetNow = (y[b])[0]
                            index = b
                    allTables.append(y[index])

                else:
                    allTables.append(1000000)
            bigSol.append(table0)
    finish=datetime.now()

    bestSol=0
    Z=1000000
    for i in range (n+1):
        if allTables[i] !=1000000:
            if (allTables[i])[0] < Z:
                Z = (allTables[i])[0]
                bestSol = i

    solutions[solIndex][0] = (allTables[bestSol])[0]
    solutions[solIndex][1] = (finish-start).total_seconds()
    solutions[solIndex][2] = (allTables[bestSol])[2]
    solIndex = solIndex + 1

titels=["z","running time ","early job"]
solutions=np.vstack([titels,solutions ])

pd.DataFrame(solutions).to_csv(r"C:\Users\oriny\Desktop\outputs\output_25_0.1.csv")

