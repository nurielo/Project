import pandas as pd
import numpy as np
from datetime import datetime

readingData =r'C:\Users\Hadar\iCloudDrive\הנדסה תעשייה וניהול\פרוייקט גמר\inputs\input_150_0.7.csv'##read from csv

jobsRead = pd.read_csv(readingData)
stam=np.array(jobsRead)
allInputs=stam.astype(int)
##inputs
n=np.size(allInputs,1)-1
m=3
solutions=np.empty((100,3), dtype=object)
solIndex=0

for t in range (0,len(allInputs)-1,5):
    start= datetime.now()
    inputs=allInputs[t+1:t+4,1:] ##0=t
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
    a_early=0
    b_tardy=0
    earlyJob=[]
    maxjob=[]
    for i in range(n):
        if jobs[3][i]>=a_early:
            earlyJob.append(jobs[0][i])
            maxjob.append(jobs[1][i])
            a_early=a_early+jobs[1][i]
        else:
            maxjob.append(jobs[1][i]+jobs[2][i])
            b_tardy=b_tardy+jobs[2][i]
    finish= datetime.now()
    Max=np.max(maxjob)


    z=(m-1)*Max+(sum(maxjob))
    solutions[solIndex][0] = z
    solutions[solIndex][1] = (finish - start).total_seconds()
    solutions[solIndex][2] = earlyJob
    solIndex = solIndex + 1
    print  (z)
    print(Max)
    print(earlyJob)
pd.DataFrame(solutions).to_csv(r"C:\Users\Hadar\Desktop\output3\output_4_150_0.7.csv")
