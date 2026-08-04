#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-04."""
import json
import os

BRIEFING_EDITION = "晚报"
LOCAL_TIME = "2026-08-04 17:30 Asia/Shanghai (UTC+8)"
DATE_LABEL = "2026年8月4日"
SUBJECT = "每日热点晚报 Evening Briefing - 2026-08-04"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "cn_title": "中央向陕西调配6.5万件救灾物资支援防汛",
            "en_title": "China dispatches 65,000 disaster relief items to flood-hit Shaanxi",
            "published": "09:52 2026年8月4日",
            "cn_summary": "应急管理部称，帐篷、折叠床等物资将支援转移安置与救灾工作。",
            "en_summary": "Tents, beds and kits will support evacuation and relief as heavy rains lash the northwestern province.",
            "source_cn": "中国日报 China Daily",
            "source_en": "China Daily",
            "url": "https://www.chinadaily.com.cn/a/202608/04/WS6a7145fca310986e2b468d9d.html",
        },
        {
            "cn_title": "中央气象台续发暴雨黄警与强对流蓝警",
            "en_title": "China renews yellow rainstorm and blue severe convection alerts",
            "published": "13:40 2026年8月4日",
            "cn_summary": "黑龙江西南部至广东等多地将现强降雨，局地或现雷暴大风冰雹。",
            "en_summary": "Heavy rain is forecast across multiple provinces, with thunderstorms, gales or hail in some areas.",
            "source_cn": "中国日报 China Daily",
            "source_en": "China Daily",
            "url": "https://www.chinadaily.com.cn/a/202608/04/WS6a717b4ca310986e2b468e83.html",
        },
        {
            "cn_title": "竹纤维复合材料机翼无人机完成首飞",
            "en_title": "Bamboo-composite wing drone completes maiden flight in China",
            "published": "13:01 2026年8月4日",
            "cn_summary": "中方企业试飞的轻型无人机结构成本降约两成，续航显著提升。",
            "en_summary": "A Chinese firm's lightweight drone cut structural costs by about 20% and improved flight endurance.",
            "source_cn": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "https://english.news.cn/20260804/3a039882ba884fa2bcfedd1c2cf6705b/c.html",
        },
        {
            "cn_title": "华龙一号核电站在广东太平岭全面投产",
            "en_title": "Hualong One unit starts commercial operation at Taipingling plant",
            "published": "23:48 2026年8月3日",
            "cn_summary": "二期机组投运后，一期两台机组年发电预计超180亿千瓦时。",
            "en_summary": "The new unit completes the first-phase project, with annual output expected above 18 billion kWh.",
            "source_cn": "新华社 Xinhua",
            "source_en": "Xinhua",
            "url": "https://english.news.cn/20260803/c3a752dbdf6e4c59b1014e04f1f01175/c.html",
        },
        {
            "cn_title": "证监会支持在港上市企业赴内地发债融资",
            "en_title": "CSRC backs Hong Kong-listed firms issuing shares and bonds on mainland",
            "published": "18:12 2026年8月3日",
            "cn_summary": "吴清在香港离岸国债期货挂牌仪式上称，将推动两地跨境融资双向便利。",
            "en_summary": "Chairman Wu Qing pledged support for two-way cross-border financing during a Hong Kong listing event.",
            "source_cn": "财新 Caixin Global",
            "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-03/china-backs-hong-kong-firms-for-mainland-listings-102470886.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "cn_title": "白宫今日召集OpenAI等讨论AI网络安全测试框架",
            "en_title": "White House hosts OpenAI, Google and others on AI safety testing",
            "published": "05:06 2026年8月4日",
            "cn_summary": "特朗普政府将介绍自愿性前沿模型网络安全评估框架，企业可自愿参与。",
            "en_summary": "The Trump administration will discuss a voluntary framework for cybersecurity tests of frontier AI models.",
            "source_cn": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/world/openai-anthropic-google-to-join-white-house-ai-safety-meeting",
        },
        {
            "cn_title": "苹果因涉儿童性虐待内容短暂下架Telegram",
            "en_title": "Apple briefly removes Telegram from App Store over abusive content",
            "published": "11:27 2026年8月4日",
            "cn_summary": "苹果称开发者已删除违规内容并封禁用户，同日恢复应用上架。",
            "en_summary": "Apple said Telegram removed violating content and banned the user before the app was restored same day.",
            "source_cn": "彭博 Bloomberg",
            "source_en": "Bloomberg",
            "url": "https://www.bloomberg.com/news/articles/2026-08-04/apple-briefly-takes-telegram-off-app-store-over-abusive-content",
        },
        {
            "cn_title": "Meta、Anthropic等受邀赴白宫谈AI安全测试",
            "en_title": "Meta, Anthropic, OpenAI and Google invited to White House AI talks",
            "published": "00:00 2026年8月4日",
            "cn_summary": "美方敲定自愿网络安全测试细节，此前两家公司的模型在测试中曾侵入其他系统。",
            "en_summary": "Washington finalized voluntary cybersecurity test details after recent model breaches during testing.",
            "source_cn": "日本时报 The Japan Times",
            "source_en": "The Japan Times",
            "url": "https://www.japantimes.co.jp/business/2026/08/04/tech/meta-anthropic-google-openai-safety/",
        },
        {
            "cn_title": "BBC调查：伊朗黑客或袭击美国七州供水系统",
            "en_title": "BBC probes possible Iranian link to US water system cyberattacks",
            "published": "12:30 2026年8月4日",
            "cn_summary": "明尼苏达逾30套供水系统遭协同攻击，FBI称部分活动已影响供水运行。",
            "en_summary": "Over 30 Minnesota water systems were hit; the FBI said some activity degraded water operations.",
            "source_cn": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c934dq95zpgo",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "cn_title": "亚马逊市值盘中突破3万亿美元",
            "en_title": "Amazon market value tops $3 trillion after earnings rally",
            "published": "00:00 2026年8月4日",
            "cn_summary": "股价周一涨4.6%，成为史上第五家触及3万亿美元市值的公司。",
            "en_summary": "Shares rose 4.6% on Monday, making Amazon the fifth firm ever to reach a $3 trillion valuation.",
            "source_cn": "美联社 AP",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-dollar-yen-trump-oil-d19a8f9a77b6fceca41da3e4b6bf17aa",
        },
        {
            "cn_title": "全球股市周二跟涨，亚股多数走高",
            "en_title": "Global shares mostly higher after Wall Street rally",
            "published": "00:00 2026年8月4日",
            "cn_summary": "日经涨0.3%，韩股涨1.6%，投资者仍评估美日联合干预日元影响。",
            "en_summary": "Nikkei rose 0.3% and Korea's Kospi gained 1.6% as investors weighed joint US-Japan yen intervention.",
            "source_cn": "美联社 AP",
            "source_en": "AP",
            "url": "https://apnews.com/article/stocks-markets-dollar-yen-trump-iran-war-fbbe6128d618509e33d45a493c2615b1",
        },
        {
            "cn_title": "美伊谈判信号矛盾，国际油价周二反弹",
            "en_title": "Oil rebounds as US and Iran give conflicting signals on talks",
            "published": "00:00 2026年8月4日",
            "cn_summary": "特朗普称谈判进行中，德黑兰否认；布油亚洲早盘涨逾1%。",
            "en_summary": "Trump said talks were underway while Tehran denied them; Brent crude rose over 1% in early Asia trade.",
            "source_cn": "半岛电视台 Al Jazeera",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/economy/2026/8/4/us-stocks-near-record-high-oil-falls-as-trump-claims-iran-talks-underway",
        },
        {
            "cn_title": "25州起诉特朗普政府新一轮强制劳动关税",
            "en_title": "25 US states sue to block Trump tariffs on forced labour claims",
            "published": "10:00 2026年8月4日",
            "cn_summary": "新关税7月生效，税率10%至12.5%，覆盖英国、中国及欧盟等贸易伙伴。",
            "en_summary": "New tariffs of 10% to 12.5% took effect in July, covering partners including the UK, China and the EU.",
            "source_cn": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cy4kp8jd0ppo",
        },
    ]),
    ("社会 Society", [
        {
            "cn_title": "首尔全境首次发布严重高温预警",
            "en_title": "Seoul issues first-ever serious heat wave warning citywide",
            "published": "11:04 2026年8月4日",
            "cn_summary": "李在明称应视酷暑为国家灾难，全国至少16人因高温死亡。",
            "en_summary": "President Lee urged treating the heat wave as a national disaster; at least 16 heat-related deaths were recorded.",
            "source_cn": "联合通讯社 Yonhap",
            "source_en": "Yonhap",
            "url": "https://en.yna.co.kr/view/AEN20260804004051315",
        },
        {
            "cn_title": "法国野火现400枚二战炮弹，百余爆炸声响彻村庄",
            "en_title": "French wildfires uncover 400 WWII shells in Gironde village",
            "published": "12:30 2026年8月4日",
            "cn_summary": "勒波尔日大火烧毁180余栋房屋，排爆后多数居民已返家。",
            "en_summary": "About 180 homes burned in Le Porge; demining allowed most residents to return after the Gironde blaze.",
            "source_cn": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cgmkxjrrwdvo",
        },
        {
            "cn_title": "古巴电网修复中再崩溃，全国第六次大停电",
            "en_title": "Cuba's power grid collapses again during restoration efforts",
            "published": "10:27 2026年8月4日",
            "cn_summary": "周日深夜全国停电后，周一恶劣天气再度冲击已恢复的发电机组。",
            "en_summary": "Bad weather disrupted generators already back online after a nationwide blackout late Sunday.",
            "source_cn": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/world/cubas-power-grid-collapses-again-during-restoration-efforts-after-nationwide-blackout",
        },
        {
            "cn_title": "孟加拉内阁批准强制失踪法案，致死可判死刑",
            "en_title": "Bangladesh cabinet approves enforced disappearance bill with death penalty",
            "published": "15:10 2026年8月3日",
            "cn_summary": "受害者死亡或五年未寻获，最高可处死刑或终身监禁并罚款1亿塔卡。",
            "en_summary": "Death or life imprisonment may apply if victims die or remain missing for five years, with heavy fines.",
            "source_cn": "普罗托姆阿罗 Prothom Alo",
            "source_en": "Prothom Alo",
            "url": "https://en.prothomalo.com/bangladesh/government/6qg1b0zfvj",
        },
    ]),
    ("国际 World", [
        {
            "cn_title": "和平委员会称哈马斯缴械完成后以色列才撤军",
            "en_title": "Board of Peace says Gaza withdrawal only after Hamas disarms",
            "published": "15:20 2026年8月4日",
            "cn_summary": "美方小组与内塔尼亚胡会晤，澄清撤军须待武器与地道全部销毁。",
            "en_summary": "The US-led board met Netanyahu, saying withdrawal waits until weapons and tunnels are decommissioned.",
            "source_cn": "南华早报 SCMP",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/world/middle-east/article/3362903/trumps-board-peace-conditions-israels-gaza-withdrawal-hamas-disarmament",
        },
        {
            "cn_title": "美伊就谈判状态各执一词，霍尔木兹货船遭袭",
            "en_title": "US-Iran talks disputed as cargo ship hit near Strait of Hormuz",
            "published": "08:42 2026年8月4日",
            "cn_summary": "特朗普称谈判进行中，伊朗否认；阿曼海域货船遭未知弹丸击中。",
            "en_summary": "Trump claimed talks were underway while Iran denied them; a cargo vessel was hit off Oman.",
            "source_cn": "日经亚洲 Nikkei Asia",
            "source_en": "Nikkei Asia",
            "url": "https://asia.nikkei.com/spotlight/iran-tensions/trump-says-talks-with-iran-under-way-but-tehran-denies-any-planned",
        },
        {
            "cn_title": "乌克兰无人机夜袭莫斯科近郊仓库致5死",
            "en_title": "Ukrainian drone strike on Moscow region warehouse kills five",
            "published": "17:05 2026年8月4日",
            "cn_summary": "州长称切霍夫工业点起火，乌媒指目标或与Wildberries仓库相关。",
            "en_summary": "A governor said a Chekhov industrial site burned; Ukrainian media linked it to a Wildberries warehouse.",
            "source_cn": "英国广播公司 BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c151pkww79zo",
        },
        {
            "cn_title": "缅甸领导人敏昂莱将首访泰国讨论边境议题",
            "en_title": "Myanmar's Min Aung Hlaing set for first Thailand visit as civilian leader",
            "published": "11:15 2026年8月4日",
            "cn_summary": "8月6日将与泰总理会谈诈骗、毒品、雾霾及劳务合作等跨境问题。",
            "en_summary": "He will meet Thailand's PM on Aug 6 to discuss scams, drugs, haze and labour cooperation.",
            "source_cn": "海峡时报 The Straits Times",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/asia/se-asia/myanmar-ex-junta-chief-min-aung-hlaing-set-for-first-thailand-visit-as-civilian-leader",
        },
        {
            "cn_title": "霍尔木兹附近货船遭未知弹丸击中起火",
            "en_title": "Cargo ship hit by unknown projectile off Oman near Hormuz",
            "published": "06:00 2026年8月4日",
            "cn_summary": "UKMTO称船在阿曼哈萨卜东北约37公里处受损，当局正调查。",
            "en_summary": "UKMTO said the vessel was struck northeast of Al Khasab; authorities are investigating the incident.",
            "source_cn": "美联社 AP",
            "source_en": "AP",
            "url": "https://apnews.com/article/iran-us-hormuz-mideast-gaza-israel-palestinians-ff5f13230ab92b5ae3022f45b2585444",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "cn_title": "屯门一周三次爆水管，逾7000居民受影响",
            "en_title": "Tuen Mun sees third water pipe burst in a week, 7,000 affected",
            "published": "12:46 2026年8月4日",
            "cn_summary": "水务署完成抢修后周二上午起逐步恢复四座屋苑供水。",
            "en_summary": "The Water Supplies Department began restoring supply to four estates after emergency repairs Tuesday.",
            "source_cn": "南华早报 SCMP",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362877/significant-distress-calls-grow-faster-water-pipe-replacement-after-repeated-bursts",
        },
        {
            "cn_title": "酒吧命案主嫌称羁留环境恶劣，要求转往监狱",
            "en_title": "Murder suspect complains of filthy police cell, asks to be jailed",
            "published": "15:41 2026年8月4日",
            "cn_summary": "曾伟清周二到九龙城法院应讯，称羁留室潮湿肮脏待认人程序。",
            "en_summary": "Tsang Wai-ching appeared in court Tuesday, complaining about custody conditions before identification parades.",
            "source_cn": "南华早报 SCMP",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362910/damp-and-filthy-murder-suspect-says-basic-necessities-denied-custody",
        },
        {
            "cn_title": "65岁惯犯巴士上非礼女生被判囚4个月",
            "en_title": "Repeat sex offender, 65, jailed four months for bus assault",
            "published": "12:26 2026年8月4日",
            "cn_summary": "被告6月在旺角双层巴士上层触摸17岁女生胸部，视频在网上广泛流传。",
            "en_summary": "He touched a 17-year-old student on a Mong Kok bus in June in a video widely shared online.",
            "source_cn": "南华早报 SCMP",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362875/4-months-jail-repeat-sex-offender-65-who-groped-form-3-student-bus",
        },
        {
            "cn_title": "李嘉诚基金会与迪士尼赠2.4万张佣工电影票",
            "en_title": "Li Ka Shing Foundation and Disney offer 24,000 helper movie tickets",
            "published": "14:27 2026年8月4日",
            "cn_summary": "《玩具总动员5》将于8月四个周日于六家百老汇影院放映，周三晚开放登记。",
            "en_summary": "Toy Story 5 screenings at six Broadway cinemas on four Sundays in August; registration opens Wednesday.",
            "source_cn": "南华早报 SCMP",
            "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/article/3362892/li-ka-shing-foundation-disney-offer-24000-helpers-free-tickets-toy-story-5",
        },
    ]),
    ("其他 Other", [
        {
            "cn_title": "巴拿马民众抗议运河水库计划，约2000人将搬迁",
            "en_title": "Panamanians protest canal reservoir plan affecting 2,000 residents",
            "published": "10:45 2026年8月4日",
            "cn_summary": "约300人在最高法院前示威，反对在Indio河建库并迁移社区墓地。",
            "en_summary": "About 300 people protested at the Supreme Court against a reservoir that would resettle communities.",
            "source_cn": "法新社 AFP",
            "source_en": "AFP",
            "url": "https://www.bssnews.net/international/411527",
        },
        {
            "cn_title": "斯波坎野火疑纵火者被捕，6.7万人疏散",
            "en_title": "Suspect arrested in Spokane wildfire as 67,000 evacuate",
            "published": "00:00 2026年8月4日",
            "cn_summary": "37岁男子涉嫌点燃Old Trails大火，三起火灾已毁数百建筑。",
            "en_summary": "A 37-year-old man was arrested over the Old Trails Fire; three blazes destroyed hundreds of buildings.",
            "source_cn": "半岛电视台 Al Jazeera",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/4/us-arrests-suspect-over-spokane-wildfire-as-tens-of-thousands-flee-blaze",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "中国日报": "#e67e22", "China Daily": "#e67e22",
    "财新": "#8e44ad", "Caixin": "#8e44ad",
    "南华早报": "#2980b9", "SCMP": "#2980b9",
    "英国广播公司": "#27ae60", "BBC": "#27ae60",
    "美联社": "#d35400", "AP": "#d35400",
    "彭博": "#2c3e50", "Bloomberg": "#2c3e50",
    "海峡时报": "#16a085", "Straits Times": "#16a085",
    "日本时报": "#7f8c8d", "Japan Times": "#7f8c8d",
    "半岛电视台": "#1abc9c", "Al Jazeera": "#1abc9c",
    "联合通讯社": "#3498db", "Yonhap": "#3498db",
    "法新社": "#9b59b6", "AFP": "#9b59b6",
    "日经": "#e74c3c", "Nikkei": "#e74c3c",
    "普罗托姆": "#6c5ce7", "Prothom": "#6c5ce7",
}


def source_color(source_cn):
    for key, color in SOURCE_COLORS.items():
        if key in source_cn:
            return color
    return "#555555"


def build_html():
    items = []
    for cat_name, cat_items in CATEGORIES:
        for item in cat_items:
            items.append((cat_name, item))
    total = len(items)

    parts = [
        '<!DOCTYPE html><html><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        f'<title>每日热点{BRIEFING_EDITION} {DATE_LABEL}</title></head>',
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,\'Helvetica Neue\',Arial,sans-serif;">',
        '<div style="max-width:600px;margin:0 auto;padding:16px 12px;">',
        '<div style="background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">',
        f'<div style="background:linear-gradient(135deg,#1a237e,#283593);color:#fff;padding:24px 20px;text-align:center;">',
        f'<div style="font-size:22px;font-weight:700;margin-bottom:4px;">每日热点{BRIEFING_EDITION}</div>',
        f'<div style="font-size:14px;opacity:.9;">Evening News Briefing · {DATE_LABEL} · 共 {total} 条</div>',
        '</div>',
        '<div style="padding:16px 20px;background:#f8f9fa;border-bottom:1px solid #e9ecef;">',
        '<p style="margin:0 0 6px;font-size:14px;color:#333;">汇总今日全日要闻，涵盖政策、市场与社会热点。</p>',
        '<p style="margin:0;font-size:13px;color:#666;font-style:italic;">Today\'s main stories across policy, markets and society.</p>',
        '</div>',
    ]

    global_idx = 0
    for cat_name, cat_items in CATEGORIES:
        parts.append(
            f'<div style="padding:12px 20px 4px;">'
            f'<h2 style="font-size:15px;color:#1a237e;margin:0;padding:8px 12px;background:#f0f4f8;border-left:4px solid #1565c0;border-radius:0 4px 4px 0;">{cat_name}</h2></div>'
        )
        for item in cat_items:
            global_idx += 1
            num = f"{global_idx:02d}"
            color = source_color(item["source_cn"])
            parts.append(
                f'<div style="padding:14px 20px;border-bottom:1px solid #eee;">'
                f'<div style="font-size:11px;color:#999;margin-bottom:4px;">{num}</div>'
                f'<a href="{item["url"]}" style="font-size:16px;font-weight:600;color:#1565c0;text-decoration:none;line-height:1.4;">{item["cn_title"]}</a>'
                f'<div style="font-size:14px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;">{item["en_title"]}</div>'
                f'<div style="font-size:11px;color:#999;margin-top:6px;">发布时间 Published: {item["published"]}</div>'
                f'<p style="font-size:14px;color:#333;margin:8px 0 4px;line-height:1.5;">{item["cn_summary"]}</p>'
                f'<p style="font-size:13px;color:#666;margin:0 0 10px;line-height:1.5;font-style:italic;">{item["en_summary"]}</p>'
                f'<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:6px;">{item["source_cn"]}</span>'
                f'<a href="{item["url"]}" style="font-size:12px;color:#1565c0;text-decoration:none;">查看全文 Read more →</a>'
                '</div>'
            )

    parts.extend([
        '<div style="padding:20px;background:#f8f9fa;font-size:11px;color:#888;line-height:1.6;">',
        '<p style="margin:0 0 6px;">本简报自动汇编公开报道，内容仅供参考，不构成投资或行动建议。版权归原媒体所有。</p>',
        '<p style="margin:0;font-style:italic;">This briefing is compiled from public reports for informational purposes only. Not investment or action advice. Content belongs to original publishers.</p>',
        '</div></div></div></body></html>',
    ])
    return "".join(parts), total


def main():
    html, total = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"Total items: {total}")
    print(f"HTML chars: {len(html)}")
    print(f"Written: {out}")


if __name__ == "__main__":
    main()
