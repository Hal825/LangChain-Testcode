import os

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field

# 1.定义模型
model = ChatOpenAI(
    model="deepseek-v4-pro",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 2.Pydantic对象演示：返回结构性数据而不是文本
class WordExplanation(BaseModel):
    word: str = Field(description="单词词性")
    definition: str = Field(description="单词含义")

# 因为deepseek模型不支持model.with_structured_output,所有替换成解析后填充模板
# 3.先创建解析器,此时解析器存的是模型的原始文本
parser = PydanticOutputParser(pydantic_object=WordExplanation)

# 4.定义输入模板
promt = PromptTemplate(
    # template="解释单词：{word}\n{format_instructions}",
    # input_variables=["word"],
    # partial_variables={"format_instructions": parser.get_format_instructions()},
    template="""请随机挑选一个英文单词，进行解释，返回JSON即可，字数不超过20个字 {format_instructions}""",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
# 5. 构建执行链（关键步骤！）
chain = promt|model|parser
print(chain.invoke({}))

# chatgpt版本
# from typing import Optional
# from langchain_openai import ChatOpenAI
# from pydantic import BaseModel, Field
#
# # 初始化模型
# model = ChatOpenAI(model="gpt-4o-mini")
#
# # 定义 Pydantic 对象
# class Joke(BaseModel):
#     setup: str = Field(description="这个笑话的开头")
#     punchline: str = Field(description="这个笑话的妙语")
#     rating: Optional[int] = Field(default=None, description="从1-10分，给这个笑话评分")
#
# # 使用结构化输出
# model_with_structured = model.with_structured_output(Joke)
# print(model_with_structured.invoke("请讲一个关于唱歌的笑话"))

# 一.pydantic
# 二.typedict
# 三。json
# 四.选择输出格式