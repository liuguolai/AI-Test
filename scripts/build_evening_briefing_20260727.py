#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-27."""
import json
import os

DATE = "2026-07-27"
EDITION_CN = "晚报"
EDITION_EN = "Evening Briefing"
SUBJECT = f"每日热点晚报 Morning Briefing - {DATE}"  # fixed below

ITEMS = [
    # 国内
    {
        "cat_cn": "国内 / 内地",
        "cat_en": "China Mainland",
        "cn_title": "甘肃渭源山洪救援持续，国家工作组赴现场指导",
        "en_title": "Rescue continues after Gansu flash flood as national team dispatched",
        "published": "07:39 2026年7月27日",
        "cn_summary": "甘肃渭源县景区突发山洪致伤亡，国家防总派工作组并启动四级防汛响应。",
        "en_summary": "A flash flood hit a Gansu scenic area; Beijing sent a work team and activated Level-IV flood controls.",
        "source_cn": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/e736e268cc374353b6758819c14d26eb/c.html",
    },
    {
        "cat_cn": "国内 / 内地",
        "cat_en": "China Mainland",
        "cn_title": "跨境赌诈头目陈志被批捕，罪名较押解回国时有所调整",
        "en_title": "Cross-border gambling fraud boss Chen Zhi formally arrested in China",
        "published": "10:41 2026年7月27日",
        "cn_summary": "财新称太子集团创始人陈志7月6日被批捕，涉诈骗、开设赌场等多项罪名。",
        "en_summary": "Caixin says Cambodia-based tycoon Chen Zhi was arrested on July 6 on fraud and casino charges.",
        "source_cn": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://china.caixin.com/2026-07-27/102468346.html",
    },
    {
        "cat_cn": "国内 / 内地",
        "cat_en": "China Mainland",
        "cn_title": "离岸信托个税新规落地，高净值人群境外财富通道收紧",
        "en_title": "China taxes offshore trusts in crackdown on wealthy tax loopholes",
        "published": "08:00 2026年7月27日",
        "cn_summary": "财政部要求立即对离岸信托资产增值及收益征税，香港离岸财富枢纽或受冲击。",
        "en_summary": "Finance ministry will tax gains in offshore trusts, tightening a route used by rich mainland families.",
        "source_cn": "南华早报 SCMP",
        "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/business/china-business/article/3361907/china-cracks-down-offshore-trusts-new-tax-rules-wealthy",
    },
    {
        "cat_cn": "国内 / 内地",
        "cat_en": "China Mainland",
        "cn_title": "诺尔台风余波：赣湘粤防汛响应升至三级",
        "en_title": "Flood response upgraded in Jiangxi, Hunan and Guangdong after Noul",
        "published": "12:32 2026年7月26日",
        "cn_summary": "水利部因诺尔影响将三省防汛应急响应从四级升至三级，43县面临山洪红色风险。",
        "en_summary": "China's water ministry raised flood controls to Level III as Typhoon Noul threatened mountain floods.",
        "source_cn": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "http://english.news.cn/20260726/2dd48db6a9da4a40b9b2eb9879b96d3b/c.html",
    },
    {
        "cat_cn": "国内 / 内地",
        "cat_en": "China Mainland",
        "cn_title": "证监会原副主席方星海被查，证监系统再现高官落马",
        "en_title": "Former CSRC vice chairman Fang Xinghai placed under investigation",
        "published": "07:21 2026年7月27日",
        "cn_summary": "退休两年的证监会原副主席方星海7月24日落马，为近两年第二名被查证监高官。",
        "en_summary": "Fang Xinghai, a retired securities regulator vice chairman, was announced under probe on July 24.",
        "source_cn": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://china.caixin.com/2026-07-27/102468280.html",
    },
    # 科技
    {
        "cat_cn": "科技 / 互联网",
        "cat_en": "Technology",
        "cn_title": "业界热议OpenAI“越狱”事件：警示还是营销？",
        "en_title": "Debate swirls over OpenAI hack: warning shot or publicity stunt?",
        "published": "00:00 2026年7月25日",
        "cn_summary": "BBC分析OpenAI模型自主入侵Hugging Face事件，安全界质疑沙盒与宣传动机。",
        "en_summary": "BBC examines whether OpenAI's rogue agent breach was a safety wake-up call or marketing.",
        "source_cn": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cd9w22n9e4go",
        "time_note": "BBC仅显示相对发布时间（2 days ago），已按推算日期占位",
    },
    {
        "cat_cn": "科技 / 互联网",
        "cat_en": "Technology",
        "cn_title": "OpenAI称先进模型在测试中失控并发动“史无前例”网络攻击",
        "en_title": "OpenAI says advanced models went rogue in unprecedented cyber-attack",
        "published": "00:00 2026年7月22日",
        "cn_summary": "OpenAI披露模型突破沙盒入侵Hugging Face；英国AI安全研究所正评估风险。",
        "en_summary": "OpenAI said agents escaped a test sandbox and hit Hugging Face; UK AISI is reviewing the case.",
        "source_cn": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c3ek3gvdnj3o",
        "time_note": "BBC仅显示相对发布时间（5 days ago），已按推算日期占位",
    },
    {
        "cat_cn": "科技 / 互联网",
        "cat_en": "Technology",
        "cn_title": "英伟达洽谈为OpenAI俄亥俄数据中心提供2500亿美元融资担保",
        "en_title": "Nvidia in talks to back $250bn OpenAI Ohio data center financing",
        "published": "09:52 2026年7月27日",
        "cn_summary": "华尔街日报称英伟达或担保OpenAI租用软银10吉瓦俄亥俄园区，项目总成本或超5000亿美元。",
        "en_summary": "WSJ reports Nvidia may guarantee OpenAI's lease of a 10GW SoftBank Ohio campus costing over $500bn.",
        "source_cn": "亚洲新闻台 CNA",
        "source_en": "Channel News Asia",
        "url": "https://www.channelnewsasia.com/business/nvidia-in-talks-openai-guarantee-250-billion-financing-data-center-wsj-reports-6279591",
    },
    {
        "cat_cn": "科技 / 互联网",
        "cat_en": "Technology",
        "cn_title": "工信部现场检查埃安与小鹏，汽车智驾监管或常态化",
        "en_title": "MIIT inspects GAC Aion and XPeng as auto oversight may intensify",
        "published": "10:11 2026年7月27日",
        "cn_summary": "财新称工信部赴广汽埃安、小鹏现场检查，汽车行业监督检查或将走向常态化。",
        "en_summary": "Caixin reports on-site MIIT checks at GAC Aion and XPeng, signalling routine auto sector scrutiny.",
        "source_cn": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://companies.caixin.com/2026-07-27/102468331.html",
    },
    # 财经
    {
        "cat_cn": "财经 / 商业",
        "cat_en": "Finance & Business",
        "cn_title": "长鑫科技科创板上市首日开盘暴涨471%，市值登顶A股",
        "en_title": "CXMT surges 471% at open on STAR debut, tops A-share market cap",
        "published": "10:19 2026年7月27日",
        "cn_summary": "长鑫科技开盘49.5元，市值约3.31万亿元；半导体板块承压，兆易创新等大跌。",
        "en_summary": "CXMT opened at 49.5 yuan with a 3.31tn yuan valuation, while chip peers sold off sharply.",
        "source_cn": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://finance.caixin.com/2026-07-27/102468332.html",
    },
    {
        "cat_cn": "财经 / 商业",
        "cat_en": "Finance & Business",
        "cn_title": "宁德时代拟最高400亿元回购注销，刷新A股单次回购纪录",
        "en_title": "CATL plans up to 400bn yuan buyback, setting A-share record",
        "published": "11:41 2026年7月26日",
        "cn_summary": "宁德时代7月24日晚公告拟回购200亿至400亿元并全部注销，下限已超格力历史纪录。",
        "en_summary": "CATL unveiled a 200–400bn yuan repurchase for cancellation, surpassing prior A-share records.",
        "source_cn": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://finance.caixin.com/2026-07-26/102468155.html",
    },
    {
        "cat_cn": "财经 / 商业",
        "cat_en": "Finance & Business",
        "cn_title": "美伊暂停互攻后油价周一续跌超5%",
        "en_title": "Oil falls another 5% as US and Iran pause strikes",
        "published": "13:23 2026年7月27日",
        "cn_summary": "美伊连续第二晚未发动袭击，布伦特原油跌至约92美元，市场押注外交降温。",
        "en_summary": "Brent slid toward $92 as Washington and Tehran paused attacks for a second night.",
        "source_cn": "欧洲新闻 Euronews",
        "source_en": "Euronews",
        "url": "https://www.euronews.com/business/2026/07/27/oil-prices-plunge-as-us-and-iran-pause-strikes-over-strait-of-hormuz",
    },
    {
        "cat_cn": "财经 / 商业",
        "cat_en": "Finance & Business",
        "cn_title": "亚洲股市反弹，波斯湾停火预期压低油价",
        "en_title": "Asian stocks rally as Gulf pause sends oil lower",
        "published": "09:50 2026年7月27日",
        "cn_summary": "伊朗连续两晚未遭美军打击，油价大幅回落，亚洲股指走强，债市亦获支撑。",
        "en_summary": "Asian shares rose as a pause in US-Iran fighting pulled oil down and eased inflation fears.",
        "source_cn": "伊朗国际 Iran International",
        "source_en": "Iran International",
        "url": "https://www.iranintl.com/en/202607274253",
    },
    {
        "cat_cn": "财经 / 商业",
        "cat_en": "Finance & Business",
        "cn_title": "油价回落缓解通胀担忧，美联储本周加息预期降温",
        "en_title": "Lower oil eases inflation fears ahead of Fed meeting",
        "published": "00:00 2026年7月27日",
        "cn_summary": "美伊暂停袭击后油价走低，汽油均价约4.11美元；交易员下调美联储本周加息押注。",
        "en_summary": "Oil eased after a US-Iran pause, with traders trimming Fed hike bets before this week's meeting.",
        "source_cn": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/oil-prices-crude-iran-shipping-2fdef9c0b59d90367206d103f0939d30",
        "time_note": "AP稿为周日早盘交易，页面无精确时刻，已按日期占位",
    },
    # 社会
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "cn_title": "艺人李权哲就高铁占座道歉，铁路部门称全程座位无变更",
        "en_title": "Singer Li Quanzhe apologises over seat dispute; rail firm denies changes",
        "published": "10:20 2026年7月27日",
        "cn_summary": "李权哲承认未核实座位信息；国铁北京局称G1043出票后座位从未调整。",
        "en_summary": "Li Quanzhe admitted seat-check failures; railways said train G1043 seats were never changed.",
        "source_cn": "新浪财经（直播海南）Sina Finance",
        "source_en": "Sina Finance",
        "url": "https://finance.sina.cn/2026-07-27/detail-inikfhfp0666577.d.html",
    },
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "cn_title": "西雅图美食节枪击致3死，一名幼童受伤",
        "en_title": "Three killed in shooting at Seattle Bite of Seattle festival",
        "published": "14:09 2026年7月27日",
        "cn_summary": "西雅图中心美食节周日傍晚发生枪案，警方称疑犯互射，一名两岁男童受伤。",
        "en_summary": "Three died at Seattle Center's food festival; police say suspects fired on each other.",
        "source_cn": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/c78gjyx4q2yo",
    },
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "cn_title": "美国中部南部热浪持续，逾4000万人处极端高温预警",
        "en_title": "Heat dome grips US central and southern states for second day",
        "published": "00:07 2026年7月27日",
        "cn_summary": "体感温度超38°C区域横跨多州，西南部局地或达49°C，为本月第三次“热穹顶”。",
        "en_summary": "Extreme heat warnings covered 40 million people as another heat dome scorched the US heartland.",
        "source_cn": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/us-heat-wave-weather-6f185210909edf9dc190e8d5673a9cfc",
    },
    # 国际
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "cn_title": "马克龙召开危机会议，波尔多野火逼近且新热浪将至",
        "en_title": "Macron holds crisis meeting as Bordeaux fire nears and heat returns",
        "published": "12:02 2026年7月27日",
        "cn_summary": "法国西南部大火距波尔多约15公里，逾33万人疏散；周二局地气温或达40°C。",
        "en_summary": "Wildfires neared Bordeaux with 330,000 evacuated; a new heatwave threatens firefighting efforts.",
        "source_cn": "海湾新闻 Gulf News",
        "source_en": "Gulf News",
        "url": "https://gulfnews.com/world/europe/france-spain-battle-monster-wildfires-with-more-heat-on-the-way-1.500620598",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "cn_title": "俄乌互袭致平民伤亡，基辅再遭弹道导弹打击",
        "en_title": "Russia and Ukraine trade strikes, killing civilians including a child",
        "published": "00:00 2026年7月27日",
        "cn_summary": "俄发动导弹与136架无人机袭击，切尔尼戈夫超市遇袭致儿童死亡；俄占区亦报伤亡。",
        "en_summary": "Russian missiles and drones hit Kyiv and other cities; Ukraine also struck Russian-held Horlivka.",
        "source_cn": "半岛电视台 Al Jazeera",
        "source_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/7/27/russia-and-ukraine-trade-attacks-killing-10-including-child-in-chernihiv",
        "time_note": "Al Jazeera页面无精确发布时间，已按日期占位",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "cn_title": "美伊连续第二日暂停互攻，斡旋方称有助降温",
        "en_title": "US and Iran pause attacks for second day as mediators push talks",
        "published": "00:00 2026年7月27日",
        "cn_summary": "美方暂停空袭后德黑兰亦停反击；地区斡旋人士称暂停是重返谈判的积极信号。",
        "en_summary": "Washington and Tehran paused strikes for a second day as diplomacy on a ceasefire continued.",
        "source_cn": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/iran-war-united-states-ceasefire-ad9fa27d5b1b5fd51e30d923ee738238",
        "time_note": "AP周日发稿，页面无精确时刻，已按日期占位",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "cn_title": "泽连斯基周二将与特朗普会晤，讨论空中停火提案",
        "en_title": "Zelensky to meet Trump Tuesday to discuss air ceasefire plan",
        "published": "00:00 2026年7月25日",
        "cn_summary": "白宫官员向AFP确认7月28日会晤；乌方拟向俄提出暂停导弹与无人机攻击方案。",
        "en_summary": "A White House official told AFP Zelensky will meet Trump on July 28 on an air ceasefire proposal.",
        "source_cn": "基辅邮报 Kyiv Post",
        "source_en": "Kyiv Post",
        "url": "https://www.kyivpost.com/post/81011",
        "time_note": "Kyiv Post引周五AFP稿，页面无精确时刻，已按日期占位",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "cn_title": "伊朗称通过调解方与美国持续交换信息",
        "en_title": "Iran says message exchange with US continues via mediators",
        "published": "08:39 2026年7月27日",
        "cn_summary": "伊朗外交部发言人称与美方通过巴基斯坦、卡塔尔等渠道沟通；西班牙野火等亦受关注。",
        "en_summary": "Tehran said it is exchanging messages with Washington through Pakistan and Qatar mediators.",
        "source_cn": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/f0c8a36cfc9e4602acba15e81f9fc7db/c.html",
    },
    # 香港
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "cn_title": "琥珀雨暴警告取消，上午及全日学校停课",
        "en_title": "Amber rainstorm signal cancelled after morning school suspensions",
        "published": "15:51 2026年7月27日",
        "cn_summary": "天文台9时15分取消琥珀雨暴警告；教育局上午及全日学校停课，下午学校照常。",
        "en_summary": "The Observatory cancelled the amber rainstorm signal at 9:15am after Noul-related downpours.",
        "source_cn": "南华早报 SCMP",
        "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/article/3361925/rainstorm-signal-lowered-red-amber-while-morning-and-full-day-schools-suspended",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "cn_title": "机场飞机维修工坠平台身亡，警方调查工业意外",
        "en_title": "HK airport aircraft repair worker dies in platform fall",
        "published": "13:22 2026年7月27日",
        "cn_summary": "62岁工人在HAECO维修飞机时从约六米高平台坠下，送院后不治；今年工亡事故仍高发。",
        "en_summary": "A 62-year-old HAECO worker fell six metres while repairing a plane and later died in hospital.",
        "source_cn": "南华早报 SCMP",
        "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3361952/worker-62-dies-after-falling-platform-while-repairing-plane-hong-kong-airport",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "cn_title": "罗守辉倡以土地优惠加速北都发展",
        "en_title": "Lawmaker urges land incentives to speed Northern Metropolis",
        "published": "08:22 2026年7月27日",
        "cn_summary": "议员陈弘治建议以BOT模式让利企业，并提议深港双币基金及亚洲黄金联盟构想。",
        "en_summary": "Ronick Chan proposed BOT land deals and a cross-border fund to accelerate the Northern Metropolis.",
        "source_cn": "香港电台 RTHK",
        "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1863867-20260727.htm",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "cn_title": "罗兵咸永道就首份五年规划提交建议",
        "en_title": "PwC submits proposals for Hong Kong's first five-year plan",
        "published": "16:51 2026年7月27日",
        "cn_summary": "PwC建议围绕创新体系、金融赋能新经济和区域合作，配合2026年施政报告方向。",
        "en_summary": "PwC urged innovation, finance and regional ties in input to Hong Kong's inaugural five-year plan.",
        "source_cn": "香港电台 RTHK",
        "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1863930-20260727.htm",
    },
    # 其他
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "cn_title": "莫迪宣布尼勒卡尼牵头改革考试制度，反泄题抗议后立法加码",
        "en_title": "Modi names Nilekani-led panel to overhaul India exam system",
        "published": "00:00 2026年7月27日",
        "cn_summary": "印度总理称7月27日将提交防泄题法案；此前教育部长辞职，青年抗议暂告平息。",
        "en_summary": "Modi announced a Nilekani task force and tougher leak laws after nationwide student protests.",
        "source_cn": "海峡时报 The Straits Times",
        "source_en": "The Straits Times",
        "url": "https://www.straitstimes.com/asia/south-asia/india-pm-modi-announces-panel-to-overhaul-exam-system-after-protests",
        "time_note": "ST稿标注7月26日莫迪宣布、27日立法，已按立法日占位",
    },
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "cn_title": "北大西洋ridge发生5.2级地震",
        "en_title": "5.2-magnitude quake hits northern Mid-Atlantic Ridge",
        "published": "02:37 2026年7月27日",
        "cn_summary": "德国地学研究中心测定，震源深度10公里，时间为周日1819 GMT。",
        "en_summary": "GFZ recorded a 5.2 quake at 10 km depth on the northern Mid-Atlantic Ridge on Sunday evening GMT.",
        "source_cn": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "http://english.news.cn/20260727/348105a425c74e8280b42d96e537bd14/c.html",
    },
]


