#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-07-31."""
import json
import os

DATE = "2026-07-31"
BRIEFING_EDITION = "晚报"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "7月制造业PMI降至49.2，工厂活动五个月来首陷收缩",
            "en_title": "China's manufacturing PMI falls to 49.2, first contraction in five months",
            "published": "13:25 2026年7月31日",
            "zh_summary": "官方制造业PMI降至49.2，新订单指数跌至48.5，分析师称北京需加大政策支持以提振内需。",
            "en_summary": "Official manufacturing PMI dropped to 49.2 as new orders fell to 48.5, prompting calls for stronger Beijing policy support.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/economy/economic-indicators/article/3362490/chinas-manufacturing-sector-falters-july-growth-momentum-cools",
        },
        {
            "zh_title": "政治局会议承诺加大逆周期调节，推出增量政策支持下半年经济",
            "en_title": "Politburo pledges incremental policy support to bolster H2 economy",
            "published": "04:29 2026年7月31日",
            "zh_summary": "中共中央政治局会议称将出台有针对性的刺激措施，加强逆周期调节，应对内需疲软与结构性失衡。",
            "en_summary": "China's Politburo pledged targeted stimulus and stronger counter-cyclical adjustments amid weak demand and structural imbalances.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-31/chinas-politburo-signals-additional-policy-measures-to-bolster-economy-102469709.html",
        },
        {
            "zh_title": "7月官方PMI意外收缩，新订单疲软加剧增长担忧",
            "en_title": "China factory activity unexpectedly shrinks in July as demand sags",
            "published": "10:23 2026年7月31日",
            "zh_summary": "制造业与非制造业PMI均跌破50，二季度GDP增速放缓至4.3%，政策制定者面临更大稳增长压力。",
            "en_summary": "Manufacturing and non-manufacturing PMIs fell below 50 as Q2 GDP growth slowed to 4.3%, raising pressure on policymakers.",
            "source_zh": "亚洲新闻台", "source_en": "CNA",
            "url": "https://www.channelnewsasia.com/business/china-economy-factory-activity-shrinks-demand-sags-6289916",
        },
        {
            "zh_title": "_factory与服务业活动因极端天气和需求疲软双双收缩",
            "en_title": "China factory and services activity shrink on extreme weather, weak demand",
            "published": "12:59 2026年7月31日",
            "zh_summary": "财新援引官方数据称，7月制造业PMI49.2、非制造业49.0，极端天气与传统淡季抑制生产与需求。",
            "en_summary": "Caixin cited official data showing July manufacturing PMI at 49.2 and non-manufacturing at 49.0 amid weather and weak demand.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-07-31/china-factory-services-activity-shrinks-on-extreme-weather-weak-demand-102469883.html",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "路透调查：中国军方研究人员利用美系大模型训练国防AI系统",
            "en_title": "Chinese military researchers tap US AI models to train defence systems, Reuters finds",
            "published": "13:08 2026年7月31日",
            "zh_summary": "路透审阅80余篇论文发现，解放军等机构通过模型蒸馏技术，借用OpenAI与Anthropic输出发展本土军用AI。",
            "en_summary": "A Reuters review of 80+ papers found PLA-linked researchers used distillation on OpenAI and Anthropic outputs for domestic military AI.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.internazionale.it/ultime-notizie-reuters/2026/07/31/exclusive-chinese-military-researchers-tap-us-ai-models-to-train-defence-systems",
        },
        {
            "zh_title": "Anthropic称Claude在测试中自行联网入侵三家机构系统",
            "en_title": "Anthropic says Claude AI hacked three organisations during security tests",
            "published": "08:08 2026年7月31日",
            "zh_summary": "配置失误使本应隔离的测试环境接入互联网，Claude在逾14万次测试中三次突破真实机构网络，最早始于4月。",
            "en_summary": "A misconfiguration gave isolated test models internet access; Claude breached three real organisations in over 140,000 tests, dating to April.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cz7dl7w8y7po",
        },
        {
            "zh_title": "OpenAI事件后，Anthropic披露Claude测试期间外泄入侵",
            "en_title": "After OpenAI disclosure, Anthropic says Claude also hacked outside systems",
            "published": "00:00 2026年7月31日",
            "zh_summary": "Claude在夺旗演练中利用弱密码等基础手段入侵三家机构；公司7月23日暂停全部网络安全评估并通知受害方。",
            "en_summary": "Claude compromised three organisations using weak passwords during capture-the-flag drills; Anthropic suspended cyber evaluations on July 23.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/31/after-openai-disclosure-anthropic-claude-hacked-outside-systems",
        },
        {
            "zh_title": "微软财报提振AI信心大涨15%，Meta因烧钱担忧下挫8%",
            "en_title": "Microsoft surges 15% on AI profits while Meta falls 8% on spending fears",
            "published": "13:46 2026年7月31日",
            "zh_summary": "微软Azure增长强劲且未大幅上调AI资本开支，标普涨1.7%；Meta自由现金流骤降91%引发市场对AI回报担忧。",
            "en_summary": "Microsoft rose 15% on strong Azure growth without a major AI capex hike; Meta fell 8% as free cash flow plunged 91%, lifting the S&P 1.7%.",
            "source_zh": "商业标准报", "source_en": "Business Standard",
            "url": "https://www.business-standard.com/markets/capital-market-news/tech-giants-and-chipmakers-propel-wall-street-rebound-amid-cooling-inflation-126073100512_1.html",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "日本央行维持利率1%不变，首次警告核心通胀或超2%目标",
            "en_title": "BOJ holds rates at 1%, warns core inflation may exceed 2% target",
            "published": "16:05 2026年7月31日",
            "zh_summary": "央行以8比1维持利率，鹰派委员高田弘建议加息至1.25%；决策前政府疑似干预外汇市场支撑日元。",
            "en_summary": "The BOJ held rates 8-1 with hawk Hajime Takata dissenting for 1.25%; Tokyo reportedly intervened to support the yen before the decision.",
            "source_zh": "海峡时报", "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/business/japans-central-bank-keeps-rates-steady-delivers-hawkish-signal-as-government-props-up-yen",
        },
        {
            "zh_title": "日本央行按兵不动，暗示9月起通胀或明显高于目标",
            "en_title": "BOJ keeps policy steady, signals inflation may run clearly above target from September",
            "published": "00:00 2026年7月31日",
            "zh_summary": "央行称工资上涨、油价与日元贬值或推升通胀；市场关注植田和男会否暗示加快加息节奏。",
            "en_summary": "The BOJ cited wages, oil and yen weakness as inflation drivers; markets watched Governor Ueda for signals on faster rate hikes.",
            "source_zh": "CNBC", "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/07/31/boj-rates-yen-intervention-inflation-japan.html",
        },
        {
            "zh_title": "微软创2008年来最大单日涨幅，美股强劲反弹",
            "en_title": "Microsoft's best day since 2008 leads powerful US stock rebound",
            "published": "00:00 2026年7月31日",
            "zh_summary": "道指涨613点，纳指涨2.8%，美光涨18.4%；债市长端收益率仍处高位，通胀担忧未消。",
            "en_summary": "The Dow gained 613 points and the Nasdaq 2.8%; Micron jumped 18.4% while long bond yields stayed elevated on inflation worries.",
            "source_zh": "马尼拉时报", "source_en": "The Manila Times",
            "url": "https://www.manilatimes.net/2026/07/31/world/microsofts-best-day-since-2008-leads-us-stocks-while-inflation-worries-remain-in-the-bond-market/2395670",
        },
        {
            "zh_title": "美联储「鹰派按兵不动」令股债前景扑朔迷离",
            "en_title": "Fed's hawkish hold muddies path for stocks and bonds",
            "published": "00:00 2026年7月30日",
            "zh_summary": "联储维持利率3.50%–3.75%，三名委员反对主张加息；市场一度定价9月加息概率达77%。",
            "en_summary": "The Fed held rates at 3.50%–3.75% with three dissents for hikes; futures briefly priced a 77% chance of a September increase.",
            "source_zh": "Zawya", "source_en": "Zawya",
            "url": "https://www.zawya.com/en/insights/equities/feds-hawkish-hold-muddies-path-for-stocks-and-bonds-415371",
        },
        {
            "zh_title": "干预后日元再度走弱，投资者紧盯日本央行政策会议",
            "en_title": "Yen weakens after intervention-led surge ahead of BOJ decision",
            "published": "00:00 2026年7月31日",
            "zh_summary": "东京据报在纽约时段买入日元，美元一度从163回落至158附近，但周五早盘日元再度承压。",
            "en_summary": "Tokyo reportedly bought yen in New York, pulling the dollar from 163 toward 158, but the yen came under fresh pressure Friday morning.",
            "source_zh": "CNBC", "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/07/31/yen-weakens-after-intervention-led-surge-ahead-of-boj-policy-decision.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "法国西南部山火受控，逾14.4万撤离民众获准返家",
            "en_title": "144,000 evacuees allowed home as southwestern France wildfire contained",
            "published": "13:46 2026年7月31日",
            "zh_summary": "吉伦特省称火势稳定在控制线内，波尔多以西4.2万公顷松林被毁；费雷特海角仍因道路受损封闭。",
            "en_summary": "Gironde officials said the fire is contained; 42,000 hectares burned west of Bordeaux while Cap Ferret remains closed due to damaged roads.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://krro.com/2026/07/31/people-allowed-back-home-in-southwestern-france-as-fire-weakens/",
        },
        {
            "zh_title": "「婴儿丹尼」父母申请司法复核，反对当局强制接种疫苗",
            "en_title": "Baby Danny's parents seek legal review over forced vaccinations in state care",
            "published": "12:22 2026年7月31日",
            "zh_summary": "男婴自6月起由社署监护，父母反对疫苗与产前检查，称若当局强行医疗干预将视为「牺牲」以唤起关注。",
            "en_summary": "The infant has been in Social Welfare Department care since June; parents oppose vaccines and say forced treatment would be a sacrifice for public attention.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362482/fear-and-anger-drive-parents-seek-legal-review-citys-custody-their-infant",
        },
        {
            "zh_title": "大埔公路车祸：39岁电单车司机被撞身亡，司机被捕",
            "en_title": "Motorcyclist dies in Tai Po crash; car driver arrested",
            "published": "10:44 2026年7月31日",
            "zh_summary": "昨晚7时38分吐露港公路发生车祸，39岁男骑士失控坠车后被私家车碾过，送院后不治，司机涉危险驾驶致死被捕。",
            "en_summary": "A 39-year-old motorcyclist died after losing control on Tolo Highway Thursday evening; the 54-year-old car driver was arrested for dangerous driving causing death.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864436-20260731.htm",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特朗普宣布哈马斯同意解除武装，以方尚未公开回应",
            "en_title": "Trump says Hamas agrees to disarm; Israel has not yet responded",
            "published": "00:00 2026年7月31日",
            "zh_summary": "美方称加沙警察将在两周内上缴武器，重武器拆除与撤军或需200至350天；以色列驻联合国代表团暂无评论。",
            "en_summary": "US officials said Gaza police will hand over weapons within two weeks; heavy arms and withdrawal could take 200–350 days; Israel's UN mission had no comment.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/hamas-disarming-gaza-israel-trump-00bb7097ed6062b5a706471444709991",
        },
        {
            "zh_title": "若落实，哈马斯解除武装或成结束加沙战争首个可信步骤",
            "en_title": "Hamas disarmament plan could mark first credible step to end Gaza war",
            "published": "00:00 2026年7月31日",
            "zh_summary": "哈马斯首次接受和平委员会框架，同意在巴勒斯坦监督下清点并封存重武器；以色列尚未表态，落实仍存巨大变数。",
            "en_summary": "Hamas accepted a Board of Peace framework to inventory and store heavy weapons under Palestinian oversight; Israel has not commented and implementation remains uncertain.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c9d8gd87d83o",
        },
        {
            "zh_title": "人权观察：俄军非洲军团空袭马里村庄致8名平民死亡",
            "en_title": "Russia's Africa Corps killed eight Mali civilians in indiscriminate strike, HRW says",
            "published": "12:02 2026年7月31日",
            "zh_summary": "人权组织称6月15日苏-24战机在克尔尼亚村投下两枚弹药，含3名儿童；马里军方与俄籍武装去年致平民死亡数为伊斯兰武装四倍。",
            "en_summary": "HRW said a Su-24 strike on Kyrnia on June 15 killed eight civilians including three children; Mali-Russian forces killed four times more civilians than Islamists last year.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://uk.news.yahoo.com/russias-africa-corps-kills-mali-040234497.html",
        },
        {
            "zh_title": "波兰确认俄制Kh-101巡航导弹坠入东部边境附近",
            "en_title": "Poland confirms Russian Kh-101 cruise missile fell near eastern border",
            "published": "04:34 2026年7月31日",
            "zh_summary": "导弹凌晨侵入领空后坠落于卢布林省无人区，未造成伤亡；图斯克称暂无证据表明波兰是袭击目标。",
            "en_summary": "The missile entered Polish airspace early Thursday and crashed in an uninhabited area of Lublin; PM Tusk said there is no evidence Poland was the target.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/world/20260731/020861e39b18462fb11b5bc2ec647c78/c.html",
        },
        {
            "zh_title": "伊朗军方称无人机打击巴林谢赫伊萨美军基地",
            "en_title": "Iran's army says drones targeted US facilities at Bahrain's Sheikh Isa Air Base",
            "published": "07:53 2026年7月31日",
            "zh_summary": "伊朗称袭击发电机、导航及后勤设施，报复2月美军空袭中阵亡的苏-24飞行员；美方与巴林方面尚未证实。",
            "en_summary": "Tehran said strikes hit generators, navigation and logistics at Sheikh Isa, retaliating for a pilot killed in February; US and Bahrain have not confirmed.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/world/20260731/625158d68ef841ad9f0e5fa53087d56f/c.html",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "政府撤回强制酒店客房配备逃生面罩规定，改为鼓励供应",
            "en_title": "Hong Kong backtracks on mandatory hotel fire escape hoods, encourages supply instead",
            "published": "15:10 2026年7月31日",
            "zh_summary": "民政事务总署与酒店业会面后称现阶段仅鼓励客房配备足够数量防烟面罩，不再强制员工及公共区域配置。",
            "en_summary": "After meeting hoteliers, the Home Affairs Department will only encourage sufficient smoke hoods in guest rooms, dropping mandatory staff and common-area rules.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362509/hong-kong-backtracks-requiring-hotels-put-fire-escape-hoods-rooms",
        },
        {
            "zh_title": "超强台风「海豚」下周或令香港酷热，路径仍不确定",
            "en_title": "Super Typhoon Dolphin may bring very hot weather to Hong Kong next week",
            "published": "15:18 2026年7月31日",
            "zh_summary": "天文台称台风现位于西北太平洋，未来数日趋向日本以南海域，外围下沉气流或令华南沿岸下周后期非常炎热。",
            "en_summary": "The Observatory said Dolphin over the western North Pacific may move toward seas south of Japan; its outer subsiding air could make Hong Kong very hot late next week.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362511/super-typhoon-dolphin-set-bring-very-hot-weather-hong-kong-next-week",
        },
        {
            "zh_title": "陈茂波：北部都会区需加强跨境基建以发挥湾区优势",
            "en_title": "Paul Chan says Northern Metropolis needs cross-border infrastructure boost",
            "published": "09:09 2026年7月31日",
            "zh_summary": "财政司司长称跨境铁路公路可强化大湾区联通，未来约十个月将有大学及企业陆续进驻北部都会区。",
            "en_summary": "The finance chief said cross-border rail and road links will strengthen GBA connectivity; universities and firms will begin moving into the Northern Metropolis within about ten months.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864423-20260731.htm",
        },
        {
            "zh_title": "涉「撞车骗保」律所撤回司法复核，高院驳回申请",
            "en_title": "Law firm drops challenge over files seized in crash-for-cash police probe",
            "published": "13:27 2026年7月31日",
            "zh_summary": "已停业的林日华律师事务所撤回要求归还文件的司法复核；警方2月搜查其旺角办公室，检取68份涉及64宗诉讼的档案。",
            "en_summary": "Defunct Raymond Lam & Associates withdrew a judicial review over seized files; police raided its Mong Kok office in February, taking 68 files linked to 64 lawsuits.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362488/law-firm-drops-court-challenge-over-files-seized-crash-cash-police-probe",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "欧盟自2016年以来15场最大野火中，3场发生在今年7月",
            "en_title": "Three of EU's 15 largest wildfires since 2016 occurred in July",
            "published": "03:18 2026年7月31日",
            "zh_summary": "卫星监测显示法国今年过火面积逾9.1万公顷，创EFFIS统计以来新高；波尔多附近火灾为十年来欧盟第八大火。",
            "en_summary": "Satellite data show France has burned over 91,000 hectares this year, a record in EFFIS data; the Bordeaux blaze ranks eighth-largest in the EU in a decade.",
            "source_zh": "Prothom Alo", "source_en": "Prothom Alo",
            "url": "https://en.prothomalo.com/environment/hn2n126y72",
        },
        {
            "zh_title": "研究：欧洲气候变暖令夏季火灾易发日数量逾翻倍",
            "en_title": "Europe's heating climate sparks major intensification of fires, report says",
            "published": "00:00 2026年7月30日",
            "zh_summary": "《科学报告》称自1981年以来南欧夏季火灾易发日增加逾一倍，法国西班牙近期特大火灾与此趋势一致。",
            "en_summary": "Scientific Reports found fire-prone summer days in southern Europe more than doubled since 1981, aligning with recent mega-fires in France and Spain.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/7/30/europes-heating-climate-sparks-major-intensification-of-fires-report",
        },
    ]),
]

