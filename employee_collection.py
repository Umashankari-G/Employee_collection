from collections import defaultdict

# Employee data to simulate indexing and searching
EMPLOYEE_DATA = [
    {'EmployeeID': 'E01', 'Name': 'uma', 'Department': 'IT', 'Gender': 'Female'},
    {'EmployeeID': 'E02', 'Name': 'ajith', 'Department': 'HR', 'Gender': 'Male'},
    {'EmployeeID': 'E03', 'Name': 'mugesh', 'Department': 'Finance', 'Gender': 'Male'},
    {'EmployeeID': 'E04', 'Name': ' Davis', 'Department': 'IT', 'Gender': 'Female'},
    # More records can be added as needed
]

# Dictionary to hold collections
collections = {}

# Function to create a collection
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")

# Function to index data into a collection, excluding a specified column
def indexData(p_collection_name, p_exclude_column):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    for record in EMPLOYEE_DATA:
        indexed_record = {key: value for key, value in record.items() if key != p_exclude_column}
        collections[p_collection_name].append(indexed_record)
    print(f"Data indexed into '{p_collection_name}', excluding '{p_exclude_column}'.")

# Function to search records by a column value
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    results = [record for record in collections[p_collection_name] if record.get(p_column_name) == p_column_value]
    print(f"Search results in '{p_collection_name}' for {p_column_name}='{p_column_value}':")
    for result in results:
        print(result)
    return results

# Function to get the count of employees in a collection
def getEmpCount(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    count = len(collections[p_collection_name])
    print(f"Employee count in '{p_collection_name}': {count}")
    return count

# Function to delete an employee by ID
def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    collections[p_collection_name] = [record for record in collections[p_collection_name] if record.get('EmployeeID') != p_employee_id]
    print(f"Employee '{p_employee_id}' deleted from '{p_collection_name}'.")

# Function to retrieve the count of employees grouped by department
def getDepFacet(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    department_count = defaultdict(int)
    for record in collections[p_collection_name]:
        department_count[record.get('Department', 'Unknown')] += 1
    print(f"Department facet for '{p_collection_name}':")
    for department, count in department_count.items():
        print(f"{department}: {count}")
    return department_count
# Variable initialization
v_nameCollection = 'Hash_YourName'
v_phoneCollection = 'Hash_1234'

# Execute functions in the specified order
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

getEmpCount(v_nameCollection)

indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

delEmpById(v_nameCollection, 'E02003')

getEmpCount(v_nameCollection)

searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
