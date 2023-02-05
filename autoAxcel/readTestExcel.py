# pip install openpyxl

# https://www.bilibili.com/video/BV1sg41167fA/?p=2&spm_id_from=pageDriver&vd_source=96276a0eadd5914be7e81924f0535ab3

from openpyxl import load_workbook

# 加载Excel
wb = load_workbook('test.xlsx', read_only=True, data_only=True)

# 获取当前激活的工作簿
ws = wb['Sheet1']

count = 0
for row in ws.rows:  # 获取每一行的数据
	# for data in row:  # 获取每一行中单元格的数据
	#     print(data.value)  # 打印单元格的值

    print(f'1:{row[0].value}	2:{row[1].value}	3:{row[2].value}')
