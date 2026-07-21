#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json."""
import json
import os

DATE = "2026-07-22"
EDITION_ZH = "早报"
EDITION_EN = "Morning Briefing"
SUBJECT = f"每日热点早报 Morning Briefing - {DATE}"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中方就仁爱礁冲突向菲律宾驻华大使严正交涉",
            "en_title": "China summons Philippine ambassador over Ren'ai Reef clash",
            "published": "15:00 2026年7月21日",
            "zh_summary": "外交部称菲方小艇危险抵近冲撞中方船只并袭击执法人员，已召见菲大使严正交涉。",
            "en_summary": "Beijing says Philippine boats rammed Chinese vessels and assaulted law-enforcement officers near Ren'ai Reef.",
            "source_zh": "中国驻美大使馆",
            "source_en": "PRC Embassy in the US",
            "url": "https://us.china-embassy.gov.cn/lcbt/wjbfyrbt/202607/t20260721_11989097.htm",
        },
        {
            "zh_title": "中国据报研拟收紧AI模型与芯片出口管制",
            "en_title": "China weighs tighter export curbs on AI models and chips",
            "published": "13:55 2026年7月21日",
            "zh_summary": "路透援引金融时报称商务部正征询阿里、字节等意见，拟限制模型权重与训练数据外流。",
            "en_summary": "Reuters cites the FT saying Beijing is consulting tech firms on curbing overseas access to advanced AI and chip designs.",
            "source_zh": "路透社",
            "source_en": "Reuters",
            "url": "https://www.ndtv.com/world-news/china-considers-tighter-export-controls-on-ai-models-and-chips-ft-reports-11799259",
        },
        {
            "zh_title": "中国加快拓展通往中亚的陆路贸易通道",
            "en_title": "China rapidly expands land trade routes to Central Asia",
            "published": "05:30 2026年7月22日",
            "zh_summary": "评论指中欧班列上半年增两成，中亚成分流海运风险、拓展陆路出口的重要枢纽。",
            "en_summary": "Commentary says China-Europe rail freight rose 20% in H1 as Central Asia gains importance amid maritime risks.",
            "source_zh": "南华早报",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/opinion/china-opinion/article/3360836/why-china-rapidly-expanding-its-land-trade-routes-central-asia",
        },
        {
            "zh_title": "央行LPR连续第14个月维持不变",
            "en_title": "China keeps benchmark lending rates unchanged for 14th month",
            "published": "09:00 2026年7月20日",
            "zh_summary": "一年期与五年期LPR分别维持3.00%和3.50%，在二季度GDP放缓至4.3%后仍按兵不动。",
            "en_summary": "The one- and five-year LPR stayed at 3.00% and 3.50% despite Q2 GDP slowing to 4.3% year on year.",
            "source_zh": "科技时报",
            "source_en": "Tech Times",
            "url": "https://www.techtimes.com/articles/321088/20260720/china-rate-freeze-stretches-14-months-gdp-slips-post-pandemic-low.htm",
        },
        {
            "zh_title": "康美药业追偿案一审判令原实控人等赔偿近140亿元",
            "en_title": "Kangmei wins court order for nearly $2bn from ex-controllers",
            "published": "21:56 2026年7月21日",
            "zh_summary": "在完成24.6亿元投资者赔偿逾四年后，广州中院判令马兴田等向公司承担追偿责任。",
            "en_summary": "A Guangzhou court ordered former controllers to pay Kangmei after its investor compensation case.",
            "source_zh": "财新网",
            "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-07-21/102466749.html",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "美财长威胁对涉嫌窃IP的中国开源AI实施制裁",
            "en_title": "US Treasury threatens sanctions over Chinese open-source AI IP theft",
            "published": "23:37 2026年7月21日",
            "zh_summary": "贝森特称支持开源但不容忍知识产权盗窃，在月之暗面Kimi K3走红后对华模型审查升温。",
            "en_summary": "Treasury Secretary Bessent warned sanctions if overseas models steal US IP, as Chinese open models gain ground.",
            "source_zh": "TechCrunch",
            "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/",
        },
        {
            "zh_title": "路透总编辑警告AI正侵蚀全球新闻业",
            "en_title": "Reuters editor-in-chief warns AI is hijacking global journalism",
            "published": "16:16 2026年7月21日",
            "zh_summary": "加洛尼在悉尼演讲称，全球一成新闻消费者已用聊天机器人获取资讯，新闻版权遭无偿挪用。",
            "en_summary": "Alessandra Galloni said 10% of news consumers now use AI chatbots, threatening publishers' revenue and IP.",
            "source_zh": "澳大利亚广播公司",
            "source_en": "ABC News",
            "url": "https://www.abc.net.au/news/2026-07-21/alessandra-galloni-ai-journalism-andrew-olle-lecture/106940228",
        },
        {
            "zh_title": "法院最终批准Anthropic 15亿美元版权和解",
            "en_title": "Court grants final approval to Anthropic's $1.5B copyright settlement",
            "published": "18:51 2026年7月21日",
            "zh_summary": "联邦法官批准作者集体诉讼和解，每部作品约获3000美元，为美国版权史上最大规模和解之一。",
            "en_summary": "A US judge approved Anthropic's landmark settlement with authors over pirated books used to train Claude.",
            "source_zh": "The Verge",
            "source_en": "The Verge",
            "url": "https://www.theverge.com/ai-artificial-intelligence/968511/anthropic-has-to-pay-authors",
        },
        {
            "zh_title": "法官叫停1100亿美元派拉蒙与华纳兄弟并购案",
            "en_title": "Judge pauses $110B Paramount-Warner Bros. merger",
            "published": "01:58 2026年7月21日",
            "zh_summary": "加州等12州检察长起诉后，联邦法官下令暂停交易14天，称合并将削弱影院与有线电视竞争。",
            "en_summary": "A federal judge issued a 14-day pause after 12 states sued, alleging the deal would harm competition.",
            "source_zh": "TechCrunch",
            "source_en": "TechCrunch",
            "url": "https://techcrunch.com/2026/07/20/judge-pauses-110b-paramount-warner-bros-merger/",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "美股芯片股反弹带动三大指数收涨",
            "en_title": "AI chip rally lifts Wall Street despite oil above $91",
            "published": "05:00 2026年7月22日",
            "zh_summary": "标普500涨0.9%至7509点，纳指涨1.3%，美光涨12%领涨，布油收于91.01美元。",
            "en_summary": "The S&P 500 rose 0.9% and Nasdaq 1.3% as Micron surged 12%, even as Brent crude settled at $91.01.",
            "source_zh": "美联社",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/stock-markets-ai-oil-iran-trump-30c42bb51683c4b43c9f64dfeff7a3ea",
        },
        {
            "zh_title": "A股强势反弹，回购与自购形成三重托底",
            "en_title": "China A-shares rebound as buybacks and fund purchases surge",
            "published": "19:33 2026年7月21日",
            "zh_summary": "沪指涨1.79%，科创综指涨8.75%，7月已有313家公司实施回购，公募私募同步加仓。",
            "en_summary": "The Shanghai Composite rose 1.79% as listed firms, mutual funds and private funds stepped up buying.",
            "source_zh": "财新网",
            "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-07-21/102466710.html",
        },
        {
            "zh_title": "蚂蚁国际完成约12亿美元A轮融资",
            "en_title": "Ant International closes about $1.2B Series A round",
            "published": "13:04 2026年7月21日",
            "zh_summary": "蚂蚁集团与阿里巴巴等参与本轮融资，资金将用于全球业务扩张及AI等前沿技术投入。",
            "en_summary": "Ant Group and Alibaba joined the round to fund global expansion and AI investments, Ant International said.",
            "source_zh": "财新网",
            "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-07-21/102466560.html",
        },
        {
            "zh_title": "亚股随半导体反弹上涨，油价攀升未阻风险偏好",
            "en_title": "Asian stocks rise as tech rebounds despite climbing oil",
            "published": "07:05 2026年7月22日",
            "zh_summary": "韩股涨3.6%、日股涨3.3%，上海涨1.8%，投资者押注大型科技公司即将公布的财报。",
            "en_summary": "Kospi jumped 3.6% and Nikkei 3.3% as chipmakers led a regional rebound ahead of Big Tech earnings.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863108-20260722.htm",
        },
        {
            "zh_title": "英国新首相宣布将取消家庭电费增值税",
            "en_title": "UK PM Burnham to cut VAT on household electricity bills",
            "published": "15:00 2026年7月21日",
            "zh_summary": "伯恩汉姆称10月1日起电费增值税由5%降至零，典型家庭年省约45英镑，资金来自取消数字身份证计划。",
            "en_summary": "Andy Burnham said VAT on electricity will drop to zero from October, saving typical homes about £45 a year.",
            "source_zh": "英国政府",
            "source_en": "UK Government",
            "url": "https://www.gov.uk/government/news/new-pm-cuts-tax-on-household-electricity-bills-to-give-breathing-space-on-cost-of-living",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "阿富汗东部洪灾致23死逾百失踪",
            "en_title": "Afghan flash floods kill 23 with more than 100 missing",
            "published": "17:15 2026年7月21日",
            "zh_summary": "努尔斯坦省帕伦市遭暴雨山洪袭击，数十栋建筑倒塌，10省仍面临新一轮洪涝威胁。",
            "en_summary": "Flash floods in eastern Nuristan killed 23 and left over 100 missing as more heavy rain was forecast.",
            "source_zh": "美国广播公司",
            "source_en": "ABC News",
            "url": "https://abcnews.com/International/wireStory/rescue-crews-afghanistan-search-missing-dead-rubble-left-134940779",
        },
        {
            "zh_title": "阿萨姆邦洪水遇难升至11人，逾31万人受灾",
            "en_title": "Assam floods kill 11 as more than 310,000 are affected",
            "published": "16:12 2026年7月21日",
            "zh_summary": "布拉马普特拉河等多条河流水位超警，铁路停运，军队与救灾队伍正展开救援。",
            "en_summary": "Major rivers overflowed in Assam, disrupting trains as the Army joined relief and rescue operations.",
            "source_zh": "商业标准报",
            "source_en": "Business Standard",
            "url": "https://www.business-standard.com/india-news/over-360k-hit-as-assam-flood-situation-remains-grim-rescue-ops-continue-126072100368_1.html",
        },
        {
            "zh_title": "法国六月热浪官方确认2025例超额死亡",
            "en_title": "France confirms 2,025 excess deaths in late-June heatwave",
            "published": "17:14 2026年7月21日",
            "zh_summary": "气温最高达43.8摄氏度，巴黎等地死亡率大幅上升，殡葬业与医院系统承受巨大压力。",
            "en_summary": "France reported 2,025 excess deaths as temperatures hit 43.8°C, straining hospitals and funeral services.",
            "source_zh": "路透社",
            "source_en": "Reuters",
            "url": "https://theprint.in/world/deadly-heatwaves-force-an-ageing-france-to-confront-a-hotter-future/2991995/",
        },
        {
            "zh_title": "锡金隧道坍塌致10死，救援仍在进行",
            "en_title": "Sikkim tunnel collapse kills 10 as rescue operations continue",
            "published": "14:59 2026年7月21日",
            "zh_summary": "南锡县在建隧道因山体滑坡坍塌，25人一度被困，莫迪与沙阿致电邦长了解救援进展。",
            "en_summary": "A landslide collapsed an NHPC tunnel in Namchi, killing 10 workers with rescue efforts ongoing.",
            "source_zh": "商业标准报",
            "source_en": "Business Standard",
            "url": "https://www.business-standard.com/india-news/sikkim-tunnel-collapse-7-dead-several-feared-trapped-as-rescue-continues-126072100071_1.html",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "泽连斯基撤换乌军总司令瑟尔斯基",
            "en_title": "Zelensky dismisses Ukraine army chief Syrskyi after protests",
            "published": "03:43 2026年7月22日",
            "zh_summary": "乌总统任命德拉帕蒂为新任总司令，此前撤换国防部长费多罗夫引发全国抗议。",
            "en_summary": "President Zelensky replaced Oleksandr Syrskyi with Mykhailo Drapatyi after days of nationwide protests.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cyvl35z3917o",
        },
        {
            "zh_title": "美军第10夜打击伊朗，霍尔木兹油轮再遭袭击",
            "en_title": "US strikes Iran for 10th night as Hormuz tanker is hit",
            "published": "08:00 2026年7月22日",
            "zh_summary": "美军称打击伊朗指挥与防空设施，伊朗称霍尔木兹两艘油轮起火，地区斡旋方正推动十天停火。",
            "en_summary": "The US carried out a 10th night of strikes as Iran reported tanker fires in the Strait of Hormuz amid ceasefire talks.",
            "source_zh": "CNBC",
            "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/07/21/us-iran-war-trump-hormuz-houthis.html",
        },
        {
            "zh_title": "黎巴嫩军方进驻南部试点区，以军鸣枪警告",
            "en_title": "Lebanese army deploys in southern pilot zone after Israeli pullout",
            "published": "02:30 2026年7月22日",
            "zh_summary": "工程部队进入扎瓦尔加尔比耶村，以军称黎军越界后朝天鸣枪，黎总统当日会晤特朗普。",
            "en_summary": "Lebanese troops entered Zawtar al-Gharbiyeh under a US-brokered plan as Israel fired warning shots.",
            "source_zh": "英国广播公司",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cy8mynlmn55o",
        },
        {
            "zh_title": "胡塞武装宣布对沙特实施海上封锁",
            "en_title": "Houthis declare naval blockade against Saudi Arabia",
            "published": "00:00 2026年7月22日",
            "zh_summary": "也门胡塞称即时封锁红海曼德海峡以报复沙特空袭，油轮已开始改道，能源市场再受冲击。",
            "en_summary": "Yemen's Houthis declared a Bab el-Mandeb blockade on Saudi Arabia, prompting tankers to reroute.",
            "source_zh": "全国公共广播电台",
            "source_en": "NPR",
            "url": "https://www.npr.org/2026/07/21/nx-s1-5901846/us-iran-updates",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "香港电影泰斗谢贤低调火化，享年89岁",
            "en_title": "Hong Kong screen legend Patrick Tse cremated at 89",
            "published": "13:05 2026年7月21日",
            "zh_summary": "家人按谢贤遗愿举行低调仪式，其子谢霆锋返港处理后事，不设公开追悼活动。",
            "en_summary": "Patrick Tse was cremated in a low-key ceremony as his family honored his wish for a private farewell.",
            "source_zh": "海峡时报",
            "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/life/hong-kong-veteran-actor-patrick-tse-died-of-pneumonia-was-cremated-in-low-key-funeral-reports",
        },
        {
            "zh_title": "击剑世锦赛首次在港举行，张家朗等名将出战",
            "en_title": "Fencing World Championships open in Hong Kong for first time",
            "published": "17:30 2026年7月21日",
            "zh_summary": "逾千名选手将在亚洲国际博览馆角逐12金，张家朗、蔡俊彦等港将凭排名直通正赛。",
            "en_summary": "Over 1,000 fencers will compete at AsiaWorld-Expo as Hong Kong hosts the event for the first time.",
            "source_zh": "南华早报",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/sport/hong-kong/article/3361312/hong-kong-fencers-prepare-compete-world-championships-home-soil-first-time",
        },
        {
            "zh_title": "港高院驳回宗馥莉上诉，维持18亿美元资产冻结",
            "en_title": "HK court rejects Zong Fuli appeal, keeps $1.8bn freeze",
            "published": "22:52 2026年7月21日",
            "zh_summary": "娃哈哈争产案中，法院维持对汇丰账户的保全令，宗馥莉五项上诉理由均被驳回。",
            "en_summary": "Hong Kong's High Court upheld an asset preservation order in the Wahaha inheritance dispute.",
            "source_zh": "财新网",
            "source_en": "Caixin",
            "url": "https://companies.caixin.com/2026-07-21/102466825.html",
        },
        {
            "zh_title": "港媒缅怀谢贤：香港电影黄金时代又一巨星陨落",
            "en_title": "Tse's death marks fading of Hong Kong cinema's golden era",
            "published": "13:34 2026年7月21日",
            "zh_summary": "学者指谢贤与吴楚帆等代表战后粤语片新潮流，其离世标志黄金一代巨星几近凋零。",
            "en_summary": "Scholars say Tse embodied post-war Cantonese cinema as another icon of the golden era passes.",
            "source_zh": "南华早报",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3361310/patrick-tses-death-marks-fading-hong-kong-cinemas-golden-era",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "法国议会批准禁止15岁以下使用社交媒体",
            "en_title": "French parliament backs social media ban for under-15s",
            "published": "07:09 2026年7月22日",
            "zh_summary": "国民议会以279票赞成通过法案，马克龙称法国在欧洲率先保护青少年，拟9月起分阶段实施。",
            "en_summary": "France's parliament approved banning social media for children under 15, with rollout from September.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863104-20260722.htm",
        },
        {
            "zh_title": "加拿大评估应对美国关税威胁的各选项",
            "en_title": "Canada evaluating options over US tariff threats",
            "published": "04:28 2026年7月22日",
            "zh_summary": "渥太华正研究包括报复性关税在内的多种回应方案，以应对华盛顿新一轮贸易施压。",
            "en_summary": "Ottawa is weighing options including retaliatory tariffs in response to new US trade pressure.",
            "source_zh": "香港电台",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1863091-20260722.htm",
        },
    ]),
]

