"""
队员类定义模块
该模块定义了 RoboMaster 队员的基本信息和行为
"""


class Member:
    """
    队员类：表示一个 RoboMaster 队员的基本信息
    
    类属性:
        _next_id (int): 类级别的变量，用于自动生成队员编号，初始值为 1
                        每次创建新队员时自动递增
    
    实例属性:
        member_id (str): 队员编号，格式为 "RM0001"、"RM0002" 等
        name (str): 队员姓名
        group (str): 队员所属组别，可选值为 "视觉"、"电控"、"机械"、"运营"
        points (int): 队员积分，初始值为 0
    """
    
    # 类属性：用于自动生成队员编号
    # 使用类属性而不是实例属性，是因为编号需要全局递增
    _next_id = 1

    def __init__(self, name, group):
        """
        初始化队员信息
        
        参数:
            name (str): 队员姓名
            group (str): 队员所属组别
        
        说明:
            - 自动生成队员编号，格式为 "RM" + 四位数字（如 RM0001）
            - 初始积分设置为 0
            - 创建后自动递增编号计数器
        """
        # 使用 f-string 格式化生成队员编号
        # {Member._next_id:04d} 表示将数字格式化为4位，不足4位前面补0
        self.member_id = f"RM{Member._next_id:04d}"
        self.name = name          # 队员姓名
        self.group = group        # 队员组别
        self.points = 0           # 初始积分为 0
        
        # 递增类属性，确保下一个队员获得新的编号
        Member._next_id += 1

    def __str__(self):
        """
        魔法方法：定义 print() 函数输出队员信息的格式
        
        返回:
            str: 格式化的队员信息字符串
        
        说明:
            当使用 print(member) 时会自动调用此方法
            返回格式：编号: RM0001 | 姓名: 张三 | 组别: 视觉 | 积分: 0
        """
        return f"编号: {self.member_id} | 姓名: {self.name} | 组别: {self.group} | 积分: {self.points}"
