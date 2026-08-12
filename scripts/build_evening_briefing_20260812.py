#!/usr/bin/env python3
"""Generate evening briefing HTML and email_payload.json for 2026-08-12."""
import json
import os

DATE = "2026-08-12"
SUBJECT = f"每日热点晚报 Evening Briefing - {DATE}"
RECIPIENTS = ["maymay_xia@163.com", "459729983@qq.com"]

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "title_zh": "北京启动江泽民百年诞辰纪念，央视连播12集纪录片",
            "title_en": "China begins Jiang Zemin centenary commemorations with 12-part CCTV documentary",
            "time": "11:53 2026年8月12日",
            "summary_zh": "央视每晚黄金时段播出两集纪录片，预计周一人民大会堂将举行高规格纪念大会，习近平或发表讲话。",
            "summary_en": "CCTV is airing two nightly episodes ahead of a grand ceremony expected Monday at the Great Hall of the People, where Xi Jinping may speak.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/china/politics/article/3363723/china-prepares-mark-jiang-zemin-centenary-full-commemorative-honours",
        },
        {
            "title_zh": "中国最高法强调反外国制裁法首案，称具示范意义",
            "title_en": "China's top court highlights first Anti-Foreign Sanctions Law ruling",
            "time": "16:52 2026年8月12日",
            "summary_zh": "上海海事法院判新加坡船公司赔偿逾499万元，认定外国歧视性限制不能作为履约抗辩理由。",
            "summary_en": "A Shanghai maritime court ordered a Singapore shipper to pay over 4.99 million yuan, rejecting foreign sanctions as a defence under the 2021 law.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/economy/china-economy/article/3363773/chinas-top-court-highlights-first-anti-foreign-sanctions-law-ruling-amid-global-tensions",
        },
        {
            "title_zh": "多地加紧夯实社保缴费基数，专家呼吁同步减负",
            "title_en": "China tightens social security base enforcement as experts urge parallel relief",
            "time": "07:07 2026年8月12日",
            "summary_zh": "财新调查十余省市，年内夯实率要求从65%至100%不等，劳动密集型企业承压引关注。",
            "summary_en": "Caixin found provinces targeting 65% to 100% full-payment rates this year, raising concerns for labor-intensive employers.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-12/102473270.html",
        },
        {
            "title_zh": "台风“白海豚”余波致豫鲁等地暴雨，多地防汛应对",
            "title_en": "Typhoon Kujira remnants bring heavy rain to Henan and Shandong as regions respond",
            "time": "00:49 2026年8月12日",
            "summary_zh": "中央气象台已解除台风蓝色预警，但残余环流与冷空气仍致十余省份出现暴雨或大暴雨。",
            "summary_en": "China lifted its typhoon alert but residual circulation and cold air still threaten torrential rain across more than ten provinces.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua News Agency",
            "url": "https://www.news.cn/politics/20260812/6f41edfafa67494ba13a35f02a2f9c/c.html",
        },
    ]),
    ("科技 Technology", [
        {
            "title_zh": "Manus将恢复独立运营，原股东以20亿美元从Meta购回股份",
            "title_en": "Manus to resume independent operations as investors buy back stake from Meta",
            "time": "07:05 2026年8月12日",
            "summary_zh": "财新称腾讯、真格、红杉等以20亿美元回购股份；部分用户8月23日起数据将按监管要求删除。",
            "summary_en": "Caixin said Tencent, ZhenFund and Sequoia China bought back shares for $2 billion; some user data will be deleted from Aug 23 under regulatory rules.",
            "source_zh": "财新 Caixin",
            "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-12/102473266.html",
        },
        {
            "title_zh": "OpenAI、Meta接连曝AI测试“越界”，英国AISI报告社交工程攻击",
            "title_en": "OpenAI, Meta and UK AISI report AI agents exceeding test boundaries",
            "time": "00:00 2026年8月6日",
            "summary_zh": "多家机构披露模型在评估中突破沙箱或伪造身份施压GitHub维护者，引发对前沿AI测试安全的担忧。",
            "summary_en": "Firms disclosed models escaping sandboxes or using fake profiles to pressure GitHub maintainers, sharpening debate on frontier AI testing safety.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cp30989ee1wo",
        },
        {
            "title_zh": "长征七号改火箭发射失败，中国Sat-4B卫星任务失利",
            "title_en": "China's Long March 7A rocket fails, destroying ChinaSat-4B payload",
            "time": "20:02 2026年8月10日",
            "summary_zh": "火箭自海南文昌起飞约85秒后爆炸，新华社称飞行出现异常，原因调查中，为近年该型号首次失败。",
            "summary_en": "The rocket exploded about 85 seconds after liftoff from Hainan; Xinhua cited a flight anomaly and said investigators are probing the cause.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.nbcnews.com/world/asia/china-says-long-march-7a-rocket-launch-failed-flight-anomaly-rcna591871",
        },
        {
            "title_zh": "英国车手格林氢动力车创406英里时速新纪录",
            "title_en": "Andy Green sets 406 mph record in hydrogen-powered car",
            "time": "12:11 2026年8月12日",
            "summary_zh": "曾在1997年陆上突破音障的英国飞行员在犹他盐滩驾驶氢内燃机车，刷新氢燃料陆地速度纪录。",
            "summary_en": "The former sound-barrier pilot reached 406 mph on Utah's salt flats in a twin hydrogen-engine car, doubling the prior official hydrogen record.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/czjl2yzx8epo",
        },
    ]),
    ("财经 Finance & Business", [
        {
            "title_zh": "油价连涨六日，霍尔木兹协议前景再受质疑",
            "title_en": "Oil rises for sixth day as Hormuz deal prospects face fresh doubt",
            "time": "00:00 2026年8月12日",
            "summary_zh": "布伦特约90美元，特朗普称“完全控制”霍尔木兹且不信任伊朗，市场对供应恢复仍持怀疑态度。",
            "summary_en": "Brent traded near $90 as Trump said the US 'totally controls' Hormuz and distrusts Iran, keeping markets skeptical about restored flows.",
            "source_zh": "彭博 Bloomberg",
            "source_en": "Bloomberg",
            "url": "https://www.energyconnects.com/news/oil/2026/august/oil-extends-gain-on-doubts-over-hormuz-deal-despite-upbeat-tone/",
        },
        {
            "title_zh": "美股小幅回落，油价波动拖累市场关注通胀数据",
            "title_en": "US stocks edge lower as oil swings keep focus on inflation data",
            "time": "05:05 2026年8月12日",
            "summary_zh": "标普500跌0.3%，布伦特结算价涨1.4%至88.91美元；投资者等待周三美国7月CPI公布。",
            "summary_en": "The S&P 500 fell 0.3% while Brent settled up 1.4% at $88.91; investors await Wednesday's US July CPI report.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://www.newser.com/article/3f3f2f2d49e4aa8744d21ecd0ce55a9c/us-stocks-edge-further-from-their-records-as-oil-prices-keep-swinging.html",
        },
        {
            "title_zh": "年内银行“二永债”发行规模已超1.3万亿元",
            "title_en": "Chinese banks' perpetual and tier-2 bond issuance tops 1.3 trillion yuan",
            "time": "00:00 2026年8月12日",
            "summary_zh": "国有大行占发行总量逾六成，交行、建行等近期密集发债补充资本，审批节奏与到期续发推升发行热度。",
            "summary_en": "State banks account for over 60% of issuance as lenders including BoCom and CCB tap markets to replenish capital amid heavier schedules.",
            "source_zh": "经济参考报 via 中国金融信息网",
            "source_en": "Economic Information Daily via CNFin",
            "url": "https://www.cnfin.com/zs-lb/detail/20260812/4454096_1.html",
        },
        {
            "title_zh": "新发基金数量创近五年新高，单只平均规模却缩水",
            "title_en": "New fund launches hit five-year high while average size shrinks",
            "time": "00:00 2026年8月12日",
            "summary_zh": "今年前7月新成立基金1032只，同比增27.9%，但单只平均募集份额约6.92亿份，为近五年同期最低。",
            "summary_en": "1,032 new funds launched in the first seven months, up 27.9%, but average issuance fell to about 692 million units, a five-year low.",
            "source_zh": "中国证券报 via 中国金融信息网",
            "source_en": "China Securities Journal via CNFin",
            "url": "https://www.cnfin.com/gs-lb/detail/20260812/4454109_1.html",
        },
    ]),
    ("社会 Society", [
        {
            "title_zh": "哥伦比亚7.4级地震遇难人数升至逾250人，搜救持续",
            "title_en": "Colombia earthquake death toll tops 250 as rescuers race for survivors",
            "time": "07:32 2026年8月12日",
            "summary_zh": "佩雷拉、卡利灾情最重，逾1100栋房屋损毁，总统宣布国家紧急状态并承诺经济援助。",
            "summary_en": "Pereira and Cali were hardest hit with over 1,100 homes destroyed; the president declared a national emergency and pledged economic support.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.gmanetwork.com/news/topstories/world/998211/colombia-earthquake-death-toll-tops-200-as-rescuers-race-to-find-survivors/story/",
        },
        {
            "title_zh": "印尼林火逾10万公顷，烟雾波及马来西亚沙捞越",
            "title_en": "Indonesia wildfires burn 107,000 hectares as haze spreads to Malaysia",
            "time": "14:30 2026年8月12日",
            "summary_zh": "六个省份为重点扑救区，当局出动云播飞机；沙捞越Serian空气质量指数升至195，属不健康水平。",
            "summary_en": "Six provinces are priority zones with cloud-seeding deployed; Serian in Sarawak logged an unhealthy air index of 195.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvgxzl8xvdxo",
        },
        {
            "title_zh": "新西兰总理卢克森再胜党内信任投票，国防部长被解职",
            "title_en": "New Zealand PM Luxon survives second caucus confidence vote, sacks defence minister",
            "time": "11:30 2026年8月12日",
            "summary_zh": "克里斯·彭克承认发起挑战后被撤职并宣布不参选；卢克森称获全党支持，11月7日将举行大选。",
            "summary_en": "Chris Penk launched the challenge, lost his portfolios and will not seek re-election; Luxon claimed full caucus backing ahead of the Nov 7 poll.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cx2ve2jk5qeo",
        },
        {
            "title_zh": "俄罗斯释放被囚逾四年的前美国海军陆战队员吉尔曼",
            "title_en": "Russia releases former US Marine Robert Gilman after four years in custody",
            "time": "00:00 2026年8月11日",
            "summary_zh": "特朗普称普京出于人道主义放人且无交换；家属称吉尔曼健康状况危急，将赴美军事医院接受治疗。",
            "summary_en": "Trump said Putin freed him on humanitarian grounds with no swap; family said Gilman was gravely ill and headed to a US military hospital.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvgj4m8e1ryo",
        },
    ]),
    ("国际 World", [
        {
            "title_zh": "泽连斯基称已向美方提交结束战争新提案",
            "title_en": "Zelenskyy says Ukraine sent new proposals to US to end war with Russia",
            "time": "04:49 2026年8月12日",
            "summary_zh": "乌方呼吁美国加强防空支援并施压莫斯科；泽连斯基未披露方案细节，称俄或借9月选举动员更多兵力。",
            "summary_en": "Kyiv urged stronger US air-defence help and pressure on Moscow; Zelenskyy gave no details and warned Russia may mobilise after September polls.",
            "source_zh": "半岛电视台 Al Jazeera",
            "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/12/zelenskyy-says-ukraine-has-sent-proposals-to-us-to-end-war-with-russia",
        },
        {
            "title_zh": "朝鲜再射弹道导弹，抗议韩美将举行联合军演",
            "title_en": "North Korea fires ballistic missile ahead of US-South Korea drills",
            "time": "05:00 2026年8月12日",
            "summary_zh": "韩军称导弹自元山一带发射，飞行逾700公里；乌尔奇自由护盾演习将于8月17日启动，为期11天。",
            "summary_en": "Seoul said the missile flew over 700 km from Wonsan; the Ulchi Freedom Shield drills start Aug 17 for 11 days.",
            "source_zh": "美联社 AP",
            "source_en": "Associated Press",
            "url": "https://apnews.com/article/korea-tensions-south-north-japan-ballistic-missle-3622cedfdba8216224f6137dea5f0cb9",
        },
        {
            "title_zh": "胡塞袭击红海货船致6死，美军直升机打击闯封锁货轮",
            "title_en": "Houthi Red Sea attack kills six; US helicopter fires on blockade-busting ship",
            "time": "00:00 2026年8月12日",
            "summary_zh": "也门运输部称四名船员遇难；美军称向巴拿马籍Vela Nova发射两枚地狱火导弹，迫其停航。",
            "summary_en": "Yemen's transport ministry reported four crew deaths; Centcom said a helicopter fired two Hellfire missiles at the Panama-flagged Vela Nova.",
            "source_zh": "CNBC",
            "source_en": "CNBC",
            "url": "https://www.cnbc.com/2026/08/12/us-iran-war-trump-hormuz-houthi-attack-blockade-.html",
        },
        {
            "title_zh": "特朗普证实离北约峰会时秘密换机，称因伊朗威胁",
            "title_en": "Trump confirms secret plane swap after NATO summit over Iran threat",
            "time": "09:50 2026年8月12日",
            "summary_zh": "其先登上空军一号后换乘C-32A离开土耳其，记者与部分幕僚留在原机；美方称侦测到可信导弹威胁情报。",
            "summary_en": "He boarded Air Force One then slipped onto a C-32A in Turkey while press stayed on the decoy jet amid a reported credible missile threat.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/c980r4wpl9lo",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "title_zh": "酷热持续，劳工团体呼吁设立分区暑热指标",
            "title_en": "Extreme heat persists as labour groups urge district-level heat index",
            "time": "13:08 2026年8月12日",
            "summary_zh": "元朗、打鼓岭等地上午已超35℃；业界指机场停机坪等区域温度远高于市区观测站读数。",
            "summary_en": "Yuen Long and Ta Kwu Ling topped 35°C before noon; unions say airport aprons run far hotter than urban station readings.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3363732/extreme-heat-grips-hong-kong-labour-groups-urge-district-level-index",
        },
        {
            "title_zh": "业界呼吁为户外工人增设休息点，配合暑热警告检讨",
            "title_en": "Calls grow for outdoor worker rest areas as heat warning system is reviewed",
            "time": "12:14 2026年8月12日",
            "summary_zh": "清洁、航空地勤等工会称工人难以远离工位避暑，建议参考内地设立劳动者休息点及分区预警。",
            "summary_en": "Unions for cleaners and airport staff say workers cannot easily reach shade and urge rest hubs and zoned alerts like those on the mainland.",
            "source_zh": "香港电台 RTHK",
            "source_en": "RTHK",
            "url": "https://news.rthk.hk/rthk/en/component/k2/1865871-20260812.htm",
        },
        {
            "title_zh": "港交所拟发讨论文件，探讨延长股票交易时间",
            "title_en": "HKEX prepares paper on extending stock market trading hours",
            "time": "11:19 2026年8月12日",
            "summary_zh": "文件将列延长交易利弊供公众讨论，暂不提出具体开收盘时间；现行时段为9:30至16:00含一小时午休。",
            "summary_en": "The paper will outline pros and cons without fixed times; cash trading now runs 9:30am–4pm with a one-hour lunch break.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/business/banking-finance/article/3363719/hkex-pushes-ahead-extended-trading-hours-discussions-it-prepares-paper-sources",
        },
        {
            "title_zh": "元朗狗只收容所女主人被控无牌畜养136只狗",
            "title_en": "Woman charged over 136 unlicensed dogs at Yuen Long shelter",
            "time": "13:55 2026年8月12日",
            "summary_zh": "渔护署接投诉突击检查后提出检控，案件9月2日在屯门裁判法院提堂；违例最高罚款1万港元。",
            "summary_en": "AFCD raided the shelter after complaints; the case will be heard Sept 2 at Tuen Mun Court with fines up to HK$10,000.",
            "source_zh": "南华早报 SCMP",
            "source_en": "South China Morning Post",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363739/hong-kong-authorities-charge-woman-who-allegedly-kept-136-dogs-without-licences",
        },
    ]),
    ("其他 Other", [
        {
            "title_zh": "英国将迎27年来最深日偏食，遮蔽率最高约96%",
            "title_en": "UK faces deepest partial solar eclipse in 27 years with up to 96% coverage",
            "time": "07:17 2026年8月12日",
            "summary_zh": "全食带经过冰岛、西班牙等地；英国峰值约在18:58至19:15 BST，西南部遮蔽率最高。",
            "summary_en": "Totality crosses Iceland and Spain; in the UK peak coverage falls between 18:58–19:15 BST with up to 96% in the southwest.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cx2jr1ew2v1o",
        },
        {
            "title_zh": "新加坡韩国下架Trader Joe's罂粟籽调味料",
            "title_en": "Singapore and South Korea pull Trader Joe's seasoning over poppy seeds",
            "time": "15:30 2026年8月12日",
            "summary_zh": "两国认定罂粟籽可能含吗啡、可待因痕迹属违禁；新加坡已下架逾20条网购链接并呼吁民众丢弃。",
            "summary_en": "Both countries ban poppy seeds over possible opiate traces; Singapore removed 20+ listings and urged owners to dispose of bottles.",
            "source_zh": "BBC",
            "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cdewpklnzwxo",
        },
        {
            "title_zh": "欧洲多地今日可见日全食，西班牙预计吸引数十万游客",
            "title_en": "Total solar eclipse visible across Europe as Spain expects huge crowds",
            "time": "00:00 2026年8月12日",
            "summary_zh": "路透社图解显示全食带经西伯利亚、冰岛至西班牙北部；马德里、巴塞罗那将见接近全食的深偏食。",
            "summary_en": "Reuters maps show totality from Siberia through Iceland to northern Spain; Madrid and Barcelona will see near-total partial eclipses.",
            "source_zh": "路透社 Reuters",
            "source_en": "Reuters",
            "url": "https://www.reuters.com/graphics/SOLAR-ECLIPSE/MAPS/mopazzzxova/",
        },
        {
            "title_zh": "中方在裁谈会驳斥美方涉华弹道导弹发射共同发言",
            "title_en": "China rebukes US-led statement on Chinese ballistic missile test at CD",
            "time": "02:38 2026年8月12日",
            "summary_zh": "李驰江大使强调中方试射提前通报属善意举措，反对个别国家滥用裁谈会平台搞政治操弄。",
            "summary_en": "Ambassador Li Chijiang said advance notice of tests showed goodwill and rejected politicised use of the Conference on Disarmament.",
            "source_zh": "新华社 Xinhua",
            "source_en": "Xinhua News Agency",
            "url": "https://www.news.cn/world/20260812/ac398e4ffcb7467899447c5ad33c5d93/c.html",
        },
    ]),
]


