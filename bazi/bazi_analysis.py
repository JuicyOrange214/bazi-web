# -*- coding: utf-8 -*-
"""
八字文字解读分析模块
为不懂命理的用户提供通俗易懂的解读
"""

# 天干五行
GAN_WUXING = {
    "甲": "木", "乙": "木",
    "丙": "火", "丁": "火",
    "戊": "土", "己": "土",
    "庚": "金", "辛": "金",
    "壬": "水", "癸": "水"
}

# 地支五行
ZHI_WUXING = {
    "子": "水", "丑": "土", "寅": "木", "卯": "木",
    "辰": "土", "巳": "火", "午": "火", "未": "土",
    "申": "金", "酉": "金", "戌": "土", "亥": "水"
}

# 五行颜色（用于标签）
WUXING_CN = {"木": "wood", "火": "fire", "土": "earth", "金": "metal", "水": "water"}

WUXING_LABELS = {"木": "木", "火": "火", "土": "土", "金": "金", "水": "水"}

# 天干阴阳
GAN_YINYANG = {
    "甲": "阳", "乙": "阴",
    "丙": "阳", "丁": "阴",
    "戊": "阳", "己": "阴",
    "庚": "阳", "辛": "阴",
    "壬": "阳", "癸": "阴"
}

# 日干对应的十神名称
TEN_GODS = {
    # 日主为甲
    "甲": {"甲": "比肩", "乙": "劫财", "丙": "食神", "丁": "伤官", "戊": "偏财", "己": "正财", "庚": "偏官", "辛": "正官", "壬": "偏印", "癸": "正印"},
    # 日主为乙
    "乙": {"甲": "劫财", "乙": "比肩", "丙": "伤官", "丁": "食神", "戊": "正财", "己": "偏财", "庚": "正官", "辛": "偏官", "壬": "正印", "癸": "偏印"},
    # 日主为丙
    "丙": {"甲": "偏印", "乙": "正印", "丙": "比肩", "丁": "劫财", "戊": "食神", "己": "伤官", "庚": "偏财", "辛": "正财", "壬": "偏官", "癸": "正官"},
    # 日主为丁
    "丁": {"甲": "正印", "乙": "偏印", "丙": "劫财", "丁": "比肩", "戊": "伤官", "己": "食神", "庚": "正财", "辛": "偏财", "壬": "正官", "癸": "偏官"},
    # 日主为戊
    "戊": {"甲": "偏财", "乙": "正财", "丙": "偏印", "丁": "正印", "戊": "比肩", "己": "劫财", "庚": "食神", "辛": "伤官", "壬": "偏官", "癸": "正官"},
    # 日主为己
    "己": {"甲": "正财", "乙": "偏财", "丙": "正印", "丁": "偏印", "戊": "劫财", "己": "比肩", "庚": "伤官", "辛": "食神", "壬": "正官", "癸": "偏官"},
    # 日主为庚
    "庚": {"甲": "偏官", "乙": "正官", "丙": "偏财", "丁": "正财", "戊": "偏印", "己": "正印", "庚": "比肩", "辛": "劫财", "壬": "食神", "癸": "伤官"},
    # 日主为辛
    "辛": {"甲": "正官", "乙": "偏官", "丙": "正财", "丁": "偏财", "戊": "正印", "己": "偏印", "庚": "劫财", "辛": "比肩", "壬": "伤官", "癸": "食神"},
    # 日主为壬
    "壬": {"甲": "食神", "乙": "伤官", "丙": "偏财", "丁": "正财", "戊": "偏官", "己": "正官", "庚": "偏印", "辛": "正印", "壬": "比肩", "癸": "劫财"},
    # 日主为癸
    "癸": {"甲": "伤官", "乙": "食神", "丙": "正财", "丁": "偏财", "戊": "正官", "己": "偏官", "庚": "正印", "辛": "偏印", "壬": "劫财", "癸": "比肩"},
}

# 月令地支对应的旺度
MONTH_ZHI_STRENGTH = {
    "寅": 100, "卯": 100,  # 木月
    "巳": 80,  "午": 80,   # 火月
    "申": 70,  "酉": 70,   # 金月
    "亥": 70,  "子": 70,   # 水月
    "辰": 60,  "戌": 60,  "丑": 60,  "未": 60,  # 土月（墓月）
}

