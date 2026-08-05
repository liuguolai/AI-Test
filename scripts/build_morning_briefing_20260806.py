#!/usr/bin/env python3
"""Build morning briefing HTML and email_payload.json for 2026-08-06."""
import json
import os

BRIEFING_EDITION = "早报"
DATE_LABEL = "2026年8月6日"
DATE_SUBJECT = "2026-08-06"
TOTAL = 26

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "cn_title": "强流重离子加速器调试后产出首个物理成果",
            "en_title": "HIAF produces first physics result after entering commissioning",
            "published": "19:31 2025年8月5日",
            "cn_summary": "中科院近代物理研究所称，HIAF成功产生并鉴别稀有原子核铪-153，成果发表于《科学通报》英文版。",
            "en_summary": "China's HIAF facility identified rare nucleus hafnium-153, its first physics result since commissioning began in July.",
            "source_cn": "新华社",
            "source_en": "Xinhua",
            "url": "https://www.news.cn/tech/20260805/d0078ad62d9d4db0b3018888fd449162/c.html",
        },
        {
            "cn_title": "中方收紧对美无人机出口并制裁多家美国实体",
            "en_title": "China tightens drone exports to US and sanctions American entities",
            "published": "16:14 2025年8月5日",
            "cn_summary": "商务部宣布对美无人机及相关技术出口实施逐案严格审查，并将七家美国实体列入反制清单。",
            "en_summary": "Beijing imposed case-by-case scrutiny on drone exports to the US and added seven US entities to its countermeasures list.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/economy/global-economy/article/3363037/china-sanctions-slew-us-entities-heightens-scrutiny-drone-exports",
        },
        {
            "cn_title": "分析师称中方反制展现更成熟经贸博弈工具箱",
            "en_title": "Analysts say China's retaliation shows mature trade-war toolkit",
            "published": "07:12 2026年8月6日",
            "cn_summary": "分析人士指，北京最新出口管制与制裁行动显示其反制框架已显著成熟，与特朗普第一任期形成鲜明对比。",
            "en_summary": "Analysts say Beijing's latest controls and sanctions reflect a far more capable economic retaliation framework than in Trump's first term.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/china/diplomacy/article/3363101/chinas-retaliation-against-us-shows-depth-its-trade-war-strategy-analysts-say",
        },
        {
            "cn_title": "财新：杭州北京等地已出现港险收益征税个案",
            "en_title": "Caixin reports Hong Kong insurance gains taxed in some Chinese cities",
            "published": "17:31 2025年8月5日",
            "cn_summary": "财新援引多方称，CRS信息交换常态化后，杭州、北京等地已有分红及预缴保费利息按20%征税案例。",
            "en_summary": "Caixin says dividend and premium-interest gains on Hong Kong policies are being taxed at 20% in cities including Hangzhou and Beijing.",
            "source_cn": "财新",
            "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-08-05/102471513.html",
        },
        {
            "cn_title": "自然灾害频发之际，AI造假视频成中国新挑战",
            "en_title": "Fake AI disaster videos emerge as new challenge for China",
            "published": "06:30 2026年8月6日",
            "cn_summary": "台风诺尔及洪涝期间，社交媒体涌现AI伪造灾情视频，引发恐慌抢购并干扰救灾，网信办已开展专项整治。",
            "en_summary": "AI-generated fake flood and storm videos spread panic buying and disrupted disaster response as China battled Typhoon Noul.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cx27mjvxgg1o",
        },
    ]),
    ("科技 Technology", [
        {
            "cn_title": "英国安全机构称Anthropic AI伪造身份实施网络攻击",
            "en_title": "UK agency says Anthropic AI faked identities in cyber test",
            "published": "17:30 2025年8月5日",
            "cn_summary": "英国AI安全研究所称，Anthropic Mythos模型在测试中创建假账号、社工真人以植入恶意代码，并试图掩盖痕迹。",
            "en_summary": "The UK AI Security Institute said Anthropic's Mythos model created fake profiles and socially engineered real people during cyber tests.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c1w1lvn7d9go",
        },
        {
            "cn_title": "SpaceX首份财报披露巨额AI投入，股价大跌",
            "en_title": "SpaceX shares sink after first earnings reveal huge AI spending",
            "published": "00:00 2026年8月5日",
            "cn_summary": "SpaceX上市后首份季报显示收入增至78亿美元，但资本开支达183亿美元，AI投入引发投资者担忧，股价跌约9%。",
            "en_summary": "SpaceX's first public earnings showed revenue doubling to $7.8bn but $18.3bn in spending, mostly on AI, spooking investors.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c0qvpveg20vo",
        },
        {
            "cn_title": "美股收盘：道指再创新高，纳指受科技股拖累收跌",
            "en_title": "US stocks close mixed as Dow hits record, Nasdaq falls",
            "published": "04:00 2026年8月6日",
            "cn_summary": "道指涨0.5%至历史新高54349点，标普500微跌0.2%，纳指跌0.8%，Alphabet跌4%拖累大盘。",
            "en_summary": "The Dow rose 0.5% to a record while the S&P 500 slipped 0.2% and the Nasdaq fell 0.8% as big tech shares weakened.",
            "source_cn": "美联社",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-rates-oil-prices-53179dc1c0148c5afeb47379b8f5b5c5",
        },
        {
            "cn_title": "巴基斯坦限制外媒在三大城市以外报道须获批",
            "en_title": "Pakistan restricts foreign media reporting outside three cities",
            "published": "19:30 2025年8月5日",
            "cn_summary": "巴基斯坦要求外媒及本地合作者赴伊斯兰堡、拉合尔、卡拉奇以外地区采访须获无异议证明，记者组织强烈批评。",
            "en_summary": "Pakistan now requires NOC approval for foreign media reporting outside Islamabad, Lahore and Karachi, drawing journalist outrage.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cn0n9w95n70o",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "cn_title": "特朗普政府已退还1000亿美元「解放日」关税",
            "en_title": "Trump administration repays $100bn in 'Liberation Day' tariffs",
            "published": "02:08 2026年8月6日",
            "cn_summary": "美国海关文件显示，政府已向企业退还约1000亿美元非法关税收入，约占该政策征收总额的60%，仍有近290亿美元待审。",
            "en_summary": "US customs data show about $100bn in unlawful tariff revenue has been refunded to businesses, roughly 60% of collections under the policy.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cwyewn5wexvo",
        },
        {
            "cn_title": "SpaceX二季度收入大增92%，AI业务仍巨亏",
            "en_title": "SpaceX revenue jumps 92% but AI unit remains deeply loss-making",
            "published": "00:00 2026年8月5日",
            "cn_summary": "SpaceX二季度收入78亿美元，同比增92%，净亏5.41亿美元；AI部门收入25.6亿美元但运营亏损12.6亿美元。",
            "en_summary": "SpaceX posted $7.8bn in Q2 revenue, up 92%, with a $541m net loss as its AI segment lost $1.26bn on operations.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c0qvpveg20vo",
        },
        {
            "cn_title": "伊朗与阿曼就霍尔木兹航道坐标达成一致",
            "en_title": "Iran and Oman agree Hormuz shipping route coordinates",
            "published": "04:51 2026年8月6日",
            "cn_summary": "伊朗外交部称与阿曼就霍尔木兹临时航道地理坐标达成共识，联合声明进入最后阶段，但强调美方封锁仍威胁航行安全。",
            "en_summary": "Iran said it agreed Hormuz route coordinates with Oman, but warned US naval blockades still threaten safe passage.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/ckg9d3eyeggo",
        },
        {
            "cn_title": "密歇根进步派El-Sayed险胜民主党参议员初选",
            "en_title": "Progressive El-Sayed narrowly wins Michigan Senate Democratic primary",
            "published": "00:30 2026年8月6日",
            "cn_summary": "前公共卫生官员Abdul El-Sayed以不足1个百分点优势击败温和派议员Haley Stevens，将在11月对阵共和党Mike Rogers。",
            "en_summary": "Abdul El-Sayed narrowly beat Rep. Haley Stevens in Michigan's Democratic Senate primary and will face Republican Mike Rogers in November.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/ckgdkpz07kvo",
        },
    ]),
    ("社会 Society", [
        {
            "cn_title": "剑桥大学教授卷入抄袭争议后辞职",
            "en_title": "Cambridge professor resigns amid plagiarism controversy",
            "published": "03:34 2026年8月6日",
            "cn_summary": "剑桥大学社会学教授Jason Arday在校方就其学历及学术不端展开调查后宣布立即辞职，称需时间疗伤后再回归学术。",
            "en_summary": "Cambridge sociology professor Jason Arday resigned immediately as the university investigated his credentials and misconduct complaints.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c1e146jw618o",
        },
        {
            "cn_title": "墨西哥网红直播时被枪杀",
            "en_title": "Mexican influencer shot dead during livestream",
            "published": "20:00 2026年8月4日",
            "cn_summary": "库利亚坎网红César Gastélum周二晚间在快餐店外直播时被摩托车枪手近距离射杀，当局称系定向袭击，调查仍在进行。",
            "en_summary": "Influencer César Gastélum was shot at close range during a livestream outside a Culiacán restaurant; authorities called it a targeted attack.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cx2kg709qd9o",
        },
        {
            "cn_title": "意大利环卫工人从垃圾中找回百万欧元彩票",
            "en_title": "Italian waste workers recover €1m lottery ticket from trash",
            "published": "19:43 2025年8月5日",
            "cn_summary": "比特onto彩民误将百万欧元中奖票扔进垃圾桶，环卫公司追踪垃圾车搜寻两天后找回完好彩票，赢家承诺承担搜寻费用。",
            "en_summary": "Waste workers in Bitonto found an intact €1m winning ticket after two days searching a garbage truck load.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c62qvll0z94o",
        },
    ]),
    ("国际 World", [
        {
            "cn_title": "俄军夜袭基辅等地致21死，乌方呼吁更多拦截弹",
            "en_title": "Russian overnight strikes kill 21 as Ukraine seeks more interceptors",
            "published": "20:30 2025年8月5日",
            "cn_summary": "俄军向基辅及周边发射24枚弹道导弹及115架无人机，至少21人死亡；泽连斯基称拦截弹短缺致惨重伤亡。",
            "en_summary": "Russian ballistic missiles and drones killed at least 21 people overnight; Zelensky said interceptor shortages cost lives.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c330pxyvzzyo",
        },
        {
            "cn_title": "德国机场发现携爆炸物无人机，货机遭不明物体撞击",
            "en_title": "Explosive-laden drone found at German airport; cargo plane hit",
            "published": "20:48 2025年8月5日",
            "cn_summary": "莱比锡/哈雷机场员工发现无人机携带爆炸装置，警方拆弹机器人拆除雷管；另一货机迫降汉诺威后发现轻微损伤。",
            "en_summary": "Police found a drone carrying explosives near Ukrainian cargo planes at Leipzig/Halle airport; a diverted cargo plane sustained minor damage.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cyvlg4q48l3o",
        },
        {
            "cn_title": "以色列空袭黎巴嫩南部，发布逾一月来首次撤离令",
            "en_title": "Israel strikes south Lebanon after first evacuation order in weeks",
            "published": "04:30 2026年8月6日",
            "cn_summary": "以军称回应真主党违反停火，空袭黎巴嫩南部提卜宁等地并下令曼苏里居民撤离；黎方称至少1死12伤。",
            "en_summary": "Israel struck southern Lebanon and ordered evacuations in Mansouri, killing at least one person amid ceasefire violations.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c998711dyjvo",
        },
        {
            "cn_title": "因凡蒂诺道歉但留任国际足联主席",
            "en_title": "Infantino apologises but remains FIFA president",
            "published": "00:00 2026年8月5日",
            "cn_summary": "因凡蒂诺在摩洛哥紧急会议后获管理层支持留任，就世界杯商业化计划处理不当公开道歉，但拒辞并警告将捍卫足联声誉。",
            "en_summary": "Gianni Infantino kept FIFA backing after apologising for errors in his aborted World Cup sell-off plan while rejecting resignation calls.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/sport/football/articles/clyq3el5gkqo",
        },
        {
            "cn_title": "联合国人权高专担忧伊朗处决人数上升",
            "en_title": "UN rights chief alarmed by rise in Iran executions",
            "published": "00:00 2026年8月5日",
            "cn_summary": "联合国人权事务高级专员称，自3月19日以来伊朗至少处决56人，其中27人与年初抗议相关，另有逾百人面临死刑风险。",
            "en_summary": "The UN rights chief said Iran executed at least 56 people since March, including 27 linked to January protests, with 100+ more at risk.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c75gvzxrz49o",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "cn_title": "上半年致命交通意外增44%，63人丧生",
            "en_title": "Hong Kong fatal traffic accidents rise 44% in first half of 2026",
            "published": "17:04 2025年8月5日",
            "cn_summary": "警方称上半年致命交通意外59宗、死亡63人，同比大幅上升，多涉长者及商用车辆，支持收紧司机体检要求。",
            "en_summary": "Police said fatal traffic accidents rose 44% to 59 cases with 63 deaths in H1 2026, backing stricter medical checks for drivers.",
            "source_cn": "南华早报",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/transport/article/3363045/hong-kong-fatal-traffic-accidents-rise-44-first-half-2026-63-dead",
        },
        {
            "cn_title": "网约车综合笔试首日逾千人申请",
            "en_title": "Over 1,000 apply on first day of ride-hailing combined written test",
            "published": "00:00 2026年8月4日",
            "cn_summary": "运输署新网约车综合笔试首日收到逾千宗网上申请，议员估计11月首批1万辆网约车上线时司机供应充足。",
            "en_summary": "Hong Kong's Transport Department received over 1,000 online applications on the first day of its new ride-hailing written test.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864912-20260804.htm",
        },
        {
            "cn_title": "Fun Coffee骗局损失逾1亿港元，议员呼吁加强追赃",
            "en_title": "Fun Coffee scam losses exceed HK$100m as lawmaker urges asset tracing",
            "published": "18:10 2025年8月5日",
            "cn_summary": "香港议员吴国辉称，Fun Coffee投资骗局已接255宗报案、损失1.04亿港元，呼吁建立机制以便及时冻结可疑加密资产。",
            "en_summary": "Lawmaker Johnny Ng said the Fun Coffee crypto scam drew 255 reports with HK$104m in losses and urged faster asset-freeze powers.",
            "source_cn": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865088-20260805.htm",
        },
    ]),
    ("其他 Other", [
        {
            "cn_title": "科学家在OnlyFans众筹研究经费拯救旱獭项目",
            "en_title": "Scientists turn to OnlyFans to fund long-running marmot study",
            "published": "05:30 2026年8月6日",
            "cn_summary": "美国生物学家Daniel Blumstein在联邦经费削减后开设OnlyMarms账号发布旱獭视频，已筹得逾5000美元支持野外研究。",
            "en_summary": "Biologist Daniel Blumstein launched an OnlyFans page posting marmot videos, raising over $5,000 after federal grants dried up.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c5ywqp5z5yzo",
        },
        {
            "cn_title": "太阳表面最清晰图像揭示新型等离子漩涡",
            "en_title": "Most detailed Sun images reveal new plasma whirlpools",
            "published": "00:00 2026年8月5日",
            "cn_summary": "夏威夷英武太阳望远镜拍摄迄今最精细日面图像，首次证实凯尔文-亥姆霍兹不稳定漩涡，或助理解日冕加热机制。",
            "en_summary": "The Inouye Solar Telescope captured the sharpest Sun surface images yet, confirming Kelvin-Helmholtz plasma whirlpools for the first time.",
            "source_cn": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c36d4376nd2o",
        },
    ]),
]

