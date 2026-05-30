# exam.py
import random
import os


def random_roll_call(student_list):
    """
    功能4：随机点名
    输入需要点名的数量，返回对应数量的不重复随机学生名单。
    """
    total_students = len(student_list)
    if total_students == 0:
        print("当前没有任何学生数据，请先确保已加载学生信息！")
        return

    while True:
        user_input = input("请输入需要点名的学生数量: ")
        try:
            # 1. 尝试将输入转换为整数（处理非数字字符异常）
            num = int(user_input)

            # 2. 处理输入人数小于或等于0的异常
            if num <= 0:
                raise ValueError("点名人数必须大于 0！")

            # 3. 处理输入人数超过总人数的异常
            if num > total_students:
                raise ValueError(f"点名人数({num})超过了班级学生总数({total_students})！")

            # 如果以上均无异常，跳出循环
            break

        except ValueError as e:
            # 如果是 int() 转换抛出的异常，提示输入非数字
            if "invalid literal" in str(e):
                print("输入异常：请输入纯数字！\n")
            else:
                # 抛出我们自定义的异常信息
                print(f"输入异常：{e}\n")

    # random.sample 可直接获取指定数量的“不重复”随机元素
    selected_students = random.sample(student_list, num)

    print("\n本次随机点名结果：")
    for index, student in enumerate(selected_students, 1):
        print(f"{index}.{student.name} {student.student_id}")


def generate_exam_arrangement(student_list):
    """
    功能5：生成考场安排表
    随机打乱学生顺序，并输出到【考场安排表.txt】中。
    """
    if not student_list:
        print("当前没有任何学生数据！")
        return

    # 使用 copy() 防止修改原始的 student_list 列表
    shuffled_students = student_list.copy()
    # 随机打乱列表顺序
    random.shuffle(shuffled_students)

    filename = "考场安排表.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for seat_num, student in enumerate(shuffled_students, 1):
                # 写入格式：考场座位号,姓名,学号
                file.write(f"{seat_num},{student.name},{student.student_id}\n")
        print(f"\n成功生成考场安排！文件已保存为：【{filename}】")
    except Exception as e:
        print(f"\n生成考场安排表时发生错误：{e}")


def generate_admission_tickets():
    """
    功能6：打印准考证号
    根据生成的考场安排表，在“准考证”文件夹下生成每位学生的独立准考证txt文件。
    """
    arrangement_file = "考场安排表.txt"
    folder_name = "准考证"

    # 前置校验：必须先生成过考场安排表
    if not os.path.exists(arrangement_file):
        print(f"\n错误：未找到【{arrangement_file}】！请先执行功能“3.生成考场安排表”。")
        return

    try:
        # 创建文件夹：exist_ok=True 完美满足“文件夹已存在时不报错并覆盖”的要求
        os.makedirs(folder_name, exist_ok=True)

        # 读取考场安排表数据
        with open(arrangement_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        success_count = 0
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # 按逗号拆分：座位号, 姓名, 学号
            data = line.split(",")
            if len(data) == 3:
                seat_num, name, student_id = data

                # 格式化文件名：int(seat_num):02d 可将 1 转为 01，将 10 保持 10
                ticket_filename = f"{int(seat_num):02d}.txt"
                ticket_filepath = os.path.join(folder_name, ticket_filename)

                # 生成单个准考证文件
                with open(ticket_filepath, "w", encoding="utf-8") as ticket_file:
                    ticket_file.write(f"考场座位号:{seat_num}\n")
                    ticket_file.write(f"姓名:{name}\n")
                    ticket_file.write(f"学号:{student_id}\n")

                success_count += 1

        print(f"\n成功！在【{folder_name}】文件夹下生成了 {success_count} 份准考证。")

    except Exception as e:
        print(f"\n生成准考证时发生错误：{e}")