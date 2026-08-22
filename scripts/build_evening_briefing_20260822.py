#!/usr/bin/env python3
"""Generate 2026-08-22 evening briefing HTML and email_payload.json."""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
PAYLOAD = os.path.join(ROOT, "email_payload.json")

CATS = [
    ("china", "国内 / 内地 China Mainland", "#1565c0"),
    ("tech", "科技 / 互联网 Technology", "#1565c0"),
    ("finance", "财经 / 商业 Finance & Business", "#1565c0"),
    ("society", "社会 Society", "#1565c0"),
    ("world", "国际 World", "#1565c0"),
    ("hk", "香港本地 Hong Kong", "#1565c0"),
    ("other", "其他 Other", "#1565c0"),
]

ITEMS = [
    {
        "cat": "china",
        "zh": "国常会部署适度超前建设新一代通信网",
        "en": "State Council urges moderately ahead-of-need next-generation networks",
        "pub": "00:17 2026年8月22日",
        "zh_s": "新华社解读称，会议要求统筹基础、空间、国际与融合网络，巩固信息通信业竞争优势。",
        "en_s": "Xinhua says the meeting called for coordinated terrestrial, space, international and fusion networks.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/20260822/0efa0c36501141059c70ea9580c1a01f/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "china",
        "zh": "中央网信委印发网信企业高质量发展行动计划",
        "en": "Cyberspace authorities issue 2026-2030 plan for internet firms",
        "pub": "20:07 2026年8月21日",
        "zh_s": "计划提出七项行动、二十一条举措，目标到2030年显著增强网信企业综合实力。",
        "en_s": "The plan sets seven actions and 21 measures to strengthen internet and cybersecurity firms by 2030.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/20260821/4f5b89230a884a0ab8f77281d3236819/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "china",
        "zh": "中国考古机构将首次赴南美联合发掘卡拉尔文明",
        "en": "Chinese archaeologists to begin first official South America fieldwork",
        "pub": "04:02 2026年8月22日",
        "zh_s": "社科院考古所在秘鲁签约，将与当地机构联合研究美洲迄今发现的最早文明。",
        "en_s": "CASS signed a Peru deal to study Caral, the earliest known civilization in the Americas.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/world/20260822/e9ea823697be4751b4adf5255167b215/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "china",
        "zh": "国常会要求加力清理拖欠企业账款并严防新增",
        "en": "Cabinet orders faster clearance of unpaid bills owed to firms",
        "pub": "20:04 2026年8月21日",
        "zh_s": "会议部署打通连环清偿链条，整治大企业拖欠中小企业账款，并明确合理账期。",
        "en_s": "Officials pledged to break payment chains and curb large firms delaying sums owed to smaller suppliers.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://m.cnfin.com/yw-lb/zixun/20260821/4458842_1.html",
        "color": "#c41e3a",
    },
    {
        "cat": "tech",
        "zh": "业界称中国具身智能正处规模化应用关键窗口",
        "en": "China embodied AI said to be at a scale-up tipping point",
        "pub": "20:26 2026年8月21日",
        "zh_s": "中国电子学会称上半年人形机器人出货已超四万台，产品正由小批量试用转向落地。",
        "en_s": "The CIE says humanoid shipments topped 40,000 in the first half as pilots move toward wider use.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.xinhuanet.com/20260821/391a5ffcf0d847e1a5cc193bdb41c529/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "tech",
        "zh": "空客称人工智能硬件已接棒跨境电商成货运增量",
        "en": "Airbus says AI hardware has overtaken e-commerce as air-cargo growth",
        "pub": "13:28 2026年8月22日",
        "zh_s": "空客货机业务负责人在北京表示，人工智能硬件以约7%运量贡献过半货值。",
        "en_s": "Airbus told Caixin AI hardware is about 7% of air-cargo volume but more than half of shipment value.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://companies.caixin.com/2026-08-22/102476830.html",
        "color": "#c9a227",
    },
    {
        "cat": "tech",
        "zh": "运输署年内推人工智能自动审批网上车辆牌照",
        "en": "Hong Kong to auto-approve most online licence renewals with AI",
        "pub": "12:19 2026年8月20日",
        "zh_s": "港台报道，年底系统可处理九成以上网上换领车辆牌照，审批由最多十个工作日缩至一日。",
        "en_s": "RTHK reports AI will handle over 90% of online renewals, cutting waits from ten working days to one.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866843-20260820.htm",
        "color": "#5c2d91",
    },
    {
        "cat": "finance",
        "zh": "美加贸易谈判破裂 华盛顿对约200亿美元加货征50%关税",
        "en": "US-Canada talks collapse as 50% tariffs hit about $20bn of goods",
        "pub": "15:08 2026年8月22日",
        "zh_s": "卡尼宣布中止谈判并将对等反制；美方称加方拒绝按此前谈妥条款收官。",
        "en_s": "Carney suspended talks and vowed dollar-for-dollar retaliation after Washington imposed Section 338 tariffs.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1867105-20260822.htm",
        "color": "#ff6600",
    },
    {
        "cat": "finance",
        "zh": "油价周五收涨 布伦特结算94.39美元",
        "en": "Oil finishes higher as Trump threatens sanctions on Iran partners",
        "pub": "08:44 2026年8月22日",
        "zh_s": "路透称布伦特涨0.7%报94.39美元，WTI报87.06美元，全周分别上涨约6.4%与5.7%。",
        "en_s": "Brent settled at $94.39 and WTI at $87.06, up about 6.4% and 5.7% on the week.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.businesstimes.com.sg/companies-markets/oil-rises-trump-threatens-sanctions-iran-partners",
        "color": "#ff6600",
    },
    {
        "cat": "finance",
        "zh": "金融监管总局发布保险公司资产负债管理办法",
        "en": "China insurance regulator issues asset-liability management rules",
        "pub": "22:58 2026年8月21日",
        "zh_s": "办法规范治理结构并设立监管指标，暂不达标公司可设三年过渡期并制定达标规划。",
        "en_s": "The NFRA set governance and ratio rules, with a three-year transition for insurers not yet compliant.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/20260821/fc3809f4bf8f489f9a51531b95e61c3d/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "finance",
        "zh": "两部门细化人民币买卖红线：流通人民币不得交易",
        "en": "PBOC bars trading of circulating yuan notes, allows withdrawn cash",
        "pub": "05:52 2026年8月22日",
        "zh_s": "人民银行与市场监管总局明确，现行流通人民币不得买卖，已停止流通券及纪念币可依法交易。",
        "en_s": "Circulating banknotes may not be sold; notes withdrawn from circulation and commemoratives may be traded.",
        "src_zh": "人民日报",
        "src_en": "People's Daily",
        "url": "http://finance.people.com.cn/n1/2026/0822/c1004-40784145.html",
        "color": "#c41e3a",
    },
    {
        "cat": "society",
        "zh": "英国蒂赛德警车与轿车相撞造成多人死亡",
        "en": "Multiple deaths after Teesside crash involving a police vehicle",
        "pub": "16:11 2026年8月22日",
        "zh_s": "克利夫兰警方称事故约凌晨3时39分发生在米德尔斯伯勒附近A66公路，现场仍封闭。",
        "en_s": "Cleveland Police said the A66 crash near Middlesbrough was at about 03:39 BST; the road stayed shut.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cx272ly3g00o",
        "color": "#bb1919",
    },
    {
        "cat": "society",
        "zh": "刚果（金）已接收首批埃博拉疫苗约1.65万剂",
        "en": "DR Congo receives first Ervebo batch as outbreak keeps spreading",
        "pub": "00:00 2026年8月22日",
        "zh_s": "卫生部长称晚间已到货16520剂，周一还将再到五万余剂，用于试验与一线人员。",
        "en_s": "Kinshasa said 16,520 Ervebo doses arrived, with more than 50,000 more expected by Monday.",
        "src_zh": "阿纳多卢通讯社",
        "src_en": "Anadolu Agency",
        "url": "https://www.aa.com.tr/en/africa/dr-congo-receives-1st-batch-of-vaccines-to-contain-ebola-outbreak/4034454",
        "color": "#e30a17",
    },
    {
        "cat": "society",
        "zh": "世卫警告刚果（金）埃博拉正以指数速度扩散",
        "en": "WHO says DR Congo Ebola outbreak is growing exponentially",
        "pub": "21:50 2026年8月21日",
        "zh_s": "协调员称死亡已近2500人，近半数发生在最近20天，感染范围已大于法国国土。",
        "en_s": "The WHO coordinator said nearly 2,500 have died, half in 20 days, across an area larger than France.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/czxe9n0vxzdo",
        "color": "#bb1919",
    },
    {
        "cat": "world",
        "zh": "美伊对峙升级 贝森特周一将公布对伊新制裁细节",
        "en": "US and Iran trade threats ahead of Monday sanctions briefing",
        "pub": "00:00 2026年8月22日",
        "zh_s": "特朗普称德黑兰尚未准备好达成他所称的正确协议，财政部将于周一说明新制裁。",
        "en_s": "Trump said Tehran is not ready for the right deal; Bessent will outline new Iran sanctions on Monday.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.globalbankingandfinance.com/us-iran-keep-up-hostile-rhetoric-ahead-new-sanctions/",
        "color": "#ff6600",
    },
    {
        "cat": "world",
        "zh": "菲律宾与日本宣布防务后勤互助协定正式生效",
        "en": "Philippines and Japan activate defense logistics sharing pact",
        "pub": "16:46 2026年8月22日",
        "zh_s": "国防部称双方武装力量可在演习和救灾中相互提供燃料、运输、维修等补给服务。",
        "en_s": "Manila said ACSA now lets the two militaries exchange fuel, transport and repair support on operations.",
        "src_zh": "马尼拉公报",
        "src_en": "Manila Bulletin",
        "url": "https://mb.com.ph/2026/08/22/ph-japan-activate-defense-logistics-pact",
        "color": "#0b3d91",
    },
    {
        "cat": "world",
        "zh": "以色列在约旦河西岸重建已撤离的卡迪姆定居点",
        "en": "Israel reopens the Kadim settlement two decades after evacuation",
        "pub": "00:00 2026年8月21日",
        "zh_s": "约三十户先行家庭已迁入杰宁附近山丘，斯莫特里奇称这是对2005年撤离的纠正。",
        "en_s": "About 30 families returned near Jenin after Israel lifted a 20-year ban; Smotrich called it a correction.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cn7n0l4p0kzo",
        "color": "#bb1919",
    },
    {
        "cat": "world",
        "zh": "伊朗警告称将对新的美国经济威胁给予毁灭性回应",
        "en": "Iran vows a devastating response as Washington prepares sanctions",
        "pub": "00:00 2026年8月22日",
        "zh_s": "军方称仍有能力干扰霍尔木兹海峡油运；贝森特称将实施史上最严厉金融制裁。",
        "en_s": "Tehran said it can still disrupt Hormuz traffic as Bessent pledged the toughest financial sanctions yet.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.thenews.pk/story/1433445-us-vows-to-tighten-financial-noose-around-iran-as-tehran-warns-of-sweeping-retaliation",
        "color": "#ff6600",
    },
    {
        "cat": "hk",
        "zh": "港府驳斥西方就支联会案定罪的批评",
        "en": "Hong Kong hits back at Western criticism of the Alliance verdict",
        "pub": "16:55 2026年8月22日",
        "zh_s": "政府发言人强烈谴责所谓抹黑，称法庭认定理由充分，判决合理并有扎实依据。",
        "en_s": "A spokesman condemned what he called baseless smears and said the verdict was well reasoned and sound.",
        "src_zh": "南华早报",
        "src_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/politics/article/3364918/hong-kong-hits-back-western-slander-over-verdict-tiananmen-vigil-leaders",
        "color": "#00838f",
    },
    {
        "cat": "hk",
        "zh": "陈国基：皇岗港方口岸第三场演练运作大致畅顺",
        "en": "Huanggang drill with Shenzhen judged broadly smooth, Chan says",
        "pub": "16:12 2026年8月22日",
        "zh_s": "逾万名公务员与近千辆车参与首次深港合作高峰负荷演练，下周六将再测峰值承载。",
        "en_s": "Over 10,000 civil servants and about 1,000 cars joined the first joint stress test with Shenzhen.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1867120-20260822.htm",
        "color": "#5c2d91",
    },
    {
        "cat": "hk",
        "zh": "建造业工会呼吁强制雇主提供户外工人风扇衣",
        "en": "Unions say fan jackets should be compulsory for outdoor workers",
        "pub": "15:38 2026年8月22日",
        "zh_s": "周思杰称工人现须自购风扇衣，并促请把中暑列入法定职业病以便索赔。",
        "en_s": "Union leaders said workers now buy the jackets themselves and asked that heatstroke become a listed disease.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1867114-20260822.htm",
        "color": "#5c2d91",
    },
    {
        "cat": "other",
        "zh": "首席大法官暂准白宫宴会厅工程先行推进",
        "en": "Chief justice lets Trump ballroom construction proceed for now",
        "pub": "10:30 2026年8月22日",
        "zh_s": "罗伯茨签署临时命令，使原定将迫使地面以上工程停工的下级法院裁决暂不生效。",
        "en_s": "Roberts issued a temporary order hours before lower-court rulings would have halted aboveground work.",
        "src_zh": "美联社",
        "src_en": "Associated Press",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1867094-20260822.htm",
        "color": "#1565c0",
    },
    {
        "cat": "other",
        "zh": "阿森纳主场3比0击败考文垂展开卫冕",
        "en": "Arsenal open title defence with a 3-0 win over promoted Coventry",
        "pub": "08:14 2026年8月22日",
        "zh_s": "哈弗茨、萨卡和厄德高各入一球，刚升级的考文垂时隔25年重返英超即告失利。",
        "en_s": "Havertz, Saka and Odegaard scored as Arteta’s side beat Coventry, back in the top flight after 25 years.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1867082-20260822.htm",
        "color": "#2e7d32",
    },
]


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def check_limits():
    banned = ["测试", "TEST", "Draft", "预览", "Part", "续"]
    for it in ITEMS:
        blob = "".join(it[k] for k in ("zh", "en", "zh_s", "en_s", "src_zh", "src_en"))
        for b in banned:
            if b in blob:
                raise SystemExit(f"banned token {b!r} in {it['zh']}")
        if len(it["zh_s"]) > 55:
            raise SystemExit(f"zh summary too long ({len(it['zh_s'])}): {it['zh']}")
        words = re.findall(r"[A-Za-z0-9']+", it["en_s"])
        if len(words) > 30:
            raise SystemExit(f"en summary too long ({len(words)}): {it['zh']}")


