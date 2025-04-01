import subprocess

start_page = 1
end_page = 1154
num_instances = 10

pages_per_instance = (end_page - start_page + 1) // num_instances

for i in range(num_instances):
    page_start = start_page + i * pages_per_instance
    page_end = page_start + pages_per_instance - 1
    if i == num_instances - 1:
        page_end = end_page

    input_str = f"{page_start}\n{page_end}\n"

    subprocess.Popen(
        ['my_spider.exe'],
        stdin=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_CONSOLE  # 新窗口
    ).communicate(input_str.encode())
