<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LangChain 学习练习代码库</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        h1, h2 {
            color: #2c3e50;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.3rem;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        ul {
            padding-left: 1.5rem;
        }
        li {
            margin: 0.5rem 0;
        }
        .file-item {
            font-family: 'Courier New', Courier, monospace;
            color: #2980b9;
        }
        .note {
            background: #e8f4fd;
            padding: 1rem;
            border-left: 4px solid #3498db;
            margin: 1rem 0;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🦜️🔗 LangChain 学习练习代码库</h1>
        <p>这是一个记录我学习 LangChain 框架的练习项目，包含多个核心功能的基础实现与示例代码。</p>

        <h2>📁 项目文件说明</h2>
        <ul>
            <li><span class="file-item">few-shotting.py</span> - 少样本提示词工程示例</li>
            <li><span class="file-item">filter_merge.py</span> - 消息过滤与合并操作</li>
            <li><span class="file-item">filter_messages.py</span> - 对话消息过滤逻辑</li>
            <li><span class="file-item">Multi-turn conversation.py</span> - 多轮对话与上下文管理</li>
            <li><span class="file-item">Prompt Maker.py</span> - 提示词构建工具示例</li>
            <li><span class="file-item">Prompt_Template.py</span> - LangChain 提示词模板使用</li>
            <li><span class="file-item">S_T.py</span> - 基础链式调用（Sequential Chain）示例</li>
            <li><span class="file-item">structured.py</span> - 结构化输出解析示例</li>
            <li><span class="file-item">Translate-Wards.py</span> - 基于 LangChain 的翻译功能实现</li>
            <li><span class="file-item">Trim_messages.py</span> - 对话消息截断与长度控制</li>
            <li><span class="file-item">Usage scenario.py</span> - LangChain 典型使用场景示例</li>
        </ul>

        <h2>🚀 运行说明</h2>
        <div class="note">
            <p>1. 确保已安装 Python 3.8+ 与 LangChain 相关依赖：<br>
               <code>pip install langchain langchain-openai python-dotenv</code></p>
            <p>2. 在项目根目录创建 <code>.env</code> 文件，配置你的 API Key：<br>
               <code>OPENAI_API_KEY=你的密钥</code></p>
            <p>3. 直接运行对应 Python 文件即可查看效果。</p>
        </div>

        <h2>📌 项目说明</h2>
        <p>本项目仅为个人学习记录，代码均为基础示例，主要用于理解 LangChain 的核心组件与工作流程，可作为学习参考。</p>
    </div>
</body>
</html>
