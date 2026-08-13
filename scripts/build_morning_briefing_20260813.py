#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-08-13."""
import json
import os

BRIEFING_EDITION = "早报"
LOCAL_TIME = "10:15 2026年8月13日"
DATE_STR = "2026-08-13"
DATE_DISPLAY = "2026年8月13日"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中共中央发布讣告：国务院原总理朱镕基逝世，享年98岁",
            "en_title": "China mourns former Premier Zhu Rongji, economic reformer, dies at 98",
            "published": "11:06 2026年8月12日",
            "zh_summary": "新华社受权发布讣告，朱镕基因病医治无效于8月12日在北京逝世。",
            "en_summary": "Xinhua says Zhu Rongji, who led China into the WTO, died in Beijing on Aug 12 at 98.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/20260812/d58258c9e4444acbbb4b530103ae77ed/c.html",
        },
        {
            "zh_title": "台风「白海豚」余波：湖北多地展开抢险救灾",
            "en_title": "Rescue efforts continue in Hubei after Typhoon Dolphin flooding",
            "published": "08:48 2026年8月13日",
            "zh_summary": "新华社报道，湖北襄阳等地正抢修公路、排涝并恢复供电，全力消除风险。",
            "en_summary": "Xinhua reports crews in Hubei are clearing roads and pumping floodwater after Typhoon Dolphin.",
            "source_zh": "新华社", "source_en": "Xinhua / People's Daily",
            "url": "http://en.people.cn/n3/2026/0813/c90000-20488228.html",
        },
        {
            "zh_title": "国产C919客机首条国际商业航线北京至乌兰巴托开通",
            "en_title": "China's C919 jet launches first international commercial route",
            "published": "00:00 2026年8月12日",
            "zh_summary": "国航C919执飞北京—乌兰巴托航线，标志国产大飞机迈向国际市场新阶段。",
            "en_summary": "Air China's C919 begins Beijing-Ulaanbaatar service, its first international commercial route.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.china.org.cn/china/Off_the_Wire/2026-08/12/content_118644246.shtml",
        },
        {
            "zh_title": "央行二季度报告：预计主要经济体货币政策调整将相对温和",
            "en_title": "PBOC report sees milder global monetary policy shifts ahead",
            "published": "18:48 2026年8月12日",
            "zh_summary": "央行称海外央行立场趋于转向，但本轮调整幅度可能较以往更温和、冲击更小。",
            "en_summary": "The PBOC says major central bank shifts may be milder and less disruptive than in past cycles.",
            "source_zh": "澎湃新闻", "source_en": "The Paper",
            "url": "https://www.thepaper.cn/newsDetail_forward_33769463",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "Spotify将标注AI虚拟艺人并移出算法推荐",
            "en_title": "Spotify to badge AI Personas and exclude them from recommendations",
            "published": "00:00 2026年8月12日",
            "zh_summary": "平台9月中旬起为AI生成身份加徽章，除非用户已关注，否则不进入个性化推荐。",
            "en_summary": "From mid-September, AI Persona artists get badges and won't appear in algorithmic feeds by default.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvgxzmgejd5o",
        },
        {
            "zh_title": "巴西监管机构责令Discord暂停直播功能",
            "en_title": "Brazil orders Discord to suspend livestreaming after teen death",
            "published": "01:15 2026年8月13日",
            "zh_summary": "13岁女孩直播自杀事件后，ANPD称平台缺乏实时内容监测，限三日内执行暂停。",
            "en_summary": "Brazil's data authority ordered Discord to halt livestreams after a teen's death on the platform.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cgewpqxyrddo",
        },
        {
            "zh_title": "厦门医院完成国产机器人心脏微创手术",
            "en_title": "Chinese hospital performs robotic cardiac surgery with homegrown system",
            "published": "13:08 2026年8月12日",
            "zh_summary": "厦心医院团队90分钟完成二尖瓣修复，系国产远程介入机器人临床应用新进展。",
            "en_summary": "A Xiamen hospital used a domestically developed robot to repair a mitral valve in 90 minutes.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://en.people.cn/n3/2026/0812/c90000-20487941.html",
        },
        {
            "zh_title": "诉讼寻求叫停Truth Social向机构出售政策帖抢先权",
            "en_title": "Lawsuit seeks to ban paid early access to Trump's policy posts",
            "published": "00:00 2026年8月13日",
            "zh_summary": "自由新闻基金会等起诉，指付费API让华尔街抢先获取总统政策帖违反宪法平等访问权。",
            "en_summary": "A lawsuit challenges Truth Social's paid API giving traders early access to Trump's policy posts.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/trump-media-lawsuit-truth-social-access-wall-street-traders-7f057fd1dba31dd4e357c8bf635ee009",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "华尔街收高逼近纪录，AI财报与通胀数据提振情绪",
            "en_title": "Wall Street rises near record on AI earnings and softer inflation",
            "published": "00:00 2026年8月13日",
            "zh_summary": "标普500涨0.3%，CoreWeave等AI股大涨；7月通胀3.4%略低于预期，降息押注升温。",
            "en_summary": "The S&P 500 rose 0.3% as AI earnings beat and July inflation eased rate-hike fears.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-rates-trump-iran-chips-db541ced9f928f993bd3a17958a3deaa",
        },
        {
            "zh_title": "美国7月通胀符合预期，市场下调9月加息概率",
            "en_title": "Tame US inflation curbs Fed hike bets as stocks edge higher",
            "published": "11:33 2026年8月13日",
            "zh_summary": "彭博称核心通胀年率2.5%，标普逼近新高；交易员认为9月加息概率不足五成。",
            "en_summary": "Bloomberg says in-line inflation eased Fed hike bets, lifting stocks near record highs.",
            "source_zh": "彭博社", "source_en": "Bloomberg",
            "url": "https://www.swissinfo.ch/eng/stocks%2c-bonds-rise-as-tame-cpi-curbs-fed-hike-bets%3a-markets-wrap/91882530",
        },
        {
            "zh_title": "乌克兰袭击俄新罗西斯克粮港，两大终端停运",
            "en_title": "Ukraine strike halts two major Russian grain terminals at Novorossiysk",
            "published": "16:13 2026年8月12日",
            "zh_summary": "路透称两处年出口能力逾1500万吨的粮港受损停运，全球小麦期货应声上涨约3%。",
            "en_summary": "Reuters sources say two major Novorossiysk grain terminals halted ops after overnight strikes.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://hk.marketscreener.com/news/two-grain-terminals-at-russia-s-novorossiysk-halt-work-after-ukrainian-attack-sources-say-ce7859d8d88af325",
        },
        {
            "zh_title": "红海袭击致6死，美军在阿曼湾打击涉伊货船",
            "en_title": "Six killed in Red Sea attack; US strikes ship in Gulf of Oman",
            "published": "17:32 2026年8月12日",
            "zh_summary": "胡塞袭击致4船员与2救援人员死亡；美军称击落驶向伊朗港口的巴拿马籍货船舵机。",
            "en_summary": "Houthi attack killed six; US forces disabled a Panama-flagged ship heading to an Iranian port.",
            "source_zh": "路透社 / NBC", "source_en": "Reuters / NBC News",
            "url": "https://www.nbcnews.com/world/iran/iran-war-yemen-red-sea-ships-attacked-bab-el-mandeb-strait-rcna592068",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "英国NHS移植体系遭资深医生公开信批评",
            "en_title": "Leading doctor rebukes NHS chiefs over transplant crisis",
            "published": "09:48 2026年8月13日",
            "zh_summary": "移植机构医学总监指体制碎片化、人手透支，致手术临时取消与器官利用不可预测。",
            "en_summary": "NHS Blood and Transplant's medical director blamed fragmented systems for last-minute cancellations.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/crl711557e6o",
        },
        {
            "zh_title": "美国中西部强风暴致龙卷风洪水，多人伤亡",
            "en_title": "Midwest storms spawn tornadoes and flooding, deaths reported",
            "published": "00:00 2026年8月13日",
            "zh_summary": "印第安纳4岁男童等遇难，逾65万户断电；俄亥俄多地开展洪水救援与灾后清理。",
            "en_summary": "Severe Midwest storms killed several people and left over 650,000 customers without power.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/weather-derecho-tornado-flooding-power-midwest-83fd919c9394218c38df03bc9db8073d",
        },
        {
            "zh_title": "黎巴嫩议会投票废除死刑，系中东首例",
            "en_title": "Lebanon parliament votes to abolish death penalty",
            "published": "00:00 2026年8月11日",
            "zh_summary": "128席议会多数通过，真主党议员反对；死刑将改为终身苦役，法案待总统签署。",
            "en_summary": "Lebanon's parliament voted to end capital punishment, the first such move in the Middle East.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c8enj8p1xwgo",
        },
        {
            "zh_title": "刚果（金）埃博拉疫情死亡人数突破2000",
            "en_title": "DRC Ebola outbreak becomes second-largest ever, over 2,000 dead",
            "published": "16:46 2026年8月12日",
            "zh_summary": "NPR援引世卫官员称Bundibugyo毒株疫情检测滞后，约三分之二患者在家中死亡。",
            "en_summary": "NPR reports over 2,000 deaths in Congo's Bundibugyo Ebola outbreak, now the second-largest ever.",
            "source_zh": "NPR", "source_en": "NPR",
            "url": "https://www.nhpr.org/2026-08-12/ebola-outbreak-in-the-democratic-republic-of-congo-is-now-the-second-largest-ever",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "伊朗称重启临时停火谈判毫无进展",
            "en_title": "Iran says no progress on reviving interim peace deal with US",
            "published": "21:24 2026年8月12日",
            "zh_summary": "路透引消息人士称双方互指违约；霍尔木兹海峡关闭及航运袭击推高国际油价。",
            "en_summary": "An Iranian source told Reuters there is no progress reviving the June interim ceasefire deal.",
            "source_zh": "海峡时报 / 路透社", "source_en": "The Straits Times / Reuters",
            "url": "https://www.straitstimes.com/asia/iran-says-no-progress-on-reviving-interim-peace-deal-with-us",
        },
        {
            "zh_title": "乌军夜袭新罗西斯克，重创俄黑海舰队基地与粮港",
            "en_title": "Major Russian grain terminals hit in Ukraine Black Sea port attack",
            "published": "00:00 2026年8月12日",
            "zh_summary": "泽连斯基称发动「独特行动」；俄方称正改道波罗的海与里海港口以应对物流瓶颈。",
            "en_summary": "Ukraine struck Novorossiysk, damaging grain terminals and Russia's last major Black Sea naval base.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c5y49xp2wrno",
        },
        {
            "zh_title": "特朗普证实离土换机脱险，称受伊朗导弹威胁",
            "en_title": "Trump confirms he switched planes after NATO summit over threat",
            "published": "00:00 2026年8月12日",
            "zh_summary": "其公开登上「空军一号」后秘密换乘小飞机；内阁成员与记者留在诱饵机上起飞。",
            "en_summary": "Trump confirmed he secretly swapped aircraft in Turkey due to a credible Iranian missile threat.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c980r4wpl9lo",
        },
        {
            "zh_title": "白宫发言人莱维特宣布月底离职",
            "en_title": "White House press secretary Karoline Leavitt to leave post",
            "published": "00:00 2026年8月12日",
            "zh_summary": "特朗普称她将转任党外顾问；28岁的莱维特称需更多时间照顾两名幼子。",
            "en_summary": "Karoline Leavitt, 28, will step down at month's end to focus on her young children, Trump said.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvglzrvyrz3o",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "香港国际金融中心下一步：离岸人民币与金融科技",
            "en_title": "What comes next for Hong Kong as a global financial hub?",
            "published": "08:30 2026年8月13日",
            "zh_summary": "SCMP分析指离岸国债期货后，香港需拓展人民币产品、大宗商品交易与金融科技。",
            "en_summary": "SCMP says Hong Kong must expand yuan products, commodities trading and fintech to stay a hub.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363826/what-comes-next-hong-kong-global-financial-hub",
        },
        {
            "zh_title": "港大生涉300万诈骗案被捕，称自身亦受骗",
            "en_title": "Hong Kong student arrested over HK$3m scam",
            "published": "19:39 2026年8月12日",
            "zh_summary": "19岁女生被指冒充内地公安诈骗本地男子逾300万港元，警方呼吁青年警惕。",
            "en_summary": "Police arrested a 19-year-old student accused of swindling over HK$3m in an impersonation scam.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363804/hong-kong-student-arrested-over-hk3m-scam-deceived-same-swindlers",
        },
        {
            "zh_title": "渣打牵头合资推出港元稳定币机构试点",
            "en_title": "Standard Chartered-led venture launches HK dollar stablecoin",
            "published": "19:06 2026年8月12日",
            "zh_summary": "Anchorpoint Financial启动HKDAP beta，面向机构与专业投资者，零售使用或年底推出。",
            "en_summary": "Anchorpoint Financial began institutional beta rollout of its Hong Kong dollar-backed HKDAP stablecoin.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/business/cryptocurrency/article/3363800/hong-kong-stablecoin-selection-expands-standard-chartered-led-ventures-launch",
        },
        {
            "zh_title": "港生厕所涂鸦煽动罪获缓刑，系国安法下首例",
            "en_title": "Hong Kong student avoids jail for seditious graffiti",
            "published": "14:45 2026年8月12日",
            "zh_summary": "19岁被告获18个月缓刑；法院认定其年轻、自闭症及影响有限属「特殊情况」。",
            "en_summary": "A 19-year-old received probation for seditious graffiti, avoiding jail under the national security law.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363750/hong-kong-student-avoids-jail-seditious-graffiti-commercial-complex-toilet",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "西班牙等地民众观赏百年一遇日全食",
            "en_title": "Millions crowd Spanish cities for a total solar eclipse",
            "published": "00:00 2026年8月12日",
            "zh_summary": "伊比利亚半岛多地进入全食带，西班牙部署逾3.3万名警力保障观食安全与秩序。",
            "en_summary": "Millions in Spain watched the country's first total solar eclipse in over a century on Aug 12.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/solar-eclipse-spain-europe-iceland-sun-4748323b3df8272d546683cc1dbc1d15",
        },
        {
            "zh_title": "2026上海书展开幕，1420项活动数智共创",
            "en_title": "2026 Shanghai Book Fair opens with 1,420 reading events",
            "published": "07:38 2026年8月12日",
            "zh_summary": "双主场展期至8月18日，黑龙江任主宾省，融合AI创作体验与文商旅场景。",
            "en_summary": "Shanghai's book fair opened Aug 12 with 1,420 events across two main venues until Aug 18.",
            "source_zh": "澎湃新闻", "source_en": "The Paper",
            "url": "https://www.thepaper.cn/newsDetail_forward_33762063",
        },
        {
            "zh_title": "多瑙河低水位露出二战德军遗骸与军用摩托",
            "en_title": "Danube low water reveals WWII soldiers' remains in Budapest",
            "published": "12:10 2026年8月12日",
            "zh_summary": "布达佩斯河床发现两具德军遗骸及DKW摩托车，身份牌保存完好，将安葬于布达厄尔公墓。",
            "en_summary": "Drought-exposed Danube riverbed in Budapest revealed two WWII German soldiers and a motorcycle.",
            "source_zh": "BBC / 欧洲新闻台", "source_en": "BBC / Euronews",
            "url": "https://www.bbc.co.uk/news/articles/cm2gp3zmkpmo",
        },
        {
            "zh_title": "香港在吉隆坡设经贸办，邱应斌吁深化马港合作",
            "en_title": "New Hong Kong trade office to spur ties with Malaysia",
            "published": "11:38 2026年8月11日",
            "zh_summary": "商经局局长指2025年双边贸易升27.4%至348亿美元，冀在金融科技与绿色金融加强合作。",
            "en_summary": "Hong Kong opened a Kuala Lumpur trade office as bilateral trade rose 27.4% to $34.8bn in 2025.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865746-20260811.htm",
        },
    ]),
]

