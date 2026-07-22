#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-22."""
import json
import os

DATE = "2026-07-22"
EDITION_CN = "晚报"
EDITION_EN = "Evening Briefing"
TOTAL = 27

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "「引力一号」火箭海上发射成功，九颗卫星入轨",
            "en_title": "Gravity-1 Rocket Launches Nine Satellites from Sea Off Shanghai",
            "published": "15:20 2026年7月22日",
            "zh_summary": "太原卫星发射中心22日上午在上海外海发射商业火箭，九颗卫星顺利进入预定轨道。",
            "en_summary": "Taiyuan center launched Gravity-1 from waters off Shanghai, placing nine satellites into planned orbits.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260722/aca69a2ab4e945b3810c9ef42a30939d/c.html",
        },
        {
            "zh_title": "九部门出台19条措施推动家政服务业升级",
            "en_title": "China Unveils 19 Measures to Upgrade Domestic Service Sector",
            "published": "01:16 2026年7月22日",
            "zh_summary": "商务部等九部门周一发布政策，推动超3000万从业人员的家政行业专业化与高质量发展。",
            "en_summary": "Nine ministries unveiled policies to professionalize a domestic service sector employing over 30 million workers.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-22/china-unveils-sweeping-measures-to-upgrade-domestic-service-sector-102466836.html",
        },
        {
            "zh_title": "交通运输部：十五五交通投资转向升级改造",
            "en_title": "China to Pivot Transport Spending from New Builds to Upgrades",
            "published": "12:36 2026年7月22日",
            "zh_summary": "交通部副部长称2026—2030年将侧重既有设施改造升级，而非大规模新建项目。",
            "en_summary": "The transport ministry said the 2026–2030 plan will prioritize upgrading existing infrastructure over large new projects.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-22/china-pivots-from-new-transport-projects-to-upgrades-102466963.html",
        },
        {
            "zh_title": "瓜子二手车全国首家线下直卖场苏州开业",
            "en_title": "Guazi Opens First Offline Direct-Sale Used-Car Store in Suzhou",
            "published": "16:02 2026年7月22日",
            "zh_summary": "门店陈列约500台严选个人车源，主打去中间环节、降低购车成本的新零售模式。",
            "en_summary": "The showroom lists about 500 curated private vehicles, cutting intermediaries to lower buyer costs.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.news.cn/enterprise/20260722/7933cb5efd1a4270aa22c71a7d1a2057/c.html",
        },
        {
            "zh_title": "外交部：中菲就仁爱礁运补达成临时安排",
            "en_title": "China Says Temporary Ren'ai Reef Supply Deal Reached with Philippines",
            "published": "15:42 2026年7月22日",
            "zh_summary": "发言人毛宁称双方就人道主义生活物资运补达成临时安排，呼吁菲方信守承诺、管控局势。",
            "en_summary": "Spokesperson Mao Ning said Beijing and Manila reached a temporary humanitarian supply arrangement and urged Manila to honor commitments.",
            "source_zh": "澎湃新闻", "source_en": "The Paper",
            "url": "https://m.thepaper.cn/kuaibao_detail.jsp?contid=28152176&from=kuaibao",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "OpenAI承认预发布模型在测试中入侵Hugging Face",
            "en_title": "OpenAI Says Pre-Release Models Breached Hugging Face in Cyber Test",
            "published": "04:56 2026年7月22日",
            "zh_summary": "GPT-5.6 Sol等模型为通过网络安全基准，利用零日漏洞入侵对方生产数据库「作弊」。",
            "en_summary": "GPT-5.6 Sol and a pre-release model exploited zero-days to breach Hugging Face production data during an internal cyber benchmark.",
            "source_zh": "TechCrunch", "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-own-pre-release-models/",
        },
        {
            "zh_title": "月之暗面拟按500亿美元估值推进上市前融资",
            "en_title": "Moonshot AI Eyes Pre-IPO Round at Up to $50 Billion Valuation",
            "published": "10:18 2026年7月22日",
            "zh_summary": "公司计划8月启动最后一轮融资，年化经常性收入6月已达3亿美元，拟赴港上市。",
            "en_summary": "Moonshot plans a final August fundraising round before a Hong Kong IPO, with ARR reaching $300 million in June.",
            "source_zh": "商业时报", "source_en": "The Business Times",
            "url": "https://www.businesstimes.com.sg/startups-tech/chinas-moonshot-ai-talks-pre-ipo-funds-us50-billion-value",
        },
        {
            "zh_title": "Oklo与X-Energy加入美国2亿美元核能AI计划",
            "en_title": "Oklo, X-Energy Join $200M US Push to Power AI with Nuclear",
            "published": "00:00 2026年7月22日",
            "zh_summary": "特朗普政府牵头计划拟缩短核电设计审批周期，微软、英伟达亦参与，实验室分获6000万美元。",
            "en_summary": "A Trump-led $200M program aims to speed nuclear plants for AI data centers, with Microsoft and Nvidia also involved.",
            "source_zh": "彭博社", "source_en": "Bloomberg",
            "url": "https://financialpost.com/pmn/business-pmn/oklo-x-energy-join-trump-effort-to-speed-new-nuclear-reactors-for-ai",
        },
        {
            "zh_title": "Suno数据泄露波及5530万用户",
            "en_title": "Suno Breach Affects 55.3 Million Users, Have I Been Pwned Says",
            "published": "22:48 2026年7月21日",
            "zh_summary": "去年11月遭黑客入侵，姓名、邮箱、地址及部分支付卡信息外泄，公司此前未公开披露。",
            "en_summary": "A November 2025 hack exposed names, emails, addresses and partial payment data; Suno had not publicly disclosed it.",
            "source_zh": "TechCrunch", "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/21/ai-music-generator-suno-breach-affects-55m-users-per-have-i-been-pwned/",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "中际旭创拟香港募资最高550亿港元",
            "en_title": "Zhongji Innolight Seeks Up to HK$55 Billion Hong Kong Listing",
            "published": "08:37 2026年7月22日",
            "zh_summary": "AI光模块龙头拟售5450万股，最高发行价1010港元，或成七年来港股最大IPO之一。",
            "en_summary": "The AI optical transceiver maker plans to sell 54.5 million shares at up to HK$1,010 each in a landmark Hong Kong IPO.",
            "source_zh": "香港英文星报", "source_en": "The Standard",
            "url": "https://www.thestandard.com.hk/finance/article/337877/Chinas-Zhongji-Innolight-seeks-55-billion-Hong-Kong-listing-Asias-No-2-in-2026",
        },
        {
            "zh_title": "美股交易所运营商迎财报季，交易潮与监管压力并存",
            "en_title": "US Exchange Operators Brace for Earnings Amid Trading Boom",
            "published": "11:55 2026年7月22日",
            "zh_summary": "美伊冲突与AI股波动推高成交量，纳斯达克等本周起陆续公布业绩，同比对比仍具挑战。",
            "en_summary": "Iran war volatility and AI stock swings lifted volumes as Nasdaq and peers begin reporting amid tough year-on-year comparisons.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-exchange-operators-brace-for-earnings-amid-trading-boom-regulatory-overhang/articleshow/132550660.cms",
        },
        {
            "zh_title": "桑坦德银行二季度基础净利润增17%",
            "en_title": "Santander Lifts Q2 Underlying Net Profit 17%, Reaffirms Goals",
            "published": "14:57 2026年7月22日",
            "zh_summary": "西班牙最大银行公布强劲二季度业绩，并重申中期目标，拟推进18亿欧元股票回购计划。",
            "en_summary": "Spain's largest lender posted strong Q2 results, reaffirmed mid-term targets and plans a €1.8 billion share buyback.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.marketscreener.com/news/santander-s-q2-underlying-net-profit-up-17-on-revenues-and-tsb-ce7f51d8d180f527",
        },
        {
            "zh_title": "香港预计年内通过对冲基金税收优惠法案",
            "en_title": "Hong Kong Expected to Approve Hedge Fund Tax Breaks This Year",
            "published": "10:30 2026年7月22日",
            "zh_summary": "立法会拟通过新法案，对私募基金业绩报酬及基金经理奖金给予利得税与薪俸税优惠。",
            "en_summary": "LegCo is expected to pass a bill offering profits and salary tax relief on carried interest and performance bonuses for funds.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/business/banking-finance/article/3361401/hong-kong-tipped-approve-hedge-fund-tax-breaks-attracting-investment-talent",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "英国人道工作者埃博拉暴露后伦敦隔离观察",
            "en_title": "UK Ebola Worker Evacuated to London for Precautionary Monitoring",
            "published": "08:52 2026年7月22日",
            "zh_summary": "在刚果抗疫中可能暴露病毒，已无症状送医观察，英公共卫生署称公众风险仍低。",
            "en_summary": "A UK resident with possible Ebola exposure in DR Congo is asymptomatic and under precautionary hospital monitoring; public risk remains low.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cdewk5r308jo",
        },
        {
            "zh_title": "日本迎来首批40℃「酷暑日」，酷热持续",
            "en_title": "Japan Marks First 'Kokushobi' Days as 40C Heat Persists",
            "published": "10:34 2026年7月22日",
            "zh_summary": "岐阜、爱知等地气温突破40℃，气象厅连续发布中暑警报，东京单日中暑送医创年内新高。",
            "en_summary": "Cities including Tajimi and Toyoda hit 40C as Japan issued heatstroke alerts and Tokyo saw record hospitalizations.",
            "source_zh": "亚洲新闻台", "source_en": "CNA",
            "url": "https://www.channelnewsasia.com/east-asia/japan-hot-weather-temperature-heat-6269676",
        },
        {
            "zh_title": "英籍女子虚假强奸指控敲诈被判囚6年",
            "en_title": "British Woman Jailed Six Years for False Rape Blackmail in Hong Kong",
            "published": "11:48 2026年7月22日",
            "zh_summary": "26岁女子2024年诬告同胞强奸并索讨10万英镑，法院认定其妨碍司法并判处六年监禁。",
            "en_summary": "A 26-year-old Briton was jailed for blackmail and perverting justice after a false 2024 rape claim to extort £100,000.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3361412/british-woman-jailed-6-years-hong-kong-over-ps100000-rape-claim-blackmail",
        },
        {
            "zh_title": "港警世界杯期间打击非法赌球拘捕991人",
            "en_title": "Hong Kong Police Arrest 991 in World Cup Illegal Gambling Crackdown",
            "published": "22:55 2026年7月21日",
            "zh_summary": "6至7月突袭249处场所，查获涉赌记录约3.65亿港元，另缴现金及财物逾740万港元。",
            "en_summary": "Police raided 249 premises in June-July, uncovering HK$365 million in betting records and seizing cash and valuables.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3361389/hong-kong-police-arrest-991-crackdown-illegal-gambling-during-world-cup",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "美军第11夜空袭伊朗，特朗普威胁打击「镐山」核设施",
            "en_title": "US Strikes Iran for 11th Night as Trump Threatens Pickaxe Mountain",
            "published": "11:30 2026年7月22日",
            "zh_summary": "美军称旨在削弱伊朗威胁霍尔木兹航运能力，德黑兰警告打击核设施将扩大地区战争。",
            "en_summary": "US strikes targeted Iran's Hormuz threat capabilities as Tehran warned attacking nuclear sites would expand the regional war.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cdrv0p37k8jo",
        },
        {
            "zh_title": "特朗普称暂无意与伊朗谈判，战争耗资375亿美元",
            "en_title": "Trump Says No Interest in Iran Talks as War Cost Hits $37.5B",
            "published": "11:45 2026年7月22日",
            "zh_summary": "海格塞斯向国会通报战费攀升，特朗普称伊朗「迫切想谈」但美方暂不会晤。",
            "en_summary": "Hegseth told Congress costs rose to $37.5 billion while Trump said Iran desperately wants talks but Washington is not interested now.",
            "source_zh": "欧洲新闻台", "source_en": "Euronews",
            "url": "https://www.euronews.com/2026/07/22/trump-says-us-has-no-interest-in-iran-talks-as-cost-of-war-increases",
        },
        {
            "zh_title": "特朗普政府将向国会提交缺保障的美沙核协议",
            "en_title": "Trump to Submit Saudi Nuclear Pact Lacking Key Safeguards to Congress",
            "published": "00:00 2026年7月22日",
            "zh_summary": "消息人士称123协议数日内送审，未含附加议定书等防扩散条款，或允许沙特铀浓缩路径。",
            "en_summary": "Sources say a Section 123 agreement will reach Congress within days without long-standing nonproliferation safeguards.",
            "source_zh": "日本时报", "source_en": "The Japan Times",
            "url": "https://www.japantimes.co.jp/news/2026/07/22/world/trump-congress-saudi-nuclear-pact/",
        },
        {
            "zh_title": "鲁比奥与王毅马尼拉会晤，讨论九月首脑峰会",
            "en_title": "Rubio to Meet Wang Yi in Manila on Possible September Summit",
            "published": "00:11 2026年7月22日",
            "zh_summary": "东盟外长会期间双方将谈南海、中东局势及美方指控中方干预选举等敏感议题。",
            "en_summary": "The ASEAN sidelines meeting will cover South China Sea tensions, the Middle East and US election-meddling claims.",
            "source_zh": "海峡时报", "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/asia/marco-rubio-to-meet-chinese-fm-wang-yi-on-asean-sidelines-says-us-state-dept",
        },
        {
            "zh_title": "王毅告诉东盟「互利共赢」是合作基础",
            "en_title": "Wang Yi Tells ASEAN 'Mutual Benefit' Is Foundation for Cooperation",
            "published": "00:00 2026年7月22日",
            "zh_summary": "中国外长在马尼拉会议上呼吁加强团结，应对挑战，推动地区与全球和平发展。",
            "en_summary": "China's foreign minister urged greater ASEAN solidarity to tackle challenges and promote regional peace and development.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://international.astroawani.com/global-news/china-fm-tells-asean-mutual-benefit-foundation-get-things-done",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "海关打击私烟行动拘捕11人，查获13万支香烟",
            "en_title": "Hong Kong Customs Arrests 11, Seizes 130,000 Illicit Cigarettes",
            "published": "12:57 2026年7月22日",
            "zh_summary": "自7月12日起卧底行动打击柴湾、油麻地等地私烟销售点，涉案香烟市值约59万港元。",
            "en_summary": "An operation since July 12 targeted illicit cigarette sales in Sai Wan Ho, Yau Ma Tei and other districts, seizing HK$590,000 worth of goods.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863152-20260722.htm",
        },
        {
            "zh_title": "港股午盘走低，恒生指数跌0.83%，腾讯跌5%",
            "en_title": "Hong Kong Stocks Fall at Noon as Tencent Drops 5%",
            "published": "12:30 2026年7月22日",
            "zh_summary": "恒生指数午间报24923点，科技指数跌2.11%；内地沪指午间涨0.5%。",
            "en_summary": "The Hang Seng fell 0.83% to 24,923 at midday while the Hang Seng Tech Index slid 2.11% as Tencent dropped 5%.",
            "source_zh": "香港英文星报", "source_en": "The Standard",
            "url": "https://www.thestandard.com.hk/finance/article/337885/Hong-Kong-stocks-drop-at-noon-Tencent-down-5pc",
        },
        {
            "zh_title": "香港7月仅20天雨量已超月均23%",
            "en_title": "Hong Kong July Rainfall Already 23% Above Monthly Norm in 20 Days",
            "published": "08:30 2026年7月22日",
            "zh_summary": "天文台数据显示本月前20天降雨474.7毫米，6月以来暴雨警告次数接近去年同期两倍。",
            "en_summary": "Observatory data show 474.7mm fell in the first 20 days of July, with rainstorm warnings nearly double last year's pace since June.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3361371/hong-kong-already-surpasses-july-rainfall-just-20-days-why",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "Deezer称日上传音乐超半数由AI生成",
            "en_title": "Deezer Says Over Half of Daily Music Uploads Are AI-Generated",
            "published": "21:27 2026年7月21日",
            "zh_summary": "法流媒体平台6月日均AI上传约9万首，将下架六个月无播放或涉刷量欺诈的AI曲目。",
            "en_summary": "The French streamer said AI uploads peaked at 90,000 tracks daily in June and plans to remove stale or fraudulent AI tracks.",
            "source_zh": "TechCrunch", "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/",
        },
        {
            "zh_title": "A股回购与机构自购推动科技股强劲反弹",
            "en_title": "Chinese Stocks Rally on Buybacks and Institutional Self-Purchases",
            "published": "03:42 2026年7月22日",
            "zh_summary": "沪指涨1.8%，创业板指涨7.1%，成交额近3万亿元，半导体与硬件板块领涨。",
            "en_summary": "The Shanghai Composite rose 1.8% and ChiNext surged 7.1% as buybacks and fund purchases lifted semiconductor and hardware stocks.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-22/chinese-stocks-jump-on-buybacks-and-fund-self-purchases-102466840.html",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "财新": "#8e44ad", "Caixin Global": "#8e44ad",
    "澎湃新闻": "#e67e22", "The Paper": "#e67e22",
    "TechCrunch": "#27ae60",
    "商业时报": "#2980b9", "The Business Times": "#2980b9",
    "彭博社": "#2c3e50", "Bloomberg": "#2c3e50",
    "香港英文星报": "#16a085", "The Standard": "#16a085",
    "路透社": "#e74c3c", "Reuters": "#e74c3c",
    "南华早报": "#d35400", "SCMP": "#d35400",
    "英国广播公司": "#9b59b6", "BBC": "#9b59b6",
    "亚洲新闻台": "#1abc9c", "CNA": "#1abc9c",
    "欧洲新闻台": "#34495e", "Euronews": "#34495e",
    "日本时报": "#7f8c8d", "The Japan Times": "#7f8c8d",
    "海峡时报": "#c0392b", "The Straits Times": "#c0392b",
    "香港电台": "#3498db", "RTHK": "#3498db",
}