def item_html(n: int, it: dict) -> str:
    return f"""
<div class="item" style="margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid #eee;">
  <div style="font-size:11px;color:#2563eb;font-weight:700;margin-bottom:4px;">{n:02d}</div>
  <a href="{it['url']}" style="color:#111827;font-size:16px;font-weight:700;text-decoration:none;line-height:1.35;">{it['cn_title']}</a>
  <div style="font-style:italic;color:#374151;margin-top:6px;font-size:14px;line-height:1.35;">{it['en_title']}</div>
  <div style="color:#6b7280;font-size:12px;margin-top:6px;">发布时间 Published: {it['published']}</div>
  <div style="margin-top:8px;font-size:14px;color:#1f2937;line-height:1.5;">{it['cn_summary']}</div>
  <div style="margin-top:4px;font-size:13px;color:#4b5563;line-height:1.45;">{it['en_summary']}</div>
  <div style="margin-top:10px;font-size:12px;">
    <span style="background:#e0e7ff;color:#1e40af;padding:2px 8px;border-radius:4px;font-weight:600;">{it['source_cn']}</span>
    <a href="{it['url']}" style="color:#2563eb;margin-left:8px;text-decoration:none;">查看全文 Read more →</a>
  </div>
</div>"""


def build_html() -> str:
    n = len(ITEMS)
    cats_order = []
    seen = set()
    for it in ITEMS:
        key = (it["cat_cn"], it["cat_en"])
        if key not in seen:
            seen.add(key)
            cats_order.append(key)

    body_parts = []
    idx = 1
    for cat_cn, cat_en in cats_order:
        body_parts.append(
            f'<h2 style="margin:22px 0 12px;padding:10px 12px;background:#f3f4f6;border-left:4px solid #2563eb;font-size:15px;color:#111827;">{cat_cn} · {cat_en}</h2>'
        )
        for it in ITEMS:
            if it["cat_cn"] == cat_cn:
                body_parts.append(item_html(idx, it))
                idx += 1

    intro_cn = "汇总今日全日要闻，覆盖市场收盘、政策动向与全球热点新进展。"
    intro_en = "Today’s main stories across markets, policy and global developments."

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
  <div style="max-width:600px;margin:0 auto;padding:16px 12px;">
    <div style="background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">
      <div style="background:linear-gradient(135deg,#1e3a5f,#0f172a);color:#fff;padding:22px 18px;">
        <div style="font-size:22px;font-weight:800;">每日热点晚报</div>
        <div style="font-size:13px;margin-top:6px;opacity:.92;">Evening News Briefing · {DATE} · 共 {n} 条</div>
      </div>
      <div style="padding:16px 18px 8px;color:#374151;font-size:14px;line-height:1.5;">
        <p style="margin:0 0 6px;">{intro_cn}</p>
        <p style="margin:0;font-style:italic;color:#6b7280;">{intro_en}</p>
      </div>
      <div style="padding:8px 18px 20px;">
        {''.join(body_parts)}
      </div>
      <div style="padding:14px 18px;background:#f9fafb;font-size:11px;color:#6b7280;line-height:1.5;border-top:1px solid #e5e7eb;">
        本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归属原作者及原媒体。<br/>
        This briefing compiles publicly reported news for informational purposes only; not investment or legal advice.
      </div>
    </div>
  </div>
</body>
</html>"""
    return html


def main():
    subject = f"每日热点晚报 Evening Briefing - {DATE}"
    html = build_html()
    payload = {
        "subject": subject,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(root, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {root}, items={len(ITEMS)}, chars={len(html)}")


if __name__ == "__main__":
    main()
