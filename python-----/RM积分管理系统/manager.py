"""
队员管理类模块
该模块提供了对队员的增删改查和积分管理功能
"""

from member import Member  # 导入队员类


class MemberManager:
    """
    队员管理类：管理所有队员的集合，提供增删改查操作
    
    实例属性:
        members (list): 存储所有队员对象的列表
    
    方法:
        add_member(name, group): 添加新队员
        view_all_members(): 查看所有队员信息
        find_member_by_id(member_id): 根据编号查找队员
        add_points(member_id, points): 为队员加分
        deduct_points(member_id, points): 为队员扣分
        rank_by_points(): 按积分排名
        delete_member(member_id): 删除队员
    """

    def __init__(self):
        """
        初始化队员管理器
        
        创建一个空的队员列表，用于存储所有队员对象
        """
        self.members = []  # 存储所有队员对象的列表

    def add_member(self, name, group):
        """
        添加新队员
        
        参数:
            name (str): 队员姓名
            group (str): 队员组别（视觉/电控/机械/运营）
        
        返回:
            Member: 新创建的队员对象
        
        说明:
            - 创建新的队员对象
            - 将队员添加到列表中
            - 返回新创建的队员对象
        """
        # 创建新的队员对象
        member = Member(name, group)
        # 将队员添加到列表中
        self.members.append(member)
        # 返回新创建的队员对象
        return member

    def view_all_members(self):
        """
        查看所有队员信息
        
        以表格形式展示所有队员的编号、姓名、组别和积分
        
        说明:
            - 如果没有队员，显示提示信息
            - 否则以表格形式显示所有队员信息
        """
        # 检查是否有队员
        if not self.members:
            print("暂无队员信息")
            return
        
        # 打印表头
        print(f"{'编号':<10}{'姓名':<10}{'组别':<10}{'积分':<10}")
        print("-" * 40)  # 打印分隔线
        
        # 遍历所有队员并打印信息
        for member in self.members:
            # 使用 f-string 格式化输出，<10 表示左对齐，宽度为10
            print(f"{member.member_id:<10}{member.name:<10}{member.group:<10}{member.points:<10}")

    def find_member_by_id(self, member_id):
        """
        根据队员编号查找队员
        
        参数:
            member_id (str): 队员编号（如 "RM0001"）
        
        返回:
            Member 或 None: 如果找到返回队员对象，否则返回 None
        
        说明:
            - 遍历队员列表，查找匹配的编号
            - 如果找到返回队员对象
            - 如果未找到返回 None
        """
        # 遍历队员列表
        for member in self.members:
            # 检查编号是否匹配
            if member.member_id == member_id:
                return member  # 找到队员，返回队员对象
        return None  # 未找到队员，返回 None

    def add_points(self, member_id, points):
        """
        为队员加分
        
        参数:
            member_id (str): 队员编号
            points (int): 要增加的分数（必须为正数）
        
        返回:
            bool: 操作是否成功
        
        说明:
            - 先查找队员是否存在
            - 如果队员不存在，显示错误信息并返回 False
            - 如果队员存在，增加积分并显示成功信息
        """
        # 查找队员
        member = self.find_member_by_id(member_id)
        
        # 检查队员是否存在
        if member is None:
            print("未找到该队员")
            return False  # 操作失败
        
        # 增加积分
        member.points += points
        
        # 显示成功信息
        print(f"已为 {member.name} 增加 {points} 分，当前积分: {member.points}")
        return True  # 操作成功

    def deduct_points(self, member_id, points):
        """
        为队员扣分
        
        参数:
            member_id (str): 队员编号
            points (int): 要扣除的分数（必须为正数）
        
        返回:
            bool: 操作是否成功
        
        说明:
            - 先查找队员是否存在
            - 如果队员不存在，显示错误信息并返回 False
            - 如果队员存在，减少积分并显示成功信息
        """
        # 查找队员
        member = self.find_member_by_id(member_id)
        
        # 检查队员是否存在
        if member is None:
            print("未找到该队员")
            return False  # 操作失败
        
        # 减少积分
        member.points -= points
        
        # 显示成功信息
        print(f"已为 {member.name} 扣除 {points} 分，当前积分: {member.points}")
        return True  # 操作成功

    def rank_by_points(self):
        """
        按积分排名
        
        从高到低展示队员积分排行榜
        
        说明:
            - 如果没有队员，显示提示信息
            - 否则按积分从高到低排序并显示排行榜
        """
        # 检查是否有队员
        if not self.members:
            print("暂无队员信息")
            return
        
        # 按积分从高到低排序
        # key=lambda m: m.points 表示按队员的 points 属性排序
        # reverse=True 表示降序排列
        sorted_members = sorted(self.members, key=lambda m: m.points, reverse=True)
        
        # 打印排行榜标题
        print("\n===== 积分排名 =====")
        print(f"{'排名':<6}{'编号':<10}{'姓名':<10}{'组别':<10}{'积分':<10}")
        print("-" * 46)
        
        # 遍历排序后的队员列表并打印排名
        # enumerate(sorted_members, 1) 表示从1开始计数
        for rank, member in enumerate(sorted_members, 1):
            print(f"{rank:<6}{member.member_id:<10}{member.name:<10}{member.group:<10}{member.points:<10}")

    def delete_member(self, member_id):
        """
        删除队员
        
        参数:
            member_id (str): 要删除的队员编号
        
        返回:
            bool: 操作是否成功
        
        说明:
            - 先查找队员是否存在
            - 如果队员不存在，显示错误信息并返回 False
            - 如果队员存在，要求二次确认后删除
        """
        # 查找队员
        member = self.find_member_by_id(member_id)
        
        # 检查队员是否存在
        if member is None:
            print("未找到该队员")
            return False  # 操作失败
        
        # 二次确认删除
        # input() 函数用于获取用户输入
        confirm = input(f"确认删除队员 {member.name}（{member.member_id}）？(y/n): ")
        
        # 检查用户输入
        if confirm.lower() == 'y':  # 用户确认删除
            # 从列表中移除队员
            self.members.remove(member)
            print(f"已删除队员 {member.name}")
            return True  # 操作成功
        else:  # 用户取消删除
            print("取消删除")
            return False  # 操作取消
