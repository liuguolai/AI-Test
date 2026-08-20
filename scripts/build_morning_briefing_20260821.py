#!/usr/bin/env python3
"""Build 2026-08-21 morning briefing HTML payload. Do not send mail."""
import json
import os
import html as htmlmod

DATE = "2026-08-21"
DATE_CN = "2026年8月21日"
SUBJECT = f"每日热点早报 Morning Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

# Sources counted: Xinhua5 AFP6 Reuters2 BBC1 SCMP1 Caixin1 Anadolu1 CNBC1 RTHK6
ITEMS = [
    {
        "cat": "国内 China Mainland",
        "zh_title": "吉尔吉斯斯坦、越南纳入中国240小时过境免签",
        "en_title": "China extends 240-hour visa-free transit to Kyrgyzstan and Vietnam",
        "published": "10:02 2026年8月20日",
        "zh_sum": "国家移民管理局宣布，两国公民即日起可适用240小时过境免签及海南30天入境免签，过境免签适用国增至57个。",
        "en_sum": "China’s immigration authority said Kyrgyz and Vietnamese citizens can use 240-hour visa-free transit and Hainan’s 30-day entry waiver from Aug. 20, taking transit coverage to 57 countries.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/20260820/5dc69b0a18a942f1aedc927f700b4deb/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "国内 China Mainland",
        "zh_title": "商务部反对美方对无人机征收232关税",
        "en_title": "Beijing urges Washington to scrap Section 232 drone tariffs",
        "published": "15:08 2026年8月20日",
        "zh_sum": "商务部发言人何亚东说，美方以国家安全为名对无人机及零部件加征232关税，中方坚决反对并敦促立即撤销。",
        "en_sum": "Commerce Ministry spokesman He Yadong said U.S. Section 232 tariffs on drones and parts, imposed in the name of national security, should be withdrawn at once.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/world/20260820/d9647b5f0d804126b3241561e11d61ba/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "国内 China Mainland",
        "zh_title": "李在明会见王毅，双方谈及提升中韩战略合作",
        "en_title": "Lee Jae-myung meets Wang Yi on China-South Korea ties",
        "published": "15:45 2026年8月20日",
        "zh_sum": "韩国总统李在明在首尔青瓦台会见王毅。王毅希望韩方坚定对华友好，以建交35周年为契机推动战略合作。",
        "en_sum": "South Korean President Lee Jae-myung received Foreign Minister Wang Yi in Seoul. Wang urged a friendly China policy and deeper partnership ahead of next year’s 35th diplomatic anniversary.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/leaders/20260820/e018d88bdaac42ad8f0f69a576a833dd/c.html",
        "color": "#c41e3a",
    },
    {
        "cat": "国内 China Mainland",
        "zh_title": "中央气象台维持暴雨蓝色预警，海南岛或现特大暴雨",
        "en_title": "China keeps blue rainstorm alert as heavy rain hits the south",
        "published": "22:41 2026年8月20日",
        "zh_sum": "中央气象台称南海低压已在海南文昌登陆，预计至周六华南多地有大到暴雨，海南岛局地雨量或达300至400毫米。",
        "en_sum": "China kept a blue rainstorm alert after a low made landfall at Wenchang, warning of heavy southern rain through Saturday, with 300–400 mm possible on Hainan.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866922-20260820.htm",
        "color": "#c41e3a",
    },
    {
        "cat": "科技 / 互联网 Technology",
        "zh_title": "神舟二十一号三名航天员获颁航天功勋奖章",
        "en_title": "China awards medals to Shenzhou-21 astronauts",
        "published": "17:00 2026年8月20日",
        "zh_sum": "中共中央、国务院、中央军委决定，向指令长张陆颁发二级航天功勋奖章，授予武飞、张洪章英雄航天员称号并颁发三级奖章。",
        "en_sum": "Beijing awarded commander Zhang Lu a second-class space merit medal and named Wu Fei and Zhang Hongzhang hero astronauts with third-class medals for the Shenzhou-21 mission.",
        "src_zh": "新华社",
        "src_en": "Xinhua",
        "url": "https://www.news.cn/politics/20260820/0332152d41e140d682eb13517fce3ee9/c.html",
        "color": "#0f766e",
    },
    {
        "cat": "科技 / 互联网 Technology",
        "zh_title": "阿里巴巴上季收入增9%，净利润跌76%",
        "en_title": "Alibaba revenue rises on AI demand as profit slumps",
        "published": "21:44 2026年8月20日",
        "zh_sum": "阿里上季收入近2690亿元、升9%，AI云与算力收入升45%；净利润跌76%至105亿元，资本开支增75%。",
        "en_sum": "Alibaba’s June-quarter revenue rose 9% to about 269 billion yuan on AI cloud demand, while net profit fell 76% and capital spending jumped 75%.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866913-20260820.htm",
        "color": "#0f766e",
    },
    {
        "cat": "科技 / 互联网 Technology",
        "zh_title": "香港运输署将以AI把车辆牌照更新缩短至一日",
        "en_title": "Hong Kong AI system to renew vehicle licences in one day",
        "published": "15:48 2026年8月20日",
        "zh_sum": "运输署年底推出AI审批系统，预计九成以上网上车辆牌照更新可自动处理，由最长10个工作日缩短至一日。",
        "en_sum": "Hong Kong’s Transport Department said an AI system launching by year-end should auto-approve more than 90% of online vehicle-licence renewals, cutting waits from 10 working days to one.",
        "src_zh": "南华早报",
        "src_en": "SCMP",
        "url": "https://www.scmp.com/news/hong-kong/transport/article/3364669/hong-kong-drivers-renew-vehicle-licences-1-day-year-end-under-ai-system",
        "color": "#0f766e",
    },
    {
        "cat": "科技 / 互联网 Technology",
        "zh_title": "中国电信上半年盈利跌约15%，智能收入仍增",
        "en_title": "China Telecom first-half profit falls as intelligent revenue grows",
        "published": "20:46 2026年8月20日",
        "zh_sum": "中国电信上半年盈利约196亿元，按年跌约15%；中期派息比率升至75%，智能收入增7.1%，天翼云收入增7.8%。",
        "en_sum": "China Telecom’s first-half net profit fell about 15% to roughly 196 billion yuan, while it raised the payout ratio to 75% and reported 7.1% growth in intelligent-service revenue.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866909-20260820.htm",
        "color": "#0f766e",
    },
    {
        "cat": "财经 / 商业 Finance & Business",
        "zh_title": "美股低收约1%，沃尔玛绩后重挫拖累零售股",
        "en_title": "Wall Street sinks as Walmart slump and yields weigh",
        "published": "07:02 2026年8月21日",
        "zh_sum": "道指跌1.32%报52759点，纳指跌1%，标普跌0.87%。沃尔玛同店销售不及预期，股价挫逾9%，美债孳息回升。",
        "en_sum": "The Dow fell 1.32% to 52,759, the Nasdaq lost 1% and the S&P 500 dropped 0.87% after Walmart sank over 9% on a sales miss as yields rose.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866947-20260821.htm",
        "color": "#b45309",
    },
    {
        "cat": "财经 / 商业 Finance & Business",
        "zh_title": "美债抛售再起，30年期收益率回升至约5.24厘",
        "en_title": "U.S. bond sell-off resumes despite Treasury buyback pledge",
        "published": "06:51 2026年8月21日",
        "zh_sum": "财政部虽承诺至少加倍回购长债，30年期美债收益率仍由周三5.19厘回升至约5.24厘。贝森特称必要时可再加大干预。",
        "en_sum": "The 30-year Treasury yield rose to about 5.24% from Wednesday’s 5.19%, a day after officials said they would at least double buybacks. Bessent said further intervention remains possible.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866941-20260821.htm",
        "color": "#b45309",
    },
    {
        "cat": "财经 / 商业 Finance & Business",
        "zh_title": "中国平安上半年净利润增36.1%，中期息提高",
        "en_title": "Ping An first-half net profit jumps 36.1%",
        "published": "20:58 2026年8月20日",
        "zh_sum": "中国平安上半年归母净利润925.85亿元，升36.1%；营运利润升8.3%至842亿元，拟派中期息每股0.98元，升3.2%。",
        "en_sum": "Ping An’s first-half net profit attributable to shareholders rose 36.1% to 92.6 billion yuan, operating profit grew 8.3%, and the interim dividend was lifted 3.2% to 0.98 yuan a share.",
        "src_zh": "财新",
        "src_en": "Caixin",
        "url": "https://finance.caixin.com/2026-08-20/102476217.html",
        "color": "#b45309",
    },
    {
        "cat": "财经 / 商业 Finance & Business",
        "zh_title": "原油收升逾2%，美伊紧张推高油价",
        "en_title": "Oil settles more than 2% higher on Iran tensions",
        "published": "04:00 2026年8月21日",
        "zh_sum": "纽约期油及布伦特原油均升逾2%，布伦特收报每桶93.78美元。特朗普威胁对伊朗及其支持者采取更大规模经济打击。",
        "en_sum": "Brent rose more than 2% to $93.78 a barrel and U.S. crude also gained, as Trump threatened broader economic action against Iran and countries that support it.",
        "src_zh": "美国消费者新闻与商业频道",
        "src_en": "CNBC",
        "url": "https://www.cnbc.com/2026/08/19/stock-market-today-live-updates.html",
        "color": "#b45309",
    },
    {
        "cat": "社会 Society",
        "zh_title": "补习社导师涉公开学生资料，私隐公署接获投诉",
        "en_title": "Hong Kong privacy watchdog receives complaints over tutor posting student data",
        "published": "20:52 2026年8月20日",
        "zh_sum": "私隐专员公署接获3宗投诉，指有补习社导师在社交平台公开学生课程及就读中学。教育局称将严肃跟进并已联络相关学校。",
        "en_sum": "Hong Kong’s privacy watchdog received three complaints after a tutor allegedly posted students’ courses and schools online. The Education Bureau said it would follow up and had contacted the schools.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866910-20260820.htm",
        "color": "#7c3aed",
    },
    {
        "cat": "社会 Society",
        "zh_title": "北部湾低压增强为热带低气压，天文台密切监察",
        "en_title": "Tropical depression forms over the Beibu Gulf, Hong Kong on watch",
        "published": "21:33 2026年8月20日",
        "zh_sum": "天文台表示北部湾低压已增强为热带低气压，未来两三日将在该处徘徊，其后或靠近广东沿岸；周五本港间中有骤雨及雷暴。",
        "en_sum": "The Hong Kong Observatory said a tropical depression over the Beibu Gulf may later edge toward the Guangdong coast, with showers and thunderstorms expected in the city on Friday.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866916-20260820.htm",
        "color": "#7c3aed",
    },
    {
        "cat": "国际 World",
        "zh_title": "美军乔治华盛顿号航母打击群抵达中东",
        "en_title": "USS George Washington strike group arrives in the Middle East",
        "published": "07:07 2026年8月21日",
        "zh_sum": "美军中央司令部称乔治华盛顿号航母打击群已抵达中东，以接替长期部署的林肯号；该调动使西太平洋暂无美军航母。",
        "en_sum": "U.S. Central Command said the USS George Washington strike group had arrived in the Middle East to relieve the long-deployed Abraham Lincoln, leaving no U.S. carrier in the western Pacific.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866929-20260821.htm",
        "color": "#1d4ed8",
    },
    {
        "cat": "国际 World",
        "zh_title": "秘鲁南部发生7.2级地震，利马等地有震感",
        "en_title": "Magnitude 7.2 quake shakes southern Peru",
        "published": "03:00 2026年8月21日",
        "zh_sum": "秘鲁地球物理研究所称阿亚库乔省当地午后发生7.2级地震，震源深约108公里。当局称暂无重大伤亡，部分房屋受损。",
        "en_sum": "Peru’s geophysical institute reported a magnitude 7.2 earthquake in Ayacucho at 13:00 local time. Officials said there were no major casualties, though some homes were damaged.",
        "src_zh": "英国广播公司",
        "src_en": "BBC",
        "url": "https://www.bbc.com/mundo/articles/c62epjggd7mo",
        "color": "#1d4ed8",
    },
    {
        "cat": "国际 World",
        "zh_title": "埃及、卡塔尔、土耳其谴责以色列袭击加沙",
        "en_title": "Egypt, Qatar and Turkey condemn Israeli strikes in Gaza",
        "published": "20:48 2026年8月20日",
        "zh_sum": "三国以调解方身份发表联合声明，谴责以色列袭击造成平民伤亡，要求全面遵守停火，并呼吁国际社会施加有效压力。",
        "en_sum": "Egypt, Qatar and Turkey, acting as mediators, jointly condemned Israeli attacks that killed civilians in Gaza and urged full ceasefire compliance plus stronger international pressure.",
        "src_zh": "阿纳多卢通讯社",
        "src_en": "Anadolu Agency",
        "url": "https://www.anews.com.tr/world/2026/08/20/turkiye-egypt-qatar-condemn-israeli-attacks-in-gaza-urge-compliance-with-ceasefire",
        "color": "#1d4ed8",
    },
    {
        "cat": "国际 World",
        "zh_title": "首批美国遣返移民抵达利比里亚",
        "en_title": "First U.S. deportees arrive in Liberia under new intake deal",
        "published": "07:09 2026年8月21日",
        "zh_sum": "20名被美国遣返的移民抵达利比里亚，为该国同意一年内接收最多1200名第三国国民后的首批人员。利方称未收取补偿。",
        "en_sum": "Twenty people deported from the United States landed in Liberia, the first of up to 1,200 third-country nationals the West African state has agreed to accept within a year.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866932-20260821.htm",
        "color": "#1d4ed8",
    },
    {
        "cat": "国际 World",
        "zh_title": "贝森特吁中国配合对伊制裁，中国使馆称制裁无助解决问题",
        "en_title": "Bessent seeks China’s help on Iran sanctions; Beijing says pressure will not work",
        "published": "07:23 2026年8月21日",
        "zh_sum": "美国财长贝森特称将对伊朗实施“史上最严厉制裁”并呼吁北京配合。中国驻美使馆回应，制裁与施压无助于解决问题。",
        "en_sum": "Treasury Secretary Scott Bessent said Washington would impose its toughest-ever Iran sanctions and urged Beijing to cooperate. China’s embassy in Washington said sanctions would not resolve the issue.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866948-20260821.htm",
        "color": "#1d4ed8",
    },
    {
        "cat": "国际 World",
        "zh_title": "金与正称美韩缩减军演暴露韩方焦虑",
        "en_title": "Kim Yo-jong says Seoul’s drill-cut response shows anxiety",
        "published": "03:08 2026年8月21日",
        "zh_sum": "朝中社引述金与正称，美国缩减韩美军演是首尔的因果报应，韩方表态暴露焦虑。俄罗斯外交部对美减少参演表示欢迎。",
        "en_sum": "KCNA quoted Kim Yo-jong as saying a U.S. cut to joint drills with South Korea was Seoul’s comeuppance. Russia’s foreign ministry welcomed the reduced American participation.",
        "src_zh": "朝中社",
        "src_en": "KCNA",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866931-20260821.htm",
        "color": "#1d4ed8",
    },
    {
        "cat": "香港本地 Hong Kong",
        "zh_title": "打鼓岭犬只训练中心女子遭狗袭击后死亡",
        "en_title": "Woman dies after dog attack at Ta Kwu Ling training centre",
        "published": "23:17 2026年8月20日",
        "zh_sum": "33岁女子在坪洋村持牌宠物酒店草地昏迷死亡，闭路电视显示其喂食后欲将唐狗入笼时遭袭击。涉事狗只已被渔护署带走。",
        "en_sum": "A 33-year-old licensee of a Ta Kwu Ling dog hotel died after CCTV showed a mongrel attacking her as she tried to cage it. AFCD took the dog away.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866926-20260820.htm",
        "color": "#db2777",
    },
    {
        "cat": "香港本地 Hong Kong",
        "zh_title": "佐敦社区客厅开幕，陈国基称还将再开设",
        "en_title": "Jordan community living room opens as Hong Kong expands the scheme",
        "published": "20:22 2026年8月20日",
        "zh_sum": "政务司司长陈国基出席佐敦社区客厅开幕，称已达今年增设6间的目标，全港累计16间，预计每年服务400个劏房户。",
        "en_sum": "Chief Secretary Eric Chan opened Hong Kong’s 16th community living room in Jordan, saying this year’s six-site target is met and 400 subdivided-flat households may be served yearly.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866907-20260820.htm",
        "color": "#db2777",
    },
    {
        "cat": "香港本地 Hong Kong",
        "zh_title": "海关在落马洲支线检获三只怀疑非法进口活猫",
        "en_title": "Hong Kong Customs seizes three live cats at Lok Ma Chau Spur Line",
        "published": "22:16 2026年8月20日",
        "zh_sum": "海关在落马洲支线管制站截查一名68岁内地女旅客，于行李内检获三只怀疑非法进口活猫，估值约3.6万元，案件交渔护署跟进。",
        "en_sum": "Customs arrested a 68-year-old mainland woman at Lok Ma Chau Spur Line after finding three suspected illegally imported live cats worth about HK$36,000 in her luggage.",
        "src_zh": "香港电台",
        "src_en": "RTHK",
        "url": "https://news.rthk.hk/rthk/ch/component/k2/1866919-20260820.htm",
        "color": "#db2777",
    },
    {
        "cat": "其他 Other",
        "zh_title": "维斯塔潘与红牛延长合约至2030年",
        "en_title": "Verstappen signs Red Bull contract extension through 2030",
        "published": "22:40 2026年8月20日",
        "zh_sum": "四届世界冠军维斯塔潘与红牛延长合约至2030年底，结束其去向传闻。他本赛季成绩下滑，目前车手积分榜排第六。",
        "en_sum": "Four-time Formula One champion Max Verstappen extended his Red Bull deal through 2030, ending speculation about a move after a difficult season that leaves him sixth in the standings.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866921-20260820.htm",
        "color": "#475569",
    },
    {
        "cat": "其他 Other",
        "zh_title": "阿尔卡拉斯宣布将出战美网卫冕",
        "en_title": "Alcaraz says he will return to defend his US Open title",
        "published": "07:44 2026年8月21日",
        "zh_sum": "七届大满贯得主阿尔卡拉斯宣布伤愈后将出战美网卫冕。他因右腕伤缺席法网和温网，已四个月未参赛。",
        "en_sum": "Carlos Alcaraz said he will defend his US Open title after a right-wrist injury kept him out for four months, including the French Open and Wimbledon.",
        "src_zh": "法新社",
        "src_en": "AFP",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866934-20260821.htm",
        "color": "#475569",
    },
    {
        "cat": "其他 Other",
        "zh_title": "巴拿马运河因干旱下调日均通航船舶数量",
        "en_title": "Panama Canal to cut daily transits as El Niño drought bites",
        "published": "07:42 2026年8月21日",
        "zh_sum": "巴拿马运河管理局因流域降雨低于预期，9月3日起每日通航由36艘减至34艘，9月15日起再减至32艘，并已限制最大吃水。",
        "en_sum": "The Panama Canal Authority will cut daily transits from 36 ships to 34 from Sept. 3 and to 32 from Sept. 15, citing weaker-than-forecast rainfall linked to El Niño.",
        "src_zh": "路透社",
        "src_en": "Reuters",
        "url": "https://news.rthk.hk/rthk/en/component/k2/1866949-20260821.htm",
        "color": "#475569",
    },
]