def build_html() -> str:
    total = sum(len(items) for _, items in CATEGORIES)
    n = 0
    body_parts = []
    for cat_name, items in CATEGORIES:
        section = f'<h2 style="margin:24px 0 12px;padding:10px 14px;background:#f0f4f8;border-left:4px solid #2563eb;font-size:16px;color:#1e293b;">{cat_name}</h2>'
        for item in items:
            n += 1
            num = f"{n:02d}"
            section += f'''
<div style="margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #e5e7eb;">
  <div style="font-size:12px;color:#2563eb;font-weight:bold;margin-bottom:4px;">{num}</div>
  <a href="{item["url"]}" style="font-size:16px;font-weight:bold;color:#1d4ed8;text-decoration:none;line-height:1.4;">{item["title_zh"]}</a>
  <div style="font-size:14px;color:#475569;font-style:italic;margin-top:4px;line-height:1.4;">{item["title_en"]}</div>
  <div style="font-size:12px;color:#94a3b8;margin-top:6px;">发布时间 Published: {item["time"]}</div>
  <p style="font-size:14px;color:#334155;margin:10px 0 4px;line-height:1.6;">{item["summary_zh"]}</p>
  <p style="font-size:13px;color:#64748b;margin:0 0 10px;line-height:1.5;">{item["summary_en"]}</p>
  <span style="display:inline-block;background:#e0e7ff;color:#3730a3;font-size:11px;padding:2px 8px;border-radius:4px;margin-right:8px;">{item["source_zh"]}</span>
  <a href="{item["url"]}" style="font-size:12px;color:#2563eb;">查看全文 Read more →</a>
</div>'''
        body_parts.append(section)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;padding:16px;">
