# -*- coding:utf-8 -*-
import xlrd

# 打开excel文件
data = xlrd.open_workbook('测试表模板.xls')

# 获取指定sheet
table = data.sheet_by_name('绩效表')

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols

# 输出HTML表格
print("<table>")
for i in range(nrows):
    print("<tr>")
    for j in range(ncols):
        print("<td>{}</td>".format(table.cell_value(i,j)))
    print("</tr>")
print("</table>")