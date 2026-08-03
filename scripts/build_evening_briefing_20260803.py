#!/usr/bin/env python3
"""Generate evening briefing email_payload.json for 2026-08-03."""
import json
import os

BRIEFING_EDITION = "晚报"
DATE = "2026-08-03"
DATE_CN = "2026年8月3日"
TOTAL = 26

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "全国仍有大范围降雨，东北至江南高温闷热持续",
            "en_title": "Widespread rain persists as heat and humidity grip northeast to Jiangnan",
            "published": "08:17 2026年8月3日",
            "zh_summary": "中央气象台称，华南至华北东北强降雨持续，副热带高压下江南等地闷热如桑拿。",
            "en_summary": "Heavy rain continues across south and north China while subtropical high drives oppressive heat from the northeast to Jiangnan.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/politics/20260803/76170da5c1e04aa08f866783d617fe4b/c.html",
        },
        {
            "zh_title": "上半年我国海洋生产总值达5.5万亿元，同比增长5.1%",
            "en_title": "China's ocean economy reaches 5.5 trillion yuan in H1, up 5.1%",
            "published": "09:19 2026年8月3日",
            "zh_summary": "自然资源部称，上半年海洋生产总值增速高于GDP，新增用海用岛投资额超3800亿元。",
            "en_summary": "The Ministry of Natural Resources said ocean GDP growth outpaced overall GDP, with over 380 billion yuan in new sea-use investment.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/20260803/1534a2e8dc9441e58fde790e4bbe8bba/c.html",
        },
        {
            "zh_title": "上半年我国海船新承接订单量同比大增105.2%",
            "en_title": "China's new ship orders surge 105.2% year on year in H1",
            "published": "09:14 2026年8月3日",
            "zh_summary": "自然资源部数据显示，新接订单全球份额达73.9%，多型高端船舶相继交付。",
            "en_summary": "Official data showed China captured 73.9% of global new orders as advanced vessels including LNG carriers were delivered.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/20260803/2d41fcbd655a4960acac36dabf252536/c.html",
        },
        {
            "zh_title": "更大力度扩内需，下半年宏观政策重点划定",
            "en_title": "China outlines stronger domestic demand push for second half",
            "published": "09:40 2026年8月3日",
            "zh_summary": "发改委称将加快8000亿元政策性金融工具投放和专项债使用，挖掘服务与智能产品消费潜力。",
            "en_summary": "The NDRC pledged faster deployment of 800 billion yuan in policy financial tools and special bonds to boost services and smart-product consumption.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/fortune/20260803/4c2219fcf32b4ade86206470ef3a3197/c.html",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "气象智能预警方案“妈祖”助力全球早期预警能力建设",
            "en_title": "China's MAZU AI weather warning scheme expands global early-warning reach",
            "published": "08:06 2026年8月3日",
            "zh_summary": "中国气象局称“妈祖”已在多国落地，并发布风云卫星人工智能工具箱提升海外适配能力。",
            "en_summary": "China's weather agency said MAZU is rolling out abroad and released new AI satellite tools to strengthen overseas early-warning capacity.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/politics/20260803/dcce4d886c494c02998f41806cf84a63/c.html",
        },
        {
            "zh_title": "新《蜘蛛侠》全球开画票房9.27亿美元，创影史第二高周末纪录",
            "en_title": "New Spider-Man film opens to $927m globally, second-biggest weekend ever",
            "published": "12:30 2026年8月3日",
            "zh_summary": "索尼称《蜘蛛侠：崭新之日》北美开画3.55亿美元，中国内地贡献1.21亿美元票房。",
            "en_summary": "Sony said Brand New Day took $355m in North America and $121m in China, ranking behind only Avengers: Endgame's global debut.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c3w052le2elo",
        },
        {
            "zh_title": "韩国芯片巨头三星、SK海力士股价周一重挫近9%",
            "en_title": "Samsung and SK Hynix shares slide nearly 9% after record Kospi rally",
            "published": "00:00 2026年8月3日",
            "zh_summary": "美联社称，在上周五创历史最大单日涨幅后，韩国两大存储芯片巨头股价周一大幅回调。",
            "en_summary": "AP reported sharp pullbacks in the two memory giants after Friday's record 17.9% surge in Seoul's chip-heavy benchmark.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-dollar-yen-trump-oil-d19a8f9a77b6fceca41da3e4b6bf17aa",
        },
        {
            "zh_title": "美元周一大幅走弱，美日联合干预后日元升至三个月高位",
            "en_title": "US dollar weakens sharply as yen hits three-month high after joint intervention",
            "published": "00:00 2026年8月3日",
            "zh_summary": "美联社称，官方确认干预后美元兑日元一度跌至155.20，为近三个月最强水平。",
            "en_summary": "AP said the dollar fell to nearly 155.20 yen after officials confirmed joint intervention, the yen's strongest level in about three months.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/yen-dollar-currency-trump-economy-7316599afed35629a27ae23a35f569fd",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "日本与美国确认罕见联合干预，支撑日元汇率",
            "en_title": "Japan and US confirm rare joint intervention to prop up yen",
            "published": "00:00 2026年8月3日",
            "zh_summary": "日本财务省称周五与美方协调买入日元，东京表示必要时将进一步联合入市。",
            "en_summary": "Tokyo confirmed coordinated yen buying with Washington on Friday and warned it is ready for further joint market action if needed.",
            "source_zh": "半岛电视台",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/economy/2026/8/3/japan-and-us-confirm-rare-joint-intervention-to-prop-up-yen",
        },
        {
            "zh_title": "全球股市分化，油价大跌，日元走强",
            "en_title": "World stocks mixed as oil slumps and yen strengthens",
            "published": "00:00 2026年8月3日",
            "zh_summary": "美联社称，特朗普称将暂缓打击伊朗后油价跌逾4%，亚洲股市多数走低，欧美期指上扬。",
            "en_summary": "AP said oil fell over 4% after Trump signalled restraint on Iran strikes, with mixed Asian equities and firmer US and European futures.",
            "source_zh": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-dollar-yen-trump-oil-d19a8f9a77b6fceca41da3e4b6bf17aa",
        },
        {
            "zh_title": "中国在美欧贸易谈判前为经济模式划“红线”",
            "en_title": "China draws 'red lines' around economic model ahead of EU, US trade talks",
            "published": "00:00 2026年8月3日",
            "zh_summary": "路透分析称，北京强调先进产业优先于消费刺激，显示在贸易争端中信心上升。",
            "en_summary": "Reuters analysis said Beijing is defending its industry-first policy mix, signalling growing confidence before looming trade talks.",
            "source_zh": "路透社",
            "source_en": "Reuters",
            "url": "https://finance.yahoo.com/news/analysis-china-draws-red-lines-170613120.html",
        },
        {
            "zh_title": "离岸中国国债期货在港首日挂牌，盘中涨逾1%",
            "en_title": "Offshore China treasury bond futures rise over 1% on Hong Kong debut",
            "published": "09:54 2026年8月3日",
            "zh_summary": "证监会主席吴清称此举是提升香港桥头堡角色的里程碑，并透露将研究REIT互联互通。",
            "en_summary": "CSRC chief Wu Qing called the launch a milestone for Hong Kong's bridge role and flagged talks on a REIT Stock Connect.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/business/article/3362734/treasury-bond-futures-milestone-boost-hong-kongs-bridgehead-role-csrc-chairman",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "韩国遭遇创纪录酷暑，多地气温突破40摄氏度",
            "en_title": "South Korea gripped by record heatwave as temperatures top 40C",
            "published": "00:00 2026年8月3日",
            "zh_summary": "韩联社称，大邱首次突破40摄氏度，极端高温已造成多起中暑伤亡事件。",
            "en_summary": "Yonhap said Daegu topped 40C for the first time since 1942 as extreme heat triggered multiple heatstroke casualties.",
            "source_zh": "韩联社",
            "source_en": "Yonhap",
            "url": "https://m-en.yna.co.kr/view/AEN20260803008100315",
        },
        {
            "zh_title": "熊本地震灾民遭遇史上最热天气，疏散安置压力加剧",
            "en_title": "Kumamoto quake evacuees face record heat as death toll reaches 38",
            "published": "00:00 2026年8月3日",
            "zh_summary": "日本时报称，熊本县气温首次超40摄氏度，逾8500人仍在避难，政府推进二次疏散安置。",
            "en_summary": "The Japan Times said Kumamoto hit 40.3C as more than 8,500 evacuees remained in shelters after the quake death toll rose to 38.",
            "source_zh": "日本时报",
            "source_en": "The Japan Times",
            "url": "https://www.japantimes.co.jp/news/2026/08/03/japan/kumamoto-quake-evacuees-heat/",
        },
        {
            "zh_title": "美国华盛顿州斯波坎野火摧毁600栋建筑，6万人疏散",
            "en_title": "Spokane-area wildfires destroy 600 structures, force 60,000 evacuations",
            "published": "00:00 2026年8月3日",
            "zh_summary": "半岛电视台称，周末大火烧毁约21平方公里，全州约1000平方公里过火，多数火势仍未受控。",
            "en_summary": "Al Jazeera said weekend blazes burned about 21 sq km near Spokane as roughly 1,000 sq km burned statewide with many fires uncontained.",
            "source_zh": "半岛电视台",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/3/fires-in-spokane-washington-burn-600-structures-force-60000-evacuations",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特朗普称美伊谈判周一下午开始，未设达成协议期限",
            "en_title": "Trump says Iran talks begin Monday afternoon, sets no deadline",
            "published": "07:27 2026年8月3日",
            "zh_summary": "路透称，特朗普取消原定打击后称谈判将启动，但尚未说明地点与参与方。",
            "en_summary": "Reuters said Trump called off imminent strikes and said talks would start Monday afternoon without naming venue or participants.",
            "source_zh": "路透社",
            "source_en": "Reuters",
            "url": "https://www.straitstimes.com/world/middle-east/trump-says-iran-talks-to-take-place-on-monday-sets-no-deadline-for-deal",
        },
        {
            "zh_title": "伊朗称正与阿曼商讨霍尔木兹海峡新航线",
            "en_title": "Iran says it is discussing new Hormuz shipping route with Oman",
            "published": "08:57 2026年8月3日",
            "zh_summary": "伊朗外交部称新航线谈判与海峡是否开放无关，并警告若美国冒险行动将作出回应。",
            "en_summary": "Tehran said route talks with Oman are separate from whether the strait opens, warning it would respond to any US escalation.",
            "source_zh": "新华社",
            "source_en": "Xinhua",
            "url": "http://www.news.cn/world/20260803/05d3d512ebb649929ca0ae518acd919c/c.html",
        },
        {
            "zh_title": "缅甸军方公布昂山素季会见红十字代表团照片",
            "en_title": "Myanmar military releases photo of Aung San Suu Kyi meeting Red Cross",
            "published": "15:30 2026年8月3日",
            "zh_summary": "BBC称，这是两年多来她首次获证实的对外接触，照片中昂山素季状态看似良好。",
            "en_summary": "The BBC said it was her first confirmed outside contact in over two years, with photos showing her appearing healthy.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c1e1d5j6660o",
        },
        {
            "zh_title": "乌克兰无人机袭击俄电商Wildberries弗拉基米尔仓库",
            "en_title": "Ukrainian drone strike hits Wildberries warehouse in Russia's Vladimir region",
            "published": "00:00 2026年8月3日",
            "zh_summary": "塔斯社称，仓库起火后人员已疏散，Wildberries称物流已改道，初步无伤亡报告。",
            "en_summary": "TASS said staff were evacuated after a fire at the e-commerce hub, with logistics rerouted and no casualties initially reported.",
            "source_zh": "塔斯社",
            "source_en": "TASS",
            "url": "https://tass.com/emergencies/2168245",
        },
        {
            "zh_title": "以色列官员称美方取消对伊打击前被蒙在鼓里数小时",
            "en_title": "Israeli officials say they were blindsided for hours on cancelled Iran strike",
            "published": "07:47 2026年8月3日",
            "zh_summary": "新华社引以媒称，内塔尼亚胡等人通过特朗普社媒帖文才得知美方叫停行动，以军仍高度戒备。",
            "en_summary": "Xinhua cited Israeli media saying leaders learned of the cancelled US strike via Trump's social posts while forces remain on alert.",
            "source_zh": "中国新闻网",
            "source_en": "China News Service",
            "url": "http://www.chinanews.com.cn/gj/2026/08-03/10670989.shtml",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "大埔火灾涉事两间消防工程公司仍可承接新合约",
            "en_title": "Two Tai Po fire contractors linked to blaze still taking new contracts",
            "published": "08:00 2026年8月3日",
            "zh_summary": "南华早报调查发现，涉事公司仍正常营运，议员担忧公共安全与工程烂尾风险。",
            "en_summary": "An SCMP investigation found the firms remain operational eight months after the Wang Fuk Court fire that killed 168 people.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362710/2-fire-service-contractors-linked-tai-po-tragedy-still-running-open-new-contracts",
        },
        {
            "zh_title": "前惩教助理员性侵囚犯判囚三年",
            "en_title": "Former Hong Kong prison officer jailed three years for inmate assault",
            "published": "14:51 2026年8月3日",
            "zh_summary": "裁判官指，被告2023年在大埔监狱用棍棒袭击囚犯并教唆他人掩盖，罪行非常严重。",
            "en_summary": "A judge jailed the ex-officer for a 2023 assault at Pik Uk Prison and for instructing others to cover up the attack.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362769/former-hong-kong-prison-officer-jailed-3-years-over-brutal-attack-inmate",
        },
        {
            "zh_title": "中大试验阿尔茨海默病脑部引流手术，患者家属称效果显著",
            "en_title": "CUHK trials Alzheimer's brain drainage surgery with reported gains",
            "published": "11:00 2026年8月3日",
            "zh_summary": "研究团队在香港开展临床试验，评估引流异常蛋白堆积能否改善患者基本生活能力。",
            "en_summary": "Researchers are running a Hong Kong trial to test whether draining abnormal protein buildup can improve patients' daily functioning.",
            "source_zh": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362720/completely-new-person-can-surgery-help-alzheimers-patients-regain-basic-skills",
        },
        {
            "zh_title": "三项全能选手溺亡后，议员促改革公开水域赛事安全机制",
            "en_title": "Lawmakers urge safety reforms after Hong Kong triathlete death",
            "published": "11:27 2026年8月3日",
            "zh_summary": "香港电台引议员称，应研究实时GPS追踪与超时预警，并参考外地极端天气应变标准。",
            "en_summary": "RTHK quoted lawmakers calling for real-time GPS tracking, timeout alerts and stricter weather protocols after Sunday's open-water death.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864773-20260803.htm",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "欧足联威胁就世界杯商业化方案对国际足联采取法律行动",
            "en_title": "UEFA threatens legal action over FIFA's scrapped World Cup investment plan",
            "published": "16:30 2026年8月3日",
            "zh_summary": "BBC称，欧足联要求因凡蒂诺保留相关文件，英格兰足协亦拟撤回对其连任的支持。",
            "en_summary": "The BBC said UEFA demanded document preservation as England's FA prepared to withdraw support for Gianni Infantino's re-election bid.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.com/sport/football/articles/cp30vg829nxo",
        },
        {
            "zh_title": "Massive Attack回应新加坡禁令：对巴旗展示后的待遇感到失望",
            "en_title": "Massive Attack respond after Singapore ban over Palestine display",
            "published": "09:30 2026年8月3日",
            "zh_summary": "乐队称7月29日演出后成员遭警方问话与搜查，新加坡以展示外国旗帜为由禁止其再入境。",
            "en_summary": "The band said members were questioned and searched after a 29 July show where they displayed a Palestinian flag, leading to a re-entry ban.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cr59qe86yj4o",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c41e3a", "Xinhua": "#c41e3a",
    "南华早报": "#ff6600", "SCMP": "#ff6600",
    "英国广播公司": "#bb1919", "BBC": "#bb1919",
    "美联社": "#cc0000", "AP": "#cc0000",
    "路透社": "#ff8000", "Reuters": "#ff8000",
    "半岛电视台": "#fa9000", "Al Jazeera": "#fa9000",
    "韩联社": "#003366", "Yonhap": "#003366",
    "日本时报": "#1a5276", "The Japan Times": "#1a5276",
    "塔斯社": "#8b0000", "TASS": "#8b0000",
    "香港电台": "#7c3aed", "RTHK": "#7c3aed",
    "中国新闻网": "#c41e3a", "China News Service": "#c41e3a",
}


