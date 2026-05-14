from langchain_core .messages import HumanMessage , SystemMessage ,AIMessage ,filter_messages

# 历史消息记录
messages = [
    SystemMessage("你是一个知识助手", id="1 "),
    HumanMessage("include_types的单个类型和多个类型的参数区别", id="2 "),
    AIMessage("示例输出", id="3 "),
    HumanMessage("帮我总结", id="4 "),
    AIMessage("真实输出", id="5 "),
]
# 按类型进行筛选：
# print(filter_messages(messages,include_types="human"))
# 注意写法等价于：
#print(filter_messages(include_types ="human").invoke(messages))
#  按类型+ID进行筛选：
# include_types 参数接受两种类型：
# 单个类型：可以用字符串或类型对象
# 多个类型：必须用列表
print(filter_messages(messages,include_types=[HumanMessage ,AIMessage],exclude_ids=["3"]))