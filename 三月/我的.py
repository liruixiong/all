from pymysql import *
from redis import *
import hashlib

while True:
    def main():
        print("1.注册新用户")
        print("2.登录系统")
        print("3.删除用户")
        print("4.退出")
        a = input("请输入要使用的功能：")
        if a == '1':
            register()
        elif a == '2':
            redis_login()
        elif a == '3':
            dele()
        else:
            print("退出系统")
            exit()



    def dele():
        s_name = input('请输入用户名:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
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

            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')

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
                    car()

                else:
                    print('密码误')



        except Exception as e:
            print(e)


    def mysql_login(username, upwd):
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')

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
                    car()

                else:
                    print('密码错误')


        except Exception as e:
            print(e)


    def car():
        print("1.录入车辆")
        print("2.删除车辆")
        print("3.查询信息")
        print("4.修改信息")
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
            print("退出系统")
            connect


    def one():
        name = input("请输入车主名字：")
        car = input("请输入车的品牌：")
        money = input("请输入价格:")
        address = input("请输入车辆的生产地址：")
        years = input("请输入质保几年：")
        try:

            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')

            cs1 = conn.cursor()
            cs1.execute('insert into me values(0,"{}","{}","{}","{}","{}")'.format(name, car, money, address, years))
            conn.commit()
            print('录入成功!!!')
            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    def two():
        s_name = input('请输入车主:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()
            # 执行select语句，并返回受影响的行数：查询一条数据

            count = cs1.execute('delete from me where name="{}"'.format(s_name))
            # 打印受影响的行数
            print("查询到%d条数据:" % count)
            print('删除成功!!!')

            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    def three():
        s_name = input('请输入车主:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()
            # 执行select语句，并返回受影响的行数：查询一条数据

            count = cs1.execute('select * from me where name="{}"'.format(s_name))
            # 打印受影响的行数
            print("查询到%d条数据:" % count)

            for i in range(count):
                # 获取查询的结果
                result = cs1.fetchone()
                # 打印查询的结果
                print(result)
            # 获取查询的结果
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    def four():
        print("1.修改车主名字")
        print("2.修改车的品牌")
        print("3.修改价格")
        print("4.修改车辆的生产地址")
        print("5.修改质保年份")
        a = input("请输入要使用的功能：")

        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='lrx', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()

            if a == '1':
                name = input("请输入车主名：")
                s_name = input("请输入新的名字：")
                count = cs1.execute('update me set name="{}" where name="{}"'.format(s_name, name))
                print("修改成功！！！")
            elif a == '2':
                car = input("请输入原品牌：")
                s_car = input("请输入新品牌：")
                count = cs1.execute('update me set car="{}" where car="{}"'.format(s_car, car))
                print("修改成功！！！")
            elif a == '3':
                moner = input("请输入原价格：")
                s_moner = input("请输入新的价格：")
                count = cs1.execute('update me set money="{}" where money="{}"'.format(s_moner, moner))
                print("修改成功！！！")
            elif a == '4':
                address = input("请输入原生产地址：")
                s_address = input("请输入新的生产地址：")
                count = cs1.execute('update me set address="{}" where address="{}"'.format(s_address, address))
                print("修改成功！！！")
            elif a == '5':
                years = input("请输入原保质期：")
                s_years = input("请输入新的保质期：")
                count = cs1.execute('update me set years="{}" where years="{}"'.format(s_years, years))
                print("修改成功！！！")

            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)


    if __name__ == '__main__':
        main()
