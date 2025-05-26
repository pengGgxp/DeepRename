import os
import asyncio
import argparse
from util.deepseek import DeepSeek

async def rename_files_in_directory(directory_path):
    """
    遍历指定目录及其子目录中的所有文件，并使用DeepSeek进行重命名。
    :param directory_path: 要处理的目录路径
    """
    deepseek_renamer = DeepSeek()
    tasks = []
    for root, _, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # 确保我们只处理文件，并且避免处理由pptx2md生成的.md文件或图片文件夹
            if os.path.isfile(file_path) and not filename.endswith('.md') and '_images' not in file_path:
                print(f"准备重命名文件: {file_path}")
                # 注意：DeepSeek API 调用可能是异步的，如果不是，则不需要 await
                # 根据 deepseek.py 中的定义，file_rename 是一个 async 函数
                tasks.append(deepseek_renamer.file_rename(file_path))
    
    if tasks:
        await asyncio.gather(*tasks)
    else:
        print(f"在目录 {directory_path} 中没有找到符合条件的文件进行重命名。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用DeepSeek批量重命名指定文件夹中的文件。")
    parser.add_argument("-d", "--directory", type=str, default=".", 
                        help="要处理的文件夹路径。默认为当前目录。")
    args = parser.parse_args()

    target_directory = os.path.abspath(args.directory)

    # 请确保 DeepSeek API Key 已在 .env 文件中正确设置

    if not os.path.exists(target_directory):
        print(f"错误：目标目录 {target_directory} 不存在。")
    elif not os.path.isdir(target_directory):
        print(f"错误：路径 {target_directory} 不是一个有效的目录。")
    elif not os.listdir(target_directory):
        print(f"警告：目标目录 {target_directory} 为空。没有文件可供重命名。")
    else:
        print(f"开始处理目录: {target_directory}")
        asyncio.run(rename_files_in_directory(target_directory))
        print("所有文件处理完毕。")