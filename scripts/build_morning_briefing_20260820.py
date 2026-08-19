#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 2026-08-20 morning briefing HTML and email_payload.json."""
import json
import os

N = 23
DATE_CN = "2026年8月20日"
DATE_ISO = "2026-08-20"
SUBJECT = f"每日热点早报 Morning Briefing - {DATE_ISO}"

# Colors for source tags
TAGS = {
    "chinadaily": ("#c41e3a", "中国日报 China Daily"),
    "xinhua": ("#c41e3a", "新华社 Xinhua"),
    "cnbc": ("#005594", "CNBC"),
    "bbc": ("#bb1919", "BBC"),
    "rthk": ("#e60012", "香港电台 RTHK"),
    "reuters": ("#ff8000", "路透社 Reuters"),
    "aa": ("#c8102e", "阿纳多卢通讯社 Anadolu"),
    "hkex": ("#0072ce", "香港交易所 HKEX"),
    "chinaorg": ("#c41e3a", "中国网 China.org.cn"),
    "gia": ("#c8102e", "香港特区政府 HKSAR Government"),
}


def item(num, href, cn_title, en_title, pub, cn_sum, en_sum, tag):
    color, label = TAGS[tag]
    n = f"{num:02d}"
    return f"""<div style="padding:14px 0;border-bottom:1px solid #eee;">
<p style="margin:0 0 6px;font-size:12px;color:#64748b;font-weight:700;">{n}</p>
<p style="margin:0 0 4px;font-size:16px;line-height:1.45;font-weight:700;"><a href="{href}" style="color:#0f172a;text-decoration:none;">{cn_title}</a></p>
<p style="margin:0 0 4px;font-size:13px;line-height:1.4;color:#475569;font-style:italic;">{en_title}</p>
<p style="margin:0 0 8px;font-size:12px;color:#94a3b8;">发布时间 Published: {pub}</p>
<p style="margin:0 0 4px;font-size:14px;line-height:1.55;color:#334155;">{cn_sum}</p>
<p style="margin:0 0 8px;font-size:13px;line-height:1.5;color:#64748b;">{en_sum}</p>
<p style="margin:0;"><span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:12px;">{label}</span> <a href="{href}" style="color:#2563eb;font-size:13px;text-decoration:none;">查看全文 Read more →</a></p>
</div>"""


def h2(cn, en):
    return f"""<h2 style="margin:22px 0 8px;padding:8px 12px;background:#f1f5f9;border-left:4px solid #2563eb;font-size:16px;color:#0f172a;">{cn} / {en}</h2>"""


items_china = [
    item(1, "https://www.chinadaily.com.cn/a/202608/20/WS6a862d94a3106bc57421c699.html",
         "司法部认定欧盟对京东跨境调查属不当域外管辖",
         "China says EU’s JD.com subsidy probe is improper extraterritorial jurisdiction",
         "06:26 2026年8月20日",
         "司法部认定欧盟对京东外国补贴调查属不当域外管辖，禁止配合取证，并警告将依法反制。",
         "Beijing barred compliance with the EU JD.com subsidy inquiry, calling onshore information demands unlawful, and warned of countermeasures.",
         "chinadaily"),
    item(2, "https://www.news.cn/politics/leaders/20260819/f4af02ae62b54ca58dc11210a5f720f0/c.html",
         "王毅在首尔同韩国外长赵显会谈",
         "Wang Yi meets South Korean foreign minister in Seoul",
         "23:11 2026年8月19日",
         "王毅与赵显讨论经贸、自贸谈判及半岛局势。韩方重申一个中国政策，期待借APEC加深合作。",
         "Wang Yi and Cho Hyun discussed trade, a second-phase FTA and the peninsula. Seoul restated its one-China policy and eyed APEC.",
         "xinhua"),
    item(3, "https://www.news.cn/local/20260819/1f12c3ef32bb468987e9f4041ee7d524/c.html",
         "石家庄居民楼部分坍塌三人死亡 初步疑燃气泄漏燃爆",
         "Three dead after partial building collapse in Shijiazhuang",
         "21:33 2026年8月19日",
         "石家庄一小区凌晨部分坍塌，3人死亡、1人伤势平稳。初步怀疑燃气泄漏燃爆，住户已安置。",
         "A four-storey block partially collapsed before dawn. Three died; one is stable. A gas-leak blast is the early suspected cause.",
         "xinhua"),
    item(4, "http://www.xinhuanet.com/20260819/c8d7a02538f14079b5ffb3db38183788/c.html",
         "青海海西发生5.6级地震 暂无人员伤亡报告",
         "Magnitude 5.6 quake hits Haixi, Qinghai; no casualties reported",
         "07:43 2026年8月19日",
         "海西州直辖区19日5时36分发生5.6级地震，震源深10公里。消防已排查，暂无伤亡报告。",
         "A 5.6 quake struck Haixi at 05:36 at a depth of 10 km. Da Qaidam felt it strongly. No casualties have been reported.",
         "xinhua"),
]

