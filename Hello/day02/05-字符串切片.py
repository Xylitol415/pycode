'''
05-字符串切片
# [起始：结束：步长] 步长没写，默认为1
# 左闭右开原则
'''
name = '安庆市宜秀区大龙山镇集贤北路1318号'
names1 = name[3:6:1]
print("区名：", names1)
# 2到最后
names2 = name[2:]
print(names2)
# [1:-1] 1到倒数第二位
names3 = name[1:-1]
print(names3)
