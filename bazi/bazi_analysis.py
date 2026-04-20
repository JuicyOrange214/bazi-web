# -*- coding: utf-8 -*-
"""
八字文字解读分析模块 v2 - 详细版
为用户提供通俗易懂、深入详尽的命理解读
"""

from datetime import datetime

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

# 天干阴阳
GAN_YINYANG = {
    "甲": "阳", "乙": "阴",
    "丙": "阳", "丁": "阴",
    "戊": "阳", "己": "阴",
    "庚": "阳", "辛": "阴",
    "壬": "阳", "癸": "阴"
}

# 月令地支旺度
MONTH_ZHI_STRENGTH = {
    "寅": 100, "卯": 100,
    "巳": 80,  "午": 80,
    "申": 70,  "酉": 70,
    "亥": 70,  "子": 70,
    "辰": 60,  "戌": 60, "丑": 60, "未": 60,
}

# 日干对应的十神
TEN_GODS = {
    "甲": {"甲": "比肩", "乙": "劫财", "丙": "食神", "丁": "伤官", "戊": "偏财", "己": "正财", "庚": "偏官", "辛": "正官", "壬": "偏印", "癸": "正印"},
    "乙": {"甲": "劫财", "乙": "比肩", "丙": "伤官", "丁": "食神", "戊": "正财", "己": "偏财", "庚": "正官", "辛": "偏官", "壬": "正印", "癸": "偏印"},
    "丙": {"甲": "偏印", "乙": "正印", "丙": "比肩", "丁": "劫财", "戊": "食神", "己": "伤官", "庚": "偏财", "辛": "正财", "壬": "偏官", "癸": "正官"},
    "丁": {"甲": "正印", "乙": "偏印", "丙": "劫财", "丁": "比肩", "戊": "伤官", "己": "食神", "庚": "正财", "辛": "偏财", "壬": "正官", "癸": "偏官"},
    "戊": {"甲": "偏财", "乙": "正财", "丙": "偏印", "丁": "正印", "戊": "比肩", "己": "劫财", "庚": "食神", "辛": "伤官", "壬": "偏官", "癸": "正官"},
    "己": {"甲": "正财", "乙": "偏财", "丙": "正印", "丁": "偏印", "戊": "劫财", "己": "比肩", "庚": "伤官", "辛": "食神", "壬": "正官", "癸": "偏官"},
    "庚": {"甲": "偏官", "乙": "正官", "丙": "偏财", "丁": "正财", "戊": "偏印", "己": "正印", "庚": "比肩", "辛": "劫财", "壬": "食神", "癸": "伤官"},
    "辛": {"甲": "正官", "乙": "偏官", "丙": "正财", "丁": "偏财", "戊": "正印", "己": "偏印", "庚": "劫财", "辛": "比肩", "壬": "伤官", "癸": "食神"},
    "壬": {"甲": "食神", "乙": "伤官", "丙": "偏财", "丁": "正财", "戊": "偏官", "己": "正官", "庚": "偏印", "辛": "正印", "壬": "比肩", "癸": "劫财"},
    "癸": {"甲": "伤官", "乙": "食神", "丙": "正财", "丁": "偏财", "戊": "正官", "己": "偏官", "庚": "正印", "辛": "偏印", "壬": "劫财", "癸": "比肩"},
}

