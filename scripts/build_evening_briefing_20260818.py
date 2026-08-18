#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 2026-08-18 evening briefing HTML (not a send script)."""
import json
import os

ITEMS = [
    # 国内
    {
        "cat": "cn",
        "zh_title": "刘慧涉嫌受贿案已提起公诉，将在菏泽受审",
        "en_title": "Former Ningxia chair Liu Hui charged with bribery, to stand trial",
        "pub": "11:29 2026年8月18日",
        "zh_sum": "最高检通报，宁夏自治区政府原主席刘慧受贿案已由菏泽检方起诉，指数额特别巨大。",
        "en_sum": "China’s top prosecutor says former Ningxia chair Liu Hui has been charged with huge-scale bribery in Heze.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://china.caixin.com/2026-08-18/102475267.html",
        "color": "#c41e3a",
    },
    {
        "cat": "cn",
        "zh_title": "中国工程院撤下赵晓哲院士简历",
        "en_title": "Chinese Academy of Engineering removes Zhao Xiaozhe’s profile",
        "pub": "12:30 2026年8月18日",
        "zh_sum": "军委科技委原主任、海军中将赵晓哲的姓名与简历已从工程院全体院士名单中撤下。",
        "en_sum": "The Chinese Academy of Engineering has removed Vice Admiral Zhao Xiaozhe from its academician list.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://china.caixin.com/2026-08-18/102475286.html",
        "color": "#c41e3a",
    },
    {
        "cat": "cn",
        "zh_title": "全国人大常委会将于8月25日至28日开会",
        "en_title": "NPC Standing Committee to meet Aug. 25–28 in Beijing",
        "pub": "15:34 2026年8月18日",
        "zh_sum": "委员长会议决定召开第二十四次常委会会议，拟审议医保、国防动员及反跨境腐败等草案。",
        "en_sum": "China’s NPC Standing Committee will meet Aug. 25–28 to review medical insurance and anti-graft bills.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://finance.sina.com.cn/jjxw/2026-08-18/doc-inintpir7335549.shtml",
        "color": "#c41e3a",
    },
    {
        "cat": "cn",
        "zh_title": "发改委部署加快新型政策性金融工具投放",
        "en_title": "NDRC orders faster rollout of policy-based financing tools",
        "pub": "17:27 2026年8月17日",
        "zh_sum": "发改委召开工作会议，要求加快2026年新型政策性金融工具投放，加大民间投资项目支持。",
        "en_sum": "China’s NDRC says it will speed 2026 policy financing tools and increase support for private investment projects.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/fortune/20260817/b8f239d36dac4dc9a1c8829117b2353c/c.html",
        "color": "#c41e3a",
    },
    # 科技
    {
        "cat": "tech",
        "zh_title": "宇树科技定于8月19日登陆科创板",
        "en_title": "Unitree to list on STAR Market on August 19",
        "pub": "20:55 2026年8月17日",
        "zh_sum": "宇树公告将于8月19日科创板上市，发行价150.80元，发行后市值约610亿元。",
        "en_sum": "Unitree will list on Shanghai’s STAR Market on Aug. 19 at 150.80 yuan a share, valuing it near 61 billion yuan.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://www.caixin.com/2026-08-17/102475134.html",
        "color": "#0b6e99",
    },
    {
        "cat": "tech",
        "zh_title": "字节跳动与好莱坞MPA就AI版权达成协议",
        "en_title": "ByteDance and Hollywood’s MPA reach AI copyright pact",
        "pub": "21:32 2026年8月17日",
        "zh_sum": "双方签署谅解备忘录，加强Seedance与Seedream等生成模型的版权防护，覆盖TikTok等产品。",
        "en_sum": "ByteDance and the MPA agreed on guardrails for Seedance and Seedream after a February copyright dispute.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.reuters.com/legal/litigation/bytedance-signs-ai-copyright-pact-with-hollywood-trade-group-2026-08-17/",
        "color": "#0b6e99",
    },
    {
        "cat": "tech",
        "zh_title": "央行新增8家数字人民币运营机构至30家",
        "en_title": "PBOC adds eight digital yuan operators, taking total to 30",
        "pub": "16:32 2026年8月17日",
        "zh_sum": "平安、恒丰、渤海及5家城商行接入央行数字人民币系统，完成准备后将开办相关业务。",
        "en_sum": "China’s central bank named eight more banks as digital yuan operators, expanding the network to 30 institutions.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/20260817/5f7039d8f424409fb57eb236ecff86a6/c.html",
        "color": "#0b6e99",
    },
    {
        "cat": "tech",
        "zh_title": "英伟达为OpenAI俄亥俄数据中心提供最高1050亿美元担保",
        "en_title": "Nvidia caps $105 billion guarantee for OpenAI’s Ohio campus",
        "pub": "20:43 2026年8月17日",
        "zh_sum": "英伟达将为OpenAI租用的俄亥俄AI园区提供最高1050亿美元担保，并向SB Energy投资15亿美元。",
        "en_sum": "Nvidia will guarantee up to $105 billion for an OpenAI data center in Ohio and invest $1.5 billion in SB Energy.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://finance.yahoo.com/technology/ai/articles/nvidia-invest-1-5-billion-124300582.html",
        "color": "#0b6e99",
    },
    # 财经
    {
        "cat": "fin",
        "zh_title": "港股尾市收复失地，恒指微升17点",
        "en_title": "Hang Seng rebounds late, closes up 17 points",
        "pub": "16:25 2026年8月18日",
        "zh_sum": "恒指早段最多跌逾210点，收报25471点，升约0.1%；科指跌0.9%，智谱重挫逾13%。",
        "en_sum": "Hong Kong’s Hang Seng recovered from a 210-point drop to close up 17 points; the tech index fell 0.9%.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866582-20260818.htm",
        "color": "#1a7f37",
    },
    {
        "cat": "fin",
        "zh_title": "沪指收涨创五周新高，深成指回落",
        "en_title": "Shanghai Composite hits a five-week high; Shenzhen slips",
        "pub": "15:11 2026年8月18日",
        "zh_sum": "上证综指收报3990点，升0.19%，创五周新高；深成指跌0.56%，创业板指跌0.92%。",
        "en_sum": "The Shanghai Composite rose 0.19% to 3,990, a five-week high, while Shenzhen and ChiNext closed lower.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866575-20260818.htm",
        "color": "#1a7f37",
    },
    {
        "cat": "fin",
        "zh_title": "李书福辞任吉利汽车董事长，公司称释放去家族化信号",
        "en_title": "Li Shufu steps down as Geely Auto chairman in de-family move",
        "pub": "09:45 2026年8月18日",
        "zh_sum": "李书福卸任港股吉利汽车董事会主席，由安聪慧接任；李仍为控股股东并任控股集团董事长。",
        "en_sum": "Li Shufu left the Geely Auto chair; CEO An Conghui takes over. Li remains controlling shareholder.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://www.caixin.com/2026-08-18/102475231.html",
        "color": "#1a7f37",
    },
    {
        "cat": "fin",
        "zh_title": "美伊停火到期，亚洲债息走高、油价连日上涨",
        "en_title": "Bond yields jump and oil extends gains as US-Iran truce expires",
        "pub": "16:42 2026年8月18日",
        "zh_sum": "美国30年期国债收益率盘中创近20年高位，布伦特原油站上91美元，亚洲股市早盘回吐升幅。",
        "en_sum": "US 30-year yields hit a two-decade high and Brent topped $91 as the US-Iran truce lapsed.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://www.reuters.com/world/china/global-markets-wrapup-1-2026-08-18/",
        "color": "#1a7f37",
    },
    # 社会
    {
        "cat": "soc",
        "zh_title": "最高法披露许垚投毒杀人案证据链条",
        "en_title": "Supreme Court details evidence in Xu Yao poisoning murder case",
        "pub": "14:51 2026年8月17日",
        "zh_sum": "《刑事审判参考》刊登许垚案复核文书，指其因长期矛盾购毒投毒，已于今年5月执行死刑。",
        "en_sum": "China’s Supreme Court published its review of the Xu Yao case, citing a closed chain of indirect evidence.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://companies.caixin.com/2026-08-17/102474818.html",
        "color": "#8a4b08",
    },
    {
        "cat": "soc",
        "zh_title": "医保局明确158个基层病种，推行同病同价",
        "en_title": "China names 158 primary-care diseases for equal payment rates",
        "pub": "07:21 2026年8月18日",
        "zh_sum": "即将印发的按病种付费3.0方案将列出158个基层病种，不同等级医院执行同一支付标准。",
        "en_sum": "China’s medical insurance regulator will set the same payment rates for 158 conditions treated at lower-level hospitals.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://www.caixin.com/2026-08-18/102475186.html",
        "color": "#8a4b08",
    },
    {
        "cat": "soc",
        "zh_title": "菲律宾南部校园枪击，含枪手在内两人死亡",
        "en_title": "Student gunman kills classmate and himself at Philippine school",
        "pub": "10:19 2026年8月18日",
        "zh_sum": "三宝颜一所中学发生枪击，一名学生持枪射杀同学后自杀，另有人受伤，部分过程曾网上直播。",
        "en_sum": "A student in Zamboanga shot a classmate and himself in a livestreamed attack; two others were wounded.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://apnews.com/article/philippines-zamboanga-school-shooting-fe3aa5d6d1f3dd2ca614d68bb373d604",
        "color": "#8a4b08",
    },
    {
        "cat": "soc",
        "zh_title": "香港拟于本月底前优化工作暑热警告",
        "en_title": "Hong Kong aims to upgrade heat-at-work alerts this month",
        "pub": "12:46 2026年8月18日",
        "zh_sum": "劳工及福利局局长孙玉菡表示，将检视触发门槛，争取本月底前推出更贴合本地高温的警告机制。",
        "en_sum": "Labour chief Chris Sun said Hong Kong will try to revise heat-stress work alerts before the end of August.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866554-20260818.htm",
        "color": "#8a4b08",
    },
    # 国际
    {
        "cat": "world",
        "zh_title": "霍尔木兹海峡一船遭不明投射物击中，有船员伤亡",
        "en_title": "Vessel hit by unknown projectile in Strait of Hormuz, UKMTO says",
        "pub": "14:35 2026年8月18日",
        "zh_sum": "英国海事贸易作业中心称，一艘出港船只机舱受损并有船员伤亡，阿曼海岸警卫队正在协助。",
        "en_sum": "UKMTO said a ship leaving the Strait of Hormuz was struck, damaging the engine room and causing a crew casualty.",
        "src_zh": "半岛电视台",
        "src_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/8/18/vessel-hit-by-unknown-projectile-in-strait-of-hormuz-ukmto-says",
        "color": "#1d4ed8",
    },
    {
        "cat": "world",
        "zh_title": "赞比亚总统希奇莱马赢得连任",
        "en_title": "Zambia’s Hakainde Hichilema wins a second presidential term",
        "pub": "09:32 2026年8月18日",
        "zh_sum": "选举委员会宣布希奇莱马得票约61.4%，无需进入第二轮；计票曾因暴力指控短暂中止。",
        "en_sum": "Zambia’s electoral commission declared President Hichilema the winner with 61.4% after a tense count.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://apnews.com/article/zambia-election-hichilema-victory-562c0ee56653c8dc835af7556c913aab",
        "color": "#1d4ed8",
    },
    {
        "cat": "world",
        "zh_title": "美媒：习近平将于9月24日访白宫，不到联大发言",
        "en_title": "Xi to meet Trump on Sept. 24, skipping UN General Assembly",
        "pub": "16:22 2026年8月18日",
        "zh_sum": "Politico引述知情人士称，习近平将于9月23日抵美、24日会晤特朗普，不赴纽约联合国大会发言。",
        "en_sum": "Politico reports Xi Jinping will meet Trump in Washington on Sept. 24 and will not address the UN in New York.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866584-20260818.htm",
        "color": "#1d4ed8",
    },
    {
        "cat": "world",
        "zh_title": "特朗普称金正恩已回应美方对话请求",
        "en_title": "Trump says Kim Jong Un has replied to his outreach",
        "pub": "13:44 2026年8月18日",
        "zh_sum": "特朗普在白宫称与金正恩的接触“非常正面”，但未披露细节；朝方暂无公开评论。",
        "en_sum": "President Trump said Kim Jong Un had given a “very positive” response, a day after ordering smaller US-South Korea drills.",
        "src_zh": "半岛电视台",
        "src_en": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/8/18/trump-says-n-koreas-kim-has-responded-to-his-request-for-a-conversation",
        "color": "#1d4ed8",
    },
    # 香港
    {
        "cat": "hk",
        "zh_title": "大埔宏福苑火灾调查报告延至十月底前提交",
        "en_title": "Tai Po fire inquiry report delayed until end of October",
        "pub": "13:32 2026年8月18日",
        "zh_sum": "独立委员会称须处理逾百万份档案，已获行政长官同意将原定九月的报告期限延至十月底。",
        "en_sum": "The judge-led panel reviewing the Wang Fuk Court fire will submit its report by end-October, not September.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/society/article/3364385/committee-probing-tai-po-fire-delays-submission-report-end-october",
        "color": "#7c3aed",
    },
    {
        "cat": "hk",
        "zh_title": "十月起分阶段整合长者健康中心至地区康健网络",
        "en_title": "Elderly health centres to merge into district network from October",
        "pub": "13:35 2026年8月18日",
        "zh_sum": "基层医疗署称10月5日起先整合9间中心，服务点将由18个增至逾100个，服务量倍增。",
        "en_sum": "Hong Kong will fold nine Elderly Health Centres into District Health Centres from Oct. 5, expanding access.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866566-20260818.htm",
        "color": "#7c3aed",
    },
    {
        "cat": "hk",
        "zh_title": "香港年中人口增至751.83万，人才净移入抵销自然减少",
        "en_title": "Hong Kong mid-year population rises to 7.518 million",
        "pub": "17:01 2026年8月18日",
        "zh_sum": "统计处公布年中人口临时数字较去年同期增加1.94万人；净移入3.98万人，自然减少2.04万人。",
        "en_sum": "Hong Kong’s mid-year population rose 0.3% as net inflows offset more deaths than births, the Census says.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866590-20260818.htm",
        "color": "#7c3aed",
    },
    # 其他
    {
        "cat": "oth",
        "zh_title": "油气发展“十五五”规划印发，CCS指标首次纳入",
        "en_title": "China’s 15th five-year oil and gas plan adds CCS targets",
        "pub": "07:32 2026年8月18日",
        "zh_sum": "规划提出2030年国内油气供应4.4亿吨油当量，长输管网达22万公里，年封存二氧化碳1000万吨。",
        "en_sum": "Beijing’s new oil and gas plan targets 440 million tonnes of oil equivalent by 2030 and 10 million tonnes of CCS.",
        "src_zh": "新华财经",
        "src_en": "Xinhua Finance",
        "url": "https://www.cnfin.com/dz-lb/detail/20260818/4456438_1.html",
        "color": "#475569",
    },
    {
        "cat": "oth",
        "zh_title": "比利时高原湿地大火仍未扑灭，希腊调查致命山火",
        "en_title": "Belgian wildfire still burning as Greece probes deadly blaze",
        "pub": "19:37 2026年8月17日",
        "zh_sum": "比利时高沼国家公园大火在降雨后仍难进入核心区；希腊当局调查萨拉米斯岛造成两人死亡的山火。",
        "en_sum": "One of Belgium’s largest modern wildfires still burned near Germany, while Greece investigated a deadly island fire.",
        "src_zh": "美联社",
        "src_en": "AP",
        "url": "https://apnews.com/article/wildfire-belgium-france-heat-europe-greece-cd5a8524ca3136b009422bd24eb4194e",
        "color": "#475569",
    },
    {
        "cat": "oth",
        "zh_title": "费里入选英国戴维斯杯阵容，对阵厄瓜多尔",
        "en_title": "Arthur Fery named in Britain’s Davis Cup team to face Ecuador",
        "pub": "20:32 2026年8月17日",
        "zh_sum": "温网四强亚瑟·费里入选9月主场对阵厄瓜多尔的阵容；德雷珀因伤未入选，第五人稍后补报。",
        "en_sum": "Wimbledon semi-finalist Arthur Fery joins Britain’s Davis Cup squad for the September home tie against Ecuador.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.co.uk/sport/tennis/articles/cz97zew58xxo",
        "color": "#475569",
    },
]

