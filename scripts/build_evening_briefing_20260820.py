#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 2026-08-20 evening briefing email_payload.json."""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "email_payload.json")

# (category, zh_title, en_title, published, zh_sum, en_sum, src_zh, src_en, url, color)
ITEMS = [
    ("国内 China Mainland",
     "许家印一审获无期 恒大两公司合计罚158亿元",
     "Evergrande founder Hui Ka Yan sentenced to life in prison",
     "12:00 2026年8月20日",
     "深圳中院一审：许家印无期并没收全部财产，恒大与恒大地产合计罚158.2亿元，另有56人获刑。",
     "A Shenzhen court jailed Hui Ka Yan for life, confiscated his assets and fined Evergrande entities 15.82 billion yuan.",
     "新华社", "Xinhua",
     "https://www.news.cn/legal/20260820/737dfb54ab564fb8a549ba392af9fb0a/c.html", "#dc2626"),
    ("国内 China Mainland",
     "上海出台“沪八条” 卖旧买新最高补8万元",
     "Shanghai eases home policy with subsidies up to 80,000 yuan",
     "16:17 2026年8月20日",
     "上海六部门发布楼市措施：外环外卖旧买新最高可获8万元补贴，外环外二套房商贷首付可降至15%。",
     "Shanghai unveiled eight housing measures, including combined trade-in subsidies of up to 80,000 yuan and a 15% down payment outside the Outer Ring.",
     "新华社", "Xinhua",
     "http://district.ce.cn/newarea/roll/202608/t20260820_3159051.shtml", "#dc2626"),
    ("国内 China Mainland",
     "外交部：对伊制裁施压无助解决问题",
     "China says Iran sanctions will not solve the crisis",
     "15:41 2026年8月20日",
     "外交部发言人林剑回应美对伊朗经济施压时说，制裁无助解决问题，呼吁各方采取负责任举措、走政治外交途径。",
     "Spokesman Lin Jian said sanctions will not resolve the Iran standoff and urged political and diplomatic steps instead.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/ch/component/k2/1866867-20260820.htm", "#0f766e"),
    ("国内 China Mainland",
     "长江存储完成IPO辅导验收 上市筹备再进一步",
     "Yangtze Memory finishes IPO tutoring review",
     "07:09 2026年8月20日",
     "证监会信息显示，长江存储控股IPO辅导状态改为验收，辅导券商为中信证券与中信建投，距离申报更近一步。",
     "YMTC’s IPO tutoring status moved to acceptance, a required step before a formal A-share listing filing.",
     "财新", "Caixin",
     "https://companies.caixin.com/2026-08-20/102475883.html", "#b45309"),
    ("科技 Technology",
     "Canvas外泄波及四校逾15万人 公署认机构无违规",
     "Canvas breach hit 150,000 at four Hong Kong campuses",
     "12:44 2026年8月20日",
     "私隐公署查实Canvas外泄波及四所院校逾15万人，认定机构已采取可行防护措施、未违反私隐条例。",
     "Hong Kong’s privacy watchdog said more than 150,000 people at four institutions were affected, with no ordinance breach found.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/en/component/k2/1866848-20260820.htm", "#0f766e"),
    ("科技 Technology",
     "运输署年底起用人工智能审核车辆牌照",
     "Hong Kong to use AI for licence updates and traffic lights",
     "12:19 2026年8月20日",
     "运输署称年底起以人工智能核对牌照文件，网上车辆牌照更新可由十日缩至一日，并试点智能调灯。",
     "The Transport Department will use AI to process most online vehicle licence updates in one day and trial adaptive signals in Causeway Bay.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/en/component/k2/1866843-20260820.htm", "#0f766e"),
    ("科技 Technology",
     "拯救Swift望远镜任务失败 或于年内再入大气层",
     "NASA calls off $30m rescue of Swift space telescope",
     "11:31 2026年8月20日",
     "美国航天局称用于推高Swift轨道的探测器姿态失控，3000万美元救援终止，望远镜年内或再入焚毁。",
     "NASA and Katalyst scrapped the robotic boost after control failures, leaving the Swift observatory likely to burn up later this year.",
     "法新社", "AFP",
     "https://www.france24.com/en/americas/20260820-nasa-satellite-rescue-mission-fails-swift-telescope-set-to-fall-to-earth", "#1d4ed8"),
    ("科技 Technology",
     "莫德纳默沙东个性化疫苗三期降低黑色素瘤复发",
     "Moderna-Merck mRNA melanoma vaccine hits Phase 3 goals",
     "18:45 2026年8月19日",
     "两公司称个性化mRNA疫苗联合Keytruda在三期试验中延长无复发生存并降低远处转移风险，莫德纳股价大涨。",
     "The personalized mRNA shot plus Keytruda met recurrence and metastasis goals in resected melanoma, sending Moderna shares sharply higher.",
     "CNBC", "CNBC",
     "https://www.cnbc.com/2026/08/19/moderna-merck-cancer-vaccine-shows-initial-late-stage-melanoma-data.html", "#0369a1"),
    ("财经 Finance & Business",
     "港股随亚股反弹 恒指收升0.8%报25698",
     "Hang Seng rises 0.8% as healthcare and Asia rebound",
     "17:06 2026年8月20日",
     "恒指收升203点或0.8%报25698，成交2690亿港元；沪指升0.24%，韩股大涨近6%，生物医药走强。",
     "Hong Kong’s Hang Seng gained 203 points, or 0.8%, to 25,698, with healthcare leading and Seoul’s Kospi jumping nearly 6%.",
     "路透社", "Reuters",
     "https://news.rthk.hk/rthk/en/component/k2/1866876-20260820.htm", "#b45309"),
    ("财经 Finance & Business",
     "长和就巴拿马港口争议再启国际仲裁索偿超15亿美元",
     "CK Hutchison seeks over $1.5bn from Panama in treaty case",
     "11:49 2026年8月20日",
     "长和公告已就巴拿马违反投资保护条约展开国际仲裁，索偿逾15亿美元，指港口特许权被毁并遭接管。",
     "Li Ka-shing’s CK Hutchison launched investment-treaty arbitration against Panama, seeking more than $1.5 billion over two canal ports.",
     "财新", "Caixin",
     "https://companies.caixin.com/2026-08-20/102475934.html", "#b45309"),
    ("财经 Finance & Business",
     "香港7月通胀回落至1.7% 政府称整体温和",
     "Hong Kong inflation eases to 1.7% in July",
     "17:34 2026年8月20日",
     "统计处显示7月综合消费物价按年升1.7%，低于6月的2%；扣除一次性纾困后的基本通胀仍为1.9%。",
     "Headline consumer prices rose 1.7% year on year in July, down from 2% in June, while underlying inflation held at 1.9%.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/en/component/k2/1866879-20260820.htm", "#0f766e"),
    ("财经 Finance & Business",
     "日本7月出口升23.2%创单月纪录",
     "Japan’s July exports hit a record on 23% jump",
     "11:17 2026年8月20日",
     "日本7月出口按年升23.2%至11.5万亿日元创单月纪录，对美对华出货分别升22%与25.8%。",
     "Exports rose 23.2% to a record 11.5 trillion yen, beating forecasts, though Japan still posted a trade deficit.",
     "路透社", "Reuters",
     "https://news.rthk.hk/rthk/en/component/k2/1866829-20260820.htm", "#b45309"),
    ("社会 Society",
     "以军承认向辛德所乘车辆开火 并立案调查",
     "Israel admits troops fired on car in which Hind Rajab died",
     "06:06 2026年8月20日",
     "以军首次承认曾向加沙女童辛德·拉贾布所乘车辆开火，并对该案及15名救护人员死亡启动刑事调查。",
     "The Israeli military said troops fired on the car carrying five-year-old Hind Rajab and opened criminal probes into that case and a 2025 medic killing.",
     "BBC", "BBC",
     "https://www.bbc.com/news/articles/crl7yjlpx2po", "#b91c1c"),
    ("社会 Society",
     "巴西小型巴士与货车对撞至少23人死亡",
     "Brazil bus-truck crash kills at least 23 people",
     "07:20 2026年8月20日",
     "巴拉那州载病人小型巴士与货车对撞，当局称至少23人死亡、5人受伤，货车司机亦在遇难者之列。",
     "A minibus carrying patients hit a truck on a Paraná highway, killing at least 23 people, police said.",
     "BBC", "BBC",
     "https://www.bbc.com/news/articles/cpvwgk1n2k8o", "#b91c1c"),
    ("社会 Society",
     "英媒称哈里梅根拟迁回英国 子女已报名入学",
     "Harry and Meghan plan UK return, British media report",
     "07:39 2026年8月20日",
     "英媒称哈里与梅根拟月底离开美国、迁至伦敦以外私人住所，子女已报名新学年；王室称身份不会改变。",
     "British outlets said the Sussexes plan to leave the US this month for a private home outside London, with no change in royal status.",
     "法新社", "AFP",
     "https://news.rthk.hk/rthk/en/component/k2/1866805-20260820.htm", "#1d4ed8"),
    ("社会 Society",
     "基里奥斯承认药检呈可卡因阳性是重大失误",
     "Kyrgios says failed cocaine test was a huge mistake",
     "07:02 2026年8月20日",
     "澳网名将基里奥斯承认马略卡站药检呈可卡因代谢物阳性，已自8月4日起临时停赛，并称将承担责任。",
     "Nick Kyrgios apologised after a June test found a cocaine metabolite; he has been provisionally suspended since 4 August.",
     "法新社", "AFP",
     "https://news.rthk.hk/rthk/en/component/k2/1866780-20260820.htm", "#1d4ed8"),
    ("国际 World",
     "俄军夜袭基辅等地 乌方称至少13人死亡",
     "Russian strikes on Kyiv kill at least 13, Ukraine says",
     "09:43 2026年8月20日",
     "乌克兰称俄军以导弹和无人机夜袭首都等地，至少13人死亡、约40人受伤，泽连斯基指拦截弹短缺。",
     "Ukraine said at least 13 people were killed in overnight missile and drone strikes on Kyiv, as Zelensky again appealed for interceptors.",
     "BBC", "BBC",
     "https://www.bbc.co.uk/news/articles/c98vzmden5yo", "#b91c1c"),
    ("国际 World",
     "朝鲜向东部海域发射疑似弹道导弹",
     "North Korea fires suspected ballistic missile toward the sea",
     "17:28 2026年8月20日",
     "韩日称朝鲜向半岛以东海域发射疑似弹道导弹，已落于日本专属经济区以外，时值美韩军演提前收官。",
     "Seoul and Tokyo said North Korea fired a suspected ballistic missile eastward, outside Japan’s EEZ, during shortened US-South Korea drills.",
     "美国广播公司", "ABC News",
     "https://abcnews.com/International/north-korea-launches-ballistic-missile-us-south-korea/story?id=135798644", "#2563eb"),
    ("国际 World",
     "特朗普扬言对伊朗及其支持国加码经济打击",
     "Trump vows harsher economic measures on Iran and backers",
     "08:01 2026年8月20日",
     "特朗普称将对伊朗及其提供资金或物流支持的国家采取更严厉经济措施；伊朗外长斥其为转移视线。",
     "Donald Trump threatened severe economic costs for any country offering Iran a lifeline; Tehran called the warning a diversion.",
     "BBC", "BBC",
     "https://www.bbc.com/news/articles/c2k7e83ynj4o", "#b91c1c"),
    ("国际 World",
     "澳大利亚召见以大使 怒批拒查援助人员死亡",
     "Australia summons Israeli ambassador over aid worker deaths",
     "11:11 2026年8月20日",
     "澳外长黄英贤称对以军不对世界中央厨房澳籍雇员死亡立案感到愤慨，已召见以色列大使。",
     "Penny Wong said she was outraged Israel will not pursue a criminal inquiry into Australian aid worker Zomi Frankcom’s killing.",
     "法新社", "AFP",
     "https://news.rthk.hk/rthk/en/component/k2/1866834-20260820.htm", "#1d4ed8"),
    ("香港本地 Hong Kong",
     "国泰明年1月开通香港至阿拉木图直航",
     "Cathay Pacific to launch Hong Kong–Almaty flights in January",
     "13:49 2026年8月20日",
     "国泰宣布2027年1月9日起每周三班飞往阿拉木图，为中亚首个客运点，亦是香港与哈萨克斯坦唯一直航。",
     "Cathay will fly three times weekly to Almaty from 9 January 2027, its first Central Asia passenger route and the only nonstop HK-Kazakhstan link.",
     "南华早报", "SCMP",
     "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3364653/cathay-pacific-launch-direct-flights-between-hong-kong-and-almaty-january", "#0369a1"),
    ("香港本地 Hong Kong",
     "元朗两只小狗被咬死 饲主获准保释",
     "Yuen Long dog owner bailed after two pets killed",
     "11:54 2026年8月20日",
     "52岁男子被控未妥善控制大型犬，其犬只在元朗咬死两只小狗；他准三千元保释，案件10月再讯。",
     "A 52-year-old man was bailed on HK$3,000 after his large dog allegedly killed a poodle and a Bichon Frisé in Yuen Long.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/en/component/k2/1866840-20260820.htm", "#0f766e"),
    ("香港本地 Hong Kong",
     "容积率奖励试点被视为旧区重建关键一步",
     "Bonus plot ratio scheme hailed as urban renewal step",
     "17:40 2026年8月20日",
     "政府推出容积率奖励试点，七个目标旧区符合条件的重建项目可获两成额外楼面，业界称有助重建。",
     "Hong Kong will grant a 20% extra floor-area bonus for qualifying redevelopments of buildings aged 50 or above in seven older districts.",
     "香港电台", "RTHK",
     "https://news.rthk.hk/rthk/en/component/k2/1866872-20260820.htm", "#0f766e"),
    ("其他 Other",
     "新西兰新锐政党主张全民基本收入并以土地税筹资",
     "New Zealand party pitches universal basic income funded by land tax",
     "15:37 2026年8月20日",
     "机会党主张以1.75%土地税向多数居民发放年约1.94万新西兰元基本收入，两大党已排除采纳该税改。",
     "Opportunity’s leader said a NZ$19,400 basic income funded by a 1.75% land tax would also cool house prices; major parties ruled it out.",
     "路透社", "Reuters",
     "https://news.rthk.hk/rthk/en/component/k2/1866859-20260820.htm", "#b45309"),
]


