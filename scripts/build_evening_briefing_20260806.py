#!/usr/bin/env python3
"""Build evening briefing HTML and email_payload.json for 2026-08-06."""

import json
import os

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "cn_title": "我国科研人员首次确证「胶球」存在",
            "en_title": "Chinese scientists confirm existence of gluon-bound \"glueball\" particle",
            "published": "08:01 2026年8月6日",
            "cn_summary": "北京谱仪III实验组历经15年研究，测定X(2370)「味单态」性质，证实胶子可自我结合形成新物质形态。",
            "en_summary": "After 15 years, the BESIII team confirmed glueball nature of X(2370), validating a decades-old Standard Model prediction.",
            "source_cn": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/tech/20260806/3de18675c0e445c28baef017ffec0d65/c.html",
        },
        {
            "cn_title": "我国首座抗17级台风张力腿浮式风电平台投运",
            "en_title": "China commissions first 16MW tension-leg floating wind platform rated for Cat 5 typhoons",
            "published": "11:11 2026年8月6日",
            "cn_summary": "「海油安澜号」接入陆丰油田电网，离岸136公里水深136米，年供绿电5400万度并减碳3.5万吨。",
            "en_summary": "The Haiyou Anlan platform in the Pearl River Mouth Basin will supply 54 million kWh yearly and cut CO2 by 35,000 tonnes.",
            "source_cn": "新华社",
            "source_en": "Xinhua",
            "url": "http://www.ce.cn/xwzx/gnsz/gdxw/202608/t20260806_3131851.shtml",
        },
        {
            "cn_title": "内地税务机关开始对离岸保单收益征税",
            "en_title": "Mainland tax authorities begin levying income tax on offshore insurance returns",
            "published": "18:31 2026年8月5日",
            "cn_summary": "财新称北京、杭州等地已对香港保单分红及预缴保费利息按20%征收个税，CRS数据共享推动执法落地。",
            "en_summary": "Caixin reports 20% tax on HK policy dividends and prepaid-premium interest in Beijing and Hangzhou, aided by CRS data sharing.",
            "source_cn": "财新",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-05/exclusive-china-widens-tax-net-to-offshore-insurance-102471550.html",
        },
        {
            "cn_title": "离岸保单征税报道引发保诚、汇丰等股价大跌",
            "en_title": "Offshore insurance tax report triggers selloff in Prudential, HSBC shares",
            "published": "12:00 2026年8月6日",
            "cn_summary": "财新后续报道指伦敦上市保诚一度跌13%，汇丰跌近5%，市场担忧内地客户赴港投保吸引力下降。",
            "en_summary": "Follow-up Caixin coverage notes Prudential fell up to 13% and HSBC nearly 5% in London on offshore tax enforcement fears.",
            "source_cn": "财新",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-06/china-tax-on-offshore-insurance-returns-triggers-prudential-hsbc-selloff-102471711.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "cn_title": "Visa将支付网络嵌入ChatGPT，AI代理可代为购物付款",
            "en_title": "Visa embeds payment network in ChatGPT so AI agents can shop and pay",
            "published": "00:00 2026年8月6日",
            "cn_summary": "Visa与OpenAI合作，用户可绑定信用卡让ChatGPT在商户端完成交易，并设消费限额等风控护栏。",
            "en_summary": "Visa and OpenAI let users link cards so ChatGPT can complete purchases at merchants, with spending limits and approval steps.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/visa-chatgpt-openai-shopping-mastercard-d769dec86344cb4977c98789e8ec492f",
        },
        {
            "cn_title": "三星电子二季度营业利润创纪录，AI内存需求强劲",
            "en_title": "Samsung posts record Q2 operating profit as AI memory demand surges",
            "published": "00:00 2026年8月6日",
            "cn_summary": "4–6月营业利润89.5万亿韩元，收入171.5万亿韩元均创新高，半导体业务贡献绝大部分利润。",
            "en_summary": "Samsung reported record 89.5 trillion won operating profit and 171.5 trillion won revenue, driven almost entirely by chips.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/samsung-ai-profit-memory-chips-10c2c548a392988862d8c7bd3f6fae05",
        },
        {
            "cn_title": "AI热潮下韩股芯片股重挫，科斯达克指数跌4.6%",
            "en_title": "Kospi drops 4.6% as AI-linked chipmakers SK Hynix and Samsung slide",
            "published": "00:00 2026年8月6日",
            "cn_summary": "亚洲市场跟随华尔街科技股回调，SK海力士跌超10%，三星跌6.3%，投资者担忧AI估值与产能扩张回报。",
            "en_summary": "Asian markets tracked Wall Street tech losses; SK Hynix fell over 10% and Samsung 6.3% amid AI valuation concerns.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-ai-spacex-hynix-bonds-2f4f2638cb8430bb7c8e5d59a7b50731",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "cn_title": "港险股重挫，报道指内地对离岸保单收益征20%税",
            "en_title": "HK insurer shares plunge on reports of 20% mainland tax on offshore policy gains",
            "published": "09:59 2026年8月6日",
            "cn_summary": "友邦跌6.6%、保诚跌5.9%、汇丰跌4.1%，上海税务部门称对离岸保单收益按20%征税并可追溯至2019年。",
            "en_summary": "AIA, Prudential and HSBC fell sharply after reports mainland authorities tax offshore policy gains at 20%, retroactive to 2019.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/business/banking-finance/article/3363106/shares-major-hong-kong-insurance-finance-firms-tumble-following-report-20-levy",
        },
        {
            "cn_title": "《玩具总动员5》助力迪士尼三季度业绩超预期",
            "en_title": "Toy Story 5 powers Disney's strong third-quarter earnings beat",
            "published": "00:00 2026年8月5日",
            "cn_summary": "迪士尼收入252亿美元增7%，经调整每股收益2.06美元超预期，美国主题乐园客流与流媒体利润双双走强。",
            "en_summary": "Disney revenue rose 7% to $25.2B; adjusted EPS of $2.06 beat forecasts as parks and streaming profits strengthened.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/disney-economy-trump-parks-streaming-tiktok-d9d5482d48307f7104c677fa4b059a01",
        },
        {
            "cn_title": "港股随区域科技股走低，恒指早盘跌近2%",
            "en_title": "Hang Seng falls nearly 2% as regional markets track tech retreat",
            "published": "11:08 2026年8月6日",
            "cn_summary": "RTHK报道恒指一度跌467点，日韩芯片股领跌，投资者评估霍尔木兹通航谈判与周五美国非农就业数据。",
            "en_summary": "RTHK says the Hang Seng fell as much as 467 points as chip stocks led regional losses ahead of US jobs data.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865187-20260806.htm",
        },
        {
            "cn_title": "离岸保单征税消息拖累港险股，友邦一度跌逾8%",
            "en_title": "Reported offshore insurance tax hits HK-listed insurers; AIA drops over 8%",
            "published": "11:31 2026年8月6日",
            "cn_summary": "路透社引述财新称北京、杭州已征税，友邦、保诚、富卫早盘大跌，拖累恒指逾2%。",
            "en_summary": "Reuters cites Caixin on Beijing and Hangzhou enforcement; AIA, Prudential and FWD plunged, dragging the Hang Seng down over 2%.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865191-20260806.htm",
        },
    ]),
    ("社会 Society", [
        {
            "cn_title": "联合国专家支持将 Tate 兄弟引渡回英国受审",
            "en_title": "UN expert backs extraditing Tate brothers to UK on rape and trafficking charges",
            "published": "00:00 2026年8月5日",
            "cn_summary": "联合国暴力侵害妇女问题特别报告员称引渡程序是追究59项指控的重要一步，呼吁三国确保其面对司法。",
            "en_summary": "The UN rapporteur on violence against women welcomed US extradition moves over 59 UK charges including rape and trafficking.",
            "source_cn": "联合国新闻",
            "source_en": "UN News",
            "url": "https://news.un.org/en/story/2026/08/1168085",
        },
        {
            "cn_title": "尼日利亚安全部队解救308名被绑架者",
            "en_title": "Nigerian forces rescue 308 abductees from Kainji Lake National Park",
            "published": "13:30 2026年8月6日",
            "cn_summary": "总统府称这是单日最大规模解救行动，受害者包括夸拉州沃罗村及尼日尔州遭绑架民众，正接受医疗救治。",
            "en_summary": "Nigeria's presidency called it the largest single-day rescue; victims from Kwara and Niger states are receiving medical care.",
            "source_cn": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cn4ndd8nr8lo",
        },
        {
            "cn_title": "广岛举行原爆81周年纪念，市长批评拥核正当化",
            "en_title": "Hiroshima marks 81st atomic bombing anniversary; mayor condemns nuclear deterrence",
            "published": "12:21 2026年8月6日",
            "cn_summary": "约5万人出席和平仪式，市长称政治领袖仍将核威慑视为现实手段，使无核世界目标更加遥远。",
            "en_summary": "About 50,000 attended the ceremony; the mayor warned leaders legitimizing nuclear deterrence push a nuclear-free world further away.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865196-20260806.htm",
        },
        {
            "cn_title": "港母亲虐死5岁儿子被判囚22年",
            "en_title": "Hong Kong mother jailed 22 years for starving five-year-old son to death",
            "published": "19:13 2026年8月5日",
            "cn_summary": "高等法院指被告长期虐待隔离儿子，男童死时仅重9.7公斤并有129处伤痕，属最严重虐儿案件。",
            "en_summary": "The High Court jailed a mother for starving her son, who weighed 9.7kg with 129 injuries at death in September 2022.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363069/savage-abuse-hong-kong-mother-gets-22-years-starving-boy-5-death",
        },
    ]),
    ("国际 World", [
        {
            "cn_title": "伊朗称与阿曼霍尔木兹通航协议进入最后起草阶段",
            "en_title": "Iran says Hormuz shipping deal with Oman in final drafting stage",
            "published": "09:10 2026年8月6日",
            "cn_summary": "德黑兰称坐标与联合声明草案接近完成，但通航仍取决于美国解除对伊港口封锁；特朗普称或数日内宣布。",
            "en_summary": "Tehran says coordinates and a joint statement are near final, but reopening still hinges on the US ending its port blockade.",
            "source_cn": "France 24",
            "source_en": "France 24",
            "url": "https://www.france24.com/en/middle-east/20260806-iran-says-hormuz-deal-with-oman-in-final-stage-as-trump-signals-breakthrough",
        },
        {
            "cn_title": "泽连斯基称乌军远程打击俄两座炼油厂",
            "en_title": "Zelensky says Ukraine struck two Russian oil refineries in long-range attacks",
            "published": "08:00 2026年8月6日",
            "cn_summary": "袭击目标包括雅罗斯拉夫尔Slavneft-Yanos及巴什科尔托斯坦炼油厂；俄方称拦截605架无人机但储油罐遭碎片击中起火。",
            "en_summary": "Ukraine hit refineries in Yaroslavl and Bashkortostan; Russia says it downed 605 drones but debris ignited storage tanks.",
            "source_cn": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/live/c242dmen8y3t",
        },
        {
            "cn_title": "缅甸领导人敏昂莱访问泰国寻求外交承认",
            "en_title": "Myanmar leader Min Aung Hlaing visits Thailand seeking diplomatic legitimacy",
            "published": "10:20 2026年8月6日",
            "cn_summary": "敏昂莱在曼谷与政府大楼出席欢迎仪式并与泰国总理会谈，签署劳工、跨境河流及航天合作备忘录，引发人权团体批评。",
            "en_summary": "Min Aung Hlaing was welcomed at Government House and signed MOUs on labor and cross-border issues, drawing rights group criticism.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/thailand-myanmar-asean-min-aung-hlaing-40b15f180969717a7260e7093fa1d6fb",
        },
        {
            "cn_title": "绿党领袖批评英国政府应对热浪不力",
            "en_title": "Green Party leader accuses UK government of failing on heatwave response",
            "published": "00:00 2026年8月5日",
            "cn_summary": "波兰斯基称极端高温威胁粮食与公共健康，呼吁设立免费降温空间、阻止新油气许可并加强野火防控策略。",
            "en_summary": "Zack Polanski urged cool spaces, blocking new oil licenses and wildfire strategy as record heat and drought strain the UK.",
            "source_cn": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvg9jnqd3pgo",
        },
        {
            "cn_title": "黎以停火再生变数，以色列空袭黎巴嫩南部",
            "en_title": "Israel-Hezbollah ceasefire shaky as Israel strikes southern Lebanon",
            "published": "09:10 2026年8月6日",
            "cn_summary": "法媒称以色列就「 blatant ceasefire violation」发动精确打击，罗马谈判因地面局势提前结束但或周四续谈。",
            "en_summary": "France 24 reports Israeli precise strikes after alleged ceasefire violations; Rome talks ended early but may resume Thursday.",
            "source_cn": "France 24",
            "source_en": "France 24",
            "url": "https://www.france24.com/en/middle-east/20260806-iran-says-hormuz-deal-with-oman-in-final-stage-as-trump-signals-breakthrough",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "cn_title": "警方破获高利贷集团拘25人，年利率高达282%",
            "en_title": "Police arrest 25 in loan-shark ring charging up to 282% annual interest",
            "published": "12:45 2026年8月6日",
            "cn_summary": "集团一年放贷约2亿港元，招募13岁青少年泼红漆追债；警方周二至周三突袭旺角及火炭三个运作中心。",
            "en_summary": "The triad-linked ring lent HK$200M in a year and recruited teens as young as 13 to intimidate debtors with red paint.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363126/25-arrested-hong-kong-police-bust-loan-shark-ring-charging-282-interest-rate",
        },
        {
            "cn_title": "屯马线信号故障致乘客延误最多30分钟",
            "en_title": "Tuen Ma line signal fault causes up to 30-minute MTR delays",
            "published": "14:35 2026年8月6日",
            "cn_summary": "港铁称锦上路站附近信号设备故障，下午约1时起列车减速行驶，约2时23分修复并逐步恢复正常。",
            "en_summary": "MTR said a signalling glitch near Kam Sheung Road slowed trains for up to 30 minutes before service gradually normalized.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/transport/article/3363140/mtr-passengers-face-30-minute-delays-after-hong-kong-signal-fault",
        },
        {
            "cn_title": "联招主轮录取者须今日5时前缴交留位费",
            "en_title": "JUPAS main-round offer holders must pay HK$5,000 acceptance fee by 5pm today",
            "published": "10:00 2026年8月6日",
            "cn_summary": "约34.3%申请人获大学或资助文凭录取，共15619人；逾期未缴费视为放弃本年度联招录取资格。",
            "en_summary": "About 34.3% of applicants secured places; 15,619 must pay HK$5,000 by 5pm today or forfeit their JUPAS offers.",
            "source_cn": "香港经济日报",
            "source_en": "The Standard",
            "url": "https://www.thestandard.com.hk/news/article/339097/About-34pc-students-secure-tertiary-places-in-JUPAS-main-round",
        },
    ]),
    ("其他 Other", [
        {
            "cn_title": "克里斯·帕卡姆指英国野火印证「气候崩溃已到家门口」",
            "en_title": "Chris Packham says UK wildfires show \"climate breakdown has come home\"",
            "published": "00:00 2026年8月4日",
            "cn_summary": "Springwatch主持人在邓维奇荒原大火后呼吁政客勇敢应对气候变化；政府称将投入近1亿英镑加强野火应对。",
            "en_summary": "After the Dunwich Heath blaze, Packham urged bold political action; the government cites nearly £100M for wildfire response.",
            "source_cn": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/ce3qkkzdd22o",
        },
        {
            "cn_title": "私隐专员警告假冒电子签证网站，AI伪造官网骗护照资料",
            "en_title": "Privacy watchdog warns of AI-built fake e-visa sites harvesting passport data",
            "published": "14:15 2026年8月4日",
            "cn_summary": "过去三个月收16宗查询或投诉，个案损失300至1700港元；六宗网站已转交执法机关调查。",
            "en_summary": "PCPD received 16 cases in three months with losses up to HK$1,700; six fraudulent sites were referred to law enforcement.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362890/hong-kong-warns-scam-sites-posing-canada-uk-and-thailand-e-visa-portals",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "财新": "#8e44ad", "Caixin Global": "#8e44ad",
    "美联社": "#2c3e50", "AP": "#2c3e50",
    "南华早报": "#1a5276", "SCMP": "#1a5276",
    "英国广播公司": "#2980b9", "BBC": "#2980b9",
    "香港电台": "#16a085", "RTHK": "#16a085",
    "联合国新闻": "#27ae60", "UN News": "#27ae60",
    "France 24": "#d35400",
    "香港经济日报": "#7f8c8d", "The Standard": "#7f8c8d",
}


def build_html():
    all_items = []
    for cat_name, items in CATEGORIES:
        for item in items:
            all_items.append((cat_name, item))
    n = len(all_items)

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<title>每日热点晚报 Evening Briefing 2026-08-06</title></head>',
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<div style="max-width:600px;margin:0 auto;padding:16px 12px;">',
        '<div style="background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">',
        '<div style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;color:#fff;">',
        '<div style="font-size:22px;font-weight:700;line-height:1.3;">每日热点晚报</div>',
        '<div style="font-size:14px;opacity:.85;margin-top:6px;">Evening News Briefing · 2026年8月6日 · 共', str(n), '条</div>',
        '</div>',
        '<div style="padding:20px 24px;background:#f8f9fa;border-bottom:1px solid #e9ecef;">',
        '<p style="margin:0 0 8px;font-size:14px;color:#333;line-height:1.6;">汇总今日全日要闻，涵盖财经市场、科技动态、国际局势与香港本地热点。</p>',
        '<p style="margin:0;font-size:13px;color:#666;line-height:1.5;font-style:italic;">Today\'s main stories across markets, tech, world affairs and Hong Kong.</p>',
        '</div>',
    ]

    idx = 0
    current_cat = None
    for cat_name, item in all_items:
        if cat_name != current_cat:
            current_cat = cat_name
            parts.append(
                '<div style="padding:16px 24px 8px;">'
                '<h2 style="margin:0;padding:10px 14px;background:#f1f3f5;border-left:4px solid #2563eb;font-size:15px;color:#1a1a2e;line-height:1.4;">'
                + cat_name + '</h2></div>'
            )
        idx += 1
        num = f"{idx:02d}"
        color = SOURCE_COLORS.get(item["source_cn"], "#6c757d")
        parts.extend([
            '<div style="padding:12px 24px 16px;border-bottom:1px solid #f0f0f0;">',
            '<div style="font-size:11px;color:#2563eb;font-weight:700;margin-bottom:6px;">', num, '</div>',
            '<a href="', item["url"], '" style="font-size:16px;font-weight:600;color:#1a1a2e;text-decoration:none;line-height:1.4;display:block;">',
            item["cn_title"], '</a>',
            '<div style="font-size:14px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;">', item["en_title"], '</div>',
            '<div style="font-size:11px;color:#999;margin-top:6px;">发布时间 Published: ', item["published"], '</div>',
            '<p style="margin:10px 0 4px;font-size:14px;color:#333;line-height:1.6;">', item["cn_summary"], '</p>',
            '<p style="margin:0 0 10px;font-size:13px;color:#666;line-height:1.5;font-style:italic;">', item["en_summary"], '</p>',
            '<span style="display:inline-block;background:', color, ';color:#fff;font-size:11px;padding:2px 8px;border-radius:4px;margin-right:8px;">',
            item["source_cn"], ' · ', item["source_en"], '</span>',
            '<a href="', item["url"], '" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>',
            '</div>',
        ])

    parts.extend([
        '<div style="padding:20px 24px;background:#f8f9fa;font-size:11px;color:#999;line-height:1.6;">',
        '<p style="margin:0 0 6px;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>',
        '<p style="margin:0;font-style:italic;">This briefing is for informational purposes only. Copyright belongs to original publishers.</p>',
        '</div></div></div></body></html>',
    ])
    return "".join(parts), n


def main():
    html, n = build_html()
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-06",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print(f"Built evening briefing: {n} items, {len(html)} chars -> {out}")


if __name__ == "__main__":
    main()
