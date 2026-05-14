import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# 定义示例
examples = [
    {"input": "开心", "output": "positive"},
    {"input": "伤心", "output": "negative"},
    {"input": "兴奋", "output": "positive"},
]

# 定义每个示例的格式化模板（ChatPromptTemplate 需要 messages 列表）
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "输入: {input}"),
    ("ai", "输出: {output}"),
])

# 1. 定义 DeepSeek 模型（关键：必须填 base_url 和 api_key）
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",  # DeepSeek 官方接口地址
    api_key=os.getenv("DEEPSEEK_API_KEY"),       # 你必须填自己的密钥
    model_provider="deepseek",          # 提供商
    temperature=0.7,                         # 可选参数
)

# 创建 FewShotChatMessagePromptTemplate是⼀个提⽰词模板，专⻔⽤来将⽰例集实例化为聊天消息，
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

# 最终 prompt：组合系统提示 + 少样本示例 + 用户输入
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "请判断以下输入的情感倾向："),
    few_shot_prompt,  # 插入少样本示例
    ("human", "输入: {user_input}\n输出:"),
])

# 使用
result = final_prompt.format(user_input="愤怒")
print(DeepSeek.invoke(result))