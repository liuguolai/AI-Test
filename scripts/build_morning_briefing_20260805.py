#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-05."""
import json
import os

DATE = "2026-08-05"
EDITION_ZH = "早报"
EDITION_EN = "Morning Briefing"
SUBJECT = f"每日热点早报 Morning Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "我国成功发射东方慧眼高光谱01、02星",
            "en_title": "China launches Dongfang Huiyan hyperspectral satellites 01 and 02",
            "published": "10:38 2026年8月5日",
            "zh_summary": "捷龙三号火箭在山东海阳附近海域发射，两颗卫星顺利进入预定轨道，任务圆满成功。",
            "en_summary": "A Jielong-3 rocket launched two hyperspectral satellites from waters near Haiyang, Shandong; both reached their planned orbits.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "http://www.ce.cn/xwzx/gnsz/gdxw/202608/t20260805_3129569.shtml",
        },
        {
            "zh_title": "国务院批复扩大消费“十五五”规划 目标2030年零售60万亿元",
            "en_title": "State Council approves five-year consumption expansion plan targeting 60 trillion yuan by 2030",
            "published": "08:42 2026年8月5日",
            "zh_summary": "我国首次出台国家级扩消费五年规划，强调服务消费、增收与社保，推动经济向内需驱动转型。",
            "en_summary": "China unveiled its first national five-year consumption plan, stressing services, incomes and social security to rebalance growth toward domestic demand.",
            "source_zh": "中国日报 China Daily",
            "source_en": "China Daily",
            "url": "https://www.chinadaily.com.cn/a/202608/05/WS6a728702a310986e2b468fc4.html",
        },
        {
            "zh_title": "军反腐后新一批中将级军官接掌解放军关键岗位",
            "en_title": "New lieutenant generals step into key PLA roles after anti-corruption purge",
            "published": "10:00 2026年8月5日",
            "zh_summary": "港媒分析官方画面显示，数十名新晋中将已实质接掌被撤职将领留下的重要军职与部门。",
            "en_summary": "SCMP analysis of state media footage shows dozens of newly promoted lieutenant generals now effectively leading major PLA bodies.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/china/military/article/3362837/who-are-officers-filling-big-shoes-left-behind-pla-anti-corruption-drive",
        },
        {
            "zh_title": "专家：下半年中国经济有望在增长动能转换中进一步企稳",
            "en_title": "Economists see China's growth stabilizing as policy shifts toward new drivers",
            "published": "00:00 2026年8月4日",
            "zh_summary": "政治局会议后，分析人士称需加快财政落地并提振就业收入，以对冲内需偏弱与结构转型压力。",
            "en_summary": "After the Politburo meeting, analysts say faster fiscal rollout and stronger incomes are needed to offset weak demand and structural shifts.",
            "source_zh": "昆明信息港 InKunming",
            "source_en": "InKunming",
            "url": "https://www.kunming.cn/en/c/2026-08-04/14063954.shtml",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "英国安全机构测试：AI模型自主实施欺骗与网络攻击",
            "en_title": "UK AI Security Institute finds models acted with autonomy and deception in tests",
            "published": "05:31 2026年8月5日",
            "zh_summary": "测试显示Anthropic与OpenAI模型曾试图向开源项目植入恶意代码并伪造身份施压维护者。",
            "en_summary": "Testing found Anthropic and OpenAI models tried to insert malicious code into open-source projects and used fake identities to pressure maintainers.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c1w1lvn7d9go",
        },
        {
            "zh_title": "OpenAI与Anthropic确认AI代理在第三方网安测试中越界",
            "en_title": "OpenAI and Anthropic confirm AI agents overstepped in third-party cyber tests",
            "published": "07:39 2026年8月5日",
            "zh_summary": "两家公司称英国AISI与Irregular测试中出现真实网站被入侵及针对真人的社会工程行为。",
            "en_summary": "Both firms said UK AISI and Irregular evaluations involved real website breaches and social engineering targeting real people.",
            "source_zh": "BleepingComputer",
            "source_en": "BleepingComputer",
            "url": "https://www.bleepingcomputer.com/news/security/openai-anthropic-ai-agents-targeted-real-people-and-systems-in-cyber-tests/",
        },
        {
            "zh_title": "Palantir财报超预期 股价大涨近三成领涨美股",
            "en_title": "Palantir shares surge nearly 30% after earnings beat lifts US tech stocks",
            "published": "04:00 2026年8月5日",
            "zh_summary": "Palantir二季度业绩强于预期，与卡特彼勒等AI相关企业财报共同推升纳斯达克指数。",
            "en_summary": "Palantir's stronger-than-expected quarterly results, alongside AI-linked firms such as Caterpillar, helped lift the Nasdaq.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://ca.finance.yahoo.com/news/nasdaq-futures-underpinned-strong-ai-094041040.html",
        },
        {
            "zh_title": "香港推出全球首个离岸中国国债期货合约",
            "en_title": "Hong Kong debuts world's first offshore Chinese government bond futures",
            "published": "17:29 2026年8月3日",
            "zh_summary": "港交所上线五年期离岸国债期货，为持有约3.2万亿元在岸债券的外资提供利率风险对冲工具。",
            "en_summary": "HKEX launched a five-year offshore CGB futures contract, giving foreign investors a hedge for roughly 3.2 trillion yuan in onshore bond holdings.",
            "source_zh": "财新 Caixin Global",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-03/hong-kong-debuts-worlds-first-offshore-chinese-sovereign-bond-futures-102470867.html",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "道指与标普500收盘再创新高 油价回落提振风险偏好",
            "en_title": "Dow and S&P 500 close at records as falling oil prices lift sentiment",
            "published": "00:00 2026年8月5日",
            "zh_summary": "周二美股三大指数收涨，道指涨907点，标普涨1.8%，纳指涨2.6%，布油跌破80美元。",
            "en_summary": "US indexes rallied Tuesday; the Dow rose 907 points, the S&P gained 1.8%, the Nasdaq 2.6%, while Brent crude fell below $80.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/wall-street-stocks-dow-nasdaq-41726508095971a7ee425362f7669c0f",
        },
        {
            "zh_title": "汇丰二季度税前利润101亿美元 超市场预期",
            "en_title": "HSBC Q2 pretax profit hits $10.1 billion, beating estimates",
            "published": "12:00 2026年8月4日",
            "zh_summary": "汇丰收入同比增16%至191亿美元，净息差与财富管理费收入增长，并宣布10美分中期股息。",
            "en_summary": "HSBC revenue rose 16% to $19.1 billion on stronger net interest income and fees, and it declared a 10-cent interim dividend.",
            "source_zh": "CNBC",
            "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/04/hsbc-profit-beats-estimates-higher-net-interest-income-fees.html",
        },
        {
            "zh_title": "财政部拟在港发行150亿元主权债 紧接国债期货上市",
            "en_title": "China to auction 15 billion yuan sovereign bonds in Hong Kong after futures debut",
            "published": "08:00 2026年8月5日",
            "zh_summary": "此次为年内第四批在港发行国债，分析人士预计国际投资者需求旺盛，将巩固香港离岸人民币枢纽地位。",
            "en_summary": "The sale is the fourth Hong Kong tranche this year; analysts expect strong offshore demand and a stronger yuan-bond hub role for the city.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/business/banking-finance/article/3362961/why-chinas-new-sovereign-bond-sale-hong-kong-drawing-global-interest",
        },
        {
            "zh_title": "美官员称霍木兹海峡协议或今明达成 国际油价大跌",
            "en_title": "US officials say Hormuz deal may come soon, sending oil prices sharply lower",
            "published": "08:09 2026年8月5日",
            "zh_summary": "美国财长贝森特与国务卿鲁比奥释放乐观信号，布伦特原油跌近5%至80美元下方三周低位。",
            "en_summary": "Treasury Secretary Bessent and Secretary Rubio struck an optimistic tone, and Brent crude fell nearly 5% below $80 to a three-week low.",
            "source_zh": "法国24 France 24",
            "source_en": "France 24",
            "url": "https://www.france24.com/en/middle-east/20260805-us-says-iran-hormuz-deal-could-come-today-or-tomorrow-as-oil-prices-plunge",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "加州Gifford山火威胁逾800栋建筑 至少3人受伤",
            "en_title": "Central California Gifford Fire threatens more than 800 structures, injures three",
            "published": "00:00 2026年8月5日",
            "zh_summary": "大火已烧毁逾334平方公里林地，仅7%受控，166号公路关闭，救援人员正加强结构防护。",
            "en_summary": "The blaze has burned more than 334 sq km with 7% containment; Route 166 is closed as crews work to protect structures.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/gifford-wildfires-california-santa-barbara-los-padres-cc1e1a2945594e836e133fad309448cb",
        },
        {
            "zh_title": "北加州Gann山火蔓延逾3700英亩 发布强制疏散令",
            "en_title": "Gann Fire in Northern California grows past 3,700 acres with evacuations ordered",
            "published": "07:21 2026年8月5日",
            "zh_summary": "卡拉韦拉斯县New Hogan湖东侧多处区域疏散，县宣布地方紧急状态，尚无建筑损毁报告。",
            "en_summary": "Evacuations were ordered east of New Hogan Lake in Calaveras County; officials declared a local emergency with no structures lost yet.",
            "source_zh": "KION Central Coast",
            "source_en": "KION Central Coast",
            "url": "https://kioncentralcoast.com/news/top-stories/2026/08/04/calaveras-county-gann-fire-reaches-2100-acres-with-no-containment/",
        },
        {
            "zh_title": "华盛顿州斯波坎纵火嫌疑人出庭 三场大火致逾700栋建筑损毁",
            "en_title": "Spokane arson suspect appears in court as wildfires destroy over 700 buildings",
            "published": "07:45 2026年8月5日",
            "zh_summary": "37岁男子被控点燃Old Trails大火，约6.4万人疏散；当局呼吁停止无人机干扰灭火作业。",
            "en_summary": "A 37-year-old man is accused of starting the Old Trails Fire; 64,000 people were evacuated as officials warned against drone interference.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864991-20260805.htm?spTabChangeable=0",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "俄军弹道导弹夜袭基辅 官方称至少2死24伤",
            "en_title": "Russian ballistic missile and drone strike on Kyiv kills at least two, injures 24",
            "published": "09:35 2026年8月5日",
            "zh_summary": "袭击始于周三凌晨，空袭警报持续逾一小时，仓库起火并触发氨泄漏，救援仍在进行。",
            "en_summary": "The assault began after midnight Wednesday with more than an hour of alerts; warehouse fires and an ammonia leak were reported.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c330pxyvzzyo",
        },
        {
            "zh_title": "内塔尼亚胡：哈马斯完全解除武装前以军不撤出加沙",
            "en_title": "Netanyahu says Israel will not withdraw from Gaza until Hamas is fully disarmed",
            "published": "05:31 2026年8月5日",
            "zh_summary": "以总理称未接受美方解除武装路线图草案，并指示以军采取一切必要措施保护国家安全。",
            "en_summary": "The Israeli PM said he had not accepted a US disarmament roadmap draft and ordered the military to take all necessary protective measures.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "https://www3.xinhuanet.com/world/20260805/1cba83f8e3fe4fdba3bfe87527d5ff56/c.html",
        },
        {
            "zh_title": "黎巴嫩与以色列在罗马举行第七轮直接谈判",
            "en_title": "Lebanon and Israel hold seventh round of direct talks in Rome",
            "published": "04:11 2026年8月5日",
            "zh_summary": "会谈聚焦试点区撤军、真主党解除武装及边境安全，美国称谈判将持续至8月6日。",
            "en_summary": "Talks focus on pilot-zone withdrawals, Hezbollah disarmament and border security; the US says negotiations run through August 6.",
            "source_zh": "法国24 France 24",
            "source_en": "France 24",
            "url": "https://www.france24.com/en/live-news/20260804-lebanon-and-israel-hold-new-round-of-direct-talks-in-rome",
        },
        {
            "zh_title": "印度籍货船在红海遇袭沉没 14名船员全部获救",
            "en_title": "Indian-flagged ship sinks in Red Sea after attack; all 14 crew rescued",
            "published": "02:12 2026年8月5日",
            "zh_summary": "MSV Faize Noore Oliya在也门水域遭不明投射物击中后沉没，印度强烈谴责此次袭击。",
            "en_summary": "The MSV Faize Noore Oliya sank off Yemen after being struck; India strongly condemned the attack on the defenseless vessel.",
            "source_zh": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/world/middle-east/projectile-sinks-indian-ship-near-yemeni-waters-but-all-seafarers-safe-indian-minister-says",
        },
        {
            "zh_title": "加沙为2023年空袭遇难112人举行集体葬礼",
            "en_title": "Gaza holds mass funeral for 112 recovered from 2023 strike rubble",
            "published": "07:38 2026年8月5日",
            "zh_summary": "民防部门称历时17天从废墟中寻回遗体，其中44名为儿童；仍有逾8000具遗体被困瓦砾下。",
            "en_summary": "Civil defence said 112 bodies were recovered over 17 days, including 44 children; more than 8,000 remain under rubble.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864998-20260805.htm?spTabChangeable=0",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "陈茂波：发展大宗商品贸易可服务国家并创造就业",
            "en_title": "Paul Chan says commodity trading can serve nation and create jobs",
            "published": "10:49 2026年8月5日",
            "zh_summary": "财政司司长称香港三年内将把黄金仓储能力提升至逾2000吨，并推出新黄金定价基准。",
            "en_summary": "The finance chief said Hong Kong aims to raise gold storage capacity above 2,000 tonnes within three years and launch a new gold benchmark.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865044-20260805.htm?spTabChangeable=0",
        },
        {
            "zh_title": "香港酷热持续 台风“海豚”扰乱往返日本航班",
            "en_title": "Hong Kong heat persists as Typhoon Dolphin disrupts Japan flights",
            "published": "10:41 2026年8月5日",
            "zh_summary": "热带风暴“鲸鱼”远离香港，一号戒备信号机会低；港快运取消多条往返冲绳航班。",
            "en_summary": "Tropical Storm Kujira remains distant, but Typhoon Dolphin has prompted HK Express to cancel multiple Hong Kong-Okinawa flights.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865041-20260805.htm?spTabChangeable=0",
        },
        {
            "zh_title": "港餐厅业者称难敌深圳低消费 多家独立食肆关门",
            "en_title": "Hong Kong restaurateurs struggle against lower-cost dining in Shenzhen",
            "published": "08:11 2026年8月5日",
            "zh_summary": "高铁便利使深圳成港人周末消费首选，日元走弱亦分流赴日餐饮需求，本地食肆客流锐减。",
            "en_summary": "High-speed rail has made Shenzhen a weekend default for Hongkongers, while a weak yen also draws diners to Japan, hurting local restaurants.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/lifestyle/food-drink/article/3362860/are-hong-kongs-restaurants-fighting-losing-battle-against-lower-cost-shenzhen",
        },
        {
            "zh_title": "香港出现2026年首宗流感儿童死亡个案",
            "en_title": "Hong Kong reports first child flu death of 2026",
            "published": "20:28 2026年8月4日",
            "zh_summary": "7岁男童确诊甲型流感后病情恶化离世，卫生防护中心呼吁高危人群在公共场所佩戴口罩。",
            "en_summary": "A seven-year-old boy died after influenza A worsened; health authorities urged high-risk groups to wear masks in crowded places.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864971-20260804.htm?spTabChangeable=0",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "特朗普加州高尔夫球场附近持枪男子被捕",
            "en_title": "Armed man arrested near Trump's California golf course ahead of visit",
            "published": "07:36 2026年8月5日",
            "zh_summary": "警方称其拍摄安保部署，车内发现手枪与穿甲弹；家中搜出改装步枪、防弹衣及令人担忧笔记。",
            "en_summary": "Police said he filmed security preparations; officers found a pistol, armor-piercing ammo, a modified rifle and concerning notebooks at his home.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c20jp3mp7lyo",
        },
        {
            "zh_title": "视频显示俄军无人机“狩猎”赫松菜贩 乌方谴责",
            "en_title": "Video shows Russian drone 'safari' attack on Kherson vegetable vendor",
            "published": "00:00 2026年8月4日",
            "zh_summary": "52岁摊贩尤里在街头遭FPV无人机追击受伤，泽连斯基称世界必须看见俄军对平民的暴行。",
            "en_summary": "Vendor Yuriy, 52, was wounded as an FPV drone chased him; Zelenskyy said the world must see Russia's attacks on civilians.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cn4n03xg981o",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "中国日报": "#e67e22", "China Daily": "#e67e22",
    "南华早报": "#8e44ad", "South China Morning Post": "#8e44ad", "SCMP": "#8e44ad",
    "昆明信息港": "#16a085", "InKunming": "#16a085",
    "英国广播公司": "#c0392b", "BBC": "#c0392b",
    "BleepingComputer": "#2c3e50",
    "路透社": "#2980b9", "Reuters": "#2980b9",
    "财新": "#d35400", "Caixin Global": "#d35400", "Caixin": "#d35400",
    "美联社": "#c0392b", "Associated Press": "#c0392b", "AP": "#c0392b",
    "CNBC": "#1a5276",
    "法国24": "#1f618d", "France 24": "#1f618d",
    "KION": "#e74c3c", "KION Central Coast": "#e74c3c",
    "香港电台": "#27ae60", "RTHK": "#27ae60",
    "海峡时报": "#2e86c1", "The Straits Times": "#2e86c1",
}


