#!/usr/bin/env python3
"""Build 2026-08-18 morning briefing payload. Do not commit email_payload.json."""
import json
import os

SUBJECT = "每日热点早报 Morning Briefing - 2026-08-18"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点早报 Morning News Briefing · 2026年8月18日</title>
</head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;color:#1a1a1a;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef1f5;padding:16px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 6px 24px rgba(15,23,42,.12);">
<tr><td style="background:#0f172a;padding:22px 24px 18px;color:#fff;">
<div style="font-size:12px;letter-spacing:1px;color:#94a3b8;margin-bottom:6px;">18 AUGUST 2026 · ASIA/SHANGHAI</div>
<div style="font-size:24px;font-weight:700;line-height:1.3;">每日热点早报</div>
<div style="font-size:15px;color:#cbd5e1;margin-top:4px;">Morning News Briefing · 2026年8月18日 · 共 28 条</div>
</td></tr>
<tr><td style="padding:16px 24px 8px;font-size:14px;line-height:1.7;color:#334155;border-bottom:1px solid #e2e8f0;">
汇总昨夜至今要闻，涵盖隔夜美欧收盘、霍尔木兹局势、开盘前政策与突发。<br>
<span style="color:#64748b;">Overnight and early headlines, from Wall Street’s close and Hormuz tensions to morning policy and breaking news.</span>
</td></tr>
"""

def section(title_zh, title_en):
    return f"""<tr><td style="padding:14px 24px 6px;">
<div style="background:#f1f5f9;border-left:4px solid #2563eb;padding:8px 12px;border-radius:0 6px 6px 0;">
<h2 style="margin:0;font-size:16px;color:#0f172a;">{title_zh} <span style="font-weight:500;color:#64748b;font-size:13px;">{title_en}</span></h2>
</div></td></tr>
"""

def item(n, url, zh, en, ts, zhs, ens, src, color):
    return f"""<tr><td style="padding:10px 24px 12px;border-bottom:1px solid #f1f5f9;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr>
