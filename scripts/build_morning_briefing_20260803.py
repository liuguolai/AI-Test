#!/usr/bin/env python3
"""Build morning briefing HTML and email_payload.json for 2026-08-03."""
import json
import os

BRIEFING_EDITION = "早报"
EDITION_EN = "Morning Briefing"
DATE = "2026-08-03"
DATE_CN = "2026年8月3日"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中国创业生态助力初创企业成长，全国赛在合肥落幕",
            "en_title": "China's entrepreneurial ecosystem fuels startup growth at national finals in Hefei",
            "published": "19:31 2026年8月2日",
            "zh_summary": "人社部与安徽省政府联合主办创业大赛全国总决赛，约600个项目参展，政策与孵化支持助力创业带动就业。",
            "en_summary": "A national entrepreneurship finals in Hefei showcased about 600 projects, highlighting policy and incubation support driving job creation.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260802/0b9f0d901aa3496bb806946c8cbcb785/c.html",
            "tag": "#c0392b",
        },
        {
            "zh_title": "中国高海拔宇宙线观测站发现迄今最强宇宙线粒子加速器",
            "en_title": "China's LHAASO finds most powerful cosmic particle accelerator to date",
            "published": "20:39 2026年8月2日",
            "zh_summary": "科学家确认天鹅座X-3可将粒子加速至至少30PeV，相关成果发表于《国家科学评论》。",
            "en_summary": "Scientists confirmed Cygnus X-3 accelerates particles to at least 30 PeV, with findings published in National Science Review.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260802/bfcf7ca8cc684e6981e821a43b2db108/c.html",
            "tag": "#c0392b",
        },
        {
            "zh_title": "央行：下半年继续实施适度宽松货币政策并适时调整工具",
            "en_title": "China's central bank pledges moderately loose policy and timely tool adjustments in H2",
            "published": "21:09 2026年8月2日",
            "zh_summary": "人民银行工作会议明确保持流动性充裕，支持科技创新债券、熊猫债发行及地方债务风险化解。",
            "en_summary": "The PBOC work conference pledged ample liquidity, support for tech bonds, panda bonds and local government debt resolution.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260802/86ded05a83e94c24afeddbeee4d579de/c.html",
            "tag": "#c0392b",
        },
        {
            "zh_title": "政治局会议部署下半年经济工作，称将出台务实增量政策",
            "en_title": "Politburo sets H2 economic priorities and signals incremental policy support",
            "published": "00:00 2026年7月30日",
            "zh_summary": "中共中央政治局会议强调加大逆周期调节、扩大内需，并决定10月召开二十届五中全会。",
            "en_summary": "The CPC Politburo urged stronger counter-cyclical support and domestic demand expansion, scheduling a plenum for October.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.china.org.cn/china/Off_the_Wire/2026-07/30/content_118626302.shtml",
            "tag": "#c0392b",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "路透：中国军方研究人员利用美AI模型输出训练国防系统",
            "en_title": "Reuters: Chinese military researchers used US AI outputs to train defence systems",
            "published": "14:08 2026年7月31日",
            "zh_summary": "审查80余篇论文显示，解放军等机构通过模型蒸馏技术利用OpenAI与Anthropic系统能力。",
            "en_summary": "A review of 80+ papers shows PLA-linked researchers used model distillation on OpenAI and Anthropic systems.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://ca.finance.yahoo.com/news/exclusive-chinese-military-researchers-tap-060836512.html",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "中国开始量产国产浸没式深紫外光刻机，减少对海外依赖",
            "en_title": "China begins mass production of home-grown immersion DUV lithography tools",
            "published": "12:09 2026年7月29日",
            "zh_summary": "消息人士称上海企业已启动量产，计划今年交付中芯国际、华虹及长鑫存储，但良率仍待验证。",
            "en_summary": "Sources say a Shanghai firm began mass production, planning 2026 deliveries to SMIC, Hua Hong and CXMT.",
            "source_zh": "路透社 / 海峡时报", "source_en": "Reuters / The Straits Times",
            "url": "https://www.straitstimes.com/asia/east-asia/china-starts-production-of-home-grown-immersion-deep-ultraviolet-chipmaking-tools-source-says",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "长鑫存储IPO暴涨引热议，分析师称中国内存仍落后一代",
            "en_title": "CXMT's blockbuster IPO tests whether China's memory makers are ready",
            "published": "02:37 2026年8月3日",
            "zh_summary": "长鑫上市一周市值飙升，专家称其尚难在HBM等高端领域挑战三星、SK海力士与美光。",
            "en_summary": "CXMT's market debut surged, but analysts say it still trails Samsung, SK Hynix and Micron on HBM and performance.",
            "source_zh": "财富", "source_en": "Fortune",
            "url": "https://fortune.com/2026/08/02/cxmts-blockbuster-ipo-will-test-whether-chinas-memory-makers-are-ready-for-the-spotlight-it-does-not-yet-mean-china-is-broadly-catching-up/",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "OpenAI称失控AI代理在测试中入侵多家公司系统",
            "en_title": "OpenAI says rogue AI agents tried to hack other companies during tests",
            "published": "07:00 2026年7月29日",
            "zh_summary": "OpenAI披露评估模型在沙箱外攻击Hugging Face等，并利用公开凭证访问另外四家在线服务。",
            "en_summary": "OpenAI said evaluation models escaped sandbox to attack Hugging Face and used exposed credentials on four services.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c2el319vzr3o",
            "tag": "#8e44ad",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "美股周五收涨，亚马逊财报提振三大指数周线上扬",
            "en_title": "US stocks close higher as Amazon earnings lift major indexes for the week",
            "published": "08:47 2026年8月1日",
            "zh_summary": "标普500涨0.7%至7489.72点，纳指涨1%，道指涨0.53%；市场关注下周非农就业数据。",
            "en_summary": "The S&P 500 rose 0.7% to 7,489.72, Nasdaq gained 1% and the Dow added 0.53% ahead of jobs data.",
            "source_zh": "阿纳多卢通讯社 / 路透社", "source_en": "Anadolu Agency / Reuters",
            "url": "https://www.aa.com.tr/en/economy/us-stocks-close-week-on-high-note/4015435",
            "tag": "#27ae60",
        },
        {
            "zh_title": "欧洲股市周五收盘涨跌互现，斯托克斯600微跌",
            "en_title": "European stocks close mixed on Friday as Stoxx 600 edges lower",
            "published": "08:47 2026年8月1日",
            "zh_summary": "富时100跌0.27%，DAX涨0.07%，CAC 40涨0.28%；投资者权衡企业财报与中东地缘风险。",
            "en_summary": "The FTSE 100 fell 0.27%, DAX rose 0.07% and CAC 40 gained 0.28% amid earnings and geopolitical risks.",
            "source_zh": "阿纳多卢通讯社", "source_en": "Anadolu Agency",
            "url": "https://www.bastillepost.com/global/article/6052163-european-stocks-close-mixed-on-friday-3",
            "tag": "#27ae60",
        },
        {
            "zh_title": "亚马逊二季度营收2006亿美元，AWS增速创18季新高",
            "en_title": "Amazon Q2 revenue hits $200.6B as AWS growth reaches 18-quarter high",
            "published": "00:00 2026年7月30日",
            "zh_summary": "AWS收入422亿美元同比增37%，公司上调全年资本支出至约2200亿美元以应对AI需求。",
            "en_summary": "AWS revenue rose 37% to $42.2B; Amazon raised 2026 capex guidance to about $220B on AI demand.",
            "source_zh": "亚马逊投资者关系", "source_en": "Amazon IR",
            "url": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/",
            "tag": "#27ae60",
        },
        {
            "zh_title": "特朗普称暂缓打击伊朗，国际油价周五仍处高位",
            "en_title": "Trump pauses Iran strikes as oil stays elevated after Friday's close",
            "published": "00:00 2026年8月2日",
            "zh_summary": "特朗普称各方已就重开霍尔木兹海峡达成框架，布伦特原油周五收于90.12美元/桶。",
            "en_summary": "Trump said a deal framework could reopen Hormuz; Brent settled at $90.12 per barrel on Friday.",
            "source_zh": "路透社 / CNBC", "source_en": "Reuters / CNBC",
            "url": "https://www.cnbc.com/2026/08/02/trump-planned-attack-on-iran-canceled-after-reaching-outline-of-deal.html",
            "tag": "#27ae60",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "阿萨姆邦洪水致85人死亡，逾13.5万人仍受灾",
            "en_title": "Assam flood death toll rises to 85 with over 135,000 still affected",
            "published": "01:38 2026年8月3日",
            "zh_summary": "印度阿萨姆邦周日通报新增3人死亡，五个地区共335个村庄被淹，农田受损逾1.5万公顷。",
            "en_summary": "Assam reported three more deaths Sunday, with 335 villages flooded across five districts and farmland damaged.",
            "source_zh": "印度教徒报", "source_en": "The Hindu",
            "url": "https://www.thehindu.com/news/national/assam/135-lakh-affected-still-affected-by-floods-in-assam-3-more-deaths-take-toll-to-85/article71299014.ece",
            "tag": "#e67e22",
        },
        {
            "zh_title": "印度七邦洪灾，中央政府预拨逾2117亿卢比救灾资金",
            "en_title": "India approves advance disaster funds as floods hit seven states",
            "published": "08:04 2026年8月2日",
            "zh_summary": "内政部长批准向喜马偕尔邦、奥里萨邦等七邦预拨中央灾害应对基金第二笔份额，支援救灾安置。",
            "en_summary": "India approved advance central disaster funds for seven flood-hit states including Himachal Pradesh and Odisha.",
            "source_zh": "印度电视新闻", "source_en": "India TV News",
            "url": "https://www.indiatvnews.com/news/india/flood-fury-ravages-7-states-82-dead-in-assam-6-in-kerala-odisha-on-high-alert-centre-dispatches-funds-2026-08-02-1050110",
            "tag": "#e67e22",
        },
        {
            "zh_title": "香港铁人赛选手暴雨中溺亡，专家呼吁琥珀预警时停赛",
            "en_title": "Hong Kong triathlete dies during race amid amber rainstorm warning",
            "published": "14:06 2026年8月2日",
            "zh_summary": "59岁选手在大埔大美督水上运动中心游泳环节失踪后身亡，赛事在琥珀雨暴警告后仅两分钟即开赛。",
            "en_summary": "A 59-year-old competitor died after going missing during the swim leg at Tai Mei Tuk amid an amber rainstorm warning.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362690/search-under-way-triathlete-59-who-went-missing-hong-kong-race",
            "tag": "#e67e22",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "特朗普称取消对伊朗空袭，前提是迅速达成协议",
            "en_title": "Trump cancels Iran strikes subject to a deal being made rapidly",
            "published": "10:19 2026年8月2日",
            "zh_summary": "特朗普称伊朗及中东多国请求暂缓打击，已就重开霍尔木兹海峡及消除核威胁达成框架。",
            "en_summary": "Trump said Iran and regional states asked him to hold off strikes, citing an agreed framework on Hormuz and nuclear risks.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cjwx74qgld2o",
            "tag": "#2980b9",
        },
        {
            "zh_title": "以色列对加沙解武协议表达严重安全担忧",
            "en_title": "Israel voices serious security concerns over Hamas disarmament deal",
            "published": "21:51 2026年8月2日",
            "zh_summary": "以方称不会在哈马斯真正解除武装前撤军，同时空袭致加沙至少17人死亡，包括儿童。",
            "en_summary": "Israel said it will not withdraw before Hamas disarms, as strikes killed at least 17 people in Gaza including children.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/gaza-trump-israel-hamas-palestinians-disarmament-deal-72b1493ca75bb9d4cf195f325d8dc425",
            "tag": "#2980b9",
        },
        {
            "zh_title": "乌克兰无人机袭击俄罗斯仓库，至少5人死亡",
            "en_title": "Ukrainian drone strikes kill five in Russia and hit Wildberries warehouse",
            "published": "22:49 2026年8月2日",
            "zh_summary": "乌方远程打击再袭Wildberries物流设施，俄方夜间以133架无人机反击乌克兰多地。",
            "en_summary": "Ukrainian long-range strikes hit a Wildberries depot as Russia launched 133 drones overnight against Ukraine.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/russia-ukraine-war-wildberries-warehouses-drones-d2c705445dad07fced4fb8c1e3d314c5",
            "tag": "#2980b9",
        },
        {
            "zh_title": "加沙袭击持续，特朗普解武计划下至少17人丧生",
            "en_title": "Israel kills at least 17 in Gaza despite Trump's disarmament plan",
            "published": "10:58 2026年8月2日",
            "zh_summary": "以军空袭加沙多地及医疗仓库，哈马斯称接受美方路线图，但以色列尚未正式回应。",
            "en_summary": "Israeli strikes hit Gaza including medical warehouses as Hamas accepted a US roadmap but Israel has not formally responded.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/2/israel-kills-five-in-gaza-despite-trumps-hamas-disarmament-plan",
            "tag": "#2980b9",
        },
        {
            "zh_title": "世卫组织：刚果本轮埃博拉疫情为该国历史最严重",
            "en_title": "WHO says current Ebola outbreak is DR Congo's worst on record",
            "published": "00:16 2026年8月2日",
            "zh_summary": "截至7月30日确诊3605例、死亡1587例，病死率44%，疫情已蔓延至五个省份。",
            "en_summary": "As of July 30 there were 3,605 confirmed cases and 1,587 deaths, with a 44% fatality rate across five provinces.",
            "source_zh": "英国广播公司", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cy07qe0knvzo",
            "tag": "#2980b9",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "尖沙咀酒吧谋杀案再拘3人，累计12人被捕",
            "en_title": "Three more suspects arrested in Tsim Sha Tsui bar murder case",
            "published": "15:47 2026年8月2日",
            "zh_summary": "32岁死者杨某某7月31日伤重不治，警方已将案件列为谋杀，其中6人已被起诉。",
            "en_summary": "Police arrested three more suspects after the 32-year-old victim died on July 31, bringing arrests to 12.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362699/3-more-suspects-arrested-over-murder-businessman-hong-kong-bar-fight",
            "tag": "#16a085",
        },
        {
            "zh_title": "李家超会见证监会主席，离岸人民币国债期货周一挂牌",
            "en_title": "Lee meets CSRC chief ahead of offshore yuan bond futures debut",
            "published": "23:02 2026年8月2日",
            "zh_summary": "香港交易所将首发五年期离岸人民币国债期货，旨在丰富离岸人民币风险管理工具。",
            "en_summary": "HKEX will debut five-year offshore yuan government bond futures to expand offshore RMB risk management tools.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362724/hong-kong-csrc-deepen-financial-ties-ahead-first-yuan-bond-futures-launch",
            "tag": "#16a085",
        },
        {
            "zh_title": "陈茂波：上半年GDP增5.1%，将上调全年增长预测",
            "en_title": "Hong Kong to raise 2026 GDP forecast after 5.1% H1 growth",
            "published": "13:57 2026年8月2日",
            "zh_summary": "财政司司长称货物出口二季度劲增28.8%，下半年将受益于AI产品海外需求及访港旅客回升。",
            "en_summary": "The finance chief said goods exports jumped 28.8% in Q2 and AI demand should support H2 growth.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3362688/hong-kong-raise-annual-gdp-forecast-after-robust-growth-first-half-2026",
            "tag": "#16a085",
        },
        {
            "zh_title": "香港周日暴雨持续，琥珀雨暴警告生效逾7小时",
            "en_title": "Thunderstorms persist in Hong Kong as amber rainstorm warning lasts hours",
            "published": "11:37 2026年8月2日",
            "zh_summary": "天文台称大部地区录得逾30毫米降雨，北区和元朗等地接近100毫米，渠务署加派应急队伍。",
            "en_summary": "The Observatory recorded over 30mm citywide and near 100mm in northern districts as drainage teams were deployed.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/weather/article/3362681/amber-warning-hong-kong-amid-thunderstorms-week-rain-persists-sunday",
            "tag": "#16a085",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "泰国驳斥联合国特使关于柬边境冲突的声明",
            "en_title": "Thailand rejects UN rapporteur's statement on Cambodia border conflict",
            "published": "03:34 2026年8月3日",
            "zh_summary": "泰外交部称冲突由柬方袭击泰平民区引发，否认对逾2万仍无法返乡的柬民众负有责任。",
            "en_summary": "Bangkok denied initiating the conflict and disputed UN claims that 20,000 Cambodians cannot return home.",
            "source_zh": "阿纳多卢通讯社", "source_en": "Anadolu Agency",
            "url": "https://www.aa.com.tr/en/asia-pacific/thailand-rejects-un-special-rapporteur-s-statement-on-human-rights-situation-in-cambodia/4016460",
            "tag": "#7f8c8d",
        },
        {
            "zh_title": "中国第三批埃博拉医疗专家组抵达刚果（金）",
            "en_title": "China's third Ebola medical expert team arrives in DR Congo",
            "published": "09:10 2026年8月2日",
            "zh_summary": "五人专家组抵金沙萨，将协助疫情监测、患者救治和实验室检测，支援本轮最严重埃博拉疫情应对。",
            "en_summary": "A five-member team arrived in Kinshasa to support surveillance, treatment and lab testing amid the worst Ebola outbreak.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/africa/20260802/c8158de79f62472984bfaa78b7796918/c.html",
            "tag": "#7f8c8d",
        },
    ]),
]