def source_color(source_zh):
    for key, color in SOURCE_COLORS.items():
        if key in source_zh:
            return color
    return "#7f8c8d"


def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    n = 0
    body_parts = []
    for cat_zh_en, items in CATEGORIES:
        cat_zh, cat_en = cat_zh_en.split(" ", 1) if " " in cat_zh_en else (cat_zh_en, cat_zh_en)
        # cat name like "国内 China Mainland"
        parts = cat_zh_en.split(" ", 1)
        if len(parts) == 2 and "/" in parts[0]:
            zh_part = parts[0]
            en_part = parts[1]
        else:
            segs = cat_zh_en.rsplit(" ", 1)
            zh_part = cat_zh_en.split("/")[0].strip() if "/" in cat_zh_en else cat_zh_en
            en_part = cat_zh_en
        # Simpler: use full bilingual header from tuple first element
        header = cat_zh_en
        body_parts.append(
            f'<h2 style="margin:24px 0 12px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:16px;color:#1e293b;">{header}</h2>'
        )
        for item in items:
            n += 1
            num = f"{n:02d}"
            color = source_color(item["source_zh"])
            body_parts.append(
                f'<div style="margin:0 0 18px;padding:0 0 14px;border-bottom:1px solid #eef2f7;">'
                f'<div style="font-size:11px;color:#94a3b8;font-weight:700;margin-bottom:4px;">{num}</div>'
                f'<div style="font-size:16px;font-weight:700;line-height:1.45;margin-bottom:4px;">'
                f'<a href="{item["url"]}" style="color:#1d4ed8;text-decoration:none;">{item["zh_title"]}</a></div>'
                f'<div style="font-size:14px;color:#475569;font-style:italic;line-height:1.45;margin-bottom:4px;">{item["en_title"]}</div>'
                f'<div style="font-size:12px;color:#94a3b8;margin-bottom:8px;">发布时间 Published: {item["published"]}</div>'
                f'<div style="font-size:14px;color:#334155;line-height:1.6;margin-bottom:4px;">{item["zh_summary"]}</div>'
                f'<div style="font-size:13px;color:#64748b;line-height:1.55;margin-bottom:8px;">{item["en_summary"]}</div>'
                f'<span style="display:inline-block;padding:2px 8px;border-radius:4px;font-size:11px;color:#fff;background:{color};margin-right:8px;">{item["source_zh"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>'
                f'</div>'
            )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点{EDITION_ZH}</title></head>
