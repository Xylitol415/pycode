# {"张三": ["男","13955664321","安徽安庆"], "李四": ['女',"13805561231"]}
import sys

mps = []
while True:
    dictInfo = {}
    print("=" * 30)
    print(" " * 8, "名片管理系统v1.0")
    print(" " * 10, "1.添加名片")
    print(" " * 10, "2.删除名片")
    print(" " * 10, "3.修改名片")
    print(" " * 10, "4.查询名片")
    print(" " * 10, "5.退出系统")
    print("=" * 30)
    opt = int(input("请输入命令："))
    # 添加名片
    if opt == 1:
        newName = input("输入姓名：")
        newPhone = input("输入联系方式：")
        newAddress = input("输入地址：")
        dictInfo["Name"] = newName
        dictInfo["Phone"] = newPhone
        dictInfo["Address"] = newAddress
        mps.append(dictInfo)
        print("添加成功！")
        # 添加成功后打印
        for mp in mps:
            # print(mp)
            print("==" * 10)
            for key, value in mp.items():
                print("    %s = %s    " % (key, value))
            print("==" * 10)
            print()
    # 删除名片
    elif opt == 2:
        # 根据名片号删除
        infoId = int(input("输入要删除的名片ID号："))
        del mps[infoId]
        print("删除成功！")
    elif opt == 3:
        infoId = int(input("请输入要修改的名片ID号："))
        if infoId >= len(mps):
            print("名片不存在，请重新输入")
            continue
        else:
            newName = input("输入修改后的姓名：")
            newPhone = input("输入修改后的联系方式：")
            newAddress = input("输入修改后的地址：")
            dictInfo["Name"] = newName
            dictInfo["Phone"] = newPhone
            dictInfo["Address"] = newAddress
            mps[infoId] = dictInfo
        print("修改成功！")
    elif opt == 4:
        infoId = int(input("请输入要查找的ID号："))
        if infoId >= len(mps):
            print("名片不存在，请重新输入")
            continue
        else:
            print("查询结果如下：")
            print("==" * 10)
            for key, value in mps[infoId].items():
                print("    %s = %s    " % (key, value))
            print("==" * 10)
            print()
    elif opt == 5:
        print("您已退出系统！")
        sys.exit();
    else:
        print("输入有误，请重新输入！")
