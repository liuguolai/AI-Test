#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-05."""

import json
import os
from html import escape

BRIEFING_DATE = "2026-08-05"
BRIEFING_EDITION = "晚报"
TOTAL_LABEL = "26"

CATEGORIES = [
    ("domestic", "国内 China Mainland", [
        {
            "zh_title": "我国成功发射东方慧眼高光谱01、02星",
            "en_title": "China launches Dongfang Huiyan hyperspectral satellites",
            "published": "11:06 2026年8月5日",
            "zh_summary": "捷龙三号火箭在山东海阳附近海域发射，双星顺利入轨，任务圆满成功。",
            "en_summary": "Smart Dragon-3 lifted two Dongfang Huiyan satellites from sea near Haiyang, Shandong.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www3.xinhuanet.com/20260805/1bc39b36ccad4f15be54f2b033b32bc0/c.html",
        },
        {
            "zh_title": "最高检发布5件疑难复杂刑事抗诉指导性案例",
            "en_title": "China's top procuratorate releases five complex criminal appeal guiding cases",
            "published": "10:10 2026年8月5日",
            "zh_summary": "案例均为最高检向最高法院提出抗诉的再审案件，体现维护司法公正立场。",
            "en_summary": "All five cases involved Supreme People's Procuratorate appeals in major retrials.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "https://www3.xinhuanet.com/20260805/9c65ebfa44324b3ab8223c26dde6cc06/c.html",
        },
        {
            "zh_title": "L3/L4级自动驾驶系统安全要求国标发布",
            "en_title": "China releases mandatory safety standard for L3/L4 autonomous driving",
            "published": "00:00 2026年8月5日",
            "zh_summary": "国标GB44721—2026适用于有条件及高度自动驾驶M/N类车，2027年7月1日起实施。",
            "en_summary": "Mandatory GB 44721-2026 covers L3/L4 M/N vehicles, effective 1 July 2027.",
            "source_zh": "新华社《经济参考报》", "source_en": "Xinhua / Economic Information Daily",
            "url": "http://jjckb.xinhuanet.com/20260805/32d3819391e3450a9c5e040fc9abdb34/c.html",
        },
        {
            "zh_title": "全国试点上线“身后金融事”查询服务",
            "en_title": "China pilots posthumous financial affairs inquiry service nationwide",
            "published": "09:56 2026年8月5日",
            "zh_summary": "亲人离世后，继承人可更便捷查询逝者名下银行存款等金融资产信息。",
            "en_summary": "Heirs can more easily locate a deceased person's bank deposits and financial assets.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-05/102471315.html",
        },
        {
            "zh_title": "国家邮政局对申通快递立案调查",
            "en_title": "China's postal regulator opens probe into STO Express",
            "published": "08:54 2026年8月5日",
            "zh_summary": "因安全生产管理缺位，未对关联网点实行统一安全保障管理，依法启动调查。",
            "en_summary": "Regulator cited safety management failures across STO-branded operations.",
            "source_zh": "新浪财经（新华社）", "source_en": "Sina Finance (Xinhua)",
            "url": "https://finance.sina.com.cn/jjxw/2026-08-05/doc-inimfmyp5211642.shtml",
        },
    ]),
    ("tech", "科技 / 互联网 Technology", [
        {
            "zh_title": "特朗普政府拟禁止进口中国新型数据中心组件",
            "en_title": "Trump administration drafting ban on new Chinese data center components",
            "published": "09:28 2026年8月5日",
            "zh_summary": "路透社称FCC正起草措施，限制进口中国光模块等器件，以防范AI基础设施风险。",
            "en_summary": "Reuters says the FCC may bar new Chinese optical transceivers to protect AI data centers.",
            "source_zh": "日本时报（路透社）", "source_en": "The Japan Times (Reuters)",
            "url": "https://www.japantimes.co.jp/news/2026/08/05/world/trump-ban-chinese-data-center/",
        },
        {
            "zh_title": "SpaceX上市后首份财报显示营收78亿美元",
            "en_title": "SpaceX posts first earnings as public company with $7.8bn revenue",
            "published": "08:45 2026年8月5日",
            "zh_summary": "二季度营收同比增92%，并宣布与英伟达合作开发Starmind算力卫星。",
            "en_summary": "Q2 revenue rose 92% YoY; firm also unveiled Nvidia-linked Starmind compute satellites.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-05/102471302.html",
        },
        {
            "zh_title": "工信部叫停废旧动力电池“梯次利用”",
            "en_title": "China's MIIT halts used EV battery 'cascade utilization' policy",
            "published": "17:25 2026年8月4日",
            "zh_summary": "废止相关规范条款，100家已公告梯次利用企业移出合规名单，强化质量安全要求。",
            "en_summary": "MIIT scrapped cascade-use rules and removed 100 listed firms from the compliance roster.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-04/102471177.html",
        },
        {
            "zh_title": "宇树科技科创板IPO启动初步询价",
            "en_title": "Unitree begins STAR Market IPO price inquiry",
            "published": "07:02 2026年8月5日",
            "zh_summary": "今日为初步询价日，拟发行4044.64万股，占发行后总股本10%，申购日为8月10日。",
            "en_summary": "Price inquiry runs today for 40.45m shares, 10% of post-IPO stock; subscription on Aug 10.",
            "source_zh": "21财经", "source_en": "21st Century Business Herald",
            "url": "https://m.21jingji.com/article/20260805/herald/0920ba3457d6b7017e2a1178fff13eed.html",
        },
    ]),
    ("finance", "财经 / 商业 Finance & Business", [
        {
            "zh_title": "特朗普称霍尔木兹海峡协议最早周三达成",
            "en_title": "Trump says Strait of Hormuz deal could come as early as Wednesday",
            "published": "13:35 2026年8月5日",
            "zh_summary": "美总统称与伊朗、阿曼谈判取得进展，或数日内宣布重开水道，油价随之回落。",
            "en_summary": "Trump cited progress with Iran and Oman that could reopen the vital shipping lane soon.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/iran-war-us-hormuz-trump-august-5-2026-ecdbd96f2b46c70beb5926d8508f9c55",
        },
        {
            "zh_title": "美股创新高，市场押注霍尔木兹有望恢复通航",
            "en_title": "US stocks hit records on Hormuz reopening hopes",
            "published": "10:09 2026年8月5日",
            "zh_summary": "标普500首次突破7700点，道指连创新高，油价隔夜大幅下挫后小幅反弹。",
            "en_summary": "The S&P 500 topped 7,700 while oil fell sharply overnight on diplomatic hopes.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/economy/2026/8/5/us-stock-market-hits-record-high-amid-hopes-for-strait-of-hormuz-reopening",
        },
        {
            "zh_title": "A股低开，沪指跌0.19%创业板指跌3.35%",
            "en_title": "China A-shares open lower; ChiNext drops 3.35%",
            "published": "09:29 2026年8月5日",
            "zh_summary": "通信板块领跌，有色金属、轻工制造等相对走强，市场关注美拟禁中国数通设备消息。",
            "en_summary": "Telecoms led losses while metals and light industry outperformed at the open.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://finance.caixin.com/2026-08-05/102471311.html",
        },
        {
            "zh_title": "国泰航空上半年净利润升71%至62.4亿港元",
            "en_title": "Cathay Pacific first-half profit rises 71% to HK$6.24bn",
            "published": "12:37 2026年8月5日",
            "zh_summary": "需求回暖推动业绩，集团警告中东冲突升级或再度推高燃油成本。",
            "en_summary": "Stronger demand lifted earnings, but Middle East tensions may push fuel costs higher.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363009/cathay-pacific-posts-71-profit-rise-hk624-billion-first-half-year",
        },
    ]),
    ("society", "社会 Society", [
        {
            "zh_title": "内塔尼亚胡称未接受美方加沙撤军草案",
            "en_title": "Netanyahu says Israel rejected US Gaza withdrawal draft",
            "published": "09:46 2026年8月5日",
            "zh_summary": "以总理称在哈马斯完全解除武装前不会从当前战线撤退，与美方方案存在分歧。",
            "en_summary": "PM said troops won't pull back until Hamas is fully disarmed, diverging from US plan.",
            "source_zh": "澳大利亚广播公司", "source_en": "ABC News",
            "url": "https://www.abc.net.au/news/2026-08-05/netanyahu-says-no-idf-withdrawal-from-gaza-until-hamas-disarms/106997846",
        },
        {
            "zh_title": "赴美中国留学生F-1签证发放量同比大减",
            "en_title": "New US F-1 visas for Chinese students fall sharply",
            "published": "12:10 2026年8月5日",
            "zh_summary": "2025年5至8月对华新签F-1签证约4万张，较2024年同期下降约34%。",
            "en_summary": "About 40,034 F-1 visas were issued May-Aug 2025, down roughly 34% from a year earlier.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://international.caixin.com/2026-08-05/102471342.html",
        },
        {
            "zh_title": "中消协：上半年为消费者挽回经济损失4.47亿元",
            "en_title": "China consumer association recovered 447m yuan for consumers in H1",
            "published": "09:56 2026年8月5日",
            "zh_summary": "全国消协组织上半年受理投诉985928件，调解成功率提升，维权效率继续改善。",
            "en_summary": "Consumer associations handled 985,928 complaints in the first half of 2026.",
            "source_zh": "财新网", "source_en": "Caixin",
            "url": "https://mini.caixin.com/2026-08-05/102471315.html",
        },
        {
            "zh_title": "美国撤销巴西驻美大使签证",
            "en_title": "US revokes visa of Brazil's ambassador in Washington",
            "published": "04:27 2026年8月5日",
            "zh_summary": "美方称系回应巴西拒签两名美外交官及拖延批准特朗普提名的新任美驻巴大使。",
            "en_summary": "State Department cited Brazil's visa denials and delay approving Trump's envoy pick.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/trump-brazil-lula-ambassador-diplomats-4d7f64110fff5dda2ffd374d5e52c682",
        },
    ]),
    ("world", "国际 World", [
        {
            "zh_title": "俄军导弹袭击基辅等地致17死44伤",
            "en_title": "Russian missile strikes on Kyiv region kill 17, wound 44",
            "published": "13:49 2026年8月5日",
            "zh_summary": "乌方称24枚弹道导弹未被拦截，泽连斯基再次呼吁盟友提供爱国者拦截弹药。",
            "en_summary": "Ukraine said 24 ballistic missiles weren't intercepted; Zelenskyy sought more Patriots.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/ukraine-war-russia-kyiv-patriot-ballistic-missile-64f8e53f9650d4104bb7375361abd990",
        },
        {
            "zh_title": "乌情报称朝鲜导弹部队部署至俄西部",
            "en_title": "Ukraine says North Korean missile unit deploying in western Russia",
            "published": "12:16 2026年8月5日",
            "zh_summary": "乌方称约90名朝方人员或编入俄112导弹旅，或配备120枚弹道导弹及6台发射器。",
            "en_summary": "Kyiv said ~90 North Korean personnel may join Russia's 112th Missile Brigade.",
            "source_zh": "路透社（经济时报）", "source_en": "Reuters (Economic Times)",
            "url": "https://economictimes.indiatimes.com/news/defence/north-korean-missile-unit-deploys-in-russia-for-ukraine-war-kyiv-says/articleshow/132889591.cms",
        },
        {
            "zh_title": "台湾启动年度“汉光41号”军演",
            "en_title": "Taiwan begins annual Han Kuang military drills",
            "published": "10:27 2026年8月5日",
            "zh_summary": "8月5至14日举行最大规模演习，含后备役实弹训练及民防网络限速等场景。",
            "en_summary": "Taiwan's largest annual drills run Aug 5-14, including reservist live-fire scenarios.",
            "source_zh": "法新社（France 24）", "source_en": "AFP (France 24)",
            "url": "https://www.france24.com/en/live-news/20260805-taiwan-begins-military-drills-as-china-pressure-grows",
        },
        {
            "zh_title": "乌无人机再袭俄Wildberries仓库致1伤",
            "en_title": "Ukrainian drone hits another Wildberries warehouse in Russia",
            "published": "00:00 2026年8月5日",
            "zh_summary": "图拉州一分拣中心起火，州长确认1人受伤；乌方称三周内已打击16处该品牌物流点。",
            "en_summary": "A sorting hub in Tula Oblast caught fire; one worker was injured, officials said.",
            "source_zh": "Euromaidan Press", "source_en": "Euromaidan Press",
            "url": "https://euromaidanpress.com/2026/08/05/ukraine-hits-16th-wildberries-warehouse-in-under-three-weeks-one-injured-overnight/",
        },
        {
            "zh_title": "中方称将继续协助非洲国家抗击埃博拉疫情",
            "en_title": "China pledges continued Ebola support for African nations",
            "published": "10:39 2026年8月5日",
            "zh_summary": "外交部称第三批医疗专家组已赴刚果（金），将与当地及国际组织加强防疫协作。",
            "en_summary": "Beijing said a third expert team reached DRC to bolster epidemic response efforts.",
            "source_zh": "中国日报香港版", "source_en": "China Daily HK",
            "url": "https://www.chinadailyhk.com/hk/article/637452",
        },
    ]),
    ("hk", "香港本地 Hong Kong", [
        {
            "zh_title": "34%港生经JUPAS获大学或副学位录取",
            "en_title": "34% of Hong Kong JUPAS applicants secure tertiary places",
            "published": "10:00 2026年8月5日",
            "zh_summary": "共45545人申请，15619人获录取，竞争加剧，申请人数同比上升约5.3%。",
            "en_summary": "15,619 of 45,545 applicants won places as competition intensified this year.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/education/article/3362970/34-hong-kong-students-win-university-diploma-spots-under-admissions-system",
        },
        {
            "zh_title": "香港测试热成像无人机查处工地违规吸烟",
            "en_title": "Hong Kong tests thermal drones to catch illegal site smoking",
            "published": "15:34 2026年8月5日",
            "zh_summary": "劳工处演示红外无人机远程识别热源，后续拟引入AI识别吸烟工人并加强执法。",
            "en_summary": "Labour officials demoed infrared drones and plan AI to spot smokers on sites.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363030/hong-kong-tests-thermal-drones-catch-illegal-smoking-construction-sites",
        },
        {
            "zh_title": "台风“白海豚”迫取消至少18班赴日航班",
            "en_title": "Typhoon Dolphin prompts cancellation of at least 18 Japan flights",
            "published": "12:26 2026年8月5日",
            "zh_summary": "周末发一号戒备信号概率低，但港航、快运等取消多条往返冲绳及石垣航班。",
            "en_summary": "Airlines axed Okinawa and Ishigaki routes though a local typhoon signal looks unlikely.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363005/typhoon-signal-unlikely-hong-kong-over-weekend-least-18-flights-japan-axed",
        },
        {
            "zh_title": "80艘港资船霍尔木兹滞留，船员获心理辅导",
            "en_title": "Crews on 80 HK-owned Hormuz ships safe, offered counselling",
            "published": "13:59 2026年8月5日",
            "zh_summary": "船东会称约1600名船员补给充足，但长期无法下船带来身心压力，已提供视频辅导。",
            "en_summary": "Shipowners said ~1,600 seafarers remain supplied but face mental strain after months.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363016/hong-kong-ship-crews-stranded-strait-hormuz-safe-and-offered-counselling",
        },
        {
            "zh_title": "私院饮水机检出军团菌，89岁病人疑似感染",
            "en_title": "Legionella found in Hong Kong private hospital water dispenser",
            "published": "01:02 2026年8月5日",
            "zh_summary": "养和医院冷却开水机样本超标，基因分型与患者呼吸道标本一致，137人受医学监察。",
            "en_summary": "Hong Kong Sanatorium dispensers tested positive; an 89-year-old patient was likely infected.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3362975/water-dispenser-linked-legionnaires-disease-case-private-hong-kong-hospital",
        },
    ]),
    ("other", "其他 Other", [
        {
            "zh_title": "丹麦公主伊莎贝拉开始11个月兵役",
            "en_title": "Denmark's Princess Isabella begins 11-month military service",
            "published": "01:18 2026年8月4日",
            "zh_summary": "19岁公主8月3日到岗，为丹麦首批纳入义务兵役的女性王室成员，自愿放弃薪饷。",
            "en_summary": "The 19-year-old started service Aug 3, forgoing conscript pay like her brother did.",
            "source_zh": "独立报（法新社）", "source_en": "The Independent (AFP)",
            "url": "https://www.independent.co.uk/news/world/europe/denmark-princess-isabella-military-conscription-b3026605.html",
        },
        {
            "zh_title": "RTHK：陈茂波指商品交易可服务国家并创造就业",
            "en_title": "Hong Kong FS says commodity trading serves nation and creates jobs",
            "published": "10:49 2026年8月5日",
            "zh_summary": "财政司司长称发展黄金等商品交易生态，可强化香港国际金融中心角色并带动就业。",
            "en_summary": "Paul Chan said a gold trading hub would bolster Hong Kong's financial centre role.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865044-20260805.htm",
        },
    ]),
]