def esc(s):
    return htmlmod.escape(s, quote=True)


def build_html():
    n = len(ITEMS)
    cats = []
    for it in ITEMS:
        if not cats or cats[-1][0] != it["cat"]:
            cats.append((it["cat"], []))
        cats[-1][1].append(it)

    parts = []
    parts.append(
        f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(SUBJECT)}</title>
</head>
<body style="margin:0;padding:0;background:#eef1f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;color:#1f2937;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef1f5;padding:16px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 8px 24px rgba(15,23,42,.08);">
<tr><td style="background:#0f172a;padding:22px 24px 18px;color:#fff;">
<div style="font-size:12px;letter-spacing:.12em;color:#93c5fd;text-transform:uppercase;">Asia/Shanghai</div>
<div style="font-size:22px;font-weight:700;margin:6px 0 4px;">每日热点早报</div>
<div style="font-size:14px;color:#cbd5e1;">Morning News Briefing · {esc(DATE_CN)} · 共 {n} 条</div>
</td></tr>
<tr><td style="padding:18px 24px 8px;font-size:14px;line-height:1.65;color:#334155;">
汇总昨夜至今要闻，覆盖隔夜美欧收盘、突发与开盘前政策消息。<br>
Overnight and early headlines, including Wall Street’s close, breaking stories and pre-open policy news.
</td></tr>
"""
    )
    idx = 1
    for cat, items in cats:
        parts.append(
            f"""<tr><td style="padding:14px 24px 6px;">
