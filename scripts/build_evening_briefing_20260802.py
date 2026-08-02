#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-02."""
import json
import os

BRIEFING_EDITION = "晚报"
LOCAL_TIME = "2026年8月2日 17:30 CST (Asia/Shanghai)"
DATE_STR = "2026-08-02"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE_STR}"

CATEGORIES = [
    ("china", "国内 / 内地", "China Mainland"),
    ("tech", "科技 / 互联网", "Technology"),
    ("finance", "财经 / 商业", "Finance & Business"),
    ("society", "社会", "Society"),
    ("world", "国际", "World"),
    ("hk", "香港本地", "Hong Kong"),
    ("other", "其他", "Other"),
]

ITEMS = [
    # 国内
    {
        "cat": "china",
        "zh_title": "海南首个“华龙一号”核电项目3号机组并网发电",
        "en_title": "Hainan's first Hualong One nuclear unit begins grid-connected operation",
        "time": "08:25 2026年8月2日",
        "zh_summary": "华能昌江核电二期3号机组并网，年发电约180亿千瓦时，为自贸港提供清洁电力。",
        "en_summary": "Unit 3 at Huaneng Changjiang Phase II entered the grid, set to supply about 18 billion kWh yearly for Hainan's free-trade port.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "http://www.hq.xinhuanet.com/20260802/369494e95e90419593609fe367f25317/c.html",
    },
    {
        "cat": "china",
        "zh_title": "解放军在黄岩岛附近举行海空联合演训",
        "en_title": "PLA stages joint naval-air drills near Scarborough Shoal",
        "time": "22:28 2026年8月1日",
        "zh_summary": "南部战区在黄岩岛领海空域演训，测试海空协同与联合打击，回应菲方海底权利主张。",
        "en_summary": "Southern Theatre Command drills tested joint strikes near Scarborough Shoal after Manila's seabed rights bid.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/china/military/article/3362628/pla-stages-south-china-sea-drills-days-after-illegal-philippine-territorial-bid",
    },
    {
        "cat": "china",
        "zh_title": "电动汽车充电桩CCC认证8月1日起强制实施",
        "en_title": "Mandatory CCC certification for EV charging equipment takes effect",
        "time": "15:08 2026年8月1日",
        "zh_summary": "未获CCC认证的供电设备禁止出厂销售进口，重点检测防触电、短路保护与耐火性能。",
        "en_summary": "Uncertified EV supply equipment is banned from sale; regulators will test shock protection, short-circuit and fire safety.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/20260801/fbd92e663811404ea1c6fe1d2cbd11a2/c.html",
    },
    {
        "cat": "china",
        "zh_title": "第12批国家药品集采开标，65种药品拟中选",
        "en_title": "China's 12th national drug bulk-buy round covers 65 medicines",
        "time": "22:57 2026年7月31日",
        "zh_summary": "上海开标产生521个拟中选产品，为迄今规模最大一批，覆盖降压降糖抗肿瘤等常用药。",
        "en_summary": "Shanghai tender yielded 521 provisional winners across 65 drugs in the largest national volume-based procurement round yet.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/fortune/20260731/367fbfa08ab14474a27418f32d0b5bb6/c.html",
    },
    # 科技
    {
        "cat": "tech",
        "zh_title": "欧盟AI大模型规则今日起可强制执行",
        "en_title": "EU rules on general-purpose AI models become enforceable",
        "time": "13:50 2026年8月2日",
        "zh_summary": "欧盟《人工智能法》大模型条款生效，布鲁塞尔成为全球最具影响力的AI监管方之一。",
        "en_summary": "Key AI Act provisions on GPAI models are now enforceable, cementing Brussels' role as a leading AI regulator.",
        "source_zh": "欧洲新闻台", "source_en": "Euronews",
        "url": "https://www.euronews.com/my-europe/2026/08/02/eu-rules-on-ai-models-become-enforceable-whats-going-to-change",
    },
    {
        "cat": "tech",
        "zh_title": "欧委会8月2日起执行AI透明度新规",
        "en_title": "Commission begins enforcing AI Act transparency rules on 2 August",
        "time": "00:00 2026年8月2日",
        "zh_summary": "聊天机器人须告知用户正在与AI互动，深度伪造须标注，逾180家机构签署内容标识自愿守则。",
        "en_summary": "Chatbots must disclose AI use and deepfakes require labels; 180+ organisations signed a voluntary marking code.",
        "source_zh": "欧盟委员会", "source_en": "European Commission",
        "url": "https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august",
        "time_note": "时间未知，已按日期占位",
    },
    {
        "cat": "tech",
        "zh_title": "澎湃新闻发布AI底座战略与12.0客户端",
        "en_title": "The Paper unveils AI foundation strategy and client 12.0",
        "time": "11:21 2026年8月2日",
        "zh_summary": "推出“星座”“星途”“星映”三大AI工作台，首页上线AI小湃与公共议题热榜。",
        "en_summary": "The Paper launched three AI workbenches and client 12.0 with an AI assistant and public-interest trending list.",
        "source_zh": "澎湃新闻", "source_en": "The Paper",
        "url": "https://www.thepaper.cn/newsDetail_forward_33696805",
    },
    {
        "cat": "tech",
        "zh_title": "乌克兰无人机袭击俄Wildberries萨马拉仓库",
        "en_title": "Ukrainian drones strike Wildberries warehouse in Russia's Samara region",
        "time": "00:00 2026年8月2日",
        "zh_summary": "俄国防部称击落635架无人机，萨马拉电商仓库遭袭，自7月18日以来约十余处物流点被打击。",
        "en_summary": "Overnight drone strikes hit Wildberries' Samara hub as Russia reported downing 635 drones across the Volga region.",
        "source_zh": "莫斯科时报 / 路透社", "source_en": "The Moscow Times / Reuters",
        "url": "https://www.themoscowtimes.com/2026/08/02/ukrainian-drones-kill-3-in-russia-strike-wildberries-warehouse-a93396",
        "time_note": "时间未知，已按日期占位",
    },
    # 财经
    {
        "cat": "finance",
        "zh_title": "香港料上调全年经济增长预测",
        "en_title": "Hong Kong set to raise full-year GDP growth forecast",
        "time": "13:57 2026年8月2日",
        "zh_summary": "陈茂波称上半年GDP同比增5.1%，将上调全年预测，并推动离岸人民币国债期货周一挂牌。",
        "en_summary": "Paul Chan said H1 GDP rose 5.1% and a higher 2026 forecast is due as offshore RMB bond futures debut Monday.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362688/hong-kong-raise-annual-gdp-forecast-after-robust-growth-first-half-2026",
    },
    {
        "cat": "finance",
        "zh_title": "梅特勒-托利多二季度业绩超预期并上调全年指引",
        "en_title": "Mettler-Toledo beats Q2 views and lifts full-year outlook",
        "time": "00:00 2026年8月2日",
        "zh_summary": "二季度调整后每股收益11.46美元，全年销售增速指引升至约4%至5%，中国市场改善明显。",
        "en_summary": "Q2 adjusted EPS hit $11.46; the firm raised 2026 sales growth guidance to about 4-5% amid stronger China demand.",
        "source_zh": "金融时报", "source_en": "Financial Times",
        "url": "https://zolmax.com/investing/mettler-toledo-international-q2-earnings-call-highlights/11936254.html",
        "time_note": "时间未知，已按日期占位",
    },
    {
        "cat": "finance",
        "zh_title": "Fortive二季度营收11亿美元并上调全年盈利指引",
        "en_title": "Fortive posts $1.1bn Q2 revenue and raises annual EPS guidance",
        "time": "00:00 2026年7月29日",
        "zh_summary": "核心收入增6.7%，调整后每股收益0.74美元，全年调整后EPS指引上调至2.95至3.05美元。",
        "en_summary": "Core revenue rose 6.7%; adjusted EPS reached $0.74 and FY guidance was lifted to $2.95-$3.05 per share.",
        "source_zh": "金融时报", "source_en": "Financial Times",
        "url": "https://markets.ft.com/data/announce/detail?dockey=600-202607290730BIZWIRE_USPRX____20260729_BW085834-1",
        "time_note": "时间未知，已按日期占位",
    },
    {
        "cat": "finance",
        "zh_title": "红海与霍尔木兹风险推高油轮运价",
        "en_title": "Red Sea and Hormuz risks drive sharp tanker rate gains",
        "time": "00:00 2026年7月28日",
        "zh_summary": "沙特原油改道绕非洲，延布至亚洲VLCC日租金升至约23万美元，地缘溢价主导运费。",
        "en_summary": "Rerouting around Africa lifted Yanbu-Asia VLCC rates to about $230,000 a day amid Middle East security premiums.",
        "source_zh": "劳氏日报", "source_en": "Lloyd's List",
        "url": "https://www.lloydslist.com/LL1158003/3D-chess-The-interwoven-tanker-effects-of-Iranian-Houthi-and-Ukrainian-attacks",
        "time_note": "时间未知，已按日期占位",
    },
    # 社会
    {
        "cat": "society",
        "zh_title": "美国爱达荷州快餐店枪击致3死7伤",
        "en_title": "Idaho fast-food shooting leaves three dead and seven injured",
        "time": "04:00 2026年8月2日",
        "zh_summary": "Twin Falls In-N-Out刚开业一周即遭枪击，枪手身亡，警方称社区威胁已解除。",
        "en_summary": "A shooting at a newly opened In-N-Out in Twin Falls killed three and wounded seven; the gunman was found dead.",
        "source_zh": "美联社", "source_en": "AP",
        "url": "https://apnews.com/article/shooting-idaho-twin-falls-15be31e5c532e7dfe4b7108d83dd47be",
        "time_note": "时间未知，已按日期占位",
    },
    {
        "cat": "society",
        "zh_title": "古巴西部五省因电网部分崩溃大面积断电",
        "en_title": "Partial grid collapse blacks out five western Cuban provinces",
        "time": "06:07 2026年8月2日",
        "zh_summary": "马坦萨斯两条220千伏线路同时跳闸，哈瓦那等五省停电，当局正优先恢复医院供水设施。",
        "en_summary": "Simultaneous line failures in Matanzas cut power across five western provinces including Havana; hospitals prioritized.",
        "source_zh": "法新社", "source_en": "AFP",
        "url": "https://www.nampa.org/text/22982025",
    },
    {
        "cat": "society",
        "zh_title": "日本青森近海发生5.8级地震",
        "en_title": "Magnitude 5.8 quake strikes off Japan's Aomori Prefecture",
        "time": "10:48 2026年8月1日",
        "zh_summary": "震源深度80公里，最大震度4，未发布海啸预警，当地暂未报告重大伤亡。",
        "en_summary": "A 5.8 quake at 80 km depth hit off Aomori's Pacific coast; no tsunami warning was issued.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260801/a75366a666f042bda3690089e8733af6/c.html",
    },
    # 国际
    {
        "cat": "world",
        "zh_title": "特朗普称取消对伊朗打击，前提是迅速达成协议",
        "en_title": "Trump cancels Iran strikes subject to rapid deal",
        "time": "10:19 2026年8月2日",
        "zh_summary": "特朗普称中东各方已就协议框架达成一致，包括全面开放霍尔木兹海峡与结束核威胁。",
        "en_summary": "Trump said regional partners agreed deal parameters including opening Hormuz and ending Iran's nuclear threat.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cjwx74qgld2o",
    },
    {
        "cat": "world",
        "zh_title": "伊朗外长警告美国勿采取冒险军事行动",
        "en_title": "Iran's foreign minister warns US against reckless action",
        "time": "06:02 2026年8月2日",
        "zh_summary": "阿拉格齐通过中间方警告美方，称伊朗已做好捍卫主权准备，将对侵略作出坚决回应。",
        "en_summary": "Araghchi warned via intermediaries that Iran is ready to respond firmly to any US or Israeli aggression.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/world/20260802/cb098e764af742c296bb30123847c997/c.html",
    },
    {
        "cat": "world",
        "zh_title": "加沙袭击持续，至少8人遇难",
        "en_title": "Israeli strikes in Gaza kill at least eight despite peace roadmap",
        "time": "08:07 2026年8月2日",
        "zh_summary": "特朗普公布15点路线图两天后，加沙多地仍遭空袭，哈马斯称撤军前不会交存武器。",
        "en_summary": "Strikes continued two days after Trump's 15-point roadmap; Hamas insists disarmament follows Israeli withdrawal.",
        "source_zh": "半岛电视台", "source_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/8/2/israel-kills-five-in-gaza-despite-trumps-hamas-disarmament-plan",
        "time_note": "时间未知，已按日期占位",
    },
    {
        "cat": "world",
        "zh_title": "莫斯科餐厅爆炸致3死21伤",
        "en_title": "Moscow restaurant blast kills three and injures 21",
        "time": "01:00 2026年8月2日",
        "zh_summary": "库德里纳广场意大利餐厅外自制炸弹爆炸，女子携爆装置被保安拦下时引爆，调查仍在进行。",
        "en_summary": "A homemade bomb detonated outside Balzi Rossi restaurant, killing the carrier, a guard and a visitor.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/c86n4ljxp63o",
    },
    {
        "cat": "world",
        "zh_title": "秘鲁观光飞机坠毁纳斯卡线条上空，13人遇难",
        "en_title": "Tourist plane crash over Peru's Nazca Lines kills all 13 aboard",
        "time": "02:00 2026年8月2日",
        "zh_summary": "塞斯纳飞机从皮斯科起飞后失联坠毁，乘客含7名意大利、2名西班牙和2名德国游客。",
        "en_summary": "A Cessna Caravan crashed near Nazca with 11 tourists and two crew; all 13 people on board died.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c70g132erlko",
    },
    # 香港
    {
        "cat": "hk",
        "zh_title": "尖沙咀酒吧谋杀案再拘捕3人",
        "en_title": "Three more arrested over Tsim Sha Tsui bar murder",
        "time": "15:32 2026年8月2日",
        "zh_summary": "警方累计拘捕12人，其中3人已被控谋杀，最新3人包括一名涉嫌谋杀男子及两名协助者。",
        "en_summary": "Police have arrested 12 people linked to the July 26 killing, including three newly detained suspects.",
        "source_zh": "香港电台", "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1864682-20260802.htm",
    },
    {
        "cat": "hk",
        "zh_title": "大埔铁人赛选手游泳环节失踪，搜救进行中",
        "en_title": "Search under way for missing triathlete in Tai Po race",
        "time": "14:06 2026年8月2日",
        "zh_summary": "59岁选手在暴雨警告后入水未再露面，消防及水警在大尾笃水上运动中心一带搜索。",
        "en_summary": "A 59-year-old swimmer vanished during the Tai Mei Tuk leg amid an amber rainstorm warning Sunday morning.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3362690/search-under-way-triathlete-59-who-went-missing-hong-kong-race",
    },
    {
        "cat": "hk",
        "zh_title": "李家超称施政报告将同步汇报五年规划进展",
        "en_title": "Lee says policy address will track five-year plan progress",
        "time": "10:49 2026年8月2日",
        "zh_summary": "特首屯门街坊座谈会听取对首份五年规划及施政报告意见，称同步谘询“尤其有意义”。",
        "en_summary": "John Lee held a Tuen Mun town hall to gather views on Hong Kong's first five-year plan and policy address.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/politics/article/3362677/especially-meaningful-john-lee-debuting-5-year-plan-policy-address",
    },
    {
        "cat": "hk",
        "zh_title": "离岸人民币国债期货将于周一在港交所 debut",
        "en_title": "Offshore RMB government bond futures to debut in Hong Kong Monday",
        "time": "13:57 2026年8月2日",
        "zh_summary": "陈茂波称将借此推动人民币国际化，配合上半年经济强劲增长与出口回暖态势。",
        "en_summary": "Paul Chan said Monday's futures launch will promote global yuan use alongside robust first-half growth.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362688/hong-kong-raise-annual-gdp-forecast-after-robust-growth-first-half-2026",
    },
    # 其他
    {
        "cat": "other",
        "zh_title": "意大利对自西班牙入境旅客重启边境检查",
        "en_title": "Italy reintroduces border checks on arrivals from Spain",
        "time": "14:25 2026年8月2日",
        "zh_summary": "梅洛尼政府因休达移民危机在海空口岸对非欧盟旅客抽查一个月，并非将西班牙踢出申根区。",
        "en_summary": "Rome restored one-month air and sea checks on non-EU arrivals from Spain after the Ceuta migration crisis.",
        "source_zh": "欧洲新闻台", "source_en": "Euronews",
        "url": "https://www.euronews.com/my-europe/2026/08/02/italy-brings-in-border-checks-for-arrivals-from-spain-what-changes",
    },
    {
        "cat": "other",
        "zh_title": "22位欧盟领导人呼吁紧急会商移民问题",
        "en_title": "22 EU leaders call for emergency talks on migration",
        "time": "14:25 2026年8月2日",
        "zh_summary": "梅洛尼与丹麦首相联名致函欧盟机构，要求加强外部边境管控与非法移民遣返效率。",
        "en_summary": "Meloni and Denmark's Frederiksen urged Brussels to tighten borders, returns and action against smugglers.",
        "source_zh": "欧洲新闻台", "source_en": "Euronews",
        "url": "https://www.euronews.com/my-europe/2026/08/02/italy-brings-in-border-checks-for-arrivals-from-spain-what-changes",
    },
]


