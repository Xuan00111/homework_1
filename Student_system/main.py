# main.py
import sys
from student import load_students
import exam_system


class ExamSys:
    """学生考试信息系统控制类"""

    def __init__(self):
        # 按照要求：在__init__方法中调用load_students读取数据
        self.students = load_students("人工智能编程语言学生名单.txt")

    def query_students(self):
        """功能1：按学号查询学生信息"""
        if not self.students:
            print("当前无学生数据，请检查文件是否加载成功。")
            return

        # 对应图片：请输入要查询的学号：2001107
        search_id = input("请输入要查询的学号：").strip()

        found = False
        for stu in self.students:
            if stu.student_id == search_id:
                # 对应图片：先换行打印“查询结果：”
                print("\n查询结果：")
                # 对应图片：按特定间距输出学生信息
                print(
                    f"序号：{stu.serial_num}  姓名：{stu.name}  性别：{stu.gender}  班级：{stu.class_num}  学号：{stu.student_id}  学院：{stu.college}")
                found = True
                break

        if not found:
            print("\n查询结果：未找到该学号的学生。")

    def run(self):
        """系统功能菜单运行控制"""
        while True:
            # 严格按照要求的格式输出菜单
            print("\n===== 学生信息与考场管理系统 =====")
            print("1. 查询学生信息")
            print("2. 随机点名")
            print("3. 生成考场安排表")
            print("4. 生成准考证文件")
            print("+--------------------------------------------------------------------------")
            print("0. 退出系统")

            # 获取用户输入
            choice = input("请输入功能编号：").strip()

            # 根据功能编号调用对应的模块函数
            if choice == '1':
                self.query_students()

            elif choice == '2':
                # 调用 exam.py 中的随机点名，并传入学生列表
                exam_system.random_roll_call(self.students)

            elif choice == '3':
                # 调用 exam.py 中的生成考场安排表，并传入学生列表
                exam_system.generate_exam_arrangement(self.students)

            elif choice == '4':
                # 调用 exam.py 中的生成准考证文件功能 (该功能自行读取txt，无需传参)
                exam_system.generate_admission_tickets()

            elif choice == '0':
                print("感谢使用学生信息与考场管理系统，再见！")
                break

            else:
                # 按照要求输出边界异常友好的错误提示
                print("功能编号不存在，请正确输入功能编号（0~4）：")


# 程序启动入口
if __name__ == "__main__":
    # 实例化系统核心类
    system = ExamSys()
    # 运行系统
    system.run()