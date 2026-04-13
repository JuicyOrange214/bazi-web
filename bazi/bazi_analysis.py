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


# ===================== 详细性格分析 =====================

def detailed_character_analysis(ganzhi_dict, wuxing_count, strength_level, day_gan, ten_gods_map):
    """生成详细的性格分析"""
    from datetime import datetime
    
    day_zhi = ganzhi_dict["day"][1]
    month_gan = ganzhi_dict["month"][0]
    month_zhi = ganzhi_dict["month"][1]
    year_gan = ganzhi_dict["year"][0]
    hour_gan = ganzhi_dict["hour"][0]
    hour_zhi = ganzhi_dict["hour"][1]
    
    wx = GAN_WUXING[day_gan]
    day_yy = GAN_YINYANG[day_gan]
    
    results = {}
    
    # 1. 基础性格概述
    results["overview"] = _get_wuxing_overview(wx, day_yy, wuxing_count)
    
    # 2. 各柱性格影响
    results["pillar_influence"] = {
        "year": _get_year_pillar_effect(year_gan, ganzhi_dict["year"][1]),
        "month": _get_month_pillar_effect(month_gan, month_zhi),
        "day": _get_day_pillar_effect(day_gan, day_zhi),
        "hour": _get_hour_pillar_effect(hour_gan, hour_zhi),
    }
    
    # 3. 十神特质
    results["ten_god_traits"] = _get_ten_god_detailed_traits(ten_gods_map, day_gan)
    
    # 4. 性格优劣势
    results["strengths_weaknesses"] = _get_strengths_weaknesses(wx, ten_gods_map, wuxing_count)
    
    # 5. 人际关系模式
    results["relationships"] = _get_relationship_patterns(ten_gods_map, wx, day_yy)
    
    # 6. 事业发展建议
    results["career"] = _get_career_tendencies(ten_gods_map, wx, month_zhi)
    
    return results


def _get_wuxing_overview(wx, day_yy, wx_count):
    """五行基础性格概述"""
    overviews = {
        "木": {
            "overview": "你是一个内心有力量的人，对自己想要的事物有清晰的追求。你的想法往往比感受走得更快，有时候需要学着放慢脚步，倾听身体的声音。",
            "emotional": "情感细腻但不太外露，有时候会把情绪积压在心里。遇到压力时容易焦虑或纠结，但也有韧性能够坚持。",
            "social": "对人友善但有选择，不喜欢虚伪的社交。朋友不多但交心，容易被理解自己的人吸引。",
        },
        "火": {
            "overview": "你是一个热情直接的人，对生活充满动力和好奇心。你的感染力很强，能够带动周围人的情绪。",
            "emotional": "情绪来得快去得也快，很少真正记仇。感受力很强，但也容易因为小事受伤。",
            "social": "朋友很多，擅长社交，容易在人群中找到自己的位置。但有时候需要学会独处。",
        },
        "土": {
            "overview": "你是一个稳重踏实的人，重视承诺和责任。你有耐心，愿意为长远目标持续努力。",
            "emotional": "情绪稳定，不容易大喜大悲。但有时候会压抑情绪，不善于表达内心的感受。",
            "social": "朋友关系稳定持久，不追求数量而是质量。是一个值得信赖的伙伴。",
        },
        "金": {
            "overview": "你是一个有原则有底线的人，对公平正义看得很重。你的决定通常干脆利落，不拖泥带水。",
            "emotional": "感受力很强但不太外露，有时候显得冷硬。内心其实很敏感，只是不会轻易展示。",
            "social": "朋友不多但都是精品，宁缺毋滥。对人际关系有清晰的标准。",
        },
        "水": {
            "overview": "你是一个聪明善变的人，思维活跃，适应力强。你的直觉很准，能够快速捕捉到环境的变化。",
            "emotional": "情绪起伏较大，容易受环境影响。但也有很强的自我调节能力。",
            "social": "朋友遍天下但真正懂你的少。需要找到能够深度交流的人。",
        },
    }
    base = overviews.get(wx, overviews["土"])
    lack = [k for k, v in wx_count.items() if v == 0]
    if lack:
        base["overview"] += f" 另外，你的八字缺{lack[0]}，可能在某些方面需要多加留意。"
    return base


def _get_year_pillar_effect(year_gan, year_zhi):
    """年柱对性格的影响（祖辈/早年）"""
    wx = GAN_WUXING[year_gan]
    yy = GAN_YINYANG[year_gan]
    effects = {
        "木": "早年得到长辈的关爱，有一定的靠山，但也要学会独立。",
        "火": "早年生活环境较温暖，长辈有爱心，帮助你形成积极的心态。",
        "土": "早年生活稳定，得到家族的支持和信任。",
        "金": "早年可能经历过一些磨练，但让你更加坚强有主见。",
        "水": "早年生活可能有变迁，锻炼了你的适应能力。",
    }
    return effects.get(wx, "早年生活平稳。")


