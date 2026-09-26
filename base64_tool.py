import base64
import mimetypes
from pathlib import Path


# =========================
# 路径配置
# =========================

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


# =========================
# 文字 → Base64
# =========================

def text_to_base64():
    text = input("\n请输入文字：")

    encoded = base64.b64encode(
        text.encode("utf-8")
    ).decode("ascii")

    print("\nBase64：")
    print(encoded)


# =========================
# Base64 → 文字
# =========================

def base64_to_text():
    encoded = input("\n请输入 Base64：").strip()

    try:
        decoded = base64.b64decode(encoded)
        text = decoded.decode("utf-8")

        print("\n解码结果：")
        print(text)

    except Exception as e:
        print("\n解码失败：")
        print(e)


# =========================
# 图片 → Base64
# =========================

def image_to_base64():
    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
        ".svg",
        ".ico",
        ".tiff",
        ".tif"
    }

    images = [
        file for file in INPUT_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in image_extensions
    ]

    if not images:
        print(f"\ninput 文件夹中没有找到图片。")
        print(f"图片应该放在：{INPUT_DIR}")
        return

    print("\n找到以下图片：")

    for i, image in enumerate(images, 1):
        print(f"{i}. {image.name}")

    choice = input("\n请选择图片编号：").strip()

    try:
        index = int(choice) - 1
        image_path = images[index]
    except (ValueError, IndexError):
        print("\n选择无效。")
        return

    try:
        # 读取二进制图片
        image_data = image_path.read_bytes()

        # Base64 编码
        encoded = base64.b64encode(image_data).decode("ascii")

        # 获取 MIME 类型
        mime_type, _ = mimetypes.guess_type(image_path.name)

        if mime_type is None:
            mime_type = "application/octet-stream"

        # 生成 Data URI
        result = f"data:{mime_type};base64,{encoded}"

        print("\nBase64：")
        print(result)

    except Exception as e:
        print("\n处理图片失败：")
        print(e)


# =========================
# Base64 → 图片
# =========================

def base64_to_image():
    print("\n请输入 Base64。")
    print("如果内容很长，可以直接粘贴后按回车。")

    encoded = input("\nBase64：").strip()

    try:
        # 支持：
        # data:image/jpeg;base64,/9j/...
        # 以及纯 Base64
        if encoded.startswith("data:"):
            header, encoded = encoded.split(",", 1)

            # 从 data:image/jpeg;base64 中获取 MIME
            mime_type = header.split(";")[0][5:]

            extension = mimetypes.guess_extension(mime_type)

            if extension is None:
                extension = ".bin"

        else:
            extension = ".bin"

        # 解码
        image_data = base64.b64decode(encoded)

        # 让用户输入文件名
        filename = input(
            f"\n请输入输出文件名（直接回车使用 output{extension}）："
        ).strip()

        if not filename:
            filename = f"output{extension}"

        output_path = OUTPUT_DIR / filename

        # 写入图片
        output_path.write_bytes(image_data)

        print("\n转换成功！")
        print(f"图片已保存到：")
        print(output_path)

    except Exception as e:
        print("\nBase64 解码失败：")
        print(e)


# =========================
# 主菜单
# =========================

def main():
    while True:
        print("\n" + "=" * 40)
        print("        Base64 转换工具")
        print("=" * 40)

        print("1. 文字 → Base64")
        print("2. Base64 → 文字")
        print("3. 图片 → Base64")
        print("4. Base64 → 图片")
        print("0. 退出")

        choice = input("\n请选择模式：").strip()

        if choice == "1":
            text_to_base64()

        elif choice == "2":
            base64_to_text()

        elif choice == "3":
            image_to_base64()

        elif choice == "4":
            base64_to_image()

        elif choice == "0":
            print("\n退出程序。")
            break

        else:
            print("\n无效选择，请重新输入。")


if __name__ == "__main__":
    main()