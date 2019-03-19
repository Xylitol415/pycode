
account = "admin"
pwd = 123456

while True:
    print("="*30)
    print("欢迎进入到身份认证系统V1.0")
    print("        1.登录         ")
    print("        2.退出         ")
    print("        3.认证        ")
    print("        4.修改密码         ")
    print("="*30)

    opt = input("输入命令:")
    opt = int(opt)
    if opt == 1:
        InputAccount = input("请输入用户名:")
        InputPwd = input("请输入密码:")
        InputPwd = int(InputPwd)
        if InputAccount == account and InputPwd == pwd:
            print("登录成功！")
        else:
            print("登录失败！")
    elif opt == 2:
        print("退出了。。。")
        break
    elif opt == 3:
        print("认证成功！")
    elif opt == 4:
        ResetPwd = input("输入要修改的密码:")
        pwd = int(ResetPwd)
        print("修改成功！")
    else:
        break



