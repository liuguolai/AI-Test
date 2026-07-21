#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json."""
import json
import os

BRIEFING_EDITION = "晚报"
EDITION_EN = "Evening Briefing"
DATE = "2026-07-21"
DATE_CN = "2026年7月21日"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "民政部发布全国首批婚丧习俗改革典型案例",
            "en_title": "China releases first national model cases for marriage and funeral customs reform",
            "published": "16:02 2026年7月21日",
            "zh_summary": "民政部公布20个地方实践，涵盖低彩礼、殡葬移风易俗等，供各地借鉴推广。",
            "en_summary": "The civil affairs ministry unveiled 20 local models on dowry limits and funeral reforms for nationwide reference.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.ce.cn/xwzx/gnsz/gdxw/202607/t20260721_3099261.shtml",
        },
        {
            "zh_title": "中方就仁爱礁冲突向菲律宾大使严正交涉",
            "en_title": "China lodges stern protest with Philippine envoy over Ren'ai Jiao clash",
            "published": "16:44 2026年7月21日",
            "zh_summary": "外交部指菲方船只危险接近并冲撞海警船，要求菲方停止挑衅与炒作。",
            "en_summary": "Beijing accused Manila of dangerous ramming and attacks on coast guard officers near Ren'ai Jiao.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260721/ab6e5a7de0a84da083d062255369ae97/c.html",
        },
        {
            "zh_title": "全国育儿补贴已发放至2516万婴幼儿",
            "en_title": "China distributes childcare subsidies to over 25.16 million infants",
            "published": "17:02 2026年7月21日",
            "zh_summary": "国家卫健委称，每名三岁以下婴幼儿每月可获300元补贴，旨在营造生育友好环境。",
            "en_summary": "The health commission said 25.16 million children under three have received monthly 300-yuan subsidies.",
            "source_zh": "中国日报", "source_en": "China Daily",
            "url": "https://www.chinadailyasia.com/hk/article/636766",
        },
        {
            "zh_title": "中方反制美制裁，禁止向10家美军工企业出口两用物项",
            "en_title": "China blocks dual-use exports to 10 US defense firms in new sanctions",
            "published": "00:00 2026年7月21日",
            "zh_summary": "商务部回应美方扩大“中国军工企业清单”，禁止向无人机商等10家美企出口两用物项。",
            "en_summary": "Beijing barred dual-use exports to 10 US military-linked firms after Washington blacklisted Chinese tech giants.",
            "source_zh": "美联社", "source_en": "Associated Press",
            "url": "https://apnews.com/article/china-us-sanctions-military-defense-tech-dualuse-1aebe98718e127365859b0fb0b63d07b",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "法院最终批准Anthropic 15亿美元版权和解",
            "en_title": "Court gives final approval to Anthropic's $1.5B copyright settlement",
            "published": "08:12 2026年7月21日",
            "zh_summary": "联邦法官批准创纪录和解，训练是否属合理使用仍留待其他案件裁决。",
            "en_summary": "A federal judge approved the landmark settlement, though fair-use questions remain open in other AI cases.",
            "source_zh": "TechCrunch", "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/",
        },
        {
            "zh_title": "美五大科技巨头表外AI债务激增至1.65万亿美元",
            "en_title": "Hidden AI-related debts at five US tech giants soar to $1.65 trillion",
            "published": "01:29 2026年7月21日",
            "zh_summary": "日经研究指数据中心租约与GPU合同推高表外负债，投资者评估风险难度加大。",
            "en_summary": "A Nikkei study says off-balance-sheet liabilities from data centers and GPUs now dwarf reported debt.",
            "source_zh": "日经亚洲", "source_en": "Nikkei Asia",
            "url": "https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding",
        },
        {
            "zh_title": "美方考虑限制企业使用中国开源AI模型",
            "en_title": "US weighs curbs on Chinese AI models amid Kimi K3 competition fears",
            "published": "00:40 2026年7月21日",
            "zh_summary": "据报道，华盛顿或借采购规则与限制交易清单施压企业停用中国AI，国家安全考量升温。",
            "en_summary": "Washington may use procurement rules and restricted-transaction lists to curb use of Chinese AI models.",
            "source_zh": "朝鲜日报", "source_en": "Chosun Biz",
            "url": "https://biz.chosun.com/en/en-it/2026/07/21/ONLLVUYYVNAWZEIR2EPRWDFCHQ/",
        },
        {
            "zh_title": "三星设立CEO直辖机器人事业部，在美中日设研发中心",
            "en_title": "Samsung creates CEO-led robotics division with R&D hubs in US, China and Japan",
            "published": "14:50 2026年7月21日",
            "zh_summary": "新设RX事业部统筹战略与商业化，前现代高管李东坤出任机器人战略负责人。",
            "en_summary": "Samsung's new RX unit will drive robotics strategy and commercialization with hubs across three countries.",
            "source_zh": "商业时报", "source_en": "The Business Times",
            "url": "https://www.businesstimes.com.sg/startups-tech/technology/samsung-creates-new-robotics-division-plans-research-hubs-us-china-and-japan",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "A股强势收涨，科创50涨11%，险资承诺加仓",
            "en_title": "Chinese stocks rally as Star 50 jumps 11% on insurer buying pledges",
            "published": "16:19 2026年7月21日",
            "zh_summary": "五大险资表态长期增持，科创板领涨，沪深300收涨3%，港股恒指基本持平。",
            "en_summary": "Mainland tech boards surged after five major insurers pledged more long-term equity investment.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/business/china-business/article/3361275/chinese-stocks-rose-04-cent-state-backed-insurers-tout-long-term-investment",
        },
        {
            "zh_title": "花旗将中国股市评级上调至超配",
            "en_title": "Citigroup upgrades Chinese equities to overweight in emerging markets",
            "published": "01:09 2026年7月21日",
            "zh_summary": "花旗下调韩国股票评级，称全球资金正寻求中国AI机遇与更低估值。",
            "en_summary": "Citi lifted China to overweight while cutting South Korea, citing cheaper valuations and AI opportunities.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-21/global-banks-turn-more-bullish-on-chinese-stocks-as-south-korea-trade-cools-102466340.html",
        },
        {
            "zh_title": "渣打支持合资企业本月推出港元稳定币HKDAP",
            "en_title": "Standard Chartered-backed venture to launch Hong Kong dollar stablecoin this month",
            "published": "17:42 2026年7月21日",
            "zh_summary": "Anchorpoint拟通过OSL、HashKey等持牌平台发行港元锚定稳定币，推进数字资产枢纽建设。",
            "en_summary": "Anchorpoint plans a regulated HKD-pegged stablecoin via licensed exchanges including OSL and HashKey.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-21/standard-chartered-backed-venture-said-to-launch-hong-kong-stablecoin-this-month-102466664.html",
        },
        {
            "zh_title": "亚洲股市反弹，日韩芯片股领涨",
            "en_title": "Asian equities rebound as chip stocks power gains in Japan and Korea",
            "published": "17:32 2026年7月21日",
            "zh_summary": "日经指数涨3.3%，韩国综指涨3.6%，内地半导体板块午后大幅反弹。",
            "en_summary": "Japan's Nikkei rose 3.3% and Korea's Kospi 3.6% as semiconductor shares led a regional rebound.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863043-20260721.htm",
        },
        {
            "zh_title": "美股周一收跌，布油涨至89美元上方",
            "en_title": "Wall Street ends lower Monday as oil rises to $89 per barrel",
            "published": "14:02 2026年7月21日",
            "zh_summary": "标普500跌0.2%，道指跌307点，中东局势推升油价与美债收益率。",
            "en_summary": "The S&P 500 slipped 0.2% and the Dow fell 307 points as Middle East tensions lifted oil and bond yields.",
            "source_zh": "Business Standard", "source_en": "Business Standard",
            "url": "https://www.business-standard.com/markets/capital-market-news/wall-street-finishes-quietly-as-rising-oil-prices-and-treasury-yields-offset-ai-gains-126072100443_1.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "重庆彭水百余餐厅每日为救援免费供餐逾2000份",
            "en_title": "Chongqing restaurants serve over 2,000 free meals daily for landslide rescuers",
            "published": "14:00 2026年7月21日",
            "zh_summary": "彭水山体滑坡后，当地餐馆为撤离群众和救援人员免费送餐，展现社区互助。",
            "en_summary": "More than 100 restaurants in Pengshui are cooking free meals for evacuees and rescue workers after a landslide.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260721/b38ff4abd87a4821b7ef67d7c87a5a10/c.html",
        },
        {
            "zh_title": "阿富汗东部闪洪致23死，逾百人失踪",
            "en_title": "Flash floods in eastern Afghanistan kill 23, leave over 100 missing",
            "published": "17:15 2026年7月21日",
            "zh_summary": "努里斯坦省帕伦市等地房屋倒塌，救援持续，10省仍面临强降雨与山洪威胁。",
            "en_summary": "Floods in Nuristan province killed 23 and left over 100 missing as rescuers search collapsed buildings.",
            "source_zh": "美联社", "source_en": "Associated Press",
            "url": "https://apnews.com/article/afghanistan-floods-climate-change-extreme-weather-7daf920202cb9ed74401dddc80be2463",
        },
        {
            "zh_title": "加沙居民称停火仅停留在纸面，以军攻击仍持续",
            "en_title": "Gaza residents say ceasefire exists only on paper as Israeli attacks continue",
            "published": "11:31 2026年7月21日",
            "zh_summary": "卫生部门称去年10月停火以来逾1150名巴勒斯坦人遇难，居民指黄线不断前移。",
            "en_summary": "Residents say over 1,150 Palestinians have been killed since October's truce as attacks and displacement persist.",
            "source_zh": "The National", "source_en": "The National",
            "url": "https://www.thenationalnews.com/news/mena/2026/07/21/gaza-residents-say-ceasefire-exists-only-on-paper-as-israeli-attacks-continue/",
        },
        {
            "zh_title": "AI自主迭代研发引发科研人员就业担忧",
            "en_title": "AI systems improving AI raise job fears among researchers",
            "published": "00:34 2026年7月21日",
            "zh_summary": "巨头用AI加速研发，美国科技业今年约14万人失业，递归自我改进时代来临。",
            "en_summary": "Tech giants are automating AI research as roughly 140,000 US tech jobs were lost this year.",
            "source_zh": "朝鲜日报", "source_en": "Chosun",
            "url": "https://www.chosun.com/english/industry-en/2026/07/21/RPG33M6D5JFVNG7IWE6NJY4RCA/",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "联合国：乌克兰平民伤亡上半年同比增37%",
            "en_title": "UN says Ukraine civilian casualties rose 37% in first half of 2026",
            "published": "19:57 2026年7月21日",
            "zh_summary": "人权监测团称1至6月1396人丧生、7978人受伤，双方空袭基础设施加剧。",
            "en_summary": "The UN documented 1,396 civilians killed and 7,978 injured in Ukraine from January through June.",
            "source_zh": "法兰西24", "source_en": "France 24",
            "url": "https://www.france24.com/en/europe/20260721-russia-ukraine-war-first-half-of-2026-sees-sharp-rise-in-civilian-casualties",
        },
        {
            "zh_title": "俄军袭击致乌至少10死87伤，多地民宅受损",
            "en_title": "Russian attacks kill at least 10 and injure 87 across Ukraine",
            "published": "17:31 2026年7月21日",
            "zh_summary": "苏梅购物中心遭袭焚毁，切尔尼戈夫行政楼受损，俄方被指使用连环打击战术。",
            "en_summary": "Strikes hit residential areas in seven oblasts, destroying a shopping center in Sumy.",
            "source_zh": "基辅独立报", "source_en": "The Kyiv Independent",
            "url": "https://kyivindependent.com/russia-killed-7-injured-79-over-past-heavily-damaging-residential-areas-across-ukraine/",
        },
        {
            "zh_title": "卫星图像显示以军在加沙修建逾23公里土堤屏障",
            "en_title": "Satellite images show Israel built 23km earthen barrier inside Gaza",
            "published": "00:00 2026年7月21日",
            "zh_summary": "以军确认沿“黄线”筑堤设安全区，担忧临时停火线或演变为永久分割。",
            "en_summary": "Israel confirmed a berm along the Yellow Line, raising fears the ceasefire boundary may become permanent.",
            "source_zh": "美联社", "source_en": "Associated Press",
            "url": "https://lasvegassun.com/news/2026/jul/21/israel-is-building-a-miles-long-earthen-barrier-in/",
        },
        {
            "zh_title": "伯恩汉执政首日，新财相希利面临艰难支出抉择",
            "en_title": "New UK chancellor Healey faces tough spending choices on Burnham's first day",
            "published": "15:34 2026年7月21日",
            "zh_summary": "首相承诺10月起削减家庭电费增值税，新内阁需为住房、减税等承诺筹措资金。",
            "en_summary": "Burnham pledged VAT cuts on household electricity bills as his new chancellor must balance ambitious spending plans.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c24mnnnd18do",
        },
        {
            "zh_title": "高市内阁批准首份“骨太”经济财政方针",
            "en_title": "Japan's Takaichi cabinet approves first Honebuto economic policy framework",
            "published": "16:49 2026年7月21日",
            "zh_summary": "方针聚焦17个战略领域半导体投资，2027财年起设无上限预算申请窗口。",
            "en_summary": "The blueprint targets aggressive spending in 17 strategic sectors including semiconductors through fiscal 2040.",
            "source_zh": "朝日新闻", "source_en": "The Asahi Shimbun",
            "url": "https://www.asahi.com/ajw/articles/16743300",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "警方马车田大赛打击非法赌博，拘捕7人",
            "en_title": "Hong Kong police arrest seven in illegal betting raids at Happy Valley Racecourse",
            "published": "14:17 2026年7月21日",
            "zh_summary": "疑犯在看台僻静位置用手机向境外网站投注，另在北角捣毁月涉40万港元赌窝。",
            "en_summary": "Seven people were held for alleged offshore betting at the racecourse during an anti-triad operation.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863028-20260721.htm",
        },
        {
            "zh_title": "天文台预警数小时内局地有骤雨雷暴",
            "en_title": "Hong Kong Observatory warns of squally thunderstorms within hours",
            "published": "09:17 2026年7月21日",
            "zh_summary": "粤西雷雨云团东移，周一红雨及黄雨警告曾持续数小时，周末天气再转不稳。",
            "en_summary": "Thundery showers over western Guangdong are moving east, with heavy rain warnings issued on Monday.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3361273/squally-thunderstorms-set-hit-parts-hong-kong-within-hours",
        },
        {
            "zh_title": "恒生指数收低10点，内地芯片股午后大幅反弹",
            "en_title": "Hang Seng ends 10 points lower as mainland chip stocks rebound sharply",
            "published": "17:32 2026年7月21日",
            "zh_summary": "恒指收报25132点，科技指数涨1.3%，成交额2899亿港元，瑞银看好下半年AI主题。",
            "en_summary": "The Hang Seng closed at 25,132 as mainland semiconductor shares staged a strong afternoon recovery.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863043-20260721.htm",
        },
        {
            "zh_title": "本届立法会议员赴京开展一周国情研修",
            "en_title": "Hong Kong lawmakers begin week-long Beijing study tour on national development",
            "published": "00:00 2026年7月20日",
            "zh_summary": "89名议员中88人参加，将访问港澳办并学习国家安全、五年规划及基层治理等议题。",
            "en_summary": "Nearly all 89 lawmakers joined the first full-class study tour to learn about national policies in Beijing.",
            "source_zh": "香港自由新闻", "source_en": "Hong Kong Free Press",
            "url": "https://hongkongfp.com/2026/07/20/hong-kongs-class-of-lawmakers-join-week-long-beijing-study-tour-to-learn-about-national-development/",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "法国6月热浪期间录得2025例超额死亡",
            "en_title": "France records 2,025 excess deaths during June heatwave peak",
            "published": "00:00 2026年7月18日",
            "zh_summary": "公共卫生署称巴黎地区死亡率高62%，欧洲正经历有记录以来最快变暖。",
            "en_summary": "Public Health France reported a 30% rise in deaths during the last week of June's record heatwave.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c3ry307rxqro",
        },
        {
            "zh_title": "欧洲今夏或再迎多轮热浪，英国亦面临高温冲击",
            "en_title": "Forecasters warn more heatwaves likely across Europe this summer",
            "published": "00:00 2026年7月21日",
            "zh_summary": "气象机构指7至8月气温大概率高于常年，极端热浪在数十年前几乎不可能出现。",
            "en_summary": "BBC Weather says above-average temperatures and significant heat bursts are likely through August.",
            "source_zh": "英国广播公司", "source_en": "BBC Weather",
            "url": "https://www.bbc.com/weather/articles/cgrk4w57e74o",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "中国日报": "#e67e22", "China Daily": "#e67e22",
    "美联社": "#2c3e50", "Associated Press": "#2c3e50",
    "TechCrunch": "#27ae60",
    "日经亚洲": "#8e44ad", "Nikkei Asia": "#8e44ad",
    "朝鲜日报": "#2980b9", "Chosun Biz": "#2980b9", "Chosun": "#2980b9",
    "商业时报": "#16a085", "The Business Times": "#16a085",
    "南华早报": "#d35400", "South China Morning Post": "#d35400",
    "财新": "#7f8c8d", "Caixin Global": "#7f8c8d",
    "香港电台": "#1abc9c", "RTHK": "#1abc9c",
    "Business Standard": "#34495e",
    "The National": "#c0392b",
    "法兰西24": "#2c3e50", "France 24": "#2c3e50",
    "基辅独立报": "#e74c3c", "The Kyiv Independent": "#e74c3c",
    "英国广播公司": "#bb1919", "BBC": "#bb1919", "BBC Weather": "#bb1919",
    "朝日新闻": "#003366", "The Asahi Shimbun": "#003366",
    "香港自由新闻": "#2c3e50", "Hong Kong Free Press": "#2c3e50",
}


