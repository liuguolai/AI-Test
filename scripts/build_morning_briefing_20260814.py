#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-14."""
import json
import os

BRIEFING_EDITION = "早报"
LOCAL_TIME = "07:40 2026年8月14日"
DATE_STR = "2026-08-14"
TOTAL = 28

ITEMS = [
    # 国内 China Mainland (4)
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "央行二季度报告：谋划务实增量政策加大逆周期调节",
        "title_en": "PBOC Q2 Report Signals Pragmatic Incremental Policies, Stronger Counter-Cyclical Support",
        "pub": "07:01 2026年8月13日",
        "sum_zh": "央行发布二季度货币政策执行报告，提出及时谋划增量政策、保持流动性充裕，并强化对扩大内需与科技创新的金融支持。",
        "sum_en": "China's central bank pledged timely incremental policies, ample liquidity, and stronger financial support for domestic demand and tech innovation.",
        "src_zh": "财新", "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-08-13/102473576.html",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "上半年全国结婚登记328万对，同比下降7.5%",
        "title_en": "China Marriage Registrations Fall 7.5% in First Half of 2026",
        "pub": "15:00 2026年8月13日",
        "sum_zh": "民政部数据显示，上半年全国结婚登记约328万对，同比减少26.4万对；离婚登记138万对，同比上升3.9%。",
        "sum_en": "Ministry data show 3.28 million couples married in H1 2026, down 264,000 year-on-year, while divorces rose 3.9% to 1.38 million.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/economy/china-economy/article/3363856/chinas-marriages-fall-75-demographic-crisis-deepens-what-it-spells-economy",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "国产C919执飞北京至乌兰巴托国际定期航线",
        "title_en": "China's C919 Begins Scheduled International Service to Mongolia",
        "pub": "21:20 2026年8月13日",
        "sum_zh": "国航C919执飞CA723/724北京首都至乌兰巴托每日往返航班，标志国产大飞机首次进入国际定期商业运营。",
        "sum_en": "Air China's C919 launched daily Beijing-Ulaanbaatar flights, marking the jet's first scheduled international commercial service.",
        "src_zh": "财新", "src_en": "Caixin",
        "url": "https://companies.caixin.com/2026-08-13/102473883.html",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "十五五城市更新规划落地，涉11.5万小区与50万套危旧房",
        "title_en": "China's 15th Five-Year Plan Sets 15 Trillion Yuan Urban Renewal Targets",
        "pub": "07:01 2026年8月13日",
        "sum_zh": "国家层面城市更新五年规划明确改造11.5万个老旧小区、约50万套城镇危旧房，并给出加装电梯与重建的资金路径。",
        "sum_en": "A national urban renewal plan targets 115,000 old residential compounds and 500,000 dilapidated homes with defined funding paths.",
        "src_zh": "财新", "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-08-13/102473576.html",
    },
    # 科技 Technology (4)
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "Twitch默认用主播内容训练亚马逊AI，用户强烈反弹",
        "title_en": "Twitch Backlash as Amazon Uses Creator Content to Train AI by Default",
        "pub": "18:40 2026年8月13日",
        "sum_zh": "亚马逊旗下Twitch默认开启用直播、聊天等内容训练生成式AI，用户须在设置中手动关闭，引发创作者广泛批评。",
        "sum_en": "Amazon-owned Twitch enabled default use of streams and chats to train generative AI, sparking outrage until users opt out in settings.",
        "src_zh": "BBC", "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cp30pz8d09jo",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "谷歌发布Gemini 3.7 Flash，主打编程与智能体",
        "title_en": "Google Launches Gemini 3.7 Flash for Coding and Agent Workflows",
        "pub": "01:02 2026年8月14日",
        "sum_zh": "谷歌推出面向编程与自主工作流的Gemini 3.7 Flash，限时定价每百万输入令牌0.75美元，并同步上线Spark智能体服务。",
        "sum_en": "Google released Gemini 3.7 Flash for coding and agents at $0.75 per million input tokens, rolling it out to its Spark agent service.",
        "src_zh": "亚洲新闻台", "src_en": "CNA",
        "url": "https://www.channelnewsasia.com/business/google-unveils-gemini-37-flash-ai-model-coding-agent-workflows-6318136",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "中芯国际与华虹二季度净利润同比增逾两倍",
        "title_en": "SMIC and Hua Hong Post Triple-Digit Q2 Profit Growth on AI Chip Demand",
        "pub": "19:00 2026年8月13日",
        "sum_zh": "中芯国际二季度净利4.79亿美元，同比增261.7%；华虹净利3860万美元，同比增385.9%，代工产能接近满负荷。",
        "sum_en": "SMIC net profit jumped 262% to $479.2M and Hua Hong surged 386% to $38.6M in Q2 as domestic AI chip demand filled fabs.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/tech/tech-trends/article/3363929/ai-demand-drives-triple-digit-quarterly-profit-growth-chinese-foundries-smic-hua-hong",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "台湾称7月遭境外AI智能体混合式网络攻击",
        "title_en": "Taiwan Says July Cyberattacks Used AI Agents in Hybrid Hacking Campaign",
        "pub": "10:05 2026年8月13日",
        "sum_zh": "台数字发展部门称，7月检测到境外来源攻击，黑客结合人工操作与OpenClaw等AI智能体，已加强跨部门防护指引。",
        "sum_en": "Taiwan's digital ministry said July attacks from overseas combined manual hacking with AI agents such as OpenClaw, prompting new safeguards.",
        "src_zh": "海峡时报", "src_en": "The Straits Times",
        "url": "https://www.straitstimes.com/asia/east-asia/taiwan-says-it-was-targeted-last-month-in-ai-driven-hacking-campaign",
    },
    # 财经 Finance & Business (4)
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "标普500收盘创历史新高，通胀数据缓和加息担忧",
        "title_en": "S&P 500 Closes at Record High as Tame Inflation Eases Rate-Hike Fears",
        "pub": "02:35 2026年8月14日",
        "sum_zh": "美国7月生产者物价持平，标普500收涨0.65%至7798.99点创历史新高，纳指涨0.81%，市场对9月加息预期降温。",
        "sum_en": "The S&P 500 rose 0.65% to a record 7,798.99 after flat July PPI data eased fears of a September Fed rate hike.",
        "src_zh": "路透社", "src_en": "Reuters",
        "url": "https://uk.marketscreener.com/news/s-p-500-hits-record-high-as-rate-hike-worries-ease-ce7859ded98bf020",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "白宫报告指控中国出口商经40余国实施“大转运骗局”逃税",
        "title_en": "White House Accuses China of 'Great Transshipment Scam' via 40+ Countries",
        "pub": "18:45 2026年8月13日",
        "sum_zh": "特朗普政府报告称，中国出口商经40多个第三国转口、换标与虚假原产地申报规避美国关税，年损失约190至260亿美元。",
        "sum_en": "A White House report alleges Chinese exporters routed goods through 40+ countries to dodge US tariffs, costing $19-26B annually.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/news/us/article/3363925/us-accuses-chinese-exporters-masterminding-great-transshipment-scam",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "传Silver Lake洽谈收购Workday，股价大涨逾18%",
        "title_en": "Silver Lake in Talks to Buy Workday, Sending Shares Up Over 18%",
        "pub": "03:08 2026年8月14日",
        "sum_zh": "路透社援引知情人士称，私募巨头Silver Lake数月来与人力资源软件商Workday洽谈收购，推动其股价成为标普500涨幅榜首。",
        "sum_en": "Reuters reported Silver Lake has held talks to acquire Workday, sending the HR software firm's shares up more than 18%.",
        "src_zh": "路透社", "src_en": "Reuters",
        "url": "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-major-indexes-104933715.html",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "美国拟用AI“侦探边境”系统打击转口逃税",
        "title_en": "US Plans AI 'Detective Border' to Combat Tariff Evasion",
        "pub": "23:17 2026年8月13日",
        "sum_zh": "白宫贸易顾问纳瓦罗称，海关将与边境保护局合作开发AI系统，分析货运数据与航线历史以识别非法转口货物。",
        "sum_en": "The White House said it will deploy an AI system with Customs to analyze shipment data and routing histories to detect transshipped goods.",
        "src_zh": "海峡时报", "src_en": "The Straits Times",
        "url": "https://www.straitstimes.com/world/united-states/us-flags-dozens-of-trade-partners-as-risks-for-aiding-tariff-evasion",
    },
    # 社会 Society (4)
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "东京周边暴雨致1人死亡，逾6.8万户停电",
        "title_en": "Torrential Rain Near Tokyo Kills One, Cuts Power to 68,000 Homes",
        "pub": "00:00 2026年8月13日",
        "sum_zh": "日本气象厅对千叶14市发布最高级别暴雨预警，市川市1人遇难，约22万人获疏散建议，部分地区列车停运。",
        "sum_en": "Record rainfall flooded eastern Japan near Tokyo, killing one in Ichikawa and leaving 68,000 homes without power.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/japan-rain-floods-00b3ce16f648f9c3885bf547edad1696",
    },
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "哥伦比亚地震搜救进入关键窗口，死亡升至273人",
        "title_en": "Colombia Quake Rescue Enters Critical Window as Death Toll Hits 273",
        "pub": "00:00 2026年8月13日",
        "sum_zh": "7.4级地震发生72小时后，救援人员呼吁保持安静搜寻幸存者，卡利等地多数现场已转入废墟清理阶段。",
        "sum_en": "Rescuers called for silence in Colombia's rubble as the 72-hour window closed, with at least 273 dead and hundreds missing.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/colombia-earthquake-rescue-search-quake-99bea7b7eae8778e9e6729556c855369",
    },
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "南苏丹霍乱病例超11万，卫生部长称近期趋缓",
        "title_en": "South Sudan Cholera Cases Top 110,000 as Minister Reports Recent Decline",
        "pub": "00:00 2026年8月12日",
        "sum_zh": "南苏丹自2024年9月以来累计霍乱病例110,574例、死亡1721例，卫生部长称近月病例下降但部分地区仍有传播。",
        "sum_en": "South Sudan has logged 110,574 cholera cases and 1,721 deaths since Sept 2024, with recent declines but ongoing transmission in some areas.",
        "src_zh": "Radio Tamazuj", "src_en": "Radio Tamazuj",
        "url": "https://www.radiotamazuj.org/en/news/article/health-minister-cholera-cases-decline-after-110000-infections",
    },
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "英国今夏最热日38.1℃，为有记录以来第五高温",
        "title_en": "UK Records Hottest Day of 2026 at 38.1C, Fifth-Highest on Record",
        "pub": "00:53 2026年8月14日",
        "sum_zh": "伦敦邱园测得38.1℃，为2026年迄今最高温，也是英国有记录以来第五高温日，今夏或成最热夏季。",
        "sum_en": "Kew Gardens hit 38.1C, the UK's hottest day of 2026 and fifth-highest temperature ever recorded, amid a fifth heatwave.",
        "src_zh": "BBC", "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c8xnwz7kl2vo",
    },
    # 国际 World (4)
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "乌无人机袭击俄巴什基尔炼油厂，系四日内第四次",
        "title_en": "Ukrainian Drones Strike Major Russian Refinery Deep Inside Bashkortostan",
        "pub": "00:00 2026年8月13日",
        "sum_zh": "乌军称击中距边境约1300公里的萨拉丁瓦特炼油综合体并引发火灾，俄官员称此前被袭的奥尔斯克炼油厂或需半年修复。",
        "sum_en": "Ukraine struck the Gazprom Neftekhim Salavat refinery 1,300 km inside Russia, the fourth oil attack in three days.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/russia-ukraine-war-oil-refinery-8050b4afb5bfd6f4d93c76b4d9795dfa",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "波兰挫败俄策划刺杀美籍乌裔公民阴谋",
        "title_en": "Poland Thwarts Alleged Russian Plot to Kill Ukrainian-American in Warsaw",
        "pub": "00:00 2026年8月13日",
        "sum_zh": "波兰总理图斯克称，俄方指使的嫌疑人8月7日被捕，系北约境内首次针对美国公民的刺杀图谋，已与美方情报部门合作。",
        "sum_en": "Poland said it foiled a Russian plot to kill a Ukrainian-American in Warsaw, the first such targeting of a US citizen in NATO territory.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/poland-russia-plot-c7f8dc3e5a9ba20ae722a1b9d44614db",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "乌克兰提议黑海双方停止攻击民用目标",
        "title_en": "Ukraine Offers Russia Mutual Halt to Black Sea Strikes on Civilian Targets",
        "pub": "00:59 2026年8月14日",
        "sum_zh": "消息人士称，基辅经第三方已向莫斯科转交停火提议，等待回应；8月乌克兰粮食出口同比骤降76%。",
        "sum_en": "Kyiv proposed via a third party that both sides halt attacks on civilian Black Sea targets, with Ukraine's August grain exports down 76%.",
        "src_zh": "路透社", "src_en": "Reuters",
        "url": "https://whbl.com/2026/08/13/exclusive-ukraine-offers-russia-truce-in-black-sea-as-food-supply-fears-mount-source-says/",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "罗马尼亚唯一核电站因多瑙河水位过低关停",
        "title_en": "Romania Shuts Only Nuclear Plant as Danube Heatwave Drops Water Levels",
        "pub": "00:05 2026年8月14日",
        "sum_zh": "切尔纳沃达第二座反应堆因冷却用水不足断开电网，电厂称至少10天内难以重启，该国约两成电力受影响。",
        "sum_en": "Romania disconnected Cernavodă's second reactor as extreme heat lowered Danube levels, with no restart expected for 10 days.",
        "src_zh": "BBC", "src_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cqlxpq5q799o",
    },
    # 香港 Hong Kong (4)
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "大埔火灾调查：分包商订购非阻燃防护网获证实",
        "title_en": "Tai Po Blaze Inquiry Confirms Subcontractor Ordered Non-Fire-Retardant Nets",
        "pub": "19:26 2026年8月13日",
        "sum_zh": "独立委员会文件显示，王福苑脚手架分包商增益棚业订购不合规防护网，专家指或为火势快速蔓延关键因素。",
        "sum_en": "An inquiry found Wang Fuk Court's subcontractor ordered non-compliant scaffolding nets, a key factor in the deadly blaze's rapid spread.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3363936/supplier-says-subcontractor-ordered-non-fire-retardant-nets-tai-po-blaze",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "竞委会第二轮围标执法，涉28屋苑5亿港元工程",
        "title_en": "HK Competition Commission Raids 12 Sites in HK$500M Bid-Rigging Probe",
        "pub": "12:14 2026年8月13日",
        "sum_zh": "竞争事务委员会搜查12处处所，调查28个屋苑及大厦维修工程涉嫌围标，部分合约尚未批出。",
        "sum_en": "Hong Kong's Competition Commission raided 12 premises over alleged bid-rigging in 28 building renovation projects worth HK$500 million.",
        "src_zh": "香港电台", "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866016-20260813.htm",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "香港连续九天极热，户外劳工热应激预警受质疑",
        "title_en": "Nine-Day Heat Streak Puts Hong Kong's Worker Heat-Warning System Under Fire",
        "pub": "22:39 2026年8月13日",
        "sum_zh": "天文台连续九天最高温逾33℃，劳工处热应激预警能否充分保护建筑工人与清洁工引发社会讨论。",
        "sum_en": "Nine consecutive very hot days reignited debate over whether Hong Kong's heat-stress warnings adequately protect outdoor workers.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363953/why-hong-kongs-heat-stress-warning-system-outdoor-workers-hot-seat",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "港台「阳光少年」2026计划闭幕，逾百学生汇报成果",
        "title_en": "RTHK Solar Project 2026 Closes with Presentations by 100+ Students",
        "pub": "19:55 2026年8月13日",
        "sum_zh": "商经局常秘与李佳怡等出席闭幕礼，77间中学逾百名学生展示研学成果，专题节目8月28日起在港台电视31播出。",
        "sum_en": "More than 100 students from 77 schools presented Solar Project 2026 outcomes at RTHK's closing ceremony, with a TV special airing from Aug 28.",
        "src_zh": "香港电台", "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866068-20260813.htm",
    },
    # 其他 Other (4)
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "鹿特丹港炼油设施爆炸致1死，警方称似工伤事故",
        "title_en": "Rotterdam Port Refinery Blast Kills One; Police See Workplace Accident",
        "pub": "00:00 2026年8月14日",
        "sum_zh": "欧洲最大港口Gunvor Energy炼油终端周四上午发生爆炸，至少1人死亡、多人受伤，警方暂按工伤事故处理。",
        "sum_en": "An explosion at Gunvor Energy's Rotterdam refinery terminal killed at least one and injured several; police called it a likely workplace accident.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/netherlands-rotterdam-port-explosion-blackout-police-3196dd5655bc2a1e39914eaa1927ef81",
    },
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "罗马近郊弹药厂爆炸，未报告人员伤亡",
        "title_en": "Huge Explosion at Ammunition Plant Near Rome Causes No Injuries",
        "pub": "02:30 2026年8月14日",
        "sum_zh": "科莱费罗KNDS弹药厂火药压制车间起火后爆炸，浓烟冲天，市长称现场无人伤亡，厂方已启动调查。",
        "sum_en": "A fire and blast at KNDS Ammo Italy's Colleferro plant sent smoke towering over Rome suburbs but caused no reported injuries.",
        "src_zh": "美联社", "src_en": "AP",
        "url": "https://apnews.com/article/explosion-ammunition-factory-colleferro-a985b329d0bd6c3d2201873372299b64",
    },
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "长江存储YMTC闪存出货份额首进全球前三",
        "title_en": "China's YMTC Enters Global Top Three NAND Flash Suppliers at 14%",
        "pub": "13:00 2026年8月13日",
        "sum_zh": "Counterpoint数据显示，二季度YMTC NAND闪存出货量占全球14%，超越铠侠位列第三，但营收仍落后于美光等厂商。",
        "sum_en": "YMTC captured 14% of global NAND bit shipments in Q2, overtaking Kioxia for third place, though revenue still trails US rivals.",
        "src_zh": "南华早报", "src_en": "SCMP",
        "url": "https://www.scmp.com/tech/tech-trends/article/3363854/chinas-ymtc-breaks-global-top-three-flash-memory-suppliers-first-time",
    },
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "俄新罗西斯克三大粮食码头停运，出口或进一步下滑",
        "title_en": "All Three Novorossiysk Grain Terminals Halted, Cutting Russian Exports",
        "pub": "18:47 2026年8月13日",
        "sum_zh": "乌克兰袭击后，俄黑海最大粮食码头KSK宣布停装，新罗西斯克三大码头全部停摆，8月海运粮食出口或创十年新低。",
        "sum_en": "Ukraine's strikes halted all three grain terminals at Novorossiysk, likely pushing Russia's August seaborne exports to a 10-year low.",
        "src_zh": "Baird Maritime", "src_en": "Baird Maritime",
        "url": "https://www.bairdmaritime.com/shipping/dry-cargo/bulkers/port-shutdowns-push-russia-into-deeper-grain-export-slowdown",
    },
]

