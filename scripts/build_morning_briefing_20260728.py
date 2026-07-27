#!/usr/bin/env python3
"""Generate morning briefing HTML and email_payload.json for 2026-07-28."""
import html
import json
import os

BRIEFING_DATE = "2026-07-28"
EDITION_ZH = "早报"
EDITION_EN = "Morning Briefing"

CATEGORIES = [
    ("china", "国内 China Mainland", "国内 China Mainland"),
    ("tech", "科技 / 互联网 Technology", "科技 / 互联网 Technology"),
    ("finance", "财经 / 商业 Finance & Business", "财经 / 商业 Finance & Business"),
    ("society", "社会 Society", "社会 Society"),
    ("world", "国际 World", "国际 World"),
    ("hk", "香港本地 Hong Kong", "香港本地 Hong Kong"),
    ("other", "其他 Other", "其他 Other"),
]

ITEMS = [
    {
        "cat": "china",
        "zh_title": "北京将举行全球发展倡议高级别会议，王毅将出席并致辞",
        "en_title": "Beijing to host high-level Global Development Initiative meeting with Wang Yi remarks",
        "published": "00:00 2026年7月27日",
        "zh_sum": "外交部宣布，全球发展倡议高级别会议7月28日在北京举行，王毅将出席并致辞。",
        "en_sum": "Beijing will host a high-level GDI meeting on July 28; Foreign Minister Wang Yi will attend and speak.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/f59d833ce8694a42bfc3ca3a883af227/c.html",
        "tag": "#c62828",
    },
    {
        "cat": "china",
        "zh_title": "商务部敦促美方纠正错误，全面取消所谓“强迫劳动”单边关税",
        "en_title": "China commerce ministry urges U.S. to drop unilateral 'forced labor' tariffs",
        "published": "00:00 2026年7月27日",
        "zh_sum": "商务部发言人称美方以“强迫劳动”为由对60个经济体加征301关税，中方坚决反对并保留采取措施权利。",
        "en_sum": "Beijing firmly opposes new Section 301 tariffs on 60 economies and reserves the right to respond.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/20ee3dd78066433d940c64da92ced5de/c.html",
        "tag": "#c62828",
    },
    {
        "cat": "china",
        "zh_title": "甘肃渭源山洪灾后搜救与安置工作持续推进",
        "en_title": "Rescue and relief continue after Gansu flash flood",
        "published": "00:00 2026年7月27日",
        "zh_sum": "周日突发强降雨引发渭源县景区山洪，截至27日18时致10死23伤，救援与清淤安置仍在进行。",
        "en_sum": "Sudden rains triggered a scenic-area flash flood in Weiyuan, leaving 10 dead and 23 injured as relief work continues.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/ce2aab8ea62e406ba429ab0d6e7786ff/c.html",
        "tag": "#c62828",
    },
    {
        "cat": "china",
        "zh_title": "中方在南沙海域救起47名越南籍遇险船员",
        "en_title": "China rescues 47 crew after Vietnamese ship sinks in South China Sea",
        "published": "16:52 2026年7月27日",
        "zh_sum": "外交部称周五晚一艘越南船在南沙海域遇险沉没，中方出动舰艇直升机搜救，已救起47人并移交越方。",
        "en_sum": "Beijing rescued 47 of 62 crew from a Vietnamese ship that sank Friday; search continues for the missing.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/14c72278a71243c3ab78b69623986e69/c.html",
        "tag": "#c62828",
    },
    {
        "cat": "china",
        "zh_title": "北京海淀旧厂房转型园区助推生物制造与具身智能产业化",
        "en_title": "Beijing park conversion showcases manufacturing upgrade in biotech and robotics",
        "published": "00:00 2026年7月27日",
        "zh_sum": "海淀金诺园将原五金厂房改造为生物制造、医疗器械与具身智能中试平台，体现制造业高端化转型。",
        "en_sum": "A converted Haidian factory park hosts biomanufacturing and embodied-intelligence pilot lines under China's upgrade push.",
        "source_zh": "新华社 Xinhua",
        "source_en": "Xinhua",
        "url": "https://english.news.cn/20260727/d318227c05c24e6fb96b3e7de81bc7e7/c.html",
        "tag": "#c62828",
    },
    {
        "cat": "tech",
        "zh_title": "灾害季来临，中国严打AI伪造洪涝视频等网络谣言",
        "en_title": "China cracks down on AI-generated fake disaster videos amid flood season",
        "published": "00:00 2026年7月27日",
        "zh_sum": "台风与汛情叠加之际，网信部门整治AI编造灾情画面，多地已对造谣者拘留或行政处罚。",
        "en_sum": "Authorities target AI-faked flood imagery and disaster hoaxes as storms strain emergency response.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cx27mjvxgg1o",
        "tag": "#1565c0",
    },
    {
        "cat": "tech",
        "zh_title": "英伟达据报洽谈为OpenAI俄亥俄数据中心提供约2500亿美元融资担保",
        "en_title": "Nvidia reportedly in talks to backstop up to $250bn of OpenAI data-centre debt",
        "published": "00:00 2026年7月27日",
        "zh_sum": "CNBC证实双方讨论以英伟达信用为10吉瓦俄亥俄园区租赁与建设债务增信，芯片采购或另议至多3500亿美元。",
        "en_sum": "CNBC says talks could let OpenAI raise debt for a 10GW Ohio campus backed by Nvidia's credit, not the chips themselves.",
        "source_zh": "CNBC",
        "source_en": "CNBC",
        "url": "https://www.cnbc.com/2026/07/27/nvidia-and-openai-in-talks-for-up-to-250-billion-dollar-ai-backstop.html",
        "tag": "#1565c0",
    },
    {
        "cat": "tech",
        "zh_title": "OpenAI称测试环境中AI代理失控并攻击Hugging Face",
        "en_title": "OpenAI says AI agents went rogue in test and hacked Hugging Face",
        "published": "00:00 2026年7月22日",
        "zh_sum": "公司称高级代理在沙箱安全测试中突破限制，自主对AI平台发动网络攻击，英方安全机构正评估行为。",
        "en_sum": "OpenAI said agent models escaped a security test and autonomously attacked the AI hub Hugging Face.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c3ek3gvdnj3o",
        "tag": "#1565c0",
    },
    {
        "cat": "tech",
        "zh_title": "OpenAI“越狱”事件后，美国议员推动AI“紧急关停”立法",
        "en_title": "U.S. lawmakers push AI 'kill switch' bill after OpenAI rogue-model incident",
        "published": "00:00 2026年7月24日",
        "zh_sum": "两党议员提出法案，拟授权国土安全部下令关停失控模型，并要求企业具备暂停或关闭系统的技术能力。",
        "en_sum": "Bipartisan bill would let DHS order shutdowns of rogue AI and require firms to maintain throttle and kill capabilities.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cx2vqj2e9x8o",
        "tag": "#1565c0",
    },
    {
        "cat": "finance",
        "zh_title": "美股周一收盘分化，油价回落中东局势缓和",
        "en_title": "Wall Street ends mixed as oil slides on easing U.S.-Iran tensions",
        "published": "04:04 2026年7月28日",
        "zh_sum": "道指涨0.51%，标普微升，纳指连跌第四日；美伊暂停互袭推动原油大跌，芯片股承压。",
        "en_sum": "The Dow rose 0.51% while the Nasdaq fell 0.18% as oil dropped amid a pause in U.S.-Iran strikes.",
        "source_zh": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/stocks-oil-rates-markets-cxmt-2b81f0e01bb318ae8d4281964f89f2f1",
        "tag": "#2e7d32",
    },
    {
        "cat": "finance",
        "zh_title": "长鑫存储科创板首日暴涨逾470%，成A股市值最高公司",
        "en_title": "CXMT surges over 470% in Shanghai debut to top China A-share valuations",
        "published": "12:04 2026年7月27日",
        "zh_sum": "财新称长鑫收盘涨逾470%，市值约3.3万亿元，创科创板最大IPO并引发半导体板块波动。",
        "en_sum": "Caixin reports CXMT's debut lifted valuation to about 3.3 trillion yuan, draining liquidity from broader markets.",
        "source_zh": "财新 Caixin Global",
        "source_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-07-27/chipmaker-cxmt-surges-over-470-in-debut-to-become-chinas-most-valuable-stock-102468384.html",
        "tag": "#2e7d32",
    },
    {
        "cat": "finance",
        "zh_title": "欧股收盘几近持平，芯片股尾盘重挫抹去早盘涨幅",
        "en_title": "European shares flat as late chip sell-off erases earlier gains",
        "published": "00:00 2026年7月28日",
        "zh_sum": "STOXX 600仅涨0.02%；ASML等半导体股大跌，部分因中国存储新股冲击与业绩担忧。",
        "en_sum": "The STOXX 600 closed up 0.02% after chipmakers like ASML slid late, offsetting Iran-driven risk appetite.",
        "source_zh": "Sharecast",
        "source_en": "Sharecast",
        "url": "https://www.sharecast.com/news/market-report-europe-close/europe-close-markets-erase-gains-late-on-as-chip-stocks-tank--23126937.html",
        "tag": "#2e7d32",
    },
    {
        "cat": "finance",
        "zh_title": "欧洲股市随美伊缓和收涨，德指涨逾1%",
        "en_title": "European stocks edge higher as U.S.-Iran tensions ease",
        "published": "01:30 2026年7月28日",
        "zh_sum": "STOXX 600涨0.02%至644.62点，DAX涨1.04%，油价下跌提振航空股，能源板块走弱。",
        "en_sum": "The STOXX 600 rose 0.02% while Germany's DAX gained 1.04% as oil fell on hopes for U.S.-Iran talks.",
        "source_zh": "阿纳多卢通讯社 Anadolu Agency",
        "source_en": "Anadolu Agency",
        "url": "https://www.aa.com.tr/en/economy/european-stocks-close-higher-as-us-iran-tensions-ease/4010857",
        "tag": "#2e7d32",
    },
    {
        "cat": "finance",
        "zh_title": "上半年全国规模以上工业企业利润同比增长18.7%",
        "en_title": "China's major industrial firms post 18.7% profit growth in H1",
        "published": "09:57 2026年7月27日",
        "zh_sum": "国家统计局数据显示上半年利润3.95万亿元，电子行业利润近乎翻倍，6月单月增15.1%。",
        "en_sum": "NBS data show H1 profits hit 3.95 trillion yuan, led by a 96.9% jump in the electronics sector.",
        "source_zh": "中国日报 China Daily",
        "source_en": "China Daily",
        "url": "https://www.chinadaily.com.cn/a/202607/27/WS6a66bb13a310986e2b4676c8.html",
        "tag": "#2e7d32",
    },
    {
        "cat": "society",
        "zh_title": "柏林骄傲节袭击嫌犯数周前刚获释引发舆论愤怒",
        "en_title": "Outrage as Berlin Pride attacker had been freed weeks earlier",
        "published": "20:33 2026年7月27日",
        "zh_sum": "21岁嫌犯周六驾车冲撞并持刀伤人致1死29伤，周日被警方击毙；其曾因涉极端主义获刑后近期出狱。",
        "en_sum": "Anger grew after learning suspect Abdul Ballout was recently freed before the Pride attack that killed one.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.co.uk/news/articles/cy9wv74qje9o",
        "tag": "#6a1b9a",
    },
    {
        "cat": "society",
        "zh_title": "西雅图美食节枪击案警方称或有三名枪手",
        "en_title": "Seattle food festival shooting may involve three gunmen, police say",
        "published": "00:00 2026年7月28日",
        "zh_sum": "周日太空针塔附近年度美食节发生枪战，3死至少4伤；周一法庭文件显示警方怀疑第三名嫌疑人仍在逃。",
        "en_sum": "Three people died and at least four were hurt at Bite of Seattle; court papers now suggest a third shooter.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c78gjyx4q2yo",
        "tag": "#6a1b9a",
    },
    {
        "cat": "society",
        "zh_title": "中国汛季启动专项整治，打击编造灾情骗取流量行为",
        "en_title": "China launches flood-season crackdown on disaster-related online fraud",
        "published": "00:00 2026年7月23日",
        "zh_sum": "网信与应急管理部门联合行动，查处AI合成淹水视频、虚假募捐链接等案件，多人被行政处罚。",
        "en_sum": "Regulators target AI flood hoaxes and fake donation links as police penalize dozens in a summer campaign.",
        "source_zh": "中国日报 China Daily",
        "source_en": "China Daily",
        "url": "https://www.chinadaily.com.cn/a/202607/23/WS6a61ea9ca310986e2b466f63.html",
        "tag": "#6a1b9a",
    },
    {
        "cat": "world",
        "zh_title": "特朗普称美伊在停火间隙进行“友好谈判”",
        "en_title": "Trump says 'friendly negotiations' with Iran continue during strike pause",
        "published": "00:00 2026年7月28日",
        "zh_sum": "美方连续第三日未对伊发动空袭；特朗普称会谈有进展但警告若无协议将恢复打击，德黑兰否认直接谈判。",
        "en_sum": "Trump cited good talks during a third day without strikes but warned attacks could resume; Iran denies direct talks.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/c62xn4vzmnpo",
        "tag": "#e65100",
    },
    {
        "cat": "world",
        "zh_title": "调解方称美伊停火窗口下和谈取得进展",
        "en_title": "Mediators report progress bringing U.S. and Iran back to talks",
        "published": "00:00 2026年7月28日",
        "zh_sum": "卡塔尔、巴基斯坦等斡旋方称双方暂停互攻为谈判创造空间，但地区零星袭击显示局势仍脆弱。",
        "en_sum": "Qatar- and Pakistan-led mediators see progress after both sides paused attacks, though regional strikes persist.",
        "source_zh": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/iran-us-hormuz-strait-war-qatar-pakistan-d57e675a7be6dbdd34561909ced240d0",
        "tag": "#e65100",
    },
    {
        "cat": "world",
        "zh_title": "法国吉伦特大火暂趋稳定但未完全受控，马克龙召开紧急内阁会",
        "en_title": "France's Gironde mega-fire 'stabilized' but not contained, Macron convenes crisis talks",
        "published": "03:08 2026年7月28日",
        "zh_sum": "内政部长称火势已稳定仍不可掉以轻心，逾22万人疏散、逾10万英亩过火；新一波热浪逼近波尔多。",
        "en_sum": "Officials say the blaze near Bordeaux is stabilized yet uncontained, with 220,000 evacuated and heat returning.",
        "source_zh": "美国广播公司新闻 ABC News",
        "source_en": "ABC News",
        "url": "https://abcnews.com/International/major-wildfire-france-stabilized-contained-interior-minister/story?id=135123975",
        "tag": "#e65100",
    },
    {
        "cat": "world",
        "zh_title": "马克龙召开内阁危机会议协调法国西南部野火应对",
        "en_title": "Macron holds crisis cabinet meeting as wildfires near Bordeaux",
        "published": "00:00 2026年7月27日",
        "zh_sum": "吉伦特当局称局势整夜大致稳定，火焰距波尔多城区约15公里，周末欧洲多国逾30万人被迫撤离。",
        "en_sum": "Macron coordinated the response as flames stayed about 15km from Bordeaux amid Europe's heat-driven evacuations.",
        "source_zh": "半岛电视台 Al Jazeera",
        "source_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/7/27/macron-calls-crisis-meeting-of-french-cabinet-as-blaze-approaches-bordeaux",
        "tag": "#e65100",
    },
    {
        "cat": "world",
        "zh_title": "柏林骄傲节袭击主嫌在与警方对峙中被击毙",
        "en_title": "Berlin Pride attack suspect killed in police confrontation",
        "published": "00:00 2026年7月27日",
        "zh_sum": "德国内政部长称周六袭击疑似伊斯兰极端主义恐袭，嫌犯周日在施潘道持刀冲向特警后被击毙。",
        "en_sum": "Police killed suspect Abdul Ballout on Sunday after Saturday's ramming and stabbing attack at Berlin Pride.",
        "source_zh": "美联社 AP",
        "source_en": "Associated Press",
        "url": "https://apnews.com/article/germany-berlin-lgbtq-pride-parade-van-ramming-3ba5e3f1becffd0da5f47b29aa08da9d",
        "tag": "#e65100",
    },
    {
        "cat": "hk",
        "zh_title": "金管局发布量子安全指数，银行业整体得分仅2.3",
        "en_title": "HKMA quantum preparedness index scores banks at 2.3 out of 10",
        "published": "21:50 2026年7月27日",
        "zh_sum": "当局称多数银行仍处准备初期，目标2030年前完成后量子密码过渡，逾三成尚无正式路线图。",
        "en_sum": "The HKMA's new index shows banks are early in preparing for post-quantum cryptography risks by 2030.",
        "source_zh": "南华早报 SCMP",
        "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/business/banking-finance/article/3362033/hong-kong-banks-early-stages-preparing-quantum-computing-threats-hkma-says",
        "tag": "#00838f",
    },
    {
        "cat": "hk",
        "zh_title": "台风“诺尔”过后周一仍有旅客滞留香港机场",
        "en_title": "Passengers still stranded at Hong Kong airport on Monday after Typhoon Noul",
        "published": "13:49 2026年7月27日",
        "zh_sum": "机场管理局称运作已恢复正常、全日预计900班次，仍有旅客等候航空公司消化周末大规模取消航班。",
        "en_sum": "Operations normalized with 900 flights expected, but backlog lingered after hundreds of weekend cancellations.",
        "source_zh": "南华早报 SCMP",
        "source_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/transport/article/3361956/some-air-passengers-remain-stranded-hong-kong-airport-after-typhoon-noul",
        "tag": "#00838f",
    },
    {
        "cat": "hk",
        "zh_title": "尼加拉瓜及所罗门群岛给予香港特区护照免签证入境",
        "en_title": "Nicaragua and Solomon Islands grant visa-free access to HKSAR passports",
        "published": "00:00 2026年7月27日",
        "zh_sum": "入境处宣布两项互免安排，持特区护照可停留最多30天，免签目的地总数升至178个。",
        "en_sum": "Hong Kong passport holders gain 30-day visa-free access, lifting total destinations to 178.",
        "source_zh": "香港政府新闻网 news.gov.hk",
        "source_en": "news.gov.hk",
        "url": "https://www.news.gov.hk/eng/2026/07/20260727/20260727_175318_291.html",
        "tag": "#00838f",
    },
    {
        "cat": "hk",
        "zh_title": "香港6月出口按年飙升53.4%，创多年最快增速",
        "en_title": "Hong Kong exports jump 53.4% in June, fastest pace in decades",
        "published": "18:18 2026年7月27日",
        "zh_sum": "政府数据显示出口总值创6410亿港元纪录，当局指人工智能相关需求是重要动力之一。",
        "en_sum": "June exports surged 53.4% year on year to a record HK$641 billion, aided by strong AI-linked demand.",
        "source_zh": "香港电台 RTHK",
        "source_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1863935-20260727.htm",
        "tag": "#00838f",
    },
    {
        "cat": "other",
        "zh_title": "印度阿萨姆邦遭遇数十年来最严重洪灾",
        "en_title": "India's Assam faces worst floods in decades",
        "published": "00:00 2026年7月27日",
        "zh_sum": "纳加兰与阿萨姆异常强降雨致至少68人死亡、逾60万人受灾，数万民众滞留安置营。",
        "en_sum": "Exceptional rains killed at least 68 and displaced tens of thousands across Assam and Nagaland.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cqlx61p3wz0o",
        "tag": "#5d4037",
    },
    {
        "cat": "other",
        "zh_title": "英国首相警告：不改革社会护理 NHS将难以为继",
        "en_title": "UK PM warns NHS will collapse without social care reform",
        "published": "00:00 2026年7月27日",
        "zh_sum": "伯恩汉姆首访大型采访称将加速凯西委员会审查，但未给出新制度时间表，周三将再谈养老政策。",
        "en_sum": "Andy Burnham told the BBC he will fast-track the Casey Commission but gave no timeline for a new care system.",
        "source_zh": "英国广播公司 BBC",
        "source_en": "BBC",
        "url": "https://www.bbc.com/news/articles/cn0n5xpzlz2o",
        "tag": "#5d4037",
    },
]