def zh_len(s):
    return len(re.sub(r"\s+", "", s))


def main():
    forbidden = ["测试", "TEST", "Draft", "预览", "Part", "省略"]
    # 续 is banned as a character in HTML body copy
    cats = {}
    srcs = {}
    for i, it in enumerate(ITEMS, 1):
        cat, zh_t, en_t, pub, zh_s, en_s, sz, se, url, col = it
        cats[cat] = cats.get(cat, 0) + 1
        srcs[se] = srcs.get(se, 0) + 1
        assert zh_len(zh_s) <= 55, (i, zh_len(zh_s), zh_s)
        assert len(en_s.split()) <= 30, (i, len(en_s.split()), en_s)
        blob = zh_t + en_t + zh_s + en_s + sz + se
        for w in forbidden:
            assert w not in blob, (i, w)
        assert "续" not in (zh_t + zh_s)
        assert pub and url.startswith("http")
    assert 20 <= len(ITEMS) <= 28, len(ITEMS)
    for k, v in srcs.items():
        assert v <= 6, (k, v)

    n = len(ITEMS)
    rows = []
    cur = None
    num = 0
    for it in ITEMS:
        cat, zh_t, en_t, pub, zh_s, en_s, sz, se, url, col = it
        if cat != cur:
            cur = cat
            rows.append(
                f'<h2 style="margin:18px 0 10px;padding:8px 12px;background:#f1f5f9;border-left:4px solid #2563eb;'
                f'font-size:16px;color:#0f172a;border-radius:0 6px 6px 0">{cat}</h2>'
            )
        num += 1
        nn = f"{num:02d}"
        rows.append(
            f'<div style="padding:12px 0;border-bottom:1px solid #e2e8f0">'
            f'<div style="font-size:12px;color:#64748b;margin-bottom:4px">{nn}</div>'
            f'<a href="{url}" style="color:#1d4ed8;text-decoration:none;font-size:16px;font-weight:700;line-height:1.4">{zh_t}</a>'
            f'<div style="font-style:italic;color:#334155;font-size:14px;margin-top:4px">{en_t}</div>'
            f'<div style="font-size:12px;color:#64748b;margin-top:4px">发布时间 Published: {pub}</div>'
            f'<p style="margin:8px 0 4px;font-size:14px;color:#1e293b;line-height:1.55">{zh_s}</p>'
            f'<p style="margin:0 0 8px;font-size:13px;color:#475569;line-height:1.5">{en_s}</p>'
            f'<span style="display:inline-block;background:{col};color:#fff;font-size:11px;padding:2px 8px;border-radius:10px">{sz} {se}</span>'
            f' <a href="{url}" style="font-size:13px;color:#2563eb;margin-left:8px">查看全文 Read more →</a>'
            f"</div>"
        )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点晚报 Morning placeholder avoided</title></head>
