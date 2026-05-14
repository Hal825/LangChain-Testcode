import os

from langchain.chat_models import init_chat_model
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableWithMessageHistory

from LangChain.Init import DeepSeek
from LangChain.structured import model

#  BaseChatMessageHistory：定义对话历史管理的标准接口
# InMemoryChatMessageHistory:将对话历史存储在内存列表中
# RunnableWithMessageHistory:为 LangChain 的可运行组件（如链、模型）自动注入对话历史

# 内存缓存

# 1.定义大模型
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model_provider="deepseek",
    temperature=0.7
)

# 2.get_session_history获取或创建对应的会话历史记录对象
#定义字典用来储存
store = {}
def get_session_history(session_id : str) -> BaseChatMessageHistory :
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

#3. 包装model，管理聊天消息历史记录
with_message_history = RunnableWithMessageHistory(DeepSeek,get_session_history)

# 4.多轮对话
# 配置信息
config = {"configurable":{"session_id":"1"}}
with_message_history.invoke([HumanMessage(content="HelloWorld!")],config=config).pretty_print()
with_message_history.invoke([HumanMessage(content="我上句话说了什么？")],config=config).pretty_print()

