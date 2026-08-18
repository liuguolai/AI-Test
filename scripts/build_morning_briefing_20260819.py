#!/usr/bin/env python3
"""Build 2026-08-19 morning briefing HTML and email_payload.json. Do not send mail."""
import json
import os
import re
import sys

OUT_JSON = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")

ITEMS = [
    {
        "cat": "china",
        "zh_t": "公积金提取范围扩大，灵活就业者可自愿缴存",
        "en_t": "China widens housing provident fund use and lets gig workers join",
        "pub": "17:02 2026年8月18日",
        "zh_s": "李强签署国务院令，修订后的住房公积金条例9月20日起施行，租房提取取消收入比例门槛，灵活就业者可自愿缴存。",
        "en_s": "Premier Li signed a State Council order expanding withdrawals and allowing flexible workers to contribute from Sept. 20.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/leaders/20260818/8218b8ed91264a14a4f35960d85c2deb/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "china",
        "zh_t": "习近平同厄瓜多尔总统诺沃亚会谈并见证合作文件",
        "en_t": "Xi meets Ecuador’s president and witnesses cooperation deals",
        "pub": "19:01 2026年8月18日",
        "zh_s": "习近平下午在人民大会堂同诺沃亚会谈，强调对接发展战略、挖掘自贸潜力，会后见证绿色产业、经贸与数字经济等文件。",
        "en_s": "Xi held talks with President Noboa in Beijing and witnessed deals on green industry, trade and the digital economy.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/leaders/20260818/a15e6eee8d7e4779aaf4c75567848e49/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "china",
        "zh_t": "广州新房价格指数五连涨，过半典型楼盘均价仍跌",
        "en_t": "Guangzhou new-home prices rise a fifth month as most estates still fall",
        "pub": "19:37 2026年8月18日",
        "zh_s": "统计局显示广州7月新房价格环比升0.1%，已连涨五个月；机构数据显示202个典型楼盘中108个成交均价仍下降。",
        "en_s": "Official prices rose 0.1% in July, a fifth monthly gain, but 108 of 202 tracked estates still saw lower average selling prices.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://www.caixin.com/2026-08-18/102475421.html",
        "color": "#ff6b00",
    },
    {
        "cat": "china",
        "zh_t": "内地支持险资经沪深港通投资香港ETF",
        "en_t": "Mainland insurers get support to buy Hong Kong ETFs via Stock Connect",
        "pub": "20:04 2026年8月18日",
        "zh_s": "金融监管总局宣布支持内地保险机构通过沪深港通投资香港交易所买卖基金，两地监管暂未公布正式开闸时间表。",
        "en_s": "NFRA said it supports insurers buying Hong Kong ETFs through Stock Connect; no start date was given.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-08-18/102475442.html",
        "color": "#ff6b00",
    },
    {
        "cat": "tech",
        "zh_t": "英伟达加码资本布局，为OpenAI俄亥俄算力提供巨额担保",
        "en_t": "Nvidia’s AI edge shifts from chips toward capital backstops",
        "pub": "19:00 2026年8月18日",
        "zh_s": "英伟达一周内推动最高5000亿美元芯片融资，并为俄亥俄OpenAI数据中心提供最高1050亿美元支持。",
        "en_s": "After a $500 billion chip-finance pact, Nvidia is backing up to $105 billion for an OpenAI campus in Ohio.",
        "src_zh": "CNBC",
        "src_en": "CNBC",
        "url": "https://www.cnbc.com/2026/08/18/nvidias-ai-moat-is-shifting-from-chips-to-capital.html",
        "color": "#185fad",
    },
    {
        "cat": "tech",
        "zh_t": "爱奇艺二季度净亏2亿元，转向AI内容平台",
        "en_t": "iQIYI posts a 200 million yuan Q2 loss as it bets on AI content",
        "pub": "21:27 2026年8月18日",
        "zh_s": "爱奇艺营收同比降5%至62.9亿元，Non-GAAP净亏2亿元；龚宇称平台将做去中心化分发并加大AI影视生产。",
        "en_s": "Revenue fell 5% to 6.29 billion yuan; CEO Gong Yu said iQIYI will decentralize distribution and lean into AI production.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://companies.caixin.com/2026-08-18/102475462.html",
        "color": "#ff6b00",
    },
    {
        "cat": "tech",
        "zh_t": "垣信完成近70亿元增资，估值约500亿元低于此前预期",
        "en_t": "Satellite operator Yuanxin raises 6.98 billion yuan at a 50 billion yuan valuation",
        "pub": "18:52 2026年8月18日",
        "zh_s": "上海产权交易所披露垣信引入18家投资者募资69.76亿元，整体估值约500亿元，低于此前最高750亿元预期。",
        "en_s": "Eighteen investors funded Yuanxin at about 50.05 billion yuan, below a prior valuation target as high as 75 billion yuan.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://www.caixin.com/2026-08-18/102475403.html",
        "color": "#ff6b00",
    },
    {
        "cat": "tech",
        "zh_t": "英国与谷歌启动大西洋航路AI试验，规避增温尾迹",
        "en_t": "UK and Google trial AI altitude tweaks to cut warming contrails",
        "pub": "22:21 2026年8月18日",
        "zh_s": "为期30个月的蓝天行动将在北大西洋Shanwick空域试点，部分航班高度可调整约2000英尺以减少尾迹。",
        "en_s": "Operation Blue Skies will test 2,000-foot altitude changes over Shanwick airspace during the next two winters.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://apnews.com/article/google-contrails-climate-warming-aviation-2110e4cb5c317c3434805076764c5a47",
        "color": "#2671b8",
    },
    {
        "cat": "finance",
        "zh_t": "美股三大指数收跌，纳指跌1.3%，科技股拖累",
        "en_t": "Wall Street slips as the Nasdaq drops 1.3% on a tech selloff",
        "pub": "04:36 2026年8月19日",
        "zh_s": "道指收跌0.2%报53343.40点，标普500跌0.7%，纳指跌1.3%；英伟达等AI权重走弱。",
        "en_s": "The Dow fell 0.2% to 53,343.40, the S&P 500 lost 0.7%, and the Nasdaq sank 1.3% as AI names retreated.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://wtop.com/europe/2026/08/how-major-us-stock-indexes-fared-tuesday-8-18-2026/",
        "color": "#2671b8",
    },
    {
        "cat": "finance",
        "zh_t": "伦敦富时微升，欧陆主要股指收跌约0.8%",
        "en_t": "FTSE 100 ekes out a gain as the DAX and CAC fall about 0.8%",
        "pub": "00:14 2026年8月19日",
        "zh_s": "富时100收涨0.1%报10728.04点，油气股走强；巴黎CAC与法兰克福DAX均跌约0.8%。",
        "en_s": "London’s FTSE 100 rose 0.1% to 10,728.04 as oil majors gained; Paris and Frankfurt each closed about 0.8% lower.",
        "src_zh": "独立报",
        "src_en": "The Independent",
        "url": "https://www.independent.co.uk/news/business/donald-trump-aim-hugo-boss-iran-brent-b3035101.html",
        "color": "#111111",
    },
    {
        "cat": "finance",
        "zh_t": "港股微涨、沪指收升，日韩股市隔夜重挫",
        "en_t": "Hong Kong edges up as Tokyo and Seoul slide on oil and yields",
        "pub": "17:18 2026年8月18日",
        "zh_s": "恒指收升0.1%报25471点，能源股走强、科技偏弱；日经225跌2.5%，韩国综指跌1.55%。",
        "en_s": "The Hang Seng rose 0.1% to 25,471, while the Nikkei tumbled 2.5% and the Kospi lost 1.55%.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866585-20260818.htm",
        "color": "#0b7a4b",
    },
    {
        "cat": "finance",
        "zh_t": "国泰海通上半年净利202.6亿元，扣非利润大增",
        "en_t": "Guotai Haitong first-half profit reaches 20.26 billion yuan",
        "pub": "22:07 2026年8月18日",
        "zh_s": "营收471.63亿元、同比增97.56%；扣除非经常损益后归母净利195.1亿元，同比增168%。",
        "en_s": "Revenue nearly doubled to 47.16 billion yuan; adjusted net profit rose 168% after stripping one-off merger gains.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-08-18/102475476.html",
        "color": "#ff6b00",
    },
    {
        "cat": "finance",
        "zh_t": "沙特在霍尔木兹以东码头恢复装油并推销重质原油",
        "en_t": "Saudi Aramco resumes Hormuz loadings and offers heavy crude",
        "pub": "17:24 2026年8月18日",
        "zh_s": "航运数据显示三艘超大型油轮上周在朱阿伊马和拉斯塔努拉各装约200万桶；阿美向亚洲炼厂推销中质与重质现货。",
        "en_s": "Three VLCCs loaded about 2 million barrels each at Juaymah and Ras Tanura after weeks of halted Hormuz sales.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.reuters.com/business/energy/saudi-arabia-resumes-oil-loadings-sales-inside-strait-hormuz-2026-08-18/",
        "color": "#ff6b00",
    },
    {
        "cat": "society",
        "zh_t": "杭州通报酒局案：房企高管与公职人员被刑拘",
        "en_t": "Hangzhou detains a developer executive and an official over a KTV assault",
        "pub": "20:03 2026年8月18日",
        "zh_s": "官方称7月26日赵某峰、郁某栋在KTV强制猥亵并致人轻伤二级，两人已被刑拘并免职，纪检将立案调查。",
        "en_s": "Police detained a China Merchants Shekou executive and a Binjiang official after a July 26 assault; both were dismissed.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://china.caixin.com/2026-08-18/102475439.html",
        "color": "#ff6b00",
    },
    {
        "cat": "society",
        "zh_t": "元朗未牵绳恶犬咬死两犬，饲主被捕",
        "en_t": "Hong Kong arrests an owner after an unleashed dog kills two pets",
        "pub": "17:44 2026年8月18日",
        "zh_s": "渔护署拘捕元朗一只约60公斤犬只的饲主，该犬约二十分钟内咬死两只小型犬；上月已有咬人记录并被扣留。",
        "en_s": "AFCD arrested the owner of a 60kg unleashed dog that killed two smaller dogs in Yuen Long, after a prior biting case.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866597-20260818.htm",
        "color": "#0b7a4b",
    },
    {
        "cat": "society",
        "zh_t": "消委会：药品保健投诉升至1190宗，促药房规范售卖",
        "en_t": "Hong Kong consumer watchdog flags 1,190 medicine-shop complaints",
        "pub": "14:37 2026年8月18日",
        "zh_s": "前七个月药品保健投诉同比升50.6%；有游客买到疑似仿品，亦有把约140元药材做成2.24万元的手法。",
        "en_s": "Complaints jumped 50.6% to 1,190; one case saw a HK$140 herb bill inflated to HK$22,400 after grinding.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866567-20260818.htm",
        "color": "#0b7a4b",
    },
    {
        "cat": "society",
        "zh_t": "大埔宏福苑火灾独立委员会报告延至10月底",
        "en_t": "Tai Po fire inquiry report delayed until the end of October",
        "pub": "13:32 2026年8月18日",
        "zh_s": "委员会称书面证据逾百万份、议题复杂，行政长官同意延期；原定九个月、9月提交的报告拟于10月底呈交。",
        "en_s": "The judge-led panel said it is reviewing more than a million files and will report by late October, not September.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3364385/committee-probing-tai-po-fire-delays-submission-report-end-october",
        "color": "#0a4d8c",
    },
    {
        "cat": "world",
        "zh_t": "以色列空袭叙利亚北部基地后，美国推动三方防误击机制",
        "en_t": "US seeks Israel-Turkey-Syria deconfliction after airbase strikes",
        "pub": "03:36 2026年8月19日",
        "zh_s": "特使巴拉克称以色列袭击阿布达胡尔基地前未通报土耳其；叙媒称八次空袭跑道与仓储设施，暂无伤亡报告。",
        "en_s": "Envoy Tom Barrack said Turkey was not warned before Israel struck Abu al-Dahur; Syrian media reported no casualties.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.straitstimes.com/world/middle-east/us-working-on-deconfliction-mechanism-among-turkey-israel-and-syria-us-envoy-says",
        "color": "#ff6b00",
    },
    {
        "cat": "world",
        "zh_t": "特朗普称未与伊朗谈判，坚称霍尔木兹海峡畅通",
        "en_t": "Trump says no Iran talks are under way and insists Hormuz is open",
        "pub": "22:52 2026年8月18日",
        "zh_s": "临时停火到期后，特朗普发文称没有会谈安排、对伊港口封锁仍在；伊朗称海峡关闭至美方满足六月协议条件。",
        "en_s": "Trump said no talks are scheduled and the naval blockade stands; Iran says Hormuz stays shut until U.S. terms are met.",
        "src_zh": "加拿大广播公司",
        "src_en": "CBC",
        "url": "https://www.cbc.ca/news/world/iran-memorandum-expires-9.7310654",
        "color": "#e21b22",
    },
    {
        "cat": "world",
        "zh_t": "美加赶在50%关税生效前进行最后磋商",
        "en_t": "US and Canada hold last-minute talks to avert 50% tariffs",
        "pub": "12:01 2026年8月18日",
        "zh_s": "特朗普设定周三凌晨生效、覆盖约200亿美元加货的50%关税；卡尼办公室称两人两日内两度通话，谈判仍在进行。",
        "en_s": "A 50% levy on about $20 billion of Canadian goods is set for 12:01 a.m. Wednesday unless a truce is reached.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://apnews.com/article/tariffs-trump-canada-usmca-trade-aae597c22617bec7a99f670a2c787ef9",
        "color": "#2671b8",
    },
    {
        "cat": "world",
        "zh_t": "美国制裁国际刑事法院院长赤根智子及一名资深律师",
        "en_t": "US sanctions the ICC president and a senior trial lawyer",
        "pub": "01:40 2026年8月19日",
        "zh_s": "国务卿鲁比奥宣布制裁日本籍院长与塞内加尔籍律师；法院回应称此举损害法治。华盛顿已制裁至少11名法院人员。",
        "en_s": "Secretary Rubio targeted President Tomoko Akane and lawyer Abdoulaye Seye; the ICC said the measures undermine the rule of law.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cnvnl0elz47o",
        "color": "#bb1919",
    },
    {
        "cat": "hk",
        "zh_t": "海关“火网”行动检获约240公斤毒品，拘捕10人",
        "en_t": "Hong Kong customs seize HK$56 million in drugs and arrest 10",
        "pub": "16:16 2026年8月18日",
        "zh_s": "为期一个月的跨境行动打击经港转运大麻，市值约5600万港元；九男一女被捕，年龄介乎18至57岁。",
        "en_s": "Operation Flame Mesh seized about 240kg of suspected cannabis transiting Hong Kong toward Europe and Africa.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866578-20260818.htm",
        "color": "#0b7a4b",
    },
    {
        "cat": "hk",
        "zh_t": "美国民主党议员批评特朗普放宽对中港官员制裁",
        "en_t": "US Democrats rebuke Trump for easing China and Hong Kong sanctions",
        "pub": "06:46 2026年8月19日",
        "zh_s": "多名民主党议员致信政府，反对7月让部分中港官员脱离制裁名单，包括律政司司长林定国等。",
        "en_s": "Lawmakers said lifting restrictions on officials including Justice Secretary Paul Lam raises doubts about U.S. Hong Kong policy.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/us/diplomacy/article/3364488/us-democrats-rebuke-trump-easing-sanctions-china-hong-kong-officials",
        "color": "#0a4d8c",
    },
    {
        "cat": "hk",
        "zh_t": "港府争取本月底公布优化工作暑热警告",
        "en_t": "Hong Kong aims to improve the workplace heat warning by month-end",
        "pub": "12:46 2026年8月18日",
        "zh_s": "劳工及福利局局长孙玉菡表示，正检视由黄转红的触发门槛；本月破纪录高温下警告仍停在最低琥珀色。",
        "en_s": "Secretary Chris Sun said Labour and the Observatory are reviewing when the alert should rise from amber to red.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866554-20260818.htm",
        "color": "#0b7a4b",
    },
    {
        "cat": "other",
        "zh_t": "研究：气候变化是欧洲海域升温主因，地中海今夏多升温约2℃",
        "en_t": "Climate change added about 2C to Mediterranean marine heat this summer",
        "pub": "07:05 2026年8月19日",
        "zh_s": "世界天气归因组织称化石燃料排放推高欧洲海温；比斯开湾约九成、西地中海约八成海域出现海洋热浪。",
        "en_s": "WWA scientists said human-caused warming added about 2C in the Mediterranean and 1.3C–1.4C in western European seas.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://www.france24.com/en/live-news/20260818-climate-change-main-driver-of-european-ocean-warming-study",
        "color": "#1a8f4a",
    },
    {
        "cat": "other",
        "zh_t": "宇树科技将于周三登陆科创板，机器人板块先涨",
        "en_t": "Unitree’s STAR Market debut is due Wednesday after robot shares rally",
        "pub": "17:18 2026年8月18日",
        "zh_s": "港台援引行情称机器人产业指数收涨2.5%，谐波减速器龙头涨5.1%，市场等待宇树科技科创板上市。",
        "en_s": "A robot industry gauge rose 2.5% and Leader Harmonious Drive gained 5.1% ahead of Unitree’s listing.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866585-20260818.htm",
        "color": "#0b7a4b",
    },
]

