import itertools as its
import getpass
from libpff import file

path_to_pst_file = "D:\CRM-L460\D-disk\98_App\python\00_develop\explain_pw\2022-07-28_康龙邮箱__backip.pst"  # PST 文件路径
password_charset = "1234567890Cr*med"  # 密码字符集合
max_attempts = 10000  # 最大尝试次数
min_password_length = 9  # 最小密码长度
max_password_length = 10  # 最大密码长度

# 尝试不同长度的密码
for password_length in range(min_password_length, max_password_length + 1):
    # 生成所有可能的密码组合
    passwords = its.product(password_charset, repeat=password_length)
    
    # 尝试每个密码
    for password in passwords:
        password_str = "".join(password)
        print("当前测试密码:", password_str)
        
        try:
            # 使用密码尝试打开 PST 文件
            with file.PSTFile(path_to_pst_file, password=password_str) as pst_file:
                # 如果成功打开，打印密码并退出循环
                print("密码破解成功:", password_str)
                exit(0)
        except Exception as e:
            # 如果密码错误，继续尝试下一个密码
            print("密码错误:", password_str)
            continue
