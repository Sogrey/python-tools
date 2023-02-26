#coding:utf-8
from openpyxl import load_workbook

# 加载excel文件
wb = load_workbook('测试表模板.xlsx')

# 获取工作表
sheet = wb['绩效表']

# 获取表格内容
table = []
for row in sheet.rows:
    line = []
    for cell in row:
        line.append(cell.value)
    table.append(line)

# 输出HTML表格
html = '<table border="1" cellspacing="0" cellpadding="0" width="100%">'
for row in table:
    html += '<tr>'
    for cell in row:
        if cell is None:
            html += '<td rowspan="2"></td>'
        else:
            html += '<td>{}</td>'.format(cell)
    html += '</tr>'
html += '</table>'

print(html)