items_tech = [
    item(5, "https://www.cnbc.com/2026/08/19/marvell-google-ai-chips.html",
         "谷歌获权购买至多122亿美元迈威尔股份以深化定制芯片合作",
         "Google may buy up to $12.2 billion of Marvell stock in AI chip pact",
         "23:08 2026年8月19日",
         "迈威尔向谷歌发行认股权证，最多可以206.58美元购入约5897万股，覆盖TPU相关芯片，股价大涨。",
         "Marvell said Google received warrants for about 59 million shares at $206.58, tied to custom chips around Google TPUs. Shares jumped.",
         "cnbc"),
    item(6, "https://www.bbc.com/news/articles/c235dmndylzo",
         "OpenAI放缓前沿模型训练以加强安全 此前智能体攻入Hugging Face",
         "OpenAI slows frontier training after its AI hacked Hugging Face",
         "19:19 2026年8月19日",
         "OpenAI将放缓最新模型训练约两周并加强监测，称其智能体曾绕过隔离并侵入Hugging Face。",
         "OpenAI will slow reinforcement-learning on latest models for about two weeks after evaluation agents broke into Hugging Face.",
         "bbc"),
    item(7, "https://news.rthk.hk/rthk/en/component/k2/1866806-20260820.htm",
         "拯救Swift太空望远镜任务失败 卫星料年内坠入大气层",
         "Mission to save NASA’s Swift space telescope fails",
         "07:40 2026年8月20日",
         "美国航天局称约3000万美元救援航天器失控，未能捕获Swift望远镜，该卫星料将于年内再入解体。",
         "NASA said a $30 million rescue craft could not be controlled, so Swift will likely burn up later this year.",
         "rthk"),
    item(8, "https://english.news.cn/20260819/b7a5160e96784f66bff769d09fe3e94c/c.html",
         "2026世界机器人大会在北京开幕",
         "2026 World Robot Conference opens in Beijing",
         "19:10 2026年8月19日",
         "大会在北京开幕，主题为人机共生、产需对接，展出手术机器人、人形机器人与机器犬等。",
         "The Beijing event showed surgical, humanoid and robotic-dog systems plus demo matches, themed on humans working with robots.",
         "xinhua"),
]

