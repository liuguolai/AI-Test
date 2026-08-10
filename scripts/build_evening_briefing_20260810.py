#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-10."""

import json
import os

BRIEFING_EDITION = "晚报"
DATE = "2026-08-10"
DATE_CN = "2026年8月10日"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

ITEMS = [
    # 国内
    {
        "category": ("国内 / 内地", "China Mainland"),
        "zh_title": "迎战4700公里风雨考验：台风“白海豚”登陆浙江核心区",
        "en_title": "Typhoon Dolphin Makes Dual Landfall in Zhejiang After 4,700-km Track",
        "published": "01:22 2026年8月10日",
        "zh_summary": "强台风“白海豚”9日傍晚先后在台州玉环、温州乐清两次登陆，浙江多地转移安置、抢险救援连夜展开。",
        "en_summary": "Severe Typhoon Dolphin hit Zhejiang twice on Aug 9, triggering mass evacuations and round-the-clock rescue across eastern China.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/politics/20260810/f0af60ffec604f27ab51bfdfecbd582b/c.html",
    },
    {
        "category": ("国内 / 内地", "China Mainland"),
        "zh_title": "中国东部逾百万人撤离，台风“白海豚”带来强降雨",
        "en_title": "China Evacuates Over One Million as Typhoon Dolphin Brings Heavy Rain",
        "published": "09:44 2026年8月10日",
        "zh_summary": "台风登陆后上海近千人航班取消，浙江多地或现特大暴雨；菲律宾已有8人因相关降雨遇难。",
        "en_summary": "Flights were cancelled in Shanghai and heavy rain warnings spread eastward, with eight storm-related deaths reported in the Philippines.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cx2rgzyplg2o",
    },
    {
        "category": ("国内 / 内地", "China Mainland"),
        "zh_title": "白宫称理解内塔尼亚胡拒加沙和平计划出于选举需要",
        "en_title": "White House Says It Understands Netanyahu’s Gaza Plan Rejection",
        "published": "10:51 2026年8月10日",
        "zh_summary": "美官员称理解以总理政治考量，但要求其克制对加沙打击；内塔尼亚胡称哈马斯未真正解除武装前不会撤军。",
        "en_summary": "A U.S. official said Netanyahu’s rejection reflects election politics, while Israel insists troops will stay until Hamas is fully disarmed.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "http://www3.xinhuanet.com/20260810/955f5efda93148938e2181b21a5f744c/c.html",
    },
    {
        "category": ("国内 / 内地", "China Mainland"),
        "zh_title": "7月CPI同比上涨0.5%，PPI同比上涨3.5%",
        "en_title": "China’s July CPI Rises 0.5% and PPI 3.5% Year on Year",
        "published": "16:09 2026年8月9日",
        "zh_summary": "统计局数据显示消费价格温和上涨，工业出厂价格涨幅回落，分析师称下半年仍有促消费政策空间。",
        "en_summary": "Official data showed moderate consumer inflation and slower factory-gate price growth, leaving room for pro-consumption policies.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260809/b724c78d95c6480887092ff929558d08/c.html",
    },
    # 科技
    {
        "category": ("科技 / 互联网", "Technology"),
        "zh_title": "韩网络安全公司：朝鲜Kimsuky组织搭建本地AI攻击工具",
        "en_title": "North Korean Kimsuky Group Builds Local AI Tools for Cyberattacks",
        "published": "10:47 2026年8月10日",
        "zh_summary": "Genians称该组织部署Ollama、Cursor等工具，用于钓鱼、窃密分析与恶意软件开发自动化。",
        "en_summary": "Genians said Kimsuky deployed tools such as Ollama and Cursor to automate phishing, data analysis and malware development.",
        "source_zh": "路透社", "source_en": "Reuters",
        "url": "https://www.thestar.com.my/tech/tech-news/2026/08/10/north-korean-hacking-group-builds-ai-tools-for-cyberattacks-report-says",
    },
    {
        "category": ("科技 / 互联网", "Technology"),
        "zh_title": "五角大楼公布第五批UFO解密文件含41份影像资料",
        "en_title": "Pentagon Releases Fifth Batch of Declassified UFO Files",
        "published": "00:00 2026年8月7日",
        "zh_summary": "最新一批含41份文件与视频，包括中东球形飞行物及美国西部红外拍摄画面，部分为目击者描述艺术再现。",
        "en_summary": "The latest drop includes 41 files and videos, from Middle East orb sightings to U.S. infrared footage, some rendered from witness accounts.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/ce8kr7p2pmdo",
    },
    {
        "category": ("科技 / 互联网", "Technology"),
        "zh_title": "特朗普对多晶硅衍生品加征15%关税以应对中国竞争",
        "en_title": "Trump Imposes 15% Tariff on Polysilicon Derivatives to Counter China",
        "published": "00:00 2026年8月7日",
        "zh_summary": "白宫下令设最低进口价并加征关税，旨在保护美国芯片与太阳能供应链，措施将于12月4日生效。",
        "en_summary": "The White House set minimum import prices and a 15% tariff to shield U.S. chip and solar supply chains, effective December 4.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cdrvn686dljo",
    },
    {
        "category": ("科技 / 互联网", "Technology"),
        "zh_title": "SpaceX首批锁定期届满，可交易股份数量翻倍",
        "en_title": "SpaceX Shares Rise as First Post-IPO Lockup Expires",
        "published": "00:00 2026年8月6日",
        "zh_summary": "约9.12亿股解除限售，公众可交易股份较IPO时增加逾一倍，市场关注员工与早期投资者是否抛售。",
        "en_summary": "About 911.5 million shares became eligible to trade, more than doubling the public float since June’s record IPO.",
        "source_zh": "路透社", "source_en": "Reuters",
        "url": "https://www.reuters.com/business/spacex-shares-slip-lockup-expiry-adds-post-ipo-woes-2026-08-06/",
    },
    # 财经
    {
        "category": ("财经 / 商业", "Finance & Business"),
        "zh_title": "全球股市接近纪录高位，油价因霍尔木兹僵局上涨",
        "en_title": "Global Stocks Near Records as Oil Rises on Hormuz Impasse",
        "published": "16:49 2026年8月10日",
        "zh_summary": "弱于预期的美国就业数据降低联储9月加息预期，布伦特原油升至约84美元，投资者关注本周通胀数据。",
        "en_summary": "Soft U.S. jobs data eased Fed hike bets while Brent crude climbed toward $84 as Hormuz reopening talks stalled.",
        "source_zh": "彭博社", "source_en": "Bloomberg",
        "url": "https://www.swissinfo.ch/eng/global-stock-rally-extends%2c-oil-advances-on-iran%3a-markets-wrap/91870572",
    },
    {
        "category": ("财经 / 商业", "Finance & Business"),
        "zh_title": "亚洲股市上扬，美国疲软就业数据缓解加息担忧",
        "en_title": "Asian Shares Gain as Weak U.S. Jobs Data Ease Rate-Hike Fears",
        "published": "11:35 2026年8月10日",
        "zh_summary": "7月美国非农意外减少2.3万人，市场押注9月加息概率降至约44%，日股涨2%，油价继续走高。",
        "en_summary": "July’s surprise U.S. job loss cut September hike odds to about 44%, lifting Asian equities while oil prices kept climbing.",
        "source_zh": "星报", "source_en": "The Star",
        "url": "https://www.thestar.com.my/business/2026/08/10/asia-stocks-gain-oil-up-amid-gulf-confusion",
    },
    {
        "category": ("财经 / 商业", "Finance & Business"),
        "zh_title": "中国7月PPI涨幅放缓至3.5%，低于市场预期",
        "en_title": "China’s July PPI Growth Slows to 3.5%, Below Forecasts",
        "published": "12:47 2026年8月9日",
        "zh_summary": "全球能源价格回落拖累工业品价格，核心CPI同比涨0.9%，分析师称油价走势仍存不确定性。",
        "en_summary": "Factory-gate inflation cooled as energy prices retreated, with core CPI up 0.9% and analysts flagging oil-price uncertainty.",
        "source_zh": "路透社", "source_en": "Reuters",
        "url": "https://asia.nikkei.com/economy/china-july-factory-gate-inflation-eases-to-3-month-low-cpi-slows",
    },
    {
        "category": ("财经 / 商业", "Finance & Business"),
        "zh_title": "新兴市场资产普涨，投资者风险偏好回升",
        "en_title": "Emerging Markets Rally as Investors Regain Risk Appetite",
        "published": "11:06 2026年8月10日",
        "zh_summary": "MSCI新兴市场指数涨0.7%，美元走弱推动资金回流，市场转向关注本周美国CPI数据。",
        "en_summary": "The MSCI Emerging Markets Index rose 0.7% as a softer dollar drew flows back in, with focus shifting to U.S. CPI due this week.",
        "source_zh": "Whalesbook", "source_en": "Whalesbook",
        "url": "https://www.whalesbook.com/news/English/economy/Emerging-Markets-Rally-as-Weak-US-Jobs-Data-Eases-Fed-Hike-Fears/6a796350738044f4397c4f5d",
    },
    {
        "category": ("财经 / 商业", "Finance & Business"),
        "zh_title": "特朗普称倾向对伊朗经济施压而非军事打击",
        "en_title": "Trump Says He Prefers Economic Pressure Over Strikes on Iran",
        "published": "11:18 2026年8月10日",
        "zh_summary": "特朗普称正“低调”观望伊朗，海上封锁加剧其通胀；伊朗外长称在无美方补救前不会重启谈判。",
        "en_summary": "Trump said Washington is low-keying Iran pressure via a naval blockade, while Tehran ruled out talks until U.S. breaches are remedied.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/world/20260810/e28d697de87b4a7199a6fedf148feb1e/c.html",
    },
    # 社会
    {
        "category": ("社会", "Society"),
        "zh_title": "泰国前议员枪杀地方官员，校园枪击余波未平",
        "en_title": "Former Thai Lawmaker Kills Local Official Amid Gun-Control Debate",
        "published": "13:45 2026年8月10日",
        "zh_summary": "嫌犯称因1100万泰铢债务纠纷开枪，受害者不治；政府正推进校园安检与枪支管控新措施。",
        "en_summary": "A former MP shot a provincial chief over an alleged debt dispute as Thailand tightened school security after a mass shooting.",
        "source_zh": "海峡时报", "source_en": "The Straits Times",
        "url": "https://www.straitstimes.com/asia/se-asia/thai-official-hospitalised-after-shooting-at-government-office-and-suspect-detained-deputy-governor",
    },
    {
        "category": ("社会", "Society"),
        "zh_title": "文件显示南非特种部队或谋杀顶尖侦探",
        "en_title": "Documents Suggest South African Special Forces Murdered Top Detective",
        "published": "07:05 2026年8月10日",
        "zh_summary": "BBC获阅警方文件，指特种部队车辆曾跟踪遇害探员；12名军人被控，其中3人拒收押令仍在服役。",
        "en_summary": "BBC-reviewed police files link special forces to Lt Col Mathipa’s killing; 12 military members face charges, three still on duty.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cly8djwgem0o",
    },
    {
        "category": ("社会", "Society"),
        "zh_title": "加拿大BC省山火致2万人撤离，一名80岁女子遇难",
        "en_title": "Canada BC Wildfire Forces 20,000 to Evacuate, Killing One Elderly Woman",
        "published": "12:30 2026年8月10日",
        "zh_summary": "“秃岭”山火周末迅速扩大至逾1.3万公顷，萨默兰等地房屋损毁，省政府已宣布进入紧急状态。",
        "en_summary": "The Bald Range fire near Summerland exploded past 13,600 hectares, destroying homes and prompting a provincial state of emergency.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cx25dkwk3e3o",
    },
    {
        "category": ("社会", "Society"),
        "zh_title": "香港破纪录高温下仅发琥珀暑热警告引争议",
        "en_title": "Hong Kong Heat-Stress Alert Sparks Debate After Record Temperature",
        "published": "23:42 2026年8月9日",
        "zh_summary": "天文台录36.9°C历史新高，工会及气象专家呼吁检讨预警机制，并建议将中暑纳入工伤认定。",
        "en_summary": "A record 36.9°C reading left only an amber heat alert in force, prompting calls to review workplace heat protections.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363461/calls-system-review-after-lowest-alert-force-during-record-breaking-heat",
    },
    # 国际
    {
        "category": ("国际", "World"),
        "zh_title": "伊朗称霍尔木兹重开须美国满足赔偿等多项条件",
        "en_title": "Iran Ties Hormuz Reopening to U.S. Concessions Including Compensation",
        "published": "00:00 2026年8月10日",
        "zh_summary": "德黑兰称与阿曼航道协议接近完成，但海峡全面开放取决于美方解除封锁、制裁及支付战争赔偿。",
        "en_summary": "Tehran said an Oman lane deal is near, but full reopening requires U.S. compensation, sanctions relief and an end to threats.",
        "source_zh": "路透社", "source_en": "Reuters",
        "url": "https://www.internazionale.it/ultime-notizie-reuters/2026/08/10/iran-ties-hormuz-reopening-to-us-concessions-on-several-demands",
    },
    {
        "category": ("国际", "World"),
        "zh_title": "内塔尼亚胡正式拒绝特朗普15点加沙和平计划",
        "en_title": "Netanyahu Formally Rejects Trump’s 15-Point Gaza Peace Plan",
        "published": "00:00 2026年8月9日",
        "zh_summary": "以总理称不接受该文件，以军将在哈马斯真正解除武装前不撤离；美方特使仍呼吁给进程一次机会。",
        "en_summary": "Netanyahu rejected the document and vowed no withdrawal until Hamas is genuinely disarmed, despite U.S. envoy appeals for patience.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c5yw4lpe0yeo",
    },
    {
        "category": ("国际", "World"),
        "zh_title": "乌克兰无人机袭击鞑靼斯坦致至少13人死亡",
        "en_title": "Ukrainian Drone Strike Kills at Least 13 in Russia’s Tatarstan",
        "published": "16:51 2026年8月10日",
        "zh_summary": "袭击持续数小时，目标城市距乌边境超1100公里；俄方称39人受伤，鞑靼斯坦已宣布哀悼。",
        "en_summary": "An overnight strike on Nizhnekamsk killed 13 including a child and wounded 39 in one of Russia’s deadliest single attacks.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cvgjvgv926po",
    },
    {
        "category": ("国际", "World"),
        "zh_title": "涉嫌黑帮头目金·哈南从阿联酋引渡至爱尔兰受审",
        "en_title": "Suspected Crime Boss Daniel Kinahan Extradited from UAE to Ireland",
        "published": "00:00 2026年8月9日",
        "zh_summary": "金·哈南周日抵达都柏林后被控领导犯罪组织，特别刑事法庭将其羁押至10月5日再次开庭。",
        "en_summary": "Kinahan arrived in Dublin on Sunday, was charged with directing a criminal organisation and remanded until an October hearing.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c62qd5plzp6o",
    },
    {
        "category": ("国际", "World"),
        "zh_title": "缅甸政府拒绝东盟无条件释放昂山素季呼吁",
        "en_title": "Myanmar Rejects ASEAN Call to Free Aung San Suu Kyi Unconditionally",
        "published": "00:00 2026年8月10日",
        "zh_summary": "军政府称释放须依法进行，并质疑2027年后是否仍需东盟缅甸问题特使；红十字会上周首次探视素季。",
        "en_summary": "The junta said any release must follow law and questioned future envoy needs, after the Red Cross visited Suu Kyi last week.",
        "source_zh": "美联社", "source_en": "AP",
        "url": "https://www.wral.com/news/ap/b7431-myanmar-rebuffs-asean-call-to-free-aung-san-suu-kyi-questions-need-for-envoy/",
    },
    # 香港
    {
        "category": ("香港本地", "Hong Kong"),
        "zh_title": "香港47人案11名被告获准向终审法院上诉",
        "en_title": "Hong Kong Court Allows 11 Jailed Democrats to Appeal to Top Court",
        "published": "13:04 2026年8月10日",
        "zh_summary": "上诉庭认定五项法律问题具重大普遍意义，涉及“其他非法手段”定义及立法会职权边界。",
        "en_summary": "The Court of Appeal certified five legal issues of great importance on subversion charges tied to the 2020 primary.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363492/court-approves-last-attempt-11-jailed-opposition-figures-clear-their-name",
    },
    {
        "category": ("香港本地", "Hong Kong"),
        "zh_title": "港警破获“糖宝”约会诈骗案，8人涉款620万港元",
        "en_title": "Hong Kong Police Arrest Eight in HK$6.2 Million Dating Scam",
        "published": "14:08 2026年8月10日",
        "zh_summary": "团伙以包养合同为名收取所谓律师费，受害者含教师及医护人员，警方2至7月接报80宗相关案件。",
        "en_summary": "Fraudsters posing as lawyers charged bogus fees in compensated-dating scams, netting HK$6.2 million across 80 cases.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363500/hong-kong-police-arrest-8-over-hk62-million-sugar-baby-dating-scam",
    },
    {
        "category": ("香港本地", "Hong Kong"),
        "zh_title": "酷热天气将持续，本周末或有雷雨降温",
        "en_title": "Hong Kong Heatwave to Persist Before Showers Bring Relief",
        "published": "11:50 2026年8月10日",
        "zh_summary": "天文台指“白海豚”外围下沉气流致极端高温，部分区域气温或达37°C，周三后或有雷雨缓解。",
        "en_summary": "The Observatory said Dolphin’s subsiding air keeps extreme heat, with some areas near 37°C before showers later this week.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3363483/hong-kong-heatwave-persist-showers-bring-relief-later-week",
    },
    {
        "category": ("香港本地", "Hong Kong"),
        "zh_title": "颠覆政权案11名被告获批上诉终审法院证明书",
        "en_title": "Appeal Court Grants Certificates for 11 NSL Defendants to Appeal",
        "published": "12:29 2026年8月10日",
        "zh_summary": "港台报道，上诉庭就国安法下“其他非法手段”等五个法律问题批准证明书，全部被告今早出庭。",
        "en_summary": "RTHK said the Court of Appeal issued certificates on five legal questions, including the meaning of unlawful means under the NSL.",
        "source_zh": "香港电台", "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1865626-20260810.htm",
    },
    # 其他
    {
        "category": ("其他", "Other"),
        "zh_title": "民主党调查美军家属遭移民执法拘留事件",
        "en_title": "Democrats Probe Deportation Efforts Against U.S. Military Families",
        "published": "00:00 2026年8月10日",
        "zh_summary": "逾60名议员致函多部门，要求说明逾50名现役军人配偶或父母被拘留是否影响战备与士气。",
        "en_summary": "More than 60 lawmakers demanded answers after AP found over 50 troops’ spouses or parents detained by immigration authorities.",
        "source_zh": "美联社", "source_en": "AP",
        "url": "https://apnews.com/article/immigration-military-families-deport-trump-democrats-86087b0394dc8fe01cfec877903d266b",
    },
    {
        "category": ("其他", "Other"),
        "zh_title": "美加西部山火持续，犹他州两名灭火飞行员遇难",
        "en_title": "Western U.S. and Canada Wildfires Persist as Two Pilots Die in Utah",
        "published": "10:47 2026年8月10日",
        "zh_summary": "华盛顿州三起山火已损毁约920座建筑；加拿大BC省逾2万人撤离，省政府宣布紧急状态。",
        "en_summary": "Fires near Spokane damaged about 920 structures while over 20,000 fled BC blazes and two Utah firefighting pilots were killed.",
        "source_zh": "美联社", "source_en": "AP",
        "url": "https://apnews.com/article/western-wildfires-canada-us-946f5599db59517cb88fd3f0df9f5c46",
    },
]