CATS = [
    ("china", "国内 / 内地 China Mainland"),
    ("tech", "科技 / 互联网 Technology"),
    ("finance", "财经 / 商业 Finance & Business"),
    ("society", "社会 Society"),
    ("world", "国际 World"),
    ("hk", "香港本地 Hong Kong"),
    ("other", "其他 Other"),
]

FORBIDDEN = ["测试", "TEST", "Draft", "预览", "省略", "晚报", "续"]


def zh_len(s):
    return len(re.sub(r"\s+", "", s))


def en_words(s):
    return len(re.findall(r"[A-Za-z0-9']+", s))


def validate():
    n = len(ITEMS)
    if not 20 <= n <= 28:
        raise SystemExit(f"count {n} out of range")
    counts = {}
    for it in ITEMS:
        counts[it["cat"]] = counts.get(it["cat"], 0) + 1
        if zh_len(it["zh_s"]) > 55:
            raise SystemExit(f"zh summary too long ({zh_len(it['zh_s'])}): {it['zh_t']}")
        if en_words(it["en_s"]) > 30:
            raise SystemExit(f"en summary too long ({en_words(it['en_s'])}): {it['en_t']}")
        blob = " ".join([it["zh_t"], it["en_t"], it["zh_s"], it["en_s"], it["src_zh"], it["src_en"]])
        for w in FORBIDDEN:
            if w == "续" and "续" in blob:
                raise SystemExit(f"forbidden 续 in {it['zh_t']}")
            if w != "续" and w in blob:
                raise SystemExit(f"forbidden {w} in {it['zh_t']}")
    print("counts", counts, "total", n)
    return counts


