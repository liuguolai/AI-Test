#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-01."""
import json
import os

DATE = "2026-08-01"
SUBJECT = f"每日热点早报 Morning Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "国务院核准8台核电机组，总投资约1600亿元",
            "en_title": "China approves eight new nuclear reactors in coastal provinces",
            "published": "02:13 2026年8月1日",
            "zh_summary": "国务院周五核准浙江、广东、辽宁、山东四地共8台三代核电机组，总投资约1600亿元。",
            "en_summary": "China's State Council approved eight third-generation reactors across four coastal provinces, with estimated investment of 160 billion yuan.",
            "source_zh": "财新 Caixin Global",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-01/beijing-clears-eight-new-reactors-as-china-accelerates-nuclear-buildout-102470294.html",
        },
        {
            "zh_title": "中国60岁及以上人口达3.23亿，老龄化压力加剧",
            "en_title": "China's elderly population tops 323 million",
            "published": "00:23 2026年8月1日",
            "zh_summary": "民政部数据显示，2025年末60岁及以上人口3.23亿，占总人口23%，较2015年增逾1亿。",
            "en_summary": "Official data show 323.38 million people aged 60 and older by end-2025, equal to 23% of China's population.",
            "source_zh": "财新 Caixin Global",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-01/chinas-elderly-population-tops-323-million-as-aging-pressures-mount-102470288.html",
        },
        {
            "zh_title": "「华龙一号」2.0版亮相，六台机组纳入新核准项目",
            "en_title": "Hualong One 2.0 unveiled in new nuclear approvals",
            "published": "07:07 2026年8月1日",
            "zh_summary": "国务院常务会议核准四个核电项目共8台机组，其中6台采用「华龙一号」技术，两项为2.0版示范。",
            "en_summary": "A State Council meeting approved eight reactors, including six using domestically developed Hualong One technology with two 2.0 demos.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "http://www.ce.cn/xwzx/gnsz/gdxw/202608/t20260801_3121230.shtml",
        },
        {
            "zh_title": "政治局会议：加快已批基建支出，不搞大规模新刺激",
            "en_title": "Politburo pledges faster fiscal spending without major new stimulus",
            "published": "14:44 2026年7月30日",
            "zh_summary": "7月30日政治局会议称将加快已预算基建支出、推进「六大网络」，未推出大规模增量刺激方案。",
            "en_summary": "The Politburo pledged to accelerate already-budgeted infrastructure spending rather than launch major new stimulus measures.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.scmp.com/economy/policy/article/3362364/chinas-politburo-pledges-policy-support-spending-counteract-sluggish-growth",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "谷歌撤回地球AI图像功能，担忧虚假信息风险",
            "en_title": "Google withdraws Earth AI tool after misinformation warnings",
            "published": "00:09 2026年8月1日",
            "zh_summary": "谷歌上线不足48小时即暂停地球AI图像生成功能，因用户生成并传播可能违规的虚假卫星图。",
            "en_summary": "Google paused its new AI image tool in Google Earth less than 48 hours after launch amid misuse and misinformation concerns.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c9349yx2ydvo",
        },
        {
            "zh_title": "亚马逊财报超预期大涨，缓解市场对AI投入担忧",
            "en_title": "Amazon earnings beat lifts AI trade confidence",
            "published": "04:56 2026年8月1日",
            "zh_summary": "亚马逊季度业绩强劲，股价大涨，与微软财报一道缓解投资者对AI基础设施过度投入的担忧。",
            "en_summary": "Amazon's strong quarterly results, alongside Microsoft's report, eased investor fears about overspending on AI infrastructure.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.channelnewsasia.com/business/fed-hawks-push-yields-higher-stocks-give-back-gains-6289901",
        },
        {
            "zh_title": "苹果营收指引疲软，股价下挫拖累科技股分化",
            "en_title": "Apple sinks on lackluster revenue outlook",
            "published": "04:56 2026年8月1日",
            "zh_summary": "苹果给出疲软营收展望，股价下跌，与亚马逊等AI相关科技股形成鲜明分化。",
            "en_summary": "Apple shares fell after a lackluster revenue forecast, diverging from AI-linked peers that rallied on strong earnings.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/wall-street-stocks-dow-nasdaq-37d8d182f02f0fcdcf9f7db67e6dfadd",
        },
        {
            "zh_title": "联储理事库格勒提前辞职，特朗普可任命新人",
            "en_title": "Fed Governor Kugler resigns early, opening seat for Trump",
            "published": "04:00 2026年8月1日",
            "zh_summary": "美联储理事库格勒宣布8月8日提前离任，为特朗普任命新人进入利率决策委员会创造机会。",
            "en_summary": "Federal Reserve Governor Adriana Kugler will resign on August 8, giving President Trump a chance to appoint a replacement.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/live/cpqvdxzwv22t",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "特朗普解雇劳工统计局局长，质疑就业数据",
            "en_title": "Trump fires BLS chief after weak July jobs report",
            "published": "22:30 2026年7月31日",
            "zh_summary": "美国7月仅增7.3万就业，5—6月大幅下修后，特朗普无证据指控数据造假并解雇统计局局长。",
            "en_summary": "Trump fired the BLS commissioner after July added just 73,000 jobs and prior months were sharply revised down, alleging rigged data without evidence.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cvg3xrrzdr0o",
        },
        {
            "zh_title": "美股收低，弱就业与新关税打压市场信心",
            "en_title": "US stocks close lower on jobs data and new tariffs",
            "published": "04:00 2026年8月1日",
            "zh_summary": "弱就业数据与特朗普新一轮关税生效后，道指、标普和纳指周五收盘全线下跌。",
            "en_summary": "Major US indexes closed sharply lower Friday as weak jobs data and newly effective tariffs rattled investors.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/live/cpqvdxzwv22t",
        },
        {
            "zh_title": "欧元区7月通胀升至2.9%，核心通胀2.5%",
            "en_title": "Eurozone inflation rises to 2.9% in July",
            "published": "23:52 2026年7月31日",
            "zh_summary": "欧盟统计局初值显示，7月欧元区调和CPI同比2.9%，能源价格回升推动通胀抬头。",
            "en_summary": "Eurostat's preliminary data showed eurozone harmonised inflation climbed to 2.9% in July as energy prices turned higher.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.lse.co.uk/news/europe-close-stocks-finish-lower-as-profit-taking-kicks-in-lag925xn7p6shg1.html",
        },
        {
            "zh_title": "欧股冲高回落收跌，STOXX 600月末获利回吐",
            "en_title": "European shares close lower after record intraday high",
            "published": "23:52 2026年7月31日",
            "zh_summary": "欧股盘中创历史新高后回落，STOXX 600收跌0.1%，伦敦和苏黎世指数转跌。",
            "en_summary": "European shares gave up early gains to finish slightly lower, with the STOXX 600 down 0.1% after hitting a record intraday high.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.devdiscourse.com/article/business/3958038-european-stocks-notch-monthly-gain-on-earnings-optimism",
        },
        {
            "zh_title": "美债长端收益率创多年新高，通胀担忧升温",
            "en_title": "Long-dated Treasury yields hit multi-year highs",
            "published": "04:56 2026年8月1日",
            "zh_summary": "油价上涨与联储官员鹰派表态推升美债收益率，10年期触及2025年1月以来高位。",
            "en_summary": "Rising oil prices and hawkish Fed commentary pushed longer-dated Treasury yields to new multi-year highs.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://ca.marketscreener.com/news/stocks-boosted-by-tech-earnings-bond-yields-hit-multi-year-highs-ce7f50d8db8efe2c",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "休达逾5万人跨境后大批自愿返回摩洛哥",
            "en_title": "Tens of thousands leave Ceuta after mass border crossing",
            "published": "20:00 2026年7月31日",
            "zh_summary": "约5万至6万人涌入西班牙北非飞地休达，至少57人遇难，绝大多数已在周五晚间自愿返回摩洛哥。",
            "en_summary": "Up to 60,000 migrants crossed into Ceuta and at least 57 died, but most had voluntarily returned to Morocco by Friday evening.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/spain-ceuta-migration-66839d113f24ba80d08b36d2b337201c",
        },
        {
            "zh_title": "西班牙首相谴责休达边境冲击侵犯主权",
            "en_title": "Spain's PM condemns Ceuta crossing as sovereignty violation",
            "published": "20:00 2026年7月31日",
            "zh_summary": "桑切斯视察休达，称大规模越境侵犯西班牙领土完整，指责人口走私网络误导移民。",
            "en_summary": "Pedro Sánchez visited Ceuta and condemned the mass crossing as a violation of Spain's territorial integrity, blaming smuggling networks.",
            "source_zh": "半岛电视台 Al Jazeera",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/31/spain-pm-to-visit-ceuta-after-19-migrants-die-breaching-border-from-morocco",
        },
        {
            "zh_title": "国际足联放弃世界杯商业化引资计划",
            "en_title": "FIFA scraps private investment plan after global opposition",
            "published": "07:30 2026年8月1日",
            "zh_summary": "因欧足联等足协强烈反对并威胁抵制，因凡蒂诺宣布放弃出售世界杯等赛事股权的引资方案。",
            "en_summary": "FIFA president Gianni Infantino scrapped plans to sell stakes in World Cup commercial rights after widespread opposition from confederations.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/sport/football/articles/czekr6kn58po",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特朗普新一轮关税周五生效，多国面临更高税率",
            "en_title": "Trump's new tariff round takes effect on Friday",
            "published": "04:00 2026年8月1日",
            "zh_summary": "美国对巴西、瑞士、加拿大等多国商品加征10%至50%不等关税，全球股市承压下跌。",
            "en_summary": "New US tariffs ranging from 10% to 50% took effect on goods from Brazil, Switzerland, Canada and others, rattling global markets.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/live/cpqvdxzwv22t",
        },
        {
            "zh_title": "意大利暂停与西班牙申根协定，加强边境管控",
            "en_title": "Italy suspends Schengen agreement with Spain over Ceuta",
            "published": "20:00 2026年7月31日",
            "zh_summary": "休达移民危机后，意大利暂时中止与西班牙的申根自由流动安排，法国亦加强边境检查。",
            "en_summary": "Italy temporarily suspended open-border Schengen arrangements with Spain, and France pledged tighter border checks after the Ceuta crisis.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/spain-ceuta-migration-66839d113f24ba80d08b36d2b337201c",
        },
        {
            "zh_title": "冯德莱恩：休达局势不可接受，须打击人口走私",
            "en_title": "Von der Leyen calls Ceuta images unacceptable",
            "published": "20:00 2026年7月31日",
            "zh_summary": "欧盟委员会主席称休达画面不可接受，要求制止危险越境、瓦解走私网络并加快遣返。",
            "en_summary": "EU Commission President Ursula von der Leyen said Ceuta images were unacceptable and called for stopping dangerous crossings and swift returns.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/spain-ceuta-migration-66839d113f24ba80d08b36d2b337201c",
        },
        {
            "zh_title": "巴基斯坦布洛阿特峰雪崩，知名登山家普尔贾失踪",
            "en_title": "Avalanche on Broad Peak leaves famed climber Purja missing",
            "published": "21:15 2026年7月31日",
            "zh_summary": "10人登山队在巴基斯坦布洛阿特峰遇雪崩，已找到数具遗体，尼泊尔籍名将普尔贾等仍失踪。",
            "en_summary": "An avalanche hit a ten-member team on Pakistan's Broad Peak; several bodies were recovered while Nirmal Purja and others remain missing.",
            "source_zh": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cddjz1r01l8o",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "预立医疗指示条例生效，市民开始签署文件",
            "en_title": "Hong Kong end-of-life directive law takes effect",
            "published": "20:12 2026年7月31日",
            "zh_summary": "《预设医疗指示条例》周五生效，赋予末期病人拒绝维生治疗指令法律效力，市民开始签署。",
            "en_summary": "Hong Kong's Advance Decision on Life-sustaining Treatment Ordinance took effect Friday, giving legal status to end-of-life directives.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362579/residents-sign-directives-hong-kongs-new-end-life-law-takes-effect",
        },
        {
            "zh_title": "高院驳回87个内地家庭公立大学学费司法复核",
            "en_title": "High Court rejects mainland families' university fee challenge",
            "published": "22:35 2026年7月31日",
            "zh_summary": "高院裁定人才计划子女须居港满两年方可享本地生学费，87个内地家庭挑战政府政策败诉。",
            "en_summary": "Hong Kong's High Court rejected a bid by 87 mainland families to challenge tighter residency rules for subsidised university fees.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/education/article/3362597/mainland-chinese-families-lose-legal-challenge-over-public-university-fees",
        },
        {
            "zh_title": "香港二季度GDP同比增4.3%，出口强劲支撑",
            "en_title": "Hong Kong GDP grows 4.3% in second quarter",
            "published": "16:50 2026年7月31日",
            "zh_summary": "政府初估二季度经济同比增4.3%，出口增28.8%，政府预计下半年仍将稳健增长。",
            "en_summary": "Advance estimates showed Hong Kong's economy grew 4.3% year on year in Q2, supported by strong exports and resilient domestic demand.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362538/hong-kong-economy-grows-43-strong-external-trade-resilient-domestic-demand",
        },
        {
            "zh_title": "医管局呼吁社会支持母乳喂养母亲",
            "en_title": "Hospital Authority urges support for breastfeeding mothers",
            "published": "07:12 2026年8月1日",
            "zh_summary": "医管局称公院纯母乳喂养率降至15.5%，呼吁雇主与社区营造友善环境，帮助在职母亲。",
            "en_summary": "The Hospital Authority said exclusive breastfeeding rates have fallen to 15.5% and called for a more breastfeeding-friendly community.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864545-20260801.htm",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "当局撤回酒店客房强制配备逃生面罩要求",
            "en_title": "Hong Kong backtracks on mandatory hotel escape hoods",
            "published": "15:10 2026年7月31日",
            "zh_summary": "民政总署听取业界意见后，不再强制酒店客房及公共区域配备防烟面罩，改为鼓励自愿落实。",
            "en_summary": "Hong Kong authorities backtracked on requiring hotels to provide fire escape hoods, saying they will only encourage provision in guest rooms.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362509/hong-kong-backtracks-requiring-hotels-put-fire-escape-hoods-rooms",
        },
        {
            "zh_title": "超强台风「海豚」下周末或令香港酷热",
            "en_title": "Super Typhoon Dolphin may bring very hot weather to Hong Kong",
            "published": "15:18 2026年7月31日",
            "zh_summary": "天文台指超强台风「海豚」趋向日本以南海域，外围下沉气流或令华南沿岸下周末天气炎热。",
            "en_summary": "The Observatory said Super Typhoon Dolphin's outer subsiding airstream may bring very hot weather to southeastern China late next week.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362511/super-typhoon-dolphin-set-bring-very-hot-weather-hong-kong-next-week",
        },
    ]),
]

