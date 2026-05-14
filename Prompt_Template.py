import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

# 1. 定义 DeepSeek 模型（关键：必须填 base_url 和 api_key）
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",  # DeepSeek 官方接口地址
    api_key=os.getenv("DEEPSEEK_API_KEY"),       # 你必须填自己的密钥
    model_provider="deepseek",          # 提供商
    temperature=0.7,                         # 可选参数
)

# 字符串模板:PromptTemplate
# prompt_template = PromptTemplate.from_template("翻译这个英文单词{ward}")
#prompt_template = PromptTemplate(
# input_variables=["ward"],
# template="翻译这个英文单词{ward}",
# print(prompt_template.invoke({"ward": "Chinese"}))

# 聊天消息模板:ChatPromptTemplate,也实现了标准的 Runnable 接⼝
# 1. 设置模板
prompt_template = ChatPromptTemplate(
    [
        ("system","你是一个翻译助手，请用中文，翻译这个英文单词{ward}"),
        MessagesPlaceholder("msgs"),
        ("user","{text}")
    ]
)

messages_to_pass = [
        HumanMessage(content="capital"),
        AIMessage(content="名词属性:首都,资本"),
        HumanMessage(content="那Franch呢?")
]

# 2.实例化模板
messagesValue = prompt_template.invoke(
    {
        "ward":"Chinese",
        "text":"what is mean?"
    }
)
messages = messagesValue.to_messages()
# print(messages)
# 定义输出解析器
parser = StrOutputParser()#无参

# DeepSeek.invoke(messages).pretty_print()

# chain = DeepSeek|parser
# print(chain.invoke(messages))

full_response = ""  # 用来拼完整回答
chain = prompt_template|DeepSeek|parser
for token in chain.stream(
        {
            "ward": "English",  # 注意：你之前拼写的是 ward，保持和模板一致
            "text": "what is mean?",
            "msgs": messages_to_pass  # 把你定义的历史消息传进去
        }
):
    full_response += token
    print(token, end="", flush=True)
print()  # 换行

# ===== 第 3 步：把本轮对话追加到历史中 =====
# 把当前用户输入加进去
messages_to_pass.append(HumanMessage(content="what is mean?"))
# 把模型的完整回答加进去
messages_to_pass.append(AIMessage(content=full_response))

# 现在 messages_to_pass 包含了这次对话，下次调用可以继续用