def _get_month_pillar_effect(month_gan, month_zhi):
    """月柱对性格的影响（父母/青年时期）"""
    wx = GAN_WUXING[month_gan]
    effects = {
        "木": "月柱木旺，代表你有进取心，有明确的目标和追求。",
        "火": "月柱火旺，你行动力强，善于把握机会。",
        "土": "月柱土旺，你务实可靠，善于积累和规划。",
        "金": "月柱金旺，你有原则有魄力，做事干脆。",
        "水": "月柱水旺，你聪明灵活，善于变通和思考。",
    }
    return effects.get(wx, "")


def _get_day_pillar_effect(day_gan, day_zhi):
    """日柱对性格的影响（自身）"""
    wx = GAN_WUXING[day_gan]
    yy = GAN_YINYANG[day_gan]
    base = GAN_WUXING[day_gan]
    
    day_effects = {
        "木": "你是乙木日主，外柔内刚，有韧性、有主见，不轻易服输。",
        "火": "你是丙火日主，热情开朗，善于表达，有感染力。",
        "土": "你是戊土日主，稳重踏实，重视承诺，有责任心。",
        "金": "你是庚金日主，果断坚定，有原则有魄力。",
        "水": "你是壬水日主，聪明智慧，适应力强，善于谋略。",
    }
    return day_effects.get(base, "")


def _get_hour_pillar_effect(hour_gan, hour_zhi):
    """时柱对性格的影响（晚年/子女）"""
    wx = GAN_WUXING[hour_gan]
    effects = {
        "木": "晚年心态更加平和，与子女关系和谐。",
        "火": "晚年生活依然丰富，保持学习的心态。",
        "土": "晚年财运稳定，家庭和睦。",
        "金": "晚年依然有活力，子女有成就。",
        "水": "晚年有智慧传承，与年轻一代沟通顺畅。",
    }
    return effects.get(wx, "")


def _get_ten_god_detailed_traits(ten_gods_map, day_gan):
    """十神特质详解"""
    traits = {}
    
    ten_god_natures = {
        "比肩": {
            "positive": "独立自主、有主见、意志坚强、能够坚持自我",
            "negative": "固执己见、缺乏团队精神、不善于求助",
            "relationship": "在感情中需要平等的伙伴关系，不喜欢被控制",
            "career": "适合独立创业或自由职业",
        },
        "劫财": {
            "positive": "豪爽义气、善于交际、敢于冒险、有竞争力",
            "negative": "冲动消费、容易与人发生争执、竞争意识过强",
            "relationship": "在感情中需要保持独立性，同时学会妥协",
            "career": "适合销售、商务、公关等需要人际交往的工作",
        },
        "食神": {
            "positive": "温和善良、表达力强、懂得享受生活、有创造力",
            "negative": "容易满足现状、缺乏上进心、有时过于理想化",
            "relationship": "温柔体贴的伴侣，能够让对方感到舒适",
            "career": "适合教育、艺术、餐饮、设计等需要创意和表达的工作",
        },
        "伤官": {
            "positive": "聪明机敏、创意十足、口才好、思维活跃",
            "negative": "容易骄傲、不服管教、说话直接容易伤人",
            "relationship": "需要能够欣赏你才华的伴侣，不喜欢平淡的生活",
            "career": "适合创意行业、写作、法律、表演等",
        },
        "偏财": {
            "positive": "善于理财、社交能力强、眼光独到、懂得享受",
            "negative": "花钱大方导致财运不稳、有时过于计较利益",
            "relationship": "在感情中浪漫但有时不够专注",
            "career": "适合金融、投资、商务、销售等与金钱打交道的工作",
        },
        "正财": {
            "positive": "务实节约、理财稳健、工作认真、财运稳定",
            "negative": "赚钱欲望不够强烈、过于保守、缺乏冒险精神",
            "relationship": "在感情中忠诚可靠，是稳定的依靠",
            "career": "适合财务、会计、公务员、后勤管理等稳定的工作",
        },
        "偏官": {
            "positive": "果断有魄力、压力下成长快、善于竞争、敢于挑战",
            "negative": "脾气急躁、压力过大、容易得罪人",
            "relationship": "在感情中需要有空间和自由，不喜欢束缚",
            "career": "适合管理、司法、执法、外科医生等高压工作",
        },
        "正官": {
            "positive": "有责任心、守规矩、善于规划、名声观念强",
            "negative": "过于在意他人看法、缺乏灵活性、容易有压力",
            "relationship": "在感情中认真负责，追求稳定长久的关系",
            "career": "适合管理、公务员、教师、HR等需要责任感和规划性的工作",
        },
        "偏印": {
            "positive": "悟性高、领悟力强、有独特见解、善于钻研",
            "negative": "性格孤僻、缺乏热情、不善于表达情感",
            "relationship": "在感情中比较内敛，需要能够读懂你的伴侣",
            "career": "适合学术研究、技术、研发、咨询等需要深度思考的工作",
        },
        "正印": {
            "positive": "仁慈善良、有爱心、善于学习、有包容心",
            "negative": "有时候过于理想化、缺乏主见、容易依赖他人",
            "relationship": "在感情中给予对方无条件的支持和关爱",
            "career": "适合教育、医疗、公益、写作等需要爱心和耐心的行业",
        },
    }
    
    for pillar, god in ten_gods_map.items():
        if god in ten_god_natures:
            traits[pillar] = ten_god_natures[god]
        else:
            traits[pillar] = {"positive": "性格平衡", "negative": "", "relationship": "", "career": ""}
    
    return traits


