#!/usr/bin/env python3
"""Build morning briefing HTML and email_payload.json for 2026-08-07."""
import json
import os

BRIEFING_EDITION = "早报"
LOCAL_TIME = "07:30 2026年8月7日"
DATE_STR = "2026-08-07"

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "中方对Palo Alto Networks启动网络安全审查",
            "en_title": "China launches cybersecurity review of Palo Alto Networks",
            "published": "17:21 2026年8月6日",
            "zh_summary": "网信办称审查旨在保障关键信息基础设施安全；此前北京刚制裁多家美企并收紧无人机供应链。",
            "en_summary": "Beijing says the probe aims to secure critical infrastructure, days after sanctioning US firms and tightening drone supply chains.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/economy/global-economy/article/3363177/china-launches-probe-us-cybersecurity-firm-palo-alto-networks",
        },
        {
            "zh_title": "中国再购至少10船美国大豆，为习访美铺路",
            "en_title": "China buys at least 10 more cargoes of US soybeans",
            "published": "02:44 2026年8月7日",
            "zh_summary": "贸易商称中储粮周三购入10至15船，多数为10至11月装运；北京承诺年购2500万吨美豆。",
            "en_summary": "Traders say Sinograin bought 10-15 cargoes Wednesday, mostly for Oct-Nov shipment, ahead of Xi's expected US visit.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/world/united-states-canada/article/3363218/china-buys-least-10-more-cargoes-us-soybeans-traders-say",
        },
        {
            "zh_title": "中俄军舰绕日航行，东京称严重关切",
            "en_title": "Chinese and Russian warships circle Japan in joint patrol",
            "published": "14:41 2026年8月6日",
            "zh_summary": "日本防卫省称三艘中国军舰完成绕日航行；分析指意在展示未被第一岛链封锁及俄仍具远洋投送能力。",
            "en_summary": "Japan's defence ministry says three Chinese ships completed a circumnavigation; analysts see a show of force against Tokyo and Washington.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/china/military/article/3363143/their-warships-encircle-japan-what-signals-are-china-and-russia-sending",
        },
        {
            "zh_title": "北京首次对进口打印复印设备启动国安贸易调查",
            "en_title": "Beijing launches first national-security probe into imported printers",
            "published": "20:30 2026年8月6日",
            "zh_summary": "商务部依据外贸法第41条调查含外国软件办公设备，回应美方最新制裁并评估供应链安全风险。",
            "en_summary": "Commerce ministry probes imported printers and copiers with foreign software, its first national-security trade investigation.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/economy/policy/article/3363183/beijing-investigates-imported-office-equipment-response-us-sanctions-why-it-matters",
        },
    ]),
    ("科技 Technology", [
        {
            "zh_title": "AI首次设计出可实验室复制的新型病毒",
            "en_title": "AI used to design brand new functional viruses in lab",
            "published": "02:30 2026年8月7日",
            "zh_summary": "斯坦福团队用Evo模型合成16种噬菌体，可杀灭大肠杆菌；专家警告生物安全与滥用风险。",
            "en_summary": "Stanford researchers used Evo models to create 16 bacteriophages killing E. coli; experts warn of urgent biosecurity risks.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c5y3j3ngevmo",
        },
        {
            "zh_title": "韩国Danuri拍到SpaceX火箭撞月前后影像",
            "en_title": "South Korea's Danuri captures SpaceX rocket moon impact images",
            "published": "20:11 2026年8月6日",
            "zh_summary": "猎鹰9号上级残骸周三撞爱因斯坦坑附近月面；韩航天局称首次获取撞击前后对比图像。",
            "en_summary": "Korea's lunar orbiter captured before-and-after images of a Falcon 9 stage striking the moon near Einstein crater.",
            "source_zh": "韩国先驱报", "source_en": "The Korea Herald",
            "url": "https://www.koreaherald.com/article/10833503",
        },
        {
            "zh_title": "美议员调查DoorDash使用月之暗面Kimi模型",
            "en_title": "US lawmakers probe DoorDash use of Moonshot AI's Kimi model",
            "published": "00:00 2026年8月5日",
            "zh_summary": "华盛顿担忧中国AI模型在美扩散；外卖巨头成为最新被审查采用中国技术的美国企业之一。",
            "en_summary": "Lawmakers investigate DoorDash's use of Moonshot's Kimi K2.6 as Washington scrutinizes Chinese AI adoption by US firms.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/china/diplomacy/article/3362616/us-lawmakers-investigate-doordashs-use-moonshot-ais-kimi-k26-model",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "美股周四收跌，道指跌0.9%",
            "en_title": "US stocks edge lower as oil rises on Thursday",
            "published": "04:30 2026年8月7日",
            "zh_summary": "标普跌0.2%至7709.96点，道指跌464点至53885.10点；布伦特原油涨近4%，美债收益率走高。",
            "en_summary": "S&P 500 fell 0.2% to 7,709.96 and Dow dropped 0.9%; Brent crude rose nearly 4% amid Iran war uncertainty.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/stock-market-dow-warner-dow-jones-b13b60e192e74e6dc6ab222dc296b5d2",
        },
        {
            "zh_title": "欧股STOXX 600三连创新高",
            "en_title": "European shares close at record high for third session",
            "published": "00:51 2026年8月7日",
            "zh_summary": "泛欧斯托克600涨0.2%至658.19点；德电大涨6%，二季度盈利超预期并扩大回购至50亿欧元。",
            "en_summary": "STOXX 600 rose 0.2% to a record 658.19; Deutsche Telekom surged 6% on strong earnings and a bigger buyback.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://lufkindailynews.com/news_reuters/business/european-shares-extend-run-of-record-highs-on-earnings-us-iran-optimism/article_9712c6fb-2dc4-5d8f-8f3d-8651b7359b40.html",
        },
        {
            "zh_title": "港股周四跌1.5%，科技股承压",
            "en_title": "Hong Kong stocks slip 1.5% as tech retreat deepens",
            "published": "16:30 2026年8月6日",
            "zh_summary": "恒生指数收报25530点，科技指数跌2.3%；韩股KOSPI重挫4.6%，亚洲科技股普遍回调。",
            "en_summary": "Hang Seng fell 1.5% to 25,530; tech index dropped 2.3% as Seoul's Kospi plunged 4.6% amid AI profit worries.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865235-20260806.htm",
        },
        {
            "zh_title": "港险股大跌，财长称对港险产品有信心",
            "en_title": "HK insurers slide; minister confident in insurance products",
            "published": "19:09 2026年8月6日",
            "zh_summary": "传内地对离岸保单收益征20%税，友邦跌6%；许正宇称将与内地部门保持沟通，对产品设计有信心。",
            "en_summary": "AIA fell 6% on reports of 20% tax on offshore policy earnings; minister Hui said he remains confident in HK products.",
            "source_zh": "香港电台", "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865248-20260806.htm",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "广岛纪念原子弹爆炸81周年，市长呼吁弃核",
            "en_title": "Hiroshima marks 81st atomic bombing anniversary",
            "published": "08:15 2026年8月6日",
            "zh_summary": "约5万人出席纪念仪式，8时15分默哀；市长批评核威慑论，高市早苗称将以现实路径追求无核世界。",
            "en_summary": "About 50,000 attended the ceremony; the mayor deplored nuclear deterrence as PM Takaichi pledged a realistic approach.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/japan-hiroshima-atomic-bomb-1d0af8bb88ad9ccd8958f751937ec6b0",
        },
        {
            "zh_title": "英国Thetford反移民骚乱进入第三晚",
            "en_title": "Thetford anti-immigration disorder continues for third night",
            "published": "07:25 2026年8月7日",
            "zh_summary": "诺福克警方再拘两人，累计五人；周三晚一名女警被严重咬伤，人群试图冲击疑似安置难民住所。",
            "en_summary": "Norfolk Police made two more arrests; a female officer was seriously bitten as crowds targeted homes linked to asylum seekers.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c74g1gxvwlvo",
        },
        {
            "zh_title": "阿姆斯特丹骄傲节举办一日婚礼活动",
            "en_title": "Dozens wed for a day at Amsterdam Pride event",
            "published": "00:00 2026年8月6日",
            "zh_summary": "活动纪念荷兰同性婚姻合法25周年；组织者称爱有多种形态，但该国整体结婚率持续下降。",
            "en_summary": "The Married For A Day event marked 25 years since the Netherlands legalized same-sex marriage, though overall marriage rates are falling.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/pride-lgbtqi-amsterdam-wedding-marriage-a37f60c46c36c8c20e72a07fa4087c3b",
        },
        {
            "zh_title": "斯托克波特青年团体联手反持刀犯罪",
            "en_title": "Stoke youth groups unite to tackle knife crime",
            "published": "21:30 2026年8月6日",
            "zh_summary": "当地组织在暑假举办教育活动，回应7月公园致命刺伤案；前警长称假期青少年更需社区支持。",
            "en_summary": "Groups held a summer engagement event after a fatal July stabbing; a former police chief urged more support for vulnerable youth.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c0m7pyekpgxo",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "乌军远程打击俄两座炼油厂，雅罗斯拉夫尔浓烟蔽日",
            "en_title": "Ukraine hits two Russian oil refineries in long-range attacks",
            "published": "06:00 2026年8月7日",
            "zh_summary": "泽连斯基确认袭击雅罗斯拉夫尔和巴什科尔托斯坦炼油厂；俄方称拦截逾600架无人机，乌方至少11人死亡。",
            "en_summary": "Zelensky confirmed strikes on refineries in Yaroslavl and Bashkortostan; Russia says it downed 600+ drones as Ukraine reports 11 dead.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/live/c242dmen8y3t",
        },
        {
            "zh_title": "美伊称霍尔木兹协议接近，但分歧仍存",
            "en_title": "US and Iran say Hormuz deal is near but hurdles remain",
            "published": "00:00 2026年8月6日",
            "zh_summary": "伊朗称与阿曼草拟协议进入最后阶段；美方此前反对伊朗控制航道并征收通行费，协议或取决于解除港口封锁。",
            "en_summary": "Iran says a draft deal with Oman is in final stages; the US has opposed Iranian control and transit fees on the vital strait.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/iran-war-us-hormuz-trump-august-5-2026-ecdbd96f2b46c70beb5926d8508f9c55",
        },
        {
            "zh_title": "特朗普否认美军弹药短缺并威胁起诉泄密者",
            "en_title": "Trump denies US weapons shortage, vows to jail leakers",
            "published": "02:30 2026年8月7日",
            "zh_summary": "特朗普称美军弹药充足且正加速生产；此前媒体称伊战消耗大量远程精确导弹库存。",
            "en_summary": "Trump insists US munitions are ample and leakers face jail; media reported depleted long-range missile stocks from the Iran war.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cy8mjd19xm7o",
        },
        {
            "zh_title": "麦康奈尔出院回家继续康复",
            "en_title": "Senator Mitch McConnell discharged from rehab center",
            "published": "04:03 2026年8月7日",
            "zh_summary": "肯塔基共和党参议员6月中旬跌倒住院后今日出院；称将在参议院休会期居家接受密集物理治疗。",
            "en_summary": "The Kentucky Republican was discharged Thursday after a mid-June fall; he will continue intensive physical therapy at home.",
            "source_zh": "ABC新闻", "source_en": "ABC News",
            "url": "https://abcnews.com/Politics/mcconnell-discharged-rehab-facility/story?id=135434047",
        },
        {
            "zh_title": "欧足联称世界杯抵制威胁仍有效",
            "en_title": "Uefa says World Cup boycott threat still stands",
            "published": "00:30 2026年8月7日",
            "zh_summary": "英足总撤回对因凡蒂诺连任支持；欧足联称撤销商业化方案不足以解除抵制，需保证不再重演。",
            "en_summary": "England's FA withdrew support for Infantino; Uefa says scrapping the investment plan alone does not meet its boycott conditions.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/sport/football/articles/c2k74yevgzwo",
        },
        {
            "zh_title": "刚果拦截埃博拉疑似客船，255人接受筛查",
            "en_title": "DR Congo quarantines river boat over Ebola fears",
            "published": "22:30 2026年8月6日",
            "zh_summary": "盈丰2号在金沙萨上游被截停；一名下船乘客死亡，当局对全船进行埃博拉与霍乱检测，疫情已致1801人死亡。",
            "en_summary": "The Yingfeng 2 was halted near Kinshasa; 255 passengers are being screened after a traveller died with Ebola-like symptoms.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/ce971plr2nvo",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "跑马地泳池因救生员证件造假被勒令关闭",
            "en_title": "Happy Valley pool shut over fake lifeguard credentials",
            "published": "00:43 2026年8月7日",
            "zh_summary": "食环署指救生员资格与救生总会记录不符，泳池缺乏法定救生员人数；案件已转交警方调查。",
            "en_summary": "FEHD ordered the pool closed after a lifeguard's credentials did not match official records; police are investigating.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3363215/pool-hong-kongs-happy-valley-shut-over-suspected-fake-lifeguard-credentials",
        },
        {
            "zh_title": "民建联促修订生殖科技条例加强胚胎核查",
            "en_title": "DAB urges overhaul of reproductive tech law after embryo mix-up",
            "published": "21:06 2026年8月6日",
            "zh_summary": "议员建议胚胎活检各环节实行双人核对并书面记录；上月希复生育诊所因样本混淆被暂停大部分业务。",
            "en_summary": "Lawmakers propose two-person verification at every embryo biopsy step after a rare specimen mix-up at a fertility clinic.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363205/more-checks-embryo-biopsies-overhaul-reproductive-tech-law-dab-urges",
        },
        {
            "zh_title": "警方捣毁年息282%高利贷集团拘25人",
            "en_title": "HK police bust loan shark ring charging 282% interest",
            "published": "12:45 2026年8月6日",
            "zh_summary": "集团一年放贷约2亿港元，招募13岁少年恐吓欠债人；警方搜查旺角及火炭三个运作中心。",
            "en_summary": "Police arrested 25 people in a triad-linked syndicate that lent HK$200m at annual rates up to 282%, recruiting teens to intimidate debtors.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363126/25-arrested-hong-kong-police-bust-loan-shark-ring-charging-282-interest-rate",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "柬埔寨泰国同意东盟观察员监督停火",
            "en_title": "Cambodia and Thailand agree to ASEAN ceasefire observers",
            "published": "00:00 2026年8月7日",
            "zh_summary": "两国国防部长在吉隆坡会晤，同意由东盟武官观察边境；两周后将举行下一轮会谈巩固停火。",
            "en_summary": "Defence ministers met in Kuala Lumpur and agreed ASEAN military attaches will monitor disputed border areas after July's ceasefire.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://www.reuters.com/world/asia-pacific/cambodia-thailand-agree-asean-observers-ensure-ceasefire-holds-2025-08-07/",
        },
        {
            "zh_title": "危地马拉富埃戈火山喷发，1700人避难",
            "en_title": "Guatemala evacuates 1,700 as Fuego volcano erupts",
            "published": "00:00 2026年8月5日",
            "zh_summary": "当局对萨卡特佩克斯等三省发布红色警报，学校停课；火山泥流最长可达7公里，未来72小时风险仍高。",
            "en_summary": "Authorities raised red alerts in three provinces; about 1,700 people remain in shelters as mudflows up to 7km long continue.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/fuego-volcano-guatemala-eruption-evacuation-d4791ca218180a2daa42a3b09673a52c",
        },
    ]),
]

