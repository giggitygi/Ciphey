# Ciphey 依赖更新说明

## 概述
本次更新将 Ciphey 的依赖环境从 Python 3.7 升级到 Python 3.8+，并更新了所有主要依赖包到最新的稳定版本，同时保持功能完全不变。

## 主要变更

### 1. Python 版本要求
- **旧版本**: Python 3.7+
- **新版本**: Python 3.8+
- **原因**: Python 3.8 已内置 `typing.get_args` 和 `typing.get_origin`，无需 `typing_inspect` 依赖

### 2. 依赖包更新

#### 核心依赖
| 包名 | 旧版本 | 新版本 | 说明 |
|------|--------|--------|------|
| `python` | ^3.7 | ^3.8 | 升级到 Python 3.8+ |
| `rich` | >=4,<11 | >=13.0.0,<14.0.0 | 更新到最新稳定版 |
| `pyyaml` | >=5.3.1,<7.0.0 | >=6.0,<7.0.0 | 升级到 6.x 版本 |
| `pylint` | ^2.6.0 | ^3.0.0 | 升级到 3.x 版本 |
| `flake8` | >=3.8.4,<5.0.0 | >=6.0.0,<8.0.0 | 升级到 6.x 版本 |
| `base58` | ^2.0.1 | ^2.1.0 | 升级到最新版本 |
| `pybase62` | >=0.4.3,<0.6.0 | >=0.5.0,<1.0.0 | 升级版本范围 |
| `click` | >=7.1.2,<9.0.0 | >=8.0.0,<9.0.0 | 升级到 8.x 版本 |
| `pywhat` | 3.0.0 | >=5.0.0,<6.0.0 | 升级到 5.x 版本 |

#### 移除的依赖
- `typing_inspect`: 已移除，使用 Python 3.8+ 内置的 typing 功能替代
- `mock`: 已移除，Python 3.8+ 可使用内置的 `unittest.mock`
- `neovim`: 从开发依赖中移除（非核心功能）

#### 开发依赖
| 包名 | 旧版本 | 新版本 |
|------|--------|--------|
| `pytest-cov` | ^3.0.0 | ^4.0.0 |
| `pytest` | ^7.1.2 | ^7.4.0 |
| `black` | ^21.4b2 | ^23.0.0 |
| `sphinx` | ^5.0.1 | ^7.0.0 |
| `sphinx-autodoc-typehints` | ^1.11.1 | ^1.24.0 |
| `nltk` | ^3.5 | ^3.8 |

### 3. 代码修改

#### `ciphey/iface/_registry.py`
```python
# 旧代码
try:
    from typing import get_args, get_origin
except ImportError:
    from typing_inspect import get_origin, get_args

# 新代码
from typing import Any, Dict, List, Optional, Set, Tuple, Type, Union, get_args, get_origin
```

#### `ciphey/__main__.py`
- 更新 Python 版本检查从 3.6+ 到 3.8+
- 移除了 Windows 上 Python 3.9 的限制（原有限制已过时）
- 简化了 32 位系统检查逻辑

## 安装指南

### 使用 Poetry（推荐）
```bash
# 确保你已安装 Python 3.8 或更高版本
python --version

# 安装 poetry（如果尚未安装）
pip install poetry

# 安装依赖
poetry install

# 运行 Ciphey
poetry run ciphey -t "加密文本"
```

### 使用 pip
```bash
# 从源码安装
pip install .

# 或开发模式安装
pip install -e .
```

## 兼容性说明

### ✅ 兼容的系统
- Python 3.8+
- Windows 10/11 (64-bit)
- macOS 10.15+
- Linux (所有主流发行版)

### ❌ 不再支持
- Python 3.7 及更早版本
- Windows 32-bit 系统

## 功能验证

所有原有功能均保持不变：
- ✅ 所有加密/解密算法
- ✅ 命令行界面
- ✅ API 接口
- ✅ 配置文件支持
- ✅ 多语言支持
- ✅ 所有检测器和破解器

## 测试

运行测试套件以验证功能：
```bash
# 使用 poetry
poetry run pytest

# 或使用 pip
pytest
```

## 故障排除

### 问题: 安装失败，提示 Python 版本不兼容
**解决方案**: 升级到 Python 3.8 或更高版本
```bash
# 检查当前版本
python --version

# 下载最新版本
# 访问 https://www.python.org/downloads/
```

### 问题: 某些包安装失败
**解决方案**: 清理缓存并重新安装
```bash
poetry cache clear pypi --all
poetry install
```

### 问题: `cipheydists` 或 `cipheycore` 安装失败
**解决方案**: 这些是核心依赖，如果安装失败，可能需要：
1. 确保安装了编译工具（Windows 需要 Visual C++ Build Tools）
2. 尝试使用预编译的轮子文件
3. 参考官方文档：https://github.com/Ciphey/Ciphey/wiki/Installation

## 迁移清单

- [ ] 验证 Python 版本 >= 3.8
- [ ] 备份现有环境（可选）
- [ ] 更新代码（git pull 或下载更新后的代码）
- [ ] 重新安装依赖 (`poetry install` 或 `pip install .`)
- [ ] 运行测试套件验证功能
- [ ] 测试你的常用工作流程

## 回滚方案

如果遇到问题，可以回滚到旧版本：
```bash
git checkout <previous-commit-hash>
poetry install
```

## 贡献

如果你在更新过程中发现任何问题，请：
1. 在 GitHub 上创建 Issue
2. 加入 Discord 寻求帮助
3. 查看 Wiki 文档

## 更新日期
2025年11月1日
