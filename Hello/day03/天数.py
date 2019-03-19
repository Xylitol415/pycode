# 1. 接收年月日
date = input("请输入日期:")
# 2. 切分年月日
year = int(date[0: 4: 1])
month = int(date[4: 6])
day = int(date[6: 8])
# 用  \ 作为代码换行连接符
#print("%s %s %s" % \
#      (year, month \
#          , day))
# 3. 处理月份，将月份天数存在list中
daysNum = 0
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 4. 如果是闰年，2月改为29天
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            months[1] = 29
# 5. 累加月份天数
for i in range(month - 1):
    daysNum += months[i]
daysNum += day
print("天数：", daysNum)
