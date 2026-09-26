# Base64 Glyph

> A lightweight Python utility for converting between text, images, and Base64.

**Base64 Glyph** 是一个基于 Python 标准库实现的轻量级 Base64 转换工具。

它支持文字与 Base64、图片与 Base64 文件之间的双向转换，并通过文件读写避免处理大型 Base64 数据时受到终端输入长度限制。

## ✨ Features

- 📝 Text → Base64
- 🔤 Base64 → Text
- 🖼️ Image → Base64
- 📦 Base64 → Image
- 🌐 支持 Base64 Data URI
- 📁 通过 `input/` 和 `output/` 管理文件
- 🧩 自动识别常见图片格式
- 🚫 无第三方依赖

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- 无需安装第三方 Python 包

项目使用的全部模块均来自 Python 标准库：

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

可选：创建 Python 虚拟环境：

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

启动后会显示：

```text
========================================
        Base64 转换工具
========================================
1. 文字 → Base64
2. Base64 → 文字
3. 图片 → Base64 文件
4. Base64 文件 → 图片
0. 退出

请选择模式：
```

输入对应编号即可选择功能。

---

## 📝 Text → Base64

选择：

```text
1
```

然后在终端输入文字：

```text
请输入文字：love is love
```

程序会直接输出：

```text
bG92ZSBpcyBsb3Zl
```

文本使用 UTF-8 编码，因此支持中文及其他 Unicode 字符。

---

## 🔤 Base64 → Text

选择：

```text
2
```

输入 Base64：

```text
bG92ZSBpcyBsb3Zl
```

程序会输出：

```text
love is love
```

该模式适合处理较短的文本数据。

对于非常长的 Base64 数据，建议使用文件模式。

---

## 🖼️ Image → Base64

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

程序会扫描 `input/` 中的图片并显示选择菜单：

```text
找到以下图片：

1. image.jpg
2. image.png
3. image.webp

请选择图片编号：
```

选择后，Base64 数据会保存到：

```text
output/
```

例如：

```text
output/
└── image.base64
```

文件内容类似：

```text
data:image/jpeg;base64,/9j/4AAQSkZJRg...
```

### 支持的图片格式

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

---

## 📦 Base64 → Image

将 Base64 文件放入：

```text
input/
```

例如：

```text
input/
└── image.base64
```

程序支持：

- `.base64`
- `.txt`

选择：

```text
4
```

程序会读取文件中的 Base64 数据并自动解码。

如果输入包含 Data URI：

```text
data:image/png;base64,iVBORw0KGgo...
```

程序会根据 MIME Type 自动判断图片扩展名。

最终生成：

```text
output/
└── image.png
```

---

## 🌐 Data URI

Image → Base64 模式默认生成 Data URI：

```text
data:image/png;base64,iVBORw0KGgo...
```

其结构为：

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