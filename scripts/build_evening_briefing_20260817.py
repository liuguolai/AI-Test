#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-17."""
import json
import os

DATE = "2026-08-17"
EDITION_ZH = "晚报"
EDITION_EN = "Evening Briefing"
SUBJECT = f"每日热点晚报 Morning Briefing - {DATE}".replace("Morning", "Evening")
# fix subject
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE}"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "纪念江泽民同志诞辰100周年大会在京举行，习近平发表重要讲话",
            "en_title": "China holds centenary ceremony for Jiang Zemin as Xi delivers keynote speech",
            "published": "14:19 2026年8月17日",
            "zh_summary": "中共中央等17日上午在人民大会堂举行纪念大会，习近平高度评价江泽民历史贡献并号召继续前进。",
            "en_summary": "Beijing held a grand ceremony marking Jiang Zemin's 100th birthday as Xi Jinping praised his legacy and urged continued progress.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/politics/leaders/20260817/c09eaee334464122a24e6a6b67e756a3/c.html",
        },
        {
            "zh_title": "国家统计局：前7个月国民经济总体平稳、向新向优",
            "en_title": "NBS says China's economy stayed steady and improved in first seven months",
            "published": "15:45 2026年8月17日",
            "zh_summary": "统计局称1—7月生产供给平稳增长，就业物价总体稳定，外贸韧性持续，新动能不断壮大。",
            "en_summary": "Official data showed steady production, stable jobs and prices, resilient trade and growing new drivers in January-July.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.news.cn/20260817/aa6ef08e9eab48cba0774429cbfcfa81/c.html",
        },
        {
            "zh_title": "甘肃常务副省长程晓波主动投案，正接受审查调查",
            "en_title": "Gansu vice governor Cheng Xiaobo surrenders to anti-graft authorities",
            "published": "07:10 2026年8月17日",
            "zh_summary": "中央纪委国家监委通报，甘肃省委常委、常务副省长程晓波涉嫌严重违纪违法，已主动投案。",
            "en_summary": "China's top graft watchdog said Gansu executive vice governor Cheng Xiaobo is under investigation after turning himself in.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://china.caixin.com/2026-08-17/102474672.html",
        },
        {
            "zh_title": "我国在太原成功发射SEO卫星",
            "en_title": "China successfully launches SEO satellite from Taiyuan",
            "published": "11:26 2026年8月17日",
            "zh_summary": "长征二号丙运载火箭将SEO卫星送入预定轨道，这是长征系列火箭第664次飞行。",
            "en_summary": "A Long March 2C rocket placed the SEO satellite into orbit in the 664th launch of the Long March family.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.news.cn/20260817/ffd82a9806d84b85aa156385cb67be87/c.html",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "美拟要求伙伴在中美AI竞争中“选边站”",
            "en_title": "US to press partners to pick sides in AI race with China",
            "published": "12:32 2026年8月17日",
            "zh_summary": "路透称美国务院起草信函，警告35国若加入中方AI框架将被排除在美方联盟之外。",
            "en_summary": "Reuters says a draft US letter warns 35 countries they cannot join Beijing's AI bloc and remain in the US coalition.",
            "source_zh": "路透社 / 印度教徒报", "source_en": "Reuters / The Hindu",
            "url": "https://www.thehindu.com/sci-tech/technology/us-to-tell-partners-they-must-pick-sides-in-ai-race-with-china/article71354765.ece",
        },
        {
            "zh_title": "Meta儿童隐私案开庭，或重塑Instagram与Facebook",
            "en_title": "Meta child privacy trial could reshape Instagram and Facebook",
            "published": "12:30 2026年8月17日",
            "zh_summary": "美国30州起诉Meta违反儿童隐私法，寻求万亿美元赔偿并要求取消点赞数与无限滚动等功能。",
            "en_summary": "Thirty US states are suing Meta over child privacy laws, seeking huge damages and changes including ending likes and infinite scroll.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/clyqpx6xk69o",
        },
        {
            "zh_title": "阿里巴巴开源Qwen3.8系列，智谱发布GLM-5.3",
            "en_title": "Alibaba open-sources Qwen 3.8 series as Zhipu unveils GLM-5.3",
            "published": "08:39 2026年8月17日",
            "zh_summary": "财新称阿里开源新一代大模型，智谱强调编程与网络安全能力，世界机器人大会本周将在北京召开。",
            "en_summary": "Alibaba open-sourced new Qwen models while Zhipu released GLM-5.3 ahead of Beijing's World Robot Conference this week.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-17/102474692.html",
        },
        {
            "zh_title": "DeepSeek调价正式生效，峰值涨幅最高逾十倍",
            "en_title": "DeepSeek price hikes take effect with peak rates up over tenfold",
            "published": "09:58 2026年8月17日",
            "zh_summary": "财新称DeepSeek V4系列8月16日起实行峰谷计价，部分项目涨幅最高达1100%，闲时价格为高峰一半。",
            "en_summary": "Caixin reports DeepSeek's V4 API switched to peak/off-peak pricing on Aug 16, with some rates rising more than tenfold.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-17/102474718.html",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "中国7月工业产出放缓，零售销售不及预期",
            "en_title": "China's July industrial output slows as retail sales miss forecasts",
            "published": "15:13 2026年8月17日",
            "zh_summary": "路透称7月规上工业增加值同比增4.5%，社零增0.6%，均低于预期，极端天气与内需疲软施压经济。",
            "en_summary": "Reuters says July factory output rose 4.5% and retail sales 0.6%, both missing forecasts amid weak demand and weather shocks.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://wifc.com/2026/08/17/chinas-industrial-output-slows-in-july-retail-sales-miss-forecasts/",
        },
        {
            "zh_title": "法拉利首辆电动车Luce慈善拍卖创4000万美元纪录",
            "en_title": "Ferrari's first electric Luce sells for record $40m at charity auction",
            "published": "10:30 2026年8月17日",
            "zh_summary": "BBC称乔尼·艾维设计的Luce在加州拍卖，成交价约为零售价的35倍，收益捐予法拉利基金会教育项目。",
            "en_summary": "BBC says Jony Ive's Ferrari Luce fetched $40m at a California auction, with proceeds going to Ferrari Foundation education programs.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c77ggpgrp2do",
        },
        {
            "zh_title": "港股高开0.7%，科技股领涨",
            "en_title": "Hong Kong stocks open 0.7% higher led by tech shares",
            "published": "11:04 2026年8月17日",
            "zh_summary": "RTHK报道恒生指数开盘涨186点，科技指数升1.1%，京东、阿里、腾讯等权重股走强。",
            "en_summary": "RTHK says the Hang Seng rose 0.7% at the open with the tech index up 1.1% as JD.com, Alibaba and Tencent gained.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1866419-20260817.htm",
        },
        {
            "zh_title": "现货黄金价格突破4400美元/盎司",
            "en_title": "Gold spot price breaks above $4,400 per ounce",
            "published": "09:58 2026年8月17日",
            "zh_summary": "财新综合消息显示，国际金价升破4400美元关口，美元走弱与美联储政策预期变化推动避险买盘。",
            "en_summary": "Caixin's news roundup notes gold topped $4,400 an ounce as a weaker dollar and shifting Fed expectations boosted safe-haven demand.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-17/102474718.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "印尼弗洛勒斯地震灾民援助短缺，担忧饥饿",
            "en_title": "Indonesia quake survivors face aid shortages and hunger fears",
            "published": "13:11 2026年8月17日",
            "zh_summary": "RTHK援引报道，7.7级地震已致53死，逾1.28万人流离失所，多地道路中断、医疗设施受损。",
            "en_summary": "RTHK cites reports that a 7.7 quake killed 53 and displaced over 12,800 as aid struggles to reach cut-off Flores communities.",
            "source_zh": "香港电台 / 法新社", "source_en": "RTHK / AFP",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1866429-20260817.htm",
        },
        {
            "zh_title": "韩国巨济暴雨引发山体滑坡致1死",
            "en_title": "Record rains trigger landslide killing one in South Korea's Geoje",
            "published": "09:58 2026年8月17日",
            "zh_summary": "财新综合消息，庆尚南道巨济市遭遇创纪录暴雨，山体滑坡致1人死亡，当地多条道路中断。",
            "en_summary": "Caixin's news roundup says record rainfall in Geoje, South Korea, triggered a deadly landslide and disrupted local roads.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-17/102474718.html",
        },
        {
            "zh_title": "新加坡老人拍女童头遭推倒，警方调查",
            "en_title": "Singapore police probe assault on elderly man who patted child's head",
            "published": "15:30 2026年8月17日",
            "zh_summary": "BBC称73岁云吞面摊主轻拍女童头部后，疑为父亲男子将其推倒，事件视频周末在网络热传。",
            "en_summary": "BBC says police are investigating after a 73-year-old noodle vendor was thrown down for patting a girl's head at a food court.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cy077exnv8jo",
        },
        {
            "zh_title": "希腊萨拉米斯岛双火致2死，数百人撤离",
            "en_title": "Twin wildfires on Greek island of Salamina kill two, hundreds evacuated",
            "published": "00:00 2026年8月17日",
            "zh_summary": "RTHK援引法新社，萨拉米斯岛周日下午两起山火致2死，逾570人乘船撤离，欧洲多国周末遭遇极端野火。",
            "en_summary": "RTHK cites AFP saying twin fires on Salamina killed two and forced over 570 evacuations as Europe battled weekend wildfires.",
            "source_zh": "香港电台 / 法新社", "source_en": "RTHK / AFP",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1866391-20260817.htm",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特朗普宣布将大幅缩减美韩联合军演",
            "en_title": "Trump says US will substantially reduce joint drills with South Korea",
            "published": "09:58 2026年8月17日",
            "zh_summary": "财新援引美方表态，特朗普称对韩美联合军演不满并指示大幅缩减；韩国防部称演习仍按计划进行。",
            "en_summary": "Caixin cites Trump ordering scaled-back US-South Korea drills while Seoul's defense ministry says exercises proceed as planned.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-17/102474718.html",
        },
        {
            "zh_title": "库什纳与哈马斯会谈后抵达以色列",
            "en_title": "Kushner arrives in Israel after rare Hamas talks on Gaza peace plan",
            "published": "13:59 2026年8月17日",
            "zh_summary": "新华社援引美媒称库什纳在埃及与哈马斯领导人哈亚会谈90分钟，重点讨论解除武装与撤军安排。",
            "en_summary": "Xinhua cites US media saying Kushner held 90-minute talks with Hamas leader Hayya in Egypt on disarmament and withdrawal.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.news.cn/20260817/59b1850494294860afadf43e49c1603b/c.html",
        },
        {
            "zh_title": "乌导弹袭击俄别尔哥罗德州致6死",
            "en_title": "Ukrainian missile strike kills six in Russia's Belgorod region",
            "published": "00:00 2026年8月17日",
            "zh_summary": "半岛电视台称导弹击中科洛斯科沃村致6死4伤，含一名14岁伤者；俄乌双方周末互袭致两国19人死亡。",
            "en_summary": "Al Jazeera says a missile hit Koloskovo killing six and wounding four as weekend cross-border strikes left 19 dead on both sides.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/17/at-least-six-people-killed-in-ukrainian-missile-attack-on-russias-belgorod",
        },
        {
            "zh_title": "赞比亚逮捕11名反对派人士，涉叛乱阴谋",
            "en_title": "Zambia arrests 11 opposition figures over alleged insurrection plot",
            "published": "00:00 2026年8月17日",
            "zh_summary": "安纳多卢通讯社称警方凌晨在卢萨卡拘捕包括主要反对派候选人蒙杜比莱在内的11人，缴获军用武器。",
            "en_summary": "Anadolu Agency says police arrested 11 people including top opposition candidate Mundubile in Lusaka, seizing military weapons.",
            "source_zh": "安纳多卢通讯社", "source_en": "Anadolu Agency",
            "url": "https://www.aa.com.tr/en/africa/zambian-police-arrest-suspected-militia-members-persons-of-interest/4029044",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "港商纵火弑亲案判监五年四个月",
            "en_title": "Hong Kong merchant jailed over attempted murder of wife and daughters",
            "published": "12:30 2026年8月17日",
            "zh_summary": "SCMP称被告因欠债近90万港元，在屯门公屋以药物及烧炭企图杀害妻女三人，高院周一宣判。",
            "en_summary": "SCMP says a merchant was jailed five years four months for trying to kill his wife and three daughters over HK$900,000 debts.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3364241/hong-kong-merchant-jailed-trying-kill-wife-daughters-amid-debt-woes",
        },
        {
            "zh_title": "旺角女仆咖啡厅经营者涉嫌非礼14岁员工被捕",
            "en_title": "Hong Kong maid cafe operator arrested over alleged molestation of teen staff",
            "published": "11:20 2026年8月17日",
            "zh_summary": "SCMP报道，35岁男店主自员工入职日起多次非礼14岁初三女生，受害人周五报警，警方周六拘捕疑犯。",
            "en_summary": "SCMP says a 35-year-old cafe operator was arrested for allegedly molesting a 14-year-old employee since her first day at work.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3364232/hong-kong-maid-cafe-operator-arrested-allegedly-molesting-staff-14",
        },
        {
            "zh_title": "皇岗口岸本月将再举行两场更严峻通关演习",
            "en_title": "Two tougher Huanggang port drills planned this month, Hong Kong says",
            "published": "12:51 2026年8月17日",
            "zh_summary": "SCMP引保安局局长邓炳强称，下月再办两场演习，最多2万公务员参与，并测试反恐与高峰客流情景。",
            "en_summary": "SCMP says up to 20,000 civil servants will join two more drills testing peak flows and counter-terror scenarios at Huanggang.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3364243/2-more-drills-harsher-scenarios-planned-month-revamped-huanggang-port",
        },
        {
            "zh_title": "北部都会区柏Silicon首批单位逾半数售出",
            "en_title": "Northern Metropolis Park Silicon launch draws strong buyer interest",
            "published": "07:30 2026年8月17日",
            "zh_summary": "SCMP称合景泰富古洞北项目周日开售，82套常规单位中44套已售，另有8套以逾7843万港元成交。",
            "en_summary": "SCMP says 44 of 82 regular-sale units at Wheelock's Park Silicon sold on Sunday, with eight more fetching over HK$78.43m.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/business/article/3364205/launch-northern-metropolis-flats-attracts-strong-interest-hong-kong-homebuyers",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "《英雄》演员海顿·帕内特莱尔去世，年仅36岁",
            "en_title": "Hayden Panettiere, star of Heroes and Nashville, dies at 36",
            "published": "17:07 2026年8月17日",
            "zh_summary": "BBC报道，曾主演《英雄》《纳什维尔》的美国演员海顿·帕内特莱尔去世，父亲称其离世原因尚未公布。",
            "en_summary": "BBC says US actress Hayden Panettiere, known for Heroes and Nashville, has died at 36; her family gave no cause of death.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cq5665zgg1po",
        },
        {
            "zh_title": "英国首相与冒充特朗普幕僚长者短信往来",
            "en_title": "UK PM Burnham exchanged messages with White House imposter",
            "published": "16:24 2026年8月17日",
            "zh_summary": "BBC称伯恩汉上任后与冒充白宫幕僚长怀尔斯的陌生人互发数条短信，疑为安全事件，唐宁街拒评。",
            "en_summary": "BBC says Andy Burnham messaged someone posing as chief of staff Susie Wiles; Downing Street declined to comment on the breach.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/clyvj5zdjj2o",
        },
        {
            "zh_title": "印度UPI或向大型商户收费，消费者仍免费",
            "en_title": "India may allow merchant fees on UPI while keeping consumer payments free",
            "published": "07:30 2026年8月17日",
            "zh_summary": "BBC分析，印度立法为银行向商户收取MDR铺路，或针对大额交易，但个人转账预计继续免费。",
            "en_summary": "BBC analysis says new laws could let banks charge merchants on UPI, likely on large transactions, while P2P payments stay free.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c8xnwqe00v1o",
        },
        {
            "zh_title": "香港公司Antimatter押注中国开源AI挑战美系云服务",
            "en_title": "Hong Kong's Antimatter bets on Chinese open-weight AI to rival US clouds",
            "published": "09:00 2026年8月17日",
            "zh_summary": "SCMP称这家“新云”服务商帮企业从硅谷前沿模型迁移至中国开源方案，以降本并提升数据主权。",
            "en_summary": "SCMP says neo-cloud provider Antimatter helps firms shift from US frontier models to cheaper Chinese open-weight alternatives.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/tech/tech-trends/article/3364190/hong-kong-firm-bets-chinese-open-weight-models-rival-coreweave",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "财新": "#8e44ad", "Caixin": "#8e44ad",
    "路透社": "#2980b9", "Reuters": "#2980b9",
    "BBC": "#e67e22",
    "南华早报": "#16a085", "SCMP": "#16a085",
    "香港电台": "#27ae60", "RTHK": "#27ae60",
    "安纳多卢通讯社": "#d35400", "Anadolu Agency": "#d35400",
    "路透社 / 印度教徒报": "#2980b9", "Reuters / The Hindu": "#2980b9",
    "香港电台 / 法新社": "#27ae60", "RTHK / AFP": "#27ae60",
}


