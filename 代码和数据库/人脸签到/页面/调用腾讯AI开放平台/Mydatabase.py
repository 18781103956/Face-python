import pymysql
import 添加个体
import 删除个体
import datetime

def find_AllClass():
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "select * from class_table"


    try:
        cursor.execute(sql)
    except Exception as e:
        print("提示：", "查找失败！")
        connect.rollback()
    else:
        print("提示：", "查找成功！")
        result = cursor.fetchall()
        connect.commit()
        return result

    cursor.close()
    connect.close()

def find_Allstudent(class_id):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "select stu_id,stu_name,stu_sex,sign_val from student where stu_class='%s'"

    try:
        cursor.execute(sql%class_id)
    except Exception as e:
        print("提示：", "查找失败！")
        connect.rollback()
    else:
        print("提示：", "查找成功！")
        result = cursor.fetchall()
        connect.commit()
        return result

    cursor.close()
    connect.close()

def update_student(list_student, class_id):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )

    cursor = connect.cursor()  # 获取数据库游标
    sql = "UPDATE student SET sign_val='0' where stu_id!=''"
    try:
        cursor.execute(sql)
    except Exception as e:
        print("提示：", "查找失败！")
        connect.rollback()
    else:
        print("提示：", "查找成功！")
        result = cursor.fetchall()
        connect.commit()


    for item in list_student:



        sql = "UPDATE student SET sign_val='%s' where stu_id='%s'"
        data = (item[1], item[0])
        print("^^^^", data)
        print(sql % data)
        try:
            cursor.execute(sql % data)
        except Exception as e:
            print("提示：", "查找失败！")
            connect.rollback()
        else:
            print("提示：", "查找成功！")
            result = cursor.fetchall()
            connect.commit()

    cursor.close()
    connect.close()

def insert_student(stu_id, stu_name, stu_sex, stu_class):
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "INSERT INTO student(stu_id,stu_name,stu_sex,stu_class,sign_val) VALUES('%s', '%s', '%s', '%s', '%s')"
    data = (stu_id, stu_name, stu_sex, stu_class, '0')
    print(sql % data)
    try:
        cursor.execute(sql % data)

    except Exception as e:
        print("提示：", "插入失败！")

        connect.rollback()
    else:
        print("提示：", "插入成功！")
        result = cursor.fetchall()
        connect.commit()

    cursor.close()
    connect.close()

def Add_class(val):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "INSERT INTO class_table(class_no,class_sum,class_teacher) VALUES('%s', '%s', '%s')"

    try:
        cursor.execute(sql % val)
    except Exception as e:
        print("提示：", "插入失败！")

        connect.rollback()
    else:
        print("提示：", "插入成功！")
        result = cursor.fetchall()
        connect.commit()

    cursor.close()
    connect.close()

def Delete_class(val):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "Delete from class_table where class_no = '%s'"

    try:
        cursor.execute(sql % val)
    except Exception as e:
        print("提示：", "删除失败！")

        connect.rollback()
    else:
        print("提示：", "删除成功！")
        result = cursor.fetchall()
        connect.commit()

    cursor.close()
    connect.close()

def del_student(stu_id):
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "DELETE FROM student WHERE stu_id = '%s'"
    data = (stu_id)
    print(sql % data)
    try:
        cursor.execute(sql % data)

    except Exception as e:
        print("提示：", "删除失败！")

        connect.rollback()
    else:
        print("提示：", "删除成功！")
        result = cursor.fetchall()
        connect.commit()

    cursor.close()
    connect.close()

def l_data(id):
    connect = pymysql.Connect(
        host='localhost',  # MySQL服务器地址 (str)
        port=3306,  # MySQL服务器端口号 (int)
        user='root',  # 用户名 (str)
        passwd='root',  # 密码 (str)
        db='face_sign',  # 数据库名称 (str)
        charset='utf8'  # 连接编码 (str)
    )
    cursor = connect.cursor()  # 获取数据库游标

    sql = "SELECT pass_word FROM account WHERE Work_account = '%s'"
    data = (id)
    print("sss", sql % data)
    try:
        cursor.execute(sql % data)

    except Exception as e:
        print("提示：", "查找失败！")

        connect.rollback()
    else:
        print("提示：", "查找成功！")
        result = cursor.fetchall()
        connect.commit()
        return result

    cursor.close()
    connect.close()


#=================================================================================

if __name__ == '__main__':
    t = "2019-08-26 14:32:06"
    sno = "test_0"
