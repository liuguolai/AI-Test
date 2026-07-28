#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-28."""
import json
import os
from html import escape

EDITION_ZH = "晚报"
EDITION_EN = "Evening Briefing"
DATE_ISO = "2026-07-28"
DATE_DISPLAY = "2026年7月28日"

CATEGORIES = [
    ("domestic", "国内 / 内地", "China Mainland"),
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
        "cat": "domestic",
        "pub": "12:53 2026年7月28日",
        "zh_title": "习近平寄语海外侨胞汇聚力量推进强国建设",
        "en_title": "Xi urges overseas Chinese to help build a strong nation",
        "zh_sum": "习近平就侨务工作作指示，号召海外侨胞和归国人员为国家建设与民族复兴贡献力量。",
        "en_sum": "President Xi Jinping called on overseas Chinese and returnees to contribute to national development and rejuvenation in new guidance on diaspora affairs.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://english.news.cn/20260728/7d648f8ae6ad4500b5154ebfe8d06461/c.html",
        "tag": "#c41e3a",
    },
    {
        "cat": "domestic",
        "pub": "13:19 2026年7月28日",
        "zh_title": "商务部发布关于所谓“产能过剩”问题立场文件",
        "en_title": "China releases position paper on 'excess capacity' claims",
        "zh_sum": "商务部周二发布立场文件，回应外界对中国产业政策的指责，阐述中方对所谓产能过剩问题的看法。",
        "en_sum": "The Ministry of Commerce issued a position document Tuesday outlining Beijing's response to international criticism of Chinese industrial policy and overcapacity allegations.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://english.news.cn/20260728/17c8690982c74213bfa1534f934a6826/c.html",
        "tag": "#c41e3a",
    },
    {
        "cat": "domestic",
        "pub": "07:59 2026年7月28日",
        "zh_title": "商务部回应美方拟制裁中国人工智能企业",
        "en_title": "China hits back at planned US AI sanctions probe",
        "zh_sum": "商务部发言人称，美方以“蒸馏”等理由威胁制裁中国AI企业缺乏依据，属典型霸权行径，中方将坚决维权。",
        "en_sum": "A commerce ministry spokesperson said threatened US sanctions over model distillation lack evidence and amount to AI hegemony, vowing China will defend its interests.",
        "src_zh": "中国经济网",
        "src_en": "China Economic Net",
        "url": "http://www.ce.cn/cysc/newmain/yc/jsxw/202607/t20260728_3111868.shtml",
        "tag": "#e67e22",
    },
    {
        "cat": "domestic",
        "pub": "09:29 2026年7月28日",
        "zh_title": "新疆新常委李刚明确兼任组织部部长",
        "en_title": "Li Gang confirmed as Xinjiang party organization chief",
        "zh_sum": "财新报道，月初履新的新疆党委常委李刚已兼任组织部部长，补缺改任乌鲁木齐市委书记的王琳。",
        "en_sum": "Caixin reported that new Xinjiang standing committee member Li Gang has taken the organization department portfolio, filling a post left when Wang Lin became Urumqi party chief.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://china.caixin.com/2026-07-28/102468628.html",
        "tag": "#8e44ad",
    },
    {
        "cat": "domestic",
        "pub": "22:02 2026年7月27日",
        "zh_title": "商务部敦促美方撤销所谓“强迫劳动”关税",
        "en_title": "Beijing urges US to drop 'forced labor' tariff measures",
        "zh_sum": "商务部称美方再以301调查加征关税是单边保护主义，敦促其纠正错误并全面取消相关措施。",
        "en_sum": "The commerce ministry called new Section 301 tariffs under a forced-labor probe unilateral protectionism and urged Washington to remove the measures.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://english.news.cn/20260727/20ee3dd78066433d940c64da92ced5de/c.html",
        "tag": "#c41e3a",
    },
    # 科技
    {
        "cat": "tech",
        "pub": "20:06 2026年7月27日",
        "zh_title": "英伟达牵头成立开放安全人工智能联盟",
        "en_title": "Nvidia and Microsoft launch Open Secure AI Alliance",
        "zh_sum": "数十家科技与安全公司结盟，共享开源工具以加强AI与智能体安全，未纳入OpenAI、谷歌等头部实验室。",
        "en_sum": "Dozens of tech and security firms formed an alliance to share open tools for AI safety after concerns over autonomous agent risks, without several leading US AI labs.",
        "src_zh": "The Verge",
        "src_en": "The Verge",
        "url": "https://www.theverge.com/ai-artificial-intelligence/971281/nvidia-open-secure-ai-alliance-cybersecurity",
        "tag": "#2c3e50",
    },
    {
        "cat": "tech",
        "pub": "01:32 2026年7月28日",
        "zh_title": "英伟达据报拟为OpenAI数据中心提供巨额担保",
        "en_title": "Nvidia in talks on huge OpenAI data-centre backstop",
        "zh_sum": "CNBC确认，英伟达或最高提供约2500亿美元信用担保，助OpenAI为俄亥俄州10吉瓦数据中心项目融资。",
        "en_sum": "CNBC said Nvidia is discussing up to a $250 billion guarantee to help OpenAI finance a 10-gigawatt Ohio campus, leveraging the chipmaker's credit.",
        "src_zh": "CNBC",
        "src_en": "CNBC",
        "url": "https://www.cnbc.com/2026/07/27/nvidia-and-openai-in-talks-for-up-to-250-billion-dollar-ai-backstop.html",
        "tag": "#27ae60",
    },
    {
        "cat": "tech",
        "pub": "11:03 2026年7月28日",
        "zh_title": "中国浸没式光刻进展冲击ASML股价",
        "en_title": "Report of China DUV tools hits ASML shares",
        "zh_sum": "港媒援引报道指中国开始量产浸没式DUV光刻机，ASML股价大跌，长鑫上市热潮亦加剧亚洲芯片股波动。",
        "en_sum": "Hong Kong media cited reports that China has begun producing immersion DUV lithography gear, sending ASML shares lower as CXMT's debut roils chip stocks.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1864021-20260728.htm",
        "tag": "#16a085",
    },
    {
        "cat": "tech",
        "pub": "00:00 2026年7月28日",
        "zh_title": "科技巨头联手推进开源AI安全工具共享",
        "en_title": "Tech giants pledge open AI security tooling",
        "zh_sum": "SecurityWeek称联盟将发布可审计的智能体框架与漏洞扫描工具，回应近期自主AI失控事件引发的安全担忧。",
        "en_sum": "SecurityWeek said partners will share auditable agent frameworks and scanning harnesses after recent incidents raised fears about autonomous AI systems.",
        "src_zh": "SecurityWeek",
        "src_en": "SecurityWeek",
        "url": "https://www.securityweek.com/nvidia-and-tech-giants-launch-ai-security-alliance/",
        "tag": "#34495e",
    },
    # 财经
    {
        "cat": "finance",
        "pub": "09:29 2026年7月28日",
        "zh_title": "A股低开沪指跌0.91% 电子板块领跌",
        "en_title": "China stocks open lower as electronics slide",
        "zh_sum": "财新称沪指开盘报3823点跌0.91%，深成指、创业板指跌幅更大，电子与通信板块走弱。",
        "en_sum": "Caixin said the Shanghai Composite opened down 0.91% at 3823 with deeper losses on the Shenzhen and ChiNext boards as electronics and telecoms fell.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-07-28/102468631.html",
        "tag": "#8e44ad",
    },
    {
        "cat": "finance",
        "pub": "16:01 2026年7月28日",
        "zh_title": "韩国综指收盘暴跌逾10% 芯片股重挫",
        "en_title": "Kospi closes down nearly 11% in chip rout",
        "zh_sum": "韩股创数月最大单日跌幅，SK海力士、三星电子大跌，市场担忧中国存储竞争与AI投资泡沫。",
        "en_sum": "South Korea's Kospi posted its worst day in months as SK Hynix and Samsung plunged on fears of Chinese memory competition and AI trade fatigue.",
        "src_zh": "The Hindu BusinessLine",
        "src_en": "The Hindu BusinessLine",
        "url": "https://www.thehindubusinessline.com/markets/stock-markets/south-koreas-kospi-falls-over-7-as-china-chip-threat-hits-sk-hynix-samsung/article71275342.ece",
        "tag": "#2980b9",
    },
    {
        "cat": "finance",
        "pub": "13:47 2026年7月28日",
        "zh_title": "奔驰下调全年销量指引 指中国市场承压",
        "en_title": "Mercedes-Benz cuts sales outlook on China slump",
        "zh_sum": "路透称奔驰二季度利润回升但仍下调乘用车销量与集团收入预期，称中国竞争加剧拖累前景。",
        "en_sum": "Reuters reported Mercedes lifted quarterly profit but trimmed car sales and revenue guidance, citing tougher competition in China.",
        "src_zh": "路透 / MarketScreener",
        "src_en": "Reuters / MarketScreener",
        "url": "https://ae.marketscreener.com/news/mercedes-benz-improves-profit-cuts-forecast-for-passenger-car-sales-ce7f51dddb89f025",
        "tag": "#1a5276",
    },
    {
        "cat": "finance",
        "pub": "08:00 2026年7月28日",
        "zh_title": "新加坡买家成香港写字楼最大外资群体",
        "en_title": "Singapore investors lead foreign Hong Kong office buys",
        "zh_sum": "仲量联行数据显示，二季度新加坡资本占香港非本地商业地产投资六成，趁价格回调收购优质资产。",
        "en_sum": "Colliers data showed Singapore-based buyers accounted for 62% of non-local commercial investment in Hong Kong in Q2 as prices corrected.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/business/article/3362016/singapore-based-investors-now-top-non-local-buyers-hong-kong-office-assets",
        "tag": "#e74c3c",
    },
    {
        "cat": "finance",
        "pub": "18:43 2026年7月27日",
        "zh_title": "美伊暂停打击预期推动国际油价大跌",
        "en_title": "Oil plunges as US-Iran pause fuels de-escalation bets",
        "zh_sum": "BBC称布伦特原油一度跌超9%，投资者押注华盛顿与德黑兰谈判空间扩大，风险溢价快速回落。",
        "en_sum": "The BBC said Brent crude fell more than 9% as markets bet a pause in US-Iran strikes could ease Middle East supply fears.",
        "src_zh": "BBC",
        "src_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/clyj834jn5lo",
        "tag": "#192f6a",
    },
    # 社会
    {
        "cat": "society",
        "pub": "20:56 2026年7月27日",
        "zh_title": "巴黎持刀案致三名女子受伤 嫌犯被制服",
        "en_title": "Three women wounded in Paris knife attack",
        "zh_sum": "欧媒称克利希门附近发生持刀伤人，两名伤者伤势严重，内政部长称嫌犯言论混乱，动机仍待查。",
        "en_sum": "Euronews said three women were hospitalised after a knife assault near Porte de Clichy; police detained a suspect as officials cautioned on motive.",
        "src_zh": "欧洲新闻台",
        "src_en": "Euronews",
        "url": "https://www.euronews.com/my-europe/2026/07/27/three-injured-in-paris-knife-attack-one-suspect-arrested-police-say",
        "tag": "#7f8c8d",
    },
    {
        "cat": "society",
        "pub": "15:38 2026年7月28日",
        "zh_title": "研究警告全球儿童抗生素耐药性上升",
        "en_title": "Study warns rising antibiotic resistance in children",
        "zh_sum": "悉尼大学牵头研究分析逾10万份样本，称儿童尤其重症与低资源地区耐药菌株增速最快，或威胁救命药物。",
        "en_sum": "A University of Sydney-led study of more than 106,000 samples found rising resistance among children, especially in intensive care and lower-resource settings.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://english.news.cn/20260728/8368afc1eb474a9d925a89e05d4ddde9/c.html",
        "tag": "#c41e3a",
    },
    {
        "cat": "society",
        "pub": "11:57 2026年7月28日",
        "zh_title": "吉隆坡警方安置联合国难民署外罗兴亚群体",
        "en_title": "Police relocate Rohingya camped outside UNHCR in KL",
        "zh_sum": "自由马来西亚今日称126名罗兴亚难民被转至警总部筛查，警方确认多数人持有效联合国难民证件。",
        "en_sum": "Free Malaysia Today said 126 Rohingya refugees were moved from outside the UNHCR office for screening, with police confirming valid UN cards.",
        "src_zh": "自由马来西亚今日",
        "src_en": "Free Malaysia Today",
        "url": "https://www.freemalaysiatoday.com/category/nation/2026/07/28/detained-rohingya-are-valid-unhcr-cardholders-say-cops",
        "tag": "#6c3483",
    },
    # 国际
    {
        "cat": "world",
        "pub": "11:16 2026年7月28日",
        "zh_title": "泽连斯基赴华盛顿会晤特朗普 乌伊战局交织",
        "en_title": "Zelenskyy heads to White House talks with Trump",
        "zh_sum": "半岛电视台称泽连斯基将出席格雷厄姆葬礼并与特朗普会面，乌克兰战争与中东冲突在制裁与军援议题上相互牵动。",
        "en_sum": "Al Jazeera said Zelenskyy will meet Trump after Senator Graham's funeral as Ukraine and Middle East wars converge on sanctions and aid debates.",
        "src_zh": "半岛电视台",
        "src_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/7/28/ukraines-zelenskyy-set-to-meet-trump-as-iran-and-ukraine-wars-converge",
        "tag": "#1abc9c",
    },
    {
        "cat": "world",
        "pub": "16:41 2026年7月28日",
        "zh_title": "美国代表团在安理会法国发言时离场抗议",
        "en_title": "US walks out of UN meeting during France remarks",
        "zh_sum": "BBC称美方抗议法国将华盛顿与人权投票立场同威权国家类比，争端源于联合国人权高专连任表决分歧。",
        "en_sum": "The BBC said the US delegation left a Security Council session to protest French criticism of Washington's human rights votes on the UN rights chief's renewal.",
        "src_zh": "BBC",
        "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c87nj3w9gxjo",
        "tag": "#192f6a",
    },
    {
        "cat": "world",
        "pub": "05:28 2026年7月28日",
        "zh_title": "民调显示仅三分之一美国人支持对伊战争",
        "en_title": "Poll finds only one in three Americans back Iran war",
        "zh_sum": "路透/益普索调查显示69%受访者认为特朗普未清楚说明战争目标，支持率降至冲突以来低位。",
        "en_sum": "A Reuters/Ipsos poll found just one in three Americans support the Iran war while 69% say Trump has not clearly explained US goals.",
        "src_zh": "Daily Sabah / 路透",
        "src_en": "Daily Sabah / Reuters",
        "url": "https://www.dailysabah.com/world/americas/support-for-iran-war-sinks-as-doubts-over-trump-grow-poll",
        "tag": "#c0392b",
    },
    {
        "cat": "world",
        "pub": "14:59 2026年7月28日",
        "zh_title": "伊朗与沙特、阿曼磋商霍尔木兹海峡安全",
        "en_title": "Iran holds Hormuz talks with Saudi Arabia and Oman",
        "zh_sum": "CNBC称德黑兰外长与沙、阿同行通话，强调恢复海峡稳定；特朗普称谈判友好但警告失败将恢复打击。",
        "en_sum": "CNBC said Iran's foreign minister spoke with Saudi and Omani counterparts on Hormuz stability as Trump hailed talks but warned strikes could resume.",
        "src_zh": "CNBC",
        "src_en": "CNBC",
        "url": "https://www.cnbc.com/2026/07/28/us-iran-war-trump-hormuz.html",
        "tag": "#27ae60",
    },
    {
        "cat": "world",
        "pub": "13:47 2026年7月28日",
        "zh_title": "波尔多特大野火夜间趋稳 高温再成考验",
        "en_title": "Bordeaux megafire stable but heat wave looms",
        "zh_sum": "France24引当地当局称吉伦特省4.2万公顷火场周二早晨仍稳定，但气温回升与风向变化或再度激化火势。",
        "en_sum": "France 24 cited authorities saying the 42,000-hectare Gironde blaze was stable Tuesday morning as rising heat and winds threatened renewed spread.",
        "src_zh": "France 24",
        "src_en": "France 24",
        "url": "https://www.france24.com/en/europe/20260728-live-massive-wildfires-near-bordeaux-still-under-control-after-calm-night-local-authorities-say",
        "tag": "#2e86de",
    },
    # 香港
    {
        "cat": "hk",
        "pub": "13:33 2026年7月28日",
        "zh_title": "李家超：补选失仪议员席位非当前优先",
        "en_title": "John Lee signals by-election for vacated seat unlikely",
        "zh_sum": "南华早报引述特首称未来18个月三项重要选举优先，填补醉驾辞职议员议席的补选必要性较低。",
        "en_sum": "The SCMP quoted Lee saying three major polls over 18 months take priority over a by-election to replace a lawmaker who resigned after a drink-driving case.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/politics/article/3362089/holding-election-replace-disgraced-lawmaker-low-priority-john-lee-says",
        "tag": "#e74c3c",
    },
    {
        "cat": "hk",
        "pub": "08:55 2026年7月28日",
        "zh_title": "天文台清晨发出黄色暴雨警告信号",
        "en_title": "Amber rainstorm warning issued in Hong Kong",
        "zh_sum": "南华早报报道，天文台7时15分发黄色雨暴警告，未来数日华南沿岸低压槽带来持续不稳定天气。",
        "en_sum": "The SCMP said the Observatory issued an amber rain alert at 7:15am as a trough will keep southern China weather unsettled for days.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362054/amber-rainstorm-warning-issued-hong-kong-tuesday-morning",
        "tag": "#e74c3c",
    },
    {
        "cat": "hk",
        "pub": "14:49 2026年7月28日",
        "zh_title": "补习社老板性侵五男童判囚六年四个月",
        "en_title": "Tutorial centre owner jailed for assaulting five boys",
        "zh_sum": "高等法院判处美孚补习社前负责人逾六年监禁，其被指在处所猥亵七至14岁学童并拍摄部分过程。",
        "en_sum": "The High Court jailed a former Mei Foo tutorial centre owner for over six years for indecent assaults on five boys aged seven to 14, including filming some acts.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362101/nearly-6-1/2-years-jail-owner-hong-kong-tutorial-centre-who-molested-5-boys",
        "tag": "#e74c3c",
    },
    {
        "cat": "hk",
        "pub": "12:34 2026年7月28日",
        "zh_title": "罗淑佩：盛事经济可带动本地消费",
        "en_title": "Tourism chief says mega events can boost spending",
        "zh_sum": "香港电台引述局长指启德商场首五月销售额升四成，月底起持盛事门票可在逾百商户享额外折扣。",
        "en_sum": "RTHK quoted Rosanna Law saying Kai Tak Mall sales rose 40% in five months and ticket holders will get extra discounts at over 100 outlets from July 31.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1864037-20260728.htm",
        "tag": "#16a085",
    },
    # 其他
    {
        "cat": "other",
        "pub": "14:05 2026年7月28日",
        "zh_title": "强生提议55亿美元和解滑石粉诉讼",
        "en_title": "Johnson & Johnson offers $5.5bn talc settlement",
        "zh_sum": "香港电台援引公司称方案涵盖约7.6万起致癌索赔，否认产品致癌但寻求结束多年法律纠缠。",
        "en_sum": "RTHK cited J&J's $5.5 billion proposal to settle about 76,000 cancer claims over talc products while denying the science behind the allegations.",
        "src_zh": "香港电台 / 法新社",
        "src_en": "RTHK / AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1864047-20260728.htm",
        "tag": "#16a085",
    },
    {
        "cat": "other",
        "pub": "13:49 2026年7月28日",
        "zh_title": "比亚迪东京发布首款日本专属轻型电动车",
        "en_title": "BYD launches Japan-only electric kei car Racco",
        "zh_sum": "日经亚洲称Racco售价约215万日元起，续航最高320公里，直面本土主导的轻型车市场但补贴劣势仍存。",
        "en_sum": "Nikkei Asia said BYD's Racco kei EV starts at about 2.15 million yen with up to 320km range, challenging Japan's domestic minicar stronghold.",
        "src_zh": "日经亚洲",
        "src_en": "Nikkei Asia",
        "url": "https://asia.nikkei.com/business/automobiles/byd-launches-its-first-japan-electric-minicar-challenging-local-stronghold",
        "tag": "#d35400",
    },
]