SOURCE_COLORS = {
    "Xinhua": "#c0392b", "Caixin": "#2c3e50", "AP": "#e74c3c", "Reuters": "#f39c12",
    "SCMP": "#8e44ad", "BBC": "#c0392b", "Al Jazeera": "#d35400", "France 24": "#2980b9",
    "AFP": "#2980b9", "RTHK": "#16a085", "Independent": "#7f8c8d", "Japan Times": "#34495e",
    "China Daily": "#27ae60", "Euromaidan": "#2ecc71", "21st Century": "#1abc9c",
}


def source_color(source_en: str) -> str:
    for key, color in SOURCE_COLORS.items():
        if key.lower() in source_en.lower():
            return color
    return "#3498db"


def render_item(num: int, item: dict) -> str:
    color = source_color(item["source_en"])
    return f"""
<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
  <div style="color:#888;font-size:12px;font-weight:bold;margin-bottom:6px;">{num:02d}</div>
  <a href="{escape(item['url'])}" style="color:#1a1a1a;font-size:17px;font-weight:bold;text-decoration:none;line-height:1.4;">{escape(item['zh_title'])}</a>
  <div style="color:#555;font-size:15px;font-style:italic;margin-top:4px;line-height:1.4;">{escape(item['en_title'])}</div>
  <div style="color:#999;font-size:12px;margin-top:6px;">发布时间 Published: {escape(item['published'])}</div>
  <div style="color:#333;font-size:14px;margin-top:10px;line-height:1.6;">{escape(item['zh_summary'])}</div>
  <div style="color:#666;font-size:13px;margin-top:6px;line-height:1.5;">{escape(item['en_summary'])}</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:3px 8px;border-radius:3px;margin-right:8px;">{escape(item['source_zh'])} / {escape(item['source_en'])}</span>
    <a href="{escape(item['url'])}" style="color:#2980b9;font-size:13px;text-decoration:none;">查看全文 Read more →</a>
  </div>
</div>"""


