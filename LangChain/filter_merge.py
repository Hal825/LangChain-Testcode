# 1. 定义 DeepSeek 模型（关键：必须填 base_url 和 api_key）
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, merge_message_runs

DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",  # DeepSeek 官方接口地址
    api_key=os.getenv("DEEPSEEK_API_KEY"),       # 你必须填自己的密钥
    model_provider="deepseek",          # 提供商
    temperature=0.7,                         # 可选参数
)

  # 历史消息记录
messages = [
      SystemMessage("你是一个聊天助手。"),
      SystemMessage("你总是以笑话回应。"),
      HumanMessage("为什么要使用LangChain?"),
      HumanMessage("为什么要使用LangGraph?"),
      AIMessage("因为当你试图让你的代码更有条理时，LangGraph 会让你感到“节点”是个好主意！"),
      AIMessage("不过别担心，它不会“分散”你的注意力！"),
      HumanMessage("选择LangChain还是LangGraph?")
]
merged = merge_message_runs (messages)
print("\n".join([repr(x) for x in merged]))