SOURCE_COLORS = {
    "BBC": "#bb1919", "AP": "#d32f2f", "Reuters": "#ff8000", "Xinhua": "#c62828",
    "SCMP": "#003366", "Bloomberg": "#2800d7", "The Paper": "#0066cc", "NPR": "#2e7d32",
    "RTHK": "#8b0000", "Euronews": "#003399",
}


def source_color(source_en):
    for k, v in SOURCE_COLORS.items():
        if k in source_en:
            return v
    return "#555555"


def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    n = 0
    body_parts = []
    for cat_name, items in CATEGORIES:
        body_parts.append(
            f'<h2 style="margin:28px 0 12px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #1a73e8;font-size:16px;color:#1a1a1a;">{cat_name}</h2>'
        )
        for item in items:
            n += 1
            num = f"{n:02d}"
            color = source_color(item["source_en"])
            body_parts.append(f'''
<div style="margin:0 0 18px;padding:0 0 16px;border-bottom:1px solid #eee;">
  <div style="font-size:11px;color:#1a73e8;font-weight:bold;margin-bottom:4px;">{num}</div>
  <a href="{item['url']}" style="font-size:15px;font-weight:bold;color:#1a1a1a;text-decoration:none;line-height:1.4;">{item['zh_title']}</a>
  <div style="font-size:13px;color:#555;font-style:italic;margin:4px 0 2px;line-height:1.4;">{item['en_title']}</div>
  <div style="font-size:11px;color:#888;margin:0 0 8px;">发布时间 Published: {item['published']}</div>
  <div style="font-size:13px;color:#333;line-height:1.55;margin-bottom:4px;">{item['zh_summary']}</div>
  <div style="font-size:12px;color:#666;line-height:1.5;margin-bottom:8px;">{item['en_summary']}</div>
  <span style="display:inline-block;background:{color};color:#fff;font-size:10px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} / {item['source_en']}</span>
  <a href="{item['url']}" style="font-size:12px;color:#1a73e8;text-decoration:none;">查看全文 Read more →</a>
</div>''')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点早报 {DATE_STR}</title></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);padding:28px 24px;text-align:center;">
  <div style="font-size:24px;font-weight:bold;color:#fff;margin-bottom:6px;">每日热点早报</div>
  <div style="font-size:14px;color:#c5cae9;">Morning News Briefing · {DATE_DISPLAY} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
  <p style="font-size:14px;color:#333;line-height:1.6;margin:0 0 6px;">汇总昨夜至今晨全球要闻，涵盖政策、市场与国际突发。</p>
  <p style="font-size:13px;color:#666;line-height:1.5;margin:0 0 16px;font-style:italic;">Overnight and early headlines from China and around the world.</p>
</td></tr>
<tr><td style="padding:0 24px 24px;">
{"".join(body_parts)}
</td></tr>
<tr><td style="background:#f8f9fa;padding:16px 24px;border-top:1px solid #eee;">
  <p style="font-size:11px;color:#999;line-height:1.5;margin:0;">本简报由自动化系统汇编，内容来源于公开新闻报道，仅供参考，不构成投资建议。版权归原媒体所有。</p>
  <p style="font-size:10px;color:#aaa;line-height:1.5;margin:6px 0 0;">This briefing is auto-compiled from public news sources for informational purposes only. Not investment advice. Content © original publishers.</p>
</td></tr>
</table></td></tr></table>
</body></html>'''
    return html, total


def main():
    html, total = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {DATE_STR}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    cat_counts = {c.split()[0]: len(items) for c, items in CATEGORIES}
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"TOTAL={total}")
    print(f"CATEGORIES={cat_counts}")
    print(f"HTML_CHARS={len(html)}")
    print(f"WROTE {path}")


if __name__ == "__main__":
    main()
