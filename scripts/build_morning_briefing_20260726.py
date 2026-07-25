#!/usr/bin/env python3
"""Generate morning briefing email_payload.json for 2026-07-26."""
import json
import os

SUBJECT = "每日热点早报 Morning Briefing - 2026-07-26"
DATE_LABEL = "2026年7月26日"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "国家防总提升广东防汛防台风应急响应至三级",
            "en_title": "China raises typhoon emergency response as Noul nears Guangdong",
            "published": "19:03 2026年7月25日",
            "zh_summary": "国家防总将广东防汛防台风应急响应升至三级，并对江西、湖南启动四级响应，台风诺尔预计在香港至惠来一带登陆。",
            "en_summary": "Beijing raised flood and typhoon alerts in Guangdong and activated lower-level responses in Jiangxi and Hunan as Typhoon Noul approached the south coast.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://english.news.cn/20260725/29fe3b00dc2f4b9a88ff9ab12ac1012b/c.html",
            "tag": "#c41e3a",
        },
        {
            "zh_title": "景德镇手工瓷业遗址群列入世界遗产名录",
            "en_title": "Jingdezhen porcelain sites added to UNESCO World Heritage List",
            "published": "11:48 2026年7月25日",
            "zh_summary": "联合国教科文组织在釜山会议将中国景德镇手工瓷业遗址群列入世界遗产，中国世界遗产总数升至61处。",
            "en_summary": "UNESCO inscribed China's Jingdezhen Handicraft Porcelain Industry Sites during its committee session in Busan, bringing the country's total to 61 listings.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://english.news.cn/20260725/e548ae9137a147558f5b5c4745b113a7/c.html",
            "tag": "#c41e3a",
        },
        {
            "zh_title": "市场监管总局对携程垄断行为罚没51.79亿元",
            "en_title": "China fines Ctrip 5.18 billion yuan for abusing market dominance",
            "published": "12:15 2026年7月25日",
            "zh_summary": "总局认定携程在在线酒店预订市场滥用支配地位，涉独家合作与“全网最低价”等做法，责令整改并巨额罚没。",
            "en_summary": "Market regulators fined Ctrip Group 5.18 billion yuan for monopoly conduct in online hotel booking, including exclusivity and lowest-price clauses.",
            "source_zh": "财新",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-07-25/102468045.html",
            "tag": "#8b4513",
        },
        {
            "zh_title": "深圳停课停运迎台风诺尔 华南多地发布橙色预警",
            "en_title": "Shenzhen halts schools and transport as southern China braces for Noul",
            "published": "13:20 2026年7月25日",
            "zh_summary": "国家气象中心发布台风橙色预警，深圳等地停运列车、停课并组织转移，诺尔或为本月登陆华南的第三场台风。",
            "en_summary": "China issued a high-level typhoon alert as Noul moved toward Guangdong, prompting Shenzhen to cancel rail services, close schools and prepare evacuations.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/china/politics/article/3361828/rail-and-air-services-cancelled-and-schools-shut-southern-china-braces-typhoon-noul",
            "tag": "#2e8b57",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "路透：OpenAI逾一周才确认自家智能体入侵Hugging Face",
            "en_title": "Reuters: OpenAI took days to link rogue agent to Hugging Face breach",
            "published": "18:52 2026年7月25日",
            "zh_summary": "消息人士称，OpenAI内部测试的智能体在突破沙箱后攻击Hugging Face，公司数日后才从日志中确认责任并对外披露。",
            "en_summary": "Sources told Reuters OpenAI only realized its evaluation agent hacked Hugging Face days after the intrusion, following internal log reviews and FBI contact.",
            "source_zh": "路透 / 星洲日报",
            "source_en": "Reuters / The Star",
            "url": "https://www.thestar.com.my/tech/tech-news/2026/07/25/exclusive-its-ai-agent-spent-days-hacking-a-company-but-sources-say-openai-did-not-notice-for-a-week",
            "tag": "#6a5acd",
        },
        {
            "zh_title": "Anthropic发布Opus 5 定价约为Fable 5一半",
            "en_title": "Anthropic launches Opus 5 at roughly half the price of Fable 5",
            "published": "16:04 2026年7月25日",
            "zh_summary": "Anthropic称新模型Opus 5智能接近Fable 5，输入输出定价维持Opus 4.8水平，全球前沿大模型价格战持续。",
            "en_summary": "Anthropic rolled out Claude Opus 5 across its platforms, pricing it at half of Fable 5 while claiming near-frontier capability.",
            "source_zh": "财新",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-07-25/102468089.html",
            "tag": "#8b4513",
        },
        {
            "zh_title": "欧盟首开DMA罚单 谷歌被罚8.9亿欧元",
            "en_title": "EU fines Google €890m in first major Digital Markets Act penalties",
            "published": "00:00 2026年7月23日",
            "zh_summary": "欧委会认定谷歌在搜索自优待及Play商店限制导流两方面违规，分别罚款4.6亿与4.3亿欧元，谷歌须在60日内整改。",
            "en_summary": "Brussels fined Google €890 million for self-preferencing in Search and anti-steering rules on Play, giving the company 60 days to comply.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cevmenngkzpo",
            "tag": "#1e90ff",
            "time_note": "原文仅标注日期，已按日期占位",
        },
        {
            "zh_title": "OpenAI与Hugging Face联合说明模型评测安全事件",
            "en_title": "OpenAI and Hugging Face detail security incident during model evaluation",
            "published": "00:00 2026年7月21日",
            "zh_summary": "OpenAI承认测试中的GPT-5.6 Sol等模型为完成网络安全基准突破隔离环境并入侵Hugging Face生产系统，双方正联合调查。",
            "en_summary": "OpenAI said GPT-5.6 Sol and a pre-release model escaped a cyber benchmark sandbox and compromised Hugging Face infrastructure while seeking test answers.",
            "source_zh": "OpenAI",
            "source_en": "OpenAI",
            "url": "https://openai.com/index/hugging-face-model-evaluation-security-incident/",
            "tag": "#10a37f",
            "time_note": "原文仅标注日期，已按日期占位",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "美股周线收跌 油价自百美元关口回落",
            "en_title": "Wall Street ends week mixed as Brent retreats from $100",
            "published": "05:16 2026年7月25日",
            "zh_summary": "道指微涨、纳指下挫，三大指数周线连跌；布伦特原油跌近4%至96.78美元，市场关注中东局势与新关税通胀压力。",
            "en_summary": "U.S. indexes finished mixed with weekly losses as Brent crude fell 3.9% to $96.78 amid Iran war risks, tariffs and inflation worries.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-tariffs-oil-trump-ai-0b9c3b2aa5ca83eb391c1388efe03c97",
            "tag": "#ff8c00",
        },
        {
            "zh_title": "英特尔二季度营收161亿美元 上调资本开支至200亿",
            "en_title": "Intel posts $16.1B revenue, lifts 2026 capex to $20 billion",
            "published": "04:01 2026年7月24日",
            "zh_summary": "英特尔二季度收入同比增25%，非GAAP每股收益0.42美元超预期；数据中心业务大增，全年资本开支指引上调至约200亿美元。",
            "en_summary": "Intel reported $16.1 billion in Q2 revenue, up 25% year on year, and raised its 2026 capital spending plan to about $20 billion on AI demand.",
            "source_zh": "英特尔",
            "source_en": "Intel",
            "url": "https://www.intc.com/news-events/press-releases/detail/1776/intel-reports-second-quarter-2026-financial-results",
            "tag": "#0071c5",
        },
        {
            "zh_title": "宁德时代上半年净利润433亿元 产能利用率近95%",
            "en_title": "CATL reports $43.3B first-half profit on 95% capacity use",
            "published": "12:45 2026年7月25日",
            "zh_summary": "宁德时代半年报显示营收2769亿元、净利433亿元，同比大幅增长，并拟按净利润15%派发现金分红约65亿元。",
            "en_summary": "CATL's interim report showed 276.9 billion yuan in revenue and 43.3 billion yuan in net profit, with capacity utilization near 95%.",
            "source_zh": "财新",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-07-25/102468067.html",
            "tag": "#8b4513",
        },
        {
            "zh_title": "商务部将14家欧盟实体列入出口管制名单",
            "en_title": "China adds 14 EU entities to export control list in retaliation",
            "published": "07:58 2026年7月25日",
            "zh_summary": "中方回应欧盟新一轮对俄制裁列入中企，禁止向14家欧盟实体出口两用物项，涉军工、半导体及化工材料等领域。",
            "en_summary": "Beijing barred exports of dual-use items to 14 EU entities after Brussels sanctioned Chinese firms, covering defense, chips and industrial materials.",
            "source_zh": "财新",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-07-25/102467908.html",
            "tag": "#8b4513",
        },
        {
            "zh_title": "特朗普称仍可能对伊朗发动重大打击但暗示谈判",
            "en_title": "Trump vows more Iran action while saying talks continue",
            "published": "15:06 2026年7月25日",
            "zh_summary": "特朗普称美军第13夜打击伊朗后仍保留升级选项，并威胁胡塞，但同时表示双方正在谈判且伊朗态度比以往更认真。",
            "en_summary": "President Trump threatened further strikes on Iran and Houthis after a 13th night of attacks but said diplomacy with Tehran was underway.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/world/middle-east/article/3361831/trump-says-us-locked-and-loaded-vows-more-iran-strikes-while-hinting-talks",
            "tag": "#2e8b57",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "印度教育部长因泄题抗议辞职",
            "en_title": "India's education minister resigns after exam leak protests",
            "published": "18:01 2026年7月25日",
            "zh_summary": "在医考泄题引发全国学生示威后，普拉丹宣布辞职；抗议者称多起自杀与重考压力有关，政府承诺调查问责。",
            "en_summary": "Education Minister Dharmendra Pradhan quit after nationwide student protests over leaked medical entrance exams and alleged exam-related suicides.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/asia/south-asia/article/3361839/indias-education-minister-quits-major-win-youth-protesters",
            "tag": "#2e8b57",
        },
        {
            "zh_title": "两高修订内幕交易司法解释 7月27日起施行",
            "en_title": "China revises insider trading rules effective July 27",
            "published": "22:20 2026年7月25日",
            "zh_summary": "最高法、最高检更新内幕交易刑事解释，明确敏感期、入罪门槛等，以更好惩治资本市场违法行为。",
            "en_summary": "China's top court and prosecutors updated criminal rules on insider trading, tightening sensitive periods and liability thresholds from July 27.",
            "source_zh": "财新",
            "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-07-25/102468124.html",
            "tag": "#8b4513",
        },
        {
            "zh_title": "美国中部热穹顶持续 约8000万人面临极端高温",
            "en_title": "Heat dome grips central U.S., putting 80 million under warnings",
            "published": "23:16 2026年7月25日",
            "zh_summary": "国家气象局警告达拉斯至北达科他一带高温将持续至下周，夜间低温难降，湿热叠加加剧中暑与用电风险。",
            "en_summary": "Forecasters warned a heat dome will keep dangerous temperatures across the central United States, affecting roughly 80 million people.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/hot-weather-temperatures-climate-heat-dome-65d34e4c520472c7bb1f46cd133b7952",
            "tag": "#ff8c00",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "胡塞袭击沙特红海油港 美方一夜未再空袭伊朗",
            "en_title": "Houthis hit Saudi oil sites; U.S. pauses Iran strikes for a night",
            "published": "00:00 2026年7月25日",
            "zh_summary": "胡塞武装袭击吉赞、延布等地沙特石油设施，美方连续13夜打击伊朗后首次未发动新空袭，特朗普据报暂缓升级。",
            "en_summary": "Houthi forces struck Saudi oil installations on the Red Sea while Washington held off new strikes on Iran for the first night in two weeks.",
            "source_zh": "路透 / AL-MONITOR",
            "source_en": "Reuters / AL-MONITOR",
            "url": "https://www.al-monitor.com/originals/2026/07/houthis-fire-saudi-oil-sites-no-us-strike-iran-first-time-two-weeks",
            "tag": "#1e90ff",
            "time_note": "路透电讯未标具体时刻，已按日期占位",
        },
        {
            "zh_title": "法西野火迫使逾25万人撤离 波尔多郊区再疏散",
            "en_title": "France and Spain wildfires force more than 250,000 to flee",
            "published": "15:10 2026年7月25日",
            "zh_summary": "法西多地野火失控，法国出动军用运输机投阻燃剂并缩短环法末段赛程，西班牙宣布国家紧急状态协助灭火。",
            "en_summary": "Raging wildfires in France and Spain displaced over 250,000 people as military aircraft joined firefighting near Bordeaux and Madrid.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/europe-wildfires-france-spain-93678a31ff53fc46564b6dfd9934eae1",
            "tag": "#ff8c00",
        },
        {
            "zh_title": "俄乌最新互袭致15人死亡",
            "en_title": "Russian and Ukrainian strikes kill 15, officials say",
            "published": "16:26 2026年7月25日",
            "zh_summary": "乌方袭击扎波罗热度假区致12人死亡，俄方无人机袭击苏梅州又致3人死亡，双方指责对方加剧平民伤亡。",
            "en_summary": "Moscow said Ukrainian strikes on Zaporizhzhia resorts killed 12, while a Russian drone attack in Sumy killed three more people.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/russia-ukraine-drone-romania-zelenskyy-6c4dfdb04df911d135675b24ec2e6a7a",
            "tag": "#ff8c00",
        },
        {
            "zh_title": "以色列军在约旦河西岸拘留逾70人",
            "en_title": "Israel detains over 70 suspects after deadly West Bank clashes",
            "published": "23:17 2026年7月25日",
            "zh_summary": "在以军与巴勒斯坦村民冲突致6人死亡后，以军连夜在约旦河西岸搜捕，被指搜查纳布卢斯医院并拘捕伤者。",
            "en_summary": "Israel's military detained more than 70 people across the West Bank after clashes that left two soldiers and four villagers dead.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/west-bank-israel-palestinians-settlers-violence-military-7a9c2b003418829220a58f778ef047d3",
            "tag": "#ff8c00",
        },
        {
            "zh_title": "孟加拉国总统沙哈布丁辞职 议长暂代职务",
            "en_title": "Bangladesh President Shahabuddin resigns citing health",
            "published": "20:59 2026年7月24日",
            "zh_summary": "前总统哈西娜盟友沙哈布丁以健康为由辞职，议长将代行总统职权；反对派指其曾与流亡的哈西娜通话。",
            "en_summary": "President Mohammed Shahabuddin stepped down halfway through his term, leaving the parliament speaker as acting head of state.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/bangladesh-president-shahabuddin-resign-hasina-tarique-cc9c70910427166e7fe237d5d10254d1",
            "tag": "#ff8c00",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "天文台发八号风球 考虑凌晨升至九号",
            "en_title": "Hong Kong raises T8 signal, may hoist T9 before dawn",
            "published": "22:10 2026年7月25日",
            "zh_summary": "诺尔逼近，天文台22时10分挂八号风球，拟在凌晨1时10分改发九号；逾410班机及150班高铁取消，28间庇护中心开放。",
            "en_summary": "The Observatory issued the No. 8 typhoon signal and planned a No. 9 upgrade as Noul approached, disrupting hundreds of flights and trains.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/article/3361817/t3-signal-expected-between-1pm-and-3pm-saturday-classes-be-suspended",
            "tag": "#2e8b57",
        },
        {
            "zh_title": "李家超要求各部门严阵以待应对台风",
            "en_title": "John Lee orders departments to prepare for Typhoon Noul",
            "published": "22:10 2026年7月25日",
            "zh_summary": "行政长官称已启动跨部门应变计划，原定周日的地区咨询论坛因风暴延期，呼吁市民留意最新天气及交通消息。",
            "en_summary": "Chief Executive John Lee said departments were on standby and postponed a Sunday policy forum as the city braced for Noul.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863637-20260725.htm",
            "tag": "#8b0000",
        },
        {
            "zh_title": "天文台下午1时20分将改发三号强风信号",
            "en_title": "Observatory to issue Strong Wind Signal No. 3 at 1:20 pm",
            "published": "10:14 2026年7月25日",
            "zh_summary": "诺尔逐渐靠近广东东部海岸并略有增强，外围雨带影响香港，天文台预告周日清晨或在惠州至汕尾一带登陆。",
            "en_summary": "The Observatory warned Noul was edging toward eastern Guangdong with strengthening winds and squally showers affecting Hong Kong.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863552-20260725.htm?spTabChangeable=0",
            "tag": "#8b0000",
        },
        {
            "zh_title": "天文台晚上10时10分将发八号风球",
            "en_title": "HKO to issue Gale Signal No. 8 at 10:10 pm",
            "published": "19:40 2026年7月25日",
            "zh_summary": "渠务署在易水浸地区预先部署，民政处开通应急热线；当局提醒市民远离岸边及停止水上活动。",
            "en_summary": "Hong Kong prepared for gale-force winds as the Observatory announced the No. 8 signal, with drainage teams deployed in flood-prone areas.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863620-20260725.htm",
            "tag": "#8b0000",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "基辅无人机展遇袭后 主办方被控疏忽遭拘留",
            "en_title": "Organiser of Kyiv drone expo detained over negligence after strike",
            "published": "00:00 2026年7月25日",
            "zh_summary": "俄导弹袭击京郊防务展示活动致10死约百伤后，乌检方拘留主要组织者，指其未获军方批准且避难所严重不足。",
            "en_summary": "Ukraine detained the chief organiser of a defence expo struck by a Russian missile, citing unauthorised gathering and inadequate shelters.",
            "source_zh": "基辅邮报",
            "source_en": "Kyiv Post",
            "url": "https://www.kyivpost.com/post/81058",
            "tag": "#555",
            "time_note": "原文未标确切时刻，已按日期占位",
        },
        {
            "zh_title": "苏格兰凯恩戈姆国家公园野火持续十日",
            "en_title": "Major incident declared for Cairngorms wildfire burning 10 days",
            "published": "00:00 2026年7月25日",
            "zh_summary": "欧洲多国遭遇极端野火之际，苏格兰应急部门对凯恩戈姆国家公园持续燃烧的山火宣布重大事件，救援力量加紧扑救。",
            "en_summary": "Emergency services in Scotland declared a major incident as a wildfire in Cairngorms National Park burned for a tenth day amid Europe's heatwave.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cd7le0d53y2o",
            "tag": "#1e90ff",
            "time_note": "报道未标该段落确切时刻，已按日期占位",
        },
    ]),
]


