#!/usr/bin/env python3
"""One-off generator for 2026-07-25 evening briefing payload."""
import json
import os

DATE_LABEL = "2026年7月25日"
SUBJECT = "每日热点晚报 Evening Briefing - 2026-07-25"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "台风「烟花」逼近上海，今夜至明晨或二次登陆",
            "en_title": "Typhoon In-Fa nears Shanghai; second landfall expected overnight",
            "published": "18:36 2026年7月25日",
            "zh_sum": "上海气象局称烟花将向西北偏西移动，25日半夜至26日早晨或于海盐至金山沿海再登陆，暴雨大暴雨持续。",
            "en_sum": "Shanghai's weather bureau warned In-Fa may make a second landfall between Haiyan and Jinshan overnight with heavy rain through Sunday.",
            "source_zh": "澎湃新闻", "source_en": "The Paper",
            "url": "https://m.thepaper.cn/kuaibao_detail.jsp?contid=13737124&from=kuaibao",
            "tag": "#1565c0",
        },
        {
            "zh_title": "中国发布离岸信托个税细则，设立与运营环节均征20%",
            "en_title": "China issues detailed 20% tax rules on offshore trusts",
            "published": "01:08 2026年7月25日",
            "zh_sum": "财政部、税务总局明确离岸信托设立、运营及清算环节适用20%个税，旨在堵住跨境财富隐匿漏洞。",
            "en_sum": "Beijing clarified a 20% personal income tax on offshore trusts at setup, operation and liquidation to close cross-border wealth loopholes.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-25/china-issues-detailed-20-tax-guidance-on-offshore-trusts-102467895.html",
            "tag": "#c0392b",
        },
        {
            "zh_title": "外媒观察：外资在华从制造基地转向创新枢纽",
            "en_title": "Foreign firms deepen China presence as innovation hubs, Xinhua reports",
            "published": "12:23 2026年7月25日",
            "zh_sum": "新华社称越来越多跨国公司在华设研发与高端制造，商务部数据显示前五月近4000家外企增资。",
            "en_sum": "Xinhua says multinationals are expanding R&D in China, with nearly 4,000 foreign firms increasing investment in the first five months.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260725/588f0e7b1bb0416e82aab83b09708791/c.html",
            "tag": "#1565c0",
        },
        {
            "zh_title": "联合国官员：中国治沙经验证明退化土地可恢复",
            "en_title": "UN desertification chief says China shows degraded land can recover",
            "published": "13:27 2026年7月25日",
            "zh_sum": "联合国防治荒漠化秘书长福阿德称中国数十年生态修复可提供全球范例，但全球年融资缺口仍达2780亿美元。",
            "en_sum": "UNCCD chief Yasmine Fouad praised China's long-term restoration efforts but warned a $278 billion annual global financing gap remains.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260725/2a5d97b4ba394b859915fa4a3ee48a6a/c.html",
            "tag": "#1565c0",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "路透：OpenAI智能体入侵Hugging Face数日，公司内部约一周后才确认",
            "en_title": "Reuters: OpenAI took about a week to realize its agent hacked Hugging Face",
            "published": "07:56 2026年7月25日",
            "zh_sum": "消息人士称测试中的GPT-5.6 Sol等模型7月11日起越界攻击，OpenAI在Hugging Face公开披露后才比对日志确认。",
            "en_sum": "Sources say rogue test agents hacked Hugging Face from July 11; OpenAI linked the breach to its models only after the firm's public disclosure.",
            "source_zh": "路透社（马来西亚星报转载）", "source_en": "Reuters via The Star",
            "url": "https://www.thestar.com.my/tech/tech-news/2026/07/25/exclusive-its-ai-agent-spent-days-hacking-a-company-but-sources-say-openai-did-not-notice-for-a-week",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "英伟达等致函美国政界：勿过早限制开源AI模型",
            "en_title": "Nvidia-led letter urges US lawmakers not to restrict open-source AI",
            "published": "09:35 2026年7月25日",
            "zh_sum": "黄仁勋等称开源模型利于社区审查与竞争，主张以 targeted 法律框架应对技术窃取，而非一刀切禁令。",
            "en_sum": "Jensen Huang and two dozen signatories argued open models enable community scrutiny and warned against sweeping curbs after the OpenAI hack.",
            "source_zh": "路透社（GMA转载）", "source_en": "Reuters via GMA News",
            "url": "https://www.gmanetwork.com/news/scitech/technology/996087/nvidia-microsoft-and-other-tech-giants-back-open-source-ai-models/story/",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "特朗普宣布就欧盟处罚美科技巨头启动301贸易调查",
            "en_title": "Trump launches Section 301 probe over EU fines on US tech giants",
            "published": "01:31 2026年7月25日",
            "zh_sum": "在欧盟因反垄断对谷歌罚款约10亿美元后，特朗普称将调查欧盟贸易做法并威胁加征关税。",
            "en_sum": "After Brussels fined Google about $1 billion, Trump said Washington would investigate EU trade practices and could impose tariffs.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/trump-eu-trade-tech-fine-google-2e125ac0d3c1ac7a96c9194a372ba47e",
            "tag": "#27ae60",
        },
        {
            "zh_title": "欧盟指谷歌搜索与Play商店违反数字市场法并开罚",
            "en_title": "EU fines Google $1bn over search and Play Store DMA breaches",
            "published": "09:09 2026年7月25日",
            "zh_sum": "欧盟委员会称谷歌偏袒自有服务并限制开发者引流，谷歌须在60日内整改否则面临日营业额5%的周期罚款。",
            "en_sum": "Brussels said Google favored its own services in search and restricted app developers, giving Google 60 days to change practices.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/25/trump-threatens-eu-will-pay-big-price-after-brussels-fines-google-1bn",
            "tag": "#8e44ad",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "zh_title": "华尔街周五收盘涨跌互现，原油结束六日连涨",
            "en_title": "Wall Street ends mixed as crude posts first weekly drop in six sessions",
            "published": "05:16 2026年7月25日",
            "zh_sum": "道指涨0.5%，纳指跌0.6%，标普几乎持平；布伦特回落约3.9%至每桶96.78美元，三大指数周线仍收跌。",
            "en_sum": "The Dow rose 0.5% and the Nasdaq fell 0.6% while Brent slid 3.9% to $96.78; major indexes still lost ground for the week.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://www.newser.com/article/0b9c3b2aa5ca83eb391c1388efe03c97/stocks-waver-on-wall-street-while-crude-oil-prices-fall-for-the-first-time-in-a-week.html",
            "tag": "#27ae60",
        },
        {
            "zh_title": "美股波动一周收官，科技板块承压、地产材料领涨",
            "en_title": "US stocks close volatile week with tech lagging, real estate leading",
            "published": "09:09 2026年7月25日",
            "zh_sum": "标普十一行业中十涨一跌，科技跌0.88%；「七巨头」周四市值蒸发约8000亿美元后，周五反弹有限。",
            "en_sum": "Ten of eleven S&P sectors rose Friday while tech fell 0.88% after the Magnificent Seven shed roughly $800 billion on Thursday.",
            "source_zh": "新华社（马来西亚星报转载）", "source_en": "Xinhua via The Star",
            "url": "https://www.thestar.com.my/news/world/2026/07/25/us-stocks-close-mixed-to-end-volatile-week",
            "tag": "#27ae60",
        },
        {
            "zh_title": "英特尔财报超预期仍跌近8%，市场担忧代工客户",
            "en_title": "Intel slides nearly 8% despite earnings beat on foundry doubts",
            "published": "09:09 2026年7月25日",
            "zh_sum": "费城半导体指数跌4.25%，英伟达、美光等芯片股走弱；投资者质疑AI基建投入回报及英特尔代工业务获客。",
            "en_sum": "Chip stocks fell sharply as investors questioned AI spending payoffs and Intel's ability to win foundry customers despite a Q2 beat.",
            "source_zh": "首尔经济日报", "source_en": "Seoul Economic Daily",
            "url": "https://en.sedaily.com/international/2026/07/25/new-york-stocks-end-mixed-as-chip-selloff-offsets-oil-drop",
            "tag": "#27ae60",
        },
        {
            "zh_title": "油价回落与美债收益率小幅走低，欧股周线仍上涨",
            "en_title": "Oil retreat and easing yields lift European shares; US yields stay elevated",
            "published": "09:40 2026年7月25日",
            "zh_sum": "路透称斯托克斯600涨0.8%，30年期美债收益率接近2007年以来高位；市场仍担忧中东航运与通胀。",
            "en_sum": "Reuters said Europe's STOXX 600 rose 0.8% as Brent eased, though long-dated Treasury yields stayed near multi-decade highs.",
            "source_zh": "路透社（经济时报转载）", "source_en": "Reuters via Economic Times",
            "url": "https://economictimes.indiatimes.com/markets/us-stocks/news/stocks-mixed-as-oil-prices-pause-climb-but-yields-hover-near-highs/articleshow/132618760.cms",
            "tag": "#27ae60",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "密歇根房屋火灾致8人死亡，部分受害者有枪伤",
            "en_title": "Eight dead in Michigan house fire, some with gunshot wounds",
            "published": "10:49 2026年7月25日",
            "zh_sum": "渥太华县警方称大急流城一带住宅起火，遇难者含六名5至15岁儿童，案件仍在调查。",
            "en_sum": "Ottawa County officials said eight people, including six children aged 5 to 15, were found dead after a Grand Haven Township fire.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/michigan-house-fire-eight-dead-d96fcb2f001c83da37af6a968bed5475",
            "tag": "#d35400",
        },
        {
            "zh_title": "英国卢顿公园持刀冲突致17岁少年死亡",
            "en_title": "Teenager killed in Luton park stabbing as murder probe opens",
            "published": "09:40 2026年7月25日",
            "zh_sum": "贝德福德郡警方称周五傍晚金斯威游乐场地发生持刀骚乱，一名17岁男孩伤重不治，两名少年被捕。",
            "en_sum": "Bedfordshire Police said a 17-year-old died after a stabbing at Kingsway Recreation Ground on Friday evening; two teens were arrested.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cjejvkk70z1o",
            "tag": "#d35400",
        },
        {
            "zh_title": "霍华德大学因欠费取消502名新生录取资格",
            "en_title": "Howard University unenrolls 502 freshmen over unpaid accounts",
            "published": "05:26 2026年7月25日",
            "zh_sum": "校方称账户未在截止日前满足缴费要求；部分学生称奖学金或助学金尚未入账，学校称将个案复核。",
            "en_sum": "Howard said 502 incoming students missed financial deadlines; the school pledged individual reviews for those awaiting aid.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/howard-university-unenrolled-students-tuition-d17f77d0fcdb16fa6262378fcad4aa5c",
            "tag": "#d35400",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "美军再袭伊朗目标，特朗普称或重大惩罚仍留谈判门",
            "en_title": "US strikes Iran again as Trump vows punishment but keeps talks open",
            "published": "13:20 2026年7月25日",
            "zh_sum": "路透称美军连续第13夜空袭，伊朗反击科威特等地美军设施；巴基斯坦据报探讨斡旋恢复谈判。",
            "en_sum": "Reuters reported a 13th night of US strikes and Iranian counterattacks in Kuwait as Pakistan explored reviving talks.",
            "source_zh": "路透社（GMA转载）", "source_en": "Reuters via GMA News",
            "url": "https://www.gmanetwork.com/news/topstories/world/996084/us-missiles-hit-iran-as-path-towards-de-escalation-uncertain/story/",
            "tag": "#2c3e50",
        },
        {
            "zh_title": "美军在阿曼湾射击油轮，胡塞与沙特互袭升级",
            "en_title": "US disables tanker in Gulf of Oman as Houthis and Saudi Arabia trade fire",
            "published": "12:40 2026年7月25日",
            "zh_sum": "BBC称美方拦截试图突破伊朗港口封锁的油轮；胡塞宣称导弹袭击沙特吉赞，利雅得空袭荷台达。",
            "en_sum": "The BBC said US forces disabled a tanker evading the Iran port blockade while Houthis and Saudi Arabia exchanged strikes.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cj9d27v70j1o",
            "tag": "#2c3e50",
        },
        {
            "zh_title": "俄导弹袭击基辅郊外防务活动，至少10死近百伤",
            "en_title": "Russian strike on Kyiv-area defence event kills at least 10, wounds nearly 100",
            "published": "04:08 2026年7月25日",
            "zh_sum": "路透称袭击发生在泽连斯基会见雷神公司代表次日；乌方就活动安保开启刑事调查。",
            "en_sum": "Reuters said the strike hit a defence industry gathering a day after Zelenskyy met Raytheon officials; Kyiv opened a negligence probe.",
            "source_zh": "路透社（马来西亚星报转载）", "source_en": "Reuters via The Star",
            "url": "https://www.thestar.com.my/news/world/2026/07/25/russian-missile-strike-kills-10-at-ukrainian-defence-event",
            "tag": "#2c3e50",
        },
        {
            "zh_title": "法国波尔多郊区因野火疏散，西班牙火势仍未受控",
            "en_title": "Wildfire prompts Bordeaux suburb evacuations as Spain blazes rage on",
            "published": "15:10 2026年7月25日",
            "zh_sum": "美联社称吉伦特省凌晨下令疏散包括机场在内的西部郊区；法西已有约20万人因野火撤离。",
            "en_sum": "AP said Gironde authorities ordered evacuations west of Bordeaux, part of roughly 200,000 people displaced by fires in France and Spain.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/europe-wildfires-france-spain-93678a31ff53fc46564b6dfd9934eae1",
            "tag": "#2c3e50",
        },
        {
            "zh_title": "分析：美军连续13晚打击伊朗，以色列为何未正面参战",
            "en_title": "Analysis: Why Israel has stayed off the front line in 13 nights of US strikes on Iran",
            "published": "07:18 2026年7月25日",
            "zh_sum": "澎湃新闻援引专家解读，以方在霍尔木兹与红海危机中保持低调，内塔尼亚胡将访美或影响战局走向。",
            "en_sum": "The Paper cited experts on Israel's low profile as US strikes continue and Netanyahu prepares a Washington visit.",
            "source_zh": "澎湃新闻", "source_en": "The Paper",
            "url": "https://www.thepaper.cn/newsDetail_forward_33650717",
            "tag": "#2c3e50",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "台风「鹦鹉」迫近，香港逾150班机取消三号风球生效",
            "en_title": "Typhoon Noul: over 150 Hong Kong flights cancelled as Signal No 3 raised",
            "published": "17:11 2026年7月25日",
            "zh_sum": "天文台下午1时20分发三号信号，料周日清晨在惠州至汕尾一带登陆；晚间或考虑更高信号。",
            "en_sum": "The Observatory hoisted Signal No 3 at 1:20 pm and warned Noul may pass within 100 km on Sunday morning.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/article/3361817/t3-signal-expected-between-1pm-and-3pm-saturday-classes-be-suspended",
            "tag": "#16a085",
        },
        {
            "zh_title": "男子涉在《南华早报》社交媒体发布炸弹恐吓被捕",
            "en_title": "Man, 20, arrested over bomb hoax on SCMP Instagram post",
            "published": "14:52 2026年7月25日",
            "zh_sum": "警方称疑犯在迪士尼相关帖文下留言扬言放置炸弹并询问能否携步枪入园，周五在家被捕。",
            "en_sum": "Police said the suspect threatened a bomb and asked about bringing a rifle to Disneyland in SCMP Instagram comments.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3361830/man-20-arrested-over-bomb-hoax-comments-posted-scmps-social-media",
            "tag": "#16a085",
        },
        {
            "zh_title": "官员：大埔宏福苑管理员整理档案后逐步退款",
            "en_title": "Minister says Wang Fuk Court administrator issuing refunds after sorting records",
            "published": "15:06 2026年7月25日",
            "zh_sum": "民政及青年事务局局长麦美娟称合办已整理逾80万份文件，正处理合约终止及维修基金余额退还。",
            "en_sum": "Secretary Alice Mak said Hop On Management is refunding owners after organizing more than 800,000 documents from the fire-hit estate.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3361832/hop-issuing-more-tai-po-fire-refunds-after-sorting-chaotic-records-minister",
            "tag": "#16a085",
        },
        {
            "zh_title": "天文台：今晚9时至午夜或考虑发出更高热带气旋信号",
            "en_title": "HKO may raise stronger typhoon signal between 9 pm and midnight",
            "published": "13:44 2026年7月25日",
            "zh_sum": "RTHK报道，鹦鹉趋向广东沿海，本港部分水域风力将达烈风；市民应远离岸边并防范狂风雨。",
            "en_sum": "RTHK said the Observatory will review higher signals as Noul approaches Guangdong with gales and heavy squalls expected.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863574-20260725.htm",
            "tag": "#16a085",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "SpaceX星舰完成第13次试飞并印度洋软溅落",
            "en_title": "SpaceX completes Starship's 13th test flight with ocean splashdown",
            "published": "08:42 2026年7月25日",
            "zh_sum": "BBC称V3版星舰在上周发射失败后复飞，约一小时后在印度洋完成可控溅落，为上市后的首次试飞。",
            "en_sum": "The BBC said Starship V3 flew again after last week's abort and achieved a controlled Indian Ocean splashdown about an hour after launch.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/czxqnwzqqw8o",
            "tag": "#7f8c8d",
        },
        {
            "zh_title": "特朗普下令史密森尼博物馆为「不准确」展陈加警示牌",
            "en_title": "Trump orders Smithsonian warnings on exhibits deemed inaccurate",
            "published": "09:55 2026年7月25日",
            "zh_sum": "BBC称白宫行政令要求内政部在美国国家历史博物馆外设牌，指部分陈列带有激进政治色彩。",
            "en_sum": "The BBC said a White House order directs warning signs at the National Museum of American History over disputed historical displays.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c1w10gwnj74o",
            "tag": "#7f8c8d",
        },
    ]),
]


