#!/usr/bin/env python3
"""Generate morning briefing email payload for 2026-08-04."""
import json
import os

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中国发布电力五年规划，2030年非化石发电占比拟达50%",
            "en_title": "China targets 50% non-fossil power generation by 2030",
            "published": "22:16 2026年8月3日",
            "zh_summary": "发改委与能源局联合发布2026—2030年电力发展规划，提出2030年非化石能源发电占比达50%。",
            "en_summary": "China's new five-year power plan targets 50% electricity from non-fossil sources by 2030.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260803/b0a626fdd893425fa30882ed2536a266/c.html",
        },
        {
            "zh_title": "广东太平岭核电二号机组投入商业运行",
            "en_title": "Hualong One nuclear unit starts commercial operation in Guangdong",
            "published": "23:48 2026年8月3日",
            "zh_summary": "中广核宣布“华龙一号”二号机组周一投入商业运行，大湾区首个华龙项目一期全面建成。",
            "en_summary": "CGN said a Hualong One reactor began commercial operation, completing phase one of the Taipingling plant.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260803/c3a752dbdf6e4c59b1014e04f1f01175/c.html",
        },
        {
            "zh_title": "中央向陕西调拨6.5万件救灾物资",
            "en_title": "China allocates central disaster relief supplies to Shaanxi",
            "published": "19:39 2026年8月3日",
            "zh_summary": "应急管理部称持续强降雨致陕西多地洪峰，中央调拨帐篷、折叠床等物资支援转移安置。",
            "en_summary": "Beijing dispatched 65,000 relief items to flood-hit Shaanxi as heavy rains triggered dozens of river peaks.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260803/8c5d7ab4971d48038190eeaa7fef6401/c.html",
        },
        {
            "zh_title": "中国启动首批行业“碳效领跑者”评选",
            "en_title": "China launches first carbon-efficiency leaders selection for key industries",
            "published": "18:37 2026年8月3日",
            "zh_summary": "工信部等三部门启动电解铝、水泥、合成氨等五行业“碳效领跑者”遴选，推动工业降碳升级。",
            "en_summary": "Beijing launched its first carbon-efficiency leaders program covering five heavy industries including aluminum and cement.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://english.news.cn/20260803/421b71a523304f47a7a172fb2e85c8ae/c.html",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "阿里巴巴发布迄今最强AI模型Qwen3.8-Max",
            "en_title": "Alibaba unveils its most capable AI model Qwen3.8-Max",
            "published": "11:58 2026年8月3日",
            "zh_summary": "新模型参数量2.4万亿，支持百万token上下文，采用混合专家架构，下周开放模型权重。",
            "en_summary": "Alibaba unveiled Qwen3.8-Max with 2.4 trillion parameters and a one-million-token context window.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://tech.yahoo.com/ai/articles/alibaba-unveils-most-capable-ai-035830076.html",
        },
        {
            "zh_title": "白宫将与OpenAI等商讨AI模型自愿安全测试框架",
            "en_title": "White House to host AI firms on voluntary model-testing framework",
            "published": "00:00 2026年8月3日",
            "zh_summary": "特朗普政府完成自愿网络安全测试框架，OpenAI、Anthropic、谷歌等周二赴白宫讨论细则。",
            "en_summary": "The White House will meet OpenAI, Anthropic, Google and others Tuesday on a voluntary AI safety testing framework.",
            "source_zh": "CNBC", "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html",
            "time_note": "时间未知，已按日期占位",
        },
        {
            "zh_title": "白宫完成AI安全框架但评测基准仍保密",
            "en_title": "White House completes AI framework but keeps benchmarks secret",
            "published": "00:00 2026年8月3日",
            "zh_summary": "美方称已按期完成六月行政令框架，但模型阈值与评测标准不公开，企业担忧事实上的预审门槛。",
            "en_summary": "The White House says its voluntary AI review framework is done, but benchmarks and thresholds remain classified.",
            "source_zh": "The Next Web", "source_en": "The Next Web",
            "url": "https://thenextweb.com/news/white-house-ai-framework-secret-voluntary-classified",
            "time_note": "时间未知，已按日期占位",
        },
        {
            "zh_title": "阿里新模型推动港股科技板块走强",
            "en_title": "Alibaba AI model lifts Hong Kong tech stocks",
            "published": "00:00 2026年8月3日",
            "zh_summary": "恒生指数收涨0.5%，阿里股价涨约7%；内地芯片股受全球AI抛售拖累，科创50指数跌逾3%。",
            "en_summary": "Hong Kong's Hang Seng rose 0.5% as Alibaba jumped 7%, while mainland chip stocks slid on a global AI selloff.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1864816-20260803.htm",
            "time_note": "时间未知，已按日期占位",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "zh_title": "美股周一收涨，道指创历史新高",
            "en_title": "US stocks rally as Dow closes at record high",
            "published": "04:26 2026年8月4日",
            "zh_summary": "油价回落缓解通胀担忧，标普500涨1.5%，道指涨1.3%创新高，纳指涨2.1%，航空股领涨。",
            "en_summary": "US stocks rallied as oil fell; the Dow hit a record and the S&P 500 gained 1.5% on easing inflation fears.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/wall-street-stocks-dow-nasdaq-f8e5f81b45c83878f5b7f69832bb0c95",
        },
        {
            "zh_title": "日美确认联合买入日元并暗示或再干预",
            "en_title": "Japan and US confirm joint yen-buying intervention",
            "published": "00:02 2026年8月4日",
            "zh_summary": "日本财务省称周五与日财政部协同干预，日元升至155附近；双方称不排除采取进一步协调行动。",
            "en_summary": "Tokyo and Washington confirmed coordinated yen-buying and signaled readiness for further joint intervention.",
            "source_zh": "BusinessWorld", "source_en": "BusinessWorld",
            "url": "https://bworldonline.com/banking-finance/2026/08/04/767794/japan-us-confirm-joint-yen-buying-intervention-signal-further-action/",
        },
        {
            "zh_title": "A股收跌，全球AI抛售打击芯片供应链",
            "en_title": "China stocks close down as AI selloff hits chipmakers",
            "published": "16:23 2026年8月3日",
            "zh_summary": "上证综指跌0.59%，科创50跌3.39%；核电、人形机器人板块走强，存储芯片股承压。",
            "en_summary": "Shanghai's benchmark fell 0.59% as a global AI rout hammered semiconductor shares while nuclear stocks rallied.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://hk.marketscreener.com/news/china-stocks-close-down-as-ai-selloff-hammers-chip-supply-chain-ce7f50d8d08dfe23",
        },
        {
            "zh_title": "香港推出全球首个离岸中国国债期货",
            "en_title": "Hong Kong debuts world's first offshore Chinese sovereign bond futures",
            "published": "18:46 2026年8月3日",
            "zh_summary": "港交所五年期离岸国债期货挂牌，证监会主席吴清赴港出席仪式，首日成交3755张合约。",
            "en_summary": "HKEX launched five-year offshore Chinese government bond futures, a new hedging tool for global investors.",
            "source_zh": "财新", "source_en": "Caixin Global",
            "url": "https://www.caixinglobal.com/2026-08-03/hong-kong-debuts-worlds-first-offshore-chinese-sovereign-bond-futures-102470867.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "韩国遭遇史无前例热浪，仰山气温42.5°C",
            "en_title": "South Korea records hottest day on record amid heat wave",
            "published": "00:00 2026年8月3日",
            "zh_summary": "大邱首超40°C，全国至少16人因高温相关疾病死亡，首尔将首次发布最高级别酷暑警报。",
            "en_summary": "South Korea sweltered under record heat as Yangsan hit 42.5C and Seoul prepared its first severe heat warning.",
            "source_zh": "韩联社", "source_en": "Yonhap",
            "url": "https://en.yna.co.kr/view/AEN20260803008152315",
            "time_note": "时间未知，已按日期占位",
        },
        {
            "zh_title": "希腊雅典西部野火复燃，再度下令疏散",
            "en_title": "Greece orders new evacuations as wildfires rage west of Athens",
            "published": "17:26 2026年8月3日",
            "zh_summary": "灭火直升机重返火场，已致5人死亡、逾1.2万公顷过火，普萨塔等地居民再次紧急撤离。",
            "en_summary": "Greece ordered fresh evacuations as wildfires west of Athens burned over 12,000 hectares and killed five.",
            "source_zh": "海峡时报", "source_en": "The Straits Times",
            "url": "https://www.straitstimes.com/world/water-bombers-take-to-skies-as-greece-battles-wildfires",
        },
        {
            "zh_title": "华盛顿州斯波坎山火致约700栋建筑损毁",
            "en_title": "Spokane-area wildfires destroy hundreds of buildings",
            "published": "20:18 2026年8月3日",
            "zh_summary": "周末大火席卷斯波坎周边，约6.7万人疏散；部分居民返回后发现家园仅剩烟囱与焦土。",
            "en_summary": "Wildfires near Spokane destroyed about 700 buildings and forced roughly 67,000 people to evacuate.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/wildfire-spokane-washington-evacuate-8e42b37783bda01e7d004d71e546458e",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "加沙以军空袭致18死，和平方案推进遇阻",
            "en_title": "Israeli strikes kill 18 in Gaza as peace plan stalls",
            "published": "22:00 2026年8月3日",
            "zh_summary": "巴勒斯坦人称特朗普宣扬的解武协议与地面现实脱节；以防长称哈马斯解除武装前不会撤军。",
            "en_summary": "Gazans said Trump's disarmament push jars with reality after Israeli strikes killed 18 in one of the deadliest days.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://theprint.in/world/after-deadly-day-gazans-say-trumps-touting-of-plan-jars-with-grim-reality/3004384/",
        },
        {
            "zh_title": "特朗普称与伊朗谈判是“最后机会”",
            "en_title": "Trump says new Iran talks are 'last chance' for a deal",
            "published": "05:08 2026年8月4日",
            "zh_summary": "特朗普称周日在海湾盟友劝说下叫停对伊大规模打击，周一称新会谈是避免局势升级的最后机会。",
            "en_summary": "Trump called planned US-Iran talks the last chance to avoid escalation after halting major strikes at allies' urging.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/live/trump-news-blanche-iran-updates-08-03-2026",
        },
        {
            "zh_title": "俄称乌无人机袭击黑海海滩致7人死亡",
            "en_title": "Russia says Ukrainian drone attack killed seven at Black Sea resort",
            "published": "18:45 2026年8月3日",
            "zh_summary": "俄南部克拉斯诺达尔官员称凝胶任吉克附近海滩遭袭，含3名儿童在内7人死亡、约40人受伤。",
            "en_summary": "Russia said seven people, including three children, were killed when drone debris hit a crowded Black Sea beach.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.thestar.com.my/news/world/2026/08/03/russia-says-four-people-killed-at-holiday-resort-including-a-child-in-ukrainian-drone-attack",
        },
        {
            "zh_title": "泽连斯基任命乌梅罗夫执掌对外情报总局",
            "en_title": "Zelenskiy names top negotiator Umerov to lead foreign intelligence",
            "published": "20:30 2026年8月3日",
            "zh_summary": "乌总统调整高层人事，首席和谈代表乌梅罗夫转任对外情报局长，仍负责和平谈判与无人机军贸。",
            "en_summary": "President Zelenskiy put chief peace negotiator Rustem Umerov in charge of foreign intelligence while keeping him on talks.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://theprint.in/world/ukraines-top-negotiator-umerov-to-head-foreign-intelligence-service/3004289/",
        },
        {
            "zh_title": "红十字会探访被囚缅甸领导人昂山素季",
            "en_title": "ICRC visits detained Myanmar leader Aung San Suu Kyi",
            "published": "14:55 2026年8月3日",
            "zh_summary": "红十字称按探视标准与昂山素季私下会谈；军方公布照片显示其状态良好，为两年多来首次外界接触。",
            "en_summary": "The ICRC visited Aung San Suu Kyi in private, her first confirmed outside contact in more than two years.",
            "source_zh": "红十字国际委员会", "source_en": "ICRC",
            "url": "https://www.icrc.org/en/statement/myanmar-icrc-visits-daw-aung-san-suu-kyi",
        },
        {
            "zh_title": "25州起诉特朗普政府新一轮关税措施",
            "en_title": "25 states sue Trump administration over new tariffs",
            "published": "04:25 2026年8月4日",
            "zh_summary": "各州指控新关税系规避最高法院二月裁决的“借口”，针对59国及欧盟的强制劳动相关关税。",
            "en_summary": "Twenty-five states sued over new tariffs they call a pretext to replace import taxes struck down by the Supreme Court.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/tariffs-25-supreme-court-import-taxes-120895adbee7ae06157cd5f4bf5c7583",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "母亲误喂大麻糖果致两名儿童入院",
            "en_title": "Mother and aunt held after cannabis sweets sicken children",
            "published": "19:30 2026年8月3日",
            "zh_summary": "旺角东邨一名母亲误将含大麻成分糖果给6岁儿与12岁女食用，女童呕吐、男童一度昏迷送医。",
            "en_summary": "Police arrested a mother and aunt after two children were hospitalized from cannabis-infused sweets in Wong Tai Hom.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362820/hong-kong-mother-aunt-held-after-cannabis-sweets-send-2-children-hospital",
        },
        {
            "zh_title": "九龙城工地安全经理坠楼身亡",
            "en_title": "Construction safety manager dies in 10-floor fall",
            "published": "18:30 2026年8月3日",
            "zh_summary": "39岁男子在沙浦道地盘天台检查时坠至四楼棚架，送医不治；警方按工业意外调查。",
            "en_summary": "A 39-year-old safety manager died after falling about 10 floors at a Kowloon City construction site.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3362813/safety-manager-dies-after-falling-10-floors-hong-kong-construction-site",
        },
        {
            "zh_title": "试管婴儿诊所员工涉瞒报胚胎样本混淆后离港",
            "en_title": "IVF clinic worker fled Hong Kong after embryo mix-up cover-up",
            "published": "17:16 2026年8月3日",
            "zh_summary": "中环Heal Fertility员工被指取样出错后虚假陈述，离港返马来西亚，警方以诈骗案通缉。",
            "en_summary": "Police are hunting a fertility clinic worker who allegedly lied to cover up mixed embryo specimens and fled to Malaysia.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3362798/hong-kong-ivf-clinic-worker-lied-cover-embryo-specimen-mix-flees-city",
        },
        {
            "zh_title": "约500名港生参加解放军驻港部队夏令营",
            "en_title": "500 Hong Kong students join PLA garrison summer camp",
            "published": "23:06 2026年8月3日",
            "zh_summary": "驻港部队年度夏令营开营，学员将进行基础军事训练、专题讲座及文体活动，为期两周。",
            "en_summary": "About 500 Hong Kong students joined the PLA garrison's two-week summer camp for military training and lectures.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/politics/article/3362839/500-hong-kong-students-get-taste-military-life-pla-summer-camp-returns",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "欧洲酷暑干旱加剧，英法希多地遭遇极端天气",
            "en_title": "Europe's hot, dry summer fuels fires in Greece and drought in UK",
            "published": "13:50 2026年8月3日",
            "zh_summary": "希腊直升机相撞后灭火飞机驰援雅典西部山火；英国7月降雨量创近两世纪来最低之一。",
            "en_summary": "A record hot, dry summer tightened its grip on Europe with Greek wildfires and the UK's driest July in nearly 200 years.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/greece-france-wildfires-helicopter-crash-evacuations-65e96b9346f28b32ac00cb7c27129bb4",
        },
        {
            "zh_title": "瑞士称愿向美方提出更有吸引力贸易方案",
            "en_title": "Switzerland ready to make more attractive trade offer to Trump",
            "published": "00:00 2026年8月4日",
            "zh_summary": "瑞联邦委员会称愿在8月7日39%关税生效前继续谈判，回应美方关切以缓解当前关税局面。",
            "en_summary": "Switzerland said it is ready to present a more attractive offer before a 39% US tariff takes effect on August 7.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.reuters.com/world/europe/switzerland-says-its-ready-make-trump-more-attractive-offer-trade-2025-08-04/",
            "time_note": "时间未知，已按日期占位",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c41e3a", "Xinhua": "#c41e3a",
    "路透社": "#ff6600", "Reuters": "#ff6600",
    "美联社": "#0066cc", "AP": "#0066cc",
    "南华早报": "#1a5276", "SCMP": "#1a5276",
    "财新": "#8b0000", "Caixin Global": "#8b0000",
    "CNBC": "#005594",
    "The Next Web": "#34495e",
    "香港电台": "#006400", "RTHK": "#006400",
    "BusinessWorld": "#2c3e50",
    "韩联社": "#003366", "Yonhap": "#003366",
    "海峡时报": "#990000", "The Straits Times": "#990000",
    "红十字国际委员会": "#e74c3c", "ICRC": "#e74c3c",
}


