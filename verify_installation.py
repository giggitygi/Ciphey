#!/usr/bin/env python3
"""
Ciphey 安装验证脚本

这个脚本用于验证 Ciphey 的依赖更新是否成功，所有功能是否正常。
"""

import sys
import importlib
from typing import List, Tuple

def check_python_version() -> Tuple[bool, str]:
    """检查 Python 版本"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        return True, f"✅ Python {version.major}.{version.minor}.{version.micro}"
    else:
        return False, f"❌ Python {version.major}.{version.minor}.{version.micro} (需要 3.8+)"

def check_module(module_name: str) -> Tuple[bool, str]:
    """检查模块是否可以导入"""
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "未知版本")
        return True, f"✅ {module_name} ({version})"
    except ImportError as e:
        return False, f"❌ {module_name} - 导入失败: {str(e)}"
    except Exception as e:
        return False, f"❌ {module_name} - 错误: {str(e)}"

def check_typing_features() -> Tuple[bool, str]:
    """检查 typing 模块的功能"""
    try:
        from typing import get_args, get_origin
        # 测试功能
        from typing import List
        args = get_args(List[int])
        origin = get_origin(List[int])
        if args == (int,) and origin is list:
            return True, "✅ typing.get_args 和 get_origin 工作正常"
        else:
            return False, "❌ typing 功能测试失败"
    except ImportError:
        return False, "❌ 无法从 typing 导入 get_args 和 get_origin"
    except Exception as e:
        return False, f"❌ typing 功能测试错误: {str(e)}"

def check_ciphey_import() -> Tuple[bool, str]:
    """检查 Ciphey 是否可以导入"""
    try:
        import ciphey
        from ciphey import decrypt
        from ciphey.iface import Config
        return True, "✅ Ciphey 核心模块导入成功"
    except ImportError as e:
        return False, f"❌ Ciphey 导入失败: {str(e)}"
    except Exception as e:
        return False, f"❌ Ciphey 导入错误: {str(e)}"

def test_basic_functionality() -> Tuple[bool, str]:
    """测试基本的解密功能"""
    try:
        from ciphey import decrypt
        from ciphey.iface import Config
        
        # 测试 Base64 解密
        config = Config().library_default().complete_config()
        result = decrypt(config, "SGVsbG8gV29ybGQh")
        
        if "Hello World" in result:
            return True, "✅ 基本解密功能正常 (Base64 测试通过)"
        else:
            return False, f"❌ 解密结果不正确: {result}"
    except Exception as e:
        return False, f"❌ 功能测试失败: {str(e)}"

def main():
    """主函数"""
    print("=" * 60)
    print("Ciphey 安装验证")
    print("=" * 60)
    print()
    
    checks = [
        ("Python 版本", check_python_version()),
        ("typing 功能", check_typing_features()),
    ]
    
    # 检查核心依赖
    core_modules = [
        "rich",
        "yaml",  # PyYAML 导入为 yaml
        "click",
        "appdirs",
        "base58",
        "base91",
        "pybase62",
        "pywhat",
        "cipheydists",
        "cipheycore",
    ]
    
    for module in core_modules:
        checks.append((f"模块: {module}", check_module(module)))
    
    # 检查 Ciphey
    checks.append(("Ciphey 导入", check_ciphey_import()))
    
    # 测试功能
    checks.append(("功能测试", test_basic_functionality()))
    
    # 打印结果
    success_count = 0
    fail_count = 0
    
    for name, (success, message) in checks:
        print(f"{name:.<40} {message}")
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    print()
    print("=" * 60)
    print(f"总计: {success_count} 成功, {fail_count} 失败")
    print("=" * 60)
    
    if fail_count == 0:
        print()
        print("🎉 所有检查通过！Ciphey 已准备就绪。")
        print()
        print("你可以开始使用 Ciphey:")
        print("  poetry run ciphey -t \"你的加密文本\"")
        print("  或")
        print("  ciphey -t \"你的加密文本\"")
        print()
        return 0
    else:
        print()
        print("⚠️  发现问题，请检查失败的项目。")
        print()
        print("常见解决方案:")
        print("1. 确保 Python 版本 >= 3.8")
        print("2. 重新安装依赖: poetry install")
        print("3. 清理缓存: poetry cache clear pypi --all")
        print("4. 查看 UPGRADE_NOTES.md 获取更多帮助")
        print()
        return 1

if __name__ == "__main__":
    sys.exit(main())
