# 🔄 Ciphey 依赖环境更新

> **更新日期**: 2025年11月1日  
> **版本**: 5.14.1  
> **状态**: ✅ 完成

## 📋 快速概览

本次更新将 Ciphey 从 Python 3.7 环境升级到 Python 3.8+，并更新了所有依赖包到最新稳定版本。**所有功能保持不变，完全向后兼容（除了 Python 版本要求）。**

## 🚀 快速开始

### 安装前提

- **Python 3.8 或更高版本**

### 安装步骤

```bash
# 1. 检查 Python 版本
python --version

# 2. 安装 Poetry (如果还没有)
pip install poetry

# 3. 安装依赖
poetry install

# 4. 验证安装
python verify_installation.py

# 5. 测试运行
poetry run ciphey -t "SGVsbG8gV29ybGQh"
```

## 📚 详细文档

- **[CHANGES_SUMMARY.md](CHANGES_SUMMARY.md)** - 完整的更改总结和技术细节
- **[UPGRADE_NOTES.md](UPGRADE_NOTES.md)** - 详细的升级指南和故障排除
- **[QUICK_START.md](QUICK_START.md)** - 快速安装和使用指南

## ✨ 主要更新

### 依赖更新

| 包名 | 旧版本 | 新版本 |
|------|--------|--------|
| Python | 3.7+ | 3.8+ |
| rich | 4-10 | 13.x |
| click | 7.1+ | 8.x |
| pywhat | 3.0 | 5.x |
| pylint | 2.6 | 3.x |
| flake8 | 3.8-5 | 6.x |

### 移除的依赖

- ❌ `typing_inspect` - Python 3.8+ 已内置
- ❌ `mock` - 使用标准库 `unittest.mock`

### 代码更新

- ✅ 移除 `typing_inspect` 依赖，使用内置 `typing.get_args` 和 `get_origin`
- ✅ 更新测试文件使用 `unittest.mock`
- ✅ 更新 Python 版本检查逻辑

## 🧪 验证安装

运行验证脚本：

```bash
python verify_installation.py
```

这将检查：
- ✅ Python 版本
- ✅ 所有依赖包
- ✅ Ciphey 核心功能
- ✅ 基本解密测试

## 📖 使用示例

```bash
# Base64 解密
ciphey -t "SGVsbG8gV29ybGQh"

# 从文件读取
ciphey -f encrypted.txt

# 静默模式
ciphey -t "加密文本" -q

# 详细模式
ciphey -t "加密文本" -v
```

## 🔧 故障排除

### Python 版本过低

```bash
# 检查版本
python --version

# 如果 < 3.8，请从以下网址下载新版本：
# https://www.python.org/downloads/
```

### 安装依赖失败

```bash
# 清理缓存
poetry cache clear pypi --all

# 重新安装
poetry install
```

### cipheycore 或 cipheydists 安装失败

这些包需要编译环境：

- **Windows**: 安装 [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Linux**: `sudo apt install build-essential python3-dev`
- **macOS**: `xcode-select --install`

## 🆘 获取帮助

- 📖 查看 [Wiki](https://github.com/Ciphey/Ciphey/wiki)
- 🐛 提交 [Issue](https://github.com/Ciphey/Ciphey/issues)
- 💬 加入 [Discord](http://discord.skerritt.blog)

## ✅ 兼容性

### 支持的环境

- ✅ Python 3.8+
- ✅ Windows 10/11 (64-bit)
- ✅ macOS 10.15+
- ✅ Linux (所有主流发行版)

### 不再支持

- ❌ Python 3.7 及更早版本
- ❌ Windows 32-bit

## 🎯 功能验证清单

所有原有功能完全保留：

- ✅ 50+ 加密/编码支持
- ✅ 自动识别加密类型
- ✅ 命令行界面
- ✅ Python API
- ✅ 配置文件支持
- ✅ 多语言支持
- ✅ 所有检测器和破解器

## 📝 更新的文件

### 核心文件
- `pyproject.toml` - 依赖配置
- `ciphey/iface/_registry.py` - 移除 typing_inspect
- `ciphey/__main__.py` - Python 版本检查

### 测试文件
- `tests/test_advanced_ciphers.py`
- `tests/test_click.py`
- `tests/test_click_printing.py`
- `tests/test_quick.py`

### 新增文件
- `requirements.txt` - pip 依赖文件
- `UPGRADE_NOTES.md` - 升级指南
- `QUICK_START.md` - 快速开始指南
- `CHANGES_SUMMARY.md` - 更改总结
- `verify_installation.py` - 安装验证脚本
- `UPDATE_README.md` - 本文件

## 🔄 从旧版本迁移

```bash
# 1. 备份（可选）
cp pyproject.toml pyproject.toml.backup

# 2. 更新代码
git pull

# 3. 清理旧环境
poetry env remove python
rm -rf .venv

# 4. 重新安装
poetry install

# 5. 验证
python verify_installation.py
```

## 📊 测试

运行完整测试套件：

```bash
# 基础测试
poetry run pytest

# 带覆盖率
poetry run pytest --cov=ciphey

# 特定测试
poetry run pytest tests/test_quick.py
```

## 💡 提示

1. 使用 `verify_installation.py` 确保一切正常
2. 查看 `QUICK_START.md` 了解基本用法
3. 遇到问题查看 `UPGRADE_NOTES.md`
4. 加入 Discord 获取实时帮助

---

**准备好了吗？开始使用更新后的 Ciphey！** 🎉

```bash
poetry run ciphey -t "VGhpcyBpcyBhIHRlc3Qh"
```
