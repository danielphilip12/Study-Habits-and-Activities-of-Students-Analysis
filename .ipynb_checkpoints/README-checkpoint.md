# Study-Habits-and-Activities-of-Students-Analysis

## Introduction

This project is about determining where a balance between how students spend their day and having moderate to low stress levels, while also kepping good grades. It looks at how different students spend their day (study time, extracirricular time, sleep time, etc.) and their gpa and stress level. The goal to to try to use the hours spent each day and come up with a predition for how their GPA will be, as well as their stress level. 

For this project, I use regression alghorthims to determine what the students GPA will be based on their distribution of hours in the day, and I use classification models to determine stress levels on the same data. 

For the regression modeling, I trained multiple models, but the Linear Regression model so far has achieved the highest R2 score of 0.56. 

For the classification modeling, I have started with K Nearest Neighbors (KNN), as I believe this model is the best choice, as I am trying to determine which class (low, moderate, or high stress level) a student would belong to based on how they spend their day. 

## Problem Statement

- This dataset contains information about how students spend their day, their GPA, and their stress level. Many students suffer from having high stress, which is deterimental to their mental health, and we as a society seem to encourge this kind of behavior to acheive good marks. However, I believe that the consequences of having a high stress school life outweigh the benefits of having good grades. 

- This project is about finding the balance between study time and personal time to be able to achieve high GPA, while still having a relatively low stress life. 

## Data Dictionary
Include a data dictionary to explain the meaning of each variable or field in the dataset. You can also link to an external data dictionary.

| Column Name | Description |
|-------------|-------------|
| Student ID     | Unique Identifier assigned to each student |
| Study Hours Per Day     | The average number of hours in which a student spends time studying daily |
| Extracurricular Hours Per Day         | number of hours a student spends time on extra-curricular activites (like clubs, arts, hobbies, etc.)         |
| Sleep Hours Per Day         | number of hours a student sleeps per day         |
| Social Hours Per Day         | Numebr of hours perday a student spends with friends, family, etc.         |
| Physical Activity Hours Per Day         | numebr of hours spent in physical activity daily         |
| GPA         | Grade Point average representing academic performance         |
| Stress Level         | Stress catergory of the student (low, moderate, high)         |

## Executive Summary

### Data Cleaning Steps
There were no missing values in this dataset, nor were there any obscure data points that indicat incorrect values, so little data cleaning had to be done. 

However, to have this data be more general, I removed some "outliers" from Physical Activity, as these may be students that focus more on sports, rather than academics. 

I also removed the top and bottom 1% of students by GPA. 

### Key Visualizations

Going through the data, the most related attributes to the GPA and Stress Level seemed to be Study Hours, as well as Physical Activity Hours. 

#### Visualization 1: [GPA vs Study Hours by Stress Level]
The below scatterplot shows how GPA and Study Hours are related, as also color-codes the points by the stress level. 

We can see very clear distinctions between the stress levels when it comes to the study hours, with people of high stress generally studying 8+ hours, moderately stressed students between 6-8 hours, and low stress students 6 or less hours.  

We also see that, generally, as the number of hours studying per day go up, the GPA also goes up. 

![Visualization 1](images/gpa_study_stress.png)

#### Visualization 2: [GPA vs Physical Activity Hours by Stress Level]
The below scatterplot shows how GPA and Physical Activity Hours are related, and color codes the data points by stress level. 

We see there is less distinction between the groups than there was in the Study Hours scatterplot. 

However, there does seem to be a pattern where as the GPA goes up, the number of physical activity hours goes down. 

![Visualization 2](images/gpa_phys_stress.png)

## Conclusions/Recommendations
TBD

## Additional Information
Source: [Kaggle](https://www.kaggle.com/datasets/afnansaifafnan/study-habits-and-activities-of-students)