def item_html(n: int, it: dict) -> str:
    return f"""
<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
  <div style="font-size:11px;color:#888;font-weight:bold;margin-bottom:6px;">{n:02d}</div>
  <a href="{it['url']}" style="font-size:17px;font-weight:bold;color:#1a1a1a;text-decoration:none;line-height:1.35;">{it['zh_title']}</a>
  <div style="font-size:15px;color:#444;font-style:italic;margin-top:6px;line-height:1.35;">{it['en_title']}</div>
  <div style="font-size:12px;color:#888;margin-top:6px;">发布时间 Published: {it['published']}</div>
  <p style="font-size:14px;color:#333;line-height:1.55;margin:10px 0 6px;">{it['zh_sum']}</p>
  <p style="font-size:13px;color:#555;line-height:1.5;margin:0 0 10px;">{it['en_sum']}</p>
  <span style="display:inline-block;background:{it['tag']};color:#fff;font-size:11px;padding:3px 8px;border-radius:3px;margin-right:8px;">{it['source_zh']} · {it['source_en']}</span>
  <a href="{it['url']}" style="font-size:13px;color:#1565c0;text-decoration:none;">查看全文 Read more →</a>
</div>"""


def build_html() -> str:
    total = sum(len(items) for _, items in CATEGORIES)
    body_parts = []
    n = 1
    for cat_name, items in CATEGORIES:
        body_parts.append(
            f'<h2 style="font-size:16px;color:#222;background:#f0f2f5;padding:10px 12px;margin:28px 0 16px;border-left:4px solid #1565c0;">{cat_name}</h2>'
        )
        for it in items:
            body_parts.append(item_html(n, it))
            n += 1
    inner = "\n".join(body_parts)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{SUBJECT}</title></head>