# 十神性格描述
TEN_GOD_NATURE = {
    "比肩": "独立、自主、有主见、坚定",
    "劫财": "豪爽、义气、冲动、竞争",
    "食神": "温和、善良、表达力、享受",
    "伤官": "聪明、创意、叛逆、口才",
    "偏财": "慷慨、圆滑、财运、交际",
    "正财": "务实、节约、稳重、守成",
    "偏官": "果断、魄力、压力、竞争",
    "正官": "规矩、正统、责任、名望",
    "偏印": "悟性、创意、孤僻、钻研",
    "正印": "仁慈、包容、学习、教化",
}

# 五行性格特征
WUXING_NATURE = {
    "木": {
        "yang": "积极向上、有仁心、有主见、喜欢成长",
        "yin": "温和善良、有同情心、注重感情"
    },
    "火": {
        "yang": "热情开朗、行动力强、追求目标",
        "yin": "温柔体贴、富有表现力、善于交际"
    },
    "土": {
        "yang": "稳重踏实、忠诚守信、包容厚道",
        "yin": "细腻敏感、固执保守、重视传统"
    },
    "金": {
        "yang": "果断坚定、刚毅正直、注重原则",
        "yin": "细腻敏锐、有审美、善于决策"
    },
    "水": {
        "yang": "聪明智慧、适应力强、善于谋略",
        "yin": "温柔浪漫、情感丰富、直觉敏锐"
    },
}

# 大运好坏判断
DAYUN_ANALYSIS = {
    "木": {
        "喜": ["利文化、学术、教育、艺术领域发展", "思维活跃、有创造力", "人际关系和谐"],
        "忌": ["容易犹豫不决、行动力不足", "压力增大、健康波动"]
    },
    "火": {
        "喜": ["事业上升期、知名度提升", "财运亨通、机遇增多", "行动力十足"],
        "忌": ["情绪波动、争执是非", "健康注意心脏"]
    },
    "土": {
        "喜": ["财运稳定、积累财富", "人脉拓展、事业稳固", "适宜创业或守成"],
        "忌": ["保守固执、错失机会", "身体注意脾胃"]
    },
    "金": {
        "喜": ["事业突破、地位提升", "财运佳、贵人相助", "决策力增强"],
        "忌": ["压力过大、小人是非", "肺呼吸系统注意"]
    },
    "水": {
        "喜": ["财运流动、智慧生财", "学业有利、考试顺利", "人际关系转好"],
        "忌": ["情绪波动、方向迷茫", "肾泌尿系统注意"]
    },
}


def get_wuxing_of_char(c):
    """获取单个字符的五行"""
    return GAN_WUXING.get(c) or ZHI_WUXING.get(c)


def get_wuxing_count(ganzhi_dict):
    """统计八字五行分布"""
    all_chars = (ganzhi_dict["year"] + ganzhi_dict["month"] +
                 ganzhi_dict["day"] + ganzhi_dict["hour"])
    counts = {"木": 0, "火": 0, "土": 0, "金": 0, "水": 0}
    for c in all_chars:
        w = get_wuxing_of_char(c)
        if w:
            counts[w] += 1
    return counts


def determine_strength(day_gan, month_zhi, wuxing_count):
    """判断日主强弱"""
    day_gan_yy = GAN_YINYANG[day_gan]
    day_gan_wx = GAN_WUXING[day_gan]

    # 月令旺度
    month_strength = MONTH_ZHI_STRENGTH.get(month_zhi, 50)

    # 计算总分
    self_score = 0  # 自坐
    peer_score = 0   # 同类（天干+地支）
    other_score = 0  # 克泄

    total = sum(wuxing_count.values())

    for wx, count in wuxing_count.items():
        if wx == day_gan_wx:
            if wx == "木":  # 乙木日主
                peer_score += count * 20
            elif wx == "金":
                peer_score += count * 20
            else:
                peer_score += count * 15
        elif wx in ["水", "火"]:  # 生我或我生
            other_score += count * 5
        else:  # 克我或我克
            other_score += count * 8

    # 身旺：月令旺 + 同类多 + 克泄少
    # 身弱：月令弱 + 同类少 + 克泄多
    strength_score = month_strength + peer_score - other_score

    if strength_score > 100:
        return "身旺", strength_score
    elif strength_score > 70:
        return "偏旺", strength_score
    elif strength_score > 40:
        return "中和", strength_score
    elif strength_score > 10:
        return "偏弱", strength_score
    else:
        return "身弱", strength_score


