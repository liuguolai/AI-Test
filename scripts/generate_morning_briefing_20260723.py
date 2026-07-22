#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-07-23."""
import json
import os

BRIEFING_DATE = "2026-07-23"
BRIEFING_EDITION_CN = "早报"
BRIEFING_EDITION_EN = "Morning Briefing"
SUBJECT = f"每日热点早报 Morning Briefing - {BRIEFING_DATE}"

CATEGORIES = [
    ("china", "国内 China Mainland"),
    ("tech", "科技 Technology"),
    ("finance", "财经 Finance & Business"),
    ("society", "社会 Society"),
    ("world", "国际 World"),
    ("hk", "香港本地 Hong Kong"),
    ("other", "其他 Other"),
]

ITEMS = [
    # China Mainland (4)
    {
        "cat": "china",
        "zh_title": "上半年全国财政收入同比增长4.7%",
        "en_title": "China's fiscal revenue rises 4.7% in first half of 2026",
        "published": "16:00 2026年7月22日",
        "zh_summary": "财政部数据显示，上半年全国一般公共预算收入12.1万亿元，税收收入增5.3%，土地出让收入降31.5%。",
        "en_summary": "Fiscal revenue reached 12.1 trillion yuan in H1, with tax income up 5.3% while land-sale revenue fell 31.5%.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://finance.yahoo.com/economy/policy/articles/chinas-fiscal-revenue-expands-4-080019995.html",
    },
    {
        "cat": "china",
        "zh_title": "习近平对基础教育工作作出重要指示",
        "en_title": "Xi Jinping issues key instructions on basic education",
        "published": "17:51 2026年7月22日",
        "zh_summary": "习近平强调落实立德树人根本任务，推进基础教育扩优提质，守住教育公平底线。",
        "en_summary": "Xi stressed moral education, quality improvement and fairness as China advances basic education reform.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://www.news.cn/politics/leaders/20260722/1f778d6335b647308d0e73380411e18f/c.html",
    },
    {
        "cat": "china",
        "zh_title": "工信部启动国家级零碳工厂建设工作",
        "en_title": "China launches national zero-carbon factory initiative",
        "published": "11:58 2026年7月22日",
        "zh_summary": "工信部组织开展国家级零碳工厂建设，择优纳入名单，成熟一批验收一批，强调重建设重实效。",
        "en_summary": "The MIIT launched a national program to build zero-carbon factories through staged verification rather than one-off certification.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://www.xinhuanet.com/politics/20260722/ad1574acd3b5451bb2913c1b80c27c55/c.html",
    },
    {
        "cat": "china",
        "zh_title": "“十五五”交通投资将侧重更新改造",
        "en_title": "China to pivot transport spending toward upgrades in 15th Five-Year Plan",
        "published": "08:58 2026年7月22日",
        "zh_summary": "交通运输部表示，“十五五”不再简单铺摊子上项目，到2030年更新改造投资占比约达50%。",
        "en_summary": "The transport ministry said future investment will focus on upgrading existing infrastructure rather than rolling out new projects.",
        "source_zh": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://companies.caixin.com/2026-07-22/102466900.html",
    },
    # Technology (4)
    {
        "cat": "tech",
        "zh_title": "中美拟9月举行人工智能政府间磋商",
        "en_title": "US and China plan AI talks for September, sources say",
        "published": "18:02 2026年7月21日",
        "zh_summary": "路透援引消息人士称，双方将在特朗普政府下首次举行AI对话，美方或由贝森特牵头，日期尚未敲定。",
        "en_summary": "Reuters sources said the rivals will hold their first official AI dialogue under Trump, likely led by Treasury Secretary Bessent.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://au.finance.yahoo.com/news/exclusive-us-china-hold-ai-100210703.html",
    },
    {
        "cat": "tech",
        "zh_title": "美方指控月之暗面窃取经蒸馏技术",
        "en_title": "US accuses Moonshot AI of stealing from Anthropic's Fable model",
        "published": "21:36 2026年7月22日",
        "zh_summary": "特朗普政府科技官员称，月之暗面涉嫌蒸馏Anthropic Fable模型开发K3，并违规获取英伟达高端芯片。",
        "en_summary": "A top Trump tech official alleged Moonshot distilled Anthropic's Fable for its K3 model and acquired advanced Nvidia chips.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://d2233.cms.socastsrm.com/2026/07/22/chinas-moonshot-tapped-anthropics-fable-for-latest-ai-model-official-says/",
    },
    {
        "cat": "tech",
        "zh_title": "Anthropic以15亿美元和解作家版权诉讼",
        "en_title": "Anthropic settles authors' copyright suit for $1.5 billion",
        "published": "08:44 2026年7月22日",
        "zh_summary": "AI公司Anthropic与作家团体达成和解，赔偿创美国版权案纪录，涉未经授权使用作品训练模型。",
        "en_summary": "Anthropic agreed to pay $1.5 billion to settle a landmark authors' lawsuit over training on copyrighted works.",
        "source_zh": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://companies.caixin.com/2026-07-22/102466866.html",
    },
    {
        "cat": "tech",
        "zh_title": "阿里发布Qwen-Image-3.0图像生成模型",
        "en_title": "Alibaba unveils Qwen-Image-3.0 image generation model",
        "published": "08:44 2026年7月22日",
        "zh_summary": "新模型支持多语言原生渲染与复杂知识图解生成，可一次输出含公式符号、几何图形等元素内容。",
        "en_summary": "Alibaba's new model supports multilingual rendering and complex knowledge diagrams with formulas and graphics.",
        "source_zh": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://companies.caixin.com/2026-07-22/102466866.html",
    },
    # Finance (5)
    {
        "cat": "finance",
        "zh_title": "美股收盘涨跌互现 纳指跌0.57%",
        "en_title": "US stocks end mixed as Nasdaq falls 0.57% ahead of Big Tech earnings",
        "published": "04:47 2026年7月23日",
        "zh_summary": "道指微跌0.01%，标普500跌0.14%，纳指跌0.57%；油价升至六周高位，投资者等待科技巨头财报。",
        "en_summary": "The Dow edged down 0.01%, the S&P 500 fell 0.14% and the Nasdaq dropped 0.57% as oil hit a six-week high.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://www.aol.com/articles/wall-st-futures-edge-lower-095915000.html",
    },
    {
        "cat": "finance",
        "zh_title": "欧股STOXX 600收于两周高位",
        "en_title": "Europe's STOXX 600 closes at two-week high on earnings",
        "published": "00:32 2026年7月23日",
        "zh_summary": "欧股涨0.6%至647.07点，能源与国防股领涨；万宝盛华因业绩超预期大涨近14%。",
        "en_summary": "The STOXX 600 rose 0.6% to 647.07, led by energy and defence stocks; Randstad jumped nearly 14% on revenue beat.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://www.lse.co.uk/news/europes-stoxx-600-closes-at-two-week-high-randstad-soars-weiy9xx8oq7pe5k.html",
    },
    {
        "cat": "finance",
        "zh_title": "特斯拉Q2盈利不及预期 盘后跌约4%",
        "en_title": "Tesla Q2 earnings miss estimates despite revenue beat",
        "published": "04:30 2026年7月23日",
        "zh_summary": "特斯拉二季度调整后每股收益33美分，低于预期51美分；营收282亿美元超预期，自由现金流转负。",
        "en_summary": "Tesla posted adjusted EPS of 33 cents vs 51 cents expected, though revenue beat at $28.24 billion; free cash flow turned negative.",
        "source_zh": "CNBC",
        "source_en": "CNBC",
        "url": "https://www.cnbc.com/2026/07/22/tesla-tsla-q2-2026-earnings-report.html",
    },
    {
        "cat": "finance",
        "zh_title": "谷歌母公司Q2营收超预期 资本支出指引上调",
        "en_title": "Alphabet beats revenue estimates but lifts 2026 capex guidance",
        "published": "04:52 2026年7月23日",
        "zh_summary": "Alphabet二季度营收1198亿美元超预期，云业务增82%；全年资本支出指引上调至1950亿至2050亿美元。",
        "en_summary": "Alphabet reported $119.8 billion in Q2 revenue with cloud up 82%, but raised 2026 capex guidance to $195–205 billion.",
        "source_zh": "CNBC",
        "source_en": "CNBC",
        "url": "https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html",
    },
    {
        "cat": "finance",
        "zh_title": "国际油价涨至六周高位 突破95美元",
        "en_title": "Oil prices surge to six-week high above $95 on Middle East tensions",
        "published": "23:01 2026年7月22日",
        "zh_summary": "中东局势升级推升油价，布伦特原油突破每桶95美元，为六周来最高水平，加剧通胀担忧。",
        "en_summary": "Escalating Middle East tensions pushed Brent crude above $95 a barrel, its highest level in six weeks.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://www.lse.co.uk/news/global-markets-rising-oil-prices-weigh-on-us-stocks-ahead-of-big-tech-results-roymys42je2kqd7.html",
    },
    # Society (3)
    {
        "cat": "society",
        "zh_title": "日本多地气温突破40℃ 进入“酷暑日”",
        "en_title": "Japan swelters under second straight 'cruelly hot day' above 40C",
        "published": "15:31 2026年7月22日",
        "zh_summary": "日本气象厅称多地连续两日气温超40℃，桑名市达40.6℃；全国41都道府县发布中暑警报。",
        "en_summary": "Japan marked a second straight kokushobi day with temperatures topping 40C, triggering heatstroke alerts in 41 prefectures.",
        "source_zh": "路透社 Reuters",
        "source_en": "Reuters",
        "url": "https://www.yahoo.com/news/weather-news/articles/japan-sizzles-first-brutally-hot-021529004.html",
    },
    {
        "cat": "society",
        "zh_title": "英国6月通胀降至2.6%",
        "en_title": "UK inflation falls to 2.6% in June on lower food and fuel prices",
        "published": "14:07 2026年7月22日",
        "zh_summary": "英国国家统计局数据显示，6月CPI同比2.6%，低于5月的2.8%；分析师预计7月能源涨价将推升通胀。",
        "en_summary": "UK CPI eased to 2.6% in June from 2.8% in May, though analysts warn energy bills may push inflation back up.",
        "source_zh": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/ckg4xj8j5vjo",
    },
    {
        "cat": "society",
        "zh_title": "北爱尔兰发布宗教场所虐童调查报告",
        "en_title": "Long-awaited report on child abuse in religious settings published",
        "published": "22:24 2026年7月22日",
        "zh_summary": "报告详述37名幸存者在教堂及教会学校遭受的历史性虐待经历，呼吁设立法定机构审计保障措施。",
        "en_summary": "A report detailing abuse suffered by 37 survivors in faith settings calls for statutory oversight of safeguarding practices.",
        "source_zh": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cgje246j3p0o",
    },
    # World (5)
    {
        "cat": "world",
        "zh_title": "美沙签署为期30年民用核电合作协议",
        "en_title": "US and Saudi Arabia sign 30-year civil nuclear cooperation deal",
        "published": "05:00 2026年7月23日",
        "zh_summary": "双方签署123协议及双边保障协定，或允许沙特铀浓缩；协议将提交美国国会审议，引发防扩散担忧。",
        "en_summary": "The US and Saudi Arabia signed a 123 agreement that could allow uranium enrichment, pending congressional review.",
        "source_zh": "美联社 AP",
        "source_en": "AP",
        "url": "https://apnews.com/article/trump-saudi-arabia-nuclear-program-uranium-15fdb262bb9c83d0d959ca96b7561c12",
    },
    {
        "cat": "world",
        "zh_title": "特朗普威胁打击伊朗桥梁与发电厂",
        "en_title": "Trump threatens to target Iranian bridges and power plants over Hormuz attacks",
        "published": "11:05 2026年7月22日",
        "zh_summary": "特朗普称，若伊朗再袭击霍尔木兹海峡船只，美方将摧毁其桥梁或发电厂；美军已连续第11夜打击伊朗。",
        "en_summary": "Trump warned the US would destroy Iranian bridges or power plants if shipping in the Strait of Hormuz is attacked again.",
        "source_zh": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cdrv0p37k8jo",
    },
    {
        "cat": "world",
        "zh_title": "菲律宾军方驳斥中方“准许撤离”说法",
        "en_title": "Philippines rejects China's claim it permitted Ayungin medical evacuation",
        "published": "11:39 2026年7月22日",
        "zh_summary": "菲武装部队称，7月21日仁爱礁伤员撤离完全由菲方主导，无需任何外国许可，驳斥中方“人道准许”叙事。",
        "en_summary": "The AFP said the July 21 medevac near Ayungin Shoal was conducted solely under Philippine authority, rejecting China's claim.",
        "source_zh": "GMA News",
        "source_en": "GMA News",
        "url": "https://www.gmanetwork.com/news/topstories/nation/995717/afp-rejects-china-s-claim-it-permitted-ayungin-medical-evacuation/story/",
    },
    {
        "cat": "world",
        "zh_title": "伊朗革命卫队称打击亚马逊云巴林数据中心",
        "en_title": "Iran's IRGC claims strike on AWS data center in Bahrain",
        "published": "08:44 2026年7月22日",
        "zh_summary": "伊朗革命卫队声称打击并摧毁亚马逊云位于巴林的数据中心，中东冲突外溢至数字基础设施引发关注。",
        "en_summary": "Iran's Revolutionary Guard claimed it struck and destroyed an Amazon Web Services data center in Bahrain amid regional conflict.",
        "source_zh": "财新 Caixin",
        "source_en": "Caixin",
        "url": "https://companies.caixin.com/2026-07-22/102466866.html",
    },
    {
        "cat": "world",
        "zh_title": "菲律宾新武装部队司令誓言加强领土防卫",
        "en_title": "New Philippine military chief vows to bolster territorial defence",
        "published": "00:00 2026年7月22日",
        "zh_summary": "安东尼奥·纳法雷特就任菲武装部队司令，强调推进军队现代化与综合群岛防御概念。",
        "en_summary": "Gen. Antonio Nafarrete pledged to strengthen territorial defence and accelerate military modernization as new AFP chief.",
        "source_zh": "PTV News",
        "source_en": "PTV News",
        "url": "https://ptvnews.ph/new-afp-chief-nafarrete-vows-to-beef-up-territorial-defense-modernization/",
    },
    # Hong Kong (4)
    {
        "cat": "hk",
        "zh_title": "内地牙科连锁在港设咨询摊位或遭执法",
        "en_title": "Mainland Chinese dental clinics in Hong Kong face scrutiny",
        "published": "00:41 2026年7月23日",
        "zh_summary": "香港牙科医学会举报内地连锁在闹市设免费洗牙摊位，当局称不排除采取执法行动。",
        "en_summary": "Hong Kong authorities warned of possible enforcement against mainland dental chains suspected of illegal promotion booths.",
        "source_zh": "南华早报 SCMP",
        "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3361506/mainland-chinese-dental-clinics-hong-kong-come-under-scrutiny-authorities",
    },
    {
        "cat": "hk",
        "zh_title": "香港上半年批量购房创纪录",
        "en_title": "Hong Kong bulk flat buyers hit record high in first half",
        "published": "07:00 2026年7月23日",
        "zh_summary": "中原数据显示，上半年654名买家购入两套及以上新盘共1794伙，总值174亿港元创纪录。",
        "en_summary": "Centaline data showed 654 buyers purchased 1,794 new flats worth HK$17.4 billion in H1, all record highs.",
        "source_zh": "南华早报 SCMP",
        "source_en": "SCMP",
        "url": "https://www.scmp.com/business/markets/article/3361485/investors-bulk-buying-flats-remains-key-hong-kong-amid-red-hot-rental-market",
    },
    {
        "cat": "hk",
        "zh_title": "临终治疗指令下月起可上载医健通",
        "en_title": "End-of-life directives to be uploaded to eHealth from next week",
        "published": "19:02 2026年7月22日",
        "zh_summary": "《预设医疗指示条例》7月31日生效，患者可由注册医生将指示影像上载至电子健康纪录平台。",
        "en_summary": "From July 31, patients can have advance medical directives uploaded to Hong Kong's eHealth platform by registered doctors.",
        "source_zh": "南华早报 SCMP",
        "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3361489/end-life-directives-go-ehealth-new-law-takes-effect-hong-kong",
    },
    {
        "cat": "hk",
        "zh_title": "海关机场缉获值1100万港元毒品",
        "en_title": "Hong Kong Customs seizes HK$11 million in drugs at airport",
        "published": "02:30 2026年7月23日",
        "zh_summary": "海关在机场拘捕3名乘客，检获约5.4公斤可卡因及14公斤冰毒，总值约1100万港元。",
        "en_summary": "Customs arrested three passengers and seized cocaine and methamphetamine worth about HK$11 million at the airport.",
        "source_zh": "英文标准报 The Standard",
        "source_en": "The Standard",
        "url": "https://www.thestandard.com.hk/news/article/337968/Customs-seizes-11m-drugs-at-airport-3-passengers-arrested",
    },
    # Other (1)
    {
        "cat": "other",
        "zh_title": "利比里亚查获3.7亿美元可卡因创纪录",
        "en_title": "Liberia seizes $370 million cocaine in biggest-ever drugs bust",
        "published": "19:30 2026年7月22日",
        "zh_summary": "警方在蒙罗维亚附近突袭仓库，查获价值逾3.7亿美元可卡因，逮捕包括两名外国人在内多人。",
        "en_summary": "Police seized cocaine worth over $370 million near Monrovia in Liberia's largest drugs bust, arresting several suspects.",
        "source_zh": "BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cyvl3zgr3v4o",
    },
]