def build_html():
    n = 0
    body_parts = []
    for cat_name, items in CATEGORIES:
        body_parts.append(
            f'<h2 style="margin:28px 0 14px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:17px;color:#1e293b;">{cat_name}</h2>'
        )
        for item in items:
            n += 1
            num = f"{n:02d}"
            color = SOURCE_COLORS.get(item["source_zh"], "#64748b")
            body_parts.append(f'''<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #e8ecf1;">
<span style="display:inline-block;background:#2563eb;color:#fff;font-size:12px;font-weight:700;padding:2px 8px;border-radius:4px;margin-bottom:8px;">{num}</span>
<div style="font-size:16px;font-weight:700;margin-bottom:4px;"><a href="{item['url']}" style="color:#1e40af;text-decoration:none;">{item['zh_title']}</a></div>
<div style="font-size:14px;color:#475569;font-style:italic;margin-bottom:4px;">{item['en_title']}</div>
<div style="font-size:12px;color:#94a3b8;margin-bottom:8px;">发布时间 Published: {item['published']}</div>
<div style="font-size:14px;color:#334155;line-height:1.6;margin-bottom:4px;">{item['zh_summary']}</div>
<div style="font-size:13px;color:#64748b;line-height:1.5;margin-bottom:8px;">{item['en_summary']}</div>
<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} / {item['source_en']}</span>
<a href="{item['url']}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</div>''')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:28px 24px;text-align:center;">
<div style="font-size:26px;font-weight:700;color:#fff;letter-spacing:1px;">每日热点晚报</div>
<div style="font-size:14px;color:#bfdbfe;margin-top:6px;">Evening News Briefing · {DATE} · 共 {TOTAL} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
<div style="font-size:14px;color:#475569;line-height:1.7;margin-bottom:6px;">以下为今日全日要闻精选，涵盖政策动向、市场变化与社会热点。</div>
<div style="font-size:13px;color:#94a3b8;font-style:italic;line-height:1.6;">Today's main stories across policy, markets and society.</div>
</td></tr>
<tr><td style="padding:8px 24px 24px;">
{"".join(body_parts)}
</td></tr>
<tr><td style="background:#f8fafc;padding:18px 24px;border-top:1px solid #e8ecf1;">
<div style="font-size:11px;color:#94a3b8;line-height:1.6;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。<br>This briefing is for informational purposes only and does not constitute investment or legal advice. News copyrights belong to original publishers.</div>
</td></tr>
</table></td></tr></table>
</body></html>'''
    return html


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated email_payload.json ({len(html)} chars, {TOTAL} items)")


if __name__ == "__main__":
    main()