CATS = [
    ("cn", "国内 / 内地 China Mainland"),
    ("tech", "科技 / 互联网 Technology"),
    ("fin", "财经 / 商业 Finance & Business"),
    ("soc", "社会 Society"),
    ("world", "国际 World"),
    ("hk", "香港本地 Hong Kong"),
    ("oth", "其他 Other"),
]


def check_banned(text: str):
    for b in ("测试", "预览", "续"):
        if b in text:
            raise SystemExit(f"Banned token {b!r} found in: {text[:80]}")
    import re
    if re.search(r"(?i)\b(test|draft|part)\b", text):
        raise SystemExit(f"Banned English token found in: {text[:80]}")


def main():
    n = len(ITEMS)
    assert 20 <= n <= 28, n
    for it in ITEMS:
        assert len(it["zh_sum"]) <= 55, (it["zh_title"], len(it["zh_sum"]), it["zh_sum"])
        wc = len(it["en_sum"].split())
        assert wc <= 30, (it["zh_title"], wc, it["en_sum"])
        check_banned(it["zh_title"] + it["zh_sum"] + it["en_title"] + it["en_sum"])

    parts = []
    parts.append(
        f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点晚报 Evening News Briefing</title>
</head>
<body style="margin:0;padding:0;background:#eef1f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;color:#1f2937;">
<div style="display:none;max-height:0;overflow:hidden;">每日热点晚报 · 2026年8月18日 · 共{n}条 Today’s main stories</div>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef1f4;">
<tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="width:600px;max-width:600px;background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 8px 24px rgba(15,23,42,.08);">
<tr><td style="background:#0f172a;padding:22px 24px 18px;color:#fff;">
<div style="font-size:22px;font-weight:700;letter-spacing:.02em;">每日热点晚报</div>
<div style="margin-top:6px;font-size:13px;color:#cbd5e1;">Evening News Briefing · 2026年8月18日 · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:16px 24px 8px;background:#fff;">
<p style="margin:0 0 8px;font-size:14px;line-height:1.7;color:#334155;">汇总今日全日要闻，覆盖内地政策与人事、亚股收盘、科技产业及国际变局。</p>
<p style="margin:0 0 12px;font-size:13px;line-height:1.7;color:#64748b;font-style:italic;">Today’s main stories across China, markets, technology, society and world affairs.</p>
</td></tr>
"""
    )
    i = 0
    for key, label in CATS:
        group = [it for it in ITEMS if it["cat"] == key]
        if not group:
            continue
        parts.append(
            f"""<tr><td style="padding:8px 24px 4px;">
<div style="background:#f1f5f9;border-left:4px solid #2563eb;padding:8px 12px;border-radius:0 8px 8px 0;">
<h2 style="margin:0;font-size:16px;color:#0f172a;">{label}</h2>
</div></td></tr>"""
        )
        for it in group:
            i += 1
            num = f"{i:02d}"
            check_banned(it["zh_title"] + it["zh_sum"])
            parts.append(
                f"""<tr><td style="padding:12px 24px;border-bottom:1px solid #eef2f7;">
<div style="font-size:12px;color:#94a3b8;font-weight:700;margin-bottom:4px;">{num}</div>
<a href="{it['url']}" style="color:#0f172a;font-size:16px;font-weight:700;text-decoration:none;line-height:1.45;">{it['zh_title']}</a>
<div style="margin:4px 0 0;font-size:13px;color:#475569;font-style:italic;line-height:1.45;">{it['en_title']}</div>
<div style="margin:4px 0 8px;font-size:12px;color:#94a3b8;">发布时间 Published: {it['pub']}</div>
<div style="font-size:14px;line-height:1.65;color:#334155;">{it['zh_sum']}</div>
<div style="margin-top:4px;font-size:13px;line-height:1.6;color:#64748b;">{it['en_sum']}</div>
<div style="margin-top:8px;">
<span style="display:inline-block;background:{it['color']};color:#fff;font-size:11px;padding:2px 8px;border-radius:999px;">{it['src_zh']} {it['src_en']}</span>
<a href="{it['url']}" style="margin-left:8px;font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</div>
</td></tr>"""
            )

    assert i == n
    parts.append(
        """<tr><td style="padding:18px 24px 24px;background:#f8fafc;color:#64748b;font-size:11px;line-height:1.7;">
<div>免责声明：本简报整理公开媒体报道，仅供参考，不构成投资、法律或政策建议。标题与摘要力求客观中立，详情请阅读原文。</div>
<div style="margin-top:6px;">Disclaimer: This briefing summarises publicly available reports for information only and is not investment, legal or policy advice. Please read the original articles for full context.</div>
</td></tr>
</table>
</td></tr></table>
</body></html>"""
    )
    html = "".join(parts)
    check_banned(html)
    if "每日热点早报" in html or "Morning News Briefing" in html:
        raise SystemExit("Edition mix-up")
    if html.count("晚报") < 2:
        raise SystemExit("Missing evening edition labels")
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-18",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    check_banned(payload["subject"])
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("items", n)
    print("html_chars", len(html))
    print("wrote", os.path.abspath(out))
    # counts
    from collections import Counter
    print("cats", dict(Counter(it["cat"] for it in ITEMS)))
    print("sources", dict(Counter(it["src_en"] for it in ITEMS)))


if __name__ == "__main__":
    main()
