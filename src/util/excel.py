from openpyxl import load_workbook

# 加载工作簿
wb = load_workbook('D:\\AAP\\test.xlsx')

# 获取工作表
ws = wb.active  # 获取当前活动的工作表
# 或者通过工作表名称获取
# ws = wb['Sheet1']

# 读取单元格数据
cell_value = ws['A1'].value
print(cell_value)

# 遍历工作表中的所有行
for row in ws.iter_rows(values_only=True):
    print(row)


print("Hello world end.")
