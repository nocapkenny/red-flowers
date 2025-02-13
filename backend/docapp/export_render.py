
from openpyxl import Workbook
class BaseXlsRender:
    template_name = "template.xls"
    dest_filename="text.xlsx"
    def __init__(self):
        self.wb= Workbook()

    def save(self):
        self.wb.save(filename = self.dest_filename)