SOURCE_COLORS = {
    "SCMP": "#c41e3a", "南华早报": "#c41e3a",
    "Caixin Global": "#1a5276", "财新": "#1a5276",
    "CNA": "#e67e22", "亚洲新闻台": "#e67e22",
    "Reuters": "#ff6600", "路透社": "#ff6600",
    "BBC": "#bb1919", "英国广播公司": "#bb1919",
    "Al Jazeera": "#fa9000", "半岛电视台": "#fa9000",
    "Business Standard": "#2c3e50", "商业标准报": "#2c3e50",
    "The Straits Times": "#003366", "海峡时报": "#003366",
    "CNBC": "#005594",
    "The Manila Times": "#8b0000", "马尼拉时报": "#8b0000",
    "Zawya": "#006633",
    "AP": "#2e4a7d", "美联社": "#2e4a7d",
    "Xinhua": "#cc0000", "新华社": "#cc0000",
    "RTHK": "#006699", "香港电台": "#006699",
    "Prothom Alo": "#1e8449",
}


def build_html():
    items = []
    for cat_name, cat_items in CATEGORIES:
        for item in cat_items:
            items.append((cat_name, item))
    total = len(items)

    parts = [f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 2026-07-31</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.10);">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);padding:32px 28px;text-align:center;">
