#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-11."""
import json
import os

BRIEFING_EDITION = "早报"
LOCAL_TIME = "2026-08-11 07:31 CST"
DATE_SUBJECT = "2026-08-11"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "cn_title": "台风「白海豚」余波：华东逾百万人撤离，上海近千人航班取消",
            "en_title": "Typhoon Dolphin aftermath: 1 million evacuated in east China, Shanghai cancels nearly 1,000 flights",
            "published": "09:44 2026年8月10日",
            "cn_summary": "今年最强台风登陆浙江后减弱为热带风暴，华东多地持续暴雨洪涝与山体滑坡风险，上海等地航班大面积取消。",
            "en_summary": "After China's strongest typhoon of 2026 made landfall in Zhejiang, heavy rain, flooding and landslide risks persist as Shanghai cancelled nearly 1,000 flights.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cx2rgzyplg2o",
        },
        {
            "cn_title": "BBC调查：「闪婚」骗局席卷中国，单身男性被骗数十万彩礼",
            "en_title": "BBC: 'Flash marriage' scams target lonely Chinese men, draining life savings",
            "published": "06:02 2026年8月11日",
            "cn_summary": "婚介机构以快速成婚为诱饵，全国已查处逾1500人；北京本月启动专项整治，受害者追讨彩礼与中介费艰难。",
            "en_summary": "Matchmaking agencies lure men into quick marriages then disappear; prosecutors handled 1,546 related cases as Beijing launched a nationwide crackdown.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cn9n8pqglg4o",
        },
        {
            "cn_title": "中国7月CPI同比涨0.5%、PPI涨3.5%，物价温和但PPI高位回落",
            "en_title": "China's July CPI up 0.5% and PPI up 3.5% as factory-price gains ease",
            "published": "16:10 2026年8月9日",
            "cn_summary": "国家统计局称核心CPI同比0.9%；汽油涨幅回落拖累CPI，PPI环比降0.7%，输入性与季节性因素压制工业品价格。",
            "en_summary": "NBS data showed core CPI at 0.9% y/y; lower gasoline gains weighed on CPI while PPI fell 0.7% m/m amid input and seasonal pressures.",
            "source_cn": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/fortune/20260809/556afc7add514939b371fb1cc6d9fa30/c.html",
        },
        {
            "cn_title": "财新：7月CPI、PPI同比均低于预期，PPI结束一年持续改善态势",
            "en_title": "Caixin: July CPI and PPI both below forecasts as PPI momentum stalls",
            "published": "11:34 2026年8月9日",
            "cn_summary": "国际油价走弱拖累CPI环比连降三月；PPI同比结束持续改善，生产资料环比降幅扩大，供强需弱格局延续。",
            "en_summary": "Weaker oil prices dragged CPI lower for a third month; PPI's year-long improvement ended as producer goods prices fell more sharply.",
            "source_cn": "财新",
            "source_en": "Caixin",
            "url": "https://economy.caixin.com/2026-08-09/102472709.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "cn_title": "英伟达联手华尔街六大机构筹资5000亿美元建设AI基础设施",
            "en_title": "Nvidia partners with Wall Street giants on $500bn AI infrastructure financing",
            "published": "06:31 2026年8月11日",
            "cn_summary": "与阿波罗、黑石、高盛等签约，首次将AI算力视为独立资产类别，资金用于数据中心、芯片工厂及合作伙伴项目。",
            "en_summary": "Deals with Apollo, Blackstone, Goldman Sachs and others treat AI compute as a new asset class to fund data centres and chip factories.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c78gr0jv0mdo",
        },
        {
            "cn_title": "特朗普签署行政令缩减儿童疫苗至11种，要求拆分MMR联合针",
            "en_title": "Trump signs order cutting routine childhood vaccines to 11 and splitting MMR shots",
            "published": "03:35 2026年8月11日",
            "cn_summary": "白宫称建立「黄金标准」接种建议，儿科协会批评危险；麻疹病例创35年新高背景下，州政府仍掌握校内接种规定权。",
            "en_summary": "The White House unveiled 'gold standard' vaccine guidance as pediatric groups warned of risk amid a 35-year high in US measles cases.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/ce3q5vl581wo",
        },
        {
            "cn_title": "科技巨头鼓吹AI减负，员工称冲刺期每周工作可达90小时",
            "en_title": "Tech leaders tout AI-driven shorter workweeks while staff report 90-hour weeks",
            "published": "13:00 2026年8月10日",
            "cn_summary": "OpenAI、Anthropic员工称高强度冲刺常态化；伯克利研究指AI加快节奏、扩大任务范围，节省的时间被新工作吞噬。",
            "en_summary": "Workers at OpenAI and Anthropic describe grueling sprints; a UC Berkeley study found AI sped tasks but expanded workloads.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvgx4yd1gl2o",
        },
        {
            "cn_title": "剑桥前教授贾森·阿尔迪因抄袭争议辞职并取消公开活动",
            "en_title": "Ex-Cambridge professor Jason Arday cancels events after plagiarism row resignation",
            "published": "20:14 2026年8月10日",
            "cn_summary": "阿尔迪辞去剑桥社会学教授职务并退出地理学会演讲；校方就学历与荣誉任命展开调查，出版商仍按计划发行其回忆录。",
            "en_summary": "Arday resigned his Cambridge post and pulled conference appearances as the university probes his qualifications and honorary roles.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cd7lj3703epo",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "cn_title": "美股周一小幅收跌，霍尔木兹僵局与通胀数据令市场谨慎",
            "en_title": "US stocks edge lower as Hormuz uncertainty and inflation data keep markets cautious",
            "published": "04:10 2026年8月11日",
            "cn_summary": "标普500跌0.06%至7753.11点，纳指跌0.32%；油价上涨约5%，投资者关注本周CPI与PPI数据及中东局势。",
            "en_summary": "The S&P 500 slipped 0.06% to 7,753.11 and the Nasdaq fell 0.32% as oil rose about 5% amid Hormuz and inflation concerns.",
            "source_cn": "CNBC",
            "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/09/stock-market-today-live-updates.html",
        },
        {
            "cn_title": "特朗普拒付伊朗战争赔偿，反要求德黑兰补偿美方伤亡",
            "en_title": "Trump rejects Iran reparations demand and seeks compensation for US casualties",
            "published": "18:48 2026年8月10日",
            "cn_summary": "伊朗要求赔偿并解除制裁才重开霍尔木兹；特朗普称将追讨数十年美军伤亡及伊朗抗议者遇害赔偿，纳入未来谈判。",
            "en_summary": "Tehran tied reopening Hormuz to sanctions relief and war compensation; Trump countered with demands for payments over US casualties.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/iran-us-strait-hormuz-august-10-2026-0bdaae8f1d7b781918e76dca4317c897",
        },
        {
            "cn_title": "美国最大水库米德湖水位创90年来新低，科罗拉多河危机加深",
            "en_title": "Lake Mead hits lowest level in 90 years as Colorado River crisis deepens",
            "published": "22:01 2026年8月8日",
            "cn_summary": "米德湖水位降至1040.4英尺，低于2022年纪录；多年过度用水叠加干旱升温，鲍威尔湖亦处近七十年最低水平。",
            "en_summary": "Lake Mead fell to 1,040.4 feet below its 2022 record as overuse, drought and heat depleted the Colorado River system's reservoirs.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/colorado-river-lake-mead-record-low-fa402842e76ed624f71360f467b2579d",
        },
        {
            "cn_title": "贝索斯领衔财团推进收购利物浦约30%股份谈判",
            "en_title": "Bezos-led consortium advances talks to buy about 30% stake in Liverpool FC",
            "published": "21:29 2026年8月10日",
            "cn_summary": "财团由阿米特·巴蒂亚牵头，含贝索斯与Facebook联合创始人萨维林；芬威体育集团或本周宣布少数股权交易。",
            "en_summary": "Amit Bhatia's group including Jeff Bezos and Eduardo Saverin is nearing a minority stake deal with Fenway Sports Group.",
            "source_cn": "BBC",
            "source_en": "BBC Sport",
            "url": "https://www.bbc.com/sport/football/articles/c5yw98d4edzo",
        },
    ]),
    ("社会 Society", [
        {
            "cn_title": "哥伦比亚7.4级地震致至少111人死亡，全国进入灾难状态",
            "en_title": "Colombia's 7.4 magnitude quake kills at least 111 as national disaster declared",
            "published": "21:09 2026年8月10日",
            "cn_summary": "震中位于乔科省，卡利、佩雷拉等地建筑倒塌，逾1600栋受损；新总统德拉斯普里埃利亚宣布紧急状态并赴灾区。",
            "en_summary": "The quake struck western Colombia with at least 111 dead and 1,600 buildings damaged; President de la Espriella declared an emergency.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/colombia-ecuador-earthquake-26fd40f93272d834fced47a4a673edc9",
        },
        {
            "cn_title": "英格兰逾七成地区进入干旱，4500万人受影响",
            "en_title": "More than two-thirds of England now in drought affecting 45 million people",
            "published": "15:18 2026年8月10日",
            "cn_summary": "7月为1836年以来最干七月；东米德兰、肯特等地新入干旱，2700万人面临用水限制，本周或迎第五波热浪。",
            "en_summary": "July was England's driest since 1836; new drought zones leave 27 million under water restrictions as a fifth heatwave looms.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c70gk2dl5jyo",
        },
        {
            "cn_title": "加拿大BC省山火致逾2万人撤离，疏散民众忧心家园损毁",
            "en_title": "BC wildfire forces 20,000 evacuations as residents fear homes lost",
            "published": "00:10 2026年8月11日",
            "cn_summary": "秃岭山火周末迅速扩大至136平方公里，萨默兰等地疏散；一名80岁妇女遇难，省府宣布紧急状态。",
            "en_summary": "The Bald Range fire grew to 136 sq km forcing mass evacuations in Summerland; an 80-year-old woman died as BC declared an emergency.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cx2lwv032j9o",
        },
        {
            "cn_title": "图帕克谋杀案嫌疑人三十年后将出庭受审，陪审团遴选开始",
            "en_title": "Suspect in Tupac murder to stand trial 30 years on as jury selection begins",
            "published": "00:52 2026年8月11日",
            "cn_summary": "前帮派头目杜安·戴维斯被控策划1996年枪击，关键证据为其自著回忆录；开庭陈述定于8月17日，或传唤苏格·奈特等人。",
            "en_summary": "Duane 'Keffe D' Davis faces trial for allegedly orchestrating the 1996 shooting; prosecutors cite his memoir as key evidence.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cgmkl1j3dwvo",
        },
    ]),
    ("国际 World", [
        {
            "cn_title": "哥伦比亚强震为本世纪最强，佩雷拉等地数十栋建筑坍塌",
            "en_title": "Colombia quake is strongest this century as buildings collapse in Pereira",
            "published": "21:54 2026年8月10日",
            "cn_summary": "7.4级深源地震在咖啡产区造成严重破坏，佩雷拉至少40人死亡；多国承诺援助，美方将提供1550万美元紧急救援。",
            "en_summary": "The 7.4 deep quake devastated Pereira and Cali; world leaders pledged aid as the US offered $15.5 million in emergency support.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c20e360lx0vo",
        },
        {
            "cn_title": "创纪录230人挤乘一艘小艇横渡英吉利海峡",
            "en_title": "Record 230 people cross English Channel in one small boat",
            "published": "17:43 2026年8月10日",
            "cn_summary": "凌晨2时30分抵达多佛，打破7月165人纪录；英国内政部称偷渡团伙愈趋危险，今年穿越总人数仍同比下降43%。",
            "en_summary": "230 migrants arrived in Dover overnight, breaking July's record of 165; crossings remain down 43% year-on-year despite the surge.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c4g4vxjg2yno",
        },
        {
            "cn_title": "俄法院禁止唯一反战政党亚博卢参加下月议会选举",
            "en_title": "Russian court bars anti-war Yabloko party from September parliamentary elections",
            "published": "02:19 2026年8月11日",
            "cn_summary": "民族党罗迪纳以版权与「极端主义」指控起诉；数百名支持者法院外抗议，亚博卢是唯一公开反对乌克兰战争的注册政党。",
            "en_summary": "A Moscow court barred Yabloko, Russia's only registered anti-war party, as hundreds protested outside the courthouse.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cy9w1l5jr7lo",
        },
        {
            "cn_title": "内塔尼亚胡拒特朗普15点加沙计划，白宫称或为选举言论",
            "en_title": "Netanyahu rejects Trump's 15-point Gaza plan; White House sees campaign rhetoric",
            "published": "22:43 2026年8月10日",
            "cn_summary": "以色列总理称不接受解除哈马斯武装路线图；美方官员认为临近10月大选表态，仍推进国际稳定部队基地筹建。",
            "en_summary": "Netanyahu rejected the Hamas disarmament roadmap; US officials view it as election rhetoric while stabilization force plans proceed.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/ce3q5282ep3o",
        },
        {
            "cn_title": "BBC获南非检方文件：特种部队涉嫌谋杀顶尖侦探",
            "en_title": "BBC access to files suggests South African special forces murdered top detective",
            "published": "08:05 2026年8月10日",
            "cn_summary": "探员马蒂帕调查军方绑架案后被枪杀；8名特种兵被控谋杀，其中3人拒还保释仍在服役，审判日期尚未确定。",
            "en_summary": "Detective Mathipa was killed while probing an alleged military abduction; eight special forces members face murder charges.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cly8djwgem0o",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "cn_title": "酷热仅触发最低级别预警，港府承诺检讨户外工作热应激系统",
            "en_title": "HK pledges heat stress warning review after record heat triggered only amber alert",
            "published": "23:04 2026年8月10日",
            "cn_summary": "周日观测站录36.9°C历史最高，劳工处称将优化机制；专家呼吁采用国际标准并增加监测站点覆盖各区。",
            "en_summary": "After a record 36.9°C day with only an amber work warning, labour officials pledged to review the heat stress index system.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363571/hong-kong-review-warning-system-after-record-heat-triggers-lowest-alert",
        },
        {
            "cn_title": "港警拘捕8人涉「糖宝」约会诈骗，损失约620万港元",
            "en_title": "HK police arrest 8 in HK$6.2 million 'sugar baby' dating scam",
            "published": "14:08 2026年8月10日",
            "cn_summary": "诈骗团伙伪装富豪与律师，以签约费、法庭费诱骗教师及医护等受害人；2月至7月共80宗案件，单笔最高损失约48万。",
            "en_summary": "Scammers posing as wealthy clients and lawyers tricked victims into paying bogus legal fees in 80 cases since February.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363500/hong-kong-police-arrest-8-over-hk62-million-sugar-baby-dating-scam",
        },
        {
            "cn_title": "劳工处将检讨酷热工作警告机制，周日仅发最低级别预警",
            "en_title": "Labour Department to review heat warning system after lowest alert on record day",
            "published": "07:27 2026年8月10日",
            "cn_summary": "台风外围下沉气流带来极端高温，劳工处称湿度与风力因素下按机制发琥珀预警，将密切监测并评估优化空间。",
            "en_summary": "The Labour Department said it will review the warning system after amber was issued on Hong Kong's hottest day on record.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865584-20260810.htm",
        },
        {
            "cn_title": "颠覆政权案11名被告获上诉庭批出终审法院上诉证明书",
            "en_title": "Court grants 11 jailed opposition figures certificates to appeal to CFA",
            "published": "12:29 2026年8月10日",
            "cn_summary": "上诉庭认定五项法律问题具重大普遍意义，涉及2020年初选及瘫痪立法会指控；终审法院仍可决定是否受理上诉。",
            "en_summary": "The Court of Appeal identified five legal issues for the CFA over the 2020 primary and alleged legislature paralysis scheme.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865626-20260810.htm",
        },
    ]),
    ("其他 Other", [
        {
            "cn_title": "世卫组织警告：刚果埃博拉疫情暴发早于宣布且仍在失控",
            "en_title": "WHO warns DR Congo Ebola outbreak began earlier and response is lagging",
            "published": "01:50 2026年8月11日",
            "cn_summary": "病毒或2月已传播却被误诊；确诊逾4294例、死亡约1960人，为该国史上最严重疫情，接触者追踪率仅约75%。",
            "en_summary": "WHO said the outbreak likely started in February; over 4,294 cases and 1,960 deaths make it DR Congo's deadliest Ebola crisis.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c5ydx7m8gzeo",
        },
        {
            "cn_title": "全球海洋7月表面温度创纪录，西欧遭遇极端热浪与干旱",
            "en_title": "World's oceans hit record July temperatures as western Europe bakes",
            "published": "19:24 2026年8月10日",
            "cn_summary": "欧盟气候服务称全球7月为史上第二热月份；大西洋沿岸与西地中海海温创新高，厄尔尼诺发展或进一步推高气温。",
            "en_summary": "Copernicus data showed record sea surface temperatures and western Europe's hottest June-July period on record.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cpvw8vmmgrwo",
        },
        {
            "cn_title": "加州网红秃鹰「杰基」经数周救治后死亡",
            "en_title": "California bald eagle Jackie dies after weeks of intensive care",
            "published": "06:40 2026年8月11日",
            "cn_summary": "大熊谷巢穴直播明星秃鹰杰基遭其他鹰攻击后伤势恶化；其与伴侣影子的巢穴直播拥有数十万订阅者。",
            "en_summary": "Jackie, a star of the Big Bear Eagle Nest livestream, died after an attack by other eagles despite weeks of veterinary care.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c62vj8eywdlo",
        },
        {
            "cn_title": "加拿大偏远社区自发培训居民参与野火防控",
            "en_title": "Remote Canadian communities train residents to fight wildfires themselves",
            "published": "08:02 2026年8月10日",
            "cn_summary": "火灾季愈发猛烈，原住民与农村社区学习自保与结构防护；专家担忧违令留守可能危及生命安全。",
            "en_summary": "As wildfires intensify, rural Canadians are learning to protect homes while officials warn defying evacuations carries deadly risk.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c20d89jxpqno",
        },
    ]),
]