# 详细十神解读
TEN_GOD_DETAILED = {
    "比肩": {
        "name": "比肩",
        "definition": "与日主天干相同五行之字，象征同等实力、并肩同行的关系。在命局中代表自身的能力、意志和独立性。",
        "positive": [
            "你性格独立自主，不依赖他人，有明确的目标和方向感。",
            "你意志坚定，遇到困难能够坚持到底，不轻易放弃。",
            "你做事有主见，不随波逐流，能够坚持自己的判断。",
            "你重视公平和朋友间的对等关系，不喜欢占便宜也不愿意被占便宜。",
            "你能够在压力下保持冷静，有较强的抗压能力。",
        ],
        "negative": [
            "有时候会固执己见，听不进别人的建议，容易错过好机会。",
            "你不太善于向人求助，习惯独自承担一切，可能让自己压力过大。",
            "在团队合作中，你可能会因为过于强调个人能力而影响团队氛围。",
            "你有时会过于坚持自己的方式，缺乏变通和灵活性。",
        ],
        "relationship": "感情中你需要平等的伙伴关系，不喜欢被控制或被过度依赖。你倾向于选择能够互相尊重、彼此支持的对象。在亲密关系中，保持一定的独立性会让你们相处更和谐。",
        "career": "你适合独立创业、做自由职业者，或者担任需要独当一面的岗位。你适合技术性、专业性较强的工作，靠实力说话。",
        "wealth": "你财运相对稳定，不靠投机，更适合靠实力和专业积累财富。你对金钱有一定规划，不乱花钱。",
        "health": "比肩旺者需注意筋骨、肝胆方面的健康，运动损伤、关节问题需要留意。",
    },
    "劫财": {
        "name": "劫财",
        "definition": "与日主天干阴阳不同但五行相同之字，象征竞争、争夺、辅助。在命局中代表争夺力、行动力和人际竞争。",
        "positive": [
            "你充满活力和竞争力，面对挑战时总能爆发出惊人的战斗力。",
            "你为人豪爽、仗义，朋友有难时你会毫不犹豫地伸出援手。",
            "你有不服输的精神，越是困难越能激发出你的潜能。",
            "你善于在竞争中找到机会，化压力为动力。",
            "你交际能力强，人脉广泛，能够快速融入各种社交场合。",
        ],
        "negative": [
            "你有时冲动行事，做决定太快而考虑不周全。",
            "你花钱大方，有时候会因为朋友义气而超支。",
            "你容易与人发生争执或冲突，说话直接可能无意中伤害他人。",
        ],
        "relationship": "感情中你热情主动，但有时占有欲较强，需要注意给彼此空间。你的感情容易经历竞争或波折，需要学会处理感情中的冲突。",
        "career": "你适合销售、商务、公关、业务拓展等需要主动出击的工作。你适合竞争激烈的行业，能够在压力下发挥超常。",
        "wealth": "你财运波动较大，赚钱能力强但散去也快。你有时会为朋友花钱或者进行人情消费，需要注意理财。",
        "health": "劫财旺者注意肝胆、筋骨健康，运动损伤需小心。注意肾气保养，不要过度消耗精力。",
    },
    "食神": {
        "name": "食神",
        "definition": "日主所生之阴阳不同之字，象征创造、表达、享受。在命局中代表才华、表达力、口福和创造力。",
        "positive": [
            "你性格温和善良，待人接物让人感觉舒适和愉快。",
            "你有很强的表达能力和文字功底，善于用言语或文字传递想法。",
            "你懂得享受生活，有生活情趣，不让自己活得太过枯燥。",
            "你创意十足，思维活跃，经常能想到别人想不到的点子。",
            "你对美食、艺术有独特的鉴赏力，生活品味较高。",
        ],
        "negative": [
            "你有时过于追求享受，缺乏上进心和事业心。",
            "你容易满足现状，对未来缺乏长远规划。",
            "你有时过于理想化，对现实的困难估计不足。",
        ],
        "relationship": "感情中你温柔体贴，是让伴侣感到被爱、被呵护的类型。你需要一个能够欣赏你才华、理解你内心的伴侣。你不太擅长处理感情中的矛盾冲突，容易选择逃避。",
        "career": "你适合教育、艺术设计、餐饮、创意、文学等需要表达和创意的工作。你适合需要与人互动但不需要激烈竞争的服务性行业。",
        "wealth": "你财运相对平稳，靠正业和稳定收入为主。你懂得享受，会花钱在提升生活品质上。",
        "health": "食神旺者注意脾胃消化系统的健康。注意饮食规律，不要暴饮暴食。",
    },
    "伤官": {
        "name": "伤官",
        "definition": "日主所生但阴阳相同之字，象征才华、叛逆、口才和变革。在命局中代表创新能力、表达力和突破精神。",
        "positive": [
            "你聪明绝顶，领悟力强，经常能够看透事物的本质。",
            "你有极强的创造力和创新能力，不走寻常路。",
            "你口才好，善于雄辩，表达能力强，能把复杂的事说简单。",
            "你不甘于平庸，有强烈的成就动机和上进心。",
        ],
        "negative": [
            "你有时过于骄傲，过于自信而忽略了他人的感受和建议。",
            "你说话直接犀利，容易无意中得罪人而不自知。",
            "你不喜欢被管束，容易与上级或权威发生冲突。",
        ],
        "relationship": "感情中你需要一个能够欣赏你才华的伴侣，平凡的生活可能让你感到无聊。你说话直接容易伤害伴侣，需要学会更柔和地表达。",
        "career": "你适合写作、法律、表演、创意设计、音乐等需要个人才华的工作。你适合自由职业或者能够充分发挥创造力的环境。",
        "wealth": "你财运波动大，可能有横财机会但也有破财风险。你赚钱方式与众不同，可能靠才华而非传统方式获得收入。",
        "health": "伤官旺者注意神经系统、心理健康。伤官泄身太过时，注意休息和精力管理。",
    },
    "偏财": {
        "name": "偏财",
        "definition": "日主所克且阴阳不同之字，象征流动之财、人际往来。在命局中代表理财能力、社交手腕和灵活收入。",
        "positive": [
            "你善于社交，人脉广泛，能够快速建立各种关系网络。",
            "你眼光独到，对商机和投资机会有敏锐的嗅觉。",
            "你花钱大方但不乱来，对金钱有灵活的运用能力。",
            "你善于把握人情世故，在社交场合如鱼得水。",
        ],
        "negative": [
            "你有时过于慷慨，花钱没有节制，容易出现财务紧张。",
            "你做事不够稳定，三分钟热度，缺乏长性。",
            "你可能过于注重利益而忽略了情感上的真诚。",
        ],
        "relationship": "感情中你浪漫而充满惊喜，懂得如何让伴侣开心。你有时过于注重外表和物质条件，可能忽略感情的本质。你的社交能力强，需要伴侣有足够的信任和安全感。",
        "career": "你适合金融、投资、贸易、销售、商务等与金钱打交道的工作。你适合需要广泛社交和人脉的管理岗位。",
        "wealth": "你财运较好，有机会获得意外之财。你理财方式灵活，但需要建立更稳健的财务规划。",
        "health": "偏财旺者注意肝胆、视力方面的健康。注意劳逸结合，不要因为社交而过度消耗精力。",
    },
    "正财": {
        "name": "正财",
        "definition": "日主所克但阴阳相同之字，象征稳定收入、固定资产。在命局中代表勤劳、节约、稳定和正当收入。",
        "positive": [
            "你务实能干，对工作认真负责，是老板眼中的可靠员工。",
            "你理财观念好，知道量入为出，不会乱花钱。",
            "你财运稳定，靠踏实工作积累财富，而非投机取巧。",
            "你重视承诺，说到做到，在人际交往中信誉很好。",
            "你做事有耐心，能够持续努力，不急功近利。",
        ],
        "negative": [
            "你赚钱欲望不够强烈，有时会错过一些发展机会。",
            "你做事比较保守，缺乏冒险精神，不容易突破现状。",
            "你对金钱有时过于计较，影响人际关系的和谐。",
        ],
        "relationship": "感情中你是忠诚可靠的伴侣，愿意为家庭付出稳定的时间和精力。你对伴侣负责，注重实际付出而非浪漫表达。你的感情相对稳定，不会有太大的波澜。",
        "career": "你适合财务、会计、后勤、公务员、管理等稳定的工作。你适合需要细心、耐心和责任心的岗位。你更适合在大企业或机构中稳步发展。",
        "wealth": "你财运稳定但增长缓慢，靠积累而非爆发。你理财稳健，适合定期存款、基金等长期投资。",
        "health": "正财旺者注意脾胃消化系统的健康。注意劳逸结合，久坐不动容易引发健康问题。",
    },
    "偏官": {
        "name": "偏官",
        "definition": "克日主且阴阳不同之字，象征压力、竞争、权威、魄力。在命局中代表行动力、竞争和危机处理能力。",
        "positive": [
            "你做事果断有魄力，面对问题能够快速做出决策。",
            "你有不服输的精神，在竞争中能够脱颖而出。",
            "你有危机处理能力，能够在压力下保持清醒的头脑。",
            "你有管理和领导才能，能够带领团队完成目标。",
        ],
        "negative": [
            "你有时脾气急躁，容易在情绪激动时做出后悔的决定。",
            "你过于强调结果，可能忽略过程中的公平和人情。",
            "你压力过大时容易焦虑和暴躁，需要学会放松。",
        ],
        "relationship": "感情中你占有欲较强，需要学会给伴侣更多的空间。你的感情中可能经历过一些竞争或第三者的情况。你需要一个内心强大的伴侣，能够承受你的强势。",
        "career": "你适合管理、司法、执法、军事、外科医生等需要决断力的工作。你适合高压环境，在压力下反而能发挥得更好。",
        "wealth": "你财运较好，有通过权力或职位获得财富的运。你的财运与事业成就高度相关。",
        "health": "偏官旺者注意肝脏、神经系统、血压方面的健康。偏官代表压力，要注意心理健康的维护。",
    },
    "正官": {
        "name": "正官",
        "definition": "克日主且阴阳相同之字，象征规矩、责任、名誉。在命局中代表社会地位、管理能力和名声。",
        "positive": [
            "你遵纪守法，有正确的价值观和道德观，是社会中的正面力量。",
            "你有责任心，一旦答应的事就一定会做到。",
            "你善于规划和管理，有条理地安排工作和生活。",
            "你注重名声和形象，希望在社会中获得认可和尊重。",
        ],
        "negative": [
            "你有时过于在意他人的看法，给自己造成不必要的压力。",
            "你做事比较死板，缺乏灵活性，难以应对突变情况。",
            "你可能因为追求稳定而错失一些发展机会。",
        ],
        "relationship": "感情中你是认真负责的伴侣，对感情关系看得很重。你追求稳定长久的关系，不喜欢感情中有太多波折。你不太擅长处理情感中的浪漫和惊喜，但会用实际行动表达爱意。",
        "career": "你适合管理、公务员、教师、人力资源等需要责任感和规划性的工作。你适合在正规机构和大型企业中发展。",
        "wealth": "你财运稳定，与事业地位同步增长。你更适合通过晋升、加薪等稳定方式增加收入。",
        "health": "正官旺者注意肝脏、筋骨、血液循环方面的健康。注意工作压力过大带来的亚健康问题。",
    },
    "偏印": {
        "name": "偏印",
        "definition": "生日主但阴阳不同之字，象征领悟、钻研、孤僻。在命局中代表学习能力、领悟力和独特思维。",
        "positive": [
            "你悟性极高，能够快速理解和掌握新知识、新技能。",
            "你思维独特，看问题角度与大多数人不同，经常有独到见解。",
            "你有钻研精神，能够在某个领域深入下去成为专家。",
            "你直觉敏锐，往往能够凭感觉预判事情的发展。",
        ],
        "negative": [
            "你性格较为孤僻，社交圈子窄，朋友不多。",
            "你不太善于表达情感，内心世界难以被人理解。",
            "你有时会过于追求完美而难以行动。",
        ],
        "relationship": "感情中你较为被动，不擅长主动追求。你需要一个能够理解你内心世界的伴侣。你的感情往往是通过学习、工作等场合日久生情。",
        "career": "你适合学术研究、技术研发、咨询、策划等需要深度思考的工作。你适合在专业领域深入钻研，成为细分领域的专家。",
        "wealth": "你财运平稳，财来较慢但稳定。你更适合通过专业技能而非人脉获得收入。",
        "health": "偏印旺者注意消化系统、营养吸收方面的健康。注意心理健康，不要过度封闭自己。",
    },
    "正印": {
        "name": "正印",
        "definition": "生日主且阴阳相同之字，象征教育、慈悲、文凭。在命局中代表学习能力、贵人运和长辈缘分。",
        "positive": [
            "你心地善良，有同情心，愿意帮助有困难的人。",
            "你学习能力强，善于吸收知识和技能。",
            "你有贵人运，在关键时刻总能得到他人的帮助。",
            "你包容心强，能够接纳不同的人和观点。",
            "你有教化能力，适合从事教育、培训类工作。",
        ],
        "negative": [
            "你有时过于理想化，对现实中的困难估计不足。",
            "你有时过于依赖他人，缺乏独立思考和行动的能力。",
            "你不太会拒绝人，有时会因此承担不必要的压力。",
        ],
        "relationship": "感情中你是无私付出的伴侣，愿意为对方牺牲和让步。你能够得到伴侣的尊重和爱戴。你的原生家庭往往对你影响较大。",
        "career": "你适合教育、医疗、公益、写作出版、宗教等需要爱心和耐心的行业。你有贵人运，适合在大平台发展。",
        "wealth": "你财运平稳，不以财为目的而财自然来。你适合通过技能、口碑获得长期稳定的收入。",
        "health": "正印旺者注意消化系统、皮肤方面的健康。正印代表消化吸收好的人，但过旺则反。",
    },
}

