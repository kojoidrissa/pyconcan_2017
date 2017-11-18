employee_ids = set()
for row in demo_worksheet.rows:
    if row[0].value != 'employee_num':
        employee_ids.add(row[0].value)