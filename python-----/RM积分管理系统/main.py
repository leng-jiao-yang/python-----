from manager import MemberManager


def menu():
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
    manager = MemberManager()

    while True:
        menu()
        choose = input("请选择操作（1-7）：")

        if not choose.isdigit():
            print("输入无效，请输入数字 1-7")
            continue

        choose = int(choose)

        if choose == 1:
            name = input("请输入队员姓名：")
            if not name.strip():
                print("姓名不能为空")
                continue
            group = input("请输入组别（视觉/电控/机械/运营）：")
            valid_groups = ["视觉", "电控", "机械", "运营"]
            if group not in valid_groups:
                print(f"组别无效，可选：{', '.join(valid_groups)}")
                continue
            member = manager.add_member(name, group)
            print(f"队员 {member.name} 添加成功，编号：{member.member_id}")

        elif choose == 2:
            manager.view_all_members()

        elif choose == 3:
            member_id = input("请输入队员编号：")
            points_str = input("请输入加分分数：")
            if not points_str.isdigit() or int(points_str) <= 0:
                print("分数必须为正整数")
                continue
            manager.add_points(member_id, int(points_str))

        elif choose == 4:
            member_id = input("请输入队员编号：")
            points_str = input("请输入扣分分数：")
            if not points_str.isdigit() or int(points_str) <= 0:
                print("分数必须为正整数")
                continue
            manager.deduct_points(member_id, int(points_str))

        elif choose == 5:
            manager.rank_by_points()

        elif choose == 6:
            member_id = input("请输入队员编号：")
            manager.delete_member(member_id)

        elif choose == 7:
            print("感谢使用，再见！")
            break

        else:
            print("输入无效，请输入 1-7 之间的数字")


if __name__ == '__main__':
    main()
