#!/usr/bin/env python3
"""Build evening briefing HTML and email_payload.json for 2026-08-15."""
import json
import os

BRIEFING_EDITION = "晚报"
DATE_STR = "2026-08-15"
DATE_CN = "2026年8月15日"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE_STR}"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "生态环境法典今日正式施行，我国环保法治迈入新阶段",
            "en_title": "China's Ecological and Environmental Code Takes Effect Today",
            "published": "00:00 2026年8月15日",
            "zh_summary": "继民法典后第二部以法典命名的法律今日施行，共5编1242条，整合30余部生态环境法律。",
            "en_summary": "China's second code-named law after the Civil Code takes effect with 1,242 articles integrating 30-plus environmental statutes.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www.cs.com.cn/xwzx/01/2026/08/15/detail_2026081510031563.html",
        },
        {
            "zh_title": "央行外汇局推跨境资金集中运营全国试点，门槛降至一体化资金池十分之一",
            "en_title": "PBOC Expands Cross-Border Treasury Pooling Nationwide at Lower Thresholds",
            "published": "12:06 2026年8月15日",
            "zh_summary": "新规9月14日起施行，支持更多中小跨国公司本外币资金归集调剂，自贸区主办企业门槛可再降。",
            "en_summary": "New rules effective Sept 14 let more mid-sized multinationals pool FX funds; FTZ hosts may qualify at even lower thresholds.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-08-15/102474412.html",
        },
        {
            "zh_title": "外交部强烈谴责日本政要参拜靖国神社，已提出严正交涉",
            "en_title": "China Condemns Japanese Officials' Yasukuni Shrine Visits",
            "published": "15:10 2026年8月15日",
            "zh_summary": "高市早苗供奉祭祀费，多名阁僚参拜。中方称此举为战犯翻案、再军事化铺路，已向日方严正抗议。",
            "en_summary": "Beijing protested shrine visits and offerings on Japan's surrender anniversary, calling them efforts to whitewash war criminals.",
            "source_zh": "人民网", "source_en": "People's Daily",
            "url": "http://world.people.com.cn/n1/2026/0815/c1002-40780167.html",
        },
        {
            "zh_title": "日本战败81周年，防卫大臣等阁僚参拜靖国神社引和平人士反对",
            "en_title": "Japanese Ministers Visit Yasukuni on 81st Surrender Anniversary",
            "published": "11:11 2026年8月15日",
            "zh_summary": "高市以自民党总裁身份供奉玉串料，防卫大臣小泉进次郎等4名阁僚参拜，日本国内爱好和平人士强烈反对。",
            "en_summary": "Four cabinet ministers visited Yasukuni as the PM sent an offering; Japanese peace advocates strongly condemned the moves.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://intl.ce.cn/qqss/202608/t20260815_3149176.shtml",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "苹果与阿里合作训练中国市场专属大模型，拟数月内推出Apple Intelligence",
            "en_title": "Apple Trains China-Specific AI Model With Alibaba Support",
            "published": "17:21 2026年8月14日",
            "zh_summary": "路透称苹果首次自训在华大模型，已获网信办注册，将与阿里通义千问等整合，拟经iOS更新在华上线。",
            "en_summary": "Reuters says Apple trained a China-only LLM with Alibaba, cleared regulators, and plans an iOS rollout within months.",
            "source_zh": "The Verge", "source_en": "The Verge",
            "url": "https://www.theverge.com/ai-artificial-intelligence/980160/apple-intelligence-china-custom-ai-model-alibaba",
        },
        {
            "zh_title": "Anthropic详解Claude文本水印机制，以符合欧盟AI法案透明度要求",
            "en_title": "Anthropic Explains Claude Text Watermarking for EU AI Act Compliance",
            "published": "00:00 2026年8月15日",
            "zh_summary": "水印通过微调无关紧要用词实现，不影响质量与成本；公司计划推出第三方检测API，全球同步上线。",
            "en_summary": "Anthropic says watermarking tweaks low-stakes word choices without hurting quality and plans a third-party detection API.",
            "source_zh": "The Register", "source_en": "The Register",
            "url": "https://www.theregister.com/ai-and-ml/2026/08/15/anthropic-says-text-watermarking-scheme-relies-on-inconsequential-words/5288156",
        },
        {
            "zh_title": "美国拟要求伙伴国在AI阵营中选边，否则将被排除在Pax Silica联盟外",
            "en_title": "US to Press Allies to Pick Sides in AI Race With China",
            "published": "13:45 2026年8月15日",
            "zh_summary": "国务院草拟信函警告35个签署国，同时参与北京主导的AI倡议将与美方供应链合作相冲突，须明确抉择。",
            "en_summary": "A draft State Department letter warns 35 signatories that rival AI frameworks conflict with the US-led Pax Silica coalition.",
            "source_zh": "路透", "source_en": "Reuters",
            "url": "https://www.rappler.com/world/us-canada/us-china-ai-pick-sides-state-department-letter/",
        },
        {
            "zh_title": "Anthropic将推水印检测API，第三方可识别Claude生成文本",
            "en_title": "Anthropic to Offer Watermark Detection API for Claude-Generated Text",
            "published": "00:00 2026年8月14日",
            "zh_summary": "采用谷歌DeepMind SynthID-Text变体，轻量编辑难以去除；因暂无法按地区限制，水印将全球同步部署。",
            "en_summary": "Using a SynthID-Text variant, Anthropic will roll out watermarking globally and offer detection tools to third parties.",
            "source_zh": "The Decoder", "source_en": "The Decoder",
            "url": "https://the-decoder.com/anthropic-announces-watermark-detection-api-that-will-let-third-parties-detect-claudes-ai-texts/",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "摊余成本法债基重启，15家中小公募集中上报63个月封闭产品",
            "en_title": "Amortized-Cost Bond Funds Reopen for 15 Mid-Sized Fund Houses",
            "published": "14:13 2026年8月15日",
            "zh_summary": "证监会网站显示15家公募同日申报63个月封闭式债基，为支持中小基金公司差异化发展的实质举措。",
            "en_summary": "Fifteen fund managers filed 63-month closed bond funds after regulators reopened amortized-cost products for smaller houses.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-08-15/102474476.html",
        },
        {
            "zh_title": "美国7月零售销售意外下滑0.6%，创逾一年来最大降幅",
            "en_title": "US July Retail Sales Fall 0.6% in Biggest Drop in Over a Year",
            "published": "20:41 2026年8月14日",
            "zh_summary": "商务部数据显示消费在Prime Day后回落，汽车与网购领跌；经济学家担忧增长放缓与通胀并存风险。",
            "en_summary": "Commerce Department data showed a 0.6% July drop as auto and online sales cooled after Prime Day spending.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://abcnews.com/Business/wireStory/us-retail-sales-unexpectedly-post-largest-drop-year-135639388",
        },
        {
            "zh_title": "华尔街周五收跌，弱零售数据与油价上涨压制股指",
            "en_title": "Wall Street Slips on Weak Retail Data and Rising Oil Prices",
            "published": "05:00 2026年8月15日",
            "zh_summary": "标普500跌0.2%至7785.76点，仍录得第三周连涨；10年期美债收益率升至4.69%，市场担忧滞胀风险。",
            "en_summary": "The S&P 500 fell 0.2% despite a third winning week as weak retail sales and higher oil fed stagflation worries.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://www.newser.com/article/5d9870d6c5ae735f9b74bf4ceefaa3ec/wall-street-slips-from-its-record-following-the-latest-weak-update-on-the-us-economy.html",
        },
        {
            "zh_title": "霍尔木兹僵局推升油价，布伦特原油周五涨近1.7%",
            "en_title": "Hormuz Standoff Pushes Brent Crude Up Nearly 1.7% on Friday",
            "published": "18:47 2026年8月15日",
            "zh_summary": "美伊就海峡控制权互不让步，特朗普称愿接受更高油价；周五仅两艘船通过海峡，未见原油运输。",
            "en_summary": "Brent rose as US-Iran tensions kept Hormuz traffic near a halt and Trump defended higher fuel costs at home.",
            "source_zh": "CNBC", "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/15/iran-rebuffs-trumps-claim-over-hormuz-amid-report-of-ship-strike.html",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "日本千叶创纪录暴雨致8人死亡，逾7000人滞留成田机场",
            "en_title": "Record Rain in Japan's Chiba Kills Eight, Strands Thousands at Narita",
            "published": "13:30 2026年8月15日",
            "zh_summary": "24小时降雨超360毫米创当地纪录，逾2万户停电；气象厅首次发布新版最高级别暴雨与滑坡预警。",
            "en_summary": "More than 360mm of rain in 24 hours killed eight and left about 7,000 travelers stranded at Narita Airport.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.rappler.com/world/asia-pacific/japan-record-rain-chiba-flooding-narita-airport-august-2026/",
        },
        {
            "zh_title": "印尼弗洛勒斯岛7.7级地震致至少47人死亡，海啸预警随后解除",
            "en_title": "Magnitude 7.7 Indonesia Quake Kills at Least 47 as Tsunami Alert Lifted",
            "published": "04:58 2026年8月15日",
            "zh_summary": "浅源地震凌晨袭击弗洛勒斯岛，150余栋房屋严重受损，逾2000人疏散；救援在余震与滑坡中持续。",
            "en_summary": "A shallow pre-dawn quake on Flores killed at least 47, damaged 150-plus homes and forced about 2,000 evacuations.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c5y0zz63gero",
        },
        {
            "zh_title": "法国宪法委员会否决15岁以下社交媒体禁令",
            "en_title": "France's Top Court Blocks Social Media Ban for Under-15s",
            "published": "23:09 2026年8月14日",
            "zh_summary": "法院认定禁令过度限制未成年人表达自由且年龄验证缺乏隐私保障；马克龙要求尽快起草新法案，目标2027年春。",
            "en_summary": "The Constitutional Council struck down the ban as disproportionate; Macron asked for a revised draft by spring 2027.",
            "source_zh": "France24", "source_en": "France24",
            "url": "https://www.france24.com/en/live-news/20260814-france-upholds-assisted-dying-law-strikes-down-social-media-ban-for-children",
        },
        {
            "zh_title": "弗吉尼亚州立大学枪击致5人受伤，1人伤势危重",
            "en_title": "Five Injured, One Critical, in Virginia State University Shooting",
            "published": "13:28 2026年8月15日",
            "zh_summary": "周六凌晨宿舍区发生枪击，警方称涉及多名嫌疑人；校园临时封锁已解除，切斯特菲尔德县警局牵头调查。",
            "en_summary": "Five people were shot outside residence halls early Saturday; campus lockdown was lifted as police hunt multiple suspects.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c0l5583903yo",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "伊朗驳斥特朗普将霍尔木兹海峡宣布为美国领土的言论",
            "en_title": "Iran Rejects Trump's Claim to Declare Hormuz US Territory",
            "published": "18:47 2026年8月15日",
            "zh_summary": "副外长称海峡开放关闭由伊朗掌控；外长阿拉格齐称暂无恢复与美谈判决定，仅卡塔尔巴基斯坦在传递信息。",
            "en_summary": "Tehran rejected Trump's Hormuz claim and said no US talks are underway, only mediator messaging via Qatar and Pakistan.",
            "source_zh": "NBC News", "source_en": "NBC News",
            "url": "https://www.nbcnews.com/world/iran/iran-rejects-delusions-trump-strait-hormuz-us-territory-rcna592666",
        },
        {
            "zh_title": "以色列空袭黎巴嫩南部致11人死亡，为6月停火以来最致命袭击",
            "en_title": "Israeli Strikes on Southern Lebanon Kill 11 in Deadliest Attack Since Truce",
            "published": "00:00 2026年8月15日",
            "zh_summary": "以军称回应真主党威胁，空袭安萨尔和代尔扎赫拉尼等地；黎总理谴责以方恐吓平民、破坏稳定南部局势努力。",
            "en_summary": "Israel said it hit Hezbollah infrastructure; Lebanon called the strikes the deadliest since June's fragile ceasefire.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/southern-lebanon-israel-strike-hezbollah-iran-ansar-1124fd2bd0b7ed76b0e97683dddbcaad",
        },
        {
            "zh_title": "韩国总统李在明提议与朝鲜正式结束战争状态",
            "en_title": "South Korea Proposes Talks to Formally End War With North",
            "published": "00:00 2026年8月15日",
            "zh_summary": "光复节讲话中，李在明提议建立多层安全机制并讨论遏制朝核；平壤尚未回应，周二刚试射弹道导弹。",
            "en_summary": "On Liberation Day, President Lee proposed talks on ending the war and curbing nuclear advances; Pyongyang has not replied.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c8en2z9jp2xo",
        },
        {
            "zh_title": "乌克兰远程打击俄罗斯萨马拉工业设施，泽连斯基称使用火烈鸟导弹",
            "en_title": "Ukraine Strikes Samara Industrial Site With Long-Range Flamingo Missiles",
            "published": "19:57 2026年8月15日",
            "zh_summary": "乌方称击中俄航天相关企业及萨维什利亚卡空军基地；俄方称在19个地区击落598架无人机。",
            "en_summary": "Kyiv said it hit a Roscosmos-linked site and an air base; Moscow reported downing 598 drones across 19 regions.",
            "source_zh": "NBC News", "source_en": "NBC News",
            "url": "https://www.nbcnews.com/world/ukraine/ukraine-attacks-russias-samara-industrial-site-rcna592668",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "玛丽医院新临床大楼24部电梯故障，承建商被暂停投标资格",
            "en_title": "Queen Mary Hospital Lift Defects Suspend Contractors From Tenders",
            "published": "14:40 2026年8月15日",
            "zh_summary": "建筑署称28部新电梯中24部存在严重缺陷，临床服务延期；承建商须承担整改费用并可能被追讨损失。",
            "en_summary": "Authorities suspended contractors after 24 of 28 new lifts failed, delaying the HK$15.15 billion clinical block opening.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3364137/contractors-suspended-over-extremely-serious-queen-mary-hospital-lift-defects",
        },
        {
            "zh_title": "上半年个人资料投诉同比激增62%，私隐专员吁网购谨慎分享信息",
            "en_title": "Hong Kong Privacy Complaints Jump 62% in First Half of 2026",
            "published": "13:50 2026年8月15日",
            "zh_summary": "私隐公署上半年接获2990宗投诉，资讯科技业占867宗最多；专员称AI时代数据可被快速大规模收集利用。",
            "en_summary": "The privacy watchdog logged 2,990 complaints in H1 2026, with IT cases leading as AI accelerates data collection.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3364134/extreme-caution-urged-hongkongers-data-privacy-complaints-jump-62-ai-era",
        },
        {
            "zh_title": "新学年教科书均价涨至4000至6000港元，家长呼吁恢复学生津贴",
            "en_title": "Hong Kong Textbook Prices Hit Highest Level Since 2020 Pandemic",
            "published": "18:45 2026年8月15日",
            "zh_summary": "教育局书单显示2026-27学年均价涨3.6%，仅两成书名冻结加价；数字教材普及与印量减少推升纸书成本。",
            "en_summary": "Textbook lists now average HK$4,000-6,000 as digital shift squeezes print runs and families seek restored subsidies.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/education/article/3364138/struggling-families-urge-return-student-grant-after-textbook-prices-jump",
        },
        {
            "zh_title": "商界提交五年规划建议，强调北都、金融枢纽与AI战略",
            "en_title": "Hong Kong Chambers Urge Northern Metropolis and AI in Five-Year Plan",
            "published": "18:57 2026年8月15日",
            "zh_summary": "美商会及工总等提交意见，公众咨询周五结束，共收逾1.6万份意见；蓝图预计9月公布，对接国家十五五规划。",
            "en_summary": "AmCham and FHKI backed the Northern Metropolis and AI strategy as public consultation closed with 16,000 submissions.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3364149/northern-metropolis-and-ai-vital-hong-kongs-5-year-plan-business-chambers",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "克罗地亚沿海野火致1死、逾千人疏散，总理称火势蔓延极快",
            "en_title": "Croatia Coastal Wildfire Kills One and Evacuates Over 1,200",
            "published": "00:00 2026年8月15日",
            "zh_summary": "周四晚洛克拉戈日尼察起火后迅速逼近奥米什，强风四小时内烧毁约1000公顷；逾40人受伤，10人重症监护。",
            "en_summary": "A fast-moving blaze near Omis killed one, injured about 40 and forced more than 1,200 evacuations overnight.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c9342wn2x27o",
        },
        {
            "zh_title": "法国父子三人苏梅岛海上漂流16小时获救",
            "en_title": "French Family Rescued After 16 Hours Adrift Off Koh Samui",
            "published": "11:00 2026年8月14日",
            "zh_summary": "摩托艇引擎故障后一家三口在风浪中过夜，次日上午约10时被搜救队发现，送医检查后已继续度假行程。",
            "en_summary": "A father and two sons survived overnight at sea after their jet ski failed; rescuers found them near Koh Samui Friday morning.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cy0j60p0d29o",
        },
        {
            "zh_title": "胡塞武装袭击沙特石油设施及也门摩卡港，造成平民伤亡",
            "en_title": "Houthis Strike Saudi Oil Site and Yemen's Mocha Port",
            "published": "08:27 2026年8月15日",
            "zh_summary": "胡塞称无人机击中沙特奈季兰阿美设施并向摩卡港发射弹道导弹；也门政府称5枚导弹击中港口致4名平民死亡。",
            "en_summary": "The Houthis hit a Saudi Aramco site and fired missiles at Mocha port; Yemen's government reported four civilian deaths.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://intl.ce.cn/qqss/202608/t20260815_3149033.shtml",
        },
        {
            "zh_title": "林肯号航母海上部署超250天，补给与士气问题引美国议员关注",
            "en_title": "USS Abraham Lincoln's 250-Day Deployment Raises Supply and Morale Alarms",
            "published": "00:00 2026年8月13日",
            "zh_summary": "舰员家属反映食物短缺、卫浴故障与邮件延误；海军称战区补给受阻，乔治·华盛顿号正前往中东接替部署。",
            "en_summary": "Lawmakers pressed the Pentagon over shortages aboard the carrier after 250 days at sea supporting Iran war operations.",
            "source_zh": "PBS", "source_en": "PBS News",
            "url": "https://www.pbs.org/newshour/world/new-aircraft-carrier-en-route-to-middle-east-after-issues-reported-aboard-uss-abraham-lincoln",
        },
    ]),
]