def build_html():
    cat_map = {c[0]: c for c in CATEGORIES}
    grouped = {c[0]: [] for c in CATEGORIES}
    for item in ITEMS:
        grouped[item["cat"]].append(item)

    n = len(ITEMS)
    num = 0
    body_parts = []

    for cat_id, zh_cat, en_cat in CATEGORIES:
        items = grouped[cat_id]
        if not items:
            continue
        body_parts.append(
            f'<div class="category"><h2><span class="cat-zh">{zh_cat}</span>'
            f'<span class="cat-en">{en_cat}</span></h2>'
        )
        for item in items:
            num += 1
            label = f"{num:02d}"
            body_parts.append(
                f'<div class="item">'
                f'<div class="item-num">{label}</div>'
                f'<div class="item-body">'
                f'<a class="title-zh" href="{item["url"]}">{item["zh_title"]}</a>'
                f'<div class="title-en"><em>{item["en_title"]}</em></div>'
                f'<div class="pub-time">发布时间 Published: {item["time"]}</div>'
                f'<div class="summary-zh">{item["zh_summary"]}</div>'
                f'<div class="summary-en">{item["en_summary"]}</div>'
                f'<div class="meta">'
                f'<span class="source-tag">{item["source_zh"]} · {item["source_en"]}</span>'
                f'<a class="read-more" href="{item["url"]}">查看全文 Read more →</a>'
                f'</div></div></div>'
            )
        body_parts.append("</div>")

    body_html = "\n".join(body_parts)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日热点晚报 - {DATE_STR}</title>
