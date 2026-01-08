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
Outline the steps taken to clean and preprocess the data before analysis.

### Key Visualizations
Include key visualizations that highlight important aspects of the data. Use graphs, charts, or any other visual representation to make your points.

#### Visualization 1: [Title]
[Description and interpretation of the first visualization.]

![Visualization 1](path/to/image1.png)

#### Visualization 2: [Title]
[Description and interpretation of the second visualization.]

![Visualization 2](path/to/image2.png)

## Conclusions/Recommendations
Summarize the main findings from your analysis. If applicable, provide recommendations based on the insights gained from the data.

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.
Source: [Kaggle](https://www.kaggle.com/datasets/afnansaifafnan/study-habits-and-activities-of-students)


#### Old Project Statement 
I think this is a good dataset to do an analysis on because I believe that the amount of pressure we put on students to be constantly studying is actually deterimental to their grades and stress levels. Despite the pressure to be studying all the hours of the day, I believe that the benefits of getting good grades are outweighed by the consequences of being highly stressed and anti-social. Stress will ultimately lead to burnout, causing a loss in motivation and potentially depression. We can use this dataset to find the balance between studying, extracirriculars, sleeping, socializing, etc. to get good grades and relatively low stress levels.

My goal for this project is to find the balance between getting a good GPA, while also keeping stress levels relatively low. 
This dataset has information about study hours, sleep hours, extracurricular hours, social hours, and physical activity hours per day, as well as their GPA and Stress Level (low, moderate, high). Using these features, I would like to find the balance of each of these daily hours to find what makes a good GPA, but also has a low to moderate stress level. 
The purpose of this would be to find a way to make sure students remain mentally healthy, while also making sure they do well in school.  
