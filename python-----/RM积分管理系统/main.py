"""
RoboMaster 队员积分管理系统 - 主程序入口
该模块提供了命令行菜单界面，用于管理队员积分
"""

from manager import MemberManager  # 导入队员管理类


def menu():
    """
    显示系统菜单
    
    打印系统的功能菜单，供用户选择操作
    """
    print("\n" + "=" * 50)
    print("       RoboMaster 队员积分管理系统")
    print("=" * 50)
    print("1. 添加队员")
    print("2. 查看所有队员")
    print("3. 为队员加分")
    print("4. 为队员扣分")
    print("5. 按积分排名")
    print("6. 删除队员")
    print("7. 退出系统")
    print("=" * 50)


def main():
    """
    主函数：程序入口点
    
    实现系统的主循环，处理用户输入并调用相应的功能
    
    功能说明:
        - 创建队员管理器实例
        - 循环显示菜单并获取用户选择
        - 根据用户选择执行相应操作
        - 对用户输入进行合法性检查
    """
    # 创建队员管理器实例
    manager = MemberManager()

    # 主循环：持续运行直到用户选择退出
    while True:
        # 显示菜单
        menu()
        
        # 获取用户输入
        choose = input("请选择操作（1-7）：")

        # 检查输入是否为数字
        if not choose.isdigit():
            print("输入无效，请输入数字 1-7")
            continue  # 跳过本次循环，重新显示菜单

        # 将字符串转换为整数
        choose = int(choose)

        # 根据用户选择执行相应操作
        if choose == 1:
            # 功能1：添加队员
            name = input("请输入队员姓名：")
            
            # 检查姓名是否为空
            if not name.strip():
                print("姓名不能为空")
                continue  # 跳过本次循环
            
            # 获取队员组别
            group = input("请输入组别（视觉/电控/机械/运营）：")
            
            # 定义有效的组别列表
            valid_groups = ["视觉", "电控", "机械", "运营"]
            
            # 检查组别是否有效
            if group not in valid_groups:
                print(f"组别无效，可选：{', '.join(valid_groups)}")
                continue  # 跳过本次循环
            
            # 添加队员并获取新创建的队员对象
            member = manager.add_member(name, group)
            
            # 显示添加成功信息
            print(f"队员 {member.name} 添加成功，编号：{member.member_id}")

        elif choose == 2:
            # 功能2：查看所有队员
            manager.view_all_members()

        elif choose == 3:
            # 功能3：为队员加分
            member_id = input("请输入队员编号：")
            points_str = input("请输入加分分数：")
            
            # 检查分数是否为正整数
            if not points_str.isdigit() or int(points_str) <= 0:
                print("分数必须为正整数")
                continue  # 跳过本次循环
            
            # 调用加分方法
            manager.add_points(member_id, int(points_str))

        elif choose == 4:
            # 功能4：为队员扣分
            member_id = input("请输入队员编号：")
            points_str = input("请输入扣分分数：")
            
            # 检查分数是否为正整数
            if not points_str.isdigit() or int(points_str) <= 0:
                print("分数必须为正整数")
                continue  # 跳过本次循环
            
            # 调用扣分方法
            manager.deduct_points(member_id, int(points_str))

        elif choose == 5:
            # 功能5：按积分排名
            manager.rank_by_points()

        elif choose == 6:
            # 功能6：删除队员
            member_id = input("请输入队员编号：")
            
            # 调用删除方法
            manager.delete_member(member_id)

        elif choose == 7:
            # 功能7：退出系统
            print("感谢使用，再见！")
            break  # 跳出主循环，结束程序

        else:
            # 无效选择
            print("输入无效，请输入 1-7 之间的数字")


# 程序入口点
# 当直接运行此文件时，调用 main() 函数
# 当作为模块导入时，不会执行 main() 函数
if __name__ == '__main__':
    main()
