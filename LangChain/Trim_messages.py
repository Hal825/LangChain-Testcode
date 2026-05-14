import os

from certifi import contents
from langchain.chat_models import init_chat_model
from langchain_core .messages import HumanMessage , SystemMessage ,AIMessage , trim_messages
from langchain_core.runnables import RunnableSequence, RunnableLambda
from langgraph.graph.message import Messages

# 1.定义大模型
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model_provider="deepseek",
    temperature=0.7
)

# 历史消息记录
messages = [
      SystemMessage(content="you 're a good assistant"),
      HumanMessage(content="hi! I 'm bob"),
      AIMessage(content="hi!"),
      HumanMessage(content="I like vanilla ice cream"),
      AIMessage(content="nice"),
      HumanMessage(content="whats 2 + 2 "),
      AIMessage(content="4 "),
      HumanMessage(content="thanks"),
      AIMessage(content="no problem!"),
      HumanMessage(content="having fun?"),
      AIMessage(content="yes!"),
      HumanMessage(content="What 's my name?"),
]
# 自定义 token 计数函数：按字符数估算（4个字符约等于1个token）DeepSeek计算不了token
def count_tokens(message):
    try:
        # 获取消息内容
        if hasattr(message, 'content'):
            content = message.content
        else:
            content = str(message)
        # 简单估算：字符数 / 4
        return len(content) // 4 + 1
    except:
        return 100  # 默认值

def count_messages(message):
    """每条消息计数为1"""
    return 1

trimmer = trim_messages(
    # messages=messages,     # 必需：要裁剪的消息列表,如果不传就是Runnable 对象，如果传就是列表(trimmer)
    strategy="last",       # 裁剪策略
    # token_counter=count_tokens,    # token计数函数
    token_counter=count_messages,
    # max_tokens=60,       # 最大token数
    max_tokens = 10,
    start_on="human",      # 开始位置的消息类型
    end_on=("human", "ai"), # 结束位置的消息类型
    include_system=True,   # 是否包含系统消息
    allow_partial=False,   # 是否允许部分消息
)

#trimmer位Runnable都可用，是list不可直接用chain
# chain = trimmer | DeepSeek
# print(chain.invoke(messages))
# 6. 使用裁剪后的消息调用模型（修正点1）
# response = DeepSeek.invoke(trimmer)
#
# 7. 美化打印输出（修正点2）
# response.pretty_print()