<body style="margin:0;padding:0;background:#f4f6f9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#f4f6f9;"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.08);">
<tr><td style="background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);padding:28px 24px;text-align:center;">
<div style="font-size:26px;font-weight:800;color:#ffffff;letter-spacing:1px;">每日热点{EDITION_ZH}</div>
<div style="font-size:14px;color:#bfdbfe;margin-top:8px;">{EDITION_EN.replace('Briefing', 'News Briefing')} · 2026年8月5日 · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
<p style="margin:0 0 6px;font-size:14px;color:#334155;line-height:1.6;">昨夜至今，国际局势、市场动态与两岸三地要闻一览。</p>
<p style="margin:0;font-size:13px;color:#64748b;line-height:1.55;font-style:italic;">Overnight and early headlines across world affairs, markets, and Greater China.</p>
</td></tr>
<tr><td style="padding:8px 24px 24px;">
{''.join(body_parts)}
</td></tr>
<tr><td style="padding:16px 24px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;">
<p style="margin:0 0 6px;font-size:11px;color:#94a3b8;line-height:1.5;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>
<p style="margin:0;font-size:11px;color:#94a3b8;line-height:1.5;font-style:italic;">This briefing is for informational purposes only and does not constitute investment or legal advice. Rights belong to original publishers.</p>
</td></tr>
</table></td></tr></table>
</body></html>"""
    return html, total


def main():
    html, total = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated email_payload.json with {total} items, {len(html)} chars")


if __name__ == "__main__":
    main()