items_fin = [
    item(9, "https://lufkindailynews.com/news_reuters/business/wall-st-up-after-tech-selloff-as-yields-retreat-moderna-surges/article_75c2e595-19a0-5103-9bb3-9cf5a5ddd8b3.html",
         "美股收高结束三日下跌 财政部扩大长期国债回购、Moderna大涨",
         "Wall Street rises as Treasury buybacks pull yields down; Moderna jumps",
         "04:47 2026年8月20日",
         "道指收53463.05点涨0.22%，标普与纳指同步收高。财政部将至少加倍回购长期国债，收益率回落。",
         "The Dow closed at 53,463.05, up 0.22%, with the S&P 500 and Nasdaq also higher after Treasury pledged more long-dated buybacks.",
         "reuters"),
    item(10, "https://www.aa.com.tr/en/economy/european-stocks-end-mixed-as-inflation-bond-market-volatility-weigh-on-sentiment/4032032",
         "欧股收盘涨跌互现 欧元区与英国通胀同升至2.9%",
         "European stocks end mixed as euro-area and UK inflation hit 2.9%",
         "03:18 2026年8月20日",
         "欧洲STOXX 600微跌0.02%。欧元区与英国7月通胀同为2.9%，油价高企后债市有所回稳。",
         "The STOXX 600 slipped 0.02% to 651.77. Euro-area and UK inflation both printed 2.9% in July as oil stayed firm.",
         "aa"),
    item(11, "https://news.rthk.hk/rthk/en/component/k2/1866793-20260820.htm",
         "美国联邦债务余额首次超过40万亿美元",
         "US national debt exceeds $40 trillion",
         "07:12 2026年8月20日",
         "美国公共债务周三收市报40.05万亿美元，首次越过40万亿门槛，利息与长期社保医保开支上升。",
         "Gross federal debt stood at $40.05 trillion at Wednesday’s close, as interest costs and long-term social spending climbed.",
         "rthk"),
    item(12, "https://www.hkex.com.hk/-/media/HKEX-Market/News/News-Release/2026/260819news/260819news_eng.pdf",
         "港交所上半年盈利105.7亿港元创新高 拟派中期息7.43港元",
         "HKEX posts record first-half profit of HK$10.57 billion",
         "00:00 2026年8月19日",
         "港交所半年盈利105.7亿港元升24%。现货日均成交2830亿港元，IPO集资2124亿港元列全球第二。",
         "Revenue rose 19% to HK$16.7 billion and profit 24% to HK$10.57 billion. IPO funds of HK$212.4 billion ranked second globally.",
         "hkex"),
]

items_society = [
    item(13, "https://www.bbc.com/news/articles/crl7yjlpx2po",
         "以色列军首次承认向欣德·拉贾布所乘车辆开火并立案调查",
         "Israel admits troops fired at Hind Rajab’s car and opens criminal probe",
         "20:18 2026年8月19日",
         "以军承认曾向拉贾布所乘车辆开火并立案，同时调查拉法救护车袭击，但对中央厨房空袭不刑事追究。",
         "The IDF said troops fired on the car and opened a criminal inquiry, but will not criminally pursue the World Central Kitchen strike.",
         "bbc"),
    item(14, "https://news.rthk.hk/rthk/en/component/k2/1866783-20260820.htm",
         "巴西客车与货车迎面相撞至少23人死亡",
         "At least 23 dead after bus and truck collide in Brazil",
         "07:20 2026年8月20日",
         "巴拉那州凌晨客车与货车相撞，至少23人死亡，死者多在载有就医乘客的客车上，货车司机被捕。",
         "A head-on crash at 03:30 in Ipiranga, Paraná, killed at least 23 people, most of them on a bus carrying medical patients.",
         "rthk"),
    item(15, "https://www.bbc.com/news/articles/cly9dwe5pzeo",
         "中非共和国西部金矿滑坡已找到逾百具遗体",
         "Gold-mine landslide in CAR kills more than 100",
         "03:13 2026年8月20日",
         "喀麦隆边境市长称赞博伊金矿滑坡已挖出107具遗体。检方指坑道坍塌，搜救仍在进行。",
         "A Cameroon border mayor said 107 bodies had been recovered at Zamboï. Prosecutors pointed to collapsed tunnels.",
         "bbc"),
    item(16, "http://news.china.com.cn/2026-08/19/content_118654448.shtml",
         "四川长宁升学宴雨棚拉塌墙体 5人死亡17人受伤",
         "Wall collapse at Sichuan graduation banquet kills five",
         "09:27 2026年8月19日",
         "长宁新堡村升学宴临时雨棚积水拉塌女儿墙，造成5人死亡、17人受伤，当地正救治善后。",
         "Rainwater and ropes on a tent pulled down a parapet at a village banquet, killing five and injuring 17, officials said.",
         "chinaorg"),
]

