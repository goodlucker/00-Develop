import zipfile

# 请替换为你的 ZIP 文件路径
zip_file_path = 'D:\\CRM-L460\\D-disk\\98_App\\python\\00_develop\\explain_pw\\xyz.zip'

# 创建一个密码列表，包含需要尝试的密码
passwords = ['1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+']

for password in passwords:
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f'Success! Password is: {password}')
        break  # 如果成功解锁，退出循环
    except Exception as e:
        print(f'Password {password} failed. Error: {e}')