# This is a sample Python script.
import math as mt
import pandas as pd
import numpy as np
from datetime import datetime

readingData = r'C:\Users\oriny\Desktop\פרוייקט גמר טירוף\אלגוריתם 1\input50.csv'##read from csv
jobsRead = pd.read_csv(readingData)

stam=np.array(jobsRead)
allInputs=stam.astype(int)
solIndex=0
solutions=np.empty((20,4), dtype=object)

for lk in range (0,len(allInputs),5):
    start1 = datetime.now()
    jobs = allInputs[lk:lk + 3, ]
    ##input data
    n=np.size(jobs,1)
    print(n)
    m=3
    basesTime=0
    epsilon=0.1
    indexcheck=mt.floor(2)
    print(indexcheck)

    ## sum base time
    for x in range(n) :
        basesTime = basesTime + jobs[0][x]
        print(basesTime)

    ## add sum aj and delta j
    deltaAndaj=[]
    for x in range(n):
        deltaAndaj.append(jobs[0][x]+jobs[2][x])

    jobs=np.vstack([jobs,deltaAndaj ])

    ##sorting array by AJDJ
    sortJobs = jobs
    sortJobs= np.atleast_2d(sortJobs).T
    sortJobs=sortJobs[sortJobs[:, 3].argsort()]
    sortJobs= np.atleast_2d(sortJobs).T

    ##check optimal solve
    optimal= True
    sj=0
    for x in range(n):
        if optimal ==  True :
            if sj <= sortJobs[2][x]:
                sj = sj+sortJobs[2][x]
            else:
                optimal = False

    print(optimal)

    pjtot=[]
    for x in range(n):
        pjtot.append(sortJobs[0][x]+sortJobs[1][x])
    print(pjtot)

    sortJobs=np.vstack([sortJobs,pjtot ])

    cantBeMax=False

    ##actual algorithm
    allTables=[]
    bigSol=[]
    if optimal == False :
        start1=datetime.now()
        ##for l0
        l0 = np.max(sortJobs, 1)[0]
        max_index=np.argmax(sortJobs[0])
        print(l0)
        Cmax0=(m-1)*l0+basesTime
        ##maxForRange=Cmax
        UB=(m-1) * l0 + (n*l0)
        LB=(m-1)*l0 + basesTime
        row1=(mt.ceil((n*UB)/ (epsilon*LB)))## number of interval
        IL=(epsilon*LB/n)##interval lenght
        table0 = np.empty((row1,n+1), dtype=object)
        table0[0][0]=[Cmax0,0, ""]
        for t in range(n):## run of sort job and column in table
             for k in range (row1):## run row in specifik coiumn in table
                 if ((table0[k][t]) is not None):## if the cell is not empty
                    if ((table0[k][t])[1] <= sortJobs[2][t] ): ## if the job can early
                            target = (table0[k][t])[0]
                            earlyTime = (table0[k][t])[1]+sortJobs[0][t]
                            earlyJob = str((table0[k][t])[2])+str(t+1)+","
                            if (table0[mt.floor(target/IL)][t+1]) is None:
                                table0[mt.floor(target/IL)][t+1] =[target, earlyTime, earlyJob]
                            else:
                                if (table0[mt.floor(target/IL)][t+1])[1]>earlyTime:
                                    table0[mt.floor(target/IL)][t + 1] = [target, earlyTime, earlyJob]

                    if ((sortJobs[4][t])<= l0) and (max_index!= t):
                            target = (table0[k][t])[0]+sortJobs[1][t]
                            earlyTime = (table0[k][t])[1]
                            earlyJob = str((table0[k][t])[2])
                            if (table0[mt.floor(target / IL) ][t + 1]) is None:
                                table0[mt.floor(target / IL) ][t + 1] = [target, earlyTime, earlyJob]
                            else:
                                if (table0[mt.floor(target / IL)][t + 1])[1]>earlyTime:
                                    table0[mt.floor(target / IL)][t + 1] = [target, earlyTime, earlyJob]

        if np.count_nonzero(table0[:, n])>0:
            targetNow=1000000
            index=0
            for b in range (row1):
                if (table0[b][n+1]) is not None:
                    if (table0[b][n+1])[0]< targetNow :
                        targetNow=(table0[b][n])[0]
                        index=b
            allTables.append(table0[index][n])
        else:
            allTables.append(1000000)
        bigSol.append(table0)

        for x in range(n):##for the max job aj+bj
            l0 = sortJobs[4][x]
            Cmax0 = (m - 1) * l0 + basesTime
            UB = (m - 1) * l0 + (n * l0)
            LB = (m - 1) * l0+ sortJobs[1][x]+ basesTime
            row1 = (mt.ceil((n * UB) / (epsilon * LB)))  ## number of interval
            IL = (epsilon * LB / n)  ##interval lenght
            table0 = np.empty((row1, n + 1), dtype=object)
            table0[0][0] = [Cmax0, 0, ""]
            cantBeMax=False
            for max in range(n):##check if ther job with base time bigger then the max now
               if cantBeMax== False:
                    if sortJobs[4][x] < sortJobs[0][max]:
                        cantBeMax = True
                        allTables.append(1000000)
            if cantBeMax == False:
                for t in range(n):## loop for sort job
                    for k in range(row1):
                        if ((table0[k][t]) is not None):  ## if the cell is not empty
                            if ((table0[k][t])[1] <= sortJobs[2][t]) and (t != x):  ## if the job can early
                                     target = (table0[k][t])[0]
                                     earlyTime = (table0[k][t])[1] + sortJobs[0][t]
                                     earlyJob = str((table0[k][t])[2]) + str(t + 1)+ ","
                                     if (table0[mt.floor(target / IL) ][t + 1]) is None:
                                         table0[mt.floor(target / IL) ][t + 1] = [target, earlyTime, earlyJob]
                                     else:
                                         if (table0[mt.floor(target / IL)][t + 1])[1]>earlyTime:
                                             table0[mt.floor(target / IL)][t + 1] = [target, earlyTime, earlyJob]

                                 if (sortJobs[4][t]) <= l0:
                                     target = (table0[k][t])[0] + sortJobs[1][t]
                                     earlyTime = (table0[k][t])[1]
                                     earlyJob = str((table0[k][t])[2])
                                     if (table0[mt.floor(target / IL) ][t + 1]) is None:
                                         table0[mt.floor(target / IL) ][t + 1] = [target, earlyTime, earlyJob]
                                     else:
                                         if (table0[mt.floor(target / IL)][t + 1])[1]>earlyTime:
                                             table0[mt.floor(target / IL)][t + 1] = [target, earlyTime, earlyJob]

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
        if allTables[i] !=1000000 and allTables[i] is not None:
            if (allTables[i])[0] < Z:
                Z= (allTables[i])[0]
                bestSol = i
    solutions[solIndex][0] = (allTables[bestSol])[0]
    solutions[solIndex][1] = ( finish-start1).total_seconds()
    solutions[solIndex][2] = (allTables[bestSol])[2]
    solutions[solIndex][3]=epsilon
    solIndex = solIndex + 1
pd.DataFrame(solutions).to_csv(r"C:\Users\oriny\Desktop\outputs\50jobsalgorithm2eps0.1.csv")