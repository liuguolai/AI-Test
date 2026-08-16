#!/usr/bin/env python3
"""Build evening briefing HTML and email_payload.json for 2026-08-16."""
import json
import os

ITEMS = [
    # 国内 China Mainland
    {
        "cat_cn": "国内",
        "cat_en": "China Mainland",
        "title_cn": "北京与马尼拉就逮捕「非法」务工者交锋，双边紧张升温",
        "title_en": "Beijing and Manila clash over arrests of 'illegal' workers as tensions worsen",
        "time": "16:00 2026年8月16日",
        "summary_cn": "菲律宾逮捕中资钢厂无证华工引发外交争执，马尼拉驳斥中方批评防长干预执法。",
        "summary_en": "Manila rejects Beijing's criticism over arrests of Chinese workers at a steel plant as diplomatic friction spills beyond the South China Sea.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/china/diplomacy/article/3364178/beijing-and-manila-clash-over-arrests-illegal-workers-tensions-worsen",
    },
    {
        "cat_cn": "国内",
        "cat_en": "China Mainland",
        "title_cn": "中国新一轮扫黑除恶启动，律师担忧冤案与酷刑风险",
        "title_en": "As China launches new gang crackdown, lawyers fear wrongful convictions",
        "time": "10:00 2026年8月16日",
        "summary_cn": "律师称地方为完成指标或将普通案件定性为涉黑，甚至出现刑讯逼供等违法做法。",
        "summary_en": "Lawyers warn officials meeting quotas may label ordinary crimes as gang-related and resort to torture.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/china/politics/article/3364158/china-launches-new-gang-crackdown-lawyers-fear-wrongful-convictions",
    },
    {
        "cat_cn": "国内",
        "cat_en": "China Mainland",
        "title_cn": "全国生态日：我国首部生态环境法典正式施行",
        "title_en": "China's first ecological environment code takes effect on National Ecology Day",
        "time": "08:22 2026年8月16日",
        "summary_cn": "8月15日起施行的法典系民法典后第二部「法典」命名法律，夯实生态环境法治根基。",
        "summary_en": "The code, effective August 15, is China's second law named a 'code' after the Civil Code, strengthening environmental rule of law.",
        "source_cn": "中国金融信息网",
        "source_en": "CNFin",
        "source_color": "#1a5276",
        "url": "https://m.cnfin.com/yw-lb/zixun/20260816/4455719_1.html",
    },
    {
        "cat_cn": "国内",
        "cat_en": "China Mainland",
        "title_cn": "全国碳市场将扩围至石化化工，覆盖八成二氧化碳排放",
        "title_en": "China to add petrochemicals and chemicals to national carbon market",
        "time": "01:34 2026年8月15日",
        "summary_cn": "生态环境部称两大行业纳入后，全国碳市场监管范围将覆盖约八成二氧化碳排放。",
        "summary_en": "Adding the two sectors would bring about 80% of China's CO2 emissions under the world's largest emissions trading program.",
        "source_cn": "财新",
        "source_en": "Caixin Global",
        "source_color": "#b8860b",
        "url": "https://www.caixinglobal.com/2026-08-15/china-to-add-petrochemicals-chemicals-to-national-carbon-market-102474336.html",
    },
    # 科技 Technology
    {
        "cat_cn": "科技",
        "cat_en": "Technology",
        "title_cn": "记者实测微信「小微」AI 代理24小时：亮点与失误并存",
        "title_en": "24 hours with Tencent's WeChat AI agent: successes and stumbles",
        "time": "16:00 2026年8月16日",
        "summary_cn": "腾讯在财报中首次推介小微代理，记者试用发现其可代订餐预约，但仍有操作失误。",
        "summary_en": "Tencent's Xiaowei agent promises hands-free control across WeChat; early trials show promise and occasional frustration.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/tech/big-tech/article/3364068/i-gave-tencents-wechat-ai-agent-control-24-hours-where-it-excelled-and-stumbled",
    },
    {
        "cat_cn": "科技",
        "cat_en": "Technology",
        "title_cn": "中国研发「电鳗」传感器，机器人无需触碰即可感知物体",
        "title_en": "China's 'electric eel' sensor allows robots to feel objects without touching them",
        "time": "12:00 2026年8月16日",
        "summary_cn": "西电团队模仿电鳗电场感知，氟聚合物涂层传感器可识别金属、塑料、玻璃和木材。",
        "summary_en": "Xidian University researchers mimic eel electric fields so robots can sense metal, plastics, glass and wood before contact.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/china/science/article/3364015/chinas-electric-eel-sensor-allows-robots-feel-object-without-touching-it",
    },
    {
        "cat_cn": "科技",
        "cat_en": "Technology",
        "title_cn": "大疆与影石争食全景相机市场，360影像赛道竞争升温",
        "title_en": "China's DJI and Arashi Vision escalate battle for 360 camera market",
        "time": "23:29 2026年8月14日",
        "summary_cn": "两家中国厂商在消费级全景相机领域正面交锋，争夺欧美及亚洲年轻用户市场。",
        "summary_en": "DJI and Arashi Vision are competing head-on in the consumer 360-degree camera segment across global markets.",
        "source_cn": "财新",
        "source_en": "Caixin Global",
        "source_color": "#b8860b",
        "url": "https://www.caixinglobal.com/2026-08-14/chinas-dji-and-arashi-vision-escalate-battle-for-360-camera-market-102474326.html",
    },
    {
        "cat_cn": "科技",
        "cat_en": "Technology",
        "title_cn": "中国金融业改革提速，670家农村银行被合并裁撤",
        "title_en": "China cuts 670 rural banks as financial sector overhaul accelerates",
        "time": "01:16 2026年8月15日",
        "summary_cn": "监管推动中小银行整合重组，年内已有数百家农村金融机构退出或并入更大机构。",
        "summary_en": "Regulators are consolidating rural lenders as part of an accelerating overhaul of China's banking sector.",
        "source_cn": "财新",
        "source_en": "Caixin Global",
        "source_color": "#b8860b",
        "url": "https://www.caixinglobal.com/2026-08-15/china-cuts-670-rural-banks-as-financial-sector-overhaul-accelerates-102474334.html",
    },
    # 财经 Finance & Business
    {
        "cat_cn": "财经",
        "cat_en": "Finance & Business",
        "title_cn": "陈茂波：美国贸易政策转向对港影响「主要是心理层面」",
        "title_en": "Impact of US trade policy shifts on Hong Kong 'primarily psychological': Paul Chan",
        "time": "13:49 2026年8月16日",
        "summary_cn": "财政司长称美贸易与利率变化或冲击市场，但上半年访港旅客增12%，增长动能有望延续。",
        "summary_en": "Finance chief cites US trade and rate trends as risks but expects growth momentum to continue after strong first-half exports.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3364173/impact-us-trade-policy-shifts-hong-kong-primarily-psychological-paul-chan",
    },
    {
        "cat_cn": "财经",
        "cat_en": "Finance & Business",
        "title_cn": "美国调走亚太最后一艘航母，聚焦伊朗与西半球",
        "title_en": "US pulls last aircraft carrier in Asia as Trump focuses on Iran and the Western Hemisphere",
        "time": "20:37 2026年8月15日",
        "summary_cn": "华盛顿号将赴中东接替林肯号，西太平洋暂无美航母，盟友担忧美国战略重心偏移。",
        "summary_en": "USS George Washington departs the Pacific for the Middle East, leaving the western Pacific without a US carrier as Iran operations stretch the fleet.",
        "source_cn": "美联社",
        "source_en": "AP",
        "source_color": "#2c5282",
        "url": "https://apnews.com/article/aircraft-carriers-trump-china-pacific-iran-war-87cfb838de8c13464fa3cab1840ad87d",
    },
    {
        "cat_cn": "财经",
        "cat_en": "Finance & Business",
        "title_cn": "厄瓜多尔总统诺沃阿8月16日起访华，深化对华经贸合作",
        "title_en": "Ecuadorian President Noboa to visit China from Aug. 16 to strengthen ties",
        "time": "23:58 2026年8月14日",
        "summary_cn": "此访系诺沃阿首次对华国事访问，将谈贸易投资，今年恰逢中厄全面战略伙伴关系十周年。",
        "summary_en": "Daniel Noboa's state visit from August 16 marks the 10th anniversary of China-Ecuador comprehensive strategic partnership.",
        "source_cn": "财新",
        "source_en": "Caixin Global",
        "source_color": "#b8860b",
        "url": "https://www.caixinglobal.com/2026-08-14/the-week-ahead-aug-17-23-us-imposes-tariffs-on-canadian-goods-102474328.html",
    },
    {
        "cat_cn": "财经",
        "cat_en": "Finance & Business",
        "title_cn": "7月新增银行贷款意外负增长3400亿元，需求疲弱",
        "title_en": "China's new bank loans shrink in July as borrowing demand stays weak",
        "time": "01:05 2026年8月15日",
        "summary_cn": "7月新增人民币贷款净减少3400亿元，居民与企业均去杠杆，债券融资成社融主力。",
        "summary_en": "New yuan loans contracted by 340 billion yuan in July as households and firms reduced debt despite bond-driven credit growth.",
        "source_cn": "财新",
        "source_en": "Caixin Global",
        "source_color": "#b8860b",
        "url": "https://www.caixinglobal.com/2026-08-15/chinas-new-bank-loans-shrink-in-july-as-borrowing-demand-stays-weak-102474332.html",
    },
    # 社会 Society
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "title_cn": "法国宪法委员会否决15岁以下社媒禁令，指过度限制言论自由",
        "title_en": "France's constitutional council rules under-16 social media ban unconstitutional",
        "time": "11:46 2026年8月16日",
        "summary_cn": "委员会认为全面禁止未成年人使用社交媒体构成对表达自由不成比例的限制。",
        "summary_en": "The council said a broad ban on under-15s using social media imposed a disproportionate restriction on free expression.",
        "source_cn": "财新",
        "source_en": "Caixin",
        "source_color": "#b8860b",
        "url": "https://international.caixin.com/2026-08-16/102474636.html",
    },
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "title_cn": "调查：香港劏房住户室内最高体感温度达52度",
        "title_en": "Survey finds substandard housing tenants face extreme indoor heat in Hong Kong",
        "time": "13:11 2026年8月16日",
        "summary_cn": "团体监测78户不适切住房，74%受访者出现中暑症状，七成夜间难以入睡。",
        "summary_en": "A survey of 78 inadequate housing units found indoor 'feels-like' temperatures reaching 52°C and widespread heat exhaustion symptoms.",
        "source_cn": "香港电台",
        "source_en": "RTHK",
        "source_color": "#6b2d5c",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866332-20260816.htm",
    },
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "title_cn": "美国政坛女性谈事业与家庭平衡，引发公众热议",
        "title_en": "US women in politics spark conversation about balancing family and career",
        "time": "07:01 2026年8月16日",
        "summary_cn": "莱维特与奥卡西奥-科尔特斯等女性政治人物的经历，折射高压职业与育儿的时间冲突。",
        "summary_en": "Working mothers in US politics discuss the challenges of high-pressure careers and making time for family.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/cjwxgz95jvgo",
    },
    {
        "cat_cn": "社会",
        "cat_en": "Society",
        "title_cn": "西岸定居者暴力持续，以色列为何难以有效约束？",
        "title_en": "Why Israel has done little to rein in West Bank settler violence",
        "time": "12:00 2026年8月15日",
        "summary_cn": "库斯拉村民被迫困守家中，美方斥定居者为「恐怖分子」，但军事与政治结构仍纵容扩张。",
        "summary_en": "Palestinians in Qusra remain besieged as US envoy calls settlers 'terrorists' but Israeli policy still backs settlement growth.",
        "source_cn": "美联社",
        "source_en": "AP",
        "source_color": "#2c5282",
        "url": "https://apnews.com/article/israel-palestinians-settler-violence-us-siege-west-bank-bd4ae76cec1773c1c09233cc0b33a378",
    },
    # 国际 World
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "title_cn": "俄军无人机导弹袭击乌克兰多地，至少五人遇难",
        "title_en": "Five killed as Russia launches drone and missile attack on Ukraine",
        "time": "16:14 2026年8月16日",
        "summary_cn": "基辅、克里维里赫等地遭袭，泽连斯基指俄打击民用设施；乌方亦向莫斯科发射约600架无人机。",
        "summary_en": "Russian strikes killed at least five across Ukraine while Kyiv launched hundreds of drones toward Moscow, hitting a Wildberries warehouse.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/c1411pgje8xo",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "title_cn": "乌克兰发动战争以来最大规模空袭，俄境内至少六人死亡",
        "title_en": "Ukraine launches one of its largest aerial attacks of the war, killing at least 6 in Russia",
        "time": "15:42 2026年8月16日",
        "summary_cn": "俄国防部称摧毁822架无人机，莫斯科州仓库起火；罗斯托夫等地亦遭袭致5人丧生。",
        "summary_en": "Russia said it destroyed 822 Ukrainian drones overnight as strikes killed six people and ignited a Wildberries warehouse near Moscow.",
        "source_cn": "美联社",
        "source_en": "AP",
        "source_color": "#2c5282",
        "url": "https://apnews.com/article/russia-ukraine-war-01294bf8744282086e8f76c8130e16ba",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "title_cn": "印尼弗洛勒斯7.7级地震遇难人数升至51人，五千人疏散",
        "title_en": "Rescuers dig through rubble after Indonesia quake kills 51",
        "time": "10:48 2026年8月16日",
        "summary_cn": "救援队周日再发现四具遗体，逾900栋房屋损毁，山体滑坡阻断道路阻碍搜救。",
        "summary_en": "Rescue teams recovered four more bodies Sunday after a magnitude-7.7 quake displaced about 5,000 people on Flores island.",
        "source_cn": "美联社",
        "source_en": "AP",
        "source_color": "#2c5282",
        "url": "https://apnews.com/article/indonesia-flores-earthquake-landslide-bf1d024bdec7727094f8dc73d7dd5e34",
    },
    {
        "cat_cn": "国际",
        "cat_en": "World",
        "title_cn": "匈牙利高速公路旅游大巴翻车，12名波兰游客遇难",
        "title_en": "Twelve killed as Polish tourist bus veers off Hungarian motorway",
        "time": "15:04 2026年8月16日",
        "summary_cn": "载57名乘客的大巴凌晨偏离M3高速翻入沟中，警方怀疑司机疲劳驾驶并已拘留。",
        "summary_en": "A Polish tourist bus overturned into a ditch on the M3 motorway early Sunday; police believe the driver fell asleep.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/ckg4424zd7go",
    },
    # 香港本地 Hong Kong
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "title_cn": "酷热天气持续至周一，本港周三前后或有雷暴",
        "title_en": "Heatwave to persist in Hong Kong before thunderstorms set in midweek",
        "time": "12:35 2026年8月16日",
        "summary_cn": "酷热天气警告生效，周日周一最高气温或达35度，低压系统将为华南带来骤雨雷暴。",
        "summary_en": "The very hot weather warning remains in force with highs near 35°C before a low-pressure trough brings squally thunderstorms midweek.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/hong-kong/article/3364168/heatwave-persist-hong-kong-thunderstorms-set-midweek",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "title_cn": "陈茂波对下半年经济审慎乐观，称外部风险可控",
        "title_en": "FS cautiously optimistic in H2 despite global risks",
        "time": "11:20 2026年8月16日",
        "summary_cn": "财政司长指上半年出口强劲、零售连增14个月，美贸易与利率变动影响主要是心理层面。",
        "summary_en": "Paul Chan cited strong exports and 14 months of retail growth while saying US trade risks are manageable.",
        "source_cn": "香港电台",
        "source_en": "RTHK",
        "source_color": "#6b2d5c",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866330-20260816.htm",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "title_cn": "陈茂波：上半年机场客运增11.7%，国际航空枢纽地位稳固",
        "title_en": "Paul Chan reaffirms Hong Kong airport hub strength",
        "time": "13:14 2026年8月16日",
        "summary_cn": "财政司长博客称上半年飞机起降逾20万次，访港旅客3122万人次，三跑道系统提升运力。",
        "summary_en": "Paul Chan cited 32.8 million airport passengers in the first half and major infrastructure upgrades cementing Hong Kong's hub status.",
        "source_cn": "香港电台",
        "source_en": "RTHK",
        "source_color": "#6b2d5c",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866334-20260816.htm",
    },
    {
        "cat_cn": "香港本地",
        "cat_en": "Hong Kong",
        "title_cn": "皇岗口岸首次反恐演习，约5000名公务员参与客流测试",
        "title_en": "Hong Kong stages first counterterrorism drill at redeveloped Huanggang crossing",
        "time": "20:53 2026年8月15日",
        "summary_cn": "保安局在重建后的皇岗口岸举行首次反恐演练，测试突发客流与车辆通关应急安排。",
        "summary_en": "About 5,000 civil servants joined Hong Kong's first counterterrorism drill at the revamped Huanggang border crossing on Saturday.",
        "source_cn": "南华早报",
        "source_en": "SCMP",
        "source_color": "#c41e3a",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3364154/hong-kong-stages-first-counterterrorism-drill-redeveloped-huanggang-crossing",
    },
    # 其他 Other
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "title_cn": "飓风「拉拉」擦过大岛未登陆，夏威夷仍遭狂风暴雨袭击",
        "title_en": "Hurricane Lala skirts Hawaii's Big Island without making landfall",
        "time": "20:55 2026年8月15日",
        "summary_cn": "风暴眼掠过岛屿南端，至少一人车祸身亡，逾6万户断电，高海拔或降63厘米暴雨。",
        "summary_en": "Lala lashed Hawaii with hurricane-force winds and flooding; at least one person died and tens of thousands lost power.",
        "source_cn": "美联社",
        "source_en": "AP",
        "source_color": "#2c5282",
        "url": "https://apnews.com/article/hawaii-tropical-storm-lala-hurricane-0c3d63c8a87943cdf8d57c530a7ed9d0",
    },
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "title_cn": "摩洛哥拦截逾百名试图进入休达口岸的移民",
        "title_en": "Morocco detains dozens of migrants trying to cross into Ceuta",
        "time": "03:16 2026年8月16日",
        "summary_cn": "休达上月曾涌入约7.8万移民，当局加强边境管控，周六在附近城镇拘留111人。",
        "summary_en": "Moroccan security detained 111 people near Fnideq amid heightened patrols after last month's mass influx into the Spanish exclave.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/ckg44x2ey1ro",
    },
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "title_cn": "卡塔尔否认俘获三名伊朗飞行员，称伊朗歪曲事实",
        "title_en": "Qatar denies capturing three Iranian pilots after downing fighter jets",
        "time": "05:03 2026年8月16日",
        "summary_cn": "伊朗称三名飞行员在3月袭击卡塔尔基地后被俘，卡塔尔称已联系飞行员但未获回应。",
        "summary_en": "Iran claims three pilots were captured after jets were downed in March; Qatar says it contacted the pilots but received no response.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/cj4kk8kz271o",
    },
    {
        "cat_cn": "其他",
        "cat_en": "Other",
        "title_cn": "列支敦士登修改王位继承法，允许女性继承君位",
        "title_en": "Liechtenstein changes succession rule to allow women to ascend the throne",
        "time": "03:41 2026年8月16日",
        "summary_cn": "公国在国家日宣布改为长子长女均可继承，新规适用于王储夫妇四子女的后代。",
        "summary_en": "Liechtenstein switched from male primogeniture to absolute primogeniture on its national day, applying to the hereditary prince's descendants.",
        "source_cn": "英国广播公司",
        "source_en": "BBC",
        "source_color": "#bb1919",
        "url": "https://www.bbc.co.uk/news/articles/cn9nnxrxg4qo",
    },
]