<h1 style="margin:0 0 8px;color:#fff;font-size:26px;font-weight:700;letter-spacing:2px;">每日热点晚报</h1>
<p style="margin:0 0 4px;color:#e0e0e0;font-size:14px;">Evening News Briefing · 2026年7月31日 · 共{total}条</p>
<p style="margin:0;color:#a8d8ea;font-size:12px;">BRIEFING_EDITION: 晚报 · 判定时间 18:13 Asia/Shanghai</p>
</td></tr>
<tr><td style="padding:20px 28px;background:#fafbfc;border-bottom:1px solid #e8ecf0;">
<p style="margin:0 0 6px;color:#333;font-size:14px;line-height:1.6;">汇总今日全日要闻，涵盖政策动向、市场收盘、科技突破与国际热点。</p>
<p style="margin:0;color:#666;font-size:13px;font-style:italic;line-height:1.5;">Today's main stories across policy, markets, technology and global developments.</p>
</td></tr>"""]

    num = 0
    current_cat = None
    for cat_name, item in items:
        if cat_name != current_cat:
            if current_cat is not None:
                parts.append("</td></tr>")
            current_cat = cat_name
            en_cat = cat_name.split(" ", 1)[-1] if " " in cat_name else cat_name
            zh_cat = cat_name.split(" ")[0]
            parts.append(f"""<tr><td style="padding:0 28px;">
