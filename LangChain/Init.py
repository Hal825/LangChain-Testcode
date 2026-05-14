# import os
#
# from langchain.chat_models import init_chat_model
# from langchain_core.runnables import configurable
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import Runnable, RunnableSequence, configurable
# from langchain_openai import ChatOpenAI  # 这里必须是 ChatOpenAI，不是 ChatOpenAi
# #
# # //聊天模型组件
# # 1. 定义 DeepSeek 模型（关键：必须填 base_url 和 api_key）
# DeepSeek = ChatOpenAI(
#     model="deepseek-v4-pro",
#     base_url="https://api.deepseek.com/v1",  # DeepSeek 官方接口地址
#     api_key=os.getenv("DEEPSEEK_API_KEY"),       # 你必须填自己的密钥
#     temperature=0.7,                         # 可选参数
#     # model="gpt-4o-mini",  # 使用的模型名称
#     # temperature=2,       # 采样温度（控制随机性）
#     max_tokens=10       # 单次回答最多生成的 token 数
#     # timeout=None,        # 请求超时时间（秒）
#     # max_retries=2,       # 请求失败时的最大重试次数
#     # api_key="...",      # OpenAI API Key
#     # base_url="...",     # 自定义请求地址（如 DeepSeek/中转）
#     # organization="...", # OpenAI 组织 ID（企业账号用）
#     # other params...
# )
# # #
# # # model = ChatOpenAI(
# # #     model="deepseek-v4-pro",
# # #     base_url="https://api.deepseek.com/v1",
# # #     api_key=os.getenv("DEEPSEEK_API_KEY"),
# # #     temperature=0.7,
# # #     max_tokens=100,
# # # ).with_configurable_fields(
# # #     max_tokens={"config_prefix": "first"}
# # # )
# # #
# # 2. 测试调用（示例）
# messages = [
#     SystemMessage(content="你是一个专业的AI助手"),
#     HumanMessage(content="帮我翻译prevalent")
# ]
# # 3. 调用模型
# response = DeepSeek.invoke(messages)
# print(response.content)
# # #
# # # response = model.invoke(
# # #     input = messages,  # 不是 messages=
# # #     config = {         # 这里必须用大括号 {}
# # #         "configurable": {
# # #             "first_max_tokens": 10  # 不能两个逗号 ,,
# # #         }
# # #     }
# # # )
# # # print(response.content)
# # # //调用聊天模型组件
# #
# # #4. 定义输出解析器组件
# # # parser = StrOutputParser()
# # # print(parser.invoke(response))
# #
# # #5.定义链
# # # (1)chain = model|parser
# # # (2) chain = RunnableSequence(first=model,last=parser)
# # # chain = model.pipe(parser)
# # # # print(chain.Stream(messages))
# # # for chunk in chain.stream(messages):
# # #     print(chunk, end="", flush=True)
#
# #
# # import os
# #
# # from langchain.chat_models import init_chat_model
# # from langchain_core.messages import SystemMessage, HumanMessage
# #
# # # 1. 基础模型
# # model = init_chat_model(
# #     model="deepseek-v4-pro",
# #     base_url="https://api.deepseek.com/v1",
# #     api_key=os.getenv("DEEPSEEK_API_KEY"),
# #     temperature=0.7,
# #     max_tokens=100,
# # )
# #
# #
# # # 3. 对话消息
# # messages = [
# #     SystemMessage(content="你是一个专业的AI助手"),
# #     HumanMessage(content="帮我翻译 prevalent")
# # ]
# #
# # # 4. 调用：使用带前缀的 configurable 配置
# # response = model.invoke(
# #     input=messages,
#     config={
# #         "configurable": {
# #             "max_tokens": 10,
# #             "temperature": 0.1
# #         }
# #     }
# # )
# #
# # print(response.content)
#


import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_deepseek import ChatDeepSeek
from pyexpat.errors import messages

# 聊天模型组件
# LangChain DeepSeek 包下载:pip install -U langchain langchain-core langchain-deepseek python-dotenv
# 1. 定义 DeepSeek 模型（关键：必须填 base_url 和 api_key）
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",  # DeepSeek 官方接口地址
    api_key=os.getenv("DEEPSEEK_API_KEY"),       # 你必须填自己的密钥
    model_provider="deepseek",          # 提供商
    temperature=0.7,                         # 可选参数
)

# 2.定义数据
messages = [
    SystemMessage(content="你是一名专业的知识助手"),
    HumanMessage(content="include_types的单个类型和多个类型的参数区别"),
]

# 3. 调用模型
response = DeepSeek.invoke(messages)
print(response.content)

# import os
# from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_openai import ChatOpenAI  # 改用 OpenAI
#
# # 1. 定义 OpenAI 模型（通常只需 model 和 api_key）
# chatgpt = init_chat_model(
#     model="gpt-4o-mini",                # 或 "gpt-3.5-turbo"
#     api_key=os.getenv("OPENAI_API_KEY"), # 你的 OpenAI API 密钥
#     temperature=0.7,
# )
#
# # 2. 定义消息（完全相同）
# messages = [
#     SystemMessage(content="你是一名专业的翻译官"),
#     HumanMessage(content="帮我翻译Hello World!"),
# ]
#
# # 3. 调用模型
# response = chatgpt.invoke(messages)
# print(response.content)