# 五行详细解读
WUXING_DETAILED = {
    "木": {
        "nickname": "仁慈正义的生命力",
        "base": "木代表生长、条达、仁慈。你是一个内心有力量的人，对自己想要的事物有着清晰的追求。你的想法往往比感受走得更快，你善于思考、有韧性，能够坚持自己的方向。但木也象征着敏感和易伤，你有时候会想太多，容易内耗，需要学着放慢脚步，倾听身体的声音。",
        "emotional": "你的情感细腻而深沉，不轻易外露。你善于在内心消化情绪，这既是优点也是需要注意的地方。遇到压力时，你容易陷入思考的死循环，但你的韧性也让你最终能够走出来。你的感受力很强，能够捕捉到别人忽略的细节，但这也让你更容易受到负面影响。",
        "social": "你对人友善但有选择性，不喜欢虚伪的社交。朋友不在于多，而在于能够交心。你容易吸引那些欣赏你独立、有主见的人，但也要注意不要因为过于坚持己见而疏远了可能帮助你成长的人。",
        "strengths": ["有主见有韧性", "思维活跃善于思考", "目标明确不易动摇", "善于独立解决问题", "有仁爱之心"],
        "weaknesses": ["有时过于固执", "容易犹豫不决", "内耗较多想太多", "不善于表达情感", "容易自我封闭"],
        "career": ["教育学术", "文化出版", "艺术设计", "行政管理", "策划咨询"],
        "health": ["肝胆", "筋骨", "神经系统"],
    },
    "火": {
        "nickname": "热情洋溢的光明",
        "base": "火代表热情、活力、光明。你是一个充满热情的人，对生活充满动力和好奇心。你的感染力很强，能够带动周围人的情绪，让氛围变得积极向上。但火也象征着急躁和不稳定，你需要学会在热情和冷静之间找到平衡，避免三分钟热度。",
        "emotional": "你的情绪来得快去得也快，很少真正记仇。你的感受力很强，能够快速感知周围人的情绪变化，这让你在人际交往中很受欢迎。但你也容易因为小事受伤，需要学会不要太在意别人的评价。",
        "social": "你朋友很多，擅长社交，能够在各种人群中找到自己的位置。你喜欢成为关注的中心，但也要注意不要因为追求表面的热闹而忽略了真正重要的关系。",
        "strengths": ["热情开朗有感染力", "行动力强效率高", "善于带动氛围", "表达能力强", "适应力强"],
        "weaknesses": ["容易急躁三分钟热度", "情绪波动大", "有时过于直接", "缺乏耐心", "不易坚持"],
        "career": ["销售公关", "表演艺术", "餐饮旅游", "教育培训", "媒体传播"],
        "health": ["心脏", "血液", "眼睛"],
    },
    "土": {
        "nickname": "稳重厚德的承载",
        "base": "土代表稳重、承载、诚信。你是一个稳重踏实的人，重视承诺和责任。你有耐心，愿意为长远目标持续努力，不急功近利。土也象征着包容和大地般的胸怀，你能够接纳不同的意见和人群。但土也容易过于保守，需要学会在稳定和创新之间找到平衡。",
        "emotional": "你的情绪稳定，不容易大喜大悲，这种稳定感让你成为朋友可以依靠的港湾。但你有时会压抑情绪，不善于表达内心的感受，这可能让身边的人觉得难以走近你。",
        "social": "你的朋友关系稳定持久，不追求数量而是质量。你是那种值得信赖的伙伴，一旦认定了朋友就会真心对待。",
        "strengths": ["稳重踏实负责任", "有耐心能坚持", "重视承诺可靠", "包容心强", "理财稳健"],
        "weaknesses": ["过于保守谨慎", "不善变通", "压抑情绪", "不善于表达", "缺乏冒险精神"],
        "career": ["财务会计", "建筑工程", "农业", "公务员", "后勤管理"],
        "health": ["脾胃", "消化系统", "皮肤"],
    },
    "金": {
        "nickname": "刚毅正义的利剑",
        "base": "金代表刚毅、决断、正义。你是一个有原则有底线的人，对公平正义看得很重。你的决定通常干脆利落，不拖泥带水，这种魄力让你在管理和领导方面有天然的优势。但金也象征着冷硬，你有时候会显得不够柔和，需要学会在原则和人情之间找到平衡。",
        "emotional": "你的感受力很强但不太外露，你内心其实很敏感，只是不会轻易展示给他人。这种特质让你显得有距离感，但一旦有人走进你的内心，你会是非常忠诚的朋友或伴侣。",
        "social": "你的朋友不多但都是精品，你对人际关系有清晰的标准，宁缺毋滥。你欣赏有能力、有原则的人，也希望自己在别人眼中是可靠和有能力的形象。",
        "strengths": ["果断有原则", "决策力强", "有魄力能担当", "意志坚强", "注重公平"],
        "weaknesses": ["有时过于冷硬", "不太善于表达情感", "原则性过强", "容易挑剔", "不易妥协"],
        "career": ["法律司法", "企业管理", "金融财务", "医生", "警察"],
        "health": ["肺脏", "呼吸系统", "骨骼"],
    },
    "水": {
        "nickname": "聪明智慧的流动",
        "base": "水代表智慧、流动、适应。你是一个聪明善变的人，思维活跃，适应力强。你的直觉很准，能够快速捕捉到环境的变化和潜在的机会。水也象征着深邃和变化，你有时候想法太多而难以下定决心，需要学会在思考和行动之间找到平衡。",
        "emotional": "你的情绪起伏较大，容易受环境影响，但你有很强的自我调节能力。你内心世界丰富，想法多，有时候会因为想太多而焦虑。你的感受力很敏锐，能够感知到别人忽略的细节。",
        "social": "你朋友遍天下但真正懂你的少，你需要找到能够深度交流的人。你不太喜欢表面的寒暄，更向往有深度的心灵沟通，一旦找到志同道合的人就会非常珍惜这段关系。",
        "strengths": ["聪明善变适应力强", "直觉准善于把握机会", "想法多创意足", "善于谋略", "包容万象"],
        "weaknesses": ["容易犹豫不决", "情绪起伏大", "想法太多难执行", "有时过于算计", "缺乏恒心"],
        "career": ["贸易商业", "投资金融", "运输物流", "教育培训", "顾问咨询"],
        "health": ["肾脏", "泌尿系统", "耳朵"],
    },
}


