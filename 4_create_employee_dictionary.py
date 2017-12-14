# Create a dictionary of each employee and their info for the month
# This is the slowest step

employee_aggregate = {}
for employee in employee_ids:
    # list comprehension: I'll want to sum the hours later
    hours = [
        row[6].value
        for row in demo_worksheet.rows
        if employee == row[0].value
    ]

    # set comprehension: each employee should belong to only ONE cost center
    cost_center = {row[1].value for row in demo_worksheet.rows if employee == row[0].value}
    division = {str(row[2].value) for row in demo_worksheet.rows if employee == row[0].value}
    manager = {row[3].value for row in demo_worksheet.rows if employee == row[0].value}
    
    assert len(cost_center) == len(division) == len(manager) == 1
    
    employee_aggregate[employee]={
        "hours": sum(hours),
        "cost_center": list(cost_center)[0],
        "division": list(division)[0],
        "manager": list(manager)[0]
    }