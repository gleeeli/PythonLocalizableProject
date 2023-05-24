
#coding=gbk

import openpyxl


from openpyxl import load_workbook

# MineModule  LoginModule  PostModule MessageCenterModule MomentModule MineSetModule ConfigModule MessageListModule GoFishingModule SecretStoryModule
# ['个人中心', '登陆注册', '动态', '私信', '瞬间群', '个人设置', '通用', '消息列表', '钓鱼', '故事']

wb = load_workbook('./多语言中英文对照.xlsx')
localModuleFilePath = "files/ConfigModule.strings"

#获取工作表--Sheet
# 获得所有sheet的名称
print(str(wb.sheetnames))
# 根据sheet名字获得sheet
a_sheet = wb['通用']
# 获得sheet名
print(a_sheet.title)
# 获得当前正在显示的sheet, 也可以用wb.get_active_sheet()
sheet = wb.active
def writeFileHead():
    with open(localModuleFilePath, 'a') as file_object:
        file_object.write("/*\n " +localModuleFilePath+"\n Pods\n Created by liguanglei on 2023/3/29.\n\n*/\n\n")

def writeRowTofile(key, value):
    with open(localModuleFilePath, 'a') as file_object:
        file_object.write("\"" + key+"\" = \"" + value + "\";\n")


writeFileHead()
for row in a_sheet.values:
    key = str(row[0])
    chineseValue = str(row[1])
    chineseValue = chineseValue.replace("{count}","%s")
    yinhaoStr = "\\\""
    chineseValue = chineseValue.replace("\"", yinhaoStr)
    if key != "None" and key != "" and key != "Key值" and chineseValue != "None":
        print(key + "=" + chineseValue + "备注：" + str(row[2]))
        writeRowTofile(key, chineseValue)



