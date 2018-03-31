# -*-coding:utf-8-*-
""" 
moke
"""
import xlrd
# 打开文件
data = xlrd.open_workbook('test.xlsx')
# 打开工作表
table = data.sheets()[0]
tablex = data.sheets()[1]
# 获得所有行数
nrows = table.nrows
nrowsx = tablex.nrows

# 用一张工作表中编号对应另一张表的编号，形成一对多的关系
json_data = {}
# 获得所有行数据
for i in range(nrows):
    list_data = []
    for x in range(nrowsx):
        if table.row_values(i)[0] == tablex.row_values(x)[0]:
            list_data.append(tablex.row_values(x)[1])
    json_data[table.row_values(i)[1]] = list_data

# print(json_data)

for kk, vv in json_data.items():
    if len(vv) != 0:
        print(kk)
        print(vv)
        print("\n")