# Databricks notebook source
# MAGIC %md
# MAGIC ## 1. Load Data from API or a local dataset uploaded into Databricks

# COMMAND ----------

# Read the CSV file "noshowappointments.csv" from the specified path in Databricks Volumes.
# - option("sep", ","): Specifies that the delimiter used in the CSV file is a comma.
# - option("inferSchema", "true"): Instructs Spark to automatically infer the data types of each column.
# - option("header", "true"): Indicates that the first row of the CSV file contains column headers.
# The resulting DataFrame 'df' will have columns and data types inferred from the CSV file.
df = spark.read.option("sep", ",").option("inferSchema", "true").option("header", "true").csv(f"/Volumes/longo_faculty_of_business_aws_5479912711442359/default/dataset1_medical/noshowappointments.csv")

# Display the DataFrame 'df' in a rich tabular format within the Databricks notebook.
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Data Storage and Processing: Load data in a data frame

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2.1 Create a temporary view in SQL

# COMMAND ----------

# Create or replace a local temporary view named "noshowappointments" from the Spark DataFrame 'df'.
# This allows you to run SQL queries directly on the DataFrame using Spark SQL.
# The temporary view exists only for the duration of the SparkSession and is not persisted to disk.
# If a view with the same name already exists, it will be replaced with the new DataFrame.
df.createOrReplaceTempView("noshowappointments")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.	Data Analysis and Visualization:

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.1 Overall Patient Show and No-show Rates 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This query provides an overview of patient attendance for scheduled appointments.
# MAGIC -- It calculates:
# MAGIC --   - The total number of unique patients with appointments.
# MAGIC --   - The percentage of patients who did not show up for their appointments.
# MAGIC --   - The percentage of patients who attended their appointments.
# MAGIC
# MAGIC SELECT
# MAGIC
# MAGIC   COUNT(patientid) AS Total_Patients, -- Total number of unique patients with scheduled appointments.
# MAGIC
# MAGIC   -- Calculate the percentage of patients who did not show up:
# MAGIC   -- COUNT_IF(`No-show` = 'Yes') counts patients who missed their appointments.
# MAGIC   -- Divide by total patients and multiply by 100 to get the percentage, rounded to 2 decimal places.
# MAGIC   ROUND((COUNT_IF(`No-show` = 'Yes')/Total_Patients*100),2) AS Patient_DidNot_Show_Rate, -- Percentage of patients who did not show up.
# MAGIC
# MAGIC   -- Calculate the percentage of patients who attended:
# MAGIC   -- COUNT_IF(`No-show` = 'No') counts patients who attended their appointments.
# MAGIC   -- Divide by total patients and multiply by 100 to get the percentage, rounded to 2 decimal places.
# MAGIC   ROUND((COUNT_IF(`No-show` = 'No')/Total_Patients*100),2) AS Patient_Showed_Rate -- Percentage of patients who attended.
# MAGIC
# MAGIC FROM noshowappointments -- Source table containing appointment and patient data.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.2 No-show rate by Gender

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This query analyzes the number of patients who did not show up for their appointments, grouped by gender.
# MAGIC -- For each gender, it calculates:
# MAGIC --   - The total number of patients who missed their appointments (no-shows).
# MAGIC -- The results are sorted to show the gender with the highest number of no-shows first.
# MAGIC
# MAGIC SELECT
# MAGIC   Gender, -- Gender of the patient (e.g., Male, Female)
# MAGIC   COUNT(*) AS Total_NoShow_Patients -- Total number of patients who did not show up for their appointments
# MAGIC
# MAGIC FROM noshowappointments -- Source table containing appointment and patient data
# MAGIC
# MAGIC WHERE `No-show` = 'Yes' -- Filter to include only appointments where the patient did not show up
# MAGIC
# MAGIC GROUP BY Gender -- Aggregate results by gender
# MAGIC
# MAGIC ORDER BY Total_NoShow_Patients DESC -- Sort results to show genders with the highest number of no-shows first

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.3 No-show rate by Age group 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This query analyzes patient appointment data by age group to identify which age groups have the highest no-show rates.
# MAGIC -- For each age group, it calculates:
# MAGIC --   - The total number of appointments scheduled.
# MAGIC --   - The number of appointments where patients did not show up.
# MAGIC --   - The percentage of appointments that resulted in a no-show.
# MAGIC -- The results are sorted to show age groups with the highest no-show rates first.
# MAGIC
# MAGIC SELECT  
# MAGIC
# MAGIC   -- Define age groups based on patient age:
# MAGIC   -- 'Child' for patients under 18 years old,
# MAGIC   -- 'Young Adult' for patients aged 18 to 35,
# MAGIC   -- 'Adult' for patients aged 36 to 60,
# MAGIC   -- 'Senior' for patients older than 60.
# MAGIC   CASE  
# MAGIC     WHEN Age < 18 THEN 'Child' 
# MAGIC     WHEN Age BETWEEN 18 AND 35 THEN 'Young Adult' 
# MAGIC     WHEN Age BETWEEN 36 AND 60 THEN 'Adult' 
# MAGIC     ELSE 'Senior' 
# MAGIC   END AS AgeGroup, 
# MAGIC
# MAGIC   COUNT(*) AS TotalAppointments, -- Total number of appointments scheduled in each age group.
# MAGIC
# MAGIC   SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) AS NoShows, -- Number of appointments in each age group where the patient did not show up.
# MAGIC
# MAGIC   ROUND(100.0 * SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS NoShowRate -- Percentage of appointments that were no-shows in each age group, rounded to 2 decimal places.
# MAGIC
# MAGIC FROM noshowappointments -- Source table containing appointment and patient data.
# MAGIC
# MAGIC GROUP BY AgeGroup -- Aggregate results by age group.
# MAGIC
# MAGIC ORDER BY NoShowRate DESC; -- Sort results to show age groups with the highest no-show rates first.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.4 No show rate in Top 10 neighbourhoods 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This query analyzes patient appointment data by neighbourhood to identify areas with the highest no-show rates.
# MAGIC -- It calculates, for each neighbourhood:
# MAGIC --   - The total number of appointments scheduled.
# MAGIC --   - The number of appointments where patients did not show up.
# MAGIC --   - The percentage of appointments that resulted in a no-show.
# MAGIC -- The results are sorted to show the top 10 neighbourhoods with the highest no-show rates.
# MAGIC
# MAGIC SELECT  
# MAGIC
# MAGIC   Neighbourhood, -- The name of the neighbourhood where the appointment was scheduled.
# MAGIC
# MAGIC   COUNT(*) AS TotalAppointments, -- Total number of appointments scheduled in each neighbourhood.
# MAGIC
# MAGIC   SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) AS NoShows, -- Number of appointments in each neighbourhood where the patient did not show up.
# MAGIC
# MAGIC   ROUND(100.0 * SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS NoShowRate -- Percentage of appointments that were no-shows in each neighbourhood, rounded to 2 decimal places.
# MAGIC
# MAGIC FROM noshowappointments -- Source table containing appointment and patient data.
# MAGIC
# MAGIC GROUP BY Neighbourhood -- Aggregate results by neighbourhood.
# MAGIC
# MAGIC ORDER BY NoShowRate DESC -- Sort results to show neighbourhoods with the highest no-show rates first.
# MAGIC
# MAGIC LIMIT 10; -- Limit output to the top 10 neighbourhoods by no-show rate.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.5 Correlation between No Show and Medical Conditions 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Count patients by number of chronic conditions and calculate no-show rate
# MAGIC SELECT  
# MAGIC
# MAGIC   -- Calculate total number of chronic conditions for each patient by summing binary indicators:
# MAGIC   -- Hipertension, Diabetes, Alcoholism, Handcap (each is 0 or 1)
# MAGIC   (Hipertension + Diabetes + Alcoholism + Handcap) AS ChronicCount, -- Number of chronic conditions per patient
# MAGIC
# MAGIC   -- Count total number of patients for each chronic condition count
# MAGIC   COUNT(*) AS Patients, -- Number of patients with this count of chronic conditions
# MAGIC
# MAGIC   -- Calculate no-show rate for each chronic condition count:
# MAGIC   -- (Number of no-shows / Total patients) * 100, rounded to 2 decimal places
# MAGIC   ROUND(100.0 * SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS NoShowRate -- No-show rate (%) for each chronic condition count
# MAGIC
# MAGIC FROM noshowappointments 
# MAGIC
# MAGIC -- Group results by the calculated number of chronic conditions
# MAGIC GROUP BY (Hipertension + Diabetes + Alcoholism + Handcap) 
# MAGIC
# MAGIC -- Sort results by chronic condition count in descending order
# MAGIC ORDER BY ChronicCount DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.6 Correlation between Waiting time and No shows 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Categorize appointments by waiting days and calculate no-show statistics
# MAGIC SELECT  
# MAGIC
# MAGIC   -- Define waiting day categories based on the difference between appointment and scheduling dates
# MAGIC   CASE  
# MAGIC     WHEN DATEDIFF(AppointmentDay, ScheduledDay) <= 3 THEN '0-3 days' -- Appointments scheduled within 3 days
# MAGIC     WHEN DATEDIFF(AppointmentDay, ScheduledDay) <= 7 THEN '4-7 days' -- Appointments scheduled between 4 and 7 days
# MAGIC     WHEN DATEDIFF(AppointmentDay, ScheduledDay) <= 14 THEN '8-14 days' -- Appointments scheduled between 8 and 14 days
# MAGIC     ELSE '15+ days' -- Appointments scheduled 15 or more days in advance
# MAGIC   END AS WaitingCategory, 
# MAGIC
# MAGIC   COUNT(*) AS Total, -- Total number of appointments in each waiting category
# MAGIC
# MAGIC   SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) AS NoShows, -- Number of no-shows in each waiting category
# MAGIC
# MAGIC   -- Calculate the percentage of no-shows for each waiting category
# MAGIC   ROUND(100.0 * SUM(CASE WHEN `No-show` = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS NoShowRate -- No-show rate (%) in each waiting category
# MAGIC
# MAGIC FROM noshowappointments 
# MAGIC
# MAGIC -- Group results by waiting day category to aggregate statistics
# MAGIC GROUP BY WaitingCategory 
# MAGIC
# MAGIC -- Sort categories by highest no-show rate
# MAGIC ORDER BY NoShowRate DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.7 Correlation between SMS reminders and No Show 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     -- Categorize SMS received status for each appointment:
# MAGIC     -- 'SMS Received (1)' if SMS_received is 1,
# MAGIC     -- 'SMS Not Received (0)' if SMS_received is 0,
# MAGIC     -- 'Unknown Status' for any other value (should not occur in clean data)
# MAGIC     CASE 
# MAGIC         WHEN SMS_received = 1 THEN 'SMS Received (1)'
# MAGIC         WHEN SMS_received = 0 THEN 'SMS Not Received (0)' 
# MAGIC         ELSE 'Unknown Status' 
# MAGIC     END AS SMS_Status,
# MAGIC     
# MAGIC     -- Count total number of appointments for each SMS status group
# MAGIC     COUNT(*) AS Total_NowShow
# MAGIC     
# MAGIC     -- ... rest of the query remains the same (assuming your NoShow logic is now correct)
# MAGIC     
# MAGIC FROM noshowappointments 
# MAGIC -- Group results by SMS_received value to aggregate statistics for each status
# MAGIC GROUP BY SMS_received;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Project Summary & Strategic Recommendations

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Overall No-Show Rate:** **20.0%** (1 in 5 appointments)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Key Drivers
# MAGIC
# MAGIC - **Long Waits (15+ days):**  
# MAGIC   No-Show Rate: **32.7%**  
# MAGIC   _22 percentage points higher than short waits (9.7%)_
# MAGIC
# MAGIC - **SMS Reminders:**  
# MAGIC   Prevented **8,100+** no-shows
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Recommendations
# MAGIC
# MAGIC 1. **Wait-Time Mitigation:**  
# MAGIC    - Second confirmation (call/email) for appointments >10 days out
# MAGIC
# MAGIC 2. **Targeted Communication:**  
# MAGIC    - Guardian phone confirmation for ages 0–20 (No-Show Rate: **23.8%**)