def _get_strengths_weaknesses(wx, ten_gods_map, wx_count):
    """性格优劣势分析"""
    strengths_map = {
        "木": ["有主见有韧性", "思维活跃善于思考", "目标明确不易动摇"],
        "火": ["热情开朗有感染力", "行动力强效率高", "善于带动氛围"],
        "土": ["稳重踏实负责任", "有耐心能坚持", "重视承诺可靠"],
        "金": ["果断有原则", "决策力强", "有魄力能担当"],
        "水": ["聪明善变适应力强", "直觉准善于把握机会", "想法多创意足"],
    }
    
    weaknesses_map = {
        "木": ["有时候过于固执", "容易犹豫不决", "内耗较多想太多"],
        "火": ["容易急躁三分钟热度", "情绪波动大", "有时候过于直接"],
        "土": ["过于保守谨慎", "不善变通", "容易压抑情绪"],
        "金": ["有时候过于冷硬", "不太善于表达情感", "原则性过强"],
        "水": ["容易犹豫不决", "情绪起伏大", "有时候想法太多难执行"],
    }
    
    return {
        "strengths": strengths_map.get(wx, ["性格平衡"]),
        "weaknesses": weaknesses_map.get(wx, ["有待完善"]),
    }


def _get_relationship_patterns(ten_gods_map, wx, day_yy):
    """人际关系模式"""
    day_god = ten_gods_map.get("day", "")
    
    patterns = {
        "比肩": "你倾向于建立平等互助的关系，不喜欢欠人情。在朋友圈中通常是组织者或核心人物。",
        "劫财": "你社交能力强，人脉广泛，但有时候会与人竞争或发生冲突。需要学会处理人际冲突。",
        "食神": "你人缘好，相处起来让人感到舒适。但有时候过于随和，缺乏主见。",
        "伤官": "你说话直接，有时候会无意间得罪人。但真正了解你的人会欣赏你的坦诚。",
        "偏财": "你善于结交各路朋友，社交手腕灵活。但财运和感情运容易有波动。",
        "正财": "你对待感情认真负责，是可靠的伴侣和朋友。但有时候表达情感不够浪漫。",
        "偏官": "你在人际关系中容易有压力感，需要学会放松和信任他人。",
        "正官": "你遵守规则，重信誉，在社交中受人尊重。但有时候过于在意他人看法。",
        "偏印": "你比较独立，不太依赖他人。人际圈子可能不大，但朋友都很交心。",
        "正印": "你待人温和有爱心，是很好的倾听者。人际关系和谐，很少与人发生冲突。",
    }
    
    base = patterns.get(day_god, "你性格平衡，人际关系较为和谐。")
    return {"pattern": base}


