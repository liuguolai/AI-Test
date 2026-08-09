#!/usr/bin/env python3
"""Build evening briefing HTML and email_payload.json for 2026-08-09."""
import json
import os

DATE = "2026-08-09"
BRIEFING_EDITION = "晚报"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中国7月PPI与CPI涨幅均低于预期，通缩压力仍存",
            "en_title": "China's July PPI and CPI rise less than expected as deflation pressure persists",
            "published": "12:01 2026年8月9日",
            "zh_summary": "官方数据显示7月PPI同比涨3.5%、核心CPI涨0.9%，均弱于预期，能源回落与内需疲软压制通胀。",
            "en_summary": "Official data showed July PPI rose 3.5% and core CPI 0.9%, both below forecasts as energy prices fell and domestic demand stayed weak.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.businesstimes.com.sg/international/china-consumer-factory-prices-rise-less-expected-deflationary-pressure-persists",
        },
        {
            "zh_title": "我国渤海首个千亿方大气田渤中19-6一期全面投产",
            "en_title": "China's first 100-billion-cubic-meter Bohai gas field phase I fully operational",
            "published": "08:00 2026年8月9日",
            "zh_summary": "中国海油称渤中19-6气田一期全面投产，日产油气当量超5200吨，将优化区域能源结构。",
            "en_summary": "CNOOC said the Bozhong 19-6 gas field phase I is fully online, producing over 5,200 tonnes of oil and gas equivalent daily.",
            "source_zh": "新华财经 Xinhua Finance",
            "source_en": "Xinhua Finance",
            "url": "https://m.cnfin.com/yw-lb//zixun/20260809/4452817_1.html",
        },
        {
            "zh_title": "7月先进制造领域投资同比大增73.1%",
            "en_title": "Advanced manufacturing investment surged 73.1% year-on-year in July",
            "published": "08:00 2026年8月9日",
            "zh_summary": "国家发改委信息中心数据显示，7月先进制造投资金额同比增73.1%，算力等新基建项目中标额亦回升。",
            "en_summary": "NDRC data showed advanced manufacturing investment jumped 73.1% in July, with new infrastructure project awards also edging up.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "https://m.cnfin.com/yw-lb//zixun/20260809/4452817_1.html",
        },
        {
            "zh_title": "上半年人形机器人领域新设企业11.6万户",
            "en_title": "China registered 116,000 new humanoid robot firms in first half of 2026",
            "published": "08:00 2026年8月9日",
            "zh_summary": "市场监管总局称上半年人形机器人新设企业11.6万户，同比增9.5%，新产业新赛道经营主体动能持续增强。",
            "en_summary": "Market regulators said 116,000 humanoid robot firms were newly registered in H1, up 9.5%, highlighting momentum in emerging industries.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "https://m.cnfin.com/yw-lb//zixun/20260809/4452817_1.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "中国开源AI模型压低价格，分析师称长期或大幅提振需求",
            "en_title": "Cheap Chinese open-weight AI models may turbocharge industry growth, analysts say",
            "published": "17:00 2026年8月9日",
            "zh_summary": "SCMP称中国开源模型倒逼硅谷降价，LLM推理价自6月初大幅回落，长期或加速全球AI应用普及。",
            "en_summary": "SCMP reports Chinese open models forced Silicon Valley price cuts; analysts say falling inference costs could accelerate global AI adoption.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/tech/big-tech/article/3363381/chinas-ai-models-spooked-wall-street-they-may-turbocharge-industry-growth",
        },
        {
            "zh_title": "谷歌AI高层大洗牌：Jeff Dean离职创办Discovery Loop",
            "en_title": "Google reshuffles AI leadership as Jeff Dean leaves to found Discovery Loop",
            "published": "00:00 2026年8月5日",
            "zh_summary": "Demis Hassabis卸任DeepMind日常管理，Jeff Dean等四名资深研究员离职创业，Alphabet股价下跌约4%。",
            "en_summary": "Demis Hassabis stepped back from daily DeepMind leadership as Jeff Dean and three senior researchers left to launch Discovery Loop; Alphabet shares fell about 4%.",
            "source_zh": "CNBC",
            "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/05/google-chief-scientist-jeff-dean-leaving-company-after-27-years.html",
        },
        {
            "zh_title": "四名顶尖谷歌AI研究员获Alphabet投资创立Discovery Loop",
            "en_title": "Four top Google AI researchers launch Discovery Loop with Alphabet backing",
            "published": "00:04 2026年8月6日",
            "zh_summary": "《纽约时报》称Jeff Dean、Sanjay Ghemawat等四人创立Discovery Loop，聚焦AI自动化科学发现，获谷歌母公司投资与算力支持。",
            "en_summary": "The New York Times says Jeff Dean, Sanjay Ghemawat and two others founded Discovery Loop to automate scientific discovery with Alphabet funding and compute.",
            "source_zh": "纽约时报 The New York Times",
            "source_en": "The New York Times",
            "url": "https://archive.ph/Pogl7",
        },
        {
            "zh_title": "阿里巴巴拟对Qwen下一版开源模型大客户收取收入分成",
            "en_title": "Alibaba plans revenue share from major users of next Qwen open-source model",
            "published": "09:08 2026年8月7日",
            "zh_summary": "路透社独家称阿里下周发布Qwen新版本时，将要求大客户分享其通过模型获得的收入，中国AI商业化路径趋同。",
            "en_summary": "Reuters reports Alibaba will ask major users of the next Qwen model to share revenue, signaling convergence in Chinese AI monetization strategies.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://ca.finance.yahoo.com/news/exclusive-alibaba-plans-charge-big-010847902.html",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "胡塞武装宣称无人机袭击沙特阿美Jazan炼厂",
            "en_title": "Houthis claim drone attack on Saudi Aramco's Jazan refinery",
            "published": "11:55 2026年8月9日",
            "zh_summary": "也门胡塞武装宣称精确打击日处理40万桶的Jazan炼厂；沙特能源部称火已扑灭、无人受伤，未确认袭击原因。",
            "en_summary": "Yemen's Houthis claimed a precise strike on the 400,000-bpd Jazan refinery; Saudi authorities said the fire was extinguished with no injuries reported.",
            "source_zh": "The National",
            "source_en": "The National",
            "url": "https://www.thenationalnews.com/business/energy/2026/08/09/fire-at-saudi-arabias-400000-bpd-jazan-refinery-brought-under-control/",
        },
        {
            "zh_title": "沙特阿美Jazan炼厂清晨火灾已扑灭",
            "en_title": "Fire at Saudi Aramco Jazan refinery extinguished early Sunday",
            "published": "09:52 2026年8月9日",
            "zh_summary": "沙特能源部称阿美工业消防队已扑灭Jazan炼厂设施火灾，正处理后续事宜，暂未说明是否影响生产。",
            "en_summary": "Saudi Arabia's Energy Ministry said Aramco fire teams extinguished a blaze at the Jazan complex; production impact remains unclear.",
            "source_zh": "Arab News",
            "source_en": "Arab News",
            "url": "https://www.arabnews.com/node/2653950/saudi-arabia",
        },
        {
            "zh_title": "德国暂停批准可用于加沙的军事装备对以色列出口",
            "en_title": "Germany halts military exports to Israel that could be used in Gaza",
            "published": "00:00 2026年8月8日",
            "zh_summary": "默茨称以色列加强加沙军事行动使德国更难看到实现停火与解救人质目标，将暂停批准可用于加沙的军备出口。",
            "en_summary": "Chancellor Merz said intensified Gaza operations make Germany's war goals harder to achieve and halted approvals for weapons usable in Gaza.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/germany-mideast-weapons-b957e28b73ee94ed33fbd2d4e4d36246",
        },
        {
            "zh_title": "Alphabet拟通过发债筹集至多250亿美元支撑AI支出",
            "en_title": "Alphabet seeks up to $25 billion in bond offering to fund AI spending",
            "published": "00:00 2026年8月6日",
            "zh_summary": "彭博称谷歌母公司拟发行2至40年期债券融资AI投入，此前已出现史上首次负自由现金流并上调资本支出指引。",
            "en_summary": "Bloomberg reports Alphabet plans a multi-tranche bond sale to fund AI spending after posting its first negative free cash flow and raising capex guidance.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.reuters.com/business/google-shakes-up-ai-leadership-deepmind-chief-shifts-role-2026-08-05/",
        },
        {
            "zh_title": "韩国股市杠杆平仓后波动或趋缓，外资周五大举回流",
            "en_title": "Korea market volatility may ease after leverage unwind; foreigners bought heavily Friday",
            "published": "00:00 2026年8月9日",
            "zh_summary": "彭博称韩国单股杠杆ETF强制平仓接近尾声，KOSPI前瞻市盈率接近历史低位，周五外资单日净买入创纪录。",
            "en_summary": "Bloomberg says forced unwinding of Korean leveraged ETFs may be ending; foreigners bought a record 7.2 trillion won of shares on Friday.",
            "source_zh": "彭博 Bloomberg",
            "source_en": "Bloomberg",
            "url": "https://www.theglobeandmail.com/investing/article-big-investors-think-it-might-be-time-to-buy-in-south-korea/",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "长崎举行原爆81周年悼念，市长警告核威慑风险上升",
            "en_title": "Nagasaki marks 81st A-bomb anniversary as mayor warns nuclear deterrence raises war risk",
            "published": "11:45 2026年8月9日",
            "zh_summary": "铃木市长称核武器是“绝对之恶”，呼吁各国领导人正视依赖核威慑将增加核战风险，高市早苗重申坚持无核三原则。",
            "en_summary": "Mayor Suzuki called nuclear weapons absolute evil and warned deterrence increases war risk; PM Takaichi reiterated Japan upholds its three non-nuclear principles.",
            "source_zh": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/asia/east-asia/update2-nagasaki-warns-of-risk-of-nuclear-war-on-81st-a-bomb-anniversary",
        },
        {
            "zh_title": "泰国校园枪击案12岁女生伤重不治，死亡人数升至至少8人",
            "en_title": "Thailand school shooting death toll rises to at least eight after girl dies",
            "published": "00:00 2026年8月9日",
            "zh_summary": "曼谷北部学校枪击案一名12岁女生周六伤重不治，连同枪手及其祖父母在内至少8人死亡，14人仍在住院。",
            "en_summary": "A 12-year-old girl died Saturday from wounds in the Nonthaburi school shooting, bringing the death toll to at least eight; fourteen remain hospitalized.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/thailand-school-shooting-nonthaburi-bodies-forensic-63f7b1f3b97842251c98b5932f1d234a",
        },
        {
            "zh_title": "阿富汗撤离五周年：21岁女生在英成为护生追寻梦想",
            "en_title": "Five years after Kabul evacuation, Afghan refugee becomes student nurse in UK",
            "published": "15:30 2026年8月9日",
            "zh_summary": "BBC报道21岁Pervin 2021年从喀布尔撤离后在诺丁汉郡安家，现为伯明翰城市大学护生，称在英获得自由与新生。",
            "en_summary": "BBC profiles Pervin Juma, evacuated from Kabul in 2021, now a nursing student in Birmingham who says she finally feels free in the UK.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cevm0n1jldjo",
        },
        {
            "zh_title": "加拿大BC省山火迫使逾2万人疏散，全省进入紧急状态",
            "en_title": "Wildfires force 20,000 to flee as British Columbia declares state of emergency",
            "published": "00:00 2026年8月9日",
            "zh_summary": "AP称Bald Range山火周六迅速蔓延，Summerland全镇及Peachland周边约2万人连夜撤离，多架飞机救出被困居民。",
            "en_summary": "AP reports the Bald Range wildfire forced about 20,000 people to evacuate Summerland and Peachland overnight; aircraft rescued trapped residents.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/wildfire-canada-evacuation-british-columbia-okanagan-61002c95f641a4060b78195b016fbea3",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特拉维夫数千人抗议内塔尼亚胡扩大加沙军事行动计划",
            "en_title": "Thousands rally in Tel Aviv against Netanyahu's plan to escalate Gaza war",
            "published": "00:00 2026年8月9日",
            "zh_summary": "路透社称周六夜数千示威者要求立即结束加沙战争并解救被扣押人质，反对安全内阁扩大对加沙城军事行动的决定。",
            "en_summary": "Reuters says thousands protested Saturday night in Tel Aviv demanding an end to the Gaza war and hostage releases, opposing expanded military operations.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.reuters.com/world/middle-east/thousands-rally-tel-aviv-against-netanyahus-new-gaza-plan-demand-release-2025-08-10/",
        },
        {
            "zh_title": "伊朗威胁阻断阿塞拜疆-亚美尼亚和平协议中的特朗普走廊",
            "en_title": "Iran threatens to block Trump corridor planned in Azerbaijan-Armenia peace deal",
            "published": "00:00 2026年8月9日",
            "zh_summary": "伊朗最高领袖顾问瓦拉亚蒂警告可能阻断经亚美尼亚南部连接阿塞拜疆与纳希切万的TRIPP走廊，质疑地区安全安排。",
            "en_summary": "Iranian adviser Velayati threatened to block the TRIPP corridor through southern Armenia linking Azerbaijan to Nakhchivan under a US-backed peace plan.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.reuters.com/world/middle-east/iran-threatens-planned-trump-corridor-envisaged-by-azerbaijan-armenia-peace-deal-2025-08-09/",
        },
        {
            "zh_title": "CIA在阿富汗行动中误捕美国公民，释放努力陷入僵局",
            "en_title": "CIA al-Qaeda strike ensnared US citizen in Afghanistan, complicating release efforts",
            "published": "00:00 2026年8月9日",
            "zh_summary": "路透社称自然化美国公民Mahmood Habibi 2023年在喀布尔失踪，塔利班否认拘押，美方悬赏500万美元促其获释。",
            "en_summary": "Reuters reports naturalized US citizen Mahmood Habibi disappeared in Kabul in 2023; the Taliban deny holding him as the US offers a $5 million reward.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.reuters.com/world/asia-pacific/how-cia-hit-al-qaeda-ensnared-us-citizen-afghanistan-2025-08-09/",
        },
        {
            "zh_title": "特朗普再签行政令试图限制出生公民权与赴美生子",
            "en_title": "Trump issues new executive orders to limit birthright citizenship",
            "published": "00:00 2026年8月7日",
            "zh_summary": "AP称白宫周四发布较窄范围新令，针对赴美生子、外国外交人员子女等类别，预计仍将面临法律挑战。",
            "en_summary": "AP says new narrower orders target birth tourism and children of foreign officials, and are expected to face further legal challenges after a Supreme Court setback.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/birthright-citizenship-immigration-trump-07cf9d5f493e57d6fc652bf6f17edd92",
        },
        {
            "zh_title": "伦敦警方在挺Palestine Action示威中逮捕逾500人创纪录",
            "en_title": "London police arrest over 500 at Palestine Action support protest",
            "published": "00:00 2026年8月9日",
            "zh_summary": "BBC称周六威斯敏斯特示威中警方逮捕474人，多数因展示支持被取缔团体Palestine Action的标语，为近年单次行动最多。",
            "en_summary": "BBC reports police arrested 474 people at Saturday's Westminster protest, mostly for displaying placards supporting banned group Palestine Action.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c8de6rq37v5o",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "警方破获涉6亿港元洗钱三合会集团拘捕147人",
            "en_title": "Police dismantle triad syndicate laundering HK$600 million, arrest 147",
            "published": "14:02 2026年8月9日",
            "zh_summary": "警方“Rapidhorse”行动打击贩毒赌博及洗钱账户中心，拘捕包括主脑在内147人，查获现金及奢侈品等约500万港元财物。",
            "en_summary": "Police operation Rapidhorse targeted drug and gambling dens and laundering hubs, arresting 147 people and seizing about HK$5 million in assets.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363430/police-dismantle-alleged-triad-group-ran-account-centres-launder-hk600-million",
        },
        {
            "zh_title": "太古城住宅火灾12人不适送医，逾20人暂避天台",
            "en_title": "Taikoo Shing flat fire sends at least 12 to hospital for smoke inhalation",
            "published": "16:48 2026年8月9日",
            "zh_summary": "周日下午太古城海棠阁单位起火，疑与空调故障有关，至少12人因吸入烟雾不适送医，20余人暂避天台后安全撤离。",
            "en_summary": "A Sunday afternoon fire at Begonia Mansion in Taikoo Shing sent at least 12 people to hospital; more than 20 residents fled to the rooftop before escaping safely.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3363441/least-12-taken-hospital-after-fire-breaks-out-taikoo-shing-flat",
        },
        {
            "zh_title": "台风白海豚外围下沉气流致港刷新年内最高温36度",
            "en_title": "Typhoon Dolphin's subsiding air pushes Hong Kong to 36°C yearly high",
            "published": "13:21 2026年8月9日",
            "zh_summary": "天文台总部周日下午录36度创今年新高，上水38.3度，白海豚趋向浙江福建登陆，酷热天气料持续至本周中。",
            "en_summary": "The Observatory recorded 36°C at headquarters Sunday afternoon, with Sheung Shui hitting 38.3°C as Dolphin moved toward Zhejiang and Fujian.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363429/hong-kong-breaks-record-hottest-day-typhoon-dolphin-brings-extreme-heat",
        },
        {
            "zh_title": "警方打击三合会行动拘147人，瓦解洗钱链条",
            "en_title": "Hong Kong police arrest 147 in anti-triad operation, smash laundering chain",
            "published": "16:17 2026年8月9日",
            "zh_summary": "RTHK引警方称行动拘捕主脑及骨干，涉去年1月至本月通过傀儡账户洗钱6亿港元，查获现金、名表及毒品等财物。",
            "en_summary": "RTHK reports police arrested the suspected mastermind and key members for laundering HK$600 million via stooge accounts since January 2025.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865540-20260809.htm",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "DeepSeek预告API将大幅涨价，低成本策略承压",
            "en_title": "DeepSeek signals major API price hike after building cost advantage",
            "published": "00:00 2026年8月8日",
            "zh_summary": "DeepSeek称近期将显著上调API价格，V4 Flash虽仍远低于欧美竞品，但开发者需重新评估用量与多模型路由成本。",
            "en_summary": "DeepSeek warned of a significant upcoming API price increase; developers may need to reassess budgets despite V4 Flash remaining far cheaper than Western rivals.",
            "source_zh": "The Enterprise News",
            "source_en": "The Enterprise News",
            "url": "https://theenterprise.news/technology/ai/deepseek-moves-to-reprice-ai-after-building-a-cost-advantage/",
        },
        {
            "zh_title": "韩国单股杠杆ETF成交额首次跌破1万亿韩元",
            "en_title": "Korea single-stock leveraged ETF turnover falls below 1 trillion won for first time",
            "published": "00:00 2026年8月5日",
            "zh_summary": "韩国交易所数据显示，三星与SK海力士杠杆ETF合计成交额降至9198亿韩元，监管提高保证金后散户杠杆交易明显降温。",
            "en_summary": "Korea Exchange data showed leveraged ETF turnover on Samsung and SK Hynix fell to 919.8 billion won as tighter deposit rules cooled retail leverage trading.",
            "source_zh": "Bloomingbit",
            "source_en": "Bloomingbit",
            "url": "https://en.bloomingbit.io/feed/news/117819",
        },
    ]),
]