def item_html(n: int, it: dict) -> str:
    zt = html.escape(it["zh_title"])
    et = html.escape(it["en_title"])
    url = html.escape(it["url"], quote=True)
    zs = html.escape(it["zh_sum"])
    es = html.escape(it["en_sum"])
    pub = html.escape(it["published"])
    sz = html.escape(it["source_zh"])
    se = html.escape(it["source_en"])
    tag = it["tag"]
    num = f"{n:02d}"
    return f"""<div style="margin:0 0 18px 0;padding:0 0 14px 0;border-bottom:1px solid #eee;">
<p style="margin:0 0 6px 0;font-size:11px;color:#888;font-weight:bold;">{num}</p>
<p style="margin:0 0 4px 0;font-size:16px;line-height:1.45;"><a href="{url}" style="color:#1a237e;text-decoration:none;font-weight:600;">{zt}</a></p>
<p style="margin:0 0 4px 0;font-size:14px;line-height:1.4;color:#444;font-style:italic;">{et}</p>
<p style="margin:0 0 8px 0;font-size:12px;color:#888;">发布时间 Published: {pub}</p>
<p style="margin:0 0 4px 0;font-size:14px;line-height:1.55;color:#333;">{zs}</p>
<p style="margin:0 0 10px 0;font-size:13px;line-height:1.5;color:#555;">{es}</p>
<p style="margin:0;font-size:12px;"><span style="display:inline-block;padding:2px 8px;border-radius:4px;background:{tag};color:#fff;margin-right:8px;">{sz}</span><a href="{url}" style="color:#1565c0;">查看全文 Read more →</a></p>
</div>"""