def item_html(i, it):
    n = f"{i:02d}"
    return (
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 14px 0;border-bottom:1px solid #eee;">'
        f'<tr><td style="padding:0 0 14px 0;">'
        f'<div style="font-size:11px;color:#5b7cfa;font-weight:700;letter-spacing:1px;">{n}</div>'
        f'<a href="{it["url"]}" style="color:#1a1a1a;text-decoration:none;font-size:16px;font-weight:700;line-height:1.4;display:block;margin:4px 0 2px;">{it["zh_t"]}</a>'
        f'<div style="font-size:13px;color:#555;font-style:italic;line-height:1.4;">{it["en_t"]}</div>'
        f'<div style="font-size:12px;color:#888;margin:4px 0 8px;">发布时间 Published: {it["pub"]}</div>'
        f'<div style="font-size:14px;color:#333;line-height:1.6;">{it["zh_s"]}</div>'
        f'<div style="font-size:13px;color:#555;line-height:1.55;margin:4px 0 8px;">{it["en_s"]}</div>'
        f'<a href="{it["url"]}" style="display:inline-block;background:{it["color"]};color:#fff;text-decoration:none;font-size:11px;padding:3px 8px;border-radius:3px;">{it["src_zh"]} {it["src_en"]}</a>'
        f' <a href="{it["url"]}" style="font-size:12px;color:#5b7cfa;text-decoration:none;">查看全文 Read more →</a>'
        f"</td></tr></table>"
    )


