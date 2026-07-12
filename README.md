# Cleaning Messy HR Data (Python)

Created a data cleaning project using Pandas to transform a messy and inconsistent HR dataset into a clean dataset that is ready for further analysis.

## Tech Stack Used
•	Python – Programming language
•	VS Code – Open-source code editor used to write and run Python code
•	Pandas – High-level library for data manipulation and cleaning
•	NumPy – Used along with Pandas to handle missing values 

## Data Source
I used a 1000-row uncleaned HR dataset from GitHub, which was shared for practice purposes.

## Highlights
### Problem
Every company maintains employee information such as joining date, salary, department, and other details. If this data contains missing values, inconsistencies, formatting issues, or unnecessary characters, it becomes difficult for the company to make better decisions, such as employee promotions, transfers, or workforce analysis.

### Goal
To provide a clean and well-structured dataset that can be used for further analysis and business decision-making.

### Data Cleaning Process
The process I followed to clean this industry-level mini dataset:
•	Explored the dataset by checking each column one by one to identify data quality issues.
•	Removed duplicate rows by keeping only the first occurrence.
•	Removed leading and trailing spaces from all string columns.
•	Removed unnecessary middle spaces from the Name column.
•	Removed special characters from columns.
•	Replaced inconsistent values.
•	Handled missing values and blank spaces.
•	Converted columns to the appropriate data types.

### Data Analysis
After cleaning the data, I performed some data analysis and solved interview-style questions, including:
•	Number of employees who joined each year.
•	Employees working in the Finance department with salaries below the average salary.
•	Employees working in the HR or Marketing department.
•	Count of employees working in the Sales department.
•	Most common performance score.
•	Joining month with the highest number of recruitments.
•	Gender with the highest average salary.

### Final Output
Finally, I combined all the cleaning steps and generated a new cleaned CSV file, and loaded the cleaned dataset for ensuring the data quality of the cleaned file.