def get_wuxing_of_char(c):
    return GAN_WUXING.get(c) or ZHI_WUXING.get(c)


def get_wuxing_count(ganzhi_dict):
    all_chars = (ganzhi_dict["year"] + ganzhi_dict["month"] +
                 ganzhi_dict["day"] + ganzhi_dict["hour"])
    counts = {"木": 0, "火": 0, "土": 0, "金": 0, "水": 0}
    for c in all_chars:
        w = get_wuxing_of_char(c)
        if w:
            counts[w] += 1
    return counts


def determine_strength(day_gan, month_zhi, wuxing_count):
    day_gan_wx = GAN_WUXING[day_gan]
    month_strength = MONTH_ZHI_STRENGTH.get(month_zhi, 50)
    peer_score = 0
    other_score = 0

    for wx, count in wuxing_count.items():
        if wx == day_gan_wx:
            peer_score += count * 18
        elif wx in ["水", day_gan_wx]:
            other_score += count * 6
        else:
            other_score += count * 8

    strength_score = month_strength + peer_score - other_score

    if strength_score > 110:
        return "身旺", strength_score
    elif strength_score > 75:
        return "偏旺", strength_score
    elif strength_score > 45:
        return "中和", strength_score
    elif strength_score > 15:
        return "偏弱", strength_score
    else:
        return "身弱", strength_score


