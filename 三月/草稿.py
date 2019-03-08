from pymysql import *
from redis import *
import hashlib

for i in range(1000):
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
            breakpoint


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
                    car()
                else:
                    print('密码错误')



        except Exception as e:
            print(e)


    def mysql_login(username, upwd):
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='me', charset='utf8')

            cs1 = conn.cursor()
            r = cs1.execute('select upwd from users where username="{}"'.format(username))
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
                    car()
                else:
                    print('密码错误')


        except Exception as e:
            print(e)

    ###
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
            pass
        elif a == '5':
            print("退出系统")

    ###
    def one():
        name = input('请输入车辆名称:')
        money = input('请输入价格:')
        address = input('请输入生产地址：')
        try:

            conn = connect(host='localhost', port=3306, user='root', password='123', database='me', charset='utf8')

            cs1 = conn.cursor()
            cs1.execute('insert into car_name values(0,"{}")'.format(name))

            cs1 = conn.cursor()
            cs1.execute('insert into car_money values(0,"{}")'.format(money))

            cs1 = conn.cursor()
            cs1.execute('insert into car_address values(0,"{}")'.format(address))


            conn.commit()
            print('录入成功!!!')
        except Exception as e:
            print(e)

    def two():
        pass



    def three():
        s_name= input('请输入车辆名称:')
        try:
            conn = connect(host='localhost', port=3306, user='root', password='123', database='me', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()
            # 执行select语句，并返回受影响的行数：查询一条数据
            count = cs1.execute('select sid from car_name where a_name="{}"'.format(s_name))
            a = cs1.fetchone()
            a = a[0]
            print("生产地址为:", a)

            coun1 = cs1.execute('select a_name from car_name where sid="{}"'.format(count))
            a = cs1.fetchone()
            a = a[0]
            print("生产地址为:",a)

            cs1 = conn.cursor()
            coun2 = cs1.execute('select money from car_money where s_id="{}"'.format(count))
            a = cs1.fetchone()
            a = a[0]
            print("生产地址为:",a)

            cs1 = conn.cursor()
            coun3 = cs1.execute('select address from car_address where n_id="{}"'.format(count))

            a = cs1.fetchone()
            a = a[0]
            print("生产地址为:",a)
            conn.commit()

            cs1.close()
            conn.close()
        except Exception as e:
            print(e)





    if __name__ == '__main__':
        main()