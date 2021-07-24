import xlrd

def excel_data(sheetIndex,rowValues,filename):

    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(sheetIndex)

    data = sheet.row_values(rowValues)
    return data



