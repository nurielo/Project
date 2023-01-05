
import pandas as pd
import numpy as np
from datetime import datetime
import math as mt


readingData = r'C:\Users\Hadar\iCloudDrive\הנדסה תעשייה וניהול\פרוייקט גמר\inputs\input_150_0.7.csv'##read from csv
jobsRead = pd.read_csv(readingData)
stam=np.array(jobsRead)
allInputs=stam.astype(int)
##inputs
n=np.size(allInputs,1)
m=3
factor=0.995

solutions=np.empty((100,3), dtype=object)
solIndex=0
##start initialization
for t in range (0,len(allInputs)-1,5):
    start= datetime.now()
    inputs=allInputs[t+1:t+4,1:]
    jobs=[i for i in range (1,n+1)]

    deltaAndaj=[]
    for x in range(n):
        deltaAndaj.append(inputs[0][x]+inputs[2][x])
    inputs=np.vstack([inputs,deltaAndaj ])

    sortJobs = inputs
    sortJobs= np.atleast_2d(sortJobs).T
    sortJobs=sortJobs[sortJobs[:, 3].argsort()]
    sortJobs= np.atleast_2d(sortJobs).T

    jobs=np.vstack([jobs,sortJobs ])
    ##aj\bj
    ajDbj=[]
    for x in range(n):
        ajDbj.append(jobs[1][x]/jobs[2][x])
    jobs=np.vstack([jobs,ajDbj ])

## to check delta
    a_early=0
## early job group
    earlyJob=np.empty((6,0))
## tardy job group
    tardyJob=np.empty((6,0))
## for max job to calculate cmax
    pjJob=[]
    ## start permotation
    for i in range(n):
        if jobs[3][i]>=a_early:
            earlyJob=np.column_stack((earlyJob, jobs[0:6,i]))
            pjJob.append(jobs[1][i])
            a_early=a_early+jobs[1][i]
        else:
            tardyJob=np.column_stack((tardyJob, jobs[0:6,i]))
            pjJob.append(jobs[1][i]+jobs[2][i])
##finish initialization

    maxJob=np.max(pjJob)
    z=(m-1)*maxJob+(sum(pjJob[i] for i in range (n)))
    ## best permotation
    bestZ=z
    bestEarly=earlyJob
    bestTardy=tardyJob
    #temp permotation
    tempZ=z
    tempEarly=earlyJob
    tempTardy=tardyJob
    ##Initial temperature
    Tstart=1000
    tFinal=0.001
    # num of iteration for each temprator
    while Tstart>tFinal:
        ls=1
        lr=18
        ##find a neibor sol
        ##choose random job from tardy jobs group
        while ls<lr:
            neiEarly = tempEarly
            neiTardy = tempTardy
            jobChange=np.random.randint(0, len(neiTardy[1]), 1)
            jobNum=neiTardy[0][jobChange]
            ## move the job to early group
            neiEarly=np.column_stack((neiEarly, neiTardy[0:6,jobChange]))
            ## delete random job from tardy
            neiTardy = np.delete(neiTardy, jobChange, 1)
            ## sorting new 2d array by aj\bj
            neiEarly= np.atleast_2d(neiEarly).T
            neiEarly=neiEarly[neiEarly[:, 3].argsort()]## chack 3 is aj and dj
            neiEarly= np.atleast_2d(neiEarly).T
            ## check if early job is meets condition
            NIC=0## what the index of tardy job in early jobs
            for l in range((len(neiEarly[0]))):
                if neiEarly[0][l]== jobNum:
                    NIC=l
            ##handel early job befor the job that add that maybe tardy
            stopOutEarly=False
            deltaInJob=neiEarly[3][NIC]
            for k in range (NIC,0,-1):
                if stopOutEarly==False:
                    cNow=sum(neiEarly[1][i] for i in range (k))
                    if cNow>deltaInJob:
                        ##index for max aj\bj
                        outIndex=np.argmax(neiEarly[5,0:k+1])
                        ##move to tardy job k-1
                        neiTardy = np.column_stack((neiTardy, neiEarly[0:6, outIndex]))
                        ##delete from early k-1
                        neiEarly = np.delete(neiEarly, outIndex, 1)
                    else:
                        stopOutEarly=True
            ##handle early job after the job that early add that maybe tardy
            for l in range(len(neiEarly[0])):
                    if neiEarly[0][l] == jobNum:
                        NIC = l

            indexCheck=NIC+1
            while (indexCheck<len(neiEarly[1])):
                    indexCheck
                    print(indexCheck)
                    print(len(neiEarly[1]))
                    if (sum(neiEarly[1][i] for i in range(indexCheck)))>neiEarly[3][indexCheck]:
                        ## copy this job to tardy
                        neiTardy = np.column_stack((neiTardy, neiEarly[0:6, indexCheck]))
                        ##delete this job from early
                        neiEarly=np.delete(neiEarly,indexCheck,1)
                    else:
                        indexCheck=indexCheck+1
            pjTardy=[]
            for i in range(len(neiTardy[1])):
                        pjTardy.append(neiTardy[1][i]+neiTardy[2][i])
            maxNS=max([np.max(neiEarly[1]),np.max(pjTardy)])
            neiZ= (m-1)*maxNS + sum(neiEarly[1])+ sum(neiTardy[1])+ sum(neiTardy[2])
            if neiZ<tempZ:
                        tempZ=neiZ
                        tempEarly=neiEarly
                        tempTardy=neiTardy
                        if neiZ<bestZ:
                            bestZ=neiZ
                            bestEarly=neiEarly
                            bestTardy=neiTardy
            else:
                        if (mt.exp(-((tempZ-neiZ)/Tstart))>np.random.random()):
                            tempZ=neiZ
                            tempEarly=neiEarly
                            tempTardy=neiTardy
            if ls<lr:
                        ls=ls+1
        Tstart=Tstart*factor
    finishTime=datetime.now()

    ##output
    ##solutions[solIndex][0] = z
    ##solutions[solIndex][1] = (finish - start).total_seconds()
    ##solutions[solIndex][2] = earlyJob
    ##solIndex = solIndex + 1