import itertools as its
import rarfile

path1 = "D:\\CRM-L460\\D-disk\\98_App\\python\\00_develop\\explain_pw\\explain_pw.rar"
path2 = "D:\\CRM-L460\\D-disk\\98_App\\python\\00_develop\\explain_pw\\test"

words = "1234567890Cr*med"    ##密码里面含有大小写字母，数字以及特殊符号

max_attempts = 10000  # 最大尝试次数

re = 9  # 初始密码长度

while True:
    r = its.product(words, repeat=re)
    attempts = 0
    for i in r:
        password = "".join(i)
        print("当前测试密码:", password)

        try:
            with rarfile.RarFile(path1) as rf:
                rf.extractall(path=path2, pwd=password)
            print('密码破解成功:', password)
            exit(0)
        except Exception as e:
            print(e)
            attempts += 1
            if attempts >= max_attempts:
                break
    else:
        re += 1
