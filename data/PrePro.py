import json

with open('data.txt', 'r', encoding='utf-8') as file:
    alpaca_data = []

    # 逐行处理JSON数据并转换为Alpaca格式
    for line in file:
        try:
            json_data = json.loads(line)
            formatted_item = {
                "instruction": json_data["prompt"],
                "input": json_data["input"],
                "output": json_data["output"][0] if json_data["output"] else ""  # 处理可能为空的情况
            }
            alpaca_data.append(formatted_item)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue

# 将Alpaca格式的数据保存为JSON文件
with open('alpaca_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(alpaca_data, json_file, indent=2, ensure_ascii=False)