def determine_gods_and_harm(day_gan, wuxing_count, strength):
    """判断用神喜神忌神"""
    day_gan_wx = GAN_WUXING[day_gan]
    lack = [wx for wx, cnt in wuxing_count.items() if cnt == 0]

    # 身旺：用神为克泄耗，忌神为生助
    # 身弱：用神为印比生助，忌神为克泄耗
    if "身旺" in strength or "偏旺" in strength:
        if lack:
            use = lack[:]
            avoid = [wx for wx in ["木", "火", "土", "金", "水"] if wx not in lack and wx != day_gan_wx]
        else:
            avoid = [day_gan_wx]
            use = [wx for wx in ["水", "金"] if wx != day_gan_wx]
    else:  # 身弱
        use = ["水", day_gan_wx] if day_gan_wx in ["木", "火"] else ["金", "土"]
        avoid = [wx for wx in wuxing_count if wuxing_count[wx] >= 3 and wx != day_gan_wx]

    return use[:3], avoid[:3]


def get_dayun_interpretation(dayun_gan, dayun_zhi, is_current, day_gan, use_gods, avoid_gods, age_range):
    """解读单步大运"""
    wx = ZHI_WUXING.get(dayun_zhi, "土")
    gan_wx = GAN_WUXING.get(dayun_gan, "土")

    # 判断这步大运的五行对用神是助还是克
    helps = wx in use_gods or gan_wx in use_gods
    hurts = wx in avoid_gods or gan_wx in avoid_gods

    # 地支含义
    zhi_meanings = {
        "子": "事业拓展、财运流动", "丑": "积累沉淀、稳中求进",
        "寅": "发展进步、创业创新", "卯": "感情活跃、多方发展",
        "辰": "学业提升、才华展现", "巳": "财运上升、名利双收",
        "午": "名声提升、社交活跃", "未": "感情桃花、财运增长",
        "申": "事业转型、贵人相助", "酉": "财运积累、合作顺利",
        "戌": "财运稳固、投资获利", "亥": "学业考试、智慧提升",
    }

    base = zhi_meanings.get(dayun_zhi, "平稳发展")

    if is_current:
        tag = "当前大运"
        desc = f"这步大运以{dayun_gan}{dayun_zhi}为主调，{base}。"
    else:
        tag = f"{age_range}"
        desc = f"这步大运{dayun_gan}{dayun_zhi}，{base}。"

    if helps:
        mood = "用神到位，整体运势较好"
    elif hurts:
        mood = "忌神当令，需谨慎应对"
    else:
        mood = "平稳过渡，无大起大落"

    return {
        "period": tag,
        "ganzhi": f"{dayun_gan}{dayun_zhi}",
        "description": f"{desc} {mood}。"
    }


