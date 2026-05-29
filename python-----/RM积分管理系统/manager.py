from member import Member


class MemberManager:
    def __init__(self):
        self.members = []

    def add_member(self, name, group):
        member = Member(name, group)
        self.members.append(member)
        return member

    def view_all_members(self):
        if not self.members:
            print("暂无队员信息")
            return
        print(f"{'编号':<10}{'姓名':<10}{'组别':<10}{'积分':<10}")
        print("-" * 40)
        for member in self.members:
            print(f"{member.member_id:<10}{member.name:<10}{member.group:<10}{member.points:<10}")

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def add_points(self, member_id, points):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("未找到该队员")
            return False
        member.points += points
        print(f"已为 {member.name} 增加 {points} 分，当前积分: {member.points}")
        return True

    def deduct_points(self, member_id, points):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("未找到该队员")
            return False
        member.points -= points
        print(f"已为 {member.name} 扣除 {points} 分，当前积分: {member.points}")
        return True

    def rank_by_points(self):
        if not self.members:
            print("暂无队员信息")
            return
        sorted_members = sorted(self.members, key=lambda m: m.points, reverse=True)
        print("\n===== 积分排名 =====")
        print(f"{'排名':<6}{'编号':<10}{'姓名':<10}{'组别':<10}{'积分':<10}")
        print("-" * 46)
        for rank, member in enumerate(sorted_members, 1):
            print(f"{rank:<6}{member.member_id:<10}{member.name:<10}{member.group:<10}{member.points:<10}")

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("未找到该队员")
            return False
        confirm = input(f"确认删除队员 {member.name}（{member.member_id}）？(y/n): ")
        if confirm.lower() == 'y':
            self.members.remove(member)
            print(f"已删除队员 {member.name}")
            return True
        else:
            print("取消删除")
            return False