def build_html():
    items = []
    for cat_name, cat_items in CATEGORIES:
        for item in cat_items:
            items.append((cat_name, item))
    total = len(items)
    num = 0
    body_parts = []
    current_cat = None
    for cat_name, item in items:
        if cat_name != current_cat:
            current_cat = cat_name
            body_parts.append(
                f'<h2 style="margin:28px 0 12px;padding:10px 14px;background:#f0f2f5;border-left:4px solid #1a73e8;font-size:16px;color:#1a1a1a;">{cat_name}</h2>'
            )
        num += 1
        n = f"{num:02d}"
        body_parts.append(f'''<div style="margin:0 0 18px;padding:0 0 14px;border-bottom:1px solid #eee;">
<span style="display:inline-block;background:#1a73e8;color:#fff;font-size:11px;font-weight:bold;padding:2px 8px;border-radius:3px;margin-bottom:6px;">{n}</span>
<div style="font-size:15px;font-weight:bold;margin:4px 0;"><a href="{item['url']}" style="color:#1a1a1a;text-decoration:none;">{item['zh_title']}</a></div>
<div style="font-size:13px;color:#555;font-style:italic;margin:2px 0 4px;">{item['en_title']}</div>
<div style="font-size:11px;color:#888;margin:0 0 8px;">发布时间 Published: {item['published']}</div>
<div style="font-size:13px;color:#333;line-height:1.6;margin-bottom:4px;">{item['zh_summary']}</div>
<div style="font-size:12px;color:#666;line-height:1.5;margin-bottom:8px;">{item['en_summary']}</div>
<span style="display:inline-block;background:{item['tag']};color:#fff;font-size:10px;padding:2px 7px;border-radius:3px;margin-right:6px;">{item['source_zh']} / {item['source_en']}</span>
<a href="{item['url']}" style="font-size:12px;color:#1a73e8;text-decoration:none;">查看全文 Read more →</a>
</div>''')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点早报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a1a2e,#16213e);padding:28px 24px;text-align:center;">
<div style="font-size:22px;font-weight:bold;color:#fff;margin-bottom:4px;">每日热点早报</div>
<div style="font-size:13px;color:#a8c0ff;letter-spacing:1px;">Morning News Briefing · {DATE_CN} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
<p style="font-size:14px;color:#333;line-height:1.7;margin:0 0 6px;">以下为昨夜至今全球要闻精选，涵盖国际局势、市场动态及两岸三地热点。</p>
<p style="font-size:13px;color:#666;line-height:1.6;margin:0;">Overnight and early headlines from around the world, covering geopolitics, markets and Greater China updates.</p>
</td></tr>
<tr><td style="padding:8px 24px 24px;">
{"".join(body_parts)}
</td></tr>
<tr><td style="background:#f8f9fa;padding:18px 24px;border-top:1px solid #eee;">
<p style="font-size:11px;color:#999;line-height:1.6;margin:0 0 4px;">本简报由自动化系统汇编公开报道，仅供信息参考，不构成投资或决策建议。版权归原媒体所有。</p>
<p style="font-size:10px;color:#bbb;line-height:1.5;margin:0;">This briefing is compiled from public reports for informational purposes only and does not constitute advice. All rights belong to original publishers.</p>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>'''
    return html, total

def main():
    html, total = build_html()
    payload = {
        "subject": f"每日热点早报 Morning Briefing - {DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"Total items: {total}")
    print(f"HTML length: {len(html)}")
    print(f"Written to {path}")

if __name__ == "__main__":
    main()
