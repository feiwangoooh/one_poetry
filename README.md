## 一句话诗词

**作者：** feiwangoooh  
**版本：** 0.0.1  
**类型：** 工具  

### 描述
随机返回一句古诗词名句

### 插件说明
这是一个基于 [古诗词·一言API](http://gushi.ci/) 开发的 Dify 插件，可以随机返回一句古诗词名句。该插件无需任何凭据或其他配置信息，调用工具即可获得随机的古典诗词句子及其作者和出处信息。

### 功能特性
- 随机返回一句古诗词名句
- 自动包含作者和出处信息
- 无需凭据或额外配置
- 基于 **Dify** 插件构建

### 使用截图
<img src="/home/feiw/PycharmProjects/DifyPlugins/one_poetry/images/1.png" width="1056" height="210">
<img src="/home/feiw/PycharmProjects/DifyPlugins/one_poetry/images/2.png" width="1295" height="713">

### 致谢
在此感谢[古诗词·一言API](http://gushi.ci/)的作者对中国传统文化的贡献

### 实现细节
该插件通过向古诗词·一言API (`https://v1.jinrishici.com/all.json`) 发送请求并格式化响应来工作，返回内容包括：
- 诗词句子
- 作者
- 原始作品

实现在 [tools/one_poetry.py](tools/one_poetry.py) 文件中，使用 Python 和 requests 库完成。