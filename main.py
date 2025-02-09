# from fastapi import FastAPI, HTTPException
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# import sqlite3
# import re
# from datetime import datetime

# app = FastAPI()

# # Serve static files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Connect to SQLite database
# def get_db_connection():
#     conn = sqlite3.connect('company.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # Define request model
# class Query(BaseModel):
#     query: str

# # Function to normalize department names
# def normalize_department(department: str):
#     return department.strip().capitalize()

# # Function to parse flexible date formats
# def parse_date(date_str: str):
#     try:
#         # Try parsing date in YYYY-MM-DD format
#         return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
#     except ValueError:
#         try:
#             # Try parsing date in DD-MM-YYYY format
#             return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
#         except ValueError:
#             raise ValueError("Invalid date format. Please use YYYY-MM-DD or DD-MM-YYYY.")

# # Function to parse natural language queries
# def parse_query(query: str):
#     query = query.lower()
    
#     # Normalize department names
#     match_all_employees = re.match(r"show me all employees in the (.*) department", query)
#     if match_all_employees:
#         department = normalize_department(match_all_employees.group(1))
#         return f"SELECT * FROM Employees WHERE Department = '{department}'"
    
#     match_manager = re.match(r"(who is|what is) the manager of the (.*) department", query)
#     if match_manager:
#         department = normalize_department(match_manager.group(2))
#         return f"SELECT Manager FROM Departments WHERE Name = '{department}'"
    
#     match_hired_after = re.match(r"list all employees hired after (.*)", query)
#     if match_hired_after:
#         date_str = match_hired_after.group(1)
#         try:
#             date = parse_date(date_str)
#         except ValueError as e:
#             raise ValueError(str(e))
#         return f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"
    
#     match_total_salary = re.match(r"what is the total salary expense for the (.*) department", query)
#     if match_total_salary:
#         department = normalize_department(match_total_salary.group(1))
#         return f"SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE Department = '{department}'"
    
#     raise ValueError("Unsupported query format. Please ask about employees, managers, salaries, or hiring dates.")

# # Endpoint to handle user queries
# @app.post("/query/")
# async def handle_query(user_query: Query):
#     try:
#         sql_query = parse_query(user_query.query)
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute(sql_query)
#         results = cursor.fetchall()
#         conn.close()
        
#         if not results:
#             return {"message": "No results found for your query."}
        
#         # Convert results to list of dictionaries
#         results_list = [dict(row) for row in results]
        
#         # Format the response in natural language
#         if "Total_Salary" in results_list[0]:
#             total_salary = results_list[0]["Total_Salary"]
#             return {"message": f"The total salary expense is ${total_salary}."}
#         elif "Manager" in results_list[0]:
#             manager = results_list[0]["Manager"]
#             return {"message": f"The manager of the department is {manager}."}
#         else:
#             formatted_results = "\n".join([", ".join([f"{key}: {value}" for key, value in result.items()]) for result in results_list])
#             return {"message": f"Here are the results:\n{formatted_results}"}
    
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again later.")

# # # Root endpoint to serve the chatbot UI
# @app.get("/")
# async def read_root():
#     # Serve the index.html file from the static folder
#     return FileResponse("static/index.html")





# from fastapi import FastAPI, HTTPException
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# import sqlite3
# import re
# from datetime import datetime

# app = FastAPI()

# # Serve static files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Connect to SQLite database
# def get_db_connection():
#     conn = sqlite3.connect('company.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # Define request model
# class Query(BaseModel):
#     query: str

# # Function to normalize department names
# def normalize_department(department: str):
#     return department.strip().capitalize()

# # Function to parse flexible date formats
# def parse_date(date_str: str):
#     try:
#         # Try parsing date in YYYY-MM-DD format
#         return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
#     except ValueError:
#         try:
#             # Try parsing date in DD-MM-YYYY format
#             return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
#         except ValueError:
#             raise ValueError("Invalid date format. Please use YYYY-MM-DD or DD-MM-YYYY.")

# # Function to parse natural language queries
# def parse_query(query: str):
#     query = query.lower()

#     # Normalize department names
#     match_all_employees = re.match(r"show me all employees in the (.*) department", query)
#     if match_all_employees:
#         department = normalize_department(match_all_employees.group(1))
#         return f"SELECT * FROM Employees WHERE Department = '{department}'"

#     match_manager = re.match(r"(who is|what is) the manager of the (.*) department", query)
#     if match_manager:
#         department = normalize_department(match_manager.group(2))
#         return f"SELECT Manager FROM Departments WHERE Name = '{department}'"

