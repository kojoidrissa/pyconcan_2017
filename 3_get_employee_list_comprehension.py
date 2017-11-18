employee_ids_comprehension = {
    row[0].value
    for row in demo_worksheet.rows
    if row[0].value != 'employee_num'
}