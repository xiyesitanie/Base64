# Base64 Glyph

> A lightweight Python utility for converting between text, images, and Base64.

**Base64 Glyph** 是一个基于 Python 标准库实现的轻量级 Base64 转换工具，支持：

- 📝 Text → Base64
- 🔤 Base64 → Text
- 🖼️ Image → Base64
- 📦 Base64 → Image

无需安装第三方依赖，开箱即可使用。

---

## ✨ Features

### Text ↔ Base64

支持 UTF-8 文本与 Base64 之间的双向转换。

```text
Text
  ↓
UTF-8
  ↓
Base64
```

因此中文、日文以及其他 Unicode 字符同样可以正常处理。

### Image → Base64

将图片放入 `input/` 文件夹后，程序会自动扫描可识别的图片文件，并提供交互式选择。

支持常见格式：

```text
.jpg
.jpeg
.png
.gif
.bmp
.webp
.svg
.ico
.tiff
.tif
```

生成的结果采用 Data URI 格式：

```text
data:image/jpeg;base64,/9j/4AAQSkZJRg...
```

可以直接用于 HTML、Markdown 等场景。

### Base64 → Image

支持将 Base64 重新还原为图片。

同时兼容纯 Base64：

```text
/9j/4AAQSkZJRg...
```

以及 Data URI：

```text
data:image/jpeg;base64,/9j/4AAQSkZJRg...
```

如果输入包含 MIME 类型，程序会尝试自动确定输出文件的扩展名。

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- 无第三方依赖

项目只使用 Python 标准库：

```python
base64
pathlib
mimetypes
```

---

## 📦 Installation

Clone repository：

```bash
git clone <repository-url>
cd base64_glyph
```

如果希望使用独立的 Python 虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows：

```powershell
.venv\Scripts\activate
```

---

## ▶️ Usage

运行：

```bash
python base64_tool.py
```

启动后会进入交互式菜单：

```text
========================================
        Base64 转换工具
========================================
1. 文字 → Base64
2. Base64 → 文字
3. 图片 → Base64
4. Base64 → 图片
0. 退出

请选择模式：
```

输入对应编号即可选择功能。

### Text → Base64

选择：

```text
1
```

然后输入：

```text
love is love
```

程序输出对应的 Base64 编码。

### Base64 → Text

选择：

```text
2
```

粘贴 Base64：

```text
bG92ZSBpcyBsb3Zl
```

程序将其解码并输出：

```text
love is love
```

### Image → Base64

将图片放入：

```text
input/
```

例如：

```text
input/
├── image.jpg
├── image.png
└── image.webp
```

运行程序并选择：

```text
3
```

程序会扫描 `input/` 中的图片并让用户选择。

输出：

```text
data:image/jpeg;base64,/9j/4AAQSkZJRg...
```

### Base64 → Image

选择：

```text
4
```

粘贴 Base64 后，程序会将其还原为图片并保存到：

```text
output/
```

例如：

```text
output/
└── output.jpg
```

---

## 📁 Project Structure

```text
base64_glyph/
│
├── base64_tool.py      # Main program
├── input/               # Input images
├── output/              # Generated images
├── README.md
└── .gitignore
```

其中 `input/` 和 `output/` 文件夹会在程序运行时自动创建。

---

## 🧩 How It Works

Base64 本质上是一种**二进制数据到文本的编码方式**。

对于文字：

```text
Text
 ↓
UTF-8 bytes
 ↓
Base64
 ↓
ASCII string
```

例如：

```text
love is love
```

首先转换为 UTF-8 字节：

```text
bytes
```

然后通过 Base64 编码得到：

```text
bG92ZSBpcyBsb3Zl
```

对于图片，流程则是：

```text
Image File
    ↓
Binary Data
    ↓
Base64
    ↓
Text
```

因此图片并不是被“转换成另一种图片格式”，而是将图片本身的二进制数据编码成可以用文本表示的形式。

反向转换则完全相反：

```text
Base64
    ↓
Binary Data
    ↓
Image File
```

---

## 🌐 Data URI

Image → Base64 模式默认生成 Data URI：

```text
data:image/png;base64,iVBORw0KGgo...
```

它由三个主要部分组成：

```text
data:
  ↓
MIME Type
  ↓
;base64,
  ↓
Base64 Data
```

例如：

```text
data:image/png;base64,iVBORw0KGgo...
```

其中：

```text
data:
```

表示这是一个 Data URI。

```text
image/png
```

表示数据类型为 PNG 图片。

```text
;base64,
```

表示后面的数据采用 Base64 编码。

---

## ⚠️ Notes

### Base64 is not encryption

Base64 **不是加密算法**。

它只是一种编码方式：

```text
Original Data
      ↕
    Base64
```

任何知道编码格式的人都可以轻易将其还原。

因此不要使用 Base64 来保护：

- 密码
- API Key
- Token
- 私密文件
- 其他敏感信息

### Large Files

Base64 会使数据体积增加。

因此 Base64 更适合：

- 文本数据传输
- 小型图片
- Data URI
- API 数据
- Markdown / HTML 嵌入

而不适合作为大型文件的长期存储方式。

### Script Naming

请不要将主程序命名为：

```text
base64.py
```

因为 Python 标准库中本身存在：

```python
import base64
```

如果当前目录存在同名文件，Python 可能优先导入你的脚本，从而导致：

```text
AttributeError:
module 'base64' has no attribute 'b64encode'
```

推荐使用：

```text
base64_tool.py
```

---

## 🛠️ Development

本项目目前保持轻量化设计，不依赖第三方库。

核心功能主要建立在 Python 标准库之上：

```python
base64.b64encode()
base64.b64decode()
Path.read_bytes()
Path.write_bytes()
mimetypes.guess_type()
```

这使得项目可以在安装 Python 后直接运行。

---

## 📄 License

This project is provided for learning and personal use.

You may modify and redistribute the code according to the terms of the license included in this repository.