def item_html(n, item):
    color = SOURCE_COLORS.get(item["source_zh"], "#7f8c8d")
    return f'''<tr><td style="padding:0 0 22px 0;border-bottom:1px solid #eee;">
<div style="font-size:11px;color:#95a5a6;font-weight:700;margin-bottom:6px;">{n:02d}</div>
<div style="font-size:16px;font-weight:700;line-height:1.45;margin-bottom:4px;"><a href="{item['url']}" style="color:#1a5276;text-decoration:none;">{item['zh_title']}</a></div>
<div style="font-size:14px;color:#566573;font-style:italic;line-height:1.4;margin-bottom:4px;">{item['en_title']}</div>
<div style="font-size:11px;color:#95a5a6;margin-bottom:8px;">发布时间 Published: {item['published']}</div>
<div style="font-size:14px;color:#2c3e50;line-height:1.55;margin-bottom:4px;">{item['zh_summary']}</div>
<div style="font-size:13px;color:#5d6d7e;line-height:1.5;margin-bottom:10px;">{item['en_summary']}</div>
<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="font-size:12px;color:#2980b9;text-decoration:none;">查看全文 Read more →</a>
</td></tr>'''


def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    sections = []
    n = 1
    for cat_name, items in CATEGORIES:
        rows = "\n".join(item_html(n + i, it) for i, it in enumerate(items))
        n += len(items)
        sections.append(f'''<tr><td style="padding:18px 0 8px 0;">
<h2 style="margin:0;padding:10px 12px;background:#ecf0f1;border-left:4px solid #2980b9;font-size:15px;color:#2c3e50;">{cat_name}</h2>
</td></tr>
{rows}''')
    body = "\n".join(sections)
    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 - {DATE}</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:16px 0;"><tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a252f,#2c3e50);padding:28px 24px;text-align:center;">
