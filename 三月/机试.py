from pymysql import *
from redis import *
import hashlib
h = '2' or '4'
while True:
    def main():
        print("1.注册新用户")
        print("2.登录系统")
        print("3.删除用户")
        print("4.用户登录")
        print("5.退出")
        a = input("请输入要使用的功能：")
        if a == '1':
            register()
        elif a == '2' or '4':
            redis_login()
        elif a == '3':
            dele()
        else:
            print("退出系统")
            exit()


    def dele():
        s_name = input('请输入用户名:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='jishi', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()
            # 执行select语句，并返回受影响的行数：查询一条数据

            count = cs1.execute('delete from users where username="{}"'.format(s_name))
            # 打印受影响的行数
            print("查询到%d条数据:" % count)
            print('删除成功!!!')

            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    def register():
        username = input('请输入账号:')
        password = input('请输入密码:')

        s1 = hashlib.sha1()

        s1.update(password.encode('utf8'))

        upwd = s1.hexdigest()
        print("注册成功！！！")

        print('你的账号是：{},你的密码是：{}'.format(username, upwd))

        try:

            conn = connect(host='localhost', port=3306, user='root', password='123', database='jishi', charset='utf8')

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
                    if h == '2':
                        car()
                    elif h == '4':
                        mone()

                else:
                    print('密码误')



        except Exception as e:
            print(e)


    def mysql_login(username, upwd):
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='jishi', charset='utf8')

            cs1 = conn.cursor()
            count = cs1.execute('select upwd from users where username="{}"'.format(username))
            if count == None:
                print('请去注册')

            else:
                a = cs1.fetchone()
                a = a[0]
                if upwd == a:

                    sr = StrictRedis(decode_responses=True)
                    sr.set(username, upwd)
                    print('登录成功')
                    if h == '2':
                        car()
                    elif h == '4':
                        mone()

                else:
                    print('密码错误')

        except Exception as e:
            print(e)

    def mone():
        name = input("请输入你的名字：")
        years = input("请选择服务项目 美容.美发或美体：")
        money = input("请输入价位:")

        try:

            conn = connect(host='localhost', port=3306, user='root', password='123', database='jishi', charset='utf8')

            cs1 = conn.cursor()
            cs1.execute('insert into me values(0,"{}","{}","{}")'.format(name, money, years))
            conn.commit()
            print('录入成功!!!')
            cs1.close()
            conn.close()
        except Exception as e:
            print(e)

    def car():
        print("管理员系统")
        print("1.查询总消费金额")
        print("2.查询平均消费金额")
        print("3.查询最高消费金额")
        print("4.查询最低消费金额")
        print("5.查询指定用户")
        print("5.退出")
        a = input("请输入要使用的功能：")
        if a == '1':
            one()
        elif a == '2':
            two()
        elif a == '3':
            three()
        elif a == '4':
            four()
        elif a == '5':
            five()
        elif a == '6':
            print("退出系统")
            connect
    def one():
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            cs1 = conn.cursor()
            count = cs1.execute('select avg(money) from me')
            print("查询到%d条数据:" % count)

            for i in range(count):
                result = cs1.fetchone()
                print(result)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)

    def two():
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            cs1 = conn.cursor()
            count = cs1.execute('select sum(money) from me')
            print("查询到%d条数据:" % count)

            for i in range(count):
                result = cs1.fetchone()
                print(result)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)
    def three():
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            cs1 = conn.cursor()
            count = cs1.execute('select max(money) from me')
            print("查询到%d条数据:" % count)

            for i in range(count):
                result = cs1.fetchone()
                print(result)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)

    def four():
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            cs1 = conn.cursor()
            count = cs1.execute('select min(money) from me')
            print("查询到%d条数据:" % count)

            for i in range(count):
                result = cs1.fetchone()
                print(result)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)

    def five():
        s_name = input('请输入用户名:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            cs1 = conn.cursor()
            count = cs1.execute('select * from me where name="{}"'.format(s_name))
            print("查询到%d条数据:" % count)

            for i in range(count):
                result = cs1.fetchone()
                print(result)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    if __name__ == '__main__':
        main()
