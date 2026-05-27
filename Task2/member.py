class Member:
    next_id = 1

    def __init__(self, name, group):
        self.member_id = f"RM{Member.next_id:04d}"
        Member.next_id += 1
        self.name = name
        self.group = group
        self.score = 0

    def __str__(self):
        return (f"编号: {self.member_id} | 姓名: {self.name} | "
                f"组别: {self.group} | 积分: {self.score}")