def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">',
        f'<title>每日热点早报 Morning Briefing - {DATE}</title></head>',
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">',
        '<tr><td align="center">',
        '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">',
        '<tr><td style="background:linear-gradient(135deg,#1a2332 0%,#2c3e6b 100%);padding:28px 24px;text-align:center;">',
        '<div style="color:#fff;font-size:26px;font-weight:700;letter-spacing:1px;">每日热点早报</div>',
        f'<div style="color:#a8c4e8;font-size:14px;margin-top:8px;">Morning News Briefing · {DATE} · 共 {total} 条</div>',
        '</td></tr>',
        '<tr><td style="padding:20px 24px;background:#f8f9fb;border-bottom:1px solid #e8eaed;">',
        '<p style="margin:0 0 8px;font-size:14px;color:#333;line-height:1.6;">昨夜至今，全球政经、科技与社会热点一览。</p>',
        '<p style="margin:0;font-size:13px;color:#666;line-height:1.5;font-style:italic;">Overnight and early headlines from politics, business, tech and society.</p>',
        '</td></tr>',
    ]
    num = 0
    for cat_name, items in CATEGORIES:
        parts.append(
            f'<tr><td style="padding:16px 24px 8px;">'
            f'<h2 style="margin:0;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:16px;color:#1a2332;border-radius:0 6px 6px 0;">{cat_name}</h2>'
            f'</td></tr>'
        )
        for item in items:
            num += 1
            n = f"{num:02d}"
            parts.append(
                f'<tr><td style="padding:12px 24px;border-bottom:1px solid #eef0f3;">'
                f'<div style="font-size:11px;color:#2563eb;font-weight:700;margin-bottom:6px;">{n}</div>'
                f'<a href="{item["url"]}" style="font-size:16px;font-weight:600;color:#1a2332;text-decoration:none;line-height:1.4;">{item["zh_title"]}</a>'
                f'<div style="font-size:13px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;">{item["en_title"]}</div>'
                f'<div style="font-size:11px;color:#999;margin-top:4px;">发布时间 Published: {item["published"]}</div>'
                f'<p style="font-size:14px;color:#333;margin:10px 0 4px;line-height:1.6;">{item["zh_summary"]}</p>'
                f'<p style="font-size:13px;color:#666;margin:0 0 10px;line-height:1.5;font-style:italic;">{item["en_summary"]}</p>'
                f'<span style="display:inline-block;background:#e8f0fe;color:#1a56db;font-size:11px;padding:3px 8px;border-radius:4px;margin-right:8px;">{item["source_zh"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>'
                f'</td></tr>'
            )
    parts.extend([
        '<tr><td style="padding:20px 24px;background:#f8f9fb;border-top:1px solid #e8eaed;">',
        '<p style="margin:0 0 6px;font-size:11px;color:#999;line-height:1.6;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>',
        '<p style="margin:0;font-size:11px;color:#999;line-height:1.6;font-style:italic;">This briefing is for informational purposes only. Copyright belongs to original publishers.</p>',
        '</td></tr>',
        '</table></td></tr></table></body></html>',
    ])
    return "".join(parts), total

def main():
    html, total = build_html()
    payload = {"subject": SUBJECT, "htmlContent": html, "recipients": RECIPIENTS}
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated {total} items, HTML length {len(html)} chars")
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