#     match_hired_after = re.match(r"list all employees hired after (.*)", query)
#     if match_hired_after:
#         date_str = match_hired_after.group(1)
#         try:
#             date = parse_date(date_str)
#         except ValueError as e:
#             raise ValueError(str(e))
#         return f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"

#     match_total_salary = re.match(r"what is the total salary expense for the (.*) department", query)
#     if match_total_salary:
#         department = normalize_department(match_total_salary.group(1))
#         return f"SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE Department = '{department}'"

#     # Handle unsupported queries
#     raise ValueError("Unsupported query format. Please ask about employees, managers, salaries, or hiring dates.")

# # Endpoint to handle user queries
# @app.post("/query/")
# async def handle_query(user_query: Query):
#     try:
#         sql_query = parse_query(user_query.query)
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute(sql_query)
#         results = cursor.fetchall()
#         conn.close()

#         if not results:
#             return {"message": "No results found for your query."}

#         # Convert results to list of dictionaries
#         results_list = [dict(row) for row in results]

#         # Format the response in natural language
#         if "Total_Salary" in results_list[0]:
#             total_salary = results_list[0]["Total_Salary"]
#             return {"message": f"The total salary expense is ${total_salary}."}
#         elif "Manager" in results_list[0]:
#             manager = results_list[0]["Manager"]
#             return {"message": f"The manager of the department is {manager}."}
#         else:
#             formatted_results = "\n".join(
#                 [", ".join([f"{key}: {value}" for key, value in result.items()]) for result in results_list]
#             )
#             return {"message": f"Here are the results:\n{formatted_results}"}

#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again later.")

# # Root endpoint to serve the chatbot UI
# @app.get("/")
# async def read_root():
#     # Serve the index.html file from the static folder
#     return FileResponse("static/index.html")






from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import re
from datetime import datetime

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('company.db')
    conn.row_factory = sqlite3.Row
    return conn

# Define request model
class Query(BaseModel):
    query: str

# Function to normalize department names
def normalize_department(department: str):
    return department.strip().capitalize()

# Function to parse flexible date formats
def parse_date(date_str: str):
    try:
        # Try parsing date in YYYY-MM-DD format
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        try:
            # Try parsing date in DD-MM-YYYY format
            return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD or DD-MM-YYYY.")

# Function to parse natural language queries
def parse_query(query: str):
    # Strip trailing punctuation (e.g., ., ?, !)
    query = query.rstrip('.!?').strip().lower()

    # Normalize department names
    match_all_employees = re.match(r"show me all employees in the (.*) department", query)
    if match_all_employees:
        department = normalize_department(match_all_employees.group(1))
        return f"SELECT * FROM Employees WHERE Department = '{department}'"

    match_manager = re.match(r"(who is|what is) the manager of the (.*) department", query)
    if match_manager:
        department = normalize_department(match_manager.group(2))
        return f"SELECT Manager FROM Departments WHERE Name = '{department}'"

    match_hired_after = re.match(r"list all employees hired after (.*)", query)
    if match_hired_after:
        date_str = match_hired_after.group(1)
        try:
            date = parse_date(date_str)
        except ValueError as e:
            raise ValueError(str(e))
        return f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"

    match_total_salary = re.match(r"what is the total salary expense for the (.*) department", query)
    if match_total_salary:
        department = normalize_department(match_total_salary.group(1))
        return f"SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE Department = '{department}'"

    # Handle unsupported queries
    raise ValueError("Unsupported query format. Please ask about employees, managers, salaries, or hiring dates.")

# Endpoint to handle user queries
@app.post("/query/")
async def handle_query(user_query: Query):
    try:
        sql_query = parse_query(user_query.query)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()

        if not results:
            return {"message": "No results found for your query."}

        # Convert results to list of dictionaries
        results_list = [dict(row) for row in results]

        # Format the response in natural language
        if "Total_Salary" in results_list[0]:
            total_salary = results_list[0]["Total_Salary"]
            return {"message": f"The total salary expense is ${total_salary}."}
        elif "Manager" in results_list[0]:
            manager = results_list[0]["Manager"]
            return {"message": f"The manager of the department is {manager}."}
        else:
            formatted_results = "\n".join(
                [", ".join([f"{key}: {value}" for key, value in result.items()]) for result in results_list]
            )
            return {"message": f"Here are the results:\n{formatted_results}"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again later.")

# Root endpoint to serve the chatbot UI
@app.get("/")
async def read_root():
    # Serve the index.html file from the static folder
    return FileResponse("static/index.html")