def _get_career_tendencies(ten_gods_map, wx, month_zhi):
    """事业发展倾向"""
    day_god = ten_gods_map.get("day", "")
    month_god = ten_gods_map.get("month", "")
    
    career_map = {
        "比肩": "适合独立创业、自由职业、专业技术类工作。",
        "劫财": "适合销售、商务、公关、业务拓展类工作。",
        "食神": "适合教育、艺术设计、餐饮、创意类工作。",
        "伤官": "适合写作、法律、表演、创意行业、管理类工作。",
        "偏财": "适合金融、投资、贸易、销售类与金钱打交道的工作。",
        "正财": "适合财务、会计、后勤、公务员等稳定的工作。",
        "偏官": "适合管理、司法、执法、军事、外科医生等高压工作。",
        "正官": "适合管理、公务员、教师、HR等需要责任感和规划性的工作。",
        "偏印": "适合学术研究、技术研发、咨询等需要深度思考的工作。",
        "正印": "适合教育、医疗、公益、写作等需要爱心和耐心的行业。",
    }
    
    base = career_map.get(day_god, career_map.get(month_god, "职业倾向需要结合具体八字分析。"))
    
    # 结合月令做补充
    month_career = {
        "寅": "你执行力强，适合需要动手能力的工作。",
        "卯": "你思维活跃，适合需要创意的工作。",
        "巳": "你善于沟通，适合需要表达的工作。",
        "午": "你热情有活力，适合需要影响他人的工作。",
        "申": "你分析能力强，适合需要逻辑思维的工作。",
        "酉": "你注重细节，适合需要精确度的工作。",
        "亥": "你直觉敏锐，适合需要洞察力的工作。",
        "子": "你适应力强，适合需要灵活应变的工作。",
    }
    
    extra = month_career.get(month_zhi, "")
    return {"tendency": base + " " + extra}


# 更新 analyze_bazi 使用新的详细性格分析
def analyze_bazi_full(ganzhi_dict, dayun_list, gender, birth_year):
    """生成完整的八字解读（包含详细性格分析）"""
    from datetime import datetime

    day_gan = ganzhi_dict["day"][0]
    month_zhi = ganzhi_dict["month"][1]
    day_zhi = ganzhi_dict["day"][1]
    hour_gan = ganzhi_dict["hour"][0]
    hour_zhi = ganzhi_dict["hour"][1]

    # 五行统计
    wx_count = get_wuxing_count(ganzhi_dict)

    # 八字强弱
    strength_str, score = determine_strength(day_gan, month_zhi, wx_count)

    # 用神喜忌
    use_gods, avoid_gods = determine_gods_and_harm(day_gan, wx_count, strength_str)

    # 十神map
    ten_gods_map = {
        "year": TEN_GODS.get(day_gan, {}).get(ganzhi_dict["year"][0], "其他"),
        "month": TEN_GODS.get(day_gan, {}).get(ganzhi_dict["month"][0], "其他"),
        "day": TEN_GODS.get(day_gan, {}).get(day_gan, "其他"),
        "hour": TEN_GODS.get(day_gan, {}).get(hour_gan, "其他"),
    }

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

    # 五行缺什么
    lack = [wx for wx, cnt in wx_count.items() if cnt == 0]

    # 综述
    lack_str = f"五行缺{'、'.join(lack)}。" if lack else "五行齐全。"
    
    # 基础综述
    summary_parts = [
        f"日主{day_gan}（{GAN_WUXING[day_gan]}），{strength_str}。{lack_str}",
    ]

    # 详细性格分析
    detailed_char = detailed_character_analysis(ganzhi_dict, wx_count, strength_str, day_gan, ten_gods_map)
    
    # 性格综述
    overview = detailed_char["overview"]
    char_summary = overview.get("overview", "") + " " + overview.get("emotional", "")

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

    return {
        "summary": "".join(summary_parts),
        "summary_full": char_summary,
        "strength": {
            "level": strength_str,
            "score": score,
            "description": _strength_description(strength_str, day_gan, wx_count),
        },
        "wuxing": {
            "counts": wx_count,
            "lacking": lack,
        },
        "gods": {
            "use": use_gods,
            "avoid": avoid_gods,
            "use_description": _gods_description(use_gods, avoid_gods, strength_str),
        },
        "character": {
            "day_master": f"{day_gan}{GAN_WUXING[day_gan]}（{GAN_YINYANG[day_gan]}）",
            "ten_gods": {
                "year": ten_gods_map["year"],
                "month": ten_gods_map["month"],
                "day": ten_gods_map["day"],
                "hour": ten_gods_map["hour"],
            },
            "nature_description": overview.get("overview", ""),
            "emotional": overview.get("emotional", ""),
            "social": overview.get("social", ""),
            "ten_god_traits": detailed_char.get("ten_god_traits", {}),
            "strengths_weaknesses": detailed_char.get("strengths_weaknesses", {}),
            "relationships": detailed_char.get("relationships", {}),
            "career": detailed_char.get("career", {}),
            "pillar_influence": detailed_char.get("pillar_influence", {}),
        },
        "dayun_interpretations": dayun_interpretations,
        "liunian_interpretations": liunian_interps[:6],
    }