def item_html(n: int, it: dict) -> str:
    zh = escape(it["zh_title"])
    en = escape(it["en_title"])
    url = escape(it["url"], quote=True)
    pub = escape(it["pub"])
    return f"""
<tr><td style="padding:0 0 22px 0;">
<table width="100%" cellpadding="0" cellspacing="0" style="border-bottom:1px solid #eee;">
<tr><td style="padding-bottom:14px;">
<span style="display:inline-block;background:#2563eb;color:#fff;font-weight:700;font-size:12px;padding:4px 10px;border-radius:4px;margin-right:8px;">{n:02d}</span>
<a href="{url}" style="color:#1a1a1a;font-size:17px;font-weight:700;text-decoration:none;line-height:1.4;">{zh}</a>
<div style="margin-top:6px;font-size:15px;color:#555;font-style:italic;line-height:1.4;"><a href="{url}" style="color:#555;text-decoration:none;">{en}</a></div>
<div style="margin-top:6px;font-size:12px;color:#888;">发布时间 Published: {pub}</div>
<p style="margin:10px 0 6px;font-size:14px;color:#333;line-height:1.6;">{escape(it['zh_sum'])}</p>
<p style="margin:0 0 10px;font-size:13px;color:#555;line-height:1.55;">{escape(it['en_sum'])}</p>
<span style="display:inline-block;background:{it['tag']};color:#fff;font-size:11px;padding:3px 8px;border-radius:3px;">{escape(it['src_zh'])} / {escape(it['src_en'])}</span>
<a href="{url}" style="margin-left:10px;font-size:13px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</td></tr>
</table>
</td></tr>"""


