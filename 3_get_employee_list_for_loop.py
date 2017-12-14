employee_ids = set()
for row in demo_worksheet.rows: # returns a generator object
    if row[0].value != 'employee_num':
        employee_ids.add(row[0].value) # pulling data from a cell