SOURCE_COLORS = {
    "Reuters": "#0066CC", "AP": "#CC0000", "BBC": "#000000", "SCMP": "#1a5276",
    "CNBC": "#00529B", "Bloomberg": "#601942", "RTHK": "#2e7d32",
    "The National": "#8B4513", "Arab News": "#006400", "The Straits Times": "#c0392b",
    "The New York Times": "#333333", "Xinhua": "#b71c1c", "Xinhua Finance": "#b71c1c",
    "The Enterprise News": "#555555", "Bloomingbit": "#6a1b9a",
}


def get_color(source_en):
    for k, v in SOURCE_COLORS.items():
        if k.lower() in source_en.lower():
            return v
    return "#555555"


def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    items_html = []
    n = 0
    for cat_zh_en, items in CATEGORIES:
        items_html.append(
            f'<h2 style="margin:24px 0 12px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:16px;color:#1e293b;">{cat_zh_en}</h2>'
        )
        for item in items:
            n += 1
            num = f"{n:02d}"
            color = get_color(item["source_en"])
            items_html.append(
                f'<div style="margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #e8ecf1;">'
                f'<div style="font-size:11px;color:#2563eb;font-weight:bold;margin-bottom:4px;">{num}</div>'
                f'<a href="{item["url"]}" style="font-size:15px;font-weight:bold;color:#1e40af;text-decoration:none;line-height:1.4;">{item["zh_title"]}</a>'
                f'<div style="font-size:13px;color:#64748b;font-style:italic;margin-top:4px;line-height:1.4;">{item["en_title"]}</div>'
                f'<div style="font-size:11px;color:#94a3b8;margin-top:4px;">发布时间 Published: {item["published"]}</div>'
                f'<div style="font-size:13px;color:#334155;margin-top:8px;line-height:1.5;">{item["zh_summary"]}</div>'
                f'<div style="font-size:12px;color:#64748b;margin-top:4px;line-height:1.4;">{item["en_summary"]}</div>'
                f'<div style="margin-top:8px;">'
                f'<span style="display:inline-block;padding:2px 8px;background:{color};color:#fff;font-size:10px;border-radius:3px;margin-right:6px;">{item["source_zh"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>'
                f'</div></div>'
            )

    body = "\n".join(items_html)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;padding:16px;">
