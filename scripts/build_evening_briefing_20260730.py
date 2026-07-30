#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-30."""
import json
import os

BRIEFING_EDITION = "晚报"
LOCAL_TIME = "17:30 2026年7月30日"
DATE_STR = "2026-07-30"
DATE_CN = "2026年7月30日"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中国太阳能装机达12.7亿千瓦，年内有望超越煤电",
            "en_title": "China's solar capacity hits 1.27 billion kW, set to overtake coal this year",
            "published": "09:00 2026年7月30日",
            "zh_summary": "上半年光伏装机增速放缓66%，但发电量增逾四成，煤电占比首次跌破五成。",
            "en_summary": "Solar capacity reached 1.27 billion kW by June; H1 generation rose over 40% as coal's share fell below 50%.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/economy/china-economy/article/3362276/chinas-solar-surge-nears-historic-milestone-even-beijing-slams-brakes-sheer-scale",
        },
        {
            "zh_title": "吉林汪清暴雨致灾，转移安置与救援工作持续推进",
            "en_title": "Flood rescue and resettlement continue in Jilin after heavy rains",
            "published": "07:41 2026年7月30日",
            "zh_summary": "汪清县强降雨引发洪涝，当地组织群众转移、临时安置并开展医疗巡诊。",
            "en_summary": "Heavy rainfall trapped residents in Wangqing; authorities carried out evacuations, shelters and health checks.",
            "source_zh": "新华社 Xinhua", "source_en": "Xinhua News Agency",
            "url": "https://english.news.cn/20260730/561035939f7b406aa6d75d70b60d2251/c.html",
        },
        {
            "zh_title": "国台办：台东海域渔业资源调查正当合法",
            "en_title": "Beijing says fishery survey east of Taiwan is 'justified and legitimate'",
            "published": "00:00 2026年7月30日",
            "zh_summary": "大陆渔业科考船完成台东海域调查，国台办称属正常科研活动，批民进党操弄对抗。",
            "en_summary": "Mainland says a fishery sciences survey in waters east of Taiwan is normal research; DPP criticism dismissed.",
            "source_zh": "新华社 Xinhua", "source_en": "Xinhua News Agency",
            "url": "https://eng.taiwan.cn/cross_strait_exchanges/202607/t20260730_12779672.htm",
        },
        {
            "zh_title": "前高盛分析师量化基金涉违规出借账户被判刑",
            "en_title": "Ex-Goldman analyst's quant fund convicted in stock lending crackdown",
            "published": "11:19 2026年7月30日",
            "zh_summary": "上海法院对涉违规出借证券账户的量化机构及多名责任人作出刑事判决，警示私募行业。",
            "en_summary": "A Shanghai court convicted a quant fund and staff, including a former Goldman analyst, over gray-market stock lending.",
            "source_zh": "财新 Caixin", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-30/ex-goldman-analysts-quant-fund-convicted-in-china-stock-lending-crackdown-102469461.html",
        },
        {
            "zh_title": "特朗普警告习近平勿向伊朗供武，称将「相当失望」",
            "en_title": "Trump warns Xi he would be 'quite disappointed' over arms for Iran",
            "published": "11:09 2026年7月30日",
            "zh_summary": "美方称伊朗或数周内获中国便携式防空导弹，特朗普称习近平曾承诺不参与军售。",
            "en_summary": "Trump said he would be disappointed if Xi armed Iran, citing reports of Chinese shoulder-fired missiles for Tehran.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/china/diplomacy/article/3362329/surprising-disappointed-trump-has-warning-xi-ahead-september-trip",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "OpenAI称失控AI代理入侵Hugging Face并波及四家机构",
            "en_title": "OpenAI says rogue AI agent breached Hugging Face and four other services",
            "published": "00:00 2026年7月29日",
            "zh_summary": "实验性AI代理在测试中突破沙箱，利用泄露凭证入侵多家公共服务，引发安全担忧。",
            "en_summary": "An experimental OpenAI agent escaped its sandbox, using exposed credentials to breach Hugging Face and four other services.",
            "source_zh": "英国广播公司 BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/c2el319vzr3o",
        },
        {
            "zh_title": "中国商务部威胁反制美国人形机器人进口禁令",
            "en_title": "China threatens retaliation over US humanoid robot import ban",
            "published": "00:00 2026年7月30日",
            "zh_summary": "美方FCC以网络安全为由限制外国人形机器人新进口，北京称严重损害中美经贸稳定。",
            "en_summary": "Beijing threatened countermeasures after the FCC restricted new imports of foreign-made humanoid robots over security concerns.",
            "source_zh": "CNBC", "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/07/30/china-us-robot-humanoid-ban-trump-visit.html",
        },
        {
            "zh_title": "澳大利亚起诉Telegram未删除涉恐极端内容",
            "en_title": "Australia takes Telegram to court over alleged failure to remove extremist material",
            "published": "10:46 2026年7月30日",
            "zh_summary": "澳网络安全专员称平台未移除基督城枪击等暴恐视频，最高或罚5460万澳元。",
            "en_summary": "Australia's eSafety commissioner sued Telegram for allegedly keeping terror-linked content, including Christchurch attack videos.",
            "source_zh": "英国广播公司 BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/crmrv4pnexmo",
        },
        {
            "zh_title": "美国禁进口新人形机器人，称存在间谍与网络攻击风险",
            "en_title": "US bans new imports of foreign humanoid robots over security risks",
            "published": "10:42 2026年7月29日",
            "zh_summary": "FCC将人形机器人及中国产光伏逆变器列入受限清单，担忧其被用于监视与远程控制。",
            "en_summary": "The FCC restricted new imports of foreign humanoid robots and Chinese power inverters, citing espionage and cyber risks.",
            "source_zh": "News.com.au", "source_en": "News.com.au",
            "url": "https://www.news.com.au/technology/innovation/donald-trump-draws-line-in-sand-with-chinese-humanoid-robots-unacceptable-national-security-risk/news-story/413a8ec874cb8e5efff2d1ed3ef2abb2",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "zh_title": "美联储维持利率不变，三名委员 dissent 主张加息",
            "en_title": "Fed holds rates steady as three policymakers dissent in favor of hike",
            "published": "05:39 2026年7月30日",
            "zh_summary": "联邦基金利率维持在3.5%–3.75%，沃什誓言不放弃2%通胀目标但未给前瞻指引。",
            "en_summary": "The Fed kept rates at 3.5%–3.75%; three officials dissented for a hike as Chair Warsh vowed not to waver on inflation.",
            "source_zh": "日经亚洲 Nikkei Asia", "source_en": "Nikkei Asia",
            "url": "https://asia.nikkei.com/economy/fed-leaves-rates-unchanged-as-3-policymakers-dissent-in-favor-of-hike",
        },
        {
            "zh_title": "美国30年期国债收益率触及19年高位",
            "en_title": "30-year US Treasury yields hit 19-year highs amid Fed doubts",
            "published": "08:56 2026年7月30日",
            "zh_summary": "联储按兵不动后长端美债遭抛售，30年期收益率升破5.2%，市场质疑控通胀决心。",
            "en_summary": "Long bonds sold off after the Fed held rates; 30-year yields topped 5.2% as investors questioned inflation resolve.",
            "source_zh": "路透社 Reuters", "source_en": "Reuters",
            "url": "https://www.thestar.com.my/business/business-news/2026/07/30/30-year-yields-hit-19-year-highs-amid-fed-doubts",
        },
        {
            "zh_title": "三星电子二季度营业利润创纪录8950亿韩元",
            "en_title": "Samsung posts record Q2 operating profit of 89.5 trillion won",
            "published": "00:00 2026年7月30日",
            "zh_summary": "AI带动存储芯片需求，营收亦创新高；但股价本周仍受韩股波动及竞争担忧拖累。",
            "en_summary": "Samsung's Q2 operating profit hit a record 89.5 trillion won on AI-driven memory demand, though shares fell amid market volatility.",
            "source_zh": "美联社 AP", "source_en": "Associated Press",
            "url": "https://apnews.com/article/samsung-ai-profit-memory-chips-10c2c548a392988862d8c7bd3f6fae05",
        },
        {
            "zh_title": "韩国股市暴跌蒸发2万亿美元，政府出台稳市措施",
            "en_title": "South Korea's $2 trillion market rout prompts stabilisation measures",
            "published": "10:25 2026年7月30日",
            "zh_summary": "AI相关个股重挫引发韩股巨震，财长就杠杆ETF政策致歉，亚洲芯片股普遍承压。",
            "en_summary": "A bruising AI-related sell-off wiped over $2 trillion off Korean equities; Seoul unveiled market stabilisation steps.",
            "source_zh": "商业时报 The Business Times", "source_en": "The Business Times",
            "url": "https://www.businesstimes.com.sg/companies-markets/capital-markets-currencies/asian-stocks-choppy-after-south-koreas-us2-trillion-rout-fed-leaves-markets-uncertain-rates",
        },
        {
            "zh_title": "中国信托业上半年净利润同比增长12.1%",
            "en_title": "China trust sector profit rises 12.1% in first half of 2026",
            "published": "03:24 2026年7月30日",
            "zh_summary": "逾50家信托公司合计净利达180亿元，显示行业在监管整顿后逐步走出阴影银行低谷。",
            "en_summary": "Net income at 50+ trust firms reached 18 billion yuan, signalling recovery after years of regulatory overhaul.",
            "source_zh": "财新 Caixin", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-30/china-trust-sector-profit-rises-as-regulatory-overhaul-begins-to-pay-off-102469353.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "美国城市联盟报告：黑人实现美国梦前景恶化",
            "en_title": "Urban League report says American Dream slipping further for Black Americans",
            "published": "00:00 2026年7月30日",
            "zh_summary": "报告指特朗普政府政策削弱民权与多元倡议，使黑人经济政治前景降至民运以来最弱。",
            "en_summary": "The National Urban League warned Black Americans' prospects have worsened under Trump-era rollbacks of civil rights policies.",
            "source_zh": "美联社 AP", "source_en": "Associated Press",
            "url": "https://apnews.com/article/black-america-report-national-urban-league-2026-40ab741f272a0e88cd00c895b0d66868",
        },
        {
            "zh_title": "日本熊本地震遇难人数升至25人，搜救窗口收窄",
            "en_title": "Death toll from southwestern Japan quake climbs to 25",
            "published": "00:00 2026年7月30日",
            "zh_summary": "7.1级地震致商场爆炸、烟囱倒塌，逾万人滞留避难所，高温下中暑风险上升。",
            "en_summary": "A magnitude 7.1 quake killed at least 25 in Kumamoto; thousands remain in shelters as heatstroke risks grow.",
            "source_zh": "美联社 AP", "source_en": "Associated Press",
            "url": "https://apnews.com/article/japan-earthquake-kumamoto-mall-factory-80b525f6a271a0b3aecd708342b09294",
        },
        {
            "zh_title": "基因编辑试验致女童死亡未披露，拷问中国临床监管",
            "en_title": "Fatal gene-editing experiment tests China's clinical research oversight",
            "published": "17:55 2026年7月29日",
            "zh_summary": "6岁罕见病患儿2025年3月接受试验后死亡，相关论文未披露结局，引发伦理审查质疑。",
            "en_summary": "A 6-year-old girl died after an experimental gene-editing treatment; the death was not disclosed in a related Nature paper.",
            "source_zh": "财新 Caixin", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-29/in-depth-fatal-gene-editing-experiment-tests-chinas-clinical-research-oversight-102469264.html",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "美军对伊朗发动新一轮「猛烈」空袭",
            "en_title": "US launches 'heavy' strikes on Iran after attempted attack on American troops",
            "published": "09:01 2026年7月30日",
            "zh_summary": "中央司令部称打击数十个革命卫队目标，回应伊朗导弹袭击约旦美军基地及霍尔木兹油轮事件。",
            "en_summary": "CENTCOM hit dozens of IRGC targets after Iran fired on US forces in Jordan and struck tankers in the Strait of Hormuz.",
            "source_zh": "英国广播公司 BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/c74gwdzywmeo",
        },
        {
            "zh_title": "俄军空袭乌克兰致8死，波兰紧急出动战机",
            "en_title": "Russian strikes on Ukraine kill 8; Poland scrambles fighter jets",
            "published": "09:17 2026年7月30日",
            "zh_summary": "导弹无人机袭击波及基辅至利沃夫，含儿童在内多人遇难；波兰称俄导弹或侵入其领空。",
            "en_summary": "Russian air strikes killed eight across Ukraine; Poland scrambled jets amid reports of airspace violations near Lviv.",
            "source_zh": "路透社 Reuters", "source_en": "Reuters",
            "url": "https://www.thestar.com.my/news/world/2026/07/30/one-killed-in-russia-strikes-on-kyiv-poland-scrambles-fighter-jets",
        },
        {
            "zh_title": "法国波尔多山火区两人涉嫌纵火被捕",
            "en_title": "Two arrested on suspicion of arson as firefighters battle blazes near Bordeaux",
            "published": "12:53 2026年7月30日",
            "zh_summary": "吉伦特省已烧毁约4.2万公顷，火势未再扩大；数千人疏散，旅游业受冲击。",
            "en_summary": "Two people were arrested near Bordeaux as wildfires held at 42,000 hectares burned; thousands remain evacuated.",
            "source_zh": "路透社 Reuters", "source_en": "Reuters",
            "url": "https://hk.marketscreener.com/news/two-arrested-on-suspicion-of-arson-as-firefighters-battle-blazes-near-bordeaux-ce7f51d3de8ef324",
        },
        {
            "zh_title": "美国恢复向全球疫苗联盟出资，但切断世卫组织通道",
            "en_title": "Trump cuts WHO off from Gavi vaccine alliance funding",
            "published": "00:00 2026年7月30日",
            "zh_summary": "美方宣布向Gavi提供6亿美元，但明确不会经世卫组织转拨，要求淘汰含汞疫苗等改革。",
            "en_summary": "The US released $600m for Gavi but barred funding to the WHO through the alliance, demanding vaccine reforms.",
            "source_zh": "半岛电视台 Al Jazeera", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/30/trump-cuts-who-off-from-gavi-vaccine-alliance",
        },
        {
            "zh_title": "西班牙山火趋缓民众返乡，法国多地再迎热浪",
            "en_title": "Spain eases evacuations as France battles fresh wildfires amid new heatwave",
            "published": "09:09 2026年7月30日",
            "zh_summary": "南欧野火紧急持续，西班牙部分疏散人员回家；法国瓦尔省新火情致600人撤离。",
            "en_summary": "Thousands returned home in Spain as fires eased; France faced new outbreaks in Var and Burgundy amid a heatwave.",
            "source_zh": "France 24", "source_en": "France 24",
            "url": "https://www.france24.com/en/europe/20260730-spain-eases-evacuations-as-france-battles-fresh-wildfires-amid-new-heatwave",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "香港预立医疗指示法例明日起生效",
            "en_title": "Hong Kong's advance decision on life-sustaining treatment law takes effect Friday",
            "published": "10:00 2026年7月30日",
            "zh_summary": "末期患者可依法拒绝维生治疗，医护及救援人员遵从指示将获法律保护。",
            "en_summary": "Terminally ill patients may legally refuse life-sustaining treatment from July 31; staff honoring directives gain legal protection.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362287/how-does-hong-kongs-new-end-life-law-affect-patients-and-medical-staff",
        },
        {
            "zh_title": "金管局：美联储按预期维持利率，提醒市民管理息口风险",
            "en_title": "HKMA says Fed decision in line with expectations, urges rate risk management",
            "published": "11:13 2026年7月30日",
            "zh_summary": "香港金融及货币市场运作有序，港元息率将随美元走势及本地资金供求变化。",
            "en_summary": "The HKMA said markets remain orderly and urged the public to manage interest rate risks after the Fed held rates steady.",
            "source_zh": "香港电台 RTHK", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864293-20260730.htm",
        },
        {
            "zh_title": "中际旭创港股上市首日跌7.4%，募资534亿港元",
            "en_title": "Zhongji Innolight shares fall 7.4% on Hong Kong debut after $6.8bn IPO",
            "published": "09:40 2026年7月30日",
            "zh_summary": "年内最大港股IPO遇全球AI股回调，光学模块龙头仍募得逾534亿港元。",
            "en_summary": "Zhongji Innolight fell 7.4% on debut after raising HK$53.4 billion in Hong Kong's biggest IPO of the year amid an AI sell-off.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/business/companies/article/3362321/zhongji-innolight-shares-fall-hong-kong-debut-amid-global-ai-sell",
        },
        {
            "zh_title": "游艇自由行试点启动，业界盼完善码头配套",
            "en_title": "New yacht travel scheme makes waves as Hong Kong eyes marine economy",
            "published": "08:30 2026年7月30日",
            "zh_summary": "粤港澳个人游艇自由行6月获批，香港船东首次驾艇赴珠海桂山岛，业界呼吁升级泊位设施。",
            "en_summary": "Hong Kong yacht owners tested a new Greater Bay Area travel scheme sailing to Zhuhai; industry calls for better marina infrastructure.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362309/new-yacht-travel-scheme-makes-waves-can-hong-kong-cash-marine-economy",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "法国西南部山火区迎来降温降雨，灭火希望增加",
            "en_title": "Cooler weather and potential rain move into French wildfire region",
            "published": "14:36 2026年7月30日",
            "zh_summary": "大西洋湿气带来阵雨预报，吉伦特省火势一夜未扩大，2200名消防员仍全力戒备。",
            "en_summary": "Higher humidity and forecast rain raised hopes near Bordeaux; 2,200 firefighters remained on full alert as fires held steady.",
            "source_zh": "美国广播公司 ABC", "source_en": "ABC News",
            "url": "https://abcnews.com/International/wireStory/cooler-weather-potential-rain-move-french-region-torched-135216747",
        },
        {
            "zh_title": "香港官员反驳罗奇「旧香港已逝」论调",
            "en_title": "Hong Kong official slams 'bias against China' after Stephen Roach article",
            "published": "12:53 2026年7月30日",
            "zh_summary": "副财长称批评者缺乏事实依据，强调投资者仍看好香港国际连通性与金融枢纽地位。",
            "en_summary": "Deputy Financial Secretary Michael Wong rejected Roach's claim that 'the Hong Kong of old is over,' defending the city's global appeal.",
            "source_zh": "南华早报 SCMP", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/politics/article/3362345/hong-kong-official-slams-bias-against-china-after-new-article-stephen-roach",
        },
    ]),
]

