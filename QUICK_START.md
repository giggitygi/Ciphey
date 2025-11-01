# Ciphey 快速安装和测试指南

## 简易安装步骤

### 方法 1: 使用 Poetry（推荐）

1. **安装 Poetry**
```bash
pip install poetry
```

2. **安装 Ciphey 依赖**
```bash
poetry install
```

3. **测试运行**
```bash
poetry run ciphey -t "SGVsbG8gV29ybGQh"
```

### 方法 2: 使用 pip

1. **从 requirements.txt 安装**
```bash
pip install -r requirements.txt
```

2. **安装 Ciphey**
```bash
pip install -e .
```

3. **测试运行**
```bash
ciphey -t "SGVsbG8gV29ybGQh"
```

## 验证安装

运行以下命令验证 Ciphey 是否正常工作：

```bash
# 测试 Base64 解码
ciphey -t "SGVsbG8gV29ybGQh"

# 应该输出: Hello World!
```

## 运行测试套件

```bash
# 使用 Poetry
poetry run pytest

# 或使用 pip
pytest
```

## 常见问题

### Q: 提示 Python 版本太低？
A: 升级到 Python 3.8 或更高版本：https://www.python.org/downloads/

### Q: cipheydists 或 cipheycore 安装失败？
A: 这些包需要编译，请确保：
- Windows: 安装 Visual C++ Build Tools
- Linux: 安装 build-essential 和 python3-dev
- macOS: 安装 Xcode Command Line Tools

### Q: 如何卸载旧版本？
A: 
```bash
pip uninstall ciphey
pip cache purge
```

## 功能测试示例

```bash
# Base64
ciphey -t "SGVsbG8gV29ybGQh"

# Caesar cipher
ciphey -t "uryyb jbeyq"

# 多层编码
ciphey -t "VTJobGJHOGdWMjl5YkdRaA=="

# 从文件读取
ciphey -f encrypted.txt

# 安静模式
ciphey -t "SGVsbG8gV29ybGQh" -q
```

## 需要帮助？

- GitHub Issues: https://github.com/Ciphey/Ciphey/issues
- Wiki: https://github.com/Ciphey/Ciphey/wiki
- Discord: http://discord.skerritt.blog