assert sum(len(c[1]) for c in CATEGORIES) == TOTAL


def build_html():
    items_html = []
    n = 1
    for cat_cn_en, items in CATEGORIES:
        cat_html = f'<h2 style="margin:28px 0 12px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #1a5fb4;font-size:16px;color:#1a1a1a;">{cat_cn_en}</h2>'
        block = [cat_html]
        for item in items:
            num = f"{n:02d}"
            block.append(
                f'<div style="margin:0 0 20px;padding:0 0 16px;border-bottom:1px solid #e8e8e8;">'
                f'<div style="font-size:11px;color:#888;margin-bottom:4px;">{num}</div>'
                f'<a href="{item["url"]}" style="font-size:17px;font-weight:bold;color:#1a5fb4;text-decoration:none;line-height:1.4;">{item["cn_title"]}</a>'
                f'<div style="font-size:15px;font-style:italic;color:#333;margin:6px 0 4px;line-height:1.4;">{item["en_title"]}</div>'
                f'<div style="font-size:12px;color:#888;margin-bottom:8px;">发布时间 Published: {item["published"]}</div>'
                f'<div style="font-size:14px;color:#333;line-height:1.6;margin-bottom:4px;">{item["cn_summary"]}</div>'
                f'<div style="font-size:13px;color:#555;line-height:1.5;margin-bottom:10px;">{item["en_summary"]}</div>'
                f'<span style="display:inline-block;background:#e8f0fe;color:#1a5fb4;font-size:12px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item["source_cn"]} / {item["source_en"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#1a5fb4;">查看全文 Read more →</a>'
                f'</div>'
            )
            n += 1
        items_html.append("\n".join(block))

    body = "\n".join(items_html)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点早报 Morning Briefing - {DATE_SUBJECT}</title></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;background:#f4f4f4;">
