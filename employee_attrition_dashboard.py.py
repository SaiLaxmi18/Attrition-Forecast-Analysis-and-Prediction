#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ipython


# In[2]:


from IPython.display import display


# In[3]:


import pandas as pd


data = pd.read_csv('Dataset_HR_Employee_Attrition.csv')

display(data)


# In[4]:


print(data.dtypes)


# In[5]:


display(data.describe())


# In[6]:


print(data['Gender'].value_counts())


# In[7]:


print(data['EducationField'].value_counts())


# In[8]:


print(data['Over18'].value_counts())


# In[9]:


print(data['OverTime'].value_counts())


# In[10]:


print(data.isnull().sum())


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns

# Histogram for Age
sns.histplot(data['Age'], bins=10)
plt.title('Age Distribution')
plt.show()

# Bar plot for Gender
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.show()

sns.histplot(data['MaritalStatus'], bins=10)
plt.title('Marital Status')
plt.show()


# In[12]:


duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")


# In[13]:


print(data['MaritalStatus'].unique())


# In[14]:


print(data['Attrition'].unique())


# In[15]:


print(data['BusinessTravel'].unique())


# In[16]:


print(data['Department'].unique())


# In[17]:


print(data['EducationField'].unique())


# In[18]:


print(data['JobRole'].unique())


# In[19]:


print(data['Gender'].unique())


# In[20]:


print(data['Over18'].unique())


# In[21]:


print(data['OverTime'].unique())


# In[22]:


def to_sentence_case(text):
    return text.capitalize()

data['Gender'] = data['Gender'].apply(to_sentence_case)


# In[23]:


def to_sentence_case(text):
    return text.capitalize()

data['Over18'] = data['Over18'].apply(to_sentence_case)


# In[24]:


categorical_columns = data.select_dtypes(include=['object']).columns
print(categorical_columns)


# In[25]:


from sklearn.preprocessing import LabelEncoder


# In[26]:


label_encoder = LabelEncoder()

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])


# In[27]:


print(data['Attrition'].unique())


# In[28]:


display(data.head())


# In[29]:


data['EducationField'] = data['EducationField'].map({'Life Sciences': 1, 'Medical': 2, 'Marketing': 3, 'Technical Degree': 4, 'Human Resources': 5, 'Other': 6})


# In[30]:


data['PerformanceRating'] = data['PerformanceRating'].map({'Low': 1, 'Good': 2, 'Excellent': 3, 'Outstanding': 4})


# In[31]:


pip install dash


# In[32]:


pip install streamlit


# In[33]:


pip install --upgrade typing_extensions


# In[34]:


import sys

print(sys.version)


# In[35]:


pip install --upgrade streamlit


# In[37]:


pip install dash pandas plotly


# In[38]:


display(data)

