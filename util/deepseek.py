import json
import os

from prompts.file_name import PROMPT_TEXT
from openai import OpenAI
from util.parse_file_content import upload_file
from dotenv import load_dotenv

load_dotenv()


class DeepSeek:
    def __init__(self):
        self.client = None
        self.api_key = None
        # 加载DeepSeek API Key
        self.load_api_key()
        # 初始化DeepSeek客户端
        self.init_client(self.api_key)

    def load_api_key(self):
        """
        加载DeepSeek API Key
        :param api_key: DeepSeek API Key
        :return:
        """
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

    def init_client(self, api_key):
        """
        初始化DeepSeek客户端
        :return:
        """
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
        )

    async def file_rename(self, file_path):
        """
        文件重命名
        :param file_path: 文件路径
        :return:
        """

        file_name = os.path.basename(file_path)
        file_content = upload_file(file_path)
        if not file_content:
            print(f"{file_path}文件内容为空或者不受支持")
            return
        prompt = PROMPT_TEXT.format(file_name=file_name, file_content=file_content)

        messages = [{"role": "system", "content": "你要根据用户提供的信息对文件进行重命名,要确保文件名没有特殊字符,最后的回答只有一个文件名。不要有多余的文字。"},
                    {"role": "user", "content":prompt}]

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            # response_format={
            #     'type': 'json_object'
            # }
        )

        print(response.choices[0].message.content)
        file_name = response.choices[0].message.content.strip()
        os.rename(file_path, os.path.join(os.path.dirname(file_path), file_name))
        print(f"文件重命名成功, 新文件名为: {file_name}")

if __name__ == '__main__':
    deepseek = DeepSeek()
    deepseek.file_rename(r"E:\project\file_renaming\test\商业计划书PDF版.pdf")