SOURCE_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b", "财新": "#8e44ad", "Caixin": "#8e44ad",
    "人民网": "#c0392b", "People's Daily": "#c0392b", "The Verge": "#16a085",
    "The Register": "#2c3e50", "路透": "#2980b9", "Reuters": "#2980b9",
    "The Decoder": "#7f8c8d", "美联社": "#e67e22", "AP": "#e67e22",
    "CNBC": "#27ae60", "BBC": "#c0392b", "NBC News": "#e74c3c",
    "南华早报": "#d35400", "SCMP": "#d35400",
    "France24": "#3498db", "PBS": "#1a5276", "PBS News": "#1a5276",
}


def build_html():
    items = []
    for cat_name, cat_items in CATEGORIES:
        for item in cat_items:
            items.append((cat_name, item))
    total = len(items)

    parts = [f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>每日热点晚报 - {DATE_STR}</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">
<div style="color:#fff;font-size:22px;font-weight:700;letter-spacing:1px;">每日热点晚报</div>
<div style="color:#a8b2d1;font-size:13px;margin-top:6px;">Evening News Briefing · {DATE_CN} · 共 {total} 条</div>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafbfc;border-bottom:1px solid #eee;">
<p style="margin:0 0 8px;font-size:14px;color:#333;line-height:1.6;">汇总今日全日要闻，涵盖政策、市场、科技与社会热点。</p>
<p style="margin:0;font-size:13px;color:#666;line-height:1.5;font-style:italic;">Today's main stories across policy, markets, technology and society.</p>
</td></tr>"""]

    global_idx = 0
    current_cat = None
    for cat_name, item in items:
        if cat_name != current_cat:
            current_cat = cat_name
            zh_cat, en_cat = cat_name.split(" ", 1) if " " in cat_name else (cat_name, "")
            parts.append(f"""<tr><td style="padding:20px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f4f6f8;border-left:4px solid #2563eb;font-size:15px;color:#1a1a2e;border-radius:0 6px 6px 0;">
{zh_cat} <span style="font-weight:400;color:#666;font-size:13px;">{en_cat}</span>
</h2></td></tr>""")
        global_idx += 1
        num = f"{global_idx:02d}"
        color = SOURCE_COLORS.get(item["source_zh"], SOURCE_COLORS.get(item["source_en"], "#666"))
        parts.append(f"""<tr><td style="padding:12px 24px 16px;border-bottom:1px solid #f0f0f0;">
<div style="font-size:11px;color:#2563eb;font-weight:700;margin-bottom:4px;">{num}</div>
<a href="{item['url']}" style="font-size:15px;color:#1a1a2e;text-decoration:none;font-weight:600;line-height:1.4;">{item['zh_title']}</a>
<div style="font-size:13px;color:#555;font-style:italic;margin-top:4px;line-height:1.4;">{item['en_title']}</div>
<div style="font-size:11px;color:#999;margin-top:4px;">发布时间 Published: {item['published']}</div>
<p style="font-size:13px;color:#444;margin:8px 0 4px;line-height:1.6;">{item['zh_summary']}</p>
<p style="font-size:12px;color:#666;margin:0 0 10px;line-height:1.5;font-style:italic;">{item['en_summary']}</p>
<span style="display:inline-block;background:{color};color:#fff;font-size:10px;padding:2px 8px;border-radius:10px;margin-right:6px;">{item['source_zh']} · {item['source_en']}</span>
<a href="{item['url']}" style="font-size:11px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</td></tr>""")

    parts.append("""<tr><td style="padding:20px 24px;background:#f8f9fa;border-top:1px solid #eee;">
<p style="margin:0 0 6px;font-size:11px;color:#999;line-height:1.5;">本简报仅供参考，内容由 AI 从公开来源整理，不构成投资或法律建议。如有疏漏请以原文为准。</p>
<p style="margin:0;font-size:11px;color:#999;line-height:1.5;font-style:italic;">This briefing is for reference only, compiled by AI from public sources. Not investment or legal advice. Refer to original articles for details.</p>
</td></tr>
</table></td></tr></table></body></html>""")
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
    print(f"Total items: {total}")
    print(f"HTML length: {len(html)}")
    print(f"Written to {out}")


if __name__ == "__main__":
    main()
