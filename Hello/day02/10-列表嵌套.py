'''
10-列表嵌套
'''
school = ["安庆师范大学",
          ["安庆师范中学", "安庆师范小学"],
          "安徽工业大学",
          ["安徽工业中学", "安徽工业小学"]
          ]

# for 嵌套循环
# 如果只有一个元素，按照字符串形式找长度
# 列表 --> 按照元素数量来找
for sh in school:
    if len(sh) != 6:
        for s in sh:
            print(s)
    else:
        print(sh)

