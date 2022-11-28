import xlrd
from Library.config_DemoWebShop import ConfigDemoWeb

path = r"C:\Users\Lenovo\Desktop\DemoWebShop Data\DemoWebShop.xlsx"

zip_code = [(560019),(00000),(1233445566)]




def demoWeb_locators():

    demo_workbook = xlrd.open_workbook(ConfigDemoWeb.DATA_PATH)

    demo_worksheet = demo_workbook.sheet_by_name("DemoWeb")

    rows = demo_worksheet.get_rows()

    demo = {}

    for row in rows:
        demo[row[0].value] = (row[1].value, row[2].value)

    return demo


print(demoWeb_locators())



########################################################################################################

#######################################################################################################















# # actitime reading Objects
#
# import xlrd
# from Library.config import Config
#
# path = r"C:\Users\Lenovo\Desktop\Actitime.xlsx"
#
# def read_locators():
#     workbook = xlrd.open_workbook(Config.DATA_PATH)
#     worksheet = workbook.sheet_by_name("Sheet1")
#
#     rows = worksheet.get_rows() #it reads data & creates a generator obj
#     print(rows)
#
#     header = next(rows)
#     d = {}
#
#     for row in rows:
#         d[row[0].value] = (row[1].value,row[2].value)
#
#         # print(row[0].value,row[1].value,row[2].value,)
#     return d
#
# print(read_locators())


############################################################
# import xlrd
#from Library.config import Config
# path = r"C:\Users\Lenovo\Desktop\Actitime.xlsx"
#
#
# def read_locators():
#     workbook = xlrd.open_workbook(Config.DATA_PATH)
#     worksheet = workbook.sheet_by_name("Sheet1")
#
#     rows = worksheet.nrows
#     print(rows)
#     d = {}
#     for i in range(1, rows):
#         row = worksheet.row_values(i)
#         # print(row)
#
#         d[row[0]] = (row[1], row[2])
#     return d
#
# # read_locators()