def build_html():
    all_items = []
    for cat_name, items in CATEGORIES:
        for item in items:
            all_items.append((cat_name, item))
    total = len(all_items)

    parts = ['''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>每日热点早报 Morning Briefing - 2026-08-04</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;box-shadow:0 4px 24px rgba(0,0,0,.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:700;">每日热点早报</h1>
<p style="margin:0 0 4px;color:#a8d8ff;font-size:14px;">Morning News Briefing · 2026年8月4日</p>
<p style="margin:0;color:#8899aa;font-size:13px;">共 ''' + str(total) + ''' 条</p>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafbfc;border-bottom:1px solid #e8eaed;">
<p style="margin:0 0 8px;color:#333;font-size:14px;line-height:1.6;">昨夜至今，全球政经、科技与社会热点一览。</p>
<p style="margin:0;color:#666;font-size:13px;line-height:1.5;font-style:italic;">Overnight and early headlines from around the world.</p>
</td></tr>''']

    num = 0
    current_cat = None
    for cat_name, item in all_items:
        if cat_name != current_cat:
            current_cat = cat_name
            zh_cat, en_cat = cat_name.split(" ", 1)
            parts.append(f'''<tr><td style="padding:20px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f5f6f8;border-left:4px solid #1a73e8;font-size:16px;color:#1a1a2e;border-radius:0 6px 6px 0;">
{zh_cat} <span style="color:#666;font-weight:400;font-size:14px;">{en_cat}</span>
</h2></td></tr>''')
        num += 1
        n = f"{num:02d}"
        color = SOURCE_COLORS.get(item["source_zh"], SOURCE_COLORS.get(item["source_en"], "#555"))
        parts.append(f'''<tr><td style="padding:12px 24px;border-bottom:1px solid #f0f0f0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td style="width:36px;vertical-align:top;padding-right:10px;">
<span style="display:inline-block;background:#1a73e8;color:#fff;font-size:12px;font-weight:700;padding:4px 8px;border-radius:4px;">{n}</span>
</td>
<td style="vertical-align:top;">
<a href="{item['url']}" style="color:#1a1a2e;font-size:15px;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a>
<p style="margin:4px 0 2px;color:#555;font-size:13px;font-style:italic;line-height:1.4;">{item['en_title']}</p>
<p style="margin:0 0 8px;color:#999;font-size:11px;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 4px;color:#444;font-size:13px;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;color:#666;font-size:12px;line-height:1.5;font-style:italic;">{item['en_summary']}</p>
<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:6px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="color:#1a73e8;font-size:12px;text-decoration:none;">查看全文 Read more →</a>
</td></tr></table></td></tr>''')

    parts.append('''<tr><td style="padding:20px 24px;background:#f8f9fa;border-top:1px solid #e8eaed;">
<p style="margin:0 0 6px;color:#888;font-size:11px;line-height:1.6;">本简报由自动化系统汇编，仅供参考，不构成投资建议。新闻版权归原媒体所有。</p>
<p style="margin:0;color:#aaa;font-size:10px;line-height:1.5;font-style:italic;">This briefing is automatically compiled for reference only and does not constitute investment advice. All rights belong to original publishers.</p>
</td></tr>
</table></td></tr></table></body></html>''')
    return "".join(parts)


def main():
    html = build_html()
    payload = {
        "subject": "每日热点早报 Morning Briefing - 2026-08-04",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated email_payload.json: {len(html)} chars, {sum(len(v) for _, v in CATEGORIES)} items")


if __name__ == "__main__":
    main()