def build_html():
    n = len(ITEMS)
    cats_order = []
    cat_items = {}
    for item in ITEMS:
        key = (item["cat_cn"], item["cat_en"])
        if key not in cat_items:
            cats_order.append(key)
            cat_items[key] = []
        cat_items[key].append(item)

    body_parts = []
    idx = 1
    for cat_cn, cat_en in cats_order:
        body_parts.append(
            f'<div style="margin:24px 0 12px;padding:10px 14px;background:#f0f4f8;border-left:4px solid #2563eb;">'
            f'<h2 style="margin:0;font-size:17px;color:#1e293b;">{cat_cn} <span style="font-weight:normal;color:#64748b;">/ {cat_en}</span></h2></div>'
        )
        for item in cat_items[(cat_cn, cat_en)]:
            num = f"{idx:02d}"
            body_parts.append(
                f'<div style="margin:0 0 20px;padding:16px;border-bottom:1px solid #e2e8f0;">'
                f'<div style="font-size:13px;color:#2563eb;font-weight:bold;margin-bottom:6px;">{num}</div>'
                f'<a href="{item["url"]}" style="font-size:16px;color:#1e293b;text-decoration:none;font-weight:600;line-height:1.4;">{item["title_cn"]}</a>'
                f'<div style="font-size:14px;color:#475569;font-style:italic;margin-top:4px;line-height:1.4;">{item["title_en"]}</div>'
                f'<div style="font-size:12px;color:#94a3b8;margin-top:6px;">发布时间 Published: {item["time"]}</div>'
                f'<p style="margin:10px 0 4px;font-size:14px;color:#334155;line-height:1.6;">{item["summary_cn"]}</p>'
                f'<p style="margin:0 0 10px;font-size:13px;color:#64748b;line-height:1.5;">{item["summary_en"]}</p>'
                f'<span style="display:inline-block;padding:2px 8px;background:{item["source_color"]};color:#fff;font-size:11px;border-radius:3px;margin-right:8px;">{item["source_cn"]} / {item["source_en"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#2563eb;">查看全文 Read more →</a>'
                f'</div>'
            )
            idx += 1

    html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>每日热点晚报 Evening Briefing 2026-08-16</title></head>'
        '<body style="margin:0;padding:0;background:#f1f5f9;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">'
        '<div style="max-width:600px;margin:0 auto;padding:16px;">'
        '<div style="background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">'
        '<div style="background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);padding:28px 24px;color:#fff;">'
        '<div style="font-size:22px;font-weight:700;margin-bottom:4px;">每日热点晚报</div>'
        '<div style="font-size:14px;opacity:0.9;">Evening News Briefing · 2026年8月16日 · 共' + str(n) + '条</div>'
        '</div>'
        '<div style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0;">'
        '<p style="margin:0 0 6px;font-size:14px;color:#334155;line-height:1.6;">汇总今日全日要闻，涵盖外交摩擦、科技突破、市场动态及全球突发事件。</p>'
        '<p style="margin:0;font-size:13px;color:#64748b;line-height:1.5;">Today\'s main stories: diplomacy, tech, markets and global developments across 28 curated items.</p>'
        '</div>'
        + "".join(body_parts)
        + '<div style="padding:20px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:11px;color:#94a3b8;line-height:1.6;">'
        '<p style="margin:0 0 6px;">本简报仅供参考，不构成投资建议。新闻版权归原媒体所有。</p>'
        '<p style="margin:0;">This briefing is for informational purposes only. Copyright belongs to original publishers.</p>'
        '</div></div></div></body></html>'
    )
    return html


def main():
    html = build_html()
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-16",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print(f"Written {out} ({len(html)} chars, {len(ITEMS)} items)")


if __name__ == "__main__":
    main()
