# Big Data Patient No-Show Analysis using Databricks & PySpark

## Project Overview

Healthcare organizations lose millions of dollars every year due to patients missing scheduled appointments without prior notice. These "No-Show" appointments reduce operational efficiency, increase waiting times, and waste medical resources.

In this project, I used Databricks, PySpark, and Spark SQL to build a scalable analytics pipeline that processes a large healthcare dataset and identifies the factors contributing to patient no-shows. The project demonstrates how distributed data processing can be used to generate actionable business insights.

## Business Problem

Healthcare providers struggle with patients who fail to attend scheduled appointments.

### This project answers questions such as:

- Which patients are most likely to miss appointments?
- Does appointment waiting time increase cancellation risk?
- Do age, neighbourhood, SMS reminders, or medical conditions affect attendance?
- How can healthcare organizations reduce no-show rates?

### Dataset

#### The project uses a healthcare appointment dataset containing over 100,000 patient appointment records.

### The dataset includes:

- Patient demographics
- Appointment dates
- Scheduled dates
- Age
- Gender
- SMS reminders
- Medical conditions
- Scholarship information
- Neighbourhood
- Appointment status (Show / No-Show)
- Technologies Used
- Databricks Community Edition
- Apache Spark
- PySpark
- Spark SQL
- Python
- DataFrames
- Git & GitHub

## Project Workflow

### 1. Data Ingestion

    Imported a large CSV dataset into Databricks using Spark DataFrames.
    
    spark.read.csv("https://www.kaggle.com/datasets/joniarroba/noshowappointments?select=KaggleV2-May-2016.csv")
    
Instead of using Pandas, Spark was used to efficiently process large datasets in a distributed environment.

### 2. Schema Inference

Automatically inferred data types including:
- Integer
- Date
- String
- Boolean

This eliminated manual schema creation and improved data consistency.

### 3. Data Cleaning
Performed several preprocessing steps:
- Removed invalid values
- Checked missing records
- Standardized column formats
- Converted dates into timestamp format
- Validated data quality

### 4. Feature Engineering
- Created new analytical features to improve business insights.
- Lead Time
- Calculated the number of days between
- Appointment Booking Date
- Appointment Date

This feature was used to determine whether longer waiting periods increase the likelihood of missed appointments.

Example:
Scheduled Date	Appointment Date	Lead Time
Jan 1	Jan 10	9 Days

### 5. SQL Analytics

Developed multiple Spark SQL queries to analyze patient behavior.

Examples include:
- Overall No-Show Rate
- Calculated the percentage of missed appointments.
- Age Group Analysis
- Compared attendance across different age groups.
- Gender Analysis
- Compared attendance rates between male and female patients.
- Neighbourhood Analysis
- Identified locations with the highest no-show rates.
- Medical Condition Analysis
- Analyzed whether patients with
- Diabetes
- Hypertension
- Alcoholism

### Throughout the project I developed and optimized Spark SQL queries involving:

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- CASE WHEN
- Aggregate Functions
- COUNT
- AVG
- SUM
- DISTINCT
- Common Table Expressions (CTEs)
- Complex filtering
- Date functions
- Data transformations
- Data Validation

### Performed multiple validation checks including:

- Record count verification
- Duplicate checks
- Missing value analysis
- Data consistency validation
- Output reconciliation after transformations

This ensured analytical results were reliable and accurate.

### Key capabilities demonstrated include:

- Processing over 100,000+ healthcare records
- Distributed DataFrames
- Lazy Evaluation
- Parallel execution
- Scalable data transformations
- Memory-efficient processing
- Key Insights

### The analysis revealed several important findings:
- Approximately 20% of appointments resulted in patient no-shows.
- Longer appointment waiting times were associated with higher no-show rates.
- Certain neighbourhoods consistently experienced higher cancellation rates.
- Demographic factors influenced appointment attendance.
- SMS reminders showed varying levels of effectiveness depending on patient segments.
- Business Recommendations

### Based on the analysis, the following recommendations were proposed:
- Send automated reminders closer to appointment dates.
- Prioritize follow-up communications for high-risk patients.
- Reduce lead time between booking and appointments where possible.
- Build predictive models to identify patients at risk of missing appointments.
- Allocate healthcare resources based on historical attendance patterns.