def analyze_bazi(ganzhi_dict, dayun_list, gender, birth_year):
    """生成完整的八字解读"""
    from datetime import datetime

    day_gan = ganzhi_dict["day"][0]
    month_zhi = ganzhi_dict["month"][1]
    day_zhi = ganzhi_dict["day"][1]
    hour_gan = ganzhi_dict["hour"][0]
    hour_zhi = ganzhi_dict["hour"][1]

    # 五行统计
    wx_count = get_wuxing_count(ganzhi_dict)

    # 八字强弱
    strength, score = determine_strength(day_gan, month_zhi, wx_count)

    # 用神喜忌
    use_gods, avoid_gods = determine_gods_and_harm(day_gan, wx_count, strength)

    # 日主五行性格
    day_gan_yy = GAN_YINYANG[day_gan]
    day_nature = WUXING_NATURE.get(GAN_WUXING[day_gan], {}).get(day_gan_yy, "")

    # 十神分析（时柱代表晚年/子女）
    ten_gods_map = TEN_GODS.get(day_gan, {})
    hour_shishen = ten_gods_map.get(hour_gan, "其他")
    month_shishen = ten_gods_map.get(ganzhi_dict["month"][0], "其他")

    # 当前年份
    current_year = datetime.now().year

    # 找当前大运
    current_dayun = None
    for du in dayun_list:
        if du.get("gan_zhi") == "小运":
            continue
        yr_range = du.get("year_range", "")
        if str(current_year) in yr_range:
            current_dayun = du
            break

    # 大运解读
    dayun_interpretations = []
    for du in dayun_list:
        if du.get("gan_zhi") == "小运":
            continue
        is_current = current_dayun and du.get("gan_zhi") == current_dayun.get("gan_zhi")
        interp = get_dayun_interpretation(
            du["gan_zhi"][0], du["gan_zhi"][1],
            is_current, day_gan, use_gods, avoid_gods, du.get("age_range", "")
        )
        dayun_interpretations.append(interp)

    # 流年解读（近3年）
    liunian_interps = []
    for du in dayun_list:
        for ln in du.get("liu_nian", []):
            yr = ln.get("year", 0)
            if abs(yr - current_year) <= 2:
                ln_gan = ln["gan_zhi"][0]
                ln_zhi = ln["gan_zhi"][1]
                ln_wx = GAN_WUXING.get(ln_gan, "土")
                ln_zhi_wx = ZHI_WUXING.get(ln_zhi, "土")

                # 简单流年判断
                if ln_wx in use_gods or ln_zhi_wx in use_gods:
                    ln_mood = "用神流年，运势较好"
                elif ln_wx in avoid_gods or ln_zhi_wx in avoid_gods:
                    ln_mood = "忌神流年，谨慎行事"
                else:
                    ln_mood = "平稳过渡"

                liunian_interps.append({
                    "year": str(yr),
                    "ganzhi": ln["gan_zhi"],
                    "age": f"{ln.get('age_xu', 0)}岁",
                    "description": f"{ln['gan_zhi'][0]}{ln['gan_zhi'][1]}年，{ln_mood}。"
                })

    # 五行缺什么
    lack = [wx for wx, cnt in wx_count.items() if cnt == 0]

    # 综述
    lack_str = f"五行缺{'、'.join(lack)}。" if lack else "五行齐全。"

    summary_parts = [
        f"日主{day_gan}{GAN_WUXING[day_gan]}，{strength}。{lack_str}",
        f"性格特点：{day_nature}。",
    ]
    if month_shishen != "其他":
        summary_parts.append(f"月柱透出{month_shishen}，代表事业心和行动力。")
    if hour_shishen != "其他":
        summary_parts.append(f"时柱见{hour_shishen}，与晚年/子女缘分相关。")

    return {
        "summary": "".join(summary_parts),
        "strength": {
            "level": strength,
            "score": score,
            "description": _strength_description(strength, day_gan, wx_count),
        },
        "wuxing": {
            "counts": wx_count,
            "lacking": lack,
        },
        "gods": {
            "use": use_gods,
            "avoid": avoid_gods,
            "use_description": _gods_description(use_gods, avoid_gods, strength),
        },
        "character": {
            "day_master": f"{day_gan}{GAN_WUXING[day_gan]}（{GAN_YINYANG[day_gan]}）",
            "nature": day_nature,
            "ten_gods": {
                "month": month_shishen,
                "hour": hour_shishen,
            },
            "nature_description": _character_description(day_gan, wx_count, strength),
        },
        "dayun_interpretations": dayun_interpretations,
        "liunian_interpretations": liunian_interps[:6],
    }


def _strength_description(strength, day_gan, wx_count):
    """八字强弱描述"""
    wx = GAN_WUXING[day_gan]
    most = max(wx_count.items(), key=lambda x: x[1])[0]
    lack = [k for k, v in wx_count.items() if v == 0]

    if "身旺" in strength or "偏旺" in strength:
        base = f"日主{day_gan}木旺，精力充沛，有主见有魄力。但也容易固执或冲动。"
    elif "身弱" in strength or "偏弱" in strength:
        base = f"日主{day_gan}木偏弱，心思细腻，敏感内省。但也容易疲劳或缺乏自信。"
    else:
        base = f"日主{day_gan}木中和，性情平衡，能动能静。"

    if lack:
        base += f"缺{lack[0]}，内心可能缺乏安全感或某种支撑。"
    return base


def _gods_description(use, avoid, strength):
    """用神喜忌描述"""
    use_str = "、".join(use) if use else "待定"
    avoid_str = "、".join(avoid) if avoid else "待定"
    return f"用神：{use_str}；忌神：{avoid_str}。"


def _character_description(day_gan, wx_count, strength):
    """性格描述"""
    wx = GAN_WUXING[day_gan]
    most_wx = max(wx_count.items(), key=lambda x: x[1])[0]

    descriptions = {
        "木": "你有主见、有韧性，内心有一股不服输的劲。思维活跃，善于思考，但有时候想太多容易内耗。",
        "火": "你热情开朗，善于表达，行动力强。喜欢有挑战的事情，但有时候容易急躁或三分钟热度。",
        "土": "你稳重踏实，重视承诺，做事有耐心。善于积累和规划，但有时候过于保守。",
        "金": "你果断坚定，有原则有底线，注重公平正义。做事干脆利落，但有时候过于直接。",
        "水": "你聪明智慧，适应力强，善于变通。想法多、创意足，但有时候容易犹豫不决。",
    }

    base = descriptions.get(most_wx, "你性格平衡，五行较为齐全。")
    return base