def build_html(n):
    sections = []
    idx = 1
    by_cat = {k: [] for k, _ in CATS}
    for it in ITEMS:
        by_cat[it["cat"]].append(it)
    for key, title in CATS:
        rows = "".join(item_html(i, it) for i, it in zip(range(idx, idx + len(by_cat[key])), by_cat[key]))
        idx += len(by_cat[key])
        sections.append(
            f'<h2 style="margin:22px 0 12px;padding:8px 12px;background:#f3f5f8;border-left:4px solid #5b7cfa;font-size:16px;color:#1a1a1a;">{title}</h2>'
            + rows
        )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点早报 Morning News Briefing · 2026年8月19日</title>
</head>
<body style="margin:0;padding:0;background:#e9edf2;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'PingFang SC','Noto Sans SC',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#e9edf2;">
<tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.08);">
<tr><td style="background:#1b2430;color:#fff;padding:22px 24px;">
<div style="font-size:22px;font-weight:800;letter-spacing:.5px;">每日热点早报</div>
<div style="font-size:13px;color:#c9d3e0;margin-top:6px;">Morning News Briefing · 2026年8月19日 · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:18px 24px 8px;color:#333;font-size:14px;line-height:1.7;">
汇总昨夜至今要闻，覆盖隔夜美欧收盘、早间政策与国际突发。<br>
Overnight and early headlines, from Wall Street’s close to morning policy and breaking world news.
</td></tr>
<tr><td style="padding:4px 24px 8px;">{''.join(sections)}</td></tr>
<tr><td style="padding:16px 24px 24px;font-size:11px;color:#888;line-height:1.6;border-top:1px solid #eee;">
本邮件由公开报道汇编，仅供参考，不构成投资、法律或政策建议。发布时间已换算为Asia/Shanghai（UTC+8）。<br>
This briefing compiles publicly reported news for information only and is not investment, legal or policy advice. Times are shown in Asia/Shanghai (UTC+8).
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>"""


def main():
    counts = validate()
    html = build_html(len(ITEMS))
    blob = html
    for w in FORBIDDEN:
        if w == "续" and "续" in blob:
            raise SystemExit("forbidden 续 in HTML")
        if w != "续" and w in blob:
            raise SystemExit(f"forbidden {w} in HTML")
    if len(html) > 100000:
        print("WARN html length", len(html))
    payload = {
        "subject": "每日热点早报 Morning Briefing - 2026-08-19",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("wrote", os.path.abspath(OUT_JSON), "html_chars", len(html), "counts", counts)


if __name__ == "__main__":
    sys.exit(main())
