#!/usr/bin/env python3
"""Generate email_payload.json for 2026-07-26 evening briefing."""
import json
import os

ITEMS = [
    # 国内 China Mainland (5)
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "台风「红霞」凌晨登陆广东惠州惠东",
        "title_en": "Typhoon Noul makes landfall in Huidong, Guangdong",
        "published": "04:40 2026年7月26日",
        "summary_zh": "广东省气象台称，今年第12号台风于26日3时50分前后在惠东县平海镇登陆，中心最大风力14级。",
        "summary_en": "Guangdong's weather service said Typhoon Noul came ashore near Pinghai with force-14 winds at about 3:50 a.m. on July 26.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://www.news.cn/local/20260726/f72a3ef26871416dabf590313625c4fa/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "台风登陆后华南将迎持续强降雨与洪涝风险",
        "title_en": "Southern China faces torrential rain and flood risk after Noul landfall",
        "published": "08:35 2026年7月26日",
        "summary_zh": "路透称广东逾70万人转移，国家发布山洪红色预警；香港机场停运逾12小时后逐步复航。",
        "summary_en": "Reuters reports over 700,000 relocated in Guangdong and top flash-flood alerts, as Hong Kong airport resumes flights after 12+ hours of disruption.",
        "source_zh": "海峡时报", "source_en": "The Straits Times",
        "url": "https://www.straitstimes.com/asia/east-asia/southern-china-drenched-as-typhoon-noul-makes-landfall",
        "tag": "#16a085",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "南海遇险越南货船沉没，37人获救搜救继续",
        "title_en": "37 rescued as Vietnamese cargo ship sinks in South China Sea",
        "published": "10:17 2026年7月26日",
        "summary_zh": "三沙市称永暑礁附近「Khoi Nguyen 18」遇险沉没，船上62人已有37名越南籍船员获救，多国力量仍在搜救。",
        "summary_en": "Sansha authorities said 37 of 62 crew from the distressed Vietnamese vessel Khoi Nguyen 18 were rescued near Yongshu Reef; search efforts continue.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/83e66515132a419096bae7d74a6e91ab/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "广东逾34万人转移安置应对台风「红霞」",
        "title_en": "Over 340,000 relocated in Guangdong ahead of Typhoon Noul",
        "published": "22:47 2026年7月25日",
        "summary_zh": "广东省三防部门称，截至25日16时全省19市135县区启动应急响应，海上逾5000艘船只已引导避险。",
        "summary_en": "Guangdong flood-control authorities said more than 340,000 people were moved and over 5,100 vessels guided to shelter as Noul approached.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260725/9b3e1bceb24848feba4141536a025679/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国内", "cat_en": "China Mainland",
        "title_zh": "中央气象台对台风「红霞」发布最高级别红色预警",
        "title_en": "China issues top red alert as Typhoon Noul approaches",
        "published": "00:03 2026年7月26日",
        "summary_zh": "国家气象中心预计强台风将在广东沿海登陆，国家防总对粤赣湘提升防汛防台风应急响应。",
        "summary_en": "The national observatory warned of a severe landfall in Guangdong while flood headquarters raised emergency responses in Guangdong, Jiangxi and Hunan.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/8df0d147e1924cebb16a2f6c1438585d/c.html",
        "tag": "#c0392b",
    },
    # 科技 Technology (4)
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "苹果印度供应链遭遇史上最大规模信息泄露",
        "title_en": "Apple faces its largest-ever supply-chain leak in India",
        "published": "06:00 2026年7月26日",
        "summary_zh": "南早称黑客组织World Leaks攻击塔塔电子，逾20万份文件外泄，引发对印度制造网络治理的担忧。",
        "summary_en": "SCMP reports hackers leaked 200,000+ files from Tata Electronics, raising questions about cyber governance in India's Apple supply chain.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/tech/tech-trends/article/3361752/apples-biggest-ever-leak-happened-india-will-firms-rethink-their-china-relocations",
        "tag": "#8e44ad",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "我国启动商业太空碎片监测「 Gandé 星座」建设",
        "title_en": "China begins deploying commercial space-debris monitoring constellation",
        "published": "16:56 2026年7月26日",
        "summary_zh": "新华社称首颗「 Gandé 星座」卫星已发射，规划120颗卫星在2030年前实现全轨道目标探测。",
        "summary_en": "Xinhua says the first Gande Constellation satellite launched Friday, part of a 120-satellite network planned by 2030 for debris tracking.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/95c7daaf83254e2abe906deb370b200c/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "财新：全球AI版权诉讼转向证据精度之争",
        "title_en": "Caixin: Global AI copyright fights pivot to evidence precision",
        "published": "10:29 2026年7月26日",
        "summary_zh": "财新称训练数据取用与生成内容侵权成焦点，各国法院更关注记忆化与实质性相似等可证明问题。",
        "summary_en": "Caixin says courts worldwide focus on provable issues like memorization and substantial similarity rather than rewriting copyright statutes.",
        "source_zh": "财新", "source_en": "Caixin",
        "url": "https://mini.caixin.com/2026-07-26/102468153.html",
        "tag": "#d35400",
    },
    {
        "cat_zh": "科技", "cat_en": "Technology",
        "title_zh": "德里高院：OpenAI用ANI报道训练ChatGPT暂不构成侵权",
        "title_en": "Delhi High Court denies interim ban on OpenAI's ANI training data use",
        "published": "13:09 2026年7月25日",
        "summary_zh": "印度教徒报称法院认定存储新闻用于大模型训练属合理使用，且未证明输出与原作实质性相似。",
        "summary_en": "The Hindu reports the court found storing ANI articles for LLM training was fair dealing and outputs were not substantially similar.",
        "source_zh": "印度教徒报", "source_en": "The Hindu",
        "url": "https://www.thehindu.com/sci-tech/technology/openai-vs-ani-case-what-it-means-for-the-future-of-information/article71265247.ece",
        "tag": "#2980b9",
    },
    # 财经 Finance (4)
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "胡塞袭击沙特港口推升油价，布伦特一度破百",
        "title_en": "Houthi strikes on Saudi ports lift oil; Brent tops $100",
        "published": "12:06 2026年7月26日",
        "summary_zh": "海峡时报称红海战事扩大能源运输风险，在美方暂停对伊空袭之际全球油价本周大幅波动。",
        "summary_en": "The Straits Times says Red Sea attacks widened supply risks, driving sharp weekly oil swings as the U.S. paused strikes on Iran.",
        "source_zh": "海峡时报", "source_en": "The Straits Times",
        "url": "https://www.straitstimes.com/world/middle-east/houthis-fire-on-saudi-oil-sites-no-us-strike-on-iran-for-first-time-in-two-weeks",
        "tag": "#16a085",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "汇丰20.8亿美元向安联出售新加坡寿险业务",
        "title_en": "HSBC to sell Singapore insurance unit to Allianz for $2.08bn",
        "published": "10:38 2026年7月24日",
        "summary_zh": "南早称交易预计2027年上半年完成，汇丰预计税前收益18亿美元并签署15年独家银保分销协议。",
        "summary_en": "SCMP says the deal should close in H1 2027, with HSBC expecting a $1.8bn pre-tax gain and a 15-year bancassurance pact.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/business/companies/article/3361669/hsbc-agrees-us2-billion-deal-sell-singapore-insurance-branch-allianz",
        "tag": "#8e44ad",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "港交所推八年最大上市改革，放宽保密申请与市值门槛",
        "title_en": "HKEX unveils biggest listing reforms in eight years",
        "published": "17:05 2026年7月24日",
        "summary_zh": "南早称改革即时生效，允许普遍保密递交，并下调同股不同权及海外创新企业二次上市市值要求。",
        "summary_en": "SCMP says reforms take effect immediately, allowing confidential filings and lower market-cap thresholds for WVR and secondary listings.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/business/markets/article/3361742/hong-kong-exchanges-biggest-reform-8-years-opens-gates-more-ipos",
        "tag": "#8e44ad",
    },
    {
        "cat_zh": "财经", "cat_en": "Finance & Business",
        "title_zh": "美伊暂停空袭与霍尔木兹谈判推进，联储关注通胀",
        "title_en": "U.S.-Iran strike pause and Hormuz talks weigh on Fed outlook",
        "published": "09:37 2026年7月26日",
        "summary_zh": "海湾新闻称外交斡旋与停火信号交织，油价高位加剧市场对美联储维持高利率及通胀复燃的担忧。",
        "summary_en": "Gulf News says diplomacy around Hormuz coincides with high oil prices, keeping Fed inflation risks in focus for markets.",
        "source_zh": "海湾新闻", "source_en": "Gulf News",
        "url": "https://gulfnews.com/world/mena/us-iran-conflict-apparent-airstrike-pause-as-oman-talks-advance-on-strait-of-hormuz-1.500620344",
        "tag": "#27ae60",
    },
    # 社会 Society (3)
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "柏林骄傲节遭货车冲撞，1死16伤活动取消",
        "title_en": "Berlin Pride rally cancelled after van attack kills one",
        "published": "14:54 2026年7月26日",
        "summary_zh": "印度教徒报称警方通缉21岁嫌疑人阿卜杜勒·B，现场亦调查多起持刀伤人，总理默茨谴责袭击。",
        "summary_en": "The Hindu reports police sought suspect Abdul B., 21, after a van hit crowds in Tiergarten; Chancellor Merz condemned the attack.",
        "source_zh": "印度教徒报", "source_en": "The Hindu",
        "url": "https://www.thehindu.com/news/international/germany-berlin-lgbtqia-event-van-accident-police-casualties-updates-july-26-2026/article71268535.ece",
        "tag": "#2980b9",
    },
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "法西野火再疏散5.5万人，灭火遭遇「火旋风」",
        "title_en": "France evacuates 55,000 more as fire whirlwinds complicate response",
        "published": "15:21 2026年7月26日",
        "summary_zh": "BBC称吉伦特省火势逼近波尔多，今年法国过火面积已近9.8万公顷，军方出动A400M投阻燃剂。",
        "summary_en": "BBC says Gironde blazes neared Bordeaux with nearly 98,000 hectares burned nationwide; an A400M joined firefighting efforts.",
        "source_zh": "英国广播公司", "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/clyj8k4nn5jo",
        "tag": "#2c3e50",
    },
    {
        "cat_zh": "社会", "cat_en": "Society",
        "title_zh": "法西野火致逾30万人撤离，消防员殉职",
        "title_en": "France and Spain wildfires force 300,000 to flee; firefighters killed",
        "published": "03:26 2026年7月26日",
        "summary_zh": "澳广播公司称极端高温下两国疏散规模创和平时期纪录，法国波尔多附近两名消防员殉职。",
        "summary_en": "ABC says heat-fuelled fires triggered mass evacuations; French officials confirmed two firefighters died near Bordeaux airport.",
        "source_zh": "澳大利亚广播公司", "source_en": "ABC News",
        "url": "https://www.abc.net.au/news/2026-07-26/france-spain-wildfires-force-250-000-people-to-flee-homes/106958588",
        "tag": "#e67e22",
    },
    # 国际 World (5)
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "美国13晚后首次未空袭伊朗，红海战事仍扩大",
        "title_en": "U.S. skips Iran strikes for first night in 13 as war widens",
        "published": "11:33 2026年7月26日",
        "summary_zh": "路透称美方未说明停火原因，胡塞袭击沙特红海油港，伊朗指控乌克兰在里海袭击商船。",
        "summary_en": "Reuters says Washington gave no reason for halting strikes while Houthis hit Saudi Red Sea oil sites and Iran accused Ukraine of a Caspian attack.",
        "source_zh": "路透社", "source_en": "Reuters",
        "url": "https://www.yahoo.com/news/articles/iran-war-spreads-red-sea-231841924.html",
        "tag": "#1a5276",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "阿曼斡旋霍尔木兹谈判，卡塔尔宣布海运全面恢复",
        "title_en": "Oman Hormuz talks advance; Qatar resumes full maritime traffic",
        "published": "08:00 2026年7月26日",
        "summary_zh": "半岛电视台直播称伊方称与阿曼副外长会谈取得进展，卡塔尔运输部宣布7月26日起船舶活动全面恢复。",
        "summary_en": "Al Jazeera's liveblog says Iran reported progress with Oman on Hormuz, while Qatar declared full maritime operations resumed Sunday.",
        "source_zh": "半岛电视台", "source_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/liveblog/2026/7/26/iran-war-live-tehran-summons-ukraine-diplomats-over-caspian-sea-attack",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "古特雷斯16年来首访大马士革，承诺支持叙重建",
        "title_en": "Guterres makes first Damascus visit by UN chief since 2009",
        "published": "06:00 2026年7月26日",
        "summary_zh": "新华社称秘书长呼吁国际社会协助战后重建，并重申戈兰高地为叙利亚领土，叙方称350万人已返乡。",
        "summary_en": "Xinhua says Guterres urged global support for reconstruction and reaffirmed the Golan as Syrian territory; Syria cited 3.5 million returns.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/3413f1e5ca604eb59e9f19650b076e99/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "刚果（金）埃博拉确诊超3000例，死亡1354人",
        "title_en": "DR Congo Ebola cases surpass 3,000",
        "published": "07:18 2026年7月26日",
        "summary_zh": "新华社引官方数据称五省受影响，总理称正研发针对邦巴迪约病毒的疫苗，牛津大学已启动首例人体试验。",
        "summary_en": "Xinhua cites official data across five provinces; leaders said vaccine work continues, with Oxford starting the first human trial.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/a166ff5af33e4bc4bf66198fbb56dc60/c.html",
        "tag": "#c0392b",
    },
    {
        "cat_zh": "国际", "cat_en": "World",
        "title_zh": "西班牙野火进入全国紧急状态，9.1万人疏散或室内避险",
        "title_en": "Spain declares national emergency as wildfires displace 91,000",
        "published": "15:12 2026年7月26日",
        "summary_zh": "新华社称马德里、阿维拉等地约4.5万公顷过火，气象部门警告东部南部仍处极高火险等级。",
        "summary_en": "Xinhua says about 91,000 were evacuated or told to stay indoors, with 45,000 hectares burned near Madrid and Avila amid extreme fire risk.",
        "source_zh": "新华社", "source_en": "Xinhua",
        "url": "https://english.news.cn/20260726/d4e0c9861a1b4fe594c24cd30068a312/c.html",
        "tag": "#c0392b",
    },
    # 香港 Hong Kong (4)
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "「红霞」远离后约350班机取消，下午逐步复航",
        "title_en": "About 350 Hong Kong flights cancelled as Noul departs",
        "published": "14:54 2026年7月26日",
        "summary_zh": "南早称机管局预计下午大部分航班恢复，高铁跨境服务逾190班停运，天文台15:20将三号改为一号。",
        "summary_en": "SCMP says the Airport Authority expected most flights to resume Sunday afternoon, with 190+ cross-border rail services cancelled.",
        "source_zh": "南华早报", "source_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3361858/typhoon-noul-t8-signal-remain-force-until-least-noon",
        "tag": "#8e44ad",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "天文台下午改挂三号风球，21人台风伤入院",
        "title_en": "HK lowers signal to No. 3; 21 typhoon injuries reported",
        "published": "15:58 2026年7月26日",
        "summary_zh": "政府新闻网称八号风球于12:40取消，当局收到331宗塌树及8宗水浸报告，29个临时庇护中心曾收容246人。",
        "summary_en": "news.gov.hk says the No. 8 signal ended at 12:40 p.m., with 331 fallen-tree reports and 21 hospital treatments for typhoon injuries.",
        "source_zh": "香港政府新闻网", "source_en": "news.gov.hk",
        "url": "https://www.news.gov.hk/eng/2026/07/20260726/20260726_142103_947.html",
        "tag": "#2c3e50",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "下午3时20分改发一号戒备信号",
        "title_en": "Standby Signal No. 1 to replace No. 3 at 3:20 p.m.",
        "published": "12:55 2026年7月26日",
        "summary_zh": "港台引天文台称「红霞」北上减弱，离岸仍间中吹烈风，周日至周一仍有狂风雨及雷暴。",
        "summary_en": "RTHK cited the Observatory saying Noul was weakening inland while heavy squalls and thunderstorms would persist into Monday.",
        "source_zh": "香港电台", "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1863765-20260726.htm",
        "tag": "#1a5276",
    },
    {
        "cat_zh": "香港本地", "cat_en": "Hong Kong",
        "title_zh": "凌晨一度挂九号风球，「红霞」惠州登陆逼近本港",
        "title_en": "T9 hoisted as Severe Typhoon Noul nears Hong Kong",
        "published": "01:10 2026年7月26日",
        "summary_zh": "港台称风暴于惠州登陆并距港约80公里，天文台评估是否需发出十号飓风信号，至少维持至早上7时。",
        "summary_en": "RTHK said Noul made landfall in Huizhou about 80 km from Hong Kong, with Signal No. 9 or above expected until at least 7 a.m.",
        "source_zh": "香港电台", "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1863657-20260726.htm",
        "tag": "#1a5276",
    },
    # 其他 Other (2)
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "科威特与伊拉克阿卜达利口岸在无人机袭击后重开",
        "title_en": "Kuwait reopens Abdali border crossing with Iraq",
        "published": "15:29 2026年7月26日",
        "summary_zh": "伊拉克通讯社称口岸周日恢复客货运，此前遭无人机袭击受损但无伤亡，正值阿拉芬朝圣季交通高峰。",
        "summary_en": "Iraqi state media said the Abdali crossing reopened Sunday for passengers and trade after a drone strike caused damage but no casualties.",
        "source_zh": "伊拉克通讯社", "source_en": "Iraqi News Agency",
        "url": "https://ina.iq/en/local/50709-kuwait-reopens-abdali-border-crossing-with-iraq.html",
        "tag": "#7f8c8d",
    },
    {
        "cat_zh": "其他", "cat_en": "Other",
        "title_zh": "澳大利亚与英国签署50年AUKUS核潜艇合作条约",
        "title_en": "Australia and Britain sign 50-year AUKUS submarine treaty",
        "published": "00:00 2026年7月26日",
        "summary_zh": "澳潜艇局称《吉朗条约》涵盖SSN-AUKUS设计建造运维与处置，在吉朗签署并待两国议会批准。",
        "summary_en": "Australia's submarine agency says the Geelong Treaty covers SSN-AUKUS design, build, sustainment and disposal, signed Saturday pending ratification.",
        "source_zh": "澳大利亚潜艇局", "source_en": "Australian Submarine Agency",
        "url": "https://www.asa.gov.au/news/treaty-brings-ssn-aukus-step-closer",
        "tag": "#7f8c8d",
    },
]

