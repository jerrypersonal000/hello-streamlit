import streamlit as st
from collections import deque

def shortest_path_to_range(A, B, C):
    queue = deque([(A, 0, [])])  # 存储当前值、步数和操作列表
    visited = set()  # 防止重复处理相同的值
    operations = list(range(1, 10))  # 定义1到9的操作数

    while queue:
        current, steps, path = queue.popleft()
        
        # 检查当前数值是否在区间内
        if B <= current <= C:
            return steps, path
        
        for op in operations:
            # 尝试所有加减乘除操作，并记录每一步的操作
            next_steps = [
                (current + op, f"{current} + {op} = {current + op}"),
                (current - op, f"{current} - {op} = {current - op}"),
                (current * op, f"{current} * {op} = {current * op}"),
                (current // op if op != 0 else None, f"{current} // {op} = {current // op}" if op != 0 else None)
            ]
            for result, desc in next_steps:
                if result is not None and result not in visited:
                    visited.add(result)
                    queue.append((result, steps + 1, path + [desc]))
    
    return -1, []  # 如果没有找到任何解决方案

# 使用 Streamlit 的输入组件获取参数
A = st.number_input("请输入初始值 A: ", step=1)
B = st.number_input("请输入区间下限 B: ", step=1)
C = st.number_input("请输入区间上限 C: ", step=1)

# 输出结果
steps, path = shortest_path_to_range(A, B, C)
if steps != -1:
    st.write(f"从 {A} 到区间 [{B}, {C}] 的最短路径需要 {steps} 步")
    st.write("操作步骤如下：")
    for p in path:
        st.write(p)
else:
    st.write(f"没有找到从 {A} 到区间 [{B}, {C}] 的路径。")

