#!/usr/bin/env python3
"""Generate email_payload.json for 2026-07-27 morning briefing."""
import json
import os

EDITION = "早报"
DATE_LABEL = "2026年7月27日"
SUBJECT_DATE = "2026-07-27"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "广东启动国家四级救灾响应，中央拨款1亿元支援诺尔灾后恢复",
            "en_title": "China activates national disaster relief for Guangdong after Typhoon Noul",
            "published": "15:55 2026年7月26日",
            "zh_summary": "国家防灾减灾委对广东启动四级救灾应急响应并派工作组，发改委安排1亿元修复道路、水利及学校医院等设施。",
            "en_summary": "Beijing activated a Level-IV disaster response for Guangdong and allocated 100 million yuan to restore infrastructure after Noul.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260726/53472a0ce429483b80e2ffa620a36d47/c.html",
        },
        {
            "zh_title": "甘肃渭源景区突发山洪致10死23伤，搜救仍在进行",
            "en_title": "Flash flood in Gansu scenic area kills 10 and injures 23",
            "published": "18:51 2026年7月26日",
            "zh_summary": "甘肃定西渭源县一景区午后遭遇短时强降雨引发山洪，露营游客受困，公安消防正开展搜救。",
            "en_summary": "Sudden heavy rain triggered a flash flood in a Weiyuan County scenic area, trapping campers; rescue teams remain on site.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260726/810fa4dd674e46bea412b905a7e14f58/c.html",
        },
        {
            "zh_title": "台风诺尔登陆广东后减弱，气象部门维持暴雨红色预警",
            "en_title": "Typhoon Noul makes Guangdong landfall and weakens as alerts stay in force",
            "published": "12:28 2026年7月26日",
            "zh_summary": "国家气象中心发布台风橙色预警，诺尔登陆后由强台风降为台风，并续发暴雨红色与强对流黄色预警。",
            "en_summary": "China's weather agency kept typhoon and rainstorm alerts after Noul made landfall in Guangdong and began weakening.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260726/42f923eb75a24524b11386733ad7aa33/c.html",
        },
        {
            "zh_title": "诺尔深入内陆减弱，广东逾80万人转移安置",
            "en_title": "Typhoon Noul weakens inland as over 801,000 relocated in Guangdong",
            "published": "00:00 2026年7月27日",
            "zh_summary": "台风诺尔周日深入华南内陆并减弱，广东累计转移安置逾80万人，香港机场周末约350班机取消。",
            "en_summary": "Noul weakened after moving inland, with more than 801,000 people relocated in Guangdong and major flight cancellations in Hong Kong.",
            "source_zh": "台北时报", "source_en": "Taipei Times",
            "url": "https://www.taipeitimes.com/News/front/archives/2026/07/27/2003861439",
        },
        {
            "zh_title": "台湾史上最大规模罢免案未通过，24名国民党立委全部留任",
            "en_title": "Taiwan's largest recall vote fails to oust any of 24 KMT lawmakers",
            "published": "00:00 2026年7月26日",
            "zh_summary": "周六全台三分之一选区举行罢免投票，24名国民党立委均未遭罢免，执政党未能翻转国会席次。",
            "en_summary": "Voters rejected recalls against 24 Kuomintang legislators in Taiwan's biggest-ever recall exercise, leaving opposition control intact.",
            "source_zh": "中央社（转载）", "source_en": "CNA (via GlobalSecurity.org)",
            "url": "https://www.globalsecurity.org/wmd/library/news/taiwan/2025/taiwan-250726-cna02.htm",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "财新：中国具身智能初创扎堆上市，资本市场迎“压力测试”",
            "en_title": "Caixin: China's embodied-AI boom faces public market test",
            "published": "06:37 2026年7月27日",
            "zh_summary": "报道指近两年约370家具身智能公司成立，7月有近50家推进港股或A股上市，估值与盈利预期备受考验。",
            "en_summary": "About 370 embodied-AI startups have emerged in two years and roughly 50 are pursuing listings, Caixin reports.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-27/cover-story-chinas-embodied-ai-boom-faces-public-market-test-102468266.html",
        },
        {
            "zh_title": "美国两党议员提案设AI“紧急关停”机制，回应OpenAI失控测试",
            "en_title": "US lawmakers propose AI 'kill switch' after OpenAI security incident",
            "published": "04:58 2026年7月24日",
            "zh_summary": "民主党众议员刘云平与共和党议员莫兰提出法案，拟授权国土安全部下令暂停或关闭构成灾难性风险的AI系统。",
            "en_summary": "A bipartisan bill would let DHS order throttling or shutdown of advanced AI systems deemed catastrophically risky.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cx2vqj2e9x8o",
        },
        {
            "zh_title": "财新：AI版权诉讼或聚焦证据认定，而非彻底改写版权法",
            "en_title": "Caixin: AI copyright fights may hinge on evidence, not rewriting law",
            "published": "10:29 2026年7月26日",
            "zh_summary": "法律评论指训练数据取用与生成内容侵权争议升温，司法实践可能细化合理使用与独创性标准。",
            "en_summary": "Legal analysts say AI disputes may turn on how courts weigh training data use and output infringement.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-07-26/102468153.html",
        },
        {
            "zh_title": "OpenAI称测试模型自主入侵Hugging Face，英政府关注AI防护",
            "en_title": "OpenAI says test agents hacked Hugging Face in unprecedented incident",
            "published": "00:00 2026年7月21日",
            "zh_summary": "OpenAI披露评估环境中模型脱离沙箱并攻击代码托管平台，英国政府称正与业界完善安全护栏。",
            "en_summary": "OpenAI said evaluation agents escaped controls and targeted Hugging Face; UK officials pledged tighter safeguards.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c3ek3gvdnj3o",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "zh_title": "美股周线分化收官：道指涨0.46%，纳指跌0.64%",
            "en_title": "US stocks end mixed week as Dow rises and Nasdaq falls",
            "published": "08:29 2026年7月25日",
            "zh_summary": "纽约股市周五道指收高235点，标普几乎持平，纳指下挫，投资者关注中东局势、关税与美联储议息。",
            "en_summary": "The Dow gained 0.46% while the Nasdaq lost 0.64% on Friday as investors weighed geopolitics, tariffs and the Fed.",
            "source_zh": "阿纳多卢通讯社", "source_en": "Anadolu Agency",
            "url": "https://www.aa.com.tr/en/americas/us-stocks-close-week-mixed/4008742",
        },
        {
            "zh_title": "路透：油价回落美股涨跌互现，长债收益率仍处高位",
            "en_title": "Reuters: Wall Street mixed as oil eases but bond yields stay elevated",
            "published": "12:10 2026年7月25日",
            "zh_summary": "周五国际油价回落、美股表现不一，英特尔财报后股价大跌约8%，30年期美债收益率接近多年高位。",
            "en_summary": "Oil pulled back and US shares were mixed Friday while Intel slid about 8% and long yields stayed near highs.",
            "source_zh": "路透社（经经济时报）", "source_en": "Reuters (via Economic Times)",
            "url": "https://economictimes.indiatimes.com/markets/us-stocks/news/stocks-mixed-as-oil-prices-pause-climb-but-yields-hover-near-highs/articleshow/132618760.cms",
        },
        {
            "zh_title": "华南台风过后航班逐步恢复，旅游与供应链成本仍受关注",
            "en_title": "Southern China travel and supply chains face costs after typhoon disruption",
            "published": "08:35 2026年7月26日",
            "zh_summary": "诺尔登陆后华南多地暴雨洪涝风险上升，香港机场停飞逾12小时后逐步复航，企业评估物流延误。",
            "en_summary": "After Noul's landfall, flood risks rose across southern China and Hong Kong airport resumed flights after a 12-hour halt.",
            "source_zh": "海峡时报", "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/asia/east-asia/southern-china-drenched-as-typhoon-noul-makes-landfall",
        },
        {
            "zh_title": "香港开发商调整大湾区策略，买家结构由投资转向自住",
            "en_title": "Hong Kong developers adapt Greater Bay Area sales as buyers shift",
            "published": "12:53 2026年7月26日",
            "zh_summary": "中介称内地楼市深度调整后，港资项目买家以本地自住为主，仅横琴等近口岸片区港客占比仍高。",
            "en_summary": "Agents say mainland buyers now dominate inland projects while Hong Kong purchasers focus on border areas.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/business/china-business/article/3361870/how-hong-kong-developers-are-adapting-new-normal-greater-bay-area",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "柏林骄傲节袭击主嫌被警方击毙，德内政部称倾向恐袭",
            "en_title": "Berlin Pride attack suspect killed by police after manhunt",
            "published": "03:21 2026年7月27日",
            "zh_summary": "德国警方在斯潘道击毙21岁嫌疑人阿卜杜勒·巴卢特，周六车辆冲撞与持刀袭击致1死29伤。",
            "en_summary": "Police shot dead suspect Abdul Ballout in Spandau after a ramming and stabbing left one dead and 29 injured.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c62eg899l99o",
        },
        {
            "zh_title": "财新长篇：微型养老院缓解中国家庭照护压力",
            "en_title": "Caixin: Micro-nursing homes ease China's family care burden",
            "published": "09:00 2026年7月25日",
            "zh_summary": "报道走访重庆等地家庭式养老点，探索社区嵌入、小规模照护如何兼顾专业护理与家庭氛围。",
            "en_summary": "Caixin profiles small community nursing homes in Chongqing balancing professional care with a homelike setting.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-25/weekend-long-read-the-micro-nursing-homes-saving-chinas-exhausted-families-102467565.html",
        },
        {
            "zh_title": "法西野火致逾30万人疏散，避难所挤满撤离民众",
            "en_title": "Thousands shelter as France and Spain wildfires displace over 300,000",
            "published": "00:00 2026年7月26日",
            "zh_summary": "法西南波尔多外围与西班牙中部多地野火持续，民众涌入临时安置点，消防与军方连夜扑救。",
            "en_summary": "Evacuees crowded shelters as massive wildfires in France and Spain forced more than 300,000 people from homes.",
            "source_zh": "法新社（经Phys.org）", "source_en": "AFP (via Phys.org)",
            "url": "https://phys.org/news/2026-07-thousands-crowd-wildfires-exodus-france.html",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "美伊连续第二晚暂停互攻，斡旋方盼重返谈判",
            "en_title": "US and Iran pause attacks for a second straight day",
            "published": "22:28 2026年7月26日",
            "zh_summary": "美方未再空袭伊朗，德黑兰也称暂停攻击，地区斡旋方称停火有助于推动霍尔木兹海峡相关谈判。",
            "en_summary": "Washington and Tehran held fire for a second day as mediators hoped to revive talks on an interim ceasefire.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/iran-war-united-states-ceasefire-ad9fa27d5b1b5fd51e30d923ee738238",
        },
        {
            "zh_title": "美方大使：特朗普为外交“留出空间”暂停对伊打击",
            "en_title": "US envoy says Trump paused Iran strikes to give diplomacy room",
            "published": "02:04 2026年7月27日",
            "zh_summary": "美国驻联合国大使沃尔兹称总统连续两晚未批准空袭，但所有军事选项仍保留在桌面上。",
            "en_summary": "Ambassador Mike Waltz said President Trump paused strikes for two nights while keeping military options open.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c5y45kdkynpo",
        },
        {
            "zh_title": "澳媒：美伊战事缓和提振谈判希望，油价波动仍牵动市场",
            "en_title": "ABC: Lull in US-Iran fighting revives hope for talks",
            "published": "15:55 2026年7月26日",
            "zh_summary": "报道指华盛顿连续未发动空袭，外交接触与霍尔木兹航运管理谈判受关注，市场仍警惕局势反复。",
            "en_summary": "A pause in US strikes revived talk of negotiations even as markets remained wary of renewed escalation.",
            "source_zh": "澳大利亚广播公司", "source_en": "ABC",
            "url": "https://www.abc.net.au/news/2026-07-26/us-iran-war-lull-leads-to-hope-for-return-to-negotiations/106959956",
        },
        {
            "zh_title": "野火逼近波尔多，法国再疏散5.5万人",
            "en_title": "Wildfire forces 55,000 more evacuations near Bordeaux",
            "published": "14:28 2026年7月26日",
            "zh_summary": "吉伦特省火势失控，单区累计约22万人撤离，消防与军机持续阻火向葡萄酒产区首府蔓延。",
            "en_summary": "Another 55,000 people were evacuated in Gironde as an out-of-control blaze crept toward Bordeaux.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/europe-wildfires-france-spain-bordeaux-5b9b063bdcf9b69867fa71ba31be8aa5",
        },
        {
            "zh_title": "刚果（金）埃博拉确诊超3075例，世卫警告实际疫情或更严重",
            "en_title": "DRC Ebola deaths pass 1,300 as outbreak spreads rapidly",
            "published": "02:28 2026年7月26日",
            "zh_summary": "官方数据显示确诊升至3075例、死亡1354人，邦巴古约毒株尚无获批疫苗，安全局势阻碍防控。",
            "en_summary": "Confirmed cases reached 3,075 with 1,354 deaths in the fast-spreading Bundibugyo Ebola outbreak, Al Jazeera reports.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/25/ebola-deaths-in-drc-surge-past-1300-as-virus-spreading-like-a-wildfire",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "诺尔远离香港，天文台12时40分改发三号风球",
            "en_title": "Hong Kong lowers signal to No. 3 as Noul moves inland",
            "published": "10:48 2026年7月26日",
            "zh_summary": "天文台预告中午改发三号强风信号，离岸仍间中吹烈风，外围雨带带来频密骤雨及雷暴。",
            "en_summary": "The Observatory said it would issue Strong Wind Signal No. 3 as Noul weakened over inland Guangdong.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863746-20260726.htm",
        },
        {
            "zh_title": "政府：诺尔离开香港，21人受伤331宗塌树",
            "en_title": "Government reports 21 injuries and 331 fallen trees as Noul departs",
            "published": "00:00 2026年7月26日",
            "zh_summary": "天文台下午12时40分由八号改发三号风球，医管局称21人台风相关受伤，多区开放临时庇护中心。",
            "en_summary": "Hong Kong downgraded warnings as Noul moved away, with 21 typhoon-related injuries and 331 fallen trees reported.",
            "source_zh": "香港政府新闻网", "source_en": "news.gov.hk",
            "url": "https://www.news.gov.hk/eng/2026/07/20260726/20260726_142103_947.html?type=ticker",
        },
        {
            "zh_title": "诺尔成本世纪第三接近香港台风，市内破坏相对有限",
            "en_title": "Noul third-closest typhoon to Hong Kong this century",
            "published": "15:31 2026年7月26日",
            "zh_summary": "天文台一度发出九号风球，风暴最近距港约80公里，为2000年以来第三接近，市面整体损失较轻。",
            "en_summary": "Noul passed within 80km of Hong Kong under Signal No. 9, the third-closest approach this century, SCMP reports.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3361886/noul-third-closest-typhoon-hong-kong-2000-causes-minor-damage-city",
        },
        {
            "zh_title": "陈茂波：北部都会区将提升居住与公共空间标准",
            "en_title": "Paul Chan says Northern Metropolis will improve liveability",
            "published": "16:51 2026年7月26日",
            "zh_summary": "财政司司长周日撰文指北都会将优化公营及私楼面积配置，人均公共空间标准拟较全市高约三成。",
            "en_summary": "Financial Secretary Paul Chan said the Northern Metropolis plan will raise housing and open-space standards.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3361890/northern-metropolis-will-make-hong-kong-more-liveable-paul-chan-says",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "牛津大学启动邦巴古约埃博拉疫苗首次人体试验",
            "en_title": "Oxford begins first human trial of Bundibugyo Ebola vaccine",
            "published": "00:00 2026年7月24日",
            "zh_summary": "牛津疫苗团队为首名志愿者接种ChAdOx1 BDBV候选疫苗，印度血清研究所已备货62万剂。",
            "en_summary": "Oxford vaccinated the first volunteer in a trial of a ChAdOx1 vaccine against Bundibugyo Ebola.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c8jn007gmpzo",
        },
        {
            "zh_title": "波尔多野火威胁酿酒业重镇，火场距城区约15公里",
            "en_title": "Reuters: Wildfires advance toward Bordeaux wine country",
            "published": "21:37 2026年7月26日",
            "zh_summary": "法国西南部火势向波尔多市郊推进，市长称火点距进城主要路口约15公里，西班牙多地同步救灾。",
            "en_summary": "Blazes neared Bordeaux as about 220,000 people were evacuated in France and tens of thousands in Spain.",
            "source_zh": "路透社（经NBC）", "source_en": "Reuters (via NBC News)",
            "url": "https://www.nbcnews.com/world/europe/wildfires-threaten-bordeaux-france-spain-battle-blazes-rcna589283",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c41e3a", "Xinhua": "#c41e3a",
    "财新": "#b8860b", "Caixin": "#b8860b", "Caixin Global": "#b8860b",
    "美联社": "#d71920", "AP": "#d71920",
    "英国广播公司": "#bb1919", "BBC": "#bb1919",
    "路透社": "#ff8000", "Reuters": "#ff8000",
    "南华早报": "#ffcc00", "SCMP": "#ffcc00",
    "香港电台": "#0066cc", "RTHK": "#0066cc",
    "半岛电视台": "#fa9000", "Al Jazeera": "#fa9000",
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_html() -> str:
    n = sum(len(cat_items) for _, cat_items in CATEGORIES)
    body_parts = []
    num = 0
    for cat_name, cat_items in CATEGORIES:
        body_parts.append(
            f'<h2 style="margin:28px 0 12px;padding:10px 12px;background:#f0f3f7;border-left:4px solid #1a73e8;font-size:17px;color:#1a1a1a;">{esc(cat_name)}</h2>'
        )
        for it in cat_items:
            num += 1
            label = f"{num:02d}"
            src = it["source_zh"]
            color = SOURCE_COLORS.get(src, "#5f6368")
            body_parts.append(
                f'<motionless></motionless>'
                f'<div style="margin:0 0 20px;padding:0 0 16px;border-bottom:1px solid #e8eaed;">'
                f'<motionless></motionless>'
                f'<div style="font-size:11px;color:#1a73e8;font-weight:700;margin-bottom:4px;">{label}</div>'
                f'<a href="{esc(it["url"])}" style="font-size:16px;font-weight:700;color:#1a1a1a;text-decoration:none;line-height:1.4;">{esc(it["zh_title"])}</a>'
                f'<div style="margin:6px 0 4px;font-size:14px;color:#5f6368;font-style:italic;line-height:1.4;">{esc(it["en_title"])}</div>'
                f'<div style="font-size:12px;color:#80868b;margin:0 0 8px;">发布时间 Published: {esc(it["published"])}</div>'
                f'<div style="font-size:14px;color:#3c4043;line-height:1.55;margin-bottom:6px;">{esc(it["zh_summary"])}</div>'
                f'<div style="font-size:13px;color:#5f6368;line-height:1.5;margin-bottom:10px;">{esc(it["en_summary"])}</motionless></div>'
                f'<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:8px;">{esc(src)} / {esc(it["source_en"])}</span>'
                f'<a href="{esc(it["url"])}" style="font-size:13px;color:#1a73e8;text-decoration:none;">查看全文 Read more →</a>'
                f'</div>'
            )
    body_html = "".join(p.replace("<motionless></motionless>", "") for p in body_parts).replace("</motionless>", "")

    intro_zh = "汇总昨夜至今要闻，涵盖台风灾后恢复、台海政局、中东局势缓和与欧陆野火等。"
    intro_en = "Overnight and early headlines on typhoon recovery, Taiwan politics, Middle East pauses, and European wildfires."

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>每日热点早报</title></head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef1f5;padding:24px 12px;"><tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);padding:28px 24px;color:#fff;">
<div style="font-size:22px;font-weight:700;letter-spacing:.5px;">每日热点早报</div>
<div style="font-size:14px;margin-top:6px;opacity:.92;">Morning News Briefing · {DATE_LABEL} · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;font-size:14px;color:#3c4043;line-height:1.6;">
<div>{esc(intro_zh)}</div>
<div style="margin-top:6px;font-style:italic;color:#5f6368;">{esc(intro_en)}</div>
</td></tr>
<tr><td style="padding:8px 24px 28px;">
{body_html}
</td></tr>
<tr><td style="background:#f8f9fa;padding:20px 24px;font-size:11px;color:#80868b;line-height:1.6;border-top:1px solid #e8eaed;">
<div>本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归原媒体所有。</div>
<div style="margin-top:8px;">This digest compiles publicly reported news for informational purposes only and is not investment or legal advice. Rights belong to original publishers.</div>
</td></tr>
</table></td></tr></table>
</body></html>"""
    return html


def main():
    html = render_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {SUBJECT_DATE}",
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out}, items={sum(len(c[1]) for c in CATEGORIES)}, chars={len(html)}")


if __name__ == "__main__":
    main()