<div style="background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">
<div style="background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%);padding:28px 24px;color:#fff;">
  <div style="font-size:22px;font-weight:bold;margin-bottom:4px;">每日热点晚报</div>
  <div style="font-size:14px;opacity:0.9;">Evening News Briefing · {DATE} · 共 {total} 条</div>
</div>
<div style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0;">
  <p style="margin:0 0 8px;font-size:14px;color:#334155;line-height:1.6;">汇总今日全日要闻，涵盖盘中市场、政策动向与社会热点。</p>
  <p style="margin:0;font-size:13px;color:#64748b;line-height:1.5;">Today&apos;s main stories across markets, policy and society.</p>
</div>
<div style="padding:16px 24px 24px;">
{"".join(body_parts)}
</div>
<div style="padding:20px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:11px;color:#94a3b8;line-height:1.6;">
  <p style="margin:0 0 6px;">本简报由自动化系统编发，内容摘自公开报道，仅供信息参考，不构成投资或行动建议。</p>
  <p style="margin:0;">This briefing is automatically compiled from public sources for informational purposes only; it is not investment or action advice.</p>
</div>
</div>
</div>
</body>
</html>'''
    return html


def main():
    html = build_html()
    payload = {
        "subject": SUBJECT,
        "htmlContent": html,
        "recipients": RECIPIENTS,
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    payload_path = os.path.join(root, "email_payload.json")
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Generated {payload_path} ({len(html)} chars, {sum(len(x[1]) for x in CATEGORIES)} items)")


if __name__ == "__main__":
    main()
