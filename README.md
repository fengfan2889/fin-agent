# Fin-Agent: 智能金融分析代理

Fin-Agent 是一个基于 **DeepSeek** 大模型和 **Tushare** 金融数据的智能金融分析代理。它能够通过自然语言交互，帮助用户查询股票行情、分析财务数据、获取市场指标，并提供投资参考建议。

## ✨ 主要功能

- **自然语言交互**：直接使用中文与 AI 对话，无需记忆复杂的命令或代码。
- **实时行情查询**：获取股票的最新实时报价、成交量等数据。
- **历史数据分析**：查询股票的历史日线数据，分析价格走势。
- **基本面数据**：获取股票的 PE (市盈率)、PB (市净率)、市值、换手率等关键指标。
- **财务报表分析**：查询上市公司的营收、净利润等财务数据，辅助基本面分析。
- **智能诊断**：结合 LLM 的分析能力，对获取的数据进行解读和总结。

## 🛠️ 安装指南

### 1. 克隆项目

```bash
git clone https://github.com/YUHAI0/fin-agent
cd fin-agent
```

### 2. 安装依赖

建议使用 Python 3.8+ 环境。

```bash
pip install -r requirements.txt
```

或者通过 setup.py 安装：

```bash
pip install .
```

## ⚙️ 配置说明

Fin-Agent 需要以下两个 API 密钥才能正常工作：

1.  **Tushare Token**: 用于获取金融数据 ([注册 Tushare](https://tushare.pro/))
2.  **DeepSeek API Key**: 用于驱动智能对话 ([注册 DeepSeek](https://www.deepseek.com/))

### 自动配置
首次运行程序时，如果没有检测到配置文件，Fin-Agent 会自动进入设置向导，引导您输入 API 密钥。配置将自动保存到您的用户目录下。

### 手动配置
您也可以在项目根目录下创建一个 `.env` 文件，手动填写配置：

```env
TUSHARE_TOKEN=your_tushare_token_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

## 🚀 使用方法

### 启动代理

在项目根目录下运行：

```bash
python main.py
```

或者如果已经安装到系统路径：

```bash
fin-agent
```

### 对话示例

启动后，您可以直接向 Agent 提问，例如：

*   "平安银行现在的股价是多少？"
*   "帮我看看贵州茅台最近一个月的走势怎么样？"
*   "查询一下万科A的市盈率和市净率。"
*   "宁德时代去年的营收和净利润是多少？"
*   "最近大盘（上证指数）表现如何？"

## 📊 数据来源

*   **金融数据**: [Tushare Pro](https://tushare.pro/) - 专业免费的财经数据接口包。
*   **大模型**: [DeepSeek](https://www.deepseek.com/) - 深度求索开源大模型。

## 📝 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。