def build_html():
    total = sum(len(items) for _, items in CATEGORIES)
    parts = [f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日热点{EDITION_ZH} {EDITION_EN} - {DATE}</title>
</head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BBlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
<tr><td style="background:linear-gradient(135deg,#1a2332 0%,#2c3e6b 100%);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:700;">每日热点{EDITION_ZH}</h1>
<p style="margin:0;color:#a8c4e8;font-size:14px;">{EDITION_EN} · {DATE} · 共 {total} 条</p>
</td></tr>
<tr><td style="padding:20px 24px;background:#f8f9fb;border-bottom:1px solid #e8ecf0;">
<p style="margin:0 0 8px;color:#333;font-size:14px;line-height:1.6;">汇总昨夜至今要闻，涵盖国际局势、市场动态与两岸及香港热点。</p>
<p style="margin:0;color:#666;font-size:13px;line-height:1.5;font-style:italic;">Overnight and early headlines on world affairs, markets, and Greater China developments.</p>
</td></tr>"""]

    num = 1
    for cat_name, items in CATEGORIES:
        parts.append(f"""<tr><td style="padding:16px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f0f4f8;border-left:4px solid #2563eb;font-size:16px;color:#1e3a5f;">{cat_name}</h2>
</td></tr>""")
        for item in items:
            n = f"{num:02d}"
            parts.append(f"""<tr><td style="padding:12px 24px;border-bottom:1px solid #eef1f5;">
<div style="margin-bottom:6px;"><span style="display:inline-block;background:#2563eb;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:4px;margin-right:8px;">{n}</span>
<a href="{item['url']}" style="color:#1a56db;font-size:15px;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a></div>
<p style="margin:4px 0 6px;color:#555;font-size:13px;font-style:italic;line-height:1.4;"><a href="{item['url']}" style="color:#555;text-decoration:none;">{item['en_title']}</a></p>
<p style="margin:0 0 8px;color:#999;font-size:11px;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 4px;color:#333;font-size:13px;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;color:#666;font-size:12px;line-height:1.5;font-style:italic;">{item['en_summary']}</p>
<div style="display:flex;align-items:center;flex-wrap:wrap;gap:8px;">
<span style="background:#e8f0fe;color:#1a56db;font-size:11px;padding:3px 10px;border-radius:12px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="color:#2563eb;font-size:12px;text-decoration:none;">查看全文 Read more →</a>
</div>
</td></tr>""")
            num += 1

    parts.append("""<tr><td style="padding:20px 24px;background:#f8f9fb;border-top:1px solid #e8ecf0;">
<p style="margin:0 0 6px;color:#999;font-size:11px;line-height:1.6;">本简报仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>
<p style="margin:0;color:#999;font-size:11px;line-height:1.5;font-style:italic;">This briefing is for informational purposes only and does not constitute investment or legal advice. All rights belong to original publishers.</p>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>""")
    return "".join(parts), total


def main():
    html, total = build_html()
    assert 20 <= total <= 28, f"Expected 20-28 items, got {total}"
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    path = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated {total} items, HTML length {len(html)}")
    for cat, items in CATEGORIES:
        print(f"  {cat}: {len(items)}")


if __name__ == "__main__":
    main()
