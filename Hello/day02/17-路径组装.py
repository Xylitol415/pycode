paths = []
while True:
    # 1.获得用户输入的路经
    path= input("请输入路经地址:")
    # 2.存储到列表中
    paths.append(path)
    print(paths)
    # 3.join
    st = '/'
    #4.打印
    print(st.join(paths))