def color_for(source):
    return SOURCE_COLORS.get(source, "#3498db")


def build_html():
    all_items = []
    for cat_name, items in CATEGORIES:
        for item in items:
            all_items.append((cat_name, item))
    total = len(all_items)

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">',
        f'<title>每日热点晚报 {DATE}</title></head>',
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">',
        '<tr><td align="center">',
        '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">',
        '<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">',
        '<h1 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:700;">每日热点晚报</h1>',
        f'<p style="margin:0;color:#a8b2d1;font-size:13px;">Evening News Briefing · {DATE_CN} · 共 {total} 条</p>',
        '</td></tr>',
        '<tr><td style="padding:20px 24px 8px;border-bottom:1px solid #eee;">',
        '<p style="margin:0 0 8px;color:#333;font-size:14px;line-height:1.6;">汇总今日全日要闻，涵盖政策、市场、科技与国际热点。</p>',
        '<p style="margin:0;color:#666;font-size:13px;line-height:1.5;font-style:italic;">Today\'s main stories across policy, markets, technology and world affairs.</p>',
        '</td></tr>',
    ]

    num = 0
    for cat_name, items in CATEGORIES:
        parts.append(
            f'<tr><td style="padding:16px 24px 4px;">'
            f'<h2 style="margin:0;padding:10px 14px;background:#f8f9fa;border-left:4px solid #2563eb;font-size:15px;color:#1a1a2e;">{cat_name}</h2></td></tr>'
        )
        for item in items:
            num += 1
            n = f"{num:02d}"
            c = color_for(item["source_zh"])
            parts.extend([
                '<tr><td style="padding:12px 24px 16px;border-bottom:1px solid #f0f0f0;">',
                f'<div style="color:#2563eb;font-size:11px;font-weight:700;margin-bottom:4px;">{n}</div>',
                f'<a href="{item["url"]}" style="color:#1a1a2e;font-size:16px;font-weight:600;text-decoration:none;line-height:1.4;">{item["zh_title"]}</a>',
                f'<p style="margin:4px 0 2px;color:#555;font-size:13px;font-style:italic;line-height:1.4;">{item["en_title"]}</p>',
                f'<p style="margin:0 0 8px;color:#999;font-size:11px;">发布时间 Published: {item["published"]}</p>',
                f'<p style="margin:0 0 4px;color:#444;font-size:13px;line-height:1.6;">{item["zh_summary"]}</p>',
                f'<p style="margin:0 0 10px;color:#666;font-size:12px;line-height:1.5;font-style:italic;">{item["en_summary"]}</p>',
                '<p style="margin:0;">',
                f'<span style="display:inline-block;background:{c};color:#fff;font-size:10px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item["source_zh"]} · {item["source_en"]}</span>',
                f'<a href="{item["url"]}" style="color:#2563eb;font-size:12px;text-decoration:none;">查看全文 Read more →</a>',
                '</p></td></tr>',
            ])

    parts.extend([
        '<tr><td style="padding:20px 24px;background:#f8f9fa;text-align:center;">',
        '<p style="margin:0 0 6px;color:#999;font-size:11px;line-height:1.6;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>',
        '<p style="margin:0;color:#bbb;font-size:10px;font-style:italic;">This briefing is for informational purposes only. All rights belong to original publishers.</p>',
        '</td></tr></table></td></tr></table></body></html>',
    ])
    return "".join(parts), total


def main():
    html, total = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE}",
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"TOTAL={total}")
    print(f"HTML_CHARS={len(html)}")
    for cat_name, items in CATEGORIES:
        print(f"  {cat_name}: {len(items)}")
    print(f"Written to {path}")


if __name__ == "__main__":
    main()