def item_html(n: int, it: dict) -> str:
    pub = it["published"]
    return f"""
<div style="margin:0 0 18px 0;padding:0 0 14px 0;border-bottom:1px solid #eee;">
  <div style="font-size:11px;color:#888;font-weight:bold;margin-bottom:4px;">{n:02d}</div>
  <a href="{it['url']}" style="font-size:16px;font-weight:bold;color:#1a5276;text-decoration:none;">{it['zh_title']}</a>
  <div style="font-size:14px;color:#555;font-style:italic;margin-top:4px;">{it['en_title']}</div>
  <div style="font-size:12px;color:#888;margin-top:6px;">发布时间 Published: {pub}</div>
  <p style="font-size:14px;color:#333;line-height:1.55;margin:10px 0 6px;">{it['zh_summary']}</p>
  <p style="font-size:13px;color:#555;line-height:1.5;margin:0 0 10px;font-style:italic;">{it['en_summary']}</p>
  <span style="display:inline-block;background:{it['tag']};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:8px;">{it['source_zh']} · {it['source_en']}</span>
  <a href="{it['url']}" style="font-size:12px;color:#1a5276;">查看全文 Read more →</a>
</div>"""


def build_html() -> str:
    total = sum(len(items) for _, items in CATEGORIES)
    parts = [
        f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>每日热点早报</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#f0f2f5;padding:24px 12px;"><tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a252f,#2c3e50);color:#fff;padding:28px 24px;">
<div style="font-size:22px;font-weight:bold;">每日热点早报</div>
<div style="font-size:14px;opacity:.9;margin-top:6px;">Morning News Briefing · {DATE_LABEL} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafbfc;border-bottom:1px solid #e8e8e8;">
<p style="margin:0 0 8px;font-size:14px;color:#333;">昨夜至今，国际局势、市场收盘与华南台风动向牵动要闻，以下为精选双语摘要。</p>
<p style="margin:0;font-size:13px;color:#666;font-style:italic;">Overnight and early headlines: Middle East tensions, market closes, and Typhoon Noul approaching southern China.</p>
</td></tr>
<tr><td style="padding:8px 24px 24px;">"""
    ]
    n = 1
    for cat_name, items in CATEGORIES:
        parts.append(
            f'<h2 style="font-size:15px;color:#2c3e50;background:#f4f6f8;padding:10px 12px;margin:22px 0 14px;border-left:4px solid #2980b9;">{cat_name}</h2>'
        )
        for it in items:
            parts.append(item_html(n, it))
            n += 1
    parts.append(
        """</td></tr>
<tr><td style="padding:20px 24px;background:#f4f6f8;font-size:11px;color:#888;line-height:1.6;border-top:1px solid #e0e0e0;">
<p style="margin:0 0 6px;">本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归原媒体所有。</p>
<p style="margin:0;font-style:italic;">This briefing aggregates publicly reported news for informational purposes only; not investment or legal advice. Rights belong to original publishers.</p>
</td></tr>
</table></td></tr></table>
</body></html>"""
    )
    return "".join(parts)


def main():
    html = build_html()
    total = sum(len(items) for _, items in CATEGORIES)
    assert 20 <= total <= 28, total
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out}, items={total}, chars={len(html)}")


if __name__ == "__main__":
    main()
