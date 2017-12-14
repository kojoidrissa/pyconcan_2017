employee_ids_comprehension = {
    row[0].value
    for row in demo_worksheet.rows # returns generator object
    if row[0].value != 'employee_num'
}