# Fix Gande typo in title
ITEMS[6]["title_zh"] = "我国启动商业太空碎片监测「甘德星座」建设"
ITEMS[6]["summary_zh"] = "新华社称首颗甘德星座卫星已发射，规划120颗卫星在2030年前实现全轨道目标探测。"


def build_html(items):
    n = len(items)
    cats_order = []
    for it in items:
        key = (it["cat_zh"], it["cat_en"])
        if key not in cats_order:
            cats_order.append(key)

    by_cat = {k: [] for k in cats_order}
    for it in items:
        by_cat[(it["cat_zh"], it["cat_en"])].append(it)

    body_parts = []
    num = 0
    for cat_zh, cat_en in cats_order:
        body_parts.append(
            f'<h2 style="margin:28px 0 12px;padding:10px 12px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:17px;color:#1e293b;">{cat_zh} <span style="font-weight:normal;color:#64748b;font-size:14px;">/ {cat_en}</span></h2>'
        )
        for it in by_cat[(cat_zh, cat_en)]:
            num += 1
            nn = f"{num:02d}"
            body_parts.append(
                f'''<div style="margin:0 0 18px;padding:0 0 16px;border-bottom:1px solid #e8ecf1;">
<p style="margin:0 0 6px;font-size:12px;color:#64748b;font-weight:600;">{nn}</p>
<p style="margin:0 0 4px;font-size:16px;line-height:1.45;"><a href="{it["url"]}" style="color:#1d4ed8;text-decoration:none;font-weight:600;">{it["title_zh"]}</a></p>
<p style="margin:0 0 4px;font-size:14px;line-height:1.4;color:#334155;font-style:italic;">{it["title_en"]}</p>
<p style="margin:0 0 8px;font-size:12px;color:#94a3b8;">发布时间 Published: {it["published"]}</p>
<p style="margin:0 0 6px;font-size:14px;line-height:1.55;color:#334155;">{it["summary_zh"]}</p>
<p style="margin:0 0 10px;font-size:13px;line-height:1.5;color:#475569;">{it["summary_en"]}</p>
<p style="margin:0;font-size:12px;"><span style="display:inline-block;padding:2px 8px;border-radius:4px;background:{it["tag"]};color:#fff;margin-right:8px;">{it["source_zh"]} / {it["source_en"]}</span><a href="{it["url"]}" style="color:#2563eb;">查看全文 Read more →</a></p>
</div>'''
            )

    body = "\n".join(body_parts)
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>每日热点晚报</title></head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef1f5;"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;box-shadow:0 4px 20px rgba(15,23,42,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1e3a5f,#0f172a);padding:28px 24px;color:#fff;">
<h1 style="margin:0 0 8px;font-size:24px;font-weight:700;">每日热点晚报</h1>
<p style="margin:0 0 4px;font-size:14px;opacity:.92;">Evening News Briefing · 2026年7月26日 · 共 {n} 条</p>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
<p style="margin:0 0 6px;font-size:15px;line-height:1.6;color:#1e293b;">汇总今日全日要闻：台风「红霞」登陆华南、香港逐步恢复交通，中东局势与欧陆野火持续牵动市场与民生。</p>
<p style="margin:0;font-size:14px;line-height:1.55;color:#475569;">Today&apos;s main stories: Typhoon Noul hits southern China as Hong Kong reopens transport, while Middle East tensions and European wildfires keep global attention.</p>
</td></tr>
<tr><td style="padding:8px 24px 24px;">
{body}
</td></tr>
<tr><td style="padding:20px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:11px;line-height:1.6;color:#64748b;">
<p style="margin:0 0 8px;">本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归原媒体所有。</p>
<p style="margin:0;">This digest compiles publicly reported news for informational purposes only; not investment or legal advice. Rights remain with original publishers.</p>
</td></tr>
</table></td></tr></table>
</body></html>'''
    return html


def main():
    html = build_html(ITEMS)
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-07-26",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out}, {len(html)} chars, {len(ITEMS)} items")


if __name__ == "__main__":
    main()