<td valign="top" style="width:36px;font-weight:700;color:#2563eb;font-size:15px;padding-top:2px;">{n}</td>
<td>
<a href="{url}" style="color:#0f172a;text-decoration:none;font-size:15px;font-weight:700;line-height:1.45;">{zh}</a>
<div style="font-style:italic;color:#475569;font-size:13px;margin-top:3px;">{en}</div>
<div style="color:#94a3b8;font-size:12px;margin-top:3px;">发布时间 Published: {ts}</div>
<div style="font-size:13px;line-height:1.65;color:#334155;margin-top:6px;">{zhs}<br>
<span style="color:#64748b;">{ens}</span></div>
<div style="margin-top:8px;">
<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:10px;margin-right:8px;">{src}</span>
<a href="{url}" style="color:#2563eb;font-size:12px;text-decoration:none;font-weight:600;">查看全文 Read more →</a>
</div>
</td></tr></table>
</td></tr>
"""

HTML += section("国内 / 内地", "China Mainland")
HTML += item("01","https://news.rthk.hk/rthk/ch/component/k2/1866533-20260818.htm",
"朱镕基遗体今日火化，天安门及港澳降半旗志哀",
"Zhu Rongji cremated as flags fly at half-staff in Beijing and Hong Kong",
"08:14 2026年8月18日",
"国务院原总理朱镕基遗体今日在北京火化，天安门及港澳等地降半旗志哀。",
"Former premier Zhu Rongji was cremated in Beijing today as flags flew at half-staff nationwide, including in Hong Kong and Macao.",
"香港电台 RTHK","#0f766e")
HTML += item("02","https://www.xinhuanet.com/politics/leaders/20260817/3b4128a7dc6146039767bcb4bb6564de/c.html",
"李强主持国务院全体会议：努力完成全年目标",
"Li Qiang urges State Council to meet full-year economic targets",
"19:45 2026年8月17日",
"李强主持国务院全体会议，要求用好存量政策并及时出台增量措施，努力完成全年目标。",
"Premier Li Qiang told a State Council meeting to deploy existing tools and add measures as needed to meet this year’s goals.",
"新华社 Xinhua","#dc2626")
HTML += item("03","https://www.caixinglobal.com/2026-08-18/chinas-new-home-prices-weaken-again-as-recovery-in-smaller-cities-falters-102475179.html",
"中国七月新房价再度走弱，二线修复失速",
"China’s new-home prices weaken again as smaller-city rebound fades",
"04:21 2026年8月18日",
"官方数据显示，七月新建商品住宅价格再度走弱，二线城市早前修复势头未能保持。",
"China’s new-home prices weakened again in July as an earlier rebound in smaller cities lost momentum, official data showed.",
"财新 Caixin","#ea580c")
HTML += item("04","https://www.caixinglobal.com/2026-08-18/china-maps-out-oil-and-gas-buildout-through-2030-to-strengthen-energy-security-102475175.html",
"中国公布油气发展至2030年规划，强化能源安全",
"China maps oil and gas buildout through 2030 for energy security",
"03:35 2026年8月18日",
"中国公布石油天然气“十五五”规划，提出扩大国内产量、管网与储备以增强能源安全。",
"Beijing outlined an oil-and-gas plan through 2030, aiming to expand domestic output, pipelines and storage for energy security.",
"财新 Caixin","#ea580c")

HTML += section("科技 / 互联网", "Technology")
HTML += item("05","https://www.reuters.com/business/media-telecom/nvidia-invest-15-billion-sb-energy-under-openai-data-center-deal-2026-08-17/",
"英伟达为OpenAI俄亥俄数据中心提供最高1050亿美元担保",
"Nvidia to provide up to $105 billion guarantee for OpenAI Ohio campus",
"20:43 2026年8月17日",
"英伟达同意为OpenAI租用的俄亥俄州数据中心提供最高约1050亿美元担保，并投资15亿美元。",
"Nvidia will guarantee up to $105 billion for OpenAI’s Ohio data center and invest $1.5 billion in developer SB Energy.",
"路透社 Reuters","#f59e0b")
HTML += item("06","https://www.reuters.com/legal/transactional/alibaba-sell-lingxi-games-more-than-2-billion-deal-source-says-2026-08-17/",
"阿里巴巴逾20亿美元出售灵犀互娱予信宸资本",
"Alibaba to sell Lingxi Games to Trustar in more than $2 billion deal",
"12:00 2026年8月17日",
"知情人士称，阿里巴巴将游戏公司灵犀互娱出售予信宸资本，交易对价超过20亿美元。",
"Alibaba agreed to sell game studio Lingxi to Trustar Capital in a deal expected to fetch more than $2 billion, a source said.",
"路透社 Reuters","#f59e0b")
HTML += item("07","https://finance.caixin.com/2026-08-17/102475129.html",
"长鑫科技市值突破4万亿元，登顶中国上市公司",
"Changxin Memory tops 4 trillion yuan, becoming China’s most valuable stock",
"20:48 2026年8月17日",
"长鑫科技收涨12%，总市值升至约4.13万亿元，登顶A股并超过港股腾讯。",
"Changxin Memory jumped 12%, lifting its value to about 4.13 trillion yuan and making it China’s most valuable listed firm.",
"财新 Caixin","#ea580c")
HTML += item("08","https://www.scmp.com/news/hong-kong/society/article/3364317/hong-kong-halves-environmental-impact-review-times-ai-efficiency-drive",
"香港用人工智能将环评时间缩短约一半",
"Hong Kong halves environmental review times with AI efficiency drive",
"19:20 2026年8月17日",
"港府称应用人工智能后，环评所需时间可由三至四年缩短至约十五至二十四个月。",
"Hong Kong said AI has cut environmental impact assessment timelines from 36–48 months to about 15–24 months.",
"南华早报 SCMP","#0284c7")

HTML += section("财经 / 商业", "Finance &amp; Business")
HTML += item("09","https://apnews.com/article/wall-street-stocks-dow-nasdaq-b20808a2f37a7c505013c9b301c8ebe0",
"美股周一收低，油价上涨令通胀担忧升温",
"Wall Street slips from records as rising oil prices pressure markets",
"04:41 2026年8月18日",
"周一美股收低，标普500跌0.5%，道指跌273点，油价上涨令通胀担忧升温。",
"U.S. stocks slipped Monday, with the S&amp;P 500 down 0.5% and the Dow off 273 points as higher oil revived inflation worries.",
"美联社 AP","#1d4ed8")
HTML += item("10","https://news.rthk.hk/rthk/en/component/k2/1866545-20260818.htm",
"港股早盘下跌，伊朗战事担忧拖累风险资产",
"Hong Kong stocks slip amid Iran war fears as Asian markets open",
"10:43 2026年8月18日",
"恒生指数早盘跌约197点或0.78%，伊朗停火到期及“全面进攻”表态拖累风险资产。",
"Hong Kong’s Hang Seng Index fell about 0.78% in early trade after a U.S.-Iran truce expired and Tehran signaled an offensive shift.",
"香港电台 RTHK","#0f766e")
HTML += item("11","https://news.rthk.hk/rthk/ch/component/k2/1866520-20260818.htm",
"国际油价升逾2%，布伦特收报90.87美元",
"Oil rises more than 2% as Middle East diplomacy remains stalled",
"05:54 2026年8月18日",
"布伦特原油收报每桶90.87美元，升近2.7%，美伊外交停滞及霍尔木兹航运受限提供支撑。",
"Brent crude settled at $90.87 a barrel, up nearly 2.7%, as U.S.-Iran diplomacy stalled and Hormuz shipping stayed constrained.",
"香港电台 RTHK","#0f766e")
HTML += item("12","https://www.aa.com.tr/en/economy/european-stocks-close-mostly-lower-amid-rising-bond-yields-geopolitical-tensions/4029776",
"欧股多数收跌，斯托克600连跌四个交易日",
"European stocks close mostly lower amid yields and geopolitical tension",
"03:46 2026年8月18日",
"欧洲主要股指收跌，斯托克600跌0.22%；德国DAX跌近0.4%，法国CAC跌近0.7%。",
"European shares closed lower, with the STOXX 600 down 0.22%, Germany’s DAX off about 0.4% and France’s CAC down nearly 0.7%.",
"阿纳多卢通讯社 Anadolu","#b45309")

HTML += section("社会", "Society")
HTML += item("13","https://www.caixin.com/2026-08-18/102475186.html",
"医保局明确158个基层病种，同病同价引导下沉",
"China sets equal insurance pay for 158 conditions to steer care to clinics",
"07:21 2026年8月18日",
"国家医保局将推出158个基层病种，不同等级医院执行相同支付标准，引导常见病下沉基层。",
"China’s medical insurer will apply the same payment rates at all hospital levels for 158 common conditions to steer care to clinics.",
"财新 Caixin","#ea580c")
HTML += item("14","https://www.bbc.com/news/articles/cx2rzx5g5yro",
"法国总理视察火烧区遭起哄，宣布1200万欧元援助",
"French PM heckled over wildfire response as blazes continue across Europe",
"02:00 2026年8月18日",
"法国总理勒科尔尼视察西南部火烧区遭居民起哄，并宣布向吉伦特与朗德提供1200万欧元援助。",
"French PM Sébastien Lecornu was heckled in wildfire-hit Gironde as he announced €12 million in immediate rebuilding aid.",
"英国广播公司 BBC","#b91c1c")
HTML += item("15","https://aa.com.tr/en/asia-pacific/over-50-injured-in-explosion-near-school-in-kabul/4029838",
"喀布尔学校附近手榴弹爆炸，据报逾50人受伤",
"Over 50 injured in grenade explosion near a school in Kabul",
"00:00 2026年8月17日",
"喀布尔一所私立学校附近发生手榴弹爆炸，当地媒体称逾50人受伤，警方已展开调查。",
"A grenade exploded near a private school in Kabul, injuring more than 50 people, Afghan media reported, as police opened an inquiry.",
"阿纳多卢通讯社 Anadolu","#b45309")
HTML += item("16","https://www.bbc.co.uk/news/articles/crl7686r71yo",
"印尼弗洛勒斯地震68死，救援受阻恐现物资短缺",
"Indonesia quake leaves aid shortages and starvation fears as aftershocks hit",
"16:38 2026年8月17日",
"印尼弗洛勒斯7.7级地震已造成至少68人死亡，余震不断，部分村落仍缺医少药、恐现饥荒。",
"Indonesia’s Flores quake has killed at least 68 people, with aftershocks, aid delays and growing fears of shortages among the displaced.",
"英国广播公司 BBC","#b91c1c")

HTML += section("国际", "World")
HTML += item("17","https://www.reuters.com/world/middle-east/iran-threatens-go-offensive-strait-hormuz-if-diplomacy-with-us-fails-2026-08-17/",
"伊朗称若外交失败将转“全面进攻”，美国拒绝延长停火",
"Iran threatens fully offensive posture in Hormuz as U.S. rejects ceasefire extension",
"05:00 2026年8月18日",
"伊朗高级官员对路透社称，因永久停战谈判停滞，德黑兰将转向“全面进攻”姿态，美方拒绝延长临时停火。",
"A senior Iranian official told Reuters Tehran will shift to a “fully offensive” posture as Washington ruled out extending a ceasefire.",
"路透社 Reuters","#f59e0b")
HTML += item("18","https://www.bbc.com/news/articles/cy5dzk0ryzdo",
"特朗普威胁若阿曼“挡道”将轰炸这一美国盟友",
"Trump threatens to bomb U.S. ally Oman if it ‘gets in the way’ over Iran",
"22:36 2026年8月17日",
"福克斯新闻引述特朗普称，若阿曼“挡道”，美国将轰炸这一盟友；他同时拒绝延长美伊谅解备忘录。",
"President Trump threatened to bomb U.S. ally Oman if it “gets in the way” of Iran talks, and said he would not extend the MoU.",
"英国广播公司 BBC","#b91c1c")
HTML += item("19","https://kyivindependent.com/fires-reported-near-moscow-as-ukraine-launches-dozens-of-drones-towards-russian-capital/",
"乌克兰对莫斯科州发动大规模无人机袭击，多处起火",
"Fires reported near Moscow after Ukraine launches a large overnight drone wave",
"08:53 2026年8月18日",
"乌克兰对莫斯科州发动大规模无人机袭击，市长称击落至少187架，当地报告多处起火。",
"Ukraine launched a large overnight drone assault on the Moscow region; the mayor said at least 187 drones were shot down.",
"基辅独立报 Kyiv Independent","#2563eb")
HTML += item("20","https://www.bbc.com/news/articles/cy5dz0kkn0wo",
"俄罗斯警告英国：向乌克兰提供无人机将付出代价",
"Russia warns UK over supplying drones used in strikes inside Russia",
"09:16 2026年8月18日",
"俄罗斯指责英国向乌克兰提供的无人机用于袭击俄境目标，称伦敦须为此付出代价；英方表示坚定支持乌克兰。",
"Moscow accused Britain of escalating the war by supplying drones used inside Russia; the UK said it stands with Ukraine.",
"英国广播公司 BBC","#b91c1c")
HTML += item("21","http://www.news.cn/world/20260818/359b89cd48e141b798414423c714e659/c.html",
"库什纳会见内塔尼亚胡，以方同意成立加沙工作组",
"Kushner meets Netanyahu to advance Gaza plan as Israel forms working groups",
"00:27 2026年8月18日",
"库什纳在耶路撒冷会见内塔尼亚胡，以方同意成立哈马斯解除武装与加沙民生两个工作组。",
"Jared Kushner met Benjamin Netanyahu in Jerusalem; Israel agreed to working groups on Hamas disarmament and Gaza humanitarian needs.",
"新华社 Xinhua","#dc2626")

HTML += section("香港本地", "Hong Kong")
HTML += item("22","https://news.rthk.hk/rthk/ch/component/k2/1866534-20260818.htm",
"香港邮政削开支，试用期满员工改签两年合约",
"Hongkong Post to put probation-leavers on two-year contracts to cut costs",
"08:23 2026年8月18日",
"香港邮政称因收入不敷支出，九月期满试用员工改以两年公务员合约聘用，不再获长期聘用条款。",
"Hongkong Post will renew September probation-leavers on two-year civil-service contracts rather than permanent terms, citing losses.",
"香港电台 RTHK","#0f766e")
HTML += item("23","https://www.scmp.com/news/hong-kong/society/article/3364329/2-hygiene-officers-under-investigation-smoking-public-while-uniform",
"两名食环署人员穿制服当街吸烟，署方展开纪律调查",
"Two hygiene officers investigated for smoking in public while in uniform",
"21:20 2026年8月17日",
"食环署确认网上片段中两名小贩管理队员穿制服在街上吸烟，已按部门规定展开纪律调查。",
"Hong Kong’s hygiene department is investigating two hawker-control officers filmed smoking in uniform, which staff rules forbid.",
"南华早报 SCMP","#0284c7")
HTML += item("24","https://news.rthk.hk/rthk/en/component/k2/1866464-20260817.htm",
"民建联建议高才通转向产业导向并新增类别",
"DAB says Hong Kong talent schemes should be industry-driven",
"18:19 2026年8月17日",
"民建联建议高才通由“数量驱动”转向产业导向，削减C类名额并新增新质生产力相关类别。",
"The DAB urged Hong Kong to shift talent visas toward industry needs, cutting Category C quotas and adding a new-quality-forces track.",
"香港电台 RTHK","#0f766e")
HTML += item("25","https://finance.caixin.com/2026-08-18/102475000.html",
"香港ZD Group爆发约十亿港元级IPO兑付危机",
"ZD Group faces Hong Kong IPO repayment crunch of about HK$1 billion",
"07:27 2026年8月18日",
"财新报道，ZD Group在港参与的新股项目出现约十亿港元级兑付困难，关联账户据报遭冻结。",
"Caixin reported that ZD Group’s Hong Kong IPO-linked investments face a repayment crunch of about HK$1 billion after accounts were frozen.",
"财新 Caixin","#ea580c")

HTML += section("其他", "Other")
HTML += item("26","https://www.bbc.com/news/articles/c4g3qdj1z77o",
"挪威国王哈拉尔入院并病假两周，王储任摄政",
"Norway’s King Harald admitted to hospital and placed on two weeks’ sick leave",
"05:34 2026年8月18日",
"挪威国王哈拉尔因溶血性贫血治疗引发体液潴留入院，将病假两周，由王储哈康担任摄政。",
"Norway’s King Harald was hospitalized for fluid retention after anemia treatment and placed on two weeks’ sick leave, with Haakon as regent.",
"英国广播公司 BBC","#b91c1c")
HTML += item("27","https://www.bbc.co.uk/news/articles/crl7600rpnko",
"美加关税期限将至，卡尼称谈判“微妙而紧张”",
"U.S.-Canada trade talks intense as 50% tariff deadline looms on Wednesday",
"08:02 2026年8月18日",
"美加密集磋商以避免周三对约200亿美元加国商品加征最高50%关税，卡尼称谈判“非常微妙而紧张”。",
"Canada is racing to avert 50% U.S. tariffs on about $20 billion of goods due Wednesday, with Prime Minister Carney calling talks “intense.”",
"英国广播公司 BBC","#b91c1c")
HTML += item("28","https://news.rthk.hk/rthk/ch/component/k2/1866515-20260818.htm",
"西西里博物馆失窃四幅文艺复兴画作，两幅寻回",
"Four Renaissance paintings stolen from Sicily museum; two recovered nearby",
"05:10 2026年8月18日",
"西西里一博物馆在节日期间被盗四幅文艺复兴画作，其中两幅两小时后在附近被寻回。",
"Thieves stole four Renaissance paintings from a Sicily museum during a festival; two works were recovered nearby within two hours.",
"香港电台 RTHK","#0f766e")

HTML += """<tr><td style="padding:18px 24px 22px;background:#f8fafc;color:#64748b;font-size:11px;line-height:1.7;">
本简报仅供信息参考，内容编译自公开报道，不构成投资、法律或政策建议。发布时间已换算为北京时间（Asia/Shanghai）。<br>
This briefing is for information only, compiled from public reports, and is not investment, legal or policy advice. Times are shown in Asia/Shanghai.
</td></tr>
</table>
</td></tr></table>
</body></html>
"""

def main():
    forbidden = ["测试", "TEST", "Draft", "预览", "Part", "续", "省略"]
    for w in forbidden:
        if w in HTML or w in SUBJECT:
            raise SystemExit(f"forbidden word: {w}")
    if HTML.count("查看全文") != 28:
        raise SystemExit("item count mismatch")
    payload = {"subject": SUBJECT, "htmlContent": HTML, "recipients": RECIPIENTS}
    path = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("wrote", os.path.abspath(path), "chars", len(HTML))

if __name__ == "__main__":
    main()
