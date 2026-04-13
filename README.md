# 八字排盘 Web 应用

现代简约风格的八字命理排盘工具。

## 功能
- 四柱排盘（年柱、月柱、日柱、时柱）
- 大运流年
- 喜忌神
- 真太阳时校正

## 部署到 Replit

1. 打开 https://replit.com
2. 注册/登录账号
3. 点击 "Create Repl" → 选择 "Python" 模板
4. 删除默认的 `main.py`
5. 上传本项目所有文件：
   - `app.py`
   - `templates/index.html`
   - `bazi/` 文件夹（含 bazi_calculator.py, bazi_core.py, jieqi_loader.py）
   - `references/` 文件夹（含 cities.json）
   - `requirements.txt`
6. 点 "Run" 即可运行
7. Replit 会自动安装 `requirements.txt` 中的依赖

## 本地运行

```bash
pip install -r requirements.txt
python app.py
```

然后访问 http://localhost:5000
