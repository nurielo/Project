#imports:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import mutual_info_classif
import statsmodels.api as sm

#------------------1 Exploratory data analysis

XY = r'C:/Users/User/Desktop/machine/פרויקט/XY_train.csv'
XY_f = pd.read_csv(XY)



#cities piechart
XY_f['city'] = XY_f['city'].astype(str)
labels = XY_f['city'].astype('category').cat.categories.tolist()
counts = XY_f['city'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("Cities Distribution", fontsize=15)
plt.show()

#city_development hist
plt.ticklabel_format(style = 'plain')
plt.xlim([0,1])
plt.xticks(np.arange(0,1,0.1))
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('percent', fontsize=15)
plt.title("city development ", fontsize=15)
plt.hist(XY_f['city_development_index'], bins=20 ,edgecolor='black', color='darkblue')
plt.show()

# city_development boxplot
plt.ticklabel_format(style = 'plain')
plt.title("city development boxplot", fontsize=15)
plt.ylim([0,1])
plt.yticks(np.arange(0,1,0.1))
sns.boxplot(y=XY_f['city_development_index'])
plt.show()


#gender piechart
XY_f['gender'] = XY_f['gender'].astype(str)
labels = XY_f['gender'].astype('category').cat.categories.tolist()
counts = XY_f['gender'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("Gender Distribution", fontsize=15)
plt.show()


#enrolled_university piechart
XY_f['enrolled_university'] = XY_f['enrolled_university'].astype(str)
labels = XY_f['enrolled_university'].astype('category').cat.categories.tolist()
counts = XY_f['enrolled_university'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("University course enrolled- PieChart", fontsize=15)
plt.show()

#education_level piechart
XY_f['education_level'] = XY_f['education_level'].astype(str)
labels = XY_f['education_level'].astype('category').cat.categories.tolist()
counts = XY_f['education_level'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("education level- PieChart", fontsize=15)
plt.show()

#candidate experience in years hist
experience =[]
for i in XY_f['experience']:
    if i == '>20':
        experience.append(20)
    elif i == '<1':
        experience.append(0)
    elif i is not None and type(i) != float:
        experience.append(int(i))

plt.ticklabel_format(style = 'plain')
plt.xlim([0,20])
plt.xticks(np.arange(0,21,1))
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('candidate experience', fontsize=15)
plt.title("candidate experience in years ", fontsize=15)
plt.hist(experience, bins=20 ,edgecolor='black', color='darkblue')
plt.show()

#candidate experience in years boxPlot
plt.ticklabel_format(style = 'plain')
plt.title("candidate experience in years", fontsize=15)
plt.ylim([0,21])
plt.yticks(np.arange(0,21,1))
sns.boxplot(y= experience)
plt.show()

#relevent experience piechart
XY_f['relevent_experience'] = XY_f['relevent_experience'].astype(str)
labels = XY_f['relevent_experience'].astype('category').cat.categories.tolist()
counts = XY_f['relevent_experience'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("relevent experience- PieChart", fontsize=15)
plt.show()


#company size histogram
companysSize =[]
for i in XY_f['company_size']:
    if i == '<10':
        companysSize.append(1)
    elif i == "Oct-49":
        companysSize.append(2)
    elif i == '50-99':
        companysSize.append(3)
    elif i == '100-500':
        companysSize.append(4)
    elif i == '500-999':
        companysSize.append(5)
    elif i == '1000-4999':
        companysSize.append(6)
    elif i == '5000-9999':
        companysSize.append(7)
    elif i == '10000+':
        companysSize.append(8)

plt.ticklabel_format(style = 'plain')
plt.xlim([0,9])
plt.xticks(np.arange(0,9,1))
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('company size scale', fontsize=15)
plt.title("company size histogram ", fontsize=15)
plt.hist(companysSize, bins=20 ,edgecolor='black', color='darkblue')
plt.show()

#company type pie-charm
XY_f['company_type'] = XY_f['company_type'].astype(str)
labels = XY_f['company_type'].astype('category').cat.categories.tolist()
counts = XY_f['company_type'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title("type of the company- PieChart", fontsize=15)
plt.show()

#last new jobs pie charm
XY_f['last_new_job'] = XY_f['last_new_job'].astype(str)
labels = XY_f['last_new_job'].astype('category').cat.categories.tolist()
counts = XY_f['last_new_job'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title(" previous job- PieChart", fontsize=15)
plt.show()

#training hours hist
plt.ticklabel_format(style = 'plain')
plt.xlim([0,337])
plt.xticks(np.arange(0,340,30))
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('training hours ', fontsize=15)
plt.title("training hours histogram ", fontsize=15)
plt.hist(XY_f['training_hours'], bins=20 ,edgecolor='black', color='darkblue')
plt.show()

#training hours boxPlot
plt.ticklabel_format(style = 'plain')
plt.title("training hours", fontsize=15)
plt.ylim([0,340])
plt.yticks(np.arange(0,340,30))
sns.boxplot(y= XY_f['training_hours'])
plt.show()

#company type pie chart
XY_f['company_type'] = XY_f['company_type'].astype(str)
labels = XY_f['company_type'].astype('category').cat.categories.tolist()
counts = XY_f['company_type'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title(" company type- PieChart", fontsize=15)
plt.show()

# target pie chart
XY_f['target'] = XY_f['target'].astype(str)
labels = XY_f['target'].astype('category').cat.categories.tolist()
counts = XY_f['target'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
centre_circle = plt.Circle((0,0),0.75,color='pink', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title(" target- PieChart", fontsize=15)
plt.show()

#HeatMap
XY_WithoutCategory = pd.read_csv(XY)
XY_WithoutCategory.drop('city',1,inplace=True)
XY_WithoutCategory.drop('enrollee_id',1,inplace=True)
XY_WithoutCategory.drop('gender',1,inplace=True)
XY_WithoutCategory.drop('relevent_experience',1,inplace=True)
XY_WithoutCategory.drop('enrolled_university',1,inplace=True)
XY_WithoutCategory.drop('education_level',1,inplace=True)
XY_WithoutCategory.drop('major_discipline',1,inplace=True)
XY_WithoutCategory.drop('company_size',1,inplace=True)
XY_WithoutCategory.drop('company_type',1,inplace=True)
XY_WithoutCategory.drop('last_new_job',1,inplace=True)
XY_WithoutCategory.drop('target',1,inplace=True)
XY_WithoutCategory.drop('experience',1,inplace=True)

experience =[]
for i in XY_f['experience']:
    if i == '>20':
        experience.append(20)
    elif i == '<1':
        experience.append(0)
    elif i is not None and type(i) != float:
        experience.append(int(i))
    else:
        experience.append(i)
XY_WithoutCategory['experience'] = experience

companysSize =[]
for i in XY_f['company_size']:
    if i == '<10':
        companysSize.append(1)
    elif i == "Oct-49":
        companysSize.append(2)
    elif i == '50-99':
        companysSize.append(3)
    elif i == '100-500':
        companysSize.append(4)
    elif i == '500-999':
        companysSize.append(5)
    elif i == '1000-4999':
        companysSize.append(6)
    elif i == '5000-9999':
        companysSize.append(7)
    elif i == '10000+':
        companysSize.append(8)
    else:
        companysSize.append(i)

XY_WithoutCategory['companysSize'] = companysSize


sns.heatmap(XY_WithoutCategory.corr(), annot=True, cmap='PiYG')
plt.yticks(fontsize=7.5)
plt.xticks(rotation=20,fontsize=7.5)
plt.title("HeatMap", fontsize=15)
plt.show()


#------------------2---------------------------------------------------------------------------
###################PreProcess######################################
# 1. Nulls Handeling:
#adding to company size the midian and add an attribute to remember the data change
isCompanySizeNull=[]
company_size = []
for i in XY_f['company_size']:
    i = str(i)
    if i == 'nan':
       i = '100-500'
       isCompanySizeNull.append(True)
    else:
        isCompanySizeNull.append(False)
    company_size.append(i)

XY_f['isCompanySizeNull'] = isCompanySizeNull
XY_f['company_size'] = company_size

#adding to last_new_job  the midian and add an attribute to remember the data change
is_last_new_jobe_Null=[]
last_new_job = []
for i in XY_f['last_new_job']:
    i = str(i)
    if i == 'nan':
       i = 2
       is_last_new_jobe_Null.append(True)
    else:
        is_last_new_jobe_Null.append(False)
    last_new_job.append(i)

XY_f['is_last_new_jobe_Null'] = is_last_new_jobe_Null
XY_f['last_new_job'] = last_new_job

#updating null to new catagory- 'miss'
gender = []
for i in XY_f['gender']:
    i = str(i)
    if i == 'nan':
       gender.append('miss')
    else:
        gender.append(i)
XY_f['gender'] = gender
#-------------------------------
enrolled_university = []
for i in XY_f['enrolled_university']:
    i = str(i)
    if i == 'nan':
       enrolled_university.append('miss')
    else:
        enrolled_university.append(i)
XY_f['enrolled_university'] = enrolled_university
#-------------------------------
education_level= []
for i in XY_f['education_level']:
    i = str(i)
    if i == 'nan':
       education_level.append('miss')
    else:
       education_level.append(i)
XY_f['education_level'] = education_level
#-------------------------------
major_discipline= []
for i in XY_f['major_discipline']:
    i = str(i)
    if i == 'nan':
       major_discipline.append('miss')
    else:
       major_discipline.append(i)
XY_f['major_discipline'] = major_discipline
#-------------------------------
company_type= []
for i in XY_f['company_type']:
    i = str(i)
    if i == 'nan':
       company_type.append('miss')
    else:
       company_type.append(i)
XY_f['company_type'] = company_type

# Removing Nulls from experience
XY_f = XY_f.dropna(subset=['experience'])

#  duplicated values Handeling:
XY_f.duplicated(subset=None, keep='first')

# handling a mistake in the data in company size varable
company_size = []
for i in XY_f['company_size']:
    if i == 'Oct-49':
       company_size.append('10-49')
    else:
        company_size.append(i)
XY_f['company_size'] = company_size


#-----------------------feature extraction-----------
#-----experience*is relevant experience-----
years_of_relevant_experience = []
for i in XY_f.index:
    if XY_f.loc[i, 'relevent_experience'] == 'Has relevent experience':
        years_of_relevant_experience.append(XY_f.loc[i, 'experience'])
    else:
        years_of_relevant_experience.append('0')
XY_f['years_of_relevant_experience'] = years_of_relevant_experience

#-----•	CityRatio Job Change-----

def CityCount(city):
    cityCount = (XY_f['city'] == city).sum()
    return cityCount
def target0Amount(city):
    NotChangedAmount = 0
    for i in XY_f.index:
        if XY_f.loc[i, 'city'] == city:
            if (XY_f.loc[i, 'target']) == 0:
                NotChangedAmount+=1
    return NotChangedAmount

XY_f ['city_ratio_job_change'] = 0
for i in XY_f.index:
    cityCount = CityCount(XY_f.loc[i, 'city'])
    NotChangedAmount = target0Amount(XY_f.loc[i, 'city'])
    city_ratio = NotChangedAmount/cityCount
    XY_f.loc[i, 'city_ratio_job_change'] = city_ratio

#-----------------------feature Representation-----------

#-----------normalization-----
XY_f_normalized = pd.DataFrame(XY_f)
XY_f_normalized.drop('city',1,inplace=True)
XY_f_normalized.drop('enrollee_id',1,inplace=True)
XY_f_normalized.drop('relevent_experience',1,inplace=True)
XY_f_normalized.drop('is_last_new_jobe_Null',1,inplace=True)
XY_f_normalized.drop('isCompanySizeNull',1,inplace=True)
XY_f_normalized.drop('experience',1,inplace=True)

#convert string data into numeric
for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'years_of_relevant_experience'] == '>20':
        XY_f_normalized.loc[i, 'years_of_relevant_experience'] = '20'
    if XY_f_normalized.loc[i, 'years_of_relevant_experience'] == '<1':
        XY_f_normalized.loc[i, 'years_of_relevant_experience'] = '0'

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'last_new_job'] == 'never':
        XY_f_normalized.loc[i, 'last_new_job'] = '0'
    if XY_f_normalized.loc[i, 'last_new_job'] == '>4':
        XY_f_normalized.loc[i, 'last_new_job'] = '5'

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'company_size'] == '<10':
        XY_f_normalized.loc[i, 'company_size'] = 1
    if XY_f_normalized.loc[i, 'company_size'] == '10-49':
        XY_f_normalized.loc[i, 'company_size'] = 2
    if XY_f_normalized.loc[i, 'company_size'] == '50-99':
        XY_f_normalized.loc[i, 'company_size'] = 3
    if XY_f_normalized.loc[i, 'company_size'] == '100-500':
        XY_f_normalized.loc[i, 'company_size'] = 4
    if XY_f_normalized.loc[i, 'company_size'] == '500-999':
        XY_f_normalized.loc[i, 'company_size'] = 5
    if XY_f_normalized.loc[i, 'company_size'] == '1000-4999':
        XY_f_normalized.loc[i, 'company_size'] = 6
    if XY_f_normalized.loc[i, 'company_size'] == '5000-9999':
        XY_f_normalized.loc[i, 'company_size'] = 7
    if XY_f_normalized.loc[i, 'company_size'] == '10000+':
        XY_f_normalized.loc[i, 'company_size'] = 8

XY_f_normalized['years_of_relevant_experience'] = XY_f_normalized['years_of_relevant_experience'].astype(int)
XY_f_normalized['training_hours'] = XY_f_normalized['training_hours'].astype(int)
XY_f_normalized['last_new_job'] = XY_f_normalized['last_new_job'].astype(int)

# normalize
scaler = StandardScaler()
XY_f_normalized[['city_ratio_job_change','company_size','last_new_job','training_hours', 'years_of_relevant_experience', 'city_development_index']] = scaler.fit_transform(XY_f_normalized[['city_ratio_job_change','company_size','last_new_job','training_hours', 'years_of_relevant_experience', 'city_development_index']])

# change category into numbers groups

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'gender'] == 'Male':
        XY_f_normalized.loc[i, 'gender'] = 1
    if XY_f_normalized.loc[i, 'gender'] == 'Female':
        XY_f_normalized.loc[i, 'gender'] = 2
    if XY_f_normalized.loc[i, 'gender'] == 'Other':
        XY_f_normalized.loc[i, 'gender'] = 3
    if XY_f_normalized.loc[i, 'gender'] == 'miss':
        XY_f_normalized.loc[i, 'gender'] = 4

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'enrolled_university'] == 'no_enrollment':
        XY_f_normalized.loc[i, 'enrolled_university'] = 1
    if XY_f_normalized.loc[i, 'enrolled_university'] == 'Full time course':
        XY_f_normalized.loc[i, 'enrolled_university'] = 2
    if XY_f_normalized.loc[i, 'enrolled_university'] == 'Part time course':
        XY_f_normalized.loc[i, 'enrolled_university'] = 3
    if XY_f_normalized.loc[i, 'enrolled_university'] == 'miss':
        XY_f_normalized.loc[i, 'enrolled_university'] = 4

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'education_level'] == 'Primary School':
        XY_f_normalized.loc[i, 'education_level'] = 1
    if XY_f_normalized.loc[i, 'education_level'] == 'High School':
        XY_f_normalized.loc[i, 'education_level'] = 2
    if XY_f_normalized.loc[i, 'education_level'] == 'Graduate':
        XY_f_normalized.loc[i, 'education_level'] = 3
    if XY_f_normalized.loc[i, 'education_level'] == 'Masters':
        XY_f_normalized.loc[i, 'education_level'] = 4
    if XY_f_normalized.loc[i, 'education_level'] == 'Phd':
        XY_f_normalized.loc[i, 'education_level'] = 5
    if XY_f_normalized.loc[i, 'education_level'] == 'miss':
        XY_f_normalized.loc[i, 'education_level'] = 6

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'major_discipline'] == 'No Major':
        XY_f_normalized.loc[i, 'major_discipline'] = 0
    if XY_f_normalized.loc[i, 'major_discipline'] == 'Arts':
        XY_f_normalized.loc[i, 'major_discipline'] = 1
    if XY_f_normalized.loc[i, 'major_discipline'] == 'Business Degree':
        XY_f_normalized.loc[i, 'major_discipline'] = 2
    if XY_f_normalized.loc[i, 'major_discipline'] == 'Other':
        XY_f_normalized.loc[i, 'major_discipline'] = 3
    if XY_f_normalized.loc[i, 'major_discipline'] == 'Humanities':
        XY_f_normalized.loc[i, 'major_discipline'] = 4
    if XY_f_normalized.loc[i, 'major_discipline'] == 'STEM':
        XY_f_normalized.loc[i, 'major_discipline'] = 5
    if XY_f_normalized.loc[i, 'major_discipline'] == 'miss':
        XY_f_normalized.loc[i, 'major_discipline'] = 6

for i in XY_f_normalized.index:
    if XY_f_normalized.loc[i, 'company_type'] == 'Other':
        XY_f_normalized.loc[i, 'company_type'] = 1
    if XY_f_normalized.loc[i, 'company_type'] == 'NGO':
        XY_f_normalized.loc[i, 'company_type'] = 2
    if XY_f_normalized.loc[i, 'company_type'] == 'Early Stage Startup':
        XY_f_normalized.loc[i, 'company_type'] = 3
    if XY_f_normalized.loc[i, 'company_type'] == 'Public Sector':
        XY_f_normalized.loc[i, 'company_type'] = 4
    if XY_f_normalized.loc[i, 'company_type'] == 'Funded Startup':
        XY_f_normalized.loc[i, 'company_type'] = 5
    if XY_f_normalized.loc[i, 'company_type'] == 'Pvt Ltd':
        XY_f_normalized.loc[i, 'company_type'] = 6
    if XY_f_normalized.loc[i, 'company_type'] == 'miss':
        XY_f_normalized.loc[i, 'company_type'] = 7

XY_f_normalized.to_csv('C:/Users/User/Desktop/machine/פרויקט/X.csv')

#--------- feature Selection--------------

XY = r'C:/Users/User/Desktop/machine/פרויקט/X.csv'
XY_f_normalized = pd.read_csv(XY)

#heat Map
XY_WithoutCategory = pd.DataFrame(XY_f_normalized)
XY_WithoutCategory.drop('gender',1,inplace=True)
XY_WithoutCategory.drop('enrolled_university',1,inplace=True)
XY_WithoutCategory.drop('education_level',1,inplace=True)
XY_WithoutCategory.drop('major_discipline',1,inplace=True)
XY_WithoutCategory.drop('company_type',1,inplace=True)
XY_WithoutCategory.drop('Unnamed: 0',1,inplace=True)


sns.heatmap(XY_WithoutCategory.corr(), annot=True, cmap='PiYG')
plt.yticks(fontsize=7.5)
plt.xticks(rotation=20,fontsize=7.5)
plt.title("HeatMap", fontsize=15)
plt.show()

#Gain Ratio Information gain:
XY_f_normalized.drop("Unnamed: 0",1,inplace=True)

x = XY_f_normalized[["city_development_index", "gender", "enrolled_university",'education_level', 'major_discipline', "company_size", 'company_type','training_hours','last_new_job','city_ratio_job_change','years_of_relevant_experience']]
y = XY_f_normalized["target"]

importance = mutual_info_classif(x,y)
feat_importance = pd.Series(importance, XY_f_normalized.columns[0: len(XY_f_normalized.columns)-1])
feat_importance.plot(kind='barh', color='teal')


# backward_Logistic_regression----

def get_statsLogistic():
    model = sm.Logit(y, x)
    result = model.fit(method='newton')
    return result.summary2()


# Step 1
x = XY_f_normalized[["city_development_index", "gender", "enrolled_university",'education_level', 'major_discipline', "company_size", 'company_type','training_hours','last_new_job','city_ratio_job_change','years_of_relevant_experience']]
y = XY_f_normalized["target"]
print("--------------------step 1 full model---------")
get_statsLogistic()

# Step 2
x = XY_f_normalized[["city_development_index", "enrolled_university",'education_level', 'major_discipline', "company_size", 'company_type','training_hours','last_new_job','city_ratio_job_change','years_of_relevant_experience']]
y = XY_f_normalized["target"]
print("--------------------step 2 --------")
get_statsLogistic()

# Step 3
x = XY_f_normalized[["city_development_index", "enrolled_university",'education_level', 'major_discipline','company_type','training_hours','last_new_job','city_ratio_job_change','years_of_relevant_experience']]
y = XY_f_normalized["target"]
print("--------------------step 3 --------")
get_statsLogistic()


# ---------------Dimensionality Reduction ------------

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

PCA_Data=pd.DataFrame()
PCA_Data['training_hours'] = XY_f_normalized['training_hours']
PCA_Data['city_ratio_job_change'] = XY_f_normalized['city_ratio_job_change']
PCA_Data['years_of_relevant_experience'] = XY_f_normalized['years_of_relevant_experience']


X_std = StandardScaler().fit_transform(PCA_Data)

# Create a PCA instance: pca
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(X_std)

# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_ratio_, color='black')
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)

# Save components to a DataFrame
PCA_components = pd.DataFrame(data = principalComponents , columns = ['PC1', 'PC2', 'PC3']).astype(float)

# ORDER THE X-TRAIN
XY_f_normalized['PC1'] = PCA_components['PC1']
XY_f_normalized['PC2'] = PCA_components['PC2']
XY_f_normalized['PC3'] = PCA_components['PC3']
XY_f_normalized.drop("training_hours",axis=1,inplace=True)
XY_f_normalized.drop("city_ratio_job_change",axis=1,inplace=True)
XY_f_normalized.drop("years_of_relevant_experience",axis=1,inplace=True)

XY_f_normalized.to_csv('C:/Users/User/Desktop/machine/פרויקט/FinalDataSet.csv')
