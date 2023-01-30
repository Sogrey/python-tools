# pip install openpyxl

# https://www.bilibili.com/video/BV1sg41167fA/?p=2&spm_id_from=pageDriver&vd_source=96276a0eadd5914be7e81924f0535ab3

from openpyxl import load_workbook

# 加载Excel
wb = load_workbook('202006.xlsx', read_only=True, data_only=True)

# 获取当前激活的工作簿
ws = wb['工资发放明细表']

count = 0
for row in ws.rows:  # 获取每一行的数据
	# for data in row:  # 获取每一行中单元格的数据
	#     print(data.value)  # 打印单元格的值

    if count<4:
        count+=1
        continue

    if row[3].value == None:
        break

    print(f'序号:{row[1].value}	部门:{row[2].value}	姓名:{row[3].value}	月工资标准:{row[5].value}	岗位工资:{row[6].value}	绩效工资:{row[7].value}	工龄补贴:{row[8].value}	全勤奖:{row[9].value}')
    count+=1



