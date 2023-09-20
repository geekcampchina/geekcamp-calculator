# geekcamp-calculator

基于 ANTLR4 编写的 Python 计算器 DEMO

## 环境准备

```bash
poetry install

poetry shell

which antlr4

antlr4 -Xexact-output-dir -o calculator/antlr4 -Dlanguage=Python3 calculator/grammar/CalculatorLexer.g4
antlr4 -Xexact-output-dir -o calculator/antlr4 -listener -visitor -Dlanguage=Python3 calculator/grammar/CalculatorParser.g4 calculator/grammar/CalculatorLexer.g4

exit
```

## 单元测试

```bash
poetry run pytest -s
```

## 本地安装

```bash
poetry build -f wheel
pip install -U --user dist/geekcamp_calculator-*-py3-none-any.whl
```

列出 Python 包文件列表：

```bash
pip show geekcamp-calculator -f
```

终端输出：

    Name: geekcamp-calculator
    Version: 0.0.1.0
    Summary:
    Home-page:
    Author: FifiLyu
    Author-email: fifilyu@gmail.com
    License:
    Location: /home/user/.local/lib/python3.11/site-packages
    Requires: antlr4-python3-runtime, antlr4-tools, pytest
    Required-by:
    Files:
      ../../../bin/pycalculator
      __pycache__/gkcalculator.cpython-311.pyc
      calculator/Calculator.py
      calculator/__init__.py
      calculator/__pycache__/Calculator.cpython-311.pyc
      calculator/__pycache__/__init__.cpython-311.pyc
      calculator/__pycache__/common.cpython-311.pyc
      calculator/antlr4/CalculatorLexer.interp
      calculator/antlr4/CalculatorLexer.py
      calculator/antlr4/CalculatorLexer.tokens
      calculator/antlr4/CalculatorParser.interp
      calculator/antlr4/CalculatorParser.py
      calculator/antlr4/CalculatorParser.tokens
      calculator/antlr4/CalculatorParserListener.py
      calculator/antlr4/CalculatorParserVisitor.py
      calculator/antlr4/__pycache__/CalculatorLexer.cpython-311.pyc
      calculator/antlr4/__pycache__/CalculatorParser.cpython-311.pyc
      calculator/antlr4/__pycache__/CalculatorParserListener.cpython-311.pyc
      calculator/antlr4/__pycache__/CalculatorParserVisitor.cpython-311.pyc
      calculator/common.py
      calculator/grammar/CalculatorLexer.g4
      calculator/grammar/CalculatorParser.g4
      calculator/parser/CalculatorBailLexer.py
      calculator/parser/CustomErrorListener.py
      calculator/parser/__init__.py
      calculator/parser/__pycache__/CalculatorBailLexer.cpython-311.pyc
      calculator/parser/__pycache__/CustomErrorListener.cpython-311.pyc
      calculator/parser/__pycache__/__init__.cpython-311.pyc
      geekcamp_calculator-0.0.1.0.dist-info/INSTALLER
      geekcamp_calculator-0.0.1.0.dist-info/LICENSE
      geekcamp_calculator-0.0.1.0.dist-info/METADATA
      geekcamp_calculator-0.0.1.0.dist-info/RECORD
      geekcamp_calculator-0.0.1.0.dist-info/REQUESTED
      geekcamp_calculator-0.0.1.0.dist-info/WHEEL
      geekcamp_calculator-0.0.1.0.dist-info/direct_url.json
      geekcamp_calculator-0.0.1.0.dist-info/entry_points.txt
      gkcalculator.py

## 使用方法

获取命令行工具执行路径：

```bash
python -c "import site; print('%s/bin/pycalculator' % site.USER_BASE)"
```

终端输出：

    ~/.local/bin/pycalculator

### 运行

```bash
~/.local/bin/pycalculator
```

分别输入 `1+1==2;`、`1+1=2;`

操作演示：

    2023-09-20 00:36:09 94943 [INFO] 未启用日志配置文件，加载默认设置
    请输入表达式： 1+1==2;
    2023-09-20 00:36:13 94943 [INFO] 语法识别：

        1+1==2;


    2023-09-20 00:36:13 94943 [DEBUG] Calculator.Antlr4->语法分析成功
