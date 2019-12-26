"""
用户身份验证
"""
username = input("请输入用户名：")
password = input("请输入密码：")
if username == 'admin' and password == '123456':
    print('身份验证通过')
else:
    print('身份验证失败')