def determine_gods_and_harm(day_gan, wuxing_count, strength):
    day_gan_wx = GAN_WUXING[day_gan]

    if "身旺" in strength or "偏旺" in strength:
        # 身旺：日主太强，需要克泄。忌帮身的水木，喜克身的金，泄秀的火土次之
        avoid = ["木", "水"]
        use = ["金", "火", "土"]
    elif "身弱" in strength or "偏弱" in strength:
        # 身弱：日主太弱，需要生扶。喜水木生身，忌火土泄耗
        use = ["水", "木"]
        avoid = ["火", "土", "金"]
    else:
        # 平或从格：综合判断
        use = ["金", "水"]
        avoid = ["木", "火"]

    return use[:3], avoid[:3]


def get_dayun_interpretation(dayun_gan, dayun_zhi, is_current, day_gan, use_gods, avoid_gods, age_range):
    wx = ZHI_WUXING.get(dayun_zhi, "土")
    gan_wx = GAN_WUXING.get(dayun_gan, "土")

    helps = wx in use_gods or gan_wx in use_gods
    hurts = wx in avoid_gods or gan_wx in avoid_gods

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
    else:
        tag = f"{age_range}"

    if helps:
        mood = "用神到位，整体运势较好，机遇多多。"
    elif hurts:
        mood = "忌神当令，需谨慎应对，避免冒险和重大决策。"
    else:
        mood = "平稳过渡，无大起大落，稳扎稳打为宜。"

    return {
        "period": tag,
        "ganzhi": f"{dayun_gan}{dayun_zhi}",
        "description": f"这步大运以{dayun_gan}{dayun_zhi}为主调，{base}。{mood}"
    }


