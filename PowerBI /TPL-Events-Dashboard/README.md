# **Toronto Public Library Events Dashboard**
## **Project Overview**

This project analyzes community events offered by the Toronto Public Library using open data. The goal was to create an interactive and user-friendly dashboard that helps users explore library programs by location, audience group, and event type.

The dashboard was built using Power BI and data sourced from the Open Toronto Data Portal.

## **Business Problem**

While browsing events on the Toronto Public Library website, I noticed that it can be difficult to quickly explore events by:

* branch location

* audience type

* event schedule

* event category

To improve the experience, I designed an interactive dashboard that allows users to explore events more efficiently.

## **Data Source**

**Dataset obtained from:** [Open Toronto Data Portal](https://open.toronto.ca/dataset/library-branch-programs-and-events-feed/) 

**Dataset:** [Library Branch Programs and Events Feed](https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/fb343332-03cd-40b9-a1c8-c03a4a85ca1e/resource/64b78724-6bba-45ac-b760-7faa046834bf/download/tpl-events-feed.csv)

The dataset used in this project was connected directly to a web source from the **Open Data Toronto** portal using Power BI’s Web data connector.

This approach allows the dashboard to:

* Refresh automatically when the source dataset is updated

* Avoid storing large static datasets locally

* Keep the Power BI model lightweight and efficient

Because the data is pulled directly from the web source, the dashboard can be refreshed to reflect the most recent events published by [**Toronto Public Library**](https://open.toronto.ca/dataset/library-branch-programs-and-events-feed/).

## **Data Cleaning & Transformation**

The dataset was mostly clean. Minor transformations were performed in Power BI, including separating timestamp fields into individual components for better analysis.

**Tasks performed:**

- Split Start Date Timestamp into: Start Date & Start Time

- Split End Date Timestamp into: End Date & End Time

This allowed easier analysis of event schedules.

## **DAX Measures**

Key metrics were calculated using DAX measures, including:

* Total Events

* Total Branches

* Kids Events

* Teen Events

* Adult Events

* Older Adult Events

Audience-specific measures were calculated using **CONTAINSSTRING** to identify events targeting different age groups.

## **Dashboard Features**

The Power BI dashboard contains two interactive pages designed to provide both high-level insights and detailed event exploration.

### **1. Event Overview**

This page provides descriptive analytics about library programs and overall event distribution.

**Key features include:**

- KPI cards

- Total Events

- Total Branches

- Kids Events

- Teen Events

- Adult Events

- Older Adult Events

**Event distribution by location** - Bar chart showing which library branches host the most events.

**Audience distribution** - Pie chart showing the proportion of events targeted to different audience groups.

**Seasonal event trends** - Line chart showing how events vary across months.

**Popular events analysis** - Visual highlighting frequently occurring programs.

**Navigation buttons** - Buttons allow users to move easily between the Event Overview and Event Explorer pages.

<img width="1412" height="800" alt="Events Overview" src="https://github.com/user-attachments/assets/33c2aca1-5b8e-466e-9e96-5b3869fbf3e1" />

### **2. Event Explorer**

This page allows users to interactively explore and filter events.

Users can search events using multiple slicers, including:

- Library branch

- Audience type

- Event type

- Event title

- Event day

- Event month

- Event status

- Event timing

### **Additional features:**

- Searchable dropdown slicers for easier filtering.

- Clear All Filters button to quickly reset all slicers.

- Dynamic event table that updates automatically based on selected filters.

- Navigation buttons to return to the overview page.

<img width="1410" height="796" alt="TPL Events Exploler" src="https://github.com/user-attachments/assets/3765c5ed-e475-4c43-8d0d-5bb9c334faf9" />

## **Key Insights**

* Some branches host significantly more events than others.

* Spring months show the highest number of programs.

* Adult programs represent the largest share of library events.

## **Future Improvements**

* Map visualization for branch locations

* Event attendance analysis

* Recommendation system for events

## **Demostrations**
To demonstrate how the dashboard works, I’ve also included a short video showing how users can interact with the filters and explore different events.


https://github.com/user-attachments/assets/43474418-b303-41b6-a36f-7be8941ee336


Author

Pooja
Data Analyst
