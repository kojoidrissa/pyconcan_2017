# Create output workbook, then output worksheet
output_book = Workbook() #OpenPyXL object
output_sheet = output_book.create_sheet("Aggregate Time",0)

# Building the Output Header: Specific Cell References
header = [
    demo_worksheet["A1"].value,
    demo_worksheet["B1"].value,
    demo_worksheet["C1"].value,
    demo_worksheet["D1"].value,
    demo_worksheet["G1"].value
]

# Create output data construct & append header 
output_data = []
output_data.append(header)

# Building new rows, then appending them to output data construct
for employee in employee_aggregate: #iterating over dictionary keys
    new_row = []
    new_row.append(employee)
    new_row.append(employee_aggregate[employee]['cost_center'])
    new_row.append(employee_aggregate[employee]['division'])
    new_row.append(employee_aggregate[employee]['manager'])
    new_row.append(employee_aggregate[employee]['hours'])
    output_data.append(new_row)
