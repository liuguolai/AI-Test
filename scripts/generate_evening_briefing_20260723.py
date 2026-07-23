#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-23."""
import json
import os

DATE = "2026-07-23"
DATE_CN = "2026年7月23日"
BRIEFING_EDITION = "晚报"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE}"

CATEGORIES = [
    ("domestic", "国内 · China Mainland", [
        {
            "zh_title": "王毅马尼拉会见鲁比奥 要求美方尊重中方核心利益",
            "en_title": "Wang Yi Tells Rubio in Manila to Respect China's Core Interests",
            "published": "11:27 2026年7月23日",
            "zh_summary": "王毅与鲁比奥在马尼拉会谈，敦促美方恪守一个中国原则、妥善管控分歧，双方称会晤务实积极。",
            "en_summary": "Wang Yi urged Marco Rubio to uphold the one-China principle and manage disputes as both sides called their Manila talks constructive.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/wang-rubio-seek-to-advance-us-china-talks-after-leaders-beijing-meeting-102467221.html",
        },
        {
            "zh_title": "商务部强烈不满欧盟重罚速卖通 警告或采取反制",
            "en_title": "Beijing Slams EU's €550M AliExpress Fine, Warns of Countermeasures",
            "published": "03:30 2026年7月23日",
            "zh_summary": "欧盟以《数字服务法》对阿里速卖通开出5.5亿欧元罚单，中方批评其歧视性执法并反对法国快时尚立法。",
            "en_summary": "China condemned the EU's €550 million AliExpress fine and criticized French fast-fashion legislation as discriminatory trade barriers.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/beijing-pushes-back-as-europe-tightens-pressure-on-chinese-e-commerce-102467126.html",
        },
        {
            "zh_title": "第十二批国家药品集采7月31日开标 覆盖65个品种",
            "en_title": "China's 12th National Drug Bulk Procurement to Open Bids on July 31",
            "published": "11:13 2026年7月23日",
            "zh_summary": "第十二批集采覆盖肿瘤、心血管等65个品种，新规允许部分原研药“中选不带量”重返公立医院市场。",
            "en_summary": "The 12th centralized procurement round covers 65 drugs, with new rules letting some originator medicines re-enter hospitals without volume quotas.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/china-offers-brand-name-drugmakers-a-lifeline-in-bulk-procurement-tender-102467214.html",
        },
        {
            "zh_title": "中国人形机器人迈向批量交付 业界呼吁加快安全标准",
            "en_title": "China's Humanoid Robots Near Mass Delivery as Safety Rules Urged",
            "published": "08:48 2026年7月23日",
            "zh_summary": "专家称人形机器人正从样机演示转向批量交付，规模化应用亟需统一安全、数据与评测标准。",
            "en_summary": "Experts say humanoid robots are shifting from prototypes to batch delivery, calling for unified safety, data and testing standards at scale.",
            "source_zh": "中国日报 China Daily",
            "source_en": "China Daily",
            "url": "https://www.chinadaily.com.cn/a/202607/23/WS6a6164c6a310986e2b466c71.html",
        },
    ]),
    ("tech", "科技 · Technology", [
        {
            "zh_title": "AMD拟向Anthropic投资至多50亿美元 部署2吉瓦算力",
            "en_title": "AMD to Invest Up to $5B in Anthropic, Deploy 2GW of AI Chips",
            "published": "22:44 2026年7月22日",
            "zh_summary": "AMD与Anthropic达成战略合作，将部署MI450系列GPU并开展多年工程协作，首批1吉瓦2027年上半年上线。",
            "en_summary": "AMD will invest up to $5 billion in Anthropic and deploy MI450 GPUs, with the first gigawatt of capacity due online in H1 2027.",
            "source_zh": "The Verge",
            "source_en": "The Verge",
            "url": "https://www.theverge.com/ai-artificial-intelligence/969285/amd-anthropic-ai-infrastructure-deal",
        },
        {
            "zh_title": "鲁比奥要求外交官淡化美国科技“终止开关”说法",
            "en_title": "Rubio Tells Diplomats to Play Down U.S. Tech 'Kill Switch' Talk",
            "published": "09:27 2026年7月23日",
            "zh_summary": "美国务院电报称暂停模型访问不等于“魔法按钮”，并指示外交官反击“数字主权”倡议、推销美国AI。",
            "en_summary": "A State Department cable says pausing model access is not a 'magic button' and tells diplomats to counter digital sovereignty pushes.",
            "source_zh": "路透社 Reuters / CNA",
            "source_en": "Reuters / CNA",
            "url": "https://www.channelnewsasia.com/business/exclusive-marco-rubio-tells-diplomats-play-down-talk-american-tech-kill-switch-6270691",
        },
        {
            "zh_title": "谷歌母公司自由现金流转负 全年AI资本支出或达2050亿美元",
            "en_title": "Alphabet Posts Negative Free Cash Flow as AI Capex May Hit $205B",
            "published": "15:35 2026年7月23日",
            "zh_summary": "Alphabet二季度自由现金流为负59亿美元，并将2026年资本支出指引上调至1950亿至2050亿美元，盘后股价下跌。",
            "en_summary": "Alphabet reported negative $5.9bn free cash flow and raised 2026 capex guidance to up to $205bn, sending shares lower after hours.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c235n47g8g8o",
        },
        {
            "zh_title": "中国拟人化AI互动新规落地 豆包通义等下架陪伴功能",
            "en_title": "China's AI Companion Rules Take Effect; Major Apps Disable Features",
            "published": "09:30 2026年7月23日",
            "zh_summary": "7月15日起实施的新规禁止向未成年人提供虚拟亲属或恋人，字节、阿里等已关闭相关AI陪伴服务。",
            "en_summary": "Rules effective July 15 ban virtual relatives or partners for minors, prompting ByteDance, Alibaba and others to disable companion features.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/opinion/china-opinion/article/3361300/chinas-crackdown-ai-companions-wont-fill-emotional-void",
        },
    ]),
    ("finance", "财经 · Finance & Business", [
        {
            "zh_title": "美股收跌 油价创六周新高拖累纳指",
            "en_title": "U.S. Stocks Slip as Oil Hits Six-Week High, Nasdaq Leads Decline",
            "published": "07:03 2026年7月23日",
            "zh_summary": "道指基本持平，标普500跌0.14%，纳指跌0.57%；布伦特原油收涨约3%至94美元上方，通胀担忧升温。",
            "en_summary": "The Dow was flat, the S&P 500 fell 0.14% and the Nasdaq dropped 0.57% as Brent crude rose about 3% above $94, stoking inflation fears.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.thestar.com.my/business/2026/07/23/wall-st-dips-as-oil-tech-earnings-take-focus",
        },
        {
            "zh_title": "特斯拉二季度营收增26% 利润不及预期自由现金流转负",
            "en_title": "Tesla Revenue Rises 26% but Profit Misses, Free Cash Flow Turns Negative",
            "published": "07:00 2026年7月23日",
            "zh_summary": "特斯拉Q2营收282亿美元超预期，调整后每股收益33美分远低于预期，自由现金流赤字约11亿美元。",
            "en_summary": "Tesla's Q2 revenue of $28.2bn beat estimates but adjusted EPS of 33 cents missed badly, with a $1.1bn free cash flow deficit.",
            "source_zh": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/business/tesla-profit-falls-well-short-of-estimates-as-costs-rise",
        },
        {
            "zh_title": "万科获深铁5.19亿元借款 完成2026年公募债展期",
            "en_title": "Vanke Gets $77M Loan from Shenzhen Metro, Completes 2026 Bond Extensions",
            "published": "03:13 2026年7月23日",
            "zh_summary": "深铁年内第五次向万科输血，累计新增支持45亿元，用于偿付两笔境内债券本息。",
            "en_summary": "Shenzhen Metro's fifth liquidity injection this year brings total 2026 support to 4.5 billion yuan to cover two domestic bond obligations.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/vanke-wins-new-funding-as-it-completes-extensions-on-2026-public-bonds-102467124.html",
        },
        {
            "zh_title": "耐克终止滔搏内地线上销售权 分销商股价暴跌近25%",
            "en_title": "Nike Ends Topsports' Mainland Online Rights; Shares Plunge Nearly 25%",
            "published": "01:04 2026年7月23日",
            "zh_summary": "耐克将于2027年1月1日起收回滔搏中国内地线上经销权，以整合数字渠道、遏制电商价格战。",
            "en_summary": "Nike will terminate Topsports' mainland online sales rights from Jan 1, 2027, consolidating digital channels and curbing online price wars.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/nike-ends-topsports-online-sales-rights-on-the-chinese-mainland-in-digital-overhaul-102467120.html",
        },
        {
            "zh_title": "欧股走低 意法半导体业绩指引拖累芯片股",
            "en_title": "European Shares Slip as STMicro Outlook Drags Chip Stocks Lower",
            "published": "16:08 2026年7月23日",
            "zh_summary": "STOXX 600跌0.5%，科技板块领跌；意法半导体因三季度营收指引偏弱大跌15%，油价突破96美元支撑能源股。",
            "en_summary": "The STOXX 600 fell 0.5% led by tech; STMicro plunged 15% on a soft Q3 outlook while oil above $96 boosted energy shares.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-slip-as-tech-stocks-drag-ecb-policy-decision-in-focus/articleshow/132575316.cms",
        },
    ]),
    ("society", "社会 · Society", [
        {
            "zh_title": "法国6月热浪致超额死亡约5700人 创2003年以来新高",
            "en_title": "France Records 5,700 Excess Deaths in June Heat Wave",
            "published": "00:00 2026年7月23日",
            "zh_summary": "法国公共卫生署称6月17日至7月2日热浪相关超额死亡5764人，为2003年以来最严重高温事件。",
            "en_summary": "Public Health France said the June 17–July 2 heat wave caused 5,764 excess deaths, the worst toll since 2003.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/france-heatwave-extra-deaths-health-agency-dff2ed624e0cdad02f836d30ae3e878f",
        },
        {
            "zh_title": "全国发电装机突破40亿千瓦 上半年用电量增5.3%",
            "en_title": "China's Power Capacity Tops 4 Billion kW as H1 Use Rises 5.3%",
            "published": "17:20 2026年7月22日",
            "zh_summary": "国家能源局称截至6月底全国装机40.4亿千瓦，上半年用电量5.09万亿千瓦时，今夏负荷屡创新高。",
            "en_summary": "China's installed capacity reached 4.04 billion kW by end-June with H1 electricity use up 5.3%, as summer peak demand hit records.",
            "source_zh": "环球时报 Global Times",
            "source_en": "Global Times",
            "url": "https://www.globaltimes.cn/page/202607/1366545.shtml",
        },
        {
            "zh_title": "调查：56%中国临床人员日常使用AI 高于全球均值",
            "en_title": "Survey: 56% of Chinese Clinicians Use AI Daily, Above Global Average",
            "published": "16:05 2026年7月22日",
            "zh_summary": "爱思唯尔在世界人工智能大会发布报告，中国医生AI使用率56%超全球49%，但数据准确性与责任归属仍受质疑。",
            "en_summary": "An Elsevier report at WAIC found 56% of Chinese clinicians use AI daily versus 49% globally, though accuracy and liability concerns persist.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-22/chinese-doctors-outpace-global-peers-in-ai-adoption-amid-trust-concerns-102466992.html",
        },
    ]),
    ("world", "国际 · World", [
        {
            "zh_title": "胡塞武装袭击红海两艘沙特油轮 美方连续第12夜打击伊朗",
            "en_title": "Houthis Attack Two Saudi Tankers in Red Sea as U.S. Strikes Iran Again",
            "published": "10:33 2026年7月23日",
            "zh_summary": "胡塞称袭击Encelia与Layla号油轮，沙特证实船艏起火船员安全；美军同期对伊朗军事目标发动新一轮空袭。",
            "en_summary": "Houthis claimed strikes on the Encelia and Layla tankers; Saudi Arabia confirmed a bow fire with crew safe as the U.S. launched new strikes on Iran.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cpw9xzx9r4ko",
        },
        {
            "zh_title": "特朗普威胁霍尔木兹每袭船即摧毁伊朗一座桥梁或电厂",
            "en_title": "Trump Threatens to Destroy Iranian Bridge or Plant per Hormuz Attack",
            "published": "07:44 2026年7月23日",
            "zh_summary": "特朗普在社交媒体称，伊朗每次袭击霍尔木兹海峡船只，美国将轰炸并摧毁一座桥梁或发电厂。",
            "en_summary": "Trump said on social media that each Iranian attack on ships in the Strait of Hormuz would trigger U.S. destruction of one bridge or power plant.",
            "source_zh": "澳大利亚广播公司 ABC",
            "source_en": "ABC News (Australia)",
            "url": "https://www.abc.net.au/news/2026-07-23/trump-iran-war-bridges-power-plants-hormuz/106947132",
        },
        {
            "zh_title": "欧盟就第21轮对俄制裁达成协议 希腊获俄液化天然气运输豁免",
            "en_title": "EU Agrees 21st Russia Sanctions Package with Greek LNG Carve-Out",
            "published": "00:00 2026年7月23日",
            "zh_summary": "经数周谈判，欧盟大使批准削弱版制裁方案，允许希腊Dynagas等公司一年内继续向第三国运输俄液化天然气。",
            "en_summary": "EU ambassadors approved a watered-down 21st sanctions package allowing Greek firms like Dynagas to keep shipping Russian LNG to third countries for one year.",
            "source_zh": "Euractiv",
            "source_en": "Euractiv",
            "url": "https://www.euractiv.com/news/eu-agrees-to-watered-down-russia-sanctions-amid-greek-resistance/",
        },
        {
            "zh_title": "欧盟批准英国参与900亿欧元乌克兰支持贷款框架",
            "en_title": "EU Approves UK Participation in €90B Ukraine Support Loan",
            "published": "00:00 2026年7月22日",
            "zh_summary": "成员国批准英方加入贷款机制，乌方可向英国防务企业采购装备，伦敦将按合同份额分担借款成本。",
            "en_summary": "Member states approved UK participation, letting Ukraine procure from British defence firms with London contributing borrowing costs proportionally.",
            "source_zh": "欧盟理事会 European Council",
            "source_en": "European Council",
            "url": "https://www.consilium.europa.eu/en/press/press-releases/2026/07/22/ukraine-support-loan-eu-countries-approve-uk-participation-to-help-cover-ukraine-s-urgent-defence-needs/",
        },
        {
            "zh_title": "德国批准法俄合资核燃料项目 引发间谍与供应链安全争议",
            "en_title": "Germany Approves Controversial French-Russian Nuclear Fuel Project",
            "published": "00:58 2026年7月23日",
            "zh_summary": "下萨克森州批准Framatome与俄国家原子能公司合资生产核燃料棒，反对者担忧俄方借项目获取敏感设施信息。",
            "en_summary": "Lower Saxony approved a Framatome-Rosatom joint venture to produce fuel rods, drawing warnings of Russian espionage and supply-chain risks.",
            "source_zh": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/world/europe/germany-approves-controversial-french-russian-nuclear-project",
        },
    ]),
    ("hk", "香港本地 · Hong Kong", [
        {
            "zh_title": "香港首启全无人自动驾驶试验 机场岛取消车内安全员",
            "en_title": "Hong Kong Launches First Fully Driverless AV Trial on Airport Island",
            "published": "14:10 2026年7月23日",
            "zh_summary": "运输署扩大北 Lantau 自动驾驶试点，机场岛路线首次允许车内无备份驾驶员，仅远程监控。",
            "en_summary": "The Transport Department expanded North Lantau AV trials, allowing Airport Island routes to operate without in-vehicle backup drivers, monitored remotely.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/transport/article/3361563/hong-kong-gears-citys-first-test-run-fully-driverless-vehicles",
        },
        {
            "zh_title": "中际旭创港股IPO每手逾5.1万港元 创港股认购门槛纪录",
            "en_title": "Zhongji IPO Sets Hong Kong's Highest Subscription Threshold at HK$51,009",
            "published": "17:00 2026年7月23日",
            "zh_summary": "中际旭创今日启动招股，发行价上限1010港元、每手50股，机构认购已超额，零售门槛创港股新高。",
            "en_summary": "Zhongji Innolight began its IPO at up to HK$1,010 per share with a HK$51,009 minimum lot, drawing strong institutional demand.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/business/companies/article/3361586/zhongji-sets-highest-subscription-threshold-hong-kong-ipo-history",
        },
        {
            "zh_title": "菲律宾低压或增强为台风 周末或逼近粤东影响香港",
            "en_title": "Philippines Depression May Become Typhoon, Approaching HK This Weekend",
            "published": "09:53 2026年7月23日",
            "zh_summary": "天文台称热带低压向西西北移动，周末或以台风强度在揭阳惠来登陆，本周末至周日粤岸有狂风暴雨。",
            "en_summary": "The Observatory said a tropical depression may intensify into a typhoon and land near eastern Guangdong this weekend, bringing strong winds and squalls.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3361525/philippines-storm-may-intensify-typhoon-approach-hong-kong-weekend",
        },
        {
            "zh_title": "香港拟扩大基金税收优惠 涵盖对冲基金与数字资产基金",
            "en_title": "Hong Kong Proposes Expanded Tax Breaks for Hedge and Digital-Asset Funds",
            "published": "01:57 2026年7月23日",
            "zh_summary": "政府6月刊宪法案拟豁免基金层面业绩报酬及基金经理附带权益的利得税与薪俸税，以巩固资管中心地位。",
            "en_summary": "A gazetted bill would exempt fund-level performance fees and managers' carried interest from profits and salaries tax to bolster the wealth hub.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/hong-kong-moves-to-expand-tax-breaks-for-funds-to-bolster-wealth-hub-appeal-102467122.html",
        },
    ]),
    ("other", "其他 · Other", [
        {
            "zh_title": "泰中合作博览会在曼谷开幕 270家企业展示创新合作",
            "en_title": "Thailand-China Cooperation Expo Opens in Bangkok with 270 Firms",
            "published": "07:03 2026年7月23日",
            "zh_summary": "泰国总理称博览会是双边关系“下一个50年”开局之举，涵盖AI、电动车、人形机器人及逾3000个职位招聘。",
            "en_summary": "Thailand's PM called the expo a start to the next 50 years of ties, covering AI, EVs, humanoid robots and over 3,000 job openings.",
            "source_zh": "新华社 Xinhua / 星洲日报",
            "source_en": "Xinhua / The Star",
            "url": "https://www.thestar.com.my/news/world/2026/07/23/roundup-thailand-china-expo-kicks-off-in-bangkok-to-expand-multi-sector-cooperation",
        },
    ]),
]

