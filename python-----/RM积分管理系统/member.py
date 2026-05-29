class Member:
    _next_id = 1

    def __init__(self, name, group):
        self.member_id = f"RM{Member._next_id:04d}"
        self.name = name
        self.group = group
        self.points = 0
        Member._next_id += 1

    def __str__(self):
        return f"编号: {self.member_id} | 姓名: {self.name} | 组别: {self.group} | 积分: {self.points}"