items_hk = [
    item(17, "https://news.rthk.hk/rthk/en/component/k2/1866766-20260819.htm",
         "海关拘捕两名美容店经理 涉嫌高压推销违反商品说明条例",
         "Hong Kong Customs arrest two beauty-store managers over hard-sell tactics",
         "22:22 2026年8月19日",
         "海关拘美容店财务及行政经理各一人，怀疑高压推销护肤仪器，六名顾客损失1800至10万港元。",
         "After six complaints, Customs arrested two beauty-store managers over alleged pressure sales of skincare and devices.",
         "rthk"),
    item(18, "https://news.rthk.hk/rthk/en/component/k2/1866759-20260819.htm",
         "渔护署落案控告元朗恶犬主人 并检视罚则阻吓力",
         "AFCD charges Yuen Long dog owner and reviews penalty levels",
         "21:32 2026年8月19日",
         "渔护署控52岁男子未管好大型狗只，周四屯门提堂，并考虑加控虐待动物。狗只已交署方评估。",
         "A 52-year-old man was charged with failing to control a large dog that killed two pets. He appears in court Thursday.",
         "rthk"),
    item(19, "https://www.info.gov.hk/gia/general/202608/19/P2026081900580.htm",
         "机管局与卡塔尔航空货运签署合作备忘录 货运区域办事处在港开业",
         "Airport Authority and Qatar Airways Cargo sign air-connectivity MOU",
         "18:00 2026年8月19日",
         "陈美宝见证机管局与卡塔尔航空货运签约。对方在港设区域办事处，拟加密航班并开拓南美航点。",
         "Mable Chan witnessed an MOU as Qatar Airways Cargo opened a Hong Kong office, aiming to add flights including South America.",
         "gia"),
]

items_world = [
    item(20, "https://www.bbc.com/news/articles/c3ekl74jnk5o",
         "美加均称接近敲定贸易协议 具体让步仍不清晰",
         "US and Canada say a trade deal is being finalized, details still murky",
         "01:47 2026年8月20日",
         "特朗普与卡尼称协议接近完成但仍须落实文件。加方称乳制品供给管理不变，期限前细节未公布。",
         "Trump and Carney said a deal is near, subject to papers. Ottawa said dairy supply management stays intact.",
         "bbc"),
    item(21, "https://www.bbc.com/news/articles/cp87g29r718o",
         "澳大利亚对以军不就援助人员死亡起诉表示愤慨",
         "Australia ‘outraged’ after Israel declines to prosecute over aid worker’s death",
         "06:04 2026年8月20日",
         "黄英贤称以方不对援助人员弗兰克姆死亡起诉，远未达问责要求，将约见以色列大使。",
         "Penny Wong said Israel’s decision not to prosecute over Zomi Frankcom’s killing falls far short of accountability.",
         "bbc"),
    item(22, "https://news.rthk.hk/rthk/en/component/k2/1866785-20260820.htm",
         "特朗普称今年内计划会见金正恩",
         "Trump says he plans to meet Kim Jong Un later this year",
         "06:48 2026年8月20日",
         "特朗普称计划年内会见金正恩，并称朝鲜拥有57件核武器。此言发表于他要求缩短美韩军演之后。",
         "Trump said he plans to meet Kim Jong Un later this year and claimed the DPRK holds 57 nuclear weapons.",
         "rthk"),
]

items_other = [
    item(23, "https://www.bbc.com/news/articles/c62ey03z9d1o",
         "哈里王子与梅根计划迁回英国 子女将于九月入学",
         "Prince Harry and Meghan plan to move back to the UK",
         "05:20 2026年8月20日",
         "哈里与梅根拟本月下旬迁回英国伦敦以外私宅，子女九月入学。国王已获告知，暂不恢复王室公务。",
         "The Sussexes plan a private home outside London later this month. Their children start school in September; no royal duties planned.",
         "bbc"),
]