SOURCE_COLORS = {
    "Reuters": "#c41200", "BBC": "#bb1919", "AP": "#d32f2f", "Caixin": "#1a5276",
    "SCMP": "#2c3e50", "Xinhua": "#b71c1c", "The Verge": "#e74c3c",
    "ABC": "#1565c0", "Euractiv": "#2e7d32", "European Council": "#003399",
    "China Daily": "#c0392b", "Global Times": "#8e0000", "The Straits Times": "#1b4f72",
    "The Star": "#e65100", "CNA": "#0066b3",
}

def source_color(source_en):
    for k, v in SOURCE_COLORS.items():
        if k.lower() in source_en.lower():
            return v
    return "#555555"

def build_html():
    all_items = []
    for _, _, items in CATEGORIES:
        all_items.extend(items)
    n = len(all_items)

    parts = [f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">
<tr><td style="background:linear-gradient(135deg,#1a237e 0%,#283593 100%);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:700;">每日热点晚报</h1>
<p style="margin:0;color:#c5cae9;font-size:14px;">Evening News Briefing · {DATE_CN} · 共 {n} 条</p>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafafa;border-bottom:1px solid #e8e8e8;">
<p style="margin:0 0 8px;color:#333;font-size:14px;line-height:1.6;">汇总今日全日要闻，涵盖地缘政治、市场动态、科技与港澳本地热点。</p>
<p style="margin:0;color:#666;font-size:13px;font-style:italic;line-height:1.5;">Today's main stories across geopolitics, markets, technology and Greater China developments.</p>
</td></tr>
<tr><td style="padding:8px 0 16px;">''']

    idx = 0
    for _, cat_label, items in CATEGORIES:
        parts.append(f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="padding:16px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f5f5f5;border-left:4px solid #1565c0;font-size:16px;color:#1a237e;">{cat_label}</h2>
</td></tr></table>''')
        for item in items:
            idx += 1
            num = f"{idx:02d}"
            sc = source_color(item["source_en"])
            parts.append(f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="padding:12px 24px;border-bottom:1px solid #eee;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td width="36" valign="top" style="padding-right:10px;"><span style="display:inline-block;background:#1565c0;color:#fff;font-size:13px;font-weight:700;padding:4px 8px;border-radius:4px;">{num}</span></td>
<td valign="top">
<a href="{item['url']}" style="color:#1a237e;font-size:16px;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a>
<p style="margin:6px 0 4px;color:#555;font-size:14px;font-style:italic;line-height:1.4;">{item['en_title']}</p>
<p style="margin:0 0 8px;color:#999;font-size:12px;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 6px;color:#333;font-size:14px;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;color:#666;font-size:13px;line-height:1.5;">{item['en_summary']}</p>
<span style="display:inline-block;background:{sc};color:#fff;font-size:11px;padding:3px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="color:#1565c0;font-size:12px;text-decoration:none;">查看全文 Read more →</a>
</td></tr></table>
</td></tr></table>''')

    parts.append(f'''</td></tr>
<tr><td style="padding:20px 24px;background:#fafafa;border-top:1px solid #e8e8e8;">
<p style="margin:0 0 6px;color:#999;font-size:11px;line-height:1.5;">本简报仅供参考，不构成投资建议。新闻版权归原媒体所有。</p>
<p style="margin:0;color:#999;font-size:11px;line-height:1.5;">This briefing is for informational purposes only. All rights belong to original publishers.</p>
</td></tr>
</table></td></tr></table></body></html>''')
    return "".join(parts), n

def main():
    html, n = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total items: {n}")
    print(f"HTML length: {len(html)}")
    print(f"Written to {path}")

if __name__ == "__main__":
    main()