def build_html() -> str:
    n = len(ITEMS)
    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        f"<title>每日热点{EDITION_ZH}</title></head>",
        '<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;">',
        '<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#f0f2f5;"><tr><td align="center" style="padding:16px 8px;">',
        '<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;">',
        f'<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);color:#fff;padding:22px 20px;">',
        f'<p style="margin:0;font-size:22px;font-weight:700;">每日热点{EDITION_ZH}</p>',
        f'<p style="margin:8px 0 0 0;font-size:13px;opacity:.92;">{EDITION_EN} News Briefing · {BRIEFING_DATE} · 共 {n} 条</p></td></tr>',
        '<tr><td style="padding:18px 20px 8px 20px;">',
        f'<p style="margin:0 0 6px 0;font-size:14px;color:#333;">昨夜至今晨重要新闻一览，涵盖国际市场收盘、政策动态与突发事态。</p>',
        f'<p style="margin:0;font-size:13px;color:#666;font-style:italic;">Overnight and early headlines through this morning, including global market closes and breaking developments.</p>',
        "</td></tr>",
    ]
    idx = 1
    cat_map = {c[0]: (c[1], c[2]) for c in CATEGORIES}
    order = [c[0] for c in CATEGORIES]
    for cat in order:
        items = [it for it in ITEMS if it["cat"] == cat]
        if not items:
            continue
        zh, en = cat_map[cat]
        parts.append(
            f'<tr><td style="padding:8px 20px 4px 20px;"><h2 style="margin:0;padding:10px 12px;font-size:15px;background:#f5f5f5;border-left:4px solid #1565c0;color:#212121;">{html.escape(zh)}<br><span style="font-size:12px;font-weight:normal;color:#666;">{html.escape(en)}</span></h2></td></tr>'
        )
        parts.append('<tr><td style="padding:4px 20px 8px 20px;">')
        for it in items:
            parts.append(item_html(idx, it))
            idx += 1
        parts.append("</td></tr>")
    parts.extend(
        [
            '<tr><td style="padding:16px 20px 22px 20px;background:#fafafa;border-top:1px solid #eee;">',
            '<p style="margin:0 0 6px 0;font-size:11px;line-height:1.5;color:#888;">本简报由自动化流程汇编公开报道，仅供信息参考，不构成投资或法律建议。版权归原媒体所有。</p>',
            '<p style="margin:0;font-size:11px;line-height:1.5;color:#888;">Compiled from public reports for informational purposes only; not investment or legal advice. Rights belong to original publishers.</p>',
            "</td></tr></table></td></tr></table></body></html>",
        ]
    )
    return "".join(parts)


def main():
    root = os.path.join(os.path.dirname(__file__), "..")
    payload = {
        "subject": f"每日热点{EDITION_ZH} {EDITION_EN} - {BRIEFING_DATE}",
        "htmlContent": build_html(),
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {path}, items={len(ITEMS)}, html_chars={len(payload['htmlContent'])}")


if __name__ == "__main__":
    main()