<div style="background:#f1f5f9;border-left:4px solid #2563eb;padding:8px 12px;border-radius:0 8px 8px 0;">
<h2 style="margin:0;font-size:16px;color:#0f172a;">{esc(cat)}</h2>
</div>
</td></tr>"""
        )
        for it in items:
            num = f"{idx:02d}"
            parts.append(
                f"""<tr><td style="padding:10px 24px 12px;border-bottom:1px solid #eef2f7;">
<div style="font-size:12px;color:#64748b;font-weight:700;">{num}</div>
<a href="{esc(it['url'])}" style="color:#0f172a;text-decoration:none;font-size:16px;font-weight:700;line-height:1.45;">{esc(it['zh_title'])}</a>
<div style="font-size:13px;color:#475569;font-style:italic;margin:4px 0 2px;">{esc(it['en_title'])}</div>
<div style="font-size:12px;color:#94a3b8;">发布时间 Published: {esc(it['published'])}</div>
<div style="font-size:13px;line-height:1.6;margin:8px 0 0;color:#334155;">{esc(it['zh_sum'])}</div>
<div style="font-size:13px;line-height:1.6;color:#475569;">{esc(it['en_sum'])}</div>
<div style="margin-top:8px;">
<span style="display:inline-block;background:{it['color']};color:#fff;border-radius:999px;padding:2px 8px;font-size:11px;">{esc(it['src_zh'])} {esc(it['src_en'])}</span>
<a href="{esc(it['url'])}" style="margin-left:8px;font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</div>
</td></tr>"""
            )
            idx += 1
    parts.append(
        """<tr><td style="padding:18px 24px 24px;font-size:11px;line-height:1.6;color:#64748b;background:#f8fafc;">
