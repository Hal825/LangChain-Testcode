from langsmith import Client
import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser

# 初始化客户端并拉取模板
client = Client()
prompt_template = client.pull_prompt(
    "hardkothari/prompt-maker",
    dangerously_pull_public_prompt=True  # 👈 关键：确认你信任这个公开模板
)

# 定义模型
DeepSeek = init_chat_model(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model_provider="deepseek",
    temperature=0.7,
)

# 构建链
parser = StrOutputParser()
chain = prompt_template | DeepSeek | parser

# ===== 对话循环 =====
print("=" * 50)
print("提示词优化助手已启动！输入 'quit' 退出")
print("=" * 50)

while True:
    task = input("\n请输入任务描述（如：翻译助手、代码审查等）: ").strip()
    if task.lower() == "quit":
        print("再见！")
        break

    lazy_prompt = input("请输入需要优化的原始提示词: ").strip()
    if lazy_prompt.lower() == "quit":
        print("再见！")
        break

    if not task or not lazy_prompt:
        print("任务描述和原始提示词都不能为空，请重新输入。")
        continue

    # 调用模型，流式输出
    print("\n优化后的提示词:\n")
    try:
        for token in chain.stream({"task": task, "lazy_prompt": lazy_prompt}):
            print(token, end="", flush=True)
        print("\n" + "-" * 50)
    except Exception as e:
        print(f"\n出错了: {e}")