def build_html():
    items = []
    for cat_name, articles in CATEGORIES:
        for a in articles:
            items.append((cat_name, a))
    total = len(items)

    parts = [
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\">",
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
        "<title>每日热点早报 Morning Briefing</title></head>",
        "<body style=\"margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;\">",
        "<div style=\"max-width:600px;margin:0 auto;padding:16px 12px;\">",
        "<div style=\"background:#1a2332;color:#fff;padding:24px 20px;border-radius:10px 10px 0 0;\">",
        "<div style=\"font-size:22px;font-weight:700;line-height:1.3;\">每日热点早报</div>",
        f"<div style=\"font-size:14px;color:#b8c5d6;margin-top:6px;\">Morning News Briefing · {DATE_SUBJECT} · 共 {total} 条</div>",
        "</div>",
        "<div style=\"background:#fff;padding:20px 18px;border-left:1px solid #e8e8e8;border-right:1px solid #e8e8e8;\">",
        "<p style=\"font-size:14px;color:#333;line-height:1.6;margin:0 0 8px 0;\">汇总昨夜至今国际国内要闻，涵盖地震灾情、霍尔木兹僵局、华东台风余波与全球市场动态。</p>",
        "<p style=\"font-size:13px;color:#666;line-height:1.5;margin:0;font-style:italic;\">Overnight and early headlines: Colombia quake, Hormuz tensions, Typhoon Dolphin aftermath, and global market moves.</p>",
        "</div>",
    ]

    idx = 0
    for cat_name, articles in CATEGORIES:
        parts.append(
            f"<div style=\"background:#f5f7fa;padding:10px 18px;border-left:4px solid #2563eb;margin-top:0;\">"
            f"<h2 style=\"margin:0;font-size:15px;color:#1a2332;font-weight:700;\">{cat_name}</h2></div>"
        )
        for a in articles:
            idx += 1
            num = f"{idx:02d}"
            parts.append(
                f"<div style=\"background:#fff;padding:16px 18px;border-bottom:1px solid #eee;\">"
                f"<div style=\"font-size:11px;color:#2563eb;font-weight:700;margin-bottom:4px;\">{num}</div>"
                f"<a href=\"{a['url']}\" style=\"font-size:16px;color:#1a2332;font-weight:600;text-decoration:none;line-height:1.4;\">{a['cn_title']}</a>"
                f"<div style=\"font-size:13px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;\">{a['en_title']}</div>"
                f"<div style=\"font-size:11px;color:#999;margin-top:4px;\">发布时间 Published: {a['published']}</div>"
                f"<p style=\"font-size:14px;color:#333;line-height:1.55;margin:10px 0 4px 0;\">{a['cn_summary']}</p>"
                f"<p style=\"font-size:13px;color:#666;line-height:1.5;margin:0 0 10px 0;font-style:italic;\">{a['en_summary']}</p>"
                f"<span style=\"display:inline-block;background:#e8f0fe;color:#2563eb;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:6px;\">{a['source_cn']} / {a['source_en']}</span>"
                f"<a href=\"{a['url']}\" style=\"font-size:12px;color:#2563eb;text-decoration:none;\">查看全文 Read more →</a>"
                "</div>"
            )

    parts.append(
        "<div style=\"background:#fff;padding:18px;border-radius:0 0 10px 10px;border:1px solid #e8e8e8;border-top:none;box-shadow:0 2px 8px rgba(0,0,0,0.06);\">"
        "<p style=\"font-size:11px;color:#999;line-height:1.6;margin:0;\">本简报由自动化系统汇编，内容来源于公开媒体报道，仅供参考，不构成投资或法律建议。</p>"
        "<p style=\"font-size:11px;color:#999;line-height:1.6;margin:8px 0 0 0;font-style:italic;\">This briefing is automatically compiled from public media sources for informational purposes only; it is not investment or legal advice.</p>"
        "</div></div></body></html>"
    )
    return "".join(parts), total


def main():
    html, total = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {DATE_SUBJECT}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    counts = {c[0]: len(c[1]) for c in CATEGORIES}
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"TOTAL={total}")
    print(f"COUNTS={counts}")
    print(f"HTML_CHARS={len(html)}")
    print(f"WRITTEN={path}")


if __name__ == "__main__":
    main()
