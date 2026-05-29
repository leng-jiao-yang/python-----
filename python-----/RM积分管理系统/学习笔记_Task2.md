# Task 2 学习笔记 - RoboMaster 队员积分管理系统

## 项目概述

本项目实现了一个基于命令行的 RoboMaster 队员积分管理系统，支持队员的增删改查和积分管理功能。

## 项目结构

```
RM积分管理系统/
├── .gitignore          # Git 忽略文件配置
├── main.py             # 主程序入口，菜单循环
├── member.py           # Member 类定义
├── manager.py          # MemberManager 类定义
└── 学习笔记_Task2.md   # 本学习笔记
```

## 核心知识点

### 1. 面向对象编程

#### 类的定义与使用
- **Member 类**：表示队员实体，包含编号、姓名、组别、积分等属性
- **MemberManager 类**：管理队员集合，提供增删改查操作

#### 类属性 vs 实例属性
```python
class Member:
    _next_id = 1  # 类属性，用于自动编号

    def __init__(self, name, group):
        self.member_id = f"RM{Member._next_id:04d}"  # 实例属性
        self.name = name
        self.group = group
        self.points = 0
        Member._next_id += 1  # 修改类属性
```

#### 魔法方法 `__str__`
```python
def __str__(self):
    return f"编号: {self.member_id} | 姓名: {self.name} | 组别: {self.group} | 积分: {self.points}"
```
- 当使用 `print(member)` 时自动调用
- 返回友好的字符串表示

### 2. 模块化设计

#### 文件拆分
- `member.py`：队员类定义
- `manager.py`：管理类定义
- `main.py`：主程序逻辑

#### 导入机制
```python
from member import Member
from manager import MemberManager
```

### 3. 数据结构

#### 列表存储
```python
self.members = []  # 存储所有队员对象
```

#### 排序算法
```python
sorted_members = sorted(self.members, key=lambda m: m.points, reverse=True)
```
- 使用 `sorted()` 函数
- `key` 参数指定排序依据
- `reverse=True` 表示降序排列

### 4. 输入校验

#### 数字校验
```python
if not choose.isdigit():
    print("输入无效，请输入数字 1-7")
    continue
```

#### 空值校验
```python
if not name.strip():
    print("姓名不能为空")
    continue
```

#### 范围校验
```python
valid_groups = ["视觉", "电控", "机械", "运营"]
if group not in valid_groups:
    print(f"组别无效，可选：{', '.join(valid_groups)}")
    continue
```

### 5. 字符串格式化

#### f-string 格式化
```python
f"RM{Member._next_id:04d}"  # 补零到4位
f"{member.member_id:<10}"   # 左对齐，宽度10
```

## Git 版本控制

### 提交记录

| 提交 | 说明 |
|------|------|
| init: Task2 目录结构与空文件 | 初始化项目结构 |
| feat: 完成 Member 类定义 | 实现队员类 |
| feat: 实现添加队员与查看队员功能 | 基础增删改查 |
| feat: 实现加分与扣分功能 | 积分管理 |
| feat: 实现积分排名与删除队员功能 | 高级功能 |
| feat: 完成主菜单循环与输入校验 | 主程序完善 |

### .gitignore 配置
```
.idea/          # 忽略 IDE 配置
__pycache__/    # 忽略 Python 缓存
*.pyc           # 忽略编译文件
```

## 功能实现

### 1. 添加队员
- 输入姓名和组别
- 自动生成编号（RM0001, RM0002, ...）
- 初始积分默认为 0

### 2. 查看所有队员
- 以表格形式展示
- 显示编号、姓名、组别、积分

### 3. 为队员加分/扣分
- 输入队员编号
- 输入分数（正整数）
- 更新队员积分

### 4. 按积分排名
- 从高到低排序
- 显示排名、编号、姓名、组别、积分

### 5. 删除队员
- 输入队员编号
- 二次确认后删除

## 学习总结

### 收获
1. 掌握了面向对象编程的基本概念
2. 学会了类属性和实例属性的使用
3. 理解了模块化设计的优势
4. 实践了 Git 版本控制流程
5. 提高了代码可读性和可维护性

### 改进方向
1. 可以添加数据持久化功能（保存到文件）
2. 可以增加更多的数据验证
3. 可以添加搜索功能
4. 可以实现图形用户界面（GUI）

## 运行方式

```bash
python main.py
```

## 注意事项

1. 数据仅保存在内存中，退出程序后会丢失
2. 队员编号自动递增，不可修改
3. 组别限定为：视觉、电控、机械、运营
4. 分数必须为正整数