def build_html() -> str:
    items_html = []
    n = 1
    cat_blocks = []
    for _key, cat_title, items in CATEGORIES:
        block = f"""
<div style="margin-bottom:28px;">
  <h2 style="background:#f0f2f5;border-left:4px solid #2980b9;padding:10px 14px;margin:0 0 16px 0;font-size:16px;color:#2c3e50;">{escape(cat_title)}</h2>
"""
        for item in items:
            block += render_item(n, item)
            n += 1
        block += "</div>"
        cat_blocks.append(block)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 2026-08-05</title></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#f4f4f4;">
<tr><td align="center" style="padding:20px 12px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a2332 0%,#2c3e50 100%);padding:28px 24px;text-align:center;">
  <div style="color:#ffffff;font-size:24px;font-weight:bold;letter-spacing:1px;">每日热点晚报</div>
  <div style="color:#bdc3c7;font-size:14px;margin-top:8px;">Evening News Briefing · 2026年8月5日 · 共{TOTAL_LABEL}条</div>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafbfc;border-bottom:1px solid #eee;">
  <div style="color:#333;font-size:14px;line-height:1.6;">汇总今日全日要闻，涵盖政策、市场、科技与全球热点。</div>
  <div style="color:#666;font-size:13px;margin-top:6px;line-height:1.5;">Today's main stories across policy, markets, technology and global affairs.</div>
</td></tr>
<tr><td style="padding:8px 24px 24px;">
{''.join(cat_blocks)}
</td></tr>
<tr><td style="padding:20px 24px;background:#f8f9fa;border-top:1px solid #eee;">
  <div style="color:#999;font-size:12px;line-height:1.6;text-align:center;">本简报仅供参考，不构成投资或法律建议。新闻链接指向第三方网站，请以原文为准。<br/>This briefing is for informational purposes only. Click through to original sources for full context.</div>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>"""


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {BRIEFING_DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    out = os.path.join(root, "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"HTML chars: {len(html)}")
    print(f"Total items: {int(TOTAL_LABEL)}")
    for _key, title, items in CATEGORIES:
        print(f"  {title.split()[0]}: {len(items)}")


if __name__ == "__main__":
    main()
