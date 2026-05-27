from member import Member


class MemberManager:
    VALID_GROUPS = ["视觉", "电控", "机械", "运营"]

    def __init__(self):
        self.members = []

    def _find_by_id(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def _find_by_name(self, name):
        for m in self.members:
            if m.name == name:
                return m
        return None

    def add_member(self):
        name = input("请输入队员姓名: ").strip()
        if not name:
            print("姓名不能为空！")
            return
        if self._find_by_name(name):
            print(f"队员 \"{name}\" 已存在，禁止重复添加！")
            return
        print(f"可选组别: {', '.join(self.VALID_GROUPS)}")
        group = input("请输入组别: ").strip()
        if group not in self.VALID_GROUPS:
            print(f"组别无效！请输入以下之一: {', '.join(self.VALID_GROUPS)}")
            return
        member = Member(name, group)
        self.members.append(member)
        print(f"队员 \"{name}\" 添加成功！编号: {member.member_id}")

    def list_members(self):
        if not self.members:
            print("暂无队员信息。")
            return
        print(f"\n{'编号':<10}{'姓名':<12}{'组别':<10}{'积分':<8}")
        print("-" * 40)
        for m in self.members:
            print(f"{m.member_id:<10}{m.name:<12}{m.group:<10}{m.score:<8}")
        print()

    def add_score(self):
        member_id = input("请输入队员编号: ").strip().upper()
        member = self._find_by_id(member_id)
        if not member:
            print("编号不存在！")
            return
        try:
            points = int(input("请输入加分分值: "))
        except ValueError:
            print("请输入有效的整数！")
            return
        if points <= 0:
            print("加分分值必须为正整数！")
            return
        member.score += points
        print(f"队员 \"{member.name}\" 加 {points} 分，当前积分: {member.score}")

    def deduct_score(self):
        member_id = input("请输入队员编号: ").strip().upper()
        member = self._find_by_id(member_id)
        if not member:
            print("编号不存在！")
            return
        try:
            points = int(input("请输入扣分分值: "))
        except ValueError:
            print("请输入有效的整数！")
            return
        if points <= 0:
            print("扣分分值必须为正整数！")
            return
        member.score -= points
        print(f"队员 \"{member.name}\" 扣 {points} 分，当前积分: {member.score}")

    def rank_members(self):
        if not self.members:
            print("暂无队员信息。")
            return
        sorted_members = sorted(self.members, key=lambda m: m.score, reverse=True)
        print(f"\n{'排名':<6}{'编号':<10}{'姓名':<12}{'组别':<10}{'积分':<8}")
        print("-" * 46)
        for i, m in enumerate(sorted_members, 1):
            print(f"{i:<6}{m.member_id:<10}{m.name:<12}{m.group:<10}{m.score:<8}")
        print()

    def delete_member(self):
        member_id = input("请输入要删除的队员编号: ").strip().upper()
        member = self._find_by_id(member_id)
        if not member:
            print("编号不存在！")
            return
        confirm = input(f"确认删除队员 \"{member.name}\" ({member.member_id})？(y/n): ").strip().lower()
        if confirm == "y":
            self.members.remove(member)
            print(f"队员 \"{member.name}\" 已删除。")
        else:
            print("已取消删除。")

    def search_member(self):
        keyword = input("请输入搜索关键词（姓名或组别）: ").strip()
        if not keyword:
            print("关键词不能为空！")
            return
        results = [m for m in self.members
                   if keyword in m.name or keyword in m.group]
        if not results:
            print("未找到匹配的队员。")
            return
        print(f"\n{'编号':<10}{'姓名':<12}{'组别':<10}{'积分':<8}")
        print("-" * 40)
        for m in results:
            print(f"{m.member_id:<10}{m.name:<12}{m.group:<10}{m.score:<8}")
        print()

    def modify_member(self):
        member_id = input("请输入要修改的队员编号: ").strip().upper()
        member = self._find_by_id(member_id)
        if not member:
            print("编号不存在！")
            return
        print(f"当前信息: {member}")
        print("1. 修改姓名  2. 修改组别")
        choice = input("请选择修改项: ").strip()
        if choice == "1":
            new_name = input("请输入新姓名: ").strip()
            if not new_name:
                print("姓名不能为空！")
                return
            existing = self._find_by_name(new_name)
            if existing and existing.member_id != member_id:
                print(f"姓名 \"{new_name}\" 已被其他队员使用！")
                return
            old_name = member.name
            member.name = new_name
            print(f"姓名已从 \"{old_name}\" 修改为 \"{new_name}\"")
        elif choice == "2":
            print(f"可选组别: {', '.join(self.VALID_GROUPS)}")
            new_group = input("请输入新组别: ").strip()
            if new_group not in self.VALID_GROUPS:
                print(f"组别无效！请输入以下之一: {', '.join(self.VALID_GROUPS)}")
                return
            old_group = member.group
            member.group = new_group
            print(f"组别已从 \"{old_group}\" 修改为 \"{new_group}\"")
        else:
            print("无效选项！")

    def statistics(self):
        if not self.members:
            print("暂无队员信息。")
            return
        print(f"\n{'组别':<8}{'人数':<8}{'平均积分':<10}{'最高积分':<10}{'最低积分':<10}")
        print("-" * 46)
        for group in self.VALID_GROUPS:
            group_members = [m for m in self.members if m.group == group]
            if not group_members:
                print(f"{group:<8}{'0':<8}{'-':<10}{'-':<10}{'-':<10}")
            else:
                count = len(group_members)
                avg = sum(m.score for m in group_members) / count
                max_s = max(m.score for m in group_members)
                min_s = min(m.score for m in group_members)
                print(f"{group:<8}{count:<8}{avg:<10.1f}{max_s:<10}{min_s:<10}")
        total = len(self.members)
        total_avg = sum(m.score for m in self.members) / total
        total_max = max(m.score for m in self.members)
        total_min = min(m.score for m in self.members)
        print("-" * 46)
        print(f"{'合计':<8}{total:<8}{total_avg:<10.1f}{total_max:<10}{total_min:<10}")
        print()
