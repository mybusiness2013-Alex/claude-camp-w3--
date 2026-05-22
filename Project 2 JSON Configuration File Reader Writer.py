import json
import os

CONFIG_FILE = "config.json"

# 默认配置（如果文件不存在）
default_config = {
    "theme": "light",
    "language": "en",
    "font_size": 14
}


def load_config():
    """读取配置文件，如果不存在则创建默认配置"""
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
        print("未找到 config.json，已创建默认配置。")
        return default_config

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(config):
    """保存配置到 config.json"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    print("配置已保存！")


def validate(key, value):
    """对用户输入进行验证"""
    if key == "font_size":
        try:
            value = int(value)
        except ValueError:
            print("字体大小必须是数字。")
            return None

        if not (8 <= value <= 32):
            print("字体大小必须在 8 到 32 之间。")
            return None

    return value


def main():
    config = load_config()

    print("\n当前配置：")
    for k, v in config.items():
        print(f"- {k}: {v}")

    print("\n可修改的设置：theme / language / font_size")
    key = input("请输入你想修改的设置名称： ").strip()

    if key not in config:
        print("无效的设置名称。")
        return

    new_value = input(f"请输入新的 {key} 值： ").strip()

    # 验证输入
    validated_value = validate(key, new_value)
    if validated_value is None:
        print("修改失败，请重新运行程序。")
        return

    # 更新配置
    config[key] = validated_value
    save_config(config)

    print("\n修改后的配置：")
    for k, v in config.items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
