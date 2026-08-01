#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-02."""

import json
import os

BRIEFING_DATE = "2026-08-02"
BRIEFING_EDITION = "早报"
TOTAL = 26

ITEMS = [
    # 国内 China Mainland (4)
    {
        "cat": ("国内 China Mainland", "国内 China Mainland"),
        "zh_title": "中国60岁及以上人口达3.23亿，老龄化压力持续上升",
        "en_title": "China's elderly population tops 323 million as aging pressures mount",
        "published": "00:23 2026年8月1日",
        "zh_summary": "民政部数据显示，2025年底中国60岁及以上人口达3.23亿，占总人口23%，较2015年增加逾1亿。",
        "en_summary": "Ministry data show 323.38 million people aged 60+ by end-2025, 23% of population, up over 100 million since 2015.",
        "source_zh": "财新 Caixin Global", "source_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-01/chinas-elderly-population-tops-323-million-as-aging-pressures-mount-102470288.html",
    },
    {
        "cat": ("国内 China Mainland", "国内 China Mainland"),
        "zh_title": "国家电网原董事长辛保安接受中央纪委国家监委调查",
        "en_title": "Former State Grid chairman Xin Baoan placed under anti-graft probe",
        "published": "02:38 2026年8月1日",
        "zh_summary": "中央纪委国家监委通报，曾任国家电网董事长、党组书记的辛保安涉嫌严重违纪违法，正接受调查。",
        "en_summary": "China's top anti-graft body said Xin Baoan, former State Grid chairman, is under investigation for suspected serious violations.",
        "source_zh": "财新 Caixin Global", "source_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-01/former-state-grid-chairman-comes-under-anti-graft-investigation-102470296.html",
    },
    {
        "cat": ("国内 China Mainland", "国内 China Mainland"),
        "zh_title": "中国第三批援刚果（金）埃博拉抗疫医疗专家组抵达金沙萨",
        "en_title": "China's third Ebola medical expert team arrives in Kinshasa",
        "published": "08:00 2026年8月2日",
        "zh_summary": "专家组8月1日抵达刚果（金）首都，将协助疫情监测、患者救治和实验室检测，延续前两批团队工作。",
        "en_summary": "The team arrived Saturday to support surveillance, treatment and lab testing, building on two prior Chinese missions.",
        "source_zh": "新华社 Xinhua", "source_en": "Xinhua",
        "url": "http://www.china.org.cn/world/Off_the_Wire/2026-08/02/content_118629484.shtml",
    },
    {
        "cat": ("国内 China Mainland", "国内 China Mainland"),
        "zh_title": "华龙一号2.0版示范项目获国务院核准，四省八台机组开工",
        "en_title": "Hualong One 2.0 demo projects approved in eight-reactor nuclear push",
        "published": "02:05 2026年8月1日",
        "zh_summary": "国务院核准浙江金七门、广东太平岭等4个核电项目共8台机组，其中两台华龙一号2.0为示范工程。",
        "en_summary": "State Council approved eight reactors across four coastal projects, including Hualong One 2.0 demonstration units.",
        "source_zh": "光明日报 Guangming Daily", "source_en": "Guangming Daily",
        "url": "https://news.neamco.com/2026-08/01/content_38921618.htm",
    },
    # 科技 Technology (4)
    {
        "cat": ("科技 Technology", "科技 Technology"),
        "zh_title": "DeepSeek正式发布V4-Flash模型，强化智能体能力并降低API成本",
        "en_title": "DeepSeek releases official V4-Flash model with lower API costs",
        "published": "01:37 2026年8月1日",
        "zh_summary": "官方版V4-Flash于7月31日上线，架构与4月预览版相同，性能提升主要来自后训练优化。",
        "en_summary": "The official V4-Flash launched July 31 with stronger agent capabilities; gains came from post-training, not architecture changes.",
        "source_zh": "财新 Caixin Global", "source_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html",
    },
    {
        "cat": ("科技 Technology", "科技 Technology"),
        "zh_title": "美国议员调查DoorDash使用月之暗面Kimi K2.6模型的安全问题",
        "en_title": "US lawmakers probe DoorDash use of Moonshot AI's Kimi K2.6 model",
        "published": "06:53 2026年8月1日",
        "zh_summary": "众议院相关委员会主席致函DoorDash，要求8月14日前说明所用中国模型及安全测试，并安排8月21日简报。",
        "en_summary": "House committee chairs asked DoorDash for details on Chinese models used and security tests by Aug. 14.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/china/diplomacy/article/3362616/us-lawmakers-investigate-doordashs-use-moonshot-ais-kimi-k26-model",
    },
    {
        "cat": ("科技 Technology", "科技 Technology"),
        "zh_title": "中国计划将量子技术推广至全国电网以提升供电可靠性",
        "en_title": "China to roll out quantum tech on power grid after Hefei trial",
        "published": "15:00 2026年8月1日",
        "zh_summary": "安徽合肥变电站18个月试点显示，量子传感可快速诊断电力设备缺陷，官方称技术已成保供硬支撑。",
        "en_summary": "After an 18-month Hefei trial, quantum sensors will expand nationwide to detect faults and prevent blackouts.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/china/science/article/3362629/china-hopes-banish-blackouts-quantum-tech-puts-power-grid-superposition",
    },
    {
        "cat": ("科技 Technology", "科技 Technology"),
        "zh_title": "科学家警告：中国科研评价体系僵化或制约创新突破",
        "en_title": "Scientists warn rigid metrics may hamper China's innovation drive",
        "published": "18:00 2026年8月1日",
        "zh_summary": "上海自然科学研究院对话指出，追赶式增长模式收窄，指标导向与权威崇拜成科技突破核心障碍。",
        "en_summary": "Leading scholars said metric-driven culture and deference to authority may limit China's scientific ambitions.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/china/science/article/3362637/chinas-catch-era-ends-whats-standing-way-tech-innovation",
    },
    # 财经 Finance & Business (4)
    {
        "cat": ("财经 Finance & Business", "财经 Finance & Business"),
        "zh_title": "美国二季度GDP年化增速降至1.5%，低于市场预期",
        "en_title": "US Q2 GDP growth slows to 1.5% annual rate, below forecasts",
        "published": "20:30 2026年7月30日",
        "zh_summary": "商务部数据显示，二季度增速从一季度2.1%回落，政府支出、投资和出口走弱，消费支出仍增3.2%。",
        "en_summary": "Commerce Department data showed growth slowed from 2.1% in Q1 as government spending and exports weakened.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cd0xvrmlx2eo",
    },
    {
        "cat": ("财经 Finance & Business", "财经 Finance & Business"),
        "zh_title": "亚马逊财报强劲股价大涨，苹果因供应约束指引疲软下挫",
        "en_title": "Amazon surges on earnings while Apple sinks on supply-constraint outlook",
        "published": "20:42 2026年8月1日",
        "zh_summary": "亚马逊营收同比增20%至2006亿美元，AWS增长37%；苹果虽盈利超预期，但警告供应瓶颈将拖累增长。",
        "en_summary": "Amazon revenue rose 20% with AWS up 37%; Apple fell 7% after warning supply constraints would hurt growth.",
        "source_zh": "Fortune", "source_en": "Fortune",
        "url": "https://fortune.com/2026/08/01/amazon-apple-earnings-stock-market-july/",
    },
    {
        "cat": ("财经 Finance & Business", "财经 Finance & Business"),
        "zh_title": "财报季显示市场更挑剔AI资本开支，云业务获赏硬件承压",
        "en_title": "Earnings season shows investors scrutinizing AI capex more closely",
        "published": "00:00 2026年8月1日",
        "zh_summary": "标普500二季度盈利有望增29%，但科技巨头巨额AI投入引发回报质疑，微软获捧而Meta遭抛售。",
        "en_summary": "Strong S&P 500 profits met skepticism over AI spending; cloud revenue winners rose while heavy spenders sold off.",
        "source_zh": "Financial Post", "source_en": "Financial Post",
        "url": "https://financialpost.com/pmn/business-pmn/ai-isnt-a-catch-all-trade-for-stocks-in-this-earnings-season",
    },
    {
        "cat": ("财经 Finance & Business", "财经 Finance & Business"),
        "zh_title": "亚马逊二季度营收2006亿美元，AWS创18个季度来最快增速",
        "en_title": "Amazon Q2 revenue hits $200.6B as AWS posts fastest growth in 18 quarters",
        "published": "00:00 2026年7月31日",
        "zh_summary": "公司二季度营业利润275亿美元，同比增43%；全年资本开支指引上调至约2200亿美元以应对AI需求。",
        "en_summary": "Operating income rose 43% to $27.5B; full-year capex guidance was raised to about $220B on AI demand.",
        "source_zh": "Amazon IR", "source_en": "Amazon Investor Relations",
        "url": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/",
    },
    # 社会 Society (3)
    {
        "cat": ("社会 Society", "社会 Society"),
        "zh_title": "莫斯科高档餐厅外爆炸致3死21伤，女子携炸弹被保安拦下",
        "en_title": "Moscow restaurant bombing kills 3 and wounds at least 21",
        "published": "01:00 2026年8月2日",
        "zh_summary": "俄反恐委员会称，一名女子试图将爆炸装置带入餐厅被拒后引爆，死者含袭击者、保安及一名顾客。",
        "en_summary": "Russia said a woman carrying a bomb was stopped by a guard before the blast near an upscale Italian restaurant.",
        "source_zh": "美联社 AP", "source_en": "Associated Press",
        "url": "https://apnews.com/article/russia-moscow-explosion-98b7fe61ce6a81f679126844ea182445",
    },
    {
        "cat": ("社会 Society", "社会 Society"),
        "zh_title": "美国校园枪手父亲被判15年监禁，为该国第三宗家长担责案",
        "en_title": "Father of teen school shooter sentenced to 15 years in prison",
        "published": "08:00 2026年8月1日",
        "zh_summary": "佐治亚州法院判处科林·格雷15年徒刑，其子2024年在阿帕拉契高中枪杀4人，所用步枪为父亲所赠。",
        "en_summary": "Colin Gray was sentenced for the 2024 Apalachee High School attack in Georgia; his son used a rifle he had given him.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c78g4y18rxgo",
    },
    {
        "cat": ("社会 Society", "社会 Society"),
        "zh_title": "内华达州51区附近山火蔓延逾1.35万英亩，仅7%得到控制",
        "en_title": "Nevada wildfire near Area 51 burns over 13,500 acres, 7% contained",
        "published": "00:00 2026年8月1日",
        "zh_summary": "雷击引发的鹌鹑泉山火已燃烧近一周，在军方禁区内快速蔓延；官方称暂无民宅受威胁，附近小镇或有烟雾。",
        "en_summary": "The lightning-sparked Quail Springs Fire has burned for nearly a week in a restricted military zone near Area 51.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c89nenqg10wo",
    },
    # 国际 World (5)
    {
        "cat": ("国际 World", "国际 World"),
        "zh_title": "俄军再袭基辅致至少9死33伤，泽连斯基称爱国者拦截弹已耗尽",
        "en_title": "Russian strike on Kyiv kills at least 9 as Patriot interceptors run short",
        "published": "20:02 2026年8月1日",
        "zh_summary": "乌方称俄发射35枚导弹含27枚弹道导弹及185架无人机，仅拦截1枚；立陶宛驻基辅使馆亦受损。",
        "en_summary": "Ukraine said Russia fired 35 missiles and 185 drones overnight; only one ballistic missile was intercepted.",
        "source_zh": "美联社 AP", "source_en": "Associated Press",
        "url": "https://apnews.com/article/russia-ukraine-war-zelenskyy-missile-attack-ballistics-eb62397d10bca2d6db4269a3bcfc9dc6",
    },
    {
        "cat": ("国际 World", "国际 World"),
        "zh_title": "特朗普称尚未同意乌克兰自主生产爱国者导弹",
        "en_title": "Trump says US has not agreed to let Ukraine build Patriot missiles",
        "published": "04:00 2026年8月1日",
        "zh_summary": "特朗普在戴维营内阁会议上称共享该技术风险高，与三周前在北约峰会上承诺授权生产形成反差。",
        "en_summary": "Trump said at Camp David the US has not agreed to license Patriot production, reversing an earlier NATO pledge.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c86n0336082o",
    },
    {
        "cat": ("国际 World", "国际 World"),
        "zh_title": "欧盟将紧急会商休达移民危机，西班牙批评部分成员国反应自私",
        "en_title": "EU to hold emergency talks on Ceuta migrant crisis as Spain hits back",
        "published": "04:30 2026年8月2日",
        "zh_summary": "约6万人7月30日涌入西班牙休达，至少67人死亡；22国呼吁周二召开内政部长视频会议协调应对。",
        "en_summary": "After 60,000 migrants entered Ceuta with at least 67 deaths, 22 EU states called for emergency talks Tuesday.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cz7d17r455go",
    },
    {
        "cat": ("国际 World", "国际 World"),
        "zh_title": "美国敦促中东地区公民做好撤离准备，警惕局势意外升级",
        "en_title": "US urges citizens in Middle East to be ready to leave amid escalation risk",
        "published": "00:57 2026年8月2日",
        "zh_summary": "多国外交使团发布安全提醒，称应警惕航班取消和空域关闭，建议在地区美国人考虑离境或随时撤离。",
        "en_summary": "US embassies warned Americans to prepare for flight cancellations and consider departing the Middle East.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/world/middle-east/article/3362658/us-embassies-urge-citizens-consider-departing-middle-east",
    },
    {
        "cat": ("国际 World", "国际 World"),
        "zh_title": "登山家普尔亚在巴基斯坦雪崩中遇难，10人探险队全员罹难",
        "en_title": "Mountaineer Nirmal Purja killed in Pakistan avalanche with full team",
        "published": "20:34 2026年8月1日",
        "zh_summary": "其公司Elite Expeditions确认，43岁的普尔亚及布洛阿特峰探险队其余9人在7月30日雪崩中遇难。",
        "en_summary": "Elite Expeditions confirmed Purja, 43, and nine others died in a July 30 avalanche on Broad Peak.",
        "source_zh": "亚洲新闻台 CNA", "source_en": "Channel NewsAsia",
        "url": "https://www.channelnewsasia.com/asia/nepali-climber-nirmal-purja-die-pakistan-avalanche-6292801",
    },
    # 香港本地 Hong Kong (4)
    {
        "cat": ("香港本地 Hong Kong", "香港本地 Hong Kong"),
        "zh_title": "香港工地禁烟两周年首月：1200次巡查开出36张罚单",
        "en_title": "Hong Kong issues 36 smoking fines after 1,200 construction site checks",
        "published": "11:12 2026年8月1日",
        "zh_summary": "劳工处称7月17日全面禁烟以来，已对36名工人各罚3000港元，并向9家承建商发出改善通知书。",
        "en_summary": "Labour officials fined 36 workers HK$3,000 each and issued nine improvement notices since the July 17 ban.",
        "source_zh": "香港电台 RTHK", "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1864582-20260801.htm",
    },
    {
        "cat": ("香港本地 Hong Kong", "香港本地 Hong Kong"),
        "zh_title": "香港今年首宗输入性基孔肯雅热个案，12岁男童佛山染疫",
        "en_title": "Hong Kong reports first imported chikungunya fever case this year",
        "published": "20:26 2026年8月1日",
        "zh_summary": "观塘12岁男童7月17至30日在佛山期间被蚊叮咬，返港后确诊；卫生防护中心已加强灭蚊及流行病学调查。",
        "en_summary": "A 12-year-old Kwun Tong boy tested positive after travel to Foshan; health authorities intensified mosquito control.",
        "source_zh": "香港政府新闻处", "source_en": "Hong Kong Government",
        "url": "https://www.info.gov.hk/gia/general/202508/02/P2025080200897.htm",
    },
    {
        "cat": ("香港本地 Hong Kong", "香港本地 Hong Kong"),
        "zh_title": "香港是否应规管手游「开箱」机制引发社会讨论",
        "en_title": "Calls grow in Hong Kong to regulate mobile game loot boxes",
        "published": "09:00 2026年8月1日",
        "zh_summary": "调查显示部分玩家六年花费逾9万港元抽卡，议员及辅导机构呼吁借鉴海外经验防止成瘾性消费。",
        "en_summary": "Surveys show some players spent over HK$90,000 on loot boxes in six years, fueling calls for regulation.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3362601/should-hong-kong-regulate-loot-boxes-addiction-issues-arise-mobile-gaming",
    },
    {
        "cat": ("香港本地 Hong Kong", "香港本地 Hong Kong"),
        "zh_title": "劳工处处长：改变工地吸烟文化需时，正探索无人机红外巡查",
        "en_title": "Labour chief says changing site smoking culture will take time",
        "published": "12:57 2026年8月1日",
        "zh_summary": "许泽森称多数罚单来自突击检查，正研究在无人机上安装红外设备以提升执法效率，并考虑起诉两宗承建商。",
        "en_summary": "Commissioner Sam Hui said most fines came from surprise checks and infrared drones are being explored.",
        "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3362626/it-will-take-time-change-smoking-culture-official-says-after-1200-site-checks",
    },
    # 其他 Other (2)
    {
        "cat": ("其他 Other", "其他 Other"),
        "zh_title": "世卫组织：刚果（金）本轮埃博拉疫情为该国历史最严重",
        "en_title": "WHO says DR Congo Ebola outbreak is country's worst on record",
        "published": "00:30 2026年8月2日",
        "zh_summary": "截至7月30日确诊3605例、死亡1587例，病死率44%；上周单周新增病例和死亡均创疫情以来新高。",
        "en_summary": "As of July 30 there were 3,605 confirmed cases and 1,587 deaths, with the deadliest week yet reported.",
        "source_zh": "BBC", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cy07qe0knvzo",
    },
    {
        "cat": ("其他 Other", "其他 Other"),
        "zh_title": "因私投计划遭抵制，国际足联主席因凡蒂诺面临全面审查呼声",
        "en_title": "Concacaf calls for full review of FIFA leadership after investment U-turn",
        "published": "17:51 2026年8月1日",
        "zh_summary": "欧足联称对因凡蒂诺失去信任，中北美足联要求全面审查其领导，此前世界杯引资计划已被撤回。",
        "en_summary": "Uefa lost confidence in Infantino and Concacaf demanded a leadership review after private investment plans collapsed.",
        "source_zh": "BBC Sport", "source_en": "BBC Sport",
        "url": "https://www.bbc.co.uk/sport/football/articles/c04kr2nv3v3o",
    },
]


