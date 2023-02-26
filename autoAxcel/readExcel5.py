# 导入所需的模块
import pandas as pd

# 读取excel文件，假设文件名为data.xlsx
df = pd.read_excel('测试表模板.xlsx')

# 填充合并单元格中的NaN值
df = df.fillna(method='ffill', axis=0)

# 将数据框转换为HTML表格
table = df.to_html()

# 打印或保存HTML表格
print(table)

# 打开一个新的HTML文件，假设文件名为result.html
f = open('测试表模板.html', 'w')

# 写入HTML表格
f.write(table)

# 关闭文件
f.close()