<div style="font-size:24px;font-weight:800;color:#fff;letter-spacing:1px;">每日热点晚报</div>
<div style="font-size:13px;color:#bdc3c7;margin-top:6px;">Evening News Briefing · {DATE} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px 24px;">
<p style="margin:0 0 6px 0;font-size:14px;color:#2c3e50;line-height:1.6;">汇总今日全日要闻，涵盖国内政策、市场动态、科技前沿与国际热点。</p>
<p style="margin:0;font-size:13px;color:#7f8c8d;line-height:1.5;font-style:italic;">Today's main stories across China, tech, markets, society and world affairs.</p>
</td></tr>
<tr><td style="padding:0 24px 24px 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">
{body}
</table></td></tr>
<tr><td style="background:#f8f9fa;padding:18px 24px;border-top:1px solid #eee;">
<p style="margin:0 0 6px 0;font-size:11px;color:#95a5a6;line-height:1.5;">本简报由自动化系统编发，内容来源于公开媒体报道，仅供参考，不构成投资或法律建议。</p>
<p style="margin:0;font-size:11px;color:#95a5a6;line-height:1.5;font-style:italic;">This briefing is automatically compiled from public media sources for informational purposes only; it is not investment or legal advice.</p>
</td></tr>
</table></td></tr></table></body></html>'''


def main():
    html = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out} ({len(html)} chars, {sum(len(v) for _, v in CATEGORIES)} items)")


if __name__ == "__main__":
    main()
