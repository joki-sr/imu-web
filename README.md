## 准备
```commandline
cd imu_web_demo
```
创建一个名为 venv 的虚拟环境。
```commandline
python -m venv venv
```
激活虚拟环境
venv\Scripts\activate
激活后，前面会看到 (venv)，比如：
(venv) C:\Users\你的用户名\Documents\imu_web_demo>

安装 Flask
pip install flask

在虚拟环境中运行你写好的 server.py：
python server.py

点击链接访问localhost5050

如果你想退出虚拟环境，在终端里输入：deactivate

---
## 运行
### 后端
terminal
```commandline
venv\Scripts\activate
（venv）python server.py
```
ngrok terminal
```commandline
D:\Programe\ngrok-v3-stable-windows-amd64> ngrok http 5000
# 复制网址
```

### 前端
访问网址即可