def source_color(name):
    return SOURCE_COLORS.get(name, "#2563eb")


def build_html():
    items_html = []
    n = 0
    cats_html = []
    for cat_name, items in CATEGORIES:
        cat_blocks = []
        for item in items:
            n += 1
            num = f"{n:02d}"
            sc = source_color(item["source_zh"])
            cat_blocks.append(f"""
<div style="margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #eee;">
  <div style="font-size:11px;color:#2563eb;font-weight:bold;margin-bottom:4px;">{num}</div>
  <a href="{item['url']}" style="color:#1a1a1a;text-decoration:none;font-size:16px;font-weight:bold;line-height:1.4;">{item['zh_title']}</a>
  <div style="font-style:italic;color:#444;font-size:14px;margin-top:6px;line-height:1.4;">{item['en_title']}</div>
  <div style="color:#888;font-size:12px;margin-top:4px;">发布时间 Published: {item['published']}</div>
  <div style="margin-top:10px;font-size:14px;color:#333;line-height:1.6;">{item['zh_summary']}</div>
  <div style="margin-top:6px;font-size:13px;color:#555;line-height:1.5;">{item['en_summary']}</div>
  <div style="margin-top:10px;">
    <span style="background:{sc};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:6px;">{item['source_zh']}</span>
    <span style="background:{sc};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;">{item['source_en']}</span>
    <a href="{item['url']}" style="color:#2563eb;font-size:12px;margin-left:8px;text-decoration:none;">查看全文 Read more →</a>
  </div>
</div>""")
        cats_html.append(f"""
<div style="margin-bottom:28px;">
  <h2 style="background:#f0f4f8;border-left:4px solid #2563eb;padding:10px 14px;margin:0 0 16px 0;font-size:16px;color:#1a1a1a;">{cat_name}</h2>
  {''.join(cat_blocks)}
</div>""")

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 Evening Briefing - {DATE}</title></head>
<body style="margin:0;padding:0;background:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5;padding:20px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);padding:28px 24px;text-align:center;">
  <div style="color:#fff;font-size:24px;font-weight:bold;letter-spacing:1px;">每日热点晚报</div>
  <div style="color:#bfdbfe;font-size:14px;margin-top:8px;">Evening News Briefing · {DATE_CN} · 共 {TOTAL} 条</div>
</td></tr>
<tr><td style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e5e7eb;">
  <div style="font-size:14px;color:#374151;line-height:1.6;">汇总今日全日要闻，涵盖国内政策、市场动态、科技社会与国际热点。</div>
  <div style="font-size:13px;color:#6b7280;margin-top:6px;line-height:1.5;">Today's main stories across China, markets, technology, society and world affairs.</div>
</td></tr>
<tr><td style="padding:20px 24px;">
{''.join(cats_html)}
</td></tr>
<tr><td style="padding:20px 24px;background:#f8fafc;border-top:1px solid #e5e7eb;font-size:11px;color:#9ca3af;line-height:1.6;">
  <div>本简报由自动化系统编发，内容摘自公开报道，仅供参考，不构成投资或决策建议。</div>
  <div style="margin-top:6px;">This briefing is automatically compiled from public sources for informational purposes only and does not constitute advice.</div>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>"""


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    path = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Generated {path} ({len(html)} chars, {TOTAL} items)")


if __name__ == "__main__":
    main()