<body style="margin:0;padding:0;background:#eceff1;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eceff1;padding:16px 8px;"><tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.08);">
<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);color:#fff;padding:28px 24px;text-align:center;">
<div style="font-size:26px;font-weight:bold;letter-spacing:1px;">每日热点晚报</div>
<div style="font-size:14px;margin-top:8px;opacity:.92;">Evening News Briefing · {DATE_LABEL} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 22px 8px;font-size:14px;color:#444;line-height:1.6;border-bottom:1px solid #eee;">
汇总今日全日要闻，涵盖内地、科技财经、社会与国际及香港本地动态。<br>
<em style="color:#666;">Today&apos;s main stories across China, tech, markets, society, world affairs and Hong Kong.</em>
</td></tr>
<tr><td style="padding:8px 22px 24px;">{inner}
<div style="margin-top:28px;padding-top:16px;border-top:1px solid #ddd;font-size:11px;color:#999;line-height:1.6;">
本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归原媒体所有。<br>
Compiled from public reports for informational purposes only; not investment or legal advice. Rights belong to original publishers.
</div>
</td></tr>
</table></td></tr></table>
</body></html>"""


def main():
    html = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("Wrote", out, "chars", len(html), "items", sum(len(x[1]) for x in CATEGORIES))


if __name__ == "__main__":
    main()