def build_html():
    date_display = "2026年8月2日"
    intro_zh = "汇总昨夜至今要闻，涵盖国际局势、市场动态、科技与港澳社会热点。"
    intro_en = "Overnight and early headlines spanning world affairs, markets, technology, and regional updates."

    cat_counts = {}
    for it in ITEMS:
        cat_counts[it["cat"][0]] = cat_counts.get(it["cat"][0], 0) + 1

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">',
        f'<title>每日热点早报 Morning Briefing - {BRIEFING_DATE}</title></head>',
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">',
        '<tr><td align="center">',
        '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">',
        # Header
        '<tr><td style="background:linear-gradient(135deg,#1a237e 0%,#283593 100%);padding:28px 24px;text-align:center;">',
        '<div style="color:#fff;font-size:26px;font-weight:700;letter-spacing:2px;">每日热点早报</div>',
        f'<div style="color:#c5cae9;font-size:14px;margin-top:8px;">Morning News Briefing · {date_display} · 共{TOTAL}条</div>',
        '</td></tr>',
        # Intro
        '<tr><td style="padding:20px 24px;border-bottom:1px solid #e8eaf6;">',
        f'<p style="margin:0 0 8px;font-size:15px;color:#333;line-height:1.6;">{intro_zh}</p>',
        f'<p style="margin:0;font-size:14px;color:#666;font-style:italic;line-height:1.5;">{intro_en}</p>',
        '</td></tr>',
    ]

    current_cat = None
    num = 0
    for it in ITEMS:
        if it["cat"][0] != current_cat:
            current_cat = it["cat"][0]
            cat_zh, cat_en = it["cat"]
            parts.append(
                '<tr><td style="padding:16px 24px 8px;">'
                f'<h2 style="margin:0;padding:10px 14px;background:#f5f5f5;border-left:4px solid #1565c0;font-size:16px;color:#1a237e;">'
                f'{cat_zh}<br><span style="font-size:13px;color:#666;font-weight:normal;">{cat_en}</span></h2>'
                '</td></tr>'
            )
        num += 1
        n = f"{num:02d}"
        parts.append(
            '<tr><td style="padding:8px 24px 16px;border-bottom:1px solid #f0f0f0;">'
            f'<div style="font-size:12px;color:#1565c0;font-weight:700;margin-bottom:4px;">{n}</div>'
            f'<a href="{it["url"]}" style="font-size:16px;font-weight:600;color:#1a237e;text-decoration:none;line-height:1.4;">{it["zh_title"]}</a>'
            f'<div style="font-size:14px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;">{it["en_title"]}</div>'
            f'<div style="font-size:12px;color:#999;margin-top:4px;">发布时间 Published: {it["published"]}</div>'
            f'<p style="margin:8px 0 4px;font-size:14px;color:#333;line-height:1.6;">{it["zh_summary"]}</p>'
            f'<p style="margin:0 0 10px;font-size:13px;color:#666;line-height:1.5;">{it["en_summary"]}</p>'
            '<div style="margin-top:8px;">'
            f'<span style="display:inline-block;background:#e3f2fd;color:#1565c0;font-size:11px;padding:3px 8px;border-radius:4px;margin-right:8px;">{it["source_zh"]}</span>'
            f'<a href="{it["url"]}" style="font-size:12px;color:#1565c0;text-decoration:none;">查看全文 Read more →</a>'
            '</div></td></tr>'
        )

    parts.extend([
        '<tr><td style="padding:20px 24px;background:#fafafa;font-size:11px;color:#999;line-height:1.6;">',
        '<p style="margin:0 0 6px;">本简报由自动化系统汇编，仅供参考，不构成投资建议。新闻版权归原媒体所有。</p>',
        '<p style="margin:0;">This briefing is auto-compiled for reference only, not investment advice. News copyrights belong to original publishers.</p>',
        '</td></tr>',
        '</table></td></tr></table></body></html>',
    ])
    return "".join(parts), cat_counts


def main():
    html, cat_counts = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {BRIEFING_DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"HTML chars: {len(html)}")
    print(f"Categories: {cat_counts}")
    print(f"Written: {path}")


if __name__ == "__main__":
    main()