SOURCE_COLORS = {
    "SCMP": "#c41e3a", "南华早报": "#c41e3a",
    "BBC": "#bb1919",
    "AP": "#d32f2f", "美联社": "#d32f2f",
    "Reuters": "#ff8c00", "路透社": "#ff8c00",
    "RTHK": "#0066cc", "香港电台": "#0066cc",
    "ABC News": "#003366", "ABC新闻": "#003366",
    "The Korea Herald": "#1a5276", "韩国先驱报": "#1a5276",
}


def build_html():
  all_items = []
  for cat_name, items in CATEGORIES:
    for item in items:
      all_items.append((cat_name, item))
  total = len(all_items)

  parts = [f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>每日热点早报 Morning Briefing - {DATE_STR}</title></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;"><tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.1);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a237e,#283593);padding:28px 24px;text-align:center;">
<h1 style="margin:0 0 6px;color:#fff;font-size:24px;font-weight:700;">每日热点早报</h1>
<p style="margin:0;color:#e8eaf6;font-size:14px;">Morning News Briefing · {DATE_STR} · 共 {total} 条</p>
</td></tr>
<tr><td style="padding:20px 24px;background:#fafafa;border-bottom:1px solid #e0e0e0;">
<p style="margin:0 0 8px;color:#333;font-size:14px;line-height:1.6;">汇总昨夜至今要闻，涵盖国际局势、市场动态与两岸及香港热点。</p>
<p style="margin:0;color:#666;font-size:13px;line-height:1.5;font-style:italic;">Overnight and early headlines on world affairs, markets, and Greater China developments.</p>
</td></tr>''']

  num = 0
  current_cat = None
  for cat_name, item in all_items:
    if cat_name != current_cat:
      current_cat = cat_name
      parts.append(f'''<tr><td style="padding:20px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f5f5f5;border-left:4px solid #1565c0;font-size:16px;color:#1a237e;">{cat_name}</h2>
</td></tr>''')
    num += 1
    color = SOURCE_COLORS.get(item["source_en"], SOURCE_COLORS.get(item["source_zh"], "#607d8b"))
    parts.append(f'''<tr><td style="padding:12px 24px;border-bottom:1px solid #eee;">
<div style="font-size:11px;color:#1565c0;font-weight:700;margin-bottom:4px;">{num:02d}</div>
<a href="{item['url']}" style="color:#1a237e;font-size:15px;font-weight:600;text-decoration:none;line-height:1.4;">{item['zh_title']}</a>
<p style="margin:4px 0 2px;color:#555;font-size:13px;font-style:italic;">{item['en_title']}</p>
<p style="margin:0 0 8px;color:#999;font-size:11px;">发布时间 Published: {item['published']}</p>
<p style="margin:0 0 4px;color:#333;font-size:13px;line-height:1.6;">{item['zh_summary']}</p>
<p style="margin:0 0 10px;color:#666;font-size:12px;line-height:1.5;font-style:italic;">{item['en_summary']}</p>
<span style="display:inline-block;background:{color};color:#fff;font-size:10px;padding:2px 8px;border-radius:3px;margin-right:8px;">{item['source_zh']} / {item['source_en']}</span>
<a href="{item['url']}" style="color:#1565c0;font-size:12px;text-decoration:none;">查看全文 Read more →</a>
</td></tr>''')

  parts.append('''<tr><td style="padding:20px 24px;background:#f5f5f5;border-top:1px solid #e0e0e0;">
<p style="margin:0 0 6px;color:#888;font-size:11px;line-height:1.5;">本简报由自动化系统汇编，仅供参考，不构成投资或法律建议。新闻版权归原媒体所有。</p>
<p style="margin:0;color:#aaa;font-size:10px;font-style:italic;">This briefing is auto-compiled for reference only. All rights belong to original publishers.</p>
</td></tr>
</table></td></tr></table></body></html>''')
  return "".join(parts), total


def main():
  html, total = build_html()
  payload = {
    "subject": f"每日热点早报 Morning Briefing - {DATE_STR}",
    "htmlContent": html,
    "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
  }
  root = os.path.join(os.path.dirname(__file__), "..")
  payload_path = os.path.join(root, "email_payload.json")
  with open(payload_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
  counts = {cat: len(items) for cat, items in CATEGORIES}
  print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
  print(f"LOCAL_TIME={LOCAL_TIME}")
  print(f"TOTAL={total}")
  print(f"COUNTS={counts}")
  print(f"HTML_CHARS={len(html)}")
  print(f"PAYLOAD={payload_path}")


if __name__ == "__main__":
  main()