<body style="margin:0;padding:0;background:#e5e7eb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#e5e7eb">
<tr><td align="center" style="padding:16px 8px">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;box-shadow:0 8px 24px rgba(15,23,42,.12);overflow:hidden">
<tr><td style="background:#0f172a;padding:22px 24px;color:#fff">
<div style="font-size:22px;font-weight:800;letter-spacing:.02em">每日热点晚报</div>
<div style="font-size:13px;color:#cbd5e1;margin-top:6px">Evening News Briefing · 2026年8月20日 · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px">
<p style="margin:0 0 8px;font-size:15px;color:#0f172a;line-height:1.6">今日晚报汇总全日要闻：许家印一审获刑、上海楼市新政、港股收盘与基辅遇袭等。</p>
<p style="margin:0 0 12px;font-size:14px;color:#475569;line-height:1.6">Today’s evening briefing gathers the day’s main stories, from Evergrande’s verdict and Shanghai housing measures to market closes and strikes on Kyiv.</p>
{''.join(rows)}
</td></tr>
<tr><td style="padding:16px 24px 24px;background:#f8fafc;color:#64748b;font-size:11px;line-height:1.6">
本邮件为新闻摘要，内容整理自公开报道，不构成投资、法律或政策建议。链接指向原文，请以原媒体为准。<br>
This briefing summarises publicly reported news for information only. It is not investment, legal or policy advice. Please refer to the original publishers.
</td></tr>
</table>
</td></tr></table>
</body></html>"""

    # Fix accidental "Morning" in title
    html = html.replace(
        "<title>每日热点晚报 Morning placeholder avoided</title>",
        "<title>每日热点晚报 Evening News Briefing</title>",
    )
    assert "续" not in html
    for w in forbidden:
        assert w not in html, w
    # title had Morning then replaced
    assert "Morning" not in html
    assert "晚报" in html and "Evening" in html
    assert "每日热点早报" not in html
    assert "Morning Briefing" not in html and "Morning News" not in html
    assert "晚报" in html and "Evening" in html

    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-20",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("items", n)
    print("cats", cats)
    print("sources", srcs)
    print("chars", len(html))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