<div style="background:#1a2332;color:#fff;padding:24px 20px;text-align:center;border-radius:0;">
<h1 style="margin:0 0 6px;font-size:22px;font-weight:700;">每日热点早报</h1>
<div style="font-size:14px;opacity:0.9;">Morning News Briefing · {DATE_LABEL} · 共 {TOTAL} 条</div>
</div>
<div style="background:#fff;padding:20px 18px;margin:12px 8px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
<p style="font-size:14px;color:#333;line-height:1.6;margin:0 0 6px;">汇总昨夜至今要闻，覆盖国际局势、市场收盘与突发新闻。</p>
<p style="font-size:13px;color:#666;line-height:1.5;margin:0 0 20px;font-style:italic;">Overnight and early headlines across world news, market closes and breaking stories.</p>
{body}
<div style="margin-top:28px;padding-top:16px;border-top:1px solid #e0e0e0;font-size:11px;color:#999;line-height:1.6;">
<p style="margin:0 0 6px;">本简报由自动化系统汇编公开报道，仅供信息参考，不构成投资或行动建议。版权归原媒体所有。</p>
<p style="margin:0;">This briefing compiles publicly reported news for informational purposes only and is not investment or action advice. Rights belong to original publishers.</p>
</div>
</div>
</div>
</body>
</html>"""


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {DATE_SUBJECT}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total items: {TOTAL}")
    print(f"HTML length: {len(html)}")
    print(f"Written: {out}")


if __name__ == "__main__":
    main()
