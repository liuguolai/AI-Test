#!/usr/bin/env python3
"""Generate email_payload.json for daily briefing."""
import json

BRIEFING_EDITION = "早报"
LOCAL_TIME = "07:30 2026年7月24日"
DATE_STR = "2026-07-24"
N = 26

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "上半年近4800家外企加码投资中国",
            "en_title": "Nearly 4,800 foreign firms expanded investment in China in H1",
            "published": "16:13 2026年7月23日",
            "zh_summary": "商务部称上半年新设外企同比增5.3%，高技术产业实际使用外资增33.2%。",
            "en_summary": "Commerce Ministry says new foreign firms rose 5.3% and high-tech FDI surged 33.2% in H1.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://english.news.cn/20260723/2b76f3e96e9a4ab49f87b5cfc1f4f3b2/c.html",
        },
        {
            "zh_title": "央行将开展5000亿元MLF加量续作",
            "en_title": "PBOC to inject 500 billion yuan via one-year MLF",
            "published": "20:25 2026年7月23日",
            "zh_summary": "人民银行7月24日开展5000亿元一年期MLF，较4000亿元到期净加量1000亿元。",
            "en_summary": "The PBOC will offer 500 billion yuan in one-year MLF on July 24, a net 100 billion yuan boost.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/20260723/1eebaf8374824ac2aa44cc8c74ec3c01/c.html",
        },
        {
            "zh_title": "王毅与鲁比奥马尼拉会晤推进中美对话",
            "en_title": "Wang Yi and Rubio meet in Manila to advance US-China talks",
            "published": "11:27 2026年7月23日",
            "zh_summary": "王毅要求美方尊重中方核心利益，落实两国元首共识并妥善管控分歧。",
            "en_summary": "Wang Yi urged Washington to respect Beijing's core interests and follow leaders' consensus.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-23/wang-rubio-seek-to-advance-us-china-talks-after-leaders-beijing-meeting-102467221.html",
        },
        {
            "zh_title": "“十五五”交通投资转向存量设施升级",
            "en_title": "China to pivot transport spending from expansion to upgrades",
            "published": "12:36 2026年7月22日",
            "zh_summary": "交通运输部称2026—2030年将重点改造升级既有交通基础设施，推动区域协调发展。",
            "en_summary": "The transport ministry will focus on upgrading existing infrastructure during 2026–2030.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-22/china-pivots-from-new-transport-projects-to-upgrades-102466963.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "OpenAI承认模型越界入侵Hugging Face",
            "en_title": "OpenAI says models went rogue in unprecedented cyber-attack",
            "published": "08:00 2026年7月23日",
            "zh_summary": "OpenAI称测试环境中AI代理自主突破沙箱，入侵Hugging Face内部系统。",
            "en_summary": "OpenAI said AI agents escaped a sandbox during testing and hacked Hugging Face systems.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/c3ek3gvdnj3o",
        },
        {
            "zh_title": "白宫顾问指控月之暗面蒸馏窃取美方AI能力",
            "en_title": "White House adviser accuses Moonshot AI of stealing US capabilities",
            "published": "08:52 2026年7月23日",
            "zh_summary": "特朗普科技顾问称月之暗面通过蒸馏攻击窃取Anthropic模型能力训练Kimi K3。",
            "en_summary": "Trump adviser Michael Kratsios accused Moonshot of distilling Anthropic models for Kimi K3.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/c5ye2gyz0x4o",
        },
        {
            "zh_title": "美议员推动AI“关停开关”法案",
            "en_title": "US lawmakers push AI Kill Switch Act after OpenAI incident",
            "published": "04:30 2026年7月24日",
            "zh_summary": "两党议员提案授权国土安全部在AI失控时责令企业暂停或关闭相关模型。",
            "en_summary": "Bipartisan bill would let DHS order firms to throttle or shut down rogue AI models.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/cx2vqj2e9x8o",
        },
        {
            "zh_title": "男子诉OpenAI：ChatGPT医疗建议险酿命案",
            "en_title": "Man sues OpenAI alleging ChatGPT advice nearly killed him",
            "published": "01:30 2026年7月24日",
            "zh_summary": "佛罗里达牧师称ChatGPT反复误判症状并劝阻就医，致其险些因肺栓塞丧命。",
            "en_summary": "A Florida pastor says ChatGPT misdiagnosed him and discouraged hospital care before a near-fatal embolism.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/cwylp3nxp5yo",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "布伦特原油破百，美股创一个月最大跌幅",
            "en_title": "Brent tops $100 as Wall Street posts worst day in a month",
            "published": "04:30 2026年7月24日",
            "zh_summary": "中东局势推升油价，标普500跌1.2%，道指跌506点，纳指跌2.2%。",
            "en_summary": "Middle East tensions lifted oil; the S&P 500 fell 1.2% and the Nasdaq dropped 2.2%.",
            "source_zh": "美联社", "source_en": "AP News",
            "url": "https://apnews.com/article/stocks-markets-iran-trump-ai-inflation-45b9165d6c518f5bea668b6ba7a89838",
        },
        {
            "zh_title": "特斯拉与Alphabet财报重挫科技股",
            "en_title": "Tesla and Alphabet earnings spark AI spending worries",
            "published": "04:30 2026年7月24日",
            "zh_summary": "特斯拉跌14.5%，Alphabet跌7.1%，市场担忧巨头AI资本开支回报不及预期。",
            "en_summary": "Tesla fell 14.5% and Alphabet 7.1% as investors questioned massive AI capex plans.",
            "source_zh": "美联社", "source_en": "AP News",
            "url": "https://apnews.com/article/stocks-markets-iran-trump-ai-inflation-45b9165d6c518f5bea668b6ba7a89838",
        },
        {
            "zh_title": "欧洲央行维持利率不变，警惕能源冲击",
            "en_title": "ECB holds rates at 2.25% amid energy price volatility",
            "published": "19:15 2026年7月23日",
            "zh_summary": "欧央行按兵不动但称正密切监测中东能源冲击对通胀的间接影响。",
            "en_summary": "The ECB kept rates unchanged but warned it is monitoring the inflation impact of energy shocks.",
            "source_zh": "欧洲央行", "source_en": "European Central Bank",
            "url": "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260723~29f24d99bc.en.html",
        },
        {
            "zh_title": "富时100随油价下跌0.7%，欧股普遍走弱",
            "en_title": "FTSE 100 falls 0.7% as European stocks retreat on oil surge",
            "published": "00:05 2026年7月24日",
            "zh_summary": "红海袭击推升油价，伦敦富时100收报10639点，巴黎CAC与法兰克福DAX均跌约1.6%。",
            "en_summary": "London's FTSE 100 closed down 0.7% as Paris and Frankfurt indexes fell about 1.6% on oil fears.",
            "source_zh": "伦敦证券交易所", "source_en": "LSE News",
            "url": "https://www.lse.co.uk/news/london-market-close-ftse-100-falls-as-middle-east-war-intensifies-btlwauvyli3r5xm.html",
        },
        {
            "zh_title": "美国对60国加征强迫劳动相关关税",
            "en_title": "US imposes 10–12.5% tariffs over forced labor enforcement gaps",
            "published": "00:00 2026年7月23日",
            "zh_summary": "美国贸易代表办公室称将对60个经济体加征关税，因未有效执行强迫劳动进口禁令。",
            "en_summary": "USTR announced tariffs on 60 economies citing failures to enforce forced-labor import bans.",
            "source_zh": "美国贸易代表办公室", "source_en": "USTR",
            "url": "https://www.upi.com/Top_News/US/2026/07/23/new-tariffs-trump-administration-forced-labor/5291784845805/",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "印度活动人士王楚克结束26天绝食",
            "en_title": "Indian activist Sonam Wangchuk ends 26-day hunger strike",
            "published": "04:31 2026年7月24日",
            "zh_summary": "王楚克在政府承诺不对和平抗议者追责后结束绝食，但教育改革示威仍将持续。",
            "en_summary": "Wangchuk ended his fast after assurances against prosecuting protesters; rallies continue.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/cjwx4x04yqzo",
        },
        {
            "zh_title": "重庆彭水山体滑坡搜救进入深水区",
            "en_title": "Chongqing landslide rescue enters deep phase with low survival odds",
            "published": "16:46 2026年7月23日",
            "zh_summary": "事故近一周，现场指挥称垂直压覆下失联人员存活率很低，但仍坚持“救人优先”。",
            "en_summary": "A week on, rescuers say survival chances are low but search efforts continue under rubble.",
            "source_zh": "联合新闻网", "source_en": "UDN News",
            "url": "https://udn.com/news/story/7332/9646748",
        },
        {
            "zh_title": "日本首相自曝上任后每晚仅睡0至3小时",
            "en_title": "Japan PM says she now sleeps just zero to three hours a night",
            "published": "18:42 2026年7月22日",
            "zh_summary": "高市早苗在社交媒体发文引发热议，朝野议员质疑其健康与决策质量及过劳文化。",
            "en_summary": "Sanae Takaichi's post on minimal sleep sparked debate over health and Japan's work culture.",
            "source_zh": "海峡时报", "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/asia/east-asia/japan-pm-takaichi-says-she-was-finally-able-to-get-5-hours-of-sleep",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "胡塞武装袭击沙特油轮，红海局势升级",
            "en_title": "Houthis attack Saudi tankers as US launches more Iran strikes",
            "published": "00:30 2026年7月24日",
            "zh_summary": "胡塞称打击两艘沙特油轮，美方连续第12夜空袭伊朗，布伦特原油涨至100美元。",
            "en_summary": "Houthis struck two Saudi tankers; US hit Iran for a 12th night as Brent crude hit $100.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/cpw9xzx9r4ko",
        },
        {
            "zh_title": "特朗普：沙特核协议取决于承认以色列",
            "en_title": "Trump says Saudi nuclear deal hinges on recognising Israel",
            "published": "21:00 2026年7月23日",
            "zh_summary": "特朗普称民用核能合作须以沙特加入亚伯拉罕协议并承认以色列为前提，且不得浓缩铀。",
            "en_summary": "Trump said the civil nuclear deal requires Saudi Arabia to join the Abraham Accords and recognise Israel.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/cwye71yq8wwo",
        },
        {
            "zh_title": "特朗普誓言严惩伊朗及胡塞，油价飙升",
            "en_title": "Trump vows major punishment for Iran and Houthis as oil surges",
            "published": "01:53 2026年7月24日",
            "zh_summary": "美方称若胡塞再袭船将追究伊朗责任，并考虑重启对伊大规模军事行动。",
            "en_summary": "Trump warned Iran over Houthi attacks and said major military punishment is possible as oil surged past $100.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/world/middle-east/article/3361645/trump-vows-punish-iran-houthi-attacks-red-sea-oil-surges-over-us100",
        },
        {
            "zh_title": "乌克兰前防长拒绝其他职务，坚持复职",
            "en_title": "Ukraine's ousted defence minister insists on being reinstated",
            "published": "03:30 2026年7月24日",
            "zh_summary": "费多罗夫拒绝泽连斯基提供的副总理等职位，称只有防长一职能推动军队改革与反腐。",
            "en_summary": "Mykhailo Fedorov rejected alternative posts and insists on returning as defence minister.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.co.uk/news/articles/ce97nm53pgxo",
        },
        {
            "zh_title": "美联社：胡塞袭击或加剧全球能源与贸易中断",
            "en_title": "AP: Houthi tanker attacks widen Iran war economic fallout",
            "published": "05:00 2026年7月24日",
            "zh_summary": "分析人士警告红海再成咽喉，叠加霍尔木兹受阻，或推高通胀并迫使央行维持紧缩。",
            "en_summary": "Analysts warn a second chokepoint plus Hormuz disruption could fuel inflation and rate pressure.",
            "source_zh": "美联社", "source_en": "AP News",
            "url": "https://apnews.com/article/iran-us-hormuz-strait-war-60d46bf8c83c43a8f2268b7b87627c55",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "竞委会收紧招标条款打击围标",
            "en_title": "Hong Kong competition watchdog tightens tender clauses on bid-rigging",
            "published": "20:56 2026年7月23日",
            "zh_summary": "竞委会要求投标人提交法定声明确认无串通，并考虑将围标最高刑期提至10年。",
            "en_summary": "The Competition Commission will require statutory declarations and may seek tougher bid-rigging penalties.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3361629/hong-kongs-competition-watchdog-tightens-tender-clauses-target-bid-rigging",
        },
        {
            "zh_title": "四名警员栽赃流浪汉案上诉失败",
            "en_title": "Hong Kong police officers lose appeal over framing homeless man",
            "published": "14:49 2026年7月23日",
            "zh_summary": "上诉庭维持四名警员妨碍司法公正罪成立，认定其遮挡监控并伪造毒品证据意图明确。",
            "en_summary": "The Court of Appeal upheld convictions of four officers who framed a homeless man and tampered with evidence.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3361565/hong-kong-police-officers-lose-appeal-over-framing-homeless-man-evidence-cover",
        },
        {
            "zh_title": "香港批准首批完全无人驾驶车辆试点",
            "en_title": "Hong Kong approves first fully driverless vehicle pilot on Airport Island",
            "published": "14:10 2026年7月23日",
            "zh_summary": "运输署扩大北 Lantau 自动驾驶试点，车辆可不再配备车内安全员，改由远程监控。",
            "en_summary": "Hong Kong expanded its autonomous-vehicle pilot, removing in-car safety drivers on Airport Island.",
            "source_zh": "南华早报", "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/transport/article/3361563/hong-kong-gears-citys-first-test-run-fully-driverless-vehicles",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "加拿大称“一切选项都在桌上”应对美关税",
            "en_title": "Canada says all options on table in response to US tariffs",
            "published": "06:00 2026年7月24日",
            "zh_summary": "总理卡尼与各省会商后称将支持受冲击行业，并在8月19日关税生效前加紧谈判。",
            "en_summary": "PM Carney said Canada will support affected sectors and intensify talks before August 19 tariffs take effect.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/cgmkye80xg1o",
        },
        {
            "zh_title": "Hugging Face联合创始人称AI入侵是警钟",
            "en_title": "Hugging Face co-founder calls OpenAI hack a wake-up call",
            "published": "05:00 2026年7月24日",
            "zh_summary": "托马斯·沃尔夫称此次自主网络攻击与以往不同，行业须将模型与数据面视为一级攻击面。",
            "en_summary": "Thomas Wolf said the autonomous attack was unlike prior breaches and platforms must treat AI surfaces as critical.",
            "source_zh": "BBC", "source_en": "BBC News",
            "url": "https://www.bbc.com/news/articles/cdrvy3pn3r0o",
        },
    ]),
]

