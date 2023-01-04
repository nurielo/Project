import pandas as pd
import numpy as np
from scipy.optimize import linprog
from ortools.linear_solver import pywraplp
from datetime import datetime

readingData = r'C:\Users\oriny\Desktop\פרוייקט גמר טירוף\אלגוריתם 1\input100.csv'
jobsRead = pd.read_csv(readingData)
stam=np.array(jobsRead)
allInputs=stam.astype(int)
solIndex=0
solutions=np.empty((20,3), dtype=object)
#print(len(allInputs))
#for tabel in range(0,len(allInputs),5):
for LK in range(0,len(input()),5):
    #jobs=allInputs[0:LK+3,]
    jobs=allInputs[95:98,]
    n=np.size(jobs,1)
    m=3
    basesTime=0

    ## sum base time
    for x in range(n) :
        basesTime = basesTime + jobs[0][x]

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

    ajbj=[]
    for i in range(n):
        ajbj.append(sortJobs[0][i]+sortJobs[1][i])
    rangeMax=np.max(ajbj)

    solver=pywraplp.Solver.CreateSolver('SCIP')


    ## define the decision variable
    x={}
    for i in range(n+1):
        if i==0:
            x[i]=solver.IntVar(0,int(rangeMax),'x%s' % i)
        else:
            x[i]=solver.IntVar(0,1,'x%s' % i)


    ## define Constraint  for max job
    for i in range (n):
        solver.Add(x[0] + (sortJobs[1][i] *(x [(i + 1)])) >= (ajbj[i]))


    ## defin constraint for jobs order
    for i in range (1,n):
       solver.Add((sum((x[j+1]*sortJobs[0][j]) for j in range (i)))+ (basesTime*x[i+1])<=sortJobs[2][i]+ (basesTime))

    #for i in range (1,n):
     #   solver.Add((sum((x[j+1]*sortJobs[0][j]) for j in range (i))) <=sortJobs[2][i])

    print('con', solver.NumConstraints())

    ##target function
    solver.Minimize((m-1)*x[0]-1*(sum(x[i+1]*sortJobs[1][i] for i in range(n)))+basesTime+(sum(sortJobs[1][i] for i in range(n))))

    status=solver.Solve()



    earlyJob=[]
    for i in range (1,n+1):
        if x[i].solution_value()==1:
            earlyJob.append(i)
    #print(solver.Objective().Value())
    #print(earlyJob)
    #print(solver.WallTime()*(10**(-6)))
    solutions[solIndex][0]=solver.Objective().Value()
    solutions[solIndex][1] =solver.WallTime()*(10**(-3))
    solutions[solIndex][2] =earlyJob
    solIndex=solIndex+1
    print()
pd.DataFrame(solutions).to_csv(r"C:\Users\oriny\Desktop\outputs\100jobsalgorithm3.csv")

