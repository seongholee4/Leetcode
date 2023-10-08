import pandas as pd


# data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
data = [[1, 'Mark', 40000, 3], [3, 'Jack', 30000, 2], [2, 'Alan', 20000, None]]

employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    data = []
    for eachInd, row in employee.iterrows():
        employeeId = row['id']
        employeeName = row['name']
        managerId = row['managerId']
        employeeSalary = row['salary']
        # find out index of the manager

        managerRow = employee[employee['id']==managerId]
        managerSalary = None
        # print(managerRow)
        if not managerRow.empty:
            managerinfo = managerRow.iloc[0]
            managerSalary = managerinfo['salary']
            # managerSalary = managerRow.iloc[0]['salary']
            # print(managerSalary)
        
        if managerSalary is not None and employeeSalary > managerSalary:
            data.append([employeeName])

    # print(data)
    res = pd.DataFrame(data, columns=['Employee'])
    print(res)
    return res

find_employees(employee)