def analyze_bazi_full(ganzhi_dict, dayun_list, gender, birth_year):
    """生成完整的八字解读"""
    day_gan = ganzhi_dict["day"][0]
    month_zhi = ganzhi_dict["month"][1]
    month_gan = ganzhi_dict["month"][0]
    year_gan = ganzhi_dict["year"][0]
    hour_gan = ganzhi_dict["hour"][0]

    wx_count = get_wuxing_count(ganzhi_dict)
    strength_str, score = determine_strength(day_gan, month_zhi, wx_count)
    use_gods, avoid_gods = determine_gods_and_harm(day_gan, wx_count, strength_str)

    # 十神map
    ten_gods_map = {
        "year": TEN_GODS.get(day_gan, {}).get(year_gan, "其他"),
        "month": TEN_GODS.get(day_gan, {}).get(month_gan, "其他"),
        "day": TEN_GODS.get(day_gan, {}).get(day_gan, "其他"),
        "hour": TEN_GODS.get(day_gan, {}).get(hour_gan, "其他"),
    }

    current_year = datetime.now().year

    current_dayun = None
    for du in dayun_list:
        if du.get("gan_zhi") == "小运":
            continue
        yr_range = du.get("year_range", "")
        if str(current_year) in yr_range:
            current_dayun = du
            break

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

    lack = [wx for wx, cnt in wx_count.items() if cnt == 0]
    lack_str = f"五行缺{'、'.join(lack)}。" if lack else "五行齐全，阴阳平衡。"

    day_gan_wx = GAN_WUXING[day_gan]
    wx_detail = WUXING_DETAILED.get(day_gan_wx, WUXING_DETAILED["土"])

    # 构建综述
    strength_desc = "身旺" in strength_str or "偏旺" in strength_str
    if strength_desc:
        base_summary = f"日主{day_gan}（{day_gan_wx}），{strength_str}，精力充沛、有魄力有主见。{lack_str}"
    else:
        base_summary = f"日主{day_gan}（{day_gan_wx}），{strength_str}，心思细腻、敏感内省。{lack_str}"

    # 性格详解
    char_base = wx_detail["base"]
    char_emotional = wx_detail["emotional"]
    char_social = wx_detail["social"]

    # 十神详解
    ten_god_details = {}
    for pillar, god in ten_gods_map.items():
        if god != "其他" and god in TEN_GOD_DETAILED:
            ten_god_details[pillar] = TEN_GOD_DETAILED[god]
        else:
            ten_god_details[pillar] = None

    # 流年解读
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
                    ln_mood = "用神流年，运势较好，把握机会。"
                elif ln_wx in avoid_gods or ln_zhi_wx in avoid_gods:
                    ln_mood = "忌神流年，谨慎行事，避免冒险。"
                else:
                    ln_mood = "平稳过渡，稳扎稳打。"

                liunian_interps.append({
                    "year": str(yr),
                    "ganzhi": ln["gan_zhi"],
                    "age": f"{ln.get('age_xu', 0)}岁",
                    "description": f"{ln['gan_zhi'][0]}{ln['gan_zhi'][1]}年，{ln_mood}"
                })

    # 五行各柱解读
    pillar_meanings = {
        "year": {
            "name": "年柱（祖辈/早年）",
            "detail": f"年柱{ganzhi_dict['year']}，代表祖辈和早年生活。"
        }
    }

    return {
        "summary": base_summary,
        "summary_full": char_base + " " + char_emotional + " " + char_social,
        "strength": {
            "level": strength_str,
            "score": score,
            "description": base_summary,
        },
        "wuxing": {
            "counts": wx_count,
            "lacking": lack,
            "detail": wx_detail,
        },
        "gods": {
            "use": use_gods,
            "avoid": avoid_gods,
            "use_description": f"用神：{', '.join(use_gods)}；忌神：{', '.join(avoid_gods)}。用神代表你需要的五行能量，忌神代表你需要规避的五行能量。",
        },
        "character": {
            "day_master": f"{day_gan}{day_gan_wx}（{GAN_YINYANG[day_gan]}）",
            "ten_gods": ten_gods_map,
            "ten_god_details": ten_god_details,
            "nature_description": char_base,
            "emotional": char_emotional,
            "social": char_social,
            "ten_god_traits": {k: v for k, v in ten_gods_map.items() if v != "其他"},
            "strengths_weaknesses": {
                "strengths": wx_detail["strengths"],
                "weaknesses": wx_detail["weaknesses"],
            },
            "relationships": {"pattern": char_social},
            "career": {"tendency": wx_detail["career"]},
        },
        "dayun_interpretations": dayun_interpretations,
        "liunian_interpretations": liunian_interps[:6],
    }