</head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;color:#1a1a1a;line-height:1.6;">
<div style="max-width:600px;margin:0 auto;padding:16px 12px;">
<div style="background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">
<div style="background:linear-gradient(135deg,#1a2744 0%,#2c3e6b 100%);color:#fff;padding:28px 24px;text-align:center;">
<div style="font-size:26px;font-weight:700;margin-bottom:4px;">每日热点晚报</div>
<div style="font-size:14px;opacity:0.9;margin-bottom:8px;">Evening News Briefing · {DATE_STR}</div>
<div style="font-size:13px;opacity:0.75;">共 {n} 条</div>
</div>
<div style="padding:20px 24px;background:#f8f9fb;border-bottom:1px solid #e8eaed;">
<div style="font-size:14px;color:#444;margin-bottom:6px;">汇总今日全日要闻，涵盖政策动向、市场收盘与社会热点。</div>
<div style="font-size:13px;color:#666;font-style:italic;">Today's main stories — policy moves, market developments and social highlights.</div>
</div>
<div style="padding:8px 16px 24px;">
<style>
.category {{ margin-top:20px; }}
.category h2 {{ background:#f0f3f8;border-left:4px solid #2563eb;padding:10px 14px;margin:0 0 12px 0;font-size:15px;border-radius:0 6px 6px 0; }}
.cat-zh {{ display:block;font-weight:700;color:#1a2744; }}
.cat-en {{ display:block;font-size:12px;color:#666;font-weight:400;margin-top:2px; }}
.item {{ display:flex;gap:12px;padding:14px 8px;border-bottom:1px solid #eef0f3; }}
.item-num {{ font-size:20px;font-weight:700;color:#2563eb;min-width:36px;line-height:1.3; }}
.title-zh {{ font-size:16px;font-weight:600;color:#1a2744;text-decoration:none;display:block;margin-bottom:4px; }}
.title-zh:hover {{ color:#2563eb; }}
.title-en {{ font-size:13px;color:#555;margin-bottom:4px; }}
.pub-time {{ font-size:11px;color:#999;margin-bottom:8px; }}
.summary-zh {{ font-size:14px;color:#333;margin-bottom:4px; }}
.summary-en {{ font-size:13px;color:#666;font-style:italic;margin-bottom:8px; }}
.meta {{ display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:12px; }}
.source-tag {{ background:#e8f0fe;color:#1a56db;padding:2px 8px;border-radius:4px;font-weight:500; }}
.read-more {{ color:#2563eb;text-decoration:none;font-weight:500; }}
.read-more:hover {{ text-decoration:underline; }}
</style>
{body_html}
</div>
<div style="padding:20px 24px;background:#f8f9fb;border-top:1px solid #e8eaed;font-size:11px;color:#888;line-height:1.7;">
<div>本简报由自动化系统编发，新闻来源为公开报道，仅供信息参考，不构成投资或法律建议。观点不代表编辑部立场。</div>
<div style="margin-top:8px;font-style:italic;">This briefing is automatically compiled from public reports for informational purposes only. It does not constitute investment or legal advice.</div>
</div>
</div>
</div>
</body>
</html>"""


def main():
    html = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(root, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"TOTAL={len(ITEMS)}")
    print(f"HTML_CHARS={len(html)}")
    cats = {}
    sources = {}
    for item in ITEMS:
        cats[item["cat"]] = cats.get(item["cat"], 0) + 1
        s = item["source_en"].split("/")[0].strip().split("·")[0].strip()
        sources[s] = sources.get(s, 0) + 1
    print("CATEGORIES:", cats)
    print("SOURCES:", sources)
    for item in ITEMS:
        if item.get("time_note"):
            print(f"TIME_PLACEHOLDER: {item['zh_title'][:30]} — {item['time_note']}")


if __name__ == "__main__":
    main()
