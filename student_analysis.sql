select avg(sah.Study_Hours_Per_Day), avg(sah.Physical_Activity_Hours_Per_Day ), avg(sah.GPA), sah.Stress_Level  from study_activity_hours sah
group by sah.Stress_Level;
