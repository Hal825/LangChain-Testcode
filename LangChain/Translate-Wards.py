import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
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
# 聊天消息模板:ChatPromptTemplate,也实现了标准的 Runnable 接⼝
# 1. 设置模板
prompt_template = ChatPromptTemplate(
    [
        ("system","你是一个翻译助手，请用中文翻译用户输入的句子，并给出重点词语的解释。如果用户输入的句子错误那么请解释错误的原因和正确的语法结构"),
        MessagesPlaceholder("msgs"),
        ("user","{sentence}")
    ]
)
# 历史对话
messages_to_pass = []

# ===== 3. 构建链 =====
parser = StrOutputParser()#无参
chain = prompt_template|DeepSeek|parser

# ===== 4. 对话循环 =====

print("=" * 50)
print("翻译助手已启动！输入句子获取翻译，输入 quit 退出")
print("=" * 50)

while True:
    sentence = input("\n请输入句子: ").strip()
    if not sentence:
        print("请输入有效的数据")
        continue
    # 退出判断
    if sentence.lower() == "quit":
        print("再见！")
        break
    # 调用模型，流式输出
    print("翻译结果: ", end="")
    full_response = ""
    try:
        for token in chain.stream(
                {
                    "sentence": sentence,
                    "msgs":messages_to_pass
                }
        ):
            print(token, end="", flush=True)
            full_response += token
        print()  # 换行
        messages_to_pass.append(HumanMessage(content=sentence))
        messages_to_pass.append(AIMessage(content=full_response))
    except Exception as e:
        print(f"\n出错了: {e}")