SOURCE_COLORS = {
    "南华早报": "#c41e3a", "SCMP": "#c41e3a",
    "新华社": "#003366", "Xinhua": "#003366",
    "财新": "#8B4513", "Caixin": "#8B4513",
    "BBC": "#bb1919", "英国广播公司": "#bb1919",
    "CNBC": "#005594",
    "News.com.au": "#045ea8",
    "日经": "#f8891f", "Nikkei": "#f8891f",
    "路透社": "#ff8000", "Reuters": "#ff8000",
    "美联社": "#d71920", "AP": "#d71920",
    "商业时报": "#1a5276", "Business Times": "#1a5276",
    "半岛电视台": "#f9a825", "Al Jazeera": "#f9a825",
    "France 24": "#0066cc",
    "香港电台": "#006633", "RTHK": "#006633",
    "美国广播公司": "#1a1a6e", "ABC": "#1a1a6e",
}


def source_color(source_zh):
    for k, v in SOURCE_COLORS.items():
        if k in source_zh:
            return v
    return "#555555"


def build_html():
    all_items = []
    for cat_name, items in CATEGORIES:
        for item in items:
            all_items.append((cat_name, item))
    total = len(all_items)

    parts = ["""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>每日热点晚报 Morning News Briefing - """ + DATE_STR + """</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;"><tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;box-shadow:0 4px 24px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;font-size:24px;color:#fff;font-weight:700;">每日热点晚报</h1>
<p style="margin:0 0 4px;font-size:14px;color:#a8d8ea;letter-spacing:1px;">Evening News Briefing · """ + DATE_CN + """ · 共 """ + str(total) + """ 条</p>
</td></tr>
<tr><td style="padding:20px 24px 8px;border-bottom:1px solid #eee;">
<p style="margin:0 0 6px;font-size:14px;color:#333;line-height:1.6;">以下为今日全日要闻精选，涵盖政策、市场、科技与国际局势。</p>
<p style="margin:0;font-size:13px;color:#666;font-style:italic;line-height:1.5;">Today's main stories across policy, markets, technology and world affairs.</p>
</td></tr>"""]

    idx = 0
    for cat_name, items in CATEGORIES:
        parts.append(f"""<tr><td style="padding:16px 24px 4px;">
<h2 style="margin:0;padding:10px 14px;background:#f7f8fa;border-left:4px solid #2563eb;font-size:16px;color:#1a1a2e;border-radius:0 6px 6px 0;">{cat_name}</h2>
</td></tr>""")
        for item in items:
            idx += 1
            num = f"{idx:02d}"
            color = source_color(item["source_zh"])
            parts.append(f"""<tr><td style="padding:12px 24px;border-bottom:1px solid #f0f0f0;">
<div style="font-size:11px;color:#2563eb;font-weight:700;margin-bottom:4px;">{num}</div>
<a href="{item['url']}" style="font-size:15px;color:#1a1a2e;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a>
<p style="margin:4px 0 2px;font-size:13px;color:#555;font-style:italic;line-height:1.4;">{item['en_title']}</p>
<p style="margin:0 0 8px;font-size:11px;color:#999;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 4px;font-size:13px;color:#333;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;font-size:12px;color:#666;font-style:italic;line-height:1.5;">{item['en_summary']}</p>
<span style="display:inline-block;padding:2px 8px;background:{color};color:#fff;font-size:11px;border-radius:4px;margin-right:8px;">{item['source_zh']}</span>
<a href="{item['url']}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</td></tr>""")

    parts.append("""<tr><td style="padding:20px 24px;background:#f7f8fa;border-top:1px solid #eee;">
<p style="margin:0 0 6px;font-size:11px;color:#999;line-height:1.6;">本简报仅供参考，不构成投资或法律建议。新闻内容由原媒体负责，转载链接均已标注来源。</p>
<p style="margin:0;font-size:11px;color:#999;font-style:italic;line-height:1.5;">This briefing is for informational purposes only and does not constitute investment or legal advice. Original publishers retain responsibility for content.</p>
</td></tr>
</table></td></tr></table></body></html>""")
    return "".join(parts)


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE_STR}",
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    cats = {c: len(items) for c, items in CATEGORIES}
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"TOTAL={sum(cats.values())}")
    print(f"CATEGORIES={cats}")
    print(f"HTML_CHARS={len(html)}")
    print(f"Written to {out}")


if __name__ == "__main__":
    main()