def build_html(n: int) -> str:
    counts = {k: 0 for k, _, _ in CATS}
    for it in ITEMS:
        counts[it["cat"]] += 1

    parts = []
    parts.append(
        f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点晚报 Morning placeholder</title>
</head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Noto Sans SC',Arial,sans-serif;color:#222;">
<div style="max-width:600px;margin:0 auto;padding:16px 8px 28px;">
<div style="background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 8px 24px rgba(15,23,42,.12);">
<div style="background:#12233a;color:#fff;padding:22px 22px 18px;">
<div style="font-size:22px;font-weight:700;letter-spacing:.04em;">每日热点晚报</div>
<div style="margin-top:6px;font-size:13px;color:#c5d4e8;">Evening News Briefing · 2026年8月22日 · 共 {n} 条</div>
</div>
<div style="padding:16px 22px 8px;font-size:14px;line-height:1.7;color:#334155;">
<div>汇总今日全日要闻，聚焦盘中政策、收市商品与白天已发酵的国际局势。</div>
<div style="margin-top:6px;color:#64748b;font-style:italic;">Today’s main stories, from Saturday policy and market closes to international news that developed through the day.</div>
</div>
"""
    )
    # Fix accidental 早报 word in title tag
    parts[0] = parts[0].replace(
        "<title>每日热点晚报 Morning placeholder</title>",
        f"<title>每日热点晚报 Evening News Briefing · 2026-08-22 · {n}</title>",
    )

    idx = 0
    for cat, title, _ in CATS:
        group = [it for it in ITEMS if it["cat"] == cat]
        if not group:
            continue
        parts.append(
            f'<div style="margin:8px 16px 0;padding:8px 12px;background:#f1f5f9;border-left:4px solid #1d4ed8;border-radius:0 8px 8px 0;">'
            f'<h2 style="margin:0;font-size:16px;color:#0f172a;">{esc(title)}</h2></div>'
            f'<div style="padding:4px 22px 8px;">'
        )
        for it in group:
            idx += 1
            num = f"{idx:02d}"
            parts.append(
                f'<div style="padding:14px 0;border-bottom:1px solid #e2e8f0;">'
                f'<div style="font-size:12px;color:#64748b;font-weight:700;">#{num}</div>'
                f'<div style="margin-top:4px;font-size:16px;font-weight:700;line-height:1.45;">'
                f'<a href="{esc(it["url"])}" style="color:#0f172a;text-decoration:none;">{esc(it["zh"])}</a></div>'
                f'<div style="margin-top:4px;font-size:13px;color:#475569;font-style:italic;">{esc(it["en"])}</div>'
                f'<div style="margin-top:4px;font-size:12px;color:#94a3b8;">发布时间 Published: {esc(it["pub"])}</div>'
                f'<div style="margin-top:8px;font-size:14px;line-height:1.65;color:#334155;">{esc(it["zh_s"])}</div>'
                f'<div style="margin-top:4px;font-size:13px;line-height:1.6;color:#64748b;">{esc(it["en_s"])}</div>'
                f'<div style="margin-top:10px;">'
                f'<span style="display:inline-block;background:{it["color"]};color:#fff;border-radius:999px;padding:3px 9px;font-size:11px;">{esc(it["src_zh"])} {esc(it["src_en"])}</span> '
                f'<a href="{esc(it["url"])}" style="font-size:12px;color:#1d4ed8;text-decoration:none;">查看全文 Read more →</a>'
                f"</div></div>"
            )
        parts.append("</div>")

    parts.append(
        """<div style="padding:18px 22px 24px;font-size:11px;line-height:1.6;color:#94a3b8;background:#f8fafc;">
本邮件为资讯整理，不构成投资、法律或政策建议；事实以原文为准。<br>
This briefing is an information digest only and is not investment, legal or policy advice. Please refer to the original reports.
</div>
</div></div>
</body></html>"""
    )
    html = "".join(parts)
    for bad in ("测试", "TEST", "Draft", "预览", "Part", "续"):
        if bad in html:
            raise SystemExit(f"banned token {bad!r} in HTML")
    return html


def main():
    check_limits()
    # Drop same-event extras: Iran thenews overlaps Global Banking; Ebola BBC overlaps AA.
    # Keep both Ebola items? Same outbreak - keep AA first-batch as Saturday update, drop BBC OR keep BBC as WHO warning (related but different angle).
    # Template: 同一事件只保留1条. Drop BBC Ebola, drop thenews Iran.
    global ITEMS
    ITEMS = [
        it
        for it in ITEMS
        if it["url"]
        not in {
            "https://www.bbc.com/news/articles/czxe9n0vxzdo",
            "https://www.thenews.pk/story/1433445-us-vows-to-tighten-financial-noose-around-iran-as-tehran-warns-of-sweeping-retaliation",
        }
    ]
    n = len(ITEMS)
    if n < 20 or n > 28:
        raise SystemExit(f"count {n} out of range")
    html = build_html(n)
    if len(html) > 100000:
        raise SystemExit(f"html too long: {len(html)}")
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-22",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    with open(PAYLOAD, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    cats = {}
    for it in ITEMS:
        cats[it["cat"]] = cats.get(it["cat"], 0) + 1
    srcs = {}
    for it in ITEMS:
        srcs[it["src_en"]] = srcs.get(it["src_en"], 0) + 1
    print("items", n, "chars", len(html), "cats", cats, "sources", srcs)
    print("banned-scan ok")


if __name__ == "__main__":
    main()
