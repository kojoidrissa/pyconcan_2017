import openpyxl
from openpyxl import Workbook

# get workbook object; the data_only option captures the current value of any formulae
# Your file should be in the same directory as this code, OR you need to provide the FULL path to that file, not just it's name
wb = openpyxl.load_workbook('pyxl_demo_pyconcan.xlsx', data_only= True)

# WB -> WS -> Cell
demo_worksheet = wb.get_sheet_by_name("clean_data")