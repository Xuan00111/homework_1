# student.py
import os


class Student:
    """学生实体类，用于存储和管理单个学生的信息"""

    def __init__(self, serial_num, name, gender, class_num, student_id, college):
        self.serial_num = serial_num  # 序号
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.class_num = class_num  # 班级
        self.student_id = student_id  # 学号
        self.college = college  # 学院

    def __str__(self):
        # 方便打印测试学生信息
        return f"学号:{self.student_id} | 姓名:{self.name} | 性别:{self.gender} | 班级:{self.class_num}班 | 学院:{self.college}"


def load_students(filepath="人工智能编程语言学生名单.txt"):
    """
    功能函数：读取学生信息
    从指定的txt文件中读取数据，跳过表头，并将每一行转化为Student对象。
    返回一个包含所有Student对象的列表。
    """
    student_list = []

    # 检查文件是否存在
    if not os.path.exists(filepath):
        print(f"警告：未找到文件 '{filepath}'！请确保文件在项目根目录下。")
        return student_list

    try:
        # 推荐使用 utf-8 编码，如果你的txt是GBK编码，请将 encoding='utf-8' 改为 encoding='gbk'
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # 如果文件为空，直接返回空列表
            if not lines:
                return student_list

            # lines[1:] 用于跳过第一行的表头 (序号 姓名 性别 班级 学号 学院)
            for line in lines[1:]:
                # strip() 去除首尾换行符/空格，split() 默认按空格或制表符(Tab)分割
                data = line.strip().split()

                # 确保读取的数据是完整的（6个字段）
                if len(data) == 6:
                    # 使用解包操作将列表元素按顺序传入 Student 的构造函数
                    student = Student(*data)
                    student_list.append(student)

        print(f"成功加载 {len(student_list)} 名学生信息！")

    except Exception as e:
        print(f"读取学生信息时发生错误: {e}")

    return student_list
