from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 初始化
result = ocr.ocr("D:\AAP\\test.png", cls=True)  # 预测
for line in result[0]:
    print("提取内容")
    print(line[1][0])  # 提取文本
