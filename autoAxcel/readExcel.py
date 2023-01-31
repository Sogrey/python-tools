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

    break

'''
<style>table{border-collapse:collapse;table-layout:fixed;border-radius:5px;overflow:hidden;margin:20px 10px;border:2px solid #70aefb;background-color:#328ef4;color:#c7dafb;box-shadow:10px 10px 10px #000;}table caption{background-color:#323232;padding:15px;font-size:24px;}table td,th{padding:10px;text-align:center;border:1px solid #70aefb;vertical-align:middle;font-size:18px;}.table-color-green{background-color:green;}.table-color-grey{background-color:#696969;}.table-color-black{background-color:black;}.jt-up-color{color:red;}.parent-position{position:relative;}.child-position{position:absolute;right:0;bottom:0;}.main-font{font-size:23px;}</style>

张三，你好：<br />
&emsp;&emsp;以下是上月绩效考核及薪资组成，请查收！<br />

<table class="">
  <caption>2023年01月 绩效考核表</caption>
  <tr>
    <td>姓名</td>
    <td>考核基数</td>
    <td>工作时间投入度</td>
    <td>产出质量</td>
    <td>按期交付能力</td>
    <td>加权累计%</td>
  </tr>
  <tr>
    <td>张三</td>
    <td>100%</td>
    <td>104%</td>
    <td>110%</td>
    <td>100%</td>
    <td>106%</td>
  </tr>
  <tr>
    <td colspan=6>制表时间：2023-02-11 15:34:24</td>
  </tr>
</table>

以上数据如有疑问，请及时反馈！
'''