<div style="background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">
<div style="background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);padding:28px 24px;color:#fff;">
<h1 style="margin:0;font-size:22px;font-weight:700;">每日热点晚报</h1>
<div style="font-size:14px;margin-top:6px;opacity:0.9;">Evening News Briefing · {DATE} · 共 {total} 条</div>
</div>
<div style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0;">
<div style="font-size:14px;color:#334155;line-height:1.6;">汇总今日全日要闻，涵盖国内政策、市场动态、科技前沿与国际热点。</div>
<div style="font-size:13px;color:#64748b;margin-top:6px;line-height:1.5;">Today's main stories across China, markets, technology and world affairs.</div>
</div>
<div style="padding:16px 24px 24px;">
{body}
</div>
<div style="padding:16px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:11px;color:#94a3b8;line-height:1.6;">
<div>本简报由自动化系统汇编，仅供参考，不构成投资建议。新闻版权归原媒体所有。</div>
<div style="margin-top:4px;">This briefing is automatically compiled for reference only and does not constitute investment advice. News copyrights belong to original publishers.</div>
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
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    payload_path = os.path.join(root, "email_payload.json")
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    total = sum(len(items) for _, items in CATEGORIES)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total items: {total}")
    print(f"HTML length: {len(html)}")
    print(f"Written to {payload_path}")


if __name__ == "__main__":
    main()