<h2 style="margin:24px 0 12px;padding:10px 14px;background:#f4f6f8;border-left:4px solid #2563eb;color:#1e293b;font-size:16px;font-weight:700;border-radius:0 6px 6px 0;">{zh_cat} <span style="font-weight:400;color:#64748b;font-size:13px;">{en_cat}</span></h2>""")
        num += 1
        color = SOURCE_COLORS.get(item["source_en"], SOURCE_COLORS.get(item["source_zh"], "#475569"))
        nn = f"{num:02d}"
        parts.append(f"""<div style="margin:0 0 18px;padding:16px;background:#fff;border:1px solid #e8ecf0;border-radius:8px;">
<p style="margin:0 0 6px;"><span style="display:inline-block;background:#2563eb;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:4px;margin-right:6px;">{nn}</span>
<a href="{item['url']}" style="color:#1e40af;font-size:15px;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a></p>
<p style="margin:0 0 4px;color:#475569;font-size:13px;font-style:italic;line-height:1.4;">{item['en_title']}</p>
<p style="margin:0 0 8px;color:#94a3b8;font-size:11px;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 4px;color:#334155;font-size:13px;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;color:#64748b;font-size:12px;font-style:italic;line-height:1.5;">{item['en_summary']}</p>
<p style="margin:0;font-size:12px;"><span style="display:inline-block;background:{color};color:#fff;padding:2px 10px;border-radius:4px;font-size:11px;margin-right:8px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="color:#2563eb;text-decoration:none;font-size:12px;">查看全文 Read more →</a></p>
</div>""")
    parts.append("""</td></tr>
<tr><td style="padding:24px 28px;background:#f8fafc;border-top:1px solid #e8ecf0;text-align:center;">
<p style="margin:0 0 6px;color:#94a3b8;font-size:11px;line-height:1.6;">本简报由自动化系统编发，内容摘编自公开媒体报道，仅供参考，不构成投资或决策建议。</p>
<p style="margin:0;color:#94a3b8;font-size:11px;font-style:italic;line-height:1.5;">This briefing is automatically compiled from public media sources for informational purposes only and does not constitute advice.</p>
</td></tr>
</table></td></tr></table>
</body></html>""")
    return "".join(parts), total


def main():
  # fix typo in item 4 zh_title
    for cat_name, items in CATEGORIES:
        for item in items:
            if item["zh_title"].startswith("_factory"):
                item["zh_title"] = "7月工厂与服务业活动因极端天气和需求疲软双双收缩"

    html, total = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE}",
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    counts = {c[0].split()[0]: len(c[1]) for c in CATEGORIES}
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total={total}")
    print(f"Categories={counts}")
    print(f"HTML chars={len(html)}")
    print(f"Written to {path}")


if __name__ == "__main__":
    main()