def build_html() -> str:
    n = len(ITEMS)
    body_parts = []
    idx = 1
    for cat_id, zh_cat, en_cat in CATEGORIES:
        cat_items = [it for it in ITEMS if it["cat"] == cat_id]
        if not cat_items:
            continue
        rows = "".join(item_html(idx + i, it) for i, it in enumerate(cat_items))
        idx += len(cat_items)
        body_parts.append(
            f"""
<tr><td style="padding:18px 20px 8px;">
<h2 style="margin:0;font-size:16px;color:#1e293b;background:#f1f5f9;padding:10px 12px;border-left:4px solid #2563eb;border-radius:0 6px 6px 0;">{zh_cat} · <span style="font-weight:500;color:#475569;">{en_cat}</span></h2>
</td></tr>
<tr><td style="padding:0 20px 6px;">{rows}</td></tr>"""
        )

    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/></head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#eef1f5;padding:24px 12px;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">
<tr><td style="background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%);padding:28px 24px;color:#fff;">
<div style="font-size:26px;font-weight:800;letter-spacing:.5px;">每日热点晚报</div>
<div style="font-size:14px;margin-top:8px;opacity:.92;">Evening News Briefing · {DATE_DISPLAY} · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0;">
<p style="margin:0 0 8px;font-size:14px;color:#334155;line-height:1.6;">以下为今日全日要闻精选，涵盖盘中市场、政策动向与全球热点。</p>
<p style="margin:0;font-size:13px;color:#64748b;line-height:1.55;">Today's main stories: markets, policy moves, and global developments through the day.</p>
</td></tr>
{''.join(body_parts)}
<tr><td style="padding:20px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:11px;color:#94a3b8;line-height:1.6;">
<p style="margin:0 0 6px;">本简报仅供参考，不构成投资或法律建议。链接内容版权归原媒体所有。</p>
<p style="margin:0;">For informational purposes only; not investment or legal advice. © respective publishers.</p>
</td></tr>
</table></td></tr></table></body></html>"""


def main():
    root = os.path.join(os.path.dirname(__file__), "..")
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE_ISO}",
        "htmlContent": build_html(),
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {path}, {len(ITEMS)} items, {len(payload['htmlContent'])} chars")


if __name__ == "__main__":
    main()