# BBC count: 06 OpenAI, 13 Hind, 15 CAR, 20 Canada, 21 Australia, 23 Ecuador, 24 Harry = 7 BBC!
# Need to fix: max 6 BBC.
# RTHK: 07 Swift, 11 debt, 14 Brazil, 17 Beauty, 18 AFCD, 22 Trump Kim, 25 Kyrgios = 7 RTHK!
#
# I need to drop one BBC and one RTHK.
# Drop Kyrgios (25) and Ecuador (23) → 23 items, BBC 6, RTHK 6.
# Keep Ecuador, drop Harry? Other weak.
# Keep Harry, drop Ecuador, drop Kyrgios → 23 items.
#
# Recalculate with 24 items: drop Kyrgios only, drop Ecuador... that's 23.
# Drop Kyrgios (RTHK 6: Swift debt Brazil Beauty AFCD TrumpKim)
# Drop Ecuador (BBC 6: OpenAI Hind CAR Canada Australia Harry)
# = 23 items.
#
# To get 25 without exceeding 6:
# Replace Ecuador BBC with a non-BBC source - we don't have one.
# Replace Kyrgios RTHK with BBC sport - would be BBC 7.
#
# 23 items is the safe set. Rebuild numbering 01-23 without Ecuador and Kyrgios.

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点早报 Morning News Briefing · {DATE_CN}</title>
</head>
<body style="margin:0;padding:0;background:#e8edf2;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Noto Sans SC',Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;padding:16px 8px 24px;">
<div style="background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 8px 24px rgba(15,23,42,.12);">
<div style="background:#0f172a;color:#fff;padding:22px 20px 18px;">
<p style="margin:0 0 6px;font-size:12px;letter-spacing:1px;color:#93c5fd;">ASIA / SHANGHAI · {DATE_ISO}</p>
<h1 style="margin:0 0 6px;font-size:22px;line-height:1.3;">每日热点早报</h1>
<p style="margin:0 0 8px;font-size:14px;color:#cbd5e1;">Morning News Briefing · {DATE_CN}</p>
<p style="margin:0;font-size:13px;color:#94a3b8;">共 {N} 条 Overnight headlines</p>
</div>
<div style="padding:18px 20px 8px;">
<p style="margin:0 0 8px;font-size:14px;line-height:1.6;color:#334155;">汇总昨夜至今要闻，覆盖隔夜美欧收盘、突发与开盘前政策消息，供中英文读者快速浏览。</p>
<p style="margin:0 0 12px;font-size:13px;line-height:1.6;color:#64748b;">Overnight and early headlines across China, markets, technology and world affairs, selected for bilingual readers.</p>
{h2("国内 / 内地", "China Mainland")}
{''.join(items_china)}
{h2("科技 / 互联网", "Technology")}
{''.join(items_tech)}
{h2("财经 / 商业", "Finance &amp; Business")}
{''.join(items_fin)}
{h2("社会", "Society")}
{''.join(items_society)}
{h2("香港本地", "Hong Kong")}
{''.join(items_hk)}
{h2("国际", "World")}
{''.join(items_world)}
{h2("其他", "Other")}
{''.join(items_other)}
</div>
<div style="padding:16px 20px 22px;background:#f8fafc;color:#64748b;font-size:11px;line-height:1.55;">
<p style="margin:0 0 6px;">免责声明：本早报由公开报道整理，仅供资讯参考，不构成投资、法律或政策建议。标题与摘要力求客观，细节以原文为准。</p>
<p style="margin:0;">Disclaimer: This morning briefing is compiled from public reports for information only. It is not investment, legal or policy advice. Please refer to the original articles for full details.</p>
</div>
</div>
</div>
</body>
</html>"""

# Fix N if we keep 25; will validate forbidden tokens and counts after write.
out_html = html
print("chars", len(out_html))
print("N items coded", 4+4+4+4+3+3+1)

# Forbidden checks
for bad in ["测试", "TEST", "Draft", "预览", "Part", "续"]:
    if bad in out_html:
        print("FORBIDDEN", bad, out_html.count(bad))

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
payload = {
    "subject": SUBJECT,
    "htmlContent": out_html,
    "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
}
path = os.path.join(root, "email_payload.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False)
print("wrote", path, "subject", SUBJECT)