SRC_COLORS = {
    "财新": "#c0392b", "Caixin": "#c0392b",
    "南华早报": "#e67e22", "SCMP": "#e67e22",
    "BBC": "#8e44ad", "美联社": "#2980b9", "AP": "#2980b9",
    "路透社": "#27ae60", "Reuters": "#27ae60",
    "亚洲新闻台": "#16a085", "CNA": "#16a085",
    "海峡时报": "#2c3e50", "The Straits Times": "#2c3e50",
    "香港电台": "#d35400", "RTHK": "#d35400",
    "Radio Tamazuj": "#7f8c8d",
    "Baird Maritime": "#34495e",
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def item_html(n, it):
    color = SRC_COLORS.get(it["src_zh"], SRC_COLORS.get(it["src_en"], "#666"))
    return f'''<tr><td style="padding:0 0 18px 0;border-bottom:1px solid #eee;">
<table width="100%" cellpadding="0" cellspacing="0"><tr>
<td width="36" valign="top" style="font-size:22px;font-weight:bold;color:#1a5276;padding-top:2px;">{n:02d}</td>
<td style="padding-left:8px;">
<a href="{it['url']}" style="color:#1a5276;font-size:16px;font-weight:bold;text-decoration:none;line-height:1.4;">{esc(it['title_zh'])}</a><br>
<em style="color:#555;font-size:14px;line-height:1.4;">{esc(it['title_en'])}</em><br>
<span style="color:#888;font-size:12px;">发布时间 Published: {esc(it['pub'])}</span><br>
<span style="color:#333;font-size:14px;line-height:1.5;display:block;margin-top:6px;">{esc(it['sum_zh'])}</span>
<span style="color:#666;font-size:13px;line-height:1.5;display:block;margin-top:4px;">{esc(it['sum_en'])}</span>
<span style="display:inline-block;margin-top:8px;padding:2px 8px;background:{color};color:#fff;font-size:11px;border-radius:3px;">{esc(it['src_zh'])} / {esc(it['src_en'])}</span>
<a href="{it['url']}" style="color:#2980b9;font-size:12px;margin-left:8px;text-decoration:none;">查看全文 Read more →</a>
</td></tr></table></td></tr>'''


def build_html():
    cats = []
    seen = set()
    for it in ITEMS:
        key = (it["cat_zh"], it["cat_en"])
        if key not in seen:
            seen.add(key)
            cats.append(key)

    body = ""
    n = 1
    for cat_zh, cat_en in cats:
        body += f'<tr><td style="padding:20px 0 10px 0;"><h2 style="margin:0;padding:10px 12px;background:#f0f3f6;border-left:4px solid #2980b9;font-size:17px;color:#2c3e50;">{cat_zh} <span style="font-weight:normal;color:#666;font-size:14px;">/ {cat_en}</span></h2></td></tr>'
        for it in ITEMS:
            if it["cat_zh"] == cat_zh:
                body += item_html(n, it)
                n += 1

    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点早报 Morning Briefing - {DATE_STR}</title></head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#eef1f5;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a5276,#2980b9);padding:28px 24px;text-align:center;">
<div style="color:#fff;font-size:24px;font-weight:bold;letter-spacing:1px;">每日热点早报</div>
<div style="color:#d6eaf8;font-size:14px;margin-top:6px;">Morning News Briefing · {DATE_STR} · 共 {TOTAL} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px 24px;">
<p style="margin:0 0 6px 0;color:#333;font-size:14px;line-height:1.6;">汇总昨夜至今晨全球要闻，涵盖政策、市场、科技与民生动态。</p>
<p style="margin:0;color:#666;font-size:13px;line-height:1.6;">Overnight and early headlines across policy, markets, technology, and society.</p>
</td></tr>
<tr><td style="padding:0 24px 24px 24px;"><table width="100%" cellpadding="0" cellspacing="0">{body}</table></td></tr>
<tr><td style="background:#f8f9fa;padding:16px 24px;border-top:1px solid #eee;">
<p style="margin:0 0 4px 0;color:#999;font-size:11px;line-height:1.5;">本简报由自动化系统汇编，内容来源于公开媒体报道，仅供参考，不构成投资建议。</p>
<p style="margin:0;color:#999;font-size:11px;line-height:1.5;">This briefing is automatically compiled from public media sources for reference only and does not constitute investment advice.</p>
</td></tr>
</table></td></tr></table></body></html>'''


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {DATE_STR}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"TOTAL={TOTAL}")
    print(f"HTML_CHARS={len(html)}")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