SOURCE_COLORS = {
    "Reuters": "#FF6B35",
    "Xinhua": "#C41E3A",
    "Caixin": "#1A5276",
    "CNBC": "#005594",
    "BBC": "#BB1919",
    "AP": "#2C3E50",
    "SCMP": "#003366",
    "GMA News": "#E67E22",
    "PTV News": "#8E44AD",
    "The Standard": "#27AE60",
}


def source_color(item):
    for key, color in SOURCE_COLORS.items():
        if key in item["source_en"]:
            return color
    return "#555555"


def build_html():
    n = len(ITEMS)
    cat_map = {c[0]: c[1] for c in CATEGORIES}
    grouped = {c[0]: [] for c in CATEGORIES}
    for i, item in enumerate(ITEMS, 1):
        grouped[item["cat"]].append((i, item))

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">',
        f"<title>每日热点{BRIEFING_EDITION_CN} {BRIEFING_DATE}</title></head>",
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">',
        '<tr><td align="center">',
        '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">',
        f'<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:32px 28px;text-align:center;">',
        f'<h1 style="margin:0 0 8px;color:#fff;font-size:26px;font-weight:700;">每日热点{BRIEFING_EDITION_CN}</h1>',
        f'<p style="margin:0 0 4px;color:#a8d8ea;font-size:14px;">{BRIEFING_EDITION_EN} · {BRIEFING_DATE} · 共 {n} 条</p>',
        f'<p style="margin:8px 0 0;color:#8899aa;font-size:12px;">Morning News Briefing</p></td></tr>',
        '<tr><td style="padding:24px 28px 8px;">',
        '<p style="margin:0 0 6px;color:#333;font-size:14px;line-height:1.6;">为您汇总昨夜至今晨重要新闻，涵盖国内外时政、财经市场与科技动态。</p>',
        '<p style="margin:0;color:#666;font-size:13px;font-style:italic;line-height:1.5;">Overnight and early headlines across politics, markets, technology and world affairs.</p>',
        '</td></tr>',
    ]

    for cat_id, cat_label in CATEGORIES:
        items = grouped[cat_id]
        if not items:
            continue
        parts.append(
            f'<tr><td style="padding:16px 28px 8px;">'
            f'<h2 style="margin:0;padding:10px 14px;background:#f8f9fa;border-left:4px solid #2563eb;font-size:16px;color:#1a1a2e;">{cat_label}</h2></td></tr>'
        )
        for num, item in items:
            num_str = f"{num:02d}"
            color = source_color(item)
            parts.extend([
                '<tr><td style="padding:8px 28px 16px;border-bottom:1px solid #eee;">',
                f'<p style="margin:0 0 4px;color:#2563eb;font-size:12px;font-weight:700;">{num_str}</p>',
                f'<p style="margin:0 0 4px;font-size:15px;font-weight:600;line-height:1.4;"><a href="{item["url"]}" style="color:#1a1a2e;text-decoration:none;">{item["zh_title"]}</a></p>',
                f'<p style="margin:0 0 4px;font-size:13px;color:#555;font-style:italic;line-height:1.4;">{item["en_title"]}</p>',
                f'<p style="margin:0 0 8px;font-size:11px;color:#999;">发布时间 Published: {item["published"]}</p>',
                f'<p style="margin:0 0 4px;font-size:13px;color:#444;line-height:1.6;">{item["zh_summary"]}</p>',
                f'<p style="margin:0 0 10px;font-size:12px;color:#666;font-style:italic;line-height:1.5;">{item["en_summary"]}</p>',
                f'<p style="margin:0;font-size:12px;">',
                f'<span style="display:inline-block;background:{color};color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;margin-right:8px;">{item["source_zh"]}</span>',
                f'<a href="{item["url"]}" style="color:#2563eb;text-decoration:none;">查看全文 Read more →</a></p>',
                '</td></tr>',
            ])

    parts.extend([
        '<tr><td style="padding:20px 28px;background:#f8f9fa;border-top:1px solid #eee;">',
        '<p style="margin:0 0 6px;font-size:11px;color:#999;line-height:1.6;">本简报仅供参考，内容由公开报道整理，不构成投资建议。如有疏漏请以原文为准。</p>',
        '<p style="margin:0;font-size:11px;color:#999;line-height:1.6;font-style:italic;">This briefing is for informational purposes only. Content is compiled from public sources and does not constitute investment advice.</p>',
        '</td></tr></table></td></tr></table></body></html>',
    ])
    return "".join(parts)


def main():
    html = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(ITEMS)} items, HTML length: {len(html)}")
    counts = {}
    sources = {}
    for item in ITEMS:
        counts[item["cat"]] = counts.get(item["cat"], 0) + 1
        key = item["source_en"].split()[0] if item["source_en"] else "Other"
        sources[key] = sources.get(key, 0) + 1
    print("Category counts:", counts)
    print("Source counts:", sources)


if __name__ == "__main__":
    main()
