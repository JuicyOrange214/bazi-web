#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
八字排盘 Web 应用 - Flask 后端
"""
import os
import sys
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 添加八字脚本路径
BAZI_SCRIPTS_PATH = os.path.join(os.path.dirname(__file__), "bazi")
sys.path.insert(0, BAZI_SCRIPTS_PATH)

from bazi_calculator import compute_bazi_and_dayun


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/bazi", methods=["POST"])
def calculate_bazi():
    """接收前端数据，返回八字排盘结果"""
    data = request.get_json()
    
    # 解析参数
    year = data.get("year")
    month = data.get("month")
    day = data.get("day")
    hour = data.get("hour")
    minute = data.get("minute", 0)
    gender = data.get("gender", "女")
    city = data.get("city", "武汉")
    name = data.get("name", "访客")
    
    # 验证必填字段
    if not all([year, month, day, hour]):
        return jsonify({"error": "缺少必要的出生信息"}), 400
    
    try:
        result = compute_bazi_and_dayun(
            year=int(year),
            month=int(month),
            day=int(day),
            hour=int(hour),
            minute=int(minute),
            gender=gender,
            city=city
        )
        
        # 获取流年信息
        liu_nian_info = _extract_liu_nian_info(result)
        
        return jsonify({
            "success": True,
            "name": name,
            "gender": gender,
            "birth_info": {
                "year": year,
                "month": month,
                "day": day,
                "hour": hour,
                "minute": minute,
                "city": city
            },
            "bazi_data": result,
            "liu_nian": liu_nian_info
        })
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"计算失败: {str(e)}"}), 500


def _extract_liu_nian_info(result):
    """从八字结果中提取流年信息"""
    from datetime import datetime
    
    current_year = datetime.now().year
    liunian = {}
    
    try:
        dayun_list = result.get("dayun", {}).get("dayun_list", [])
        for dayun in dayun_list:
            for liu in dayun.get("liu_nian", []):
                year = liu.get("year")
                if year and abs(year - current_year) <= 3:
                    age_xu = liu.get("age_xu", 0)
                    gan_zhi = liu.get("gan_zhi", "")
                    liunian[str(year)] = {
                        "gan_zhi": gan_zhi,
                        "age_xu": age_xu
                    }
    except Exception:
        pass
    
    return liunian


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
