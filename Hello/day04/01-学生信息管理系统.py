'''

必须使用自定义函数，完成对程序的模块化
学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询、退出
'''

# 所有类继承于Object

class studentInfo(object):
    # __init__(self) 初始化方法-->构造器
    def __init__(self):
        #self.当前类的属性
        self.studentList = []
    # 存储列表
    studentList = []
    # 2.添加
    def add(self):
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        number = input("请输入学号：")
        # 存储到字典
        studentDict = {}
        studentDict["name"] = name
        studentDict["age"] = age
        studentDict["number"] = number
        # 存储到列表中
        self.studentList.append(studentDict)
        # 查询打印
        self.printInfo()

    # 3.查询打印
    def printInfo(self):
        for i in range(len(self.studentList)):
            student = self.studentList[i]
            print("%d: %s" % (i, student))

    # 4. 删除
    def delete(self):
        # 打印
        self.printInfo()
        # 获取下标
        num = int(input("请输入下标编号："))
        # 删除
        del self.studentList[num]
        # 打印
        self.printInfo()

    # 5. 修改
    def update(self):
        # 打印
        self.printInfo()
        # 获取下标和修改的信息
        name = input("请修改姓名：")
        age = input("请修改年龄：")
        number = input("请修改学号：")
        num = int(input("请输入下标编号："))
        # 修改
        self.studentList[num]["name"] = name
        self.studentList[num]["age"] = age
        self.studentList[num]["number"] = number
        # 打印
        self.printInfo()

    # 1.选项菜单
    def menu(self):
        print("=="* 20)
        print("1.添加")
        print("2.删除")
        print("3.修改")
        print("4.查询")
        print("5.退出")
        print("=="* 20)

    # main 函数 self 当前类对象
    def main(self):
        # 2.死循环
       while True:
           # 3.调用菜单选项
            self.menu()
           # 4.接受命令
            num = int(input("请输入选项："))
            # 5. 判断
            if num == 1:#添加
                self.add()
            elif num == 2:
                self.delete()
            elif num == 3:
                self.update()
            elif num == 4:
                self.printInfo()
            elif num == 5:
                print("退出成功！")
                break
            else:
                print("您输入有误，请重输：")


if __name__ == '__main__':
     st = studentInfo()
     st.main()