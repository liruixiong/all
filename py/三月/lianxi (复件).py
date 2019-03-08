from pymysql import *
from redis import *
import hashlib


def main():
    print("1.注册")
    print("2.登录")
    print("3.退出")
    a = input("请输入要使用的功能：")
    if a == '1':
        register()
    elif a == '2':
        redis_login()
    elif a == '3':
        print("退出系统")


def register():
    username = input('请输入账号:')
    password = input('请输入密码:')

    s1 = hashlib.sha1()

    s1.update(password.encode('utf8'))

    upwd = s1.hexdigest()

    print(username, upwd)

    try:

        conn = connect(host='localhost', port=3306, user='root', password='123', database='me', charset='utf8')

        cs1 = conn.cursor()

        cs1.execute('insert into users values(0,"{}","{}")'.format(username, upwd))

        conn.commit()
    except Exception as e:
        print(e)


def redis_login():
    username = input('请输入用户名:')
    password = input('请输入密码:')

    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))

    upwd = s1.hexdigest()

    try:

        sr = StrictRedis(decode_responses=True)

        r = sr.get(username)
        if r == None:

            mysql_login(username, upwd)
        else:

            if upwd == r:
                print('登录成功')
            else:
                print('密码错误')



    except Exception as e:
        print(e)


def mysql_login(username, upwd):
    try:
        conn = connect(host='localhost', port=3306, user='root', password='123', database='me', charset='utf8')

        cs1 = conn.cursor()
        r = cs1.execute('select upwd from users where name="{}"'.format(username))
        a = cs1.fetchone()
        a = a[0]
        print(a)

        if r == None:

            print('请去注册')
        else:
            if upwd == a:

                sr = StrictRedis(decode_responses=True)
                sr.set(username, upwd)
                print('登录成功')
            else:
                print('密码错误')


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
