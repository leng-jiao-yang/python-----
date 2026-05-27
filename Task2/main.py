from member_manager import MemberManager


def show_menu():
    print("=" * 40)
    print("   RoboMaster 队员积分管理系统")
    print("=" * 40)
    print("  1. 添加队员")
    print("  2. 查看所有队员")
    print("  3. 队员加分")
    print("  4. 队员扣分")
    print("  5. 积分排名")
    print("  6. 删除队员")
    print("  7. 退出系统")
    print("-" * 40)
    print("  8. 搜索队员")
    print("  9. 修改队员信息")
    print(" 10. 数据统计")
    print("=" * 40)


def main():
    manager = MemberManager()
    while True:
        show_menu()
        choice = input("请输入选项编号: ").strip()
        if choice == "1":
            manager.add_member()
        elif choice == "2":
            manager.list_members()
        elif choice == "3":
            manager.add_score()
        elif choice == "4":
            manager.deduct_score()
        elif choice == "5":
            manager.rank_members()
        elif choice == "6":
            manager.delete_member()
        elif choice == "7":
            print("感谢使用，再见！")
            break
        elif choice == "8":
            manager.search_member()
        elif choice == "9":
            manager.modify_member()
        elif choice == "10":
            manager.statistics()
        else:
            print("无效选项，请输入 1-10 的编号！")
        print()


if __name__ == "__main__":
    main()
