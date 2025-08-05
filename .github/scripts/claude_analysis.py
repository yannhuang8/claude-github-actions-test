import os
from anthropic import Anthropic

def analyze_code():
    # 初始化 Claude 客户端
    client = Anthropic(
        api_key='sk-xM2kDNdzKAg1DdqoZkY5NA14TYAVLv9i356jhYX0KczrTcK5',
        base_url='https://code.ppchat.vip'
    )

    # 获取当前工作目录（字符串类型）
    current_dir = os.getcwd()
    # 打印结果
    print("当前目录：", current_dir)

    # 读取需要分析的代码文件（示例：读取当前目录下的 Python 文件）
    code_files = ['/home/runner/work/claude-github-actions-test/claude-github-actions-test/src/main/java/com/example/demo/controller/HelloController.java']

    code_content = ""
    for file in code_files:
        with open(file, 'r') as f:
            code_content += f"File: {file}\n{'-'*50}\n{f.read()}\n\n"

    # 调用 Claude API 进行代码分析
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"请分析以下代码，给出改进建议和潜在问题：\n{code_content}"
            }
        ]
    )

    # 输出分析结果
    print("Claude Code Analysis Result:")
    print(message.content[0].text)

if __name__ == "__main__":
    analyze_code()