本邮件由公开新闻整理，仅供参考，不构成投资、法律或政策建议。译文力求准确，如与原文有出入，以原发布机构为准。<br>
This briefing summarises publicly reported news for general information only and is not investment, legal or policy advice. Original publishers remain authoritative if translations differ.
</td></tr>
</table>
</td></tr></table>
</body></html>"""
    )
    return "".join(parts)


def main():
    html = build_html()
    forbidden = ["测试", "TEST", "Draft", "预览", "Part", "续", "省略"]
    for w in forbidden:
        if w in html:
            raise SystemExit(f"forbidden token: {w}")
    if len(ITEMS) < 20 or len(ITEMS) > 28:
        raise SystemExit(f"bad count {len(ITEMS)}")
    for it in ITEMS:
        zc = len(it["zh_sum"].replace("，", ","))
        # count Chinese chars excluding punctuation loosely
        zh_chars = sum(1 for c in it["zh_sum"] if "\u4e00" <= c <= "\u9fff")
        en_words = len(it["en_sum"].replace("—", " ").replace("–", " ").split())
        if zh_chars > 55:
            raise SystemExit(f"zh too long ({zh_chars}): {it['zh_title']}")
        if en_words > 30:
            raise SystemExit(f"en too long ({en_words}): {it['en_title']}")
    payload = {"subject": SUBJECT, "htmlContent": html, "recipients": RECIPIENTS}
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("items", len(ITEMS))
    print("html_chars", len(html))
    print("payload", os.path.abspath(out))
    from collections import Counter
    print(Counter(i["cat"].split()[0] for i in ITEMS))
    print(Counter(i["src_en"] for i in ITEMS))


if __name__ == "__main__":
    main()
