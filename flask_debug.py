"""
这个脚本可以使用Virtual Studio Code的debug mode直接运行Flask脚本。
相对而言便于测试。
"""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