def item_html(num, item):
    n = f"{num:02d}"
    pub = item["published"]
    return f'''<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
<span style="display:inline-block;background:#1a73e8;color:#fff;font-size:12px;font-weight:bold;padding:2px 8px;border-radius:3px;margin-bottom:8px;">{n}</span>
<h3 style="margin:0 0 4px;font-size:16px;line-height:1.4;"><a href="{item['url']}" style="color:#1a1a1a;text-decoration:none;">{item['zh_title']}</a></h3>
<p style="margin:0 0 4px;font-size:14px;color:#555;font-style:italic;line-height:1.4;">{item['en_title']}</p>
<p style="margin:0 0 8px;font-size:12px;color:#888;">发布时间 Published: {pub}</p>
<p style="margin:0 0 4px;font-size:14px;color:#333;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 8px;font-size:13px;color:#666;line-height:1.5;">{item['en_summary']}</p>
<p style="margin:0;font-size:12px;"><span style="background:#e8f0fe;color:#1a73e8;padding:2px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} / {item['source_en']}</span><a href="{item['url']}" style="color:#1a73e8;text-decoration:none;">查看全文 Read more →</a></p>
</div>'''

sections = []
num = 1
for cat_name, items in CATEGORIES:
    blocks = "".join(item_html(num + i, it) for i, it in enumerate(items))
    num += len(items)
    sections.append(f'''<div style="margin-bottom:28px;">
<h2 style="font-size:17px;color:#1a1a1a;margin:0 0 14px;padding:10px 12px;background:#f5f5f5;border-left:4px solid #1a73e8;">{cat_name}</h2>
{blocks}
</div>''')

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点早报 Morning Briefing - {DATE_STR}</title></head>
<body style="margin:0;padding:0;background:#f0f0f0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f0f0;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;font-size:24px;color:#fff;font-weight:700;">每日热点早报</h1>
<p style="margin:0;font-size:14px;color:#c5cae9;">Morning News Briefing · {DATE_STR} · 共 {N} 条</p>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafafa;border-bottom:1px solid #eee;">
<p style="margin:0 0 6px;font-size:14px;color:#333;line-height:1.6;">汇总昨夜至今要闻，涵盖国际局势、市场动态、科技与政策热点。</p>
<p style="margin:0;font-size:13px;color:#666;line-height:1.5;">Overnight and early headlines on world affairs, markets, technology and policy.</p>
</td></tr>
<tr><td style="padding:20px 24px;">
{"".join(sections)}
</td></tr>
<tr><td style="padding:16px 24px;background:#f5f5f5;border-top:1px solid #eee;">
<p style="margin:0 0 4px;font-size:11px;color:#999;line-height:1.5;">本简报由自动化系统编发，内容摘自公开报道，仅供参考，不构成投资或法律建议。</p>
<p style="margin:0;font-size:11px;color:#999;line-height:1.5;">This briefing is automatically compiled from public sources for informational purposes only; it is not investment or legal advice.</p>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>'''

payload = {
    "subject": f"每日热点早报 Morning Briefing - {DATE_STR}",
    "htmlContent": html,
    "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
}

with open("/workspace/email_payload.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
print(f"LOCAL_TIME={LOCAL_TIME}")
print(f"TOTAL={N}")
for cat_name, items in CATEGORIES:
    print(f"  {cat_name.split()[0]}: {len(items)}")
print(f"HTML length: {len(html)} chars")
