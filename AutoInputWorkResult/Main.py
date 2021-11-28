from ConvertData import convertjisseki
from WebControl import InputJisseki

# 取り込むEXCELファイルのパス
ImpExcelPath = r"C:\Users\xxxx\Desktop\jisseki.xlsx"

# シート名の指定(年月)
ImpSheetName = "201907"


df = convertjisseki(ImpExcelPath,ImpSheetName)

InputJisseki(df)