SOURCE_COLORS = {
    "新华社": "#c41e3a", "Xinhua": "#c41e3a",
    "英国广播公司": "#bb1919", "BBC": "#bb1919",
    "路透社": "#ff8000", "Reuters": "#ff8000",
    "彭博社": "#2800d7", "Bloomberg": "#2800d7",
    "美联社": "#ff0000", "AP": "#ff0000",
    "南华早报": "#001f3f", "SCMP": "#001f3f",
    "香港电台": "#006633", "RTHK": "#006633",
    "星报": "#e74c3c", "The Star": "#e74c3c",
    "海峡时报": "#003366", "The Straits Times": "#003366",
    "Whalesbook": "#2c3e50",
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_html():
    n = len(ITEMS)
    cat_order = [
        ("国内 / 内地", "China Mainland"),
        ("科技 / 互联网", "Technology"),
        ("财经 / 商业", "Finance & Business"),
        ("社会", "Society"),
        ("国际", "World"),
        ("香港本地", "Hong Kong"),
        ("其他", "Other"),
    ]
    grouped = {c[0]: [] for c in cat_order}
    for it in ITEMS:
        grouped[it["category"][0]].append(it)

    cat_html = []
    num = 1
    for cat_zh, cat_en in cat_order:
        items = grouped[cat_zh]
        if not items:
            continue
        cat_html.append(
            f'<h2 style="margin:28px 0 14px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #1a73e8;font-size:17px;color:#222;">{esc(cat_zh)}<br><span style="font-size:13px;color:#666;font-weight:normal;">{esc(cat_en)}</span></h2>'
        )
        for it in items:
            color = SOURCE_COLORS.get(it["source_zh"], "#555")
            cat_html.append(
                f'<div style="margin:0 0 22px;padding:0 0 18px;border-bottom:1px solid #eee;">'
                f'<div style="font-size:12px;color:#1a73e8;font-weight:bold;margin-bottom:6px;">{num:02d}</div>'
                f'<div style="font-size:16px;font-weight:bold;margin-bottom:4px;"><a href="{esc(it["url"])}" style="color:#1a1a1a;text-decoration:none;">{esc(it["zh_title"])}</a></div>'
                f'<div style="font-size:14px;color:#555;font-style:italic;margin-bottom:4px;">{esc(it["en_title"])}</div>'
                f'<div style="font-size:12px;color:#888;margin-bottom:8px;">发布时间 Published: {esc(it["published"])}</div>'
                f'<div style="font-size:14px;color:#333;line-height:1.6;margin-bottom:4px;">{esc(it["zh_summary"])}</div>'
                f'<div style="font-size:13px;color:#666;line-height:1.5;margin-bottom:8px;">{esc(it["en_summary"])}</div>'
                f'<span style="display:inline-block;padding:2px 8px;background:{color};color:#fff;font-size:11px;border-radius:3px;margin-right:8px;">{esc(it["source_zh"])} / {esc(it["source_en"])}</span>'
                f'<a href="{esc(it["url"])}" style="font-size:12px;color:#1a73e8;text-decoration:none;">查看全文 Read more →</a>'
                f'</div>'
            )
            num += 1

    body = "\n".join(cat_html)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{esc(SUBJECT)}</title></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:#1a1a2e;color:#fff;padding:28px 24px;text-align:center;">
<div style="font-size:24px;font-weight:bold;margin-bottom:6px;">每日热点晚报</div>
<div style="font-size:14px;opacity:0.9;">Evening News Briefing · {DATE_CN} · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;font-size:14px;color:#444;line-height:1.7;border-bottom:1px solid #eee;">
<div>汇总今日全日要闻，涵盖国内、国际、财经、科技及港台热点。</div>
<div style="margin-top:6px;color:#666;font-style:italic;">Today's main stories across China, world affairs, markets, technology and regional highlights.</div>
</td></tr>
<tr><td style="padding:8px 24px 24px;">{body}</td></tr>
<tr><td style="padding:20px 24px;background:#f9f9f9;font-size:11px;color:#999;line-height:1.6;border-top:1px solid #eee;">
<div>本简报由自动化系统编发，内容摘自公开报道，仅供参考，不构成投资或法律建议。</div>
<div style="margin-top:4px;">This briefing is automatically compiled from public reports for informational purposes only; it is not investment or legal advice.</div>
</td></tr>
</table></td></tr></table>
</body></html>"""


def main():
    html = build_html()
    payload = {"subject": SUBJECT, "htmlContent": html, "recipients": RECIPIENTS}
    root = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(root, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total items: {len(ITEMS)}")
    print(f"HTML length: {len(html)}")
    from collections import Counter
    cat_counts = Counter(it["category"][0].split(" / ")[0] for it in ITEMS)
    print("Category counts:", dict(cat_counts))
    src_counts = Counter(it["source_en"] for it in ITEMS)
    print("Source counts:", dict(src_counts))


if __name__ == "__main__":
    main()
