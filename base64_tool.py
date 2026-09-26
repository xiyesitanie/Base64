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
        file
        for file in INPUT_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in image_extensions
    ]

    if not images:
        print("\ninput 文件夹中没有找到图片。")
        print(f"请将图片放入：{INPUT_DIR}")
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
        # 读取图片二进制数据
        image_data = image_path.read_bytes()

        # Base64 编码
        encoded = base64.b64encode(
            image_data
        ).decode("ascii")

        # 获取 MIME 类型
        mime_type, _ = mimetypes.guess_type(
            image_path.name
        )

        if mime_type is None:
            mime_type = "application/octet-stream"

        # 创建 Data URI
        result = (
            f"data:{mime_type};base64,{encoded}"
        )

        # 输出文件名
        output_name = image_path.stem + ".base64"
        output_path = OUTPUT_DIR / output_name

        # 保存 Base64
        output_path.write_text(
            result,
            encoding="utf-8"
        )

        print("\n转换成功！")
        print(f"Base64 已保存到：")
        print(output_path)

    except Exception as e:
        print("\n处理图片失败：")
        print(e)


# =========================
# Base64 → 图片
# =========================

def base64_to_image():
    base64_extensions = {
        ".base64",
        ".txt"
    }

    files = [
        file
        for file in INPUT_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in base64_extensions
    ]

    if not files:
        print("\ninput 文件夹中没有找到 Base64 文件。")
        print(f"请将 .base64 或 .txt 文件放入：{INPUT_DIR}")
        return

    print("\n找到以下 Base64 文件：")

    for i, file in enumerate(files, 1):
        print(f"{i}. {file.name}")

    choice = input("\n请选择文件编号：").strip()

    try:
        index = int(choice) - 1
        base64_path = files[index]

    except (ValueError, IndexError):
        print("\n选择无效。")
        return

    try:
        # 从文件读取 Base64
        encoded = base64_path.read_text(
            encoding="utf-8"
        ).strip()

        # 默认扩展名
        extension = ".bin"

        # 如果是 Data URI
        if encoded.startswith("data:"):
            header, encoded = encoded.split(",", 1)

            # 例如：
            # data:image/jpeg;base64
            mime_type = header.split(";")[0][5:]

            extension = mimetypes.guess_extension(
                mime_type
            )

            if extension is None:
                extension = ".bin"

        # 解码 Base64
        image_data = base64.b64decode(encoded)

        # 默认使用 Base64 文件名
        output_name = base64_path.stem + extension
        output_path = OUTPUT_DIR / output_name

        # 写入图片
        output_path.write_bytes(image_data)

        print("\n转换成功！")
        print("图片已保存到：")
        print(output_path)

    except ValueError:
        print("\nBase64 格式错误。")

    except Exception as e:
        print("\n处理失败：")
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
        print("3. 图片 → Base64 文件")
        print("4. Base64 文件 → 图片")
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