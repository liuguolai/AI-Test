#!/usr/bin/env python3
"""Generate evening briefing email_payload.json for 2026-08-13."""
import json
import os

ITEMS = [
    # 国内 China Mainland
    {
        "cat_cn": "国内", "cat_en": "China Mainland",
        "title_cn": "湖北襄阳继续开展白海豚台风灾后救援恢复",
        "title_en": "Rescue and recovery continue in Hubei after Typhoon Dolphin",
        "pub": "08:48 2026年8月13日",
        "sum_cn": "新华社报道，台风白海豚致湖北多地暴雨洪涝，襄阳等地正排查险情、恢复供电与交通。",
        "sum_en": "Xinhua says heavy rains and flooding continue across Hubei as crews work to restore power and transport.",
        "src_cn": "新华社", "src_en": "Xinhua", "url": "http://en.people.cn/n3/2026/0813/c90000-20488228.html",
    },
    {
        "cat_cn": "国内", "cat_en": "China Mainland",
        "title_cn": "北京结束防汛二级响应，13日起公交地铁逐步恢复",
        "title_en": "Beijing lifts Level II flood response; transit resumes Aug 13",
        "pub": "21:19 2026年8月12日",
        "sum_cn": "新华社称，北京12日20时解除暴雨橙色预警并结束全市防汛二级响应，13日起公交、游船及景区有序复运。",
        "sum_en": "Xinhua says Beijing ended its Level II flood alert on Aug 12, with buses, ferries and sites reopening Aug 13.",
        "src_cn": "新华社", "src_en": "Xinhua", "url": "https://www.xinhuanet.com/politics/20260812/c9aff3eb25aa402b9427a0527c68395d/c.html",
    },
    {
        "cat_cn": "国内", "cat_en": "China Mainland",
        "title_cn": "央行二季度报告：谋划出台务实管用增量政策",
        "title_en": "PBOC Q2 report pledges practical incremental policy measures",
        "pub": "07:01 2026年8月13日",
        "sum_cn": "财新援引央行报告，提出加大逆周期调节，保持流动性充裕并强化对内需、科创与中小微金融支持。",
        "sum_en": "Caixin cites the PBOC report calling for stronger counter-cyclical support and ample liquidity for key sectors.",
        "src_cn": "财新", "src_en": "Caixin", "url": "https://finance.caixin.com/2026-08-13/102473576.html",
    },
    {
        "cat_cn": "国内", "cat_en": "China Mainland",
        "title_cn": "浦银安盛基金完成工商更名，正式改称浦银基金",
        "title_en": "SPDB fund completes rename after AXA merger into BNP Paribas AM",
        "pub": "22:23 2026年8月12日",
        "sum_cn": "澎湃新闻报道，法巴资管吸收合并原股东安盛投资后，浦银安盛完成法定名称变更并保留浦发控股地位。",
        "sum_en": "The Paper says SPDB fund was renamed after BNP Paribas AM absorbed AXA IM, with SPDB Bank staying the top shareholder.",
        "src_cn": "澎湃新闻", "src_en": "The Paper", "url": "https://www.thepaper.cn/newsDetail_forward_33769573",
    },
    # 科技 Technology
    {
        "cat_cn": "科技", "cat_en": "Technology",
        "title_cn": "谷歌重组DeepMind领导层，加速追赶Gemini模型",
        "title_en": "Google reshuffles DeepMind leadership to close Gemini gap",
        "pub": "08:17 2026年8月13日",
        "sum_cn": "路透援引《商业时报》称，谷歌8月5日调整DeepMind架构，科拉伊·卡武库奥卢接掌Gemini日常运营以提升模型竞争力。",
        "sum_en": "Reuters via BT says Google shifted DeepMind leadership on Aug 5, putting Koray Kavukcuoglu in charge of Gemini execution.",
        "src_cn": "路透 / 商业时报", "src_en": "Reuters / Business Times", "url": "https://www.businesstimes.com.sg/international/global/race-regain-ai-model-supremacy-why-google-shifted-power-its-top-ranks",
    },
    {
        "cat_cn": "科技", "cat_en": "Technology",
        "title_cn": "Anthropic据报洽谈约60亿美元收购AI算力优化公司Decart",
        "title_en": "Anthropic reportedly in talks to buy Decart for about $6 billion",
        "pub": "13:03 2026年8月13日",
        "sum_cn": "彭博援引消息称，Anthropic正洽谈收购芯片优化软件公司Decart，以在IPO前降低推理成本并扩充算力。",
        "sum_en": "Bloomberg reports Anthropic is in talks to buy chip-optimization startup Decart ahead of a potential IPO.",
        "src_cn": "彭博社", "src_en": "Bloomberg", "url": "https://stocktwits.com/news-articles/markets/equity/anthropic-reportedly-eyes-6-b-decart-deal-as-ai-labs-hunt-for-cheaper-faster-compute/cZopCqCRJh9",
    },
    {
        "cat_cn": "科技", "cat_en": "Technology",
        "title_cn": "腾讯二季度营收增11%，AI投入拖累利润增速",
        "title_en": "Tencent Q2 revenue up 11% but AI spending slows profit growth",
        "pub": "08:17 2026年8月13日",
        "sum_cn": "财新称，腾讯二季度Non-IFRS净利润增9%，若剔除新AI产品影响则增19%，593亿元资本开支致自由现金流转负。",
        "sum_en": "Caixin says Tencent's non-IFRS profit rose 9% in Q2, with AI spending and heavy capex weighing on margins and cash flow.",
        "src_cn": "财新", "src_en": "Caixin", "url": "https://www.caixin.com/2026-08-13/102473589.html",
    },
    {
        "cat_cn": "科技", "cat_en": "Technology",
        "title_cn": "荣耀发布9999元起Robot Phone，主打多模态交互",
        "title_en": "Honor launches Robot Phone from 9,999 yuan with multimodal AI",
        "pub": "08:32 2026年8月13日",
        "sum_cn": "财新报道，荣耀12日发布配备四自由度云台的Robot Phone，CEO李健称将以此推进品牌高端化与AI终端新形态。",
        "sum_en": "Caixin says Honor unveiled a gimbal-equipped Robot Phone on Aug 12 as it pushes premium AI hardware.",
        "src_cn": "财新", "src_en": "Caixin", "url": "https://www.caixin.com/2026-08-13/102473595.html",
    },
    # 财经 Finance & Business
    {
        "cat_cn": "财经", "cat_en": "Finance & Business",
        "title_cn": "标普与纳指收高，CoreWeave业绩与温和CPI提振AI股",
        "title_en": "S&P 500 and Nasdaq rise on CoreWeave results and mild CPI",
        "pub": "06:23 2026年8月13日",
        "sum_cn": "海峡时报援引路透，8月12日标普500涨0.26%至7748.50点，纳指涨0.54%，7月CPI同比3.4%缓和加息预期。",
        "sum_en": "ST/Reuters says the S&P 500 and Nasdaq closed higher on Aug 12 as mild July CPI eased Fed hike bets.",
        "src_cn": "海峡时报 / 路透", "src_en": "The Straits Times / Reuters", "url": "https://www.straitstimes.com/business/companies-markets/sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism",
    },
    {
        "cat_cn": "财经", "cat_en": "Finance & Business",
        "title_cn": "腾讯港股开盘一度跌超5%，市场担忧AI资本开支",
        "title_en": "Tencent shares fall over 5% at open on AI capex concerns",
        "pub": "10:02 2026年8月13日",
        "sum_cn": "财新称，腾讯13日开盘受前夜财报影响一度跌超5%，593亿元季度资本开支令自由现金流2019年来首次为负。",
        "sum_en": "Caixin says Tencent opened down more than 5% on Aug 13 after heavy AI capex pushed free cash flow negative.",
        "src_cn": "财新", "src_en": "Caixin", "url": "https://companies.caixin.com/2026-08-13/102473621.html",
    },
    {
        "cat_cn": "财经", "cat_en": "Finance & Business",
        "title_cn": "港股低开，亚洲市场随美国通胀数据温和而走强",
        "title_en": "Hong Kong shares slip while Asia rises on softer US inflation",
        "pub": "10:42 2026年8月13日",
        "sum_cn": "RTHK报道，恒生指数13日低开0.6%至25288点，日韩股市随美国7月CPI符合预期而上涨，油价仍处高位。",
        "sum_en": "RTHK says the Hang Seng opened lower on Aug 13 while regional markets rose after in-line US inflation data.",
        "src_cn": "香港电台", "src_en": "RTHK", "url": "https://news.rthk.hk/rthk/en/component/k2/1866002-20260813.htm",
    },
    {
        "cat_cn": "财经", "cat_en": "Finance & Business",
        "title_cn": "渣打合资Anchorpoint启动港元稳定币HKDAP机构试用",
        "title_en": "Standard Chartered venture launches HKDAP stablecoin beta",
        "pub": "19:06 2026年8月12日",
        "sum_cn": "南华早报称，渣打、Animoca与HKT合资的Anchorpoint 12日启动港元挂钩稳定币HKDAP机构阶段发行。",
        "sum_en": "SCMP says Anchorpoint began institutional beta rollout of its Hong Kong dollar-linked stablecoin HKDAP.",
        "src_cn": "南华早报", "src_en": "SCMP", "url": "https://www.scmp.com/business/cryptocurrency/article/3363800/hong-kong-stablecoin-selection-expands-standard-chartered-led-ventures-launch",
    },
    # 社会 Society
    {
        "cat_cn": "社会", "cat_en": "Society",
        "title_cn": "加州代孕者在得州产子，法官下令维持生命救治",
        "title_en": "California surrogate gives birth in Texas after life-saving court order",
        "pub": "08:30 2026年8月13日",
        "sum_cn": "美联社称，代孕者McKenna West 13日在得州产下先天性心脏病胎儿，此前法官裁定须提供维持生命治疗。",
        "sum_en": "AP says a California surrogate gave birth in Texas on Aug 13 after a judge ordered life-sustaining care for the newborn.",
        "src_cn": "美联社", "src_en": "AP", "url": "https://apnews.com/article/surrogate-california-texas-heart-defect-birth-surgery-b19db01b62d0d06d28afc173fbc0570d",
    },
    {
        "cat_cn": "社会", "cat_en": "Society",
        "title_cn": "美国三州同日安排四名死囚注射死刑",
        "title_en": "Three US states schedule lethal injections on the same day",
        "pub": "12:03 2026年8月13日",
        "sum_cn": "美联社报道，田纳西、阿拉巴马与俄克拉荷马14日各有一名死囚待处决，为2010年来美国首次同日三州执行。",
        "sum_en": "AP says Tennessee, Alabama and Oklahoma each plan an execution Thursday, a rare same-day convergence in the US.",
        "src_cn": "美联社", "src_en": "AP", "url": "https://apnews.com/article/execution-death-penalty-tennessee-alabama-oklahoma-062c601ee0ff9a5f6d7b79045a0cc6b5",
    },
    {
        "cat_cn": "社会", "cat_en": "Society",
        "title_cn": "BTS成员V直播透露右耳听力严重受损",
        "title_en": "BTS star V reveals severe hearing loss in livestream",
        "pub": "12:09 2026年8月13日",
        "sum_cn": "BBC称，V在13日直播中首次公开右耳听力仅约正常30%，称服役期间加重并正定期就医治疗。",
        "sum_en": "BBC says V disclosed on Aug 13 that his right ear hears at about 30% of normal and he is under treatment.",
        "src_cn": "BBC", "src_en": "BBC", "url": "https://www.bbc.com/news/articles/cx2v1893n3eo",
    },
    {
        "cat_cn": "社会", "cat_en": "Society",
        "title_cn": "“人民艺术家”郭兰英在广州逝世，享年97岁",
        "title_en": "Opera artist Guo Lanying dies in Guangzhou at 97",
        "pub": "02:17 2026年8月12日",
        "sum_cn": "澎湃新闻转中国歌剧舞剧院讣告，著名歌剧表演艺术家郭兰英8月11日17时14分在广州因病逝世。",
        "sum_en": "The Paper cites a China Opera and Dance Drama Theater notice that famed soprano Guo Lanying died in Guangzhou on Aug 11.",
        "src_cn": "澎湃新闻", "src_en": "The Paper", "url": "https://www.thepaper.cn/newsDetail_forward_33763546",
    },
    # 国际 World
    {
        "cat_cn": "国际", "cat_en": "World",
        "title_cn": "伊朗称重启与美临时协议谈判毫无进展",
        "title_en": "Iran says no progress on reviving interim US peace deal",
        "pub": "07:38 2026年8月13日",
        "sum_cn": "路透援引伊朗消息人士称，双方就恢复6月临时协议及霍尔木兹通航仍无进展，特朗普同日称美方控制该海峡。",
        "sum_en": "Reuters reports an Iranian source says talks to revive the June interim deal have made no progress.",
        "src_cn": "路透 / Arab News", "src_en": "Reuters / Arab News", "url": "https://www.arabnews.com/node/2654473/middle-east",
    },
    {
        "cat_cn": "国际", "cat_en": "World",
        "title_cn": "哥伦比亚地震救援进入第三天，遇难人数超250",
        "title_en": "Colombia quake rescue enters third day with 250+ dead",
        "pub": "04:05 2026年8月13日",
        "sum_cn": "ABC报道，西部哥伦比亚地震48小时后救援人员仍在废墟中搜寻，逾250人遇难，美国承诺1550万美元援助。",
        "sum_en": "ABC says rescuers searched rubble on Aug 13 as Colombia's quake death toll passed 250, with US aid pledged.",
        "src_cn": "ABC", "src_en": "ABC", "url": "https://www.abc.net.au/news/2026-08-13/colombia-earthquake-rescuers-search-rubble-for-third-day/107030986",
    },
    {
        "cat_cn": "国际", "cat_en": "World",
        "title_cn": "普京视察日俄争议择捉岛，东京提出正式抗议",
        "title_en": "Putin visits disputed Kuril island, drawing Tokyo protest",
        "pub": "16:23 2026年8月13日",
        "sum_cn": "RTHK援引消息称，普京13日视察俄称伊图鲁普、日称择捉的争议岛屿，日本首相高市早苗称此举不可接受。",
        "sum_en": "RTHK says Putin visited disputed Iturup island on Aug 13, prompting a formal protest from Japan.",
        "src_cn": "香港电台 / 路透", "src_en": "RTHK / Reuters", "url": "https://news.rthk.hk/rthk/en/component/k2/1866043-20260813.htm",
    },
    {
        "cat_cn": "国际", "cat_en": "World",
        "title_cn": "鲁比奥与贝森特据报乘诱饵专机离土，特朗普秘密换机",
        "title_en": "Rubio and Bessent flew decoy plane as Trump switched jets from Turkey",
        "pub": "09:44 2026年8月13日",
        "sum_cn": "美联社援引官员称，特朗普因伊朗威胁在土秘密换机返美，国务卿与财长则留在诱饵专机上离境。",
        "sum_en": "AP says Rubio and Bessent flew a decoy plane from Turkey while Trump was moved to another jet over an Iranian threat.",
        "src_cn": "美联社", "src_en": "AP", "url": "https://apnews.com/article/trump-air-force-one-iran-rubio-bessent-c66cfef8a02e92620c4545097149cac0",
    },
    # 香港本地 Hong Kong
    {
        "cat_cn": "香港本地", "cat_en": "Hong Kong",
        "title_cn": "酷暑持续，香港劳工团体呼吁分区发布热应激指数",
        "title_en": "Extreme heat in HK prompts calls for district-level heat index",
        "pub": "16:30 2026年8月13日",
        "sum_cn": "南华早报称，13日新界北部气温超35°C，户外工友称买水降温每日花费过百元，团体要求分区监测热应激。",
        "sum_en": "SCMP says labour groups want district heat readings as outdoor workers struggle with sustained extreme temperatures.",
        "src_cn": "南华早报", "src_en": "SCMP", "url": "https://www.scmp.com/news/hong-kong/health-environment/article/3363901/how-hong-kong-can-protect-manual-workers-bearing-brunt-heatwave",
    },
    {
        "cat_cn": "香港本地", "cat_en": "Hong Kong",
        "title_cn": "富邦银行（香港）深圳前海首设内地分行",
        "title_en": "Fubon Bank Hong Kong opens first mainland branch in Shenzhen",
        "pub": "08:30 2026年8月13日",
        "sum_cn": "南华早报报道，富邦银行（香港）在前海开设首家内地分行，聚焦科技企业跨境融资与大湾区业务。",
        "sum_en": "SCMP says Fubon Bank Hong Kong opened its first mainland branch in Qianhai to serve cross-border tech clients.",
        "src_cn": "南华早报", "src_en": "SCMP", "url": "https://www.scmp.com/business/banking-finance/article/3363788/fubon-banks-hong-kong-subsidiary-opens-first-mainland-china-branch-shenzhen",
    },
    {
        "cat_cn": "香港本地", "cat_en": "Hong Kong",
        "title_cn": "海关关长视察皇岗口岸新设施，为开通作准备",
        "title_en": "Customs chief inspects new Huanggang port ahead of opening",
        "pub": "11:10 2026年8月13日",
        "sum_cn": "RTHK称，海关关长陈子达12日视察皇岗新口岸一站式车道设施，运输署称交通测试整体运行顺畅。",
        "sum_en": "RTHK says the customs commissioner inspected Huanggang's new one-stop vehicle lanes ahead of Thursday drills.",
        "src_cn": "香港电台", "src_en": "RTHK", "url": "https://news.rthk.hk/rthk/en/component/k2/1866006-20260813.htm",
    },
    {
        "cat_cn": "香港本地", "cat_en": "Hong Kong",
        "title_cn": "港府拟9月发布首份五年规划，李家超听取公众意见",
        "title_en": "Hong Kong aims to publish first five-year plan in September",
        "pub": "00:00 2026年8月9日",
        "time_note": "时间未知，已按日期占位",
        "sum_cn": "香港政府新闻网称，李家超在区议会论坛表示，当局拟9月公布香港首份五年规划，并整合公众对施政报告意见。",
        "sum_en": "news.gov.hk says CE John Lee aims to publish Hong Kong's first five-year plan in September after public forums.",
        "src_cn": "香港政府新闻网", "src_en": "news.gov.hk", "url": "https://www.news.gov.hk/eng/2026/08/20260809/20260809_122357_363.html",
    },
    # 其他 Other
    {
        "cat_cn": "其他", "cat_en": "Other",
        "title_cn": "梅西父亲丧礼后替补出战迈阿密国际",
        "title_en": "Messi makes substitute appearance for Inter Miami after father's death",
        "pub": "15:19 2026年8月13日",
        "sum_cn": "BBC称，梅西13日替补出场迈阿密国际对莱昂之战，此前称父亲去世后不确定还能踢多久。",
        "sum_en": "BBC says Messi came on as a substitute for Inter Miami on Aug 13 after his father's funeral in Argentina.",
        "src_cn": "BBC", "src_en": "BBC", "url": "https://www.bbc.com/sport/football/articles/cz9722y1ee7o",
    },
    {
        "cat_cn": "其他", "cat_en": "Other",
        "title_cn": "仁川机场上半年国际客流超希思罗居全球第一",
        "title_en": "Incheon overtakes Heathrow as world's busiest international airport",
        "pub": "13:49 2026年8月13日",
        "sum_cn": "BBC报道，仁川机场上半年国际旅客3840万人次，首次超越伦敦希思罗，部分因中东冲突航线改道。",
        "sum_en": "BBC says Incheon served 38.4 million international passengers in H1, overtaking Heathrow for the first time.",
        "src_cn": "BBC", "src_en": "BBC", "url": "https://www.bbc.com/news/articles/cr49p1279n0o",
    },
    {
        "cat_cn": "其他", "cat_en": "Other",
        "title_cn": "芝加哥陪审团裁定波音737 MAX遇难者家属获2900万美元",
        "title_en": "Chicago jury awards $29 million to Boeing 737 MAX victim's family",
        "pub": "07:34 2026年8月13日",
        "sum_cn": "RTHK援引法新社称，陪审团就2019年埃塞俄比亚航空坠机案中联合国雇员Ryan家属作出民事赔偿裁决。",
        "sum_en": "RTHK/AFP says a Chicago jury awarded $29 million to the family of a UN worker killed in the 2019 Ethiopian MAX crash.",
        "src_cn": "香港电台 / 法新社", "src_en": "RTHK / AFP", "url": "https://news.rthk.hk/rthk/en/component/k2/1865983-20260813.htm",
    },
    {
        "cat_cn": "其他", "cat_en": "Other",
        "title_cn": "巴西监管要求Discord暂停直播功能",
        "title_en": "Brazil orders Discord to suspend livestreaming after teen suicide",
        "pub": "01:10 2026年8月13日",
        "sum_cn": "BBC称，巴西数据保护机构在13岁女孩直播自杀事件后，要求Discord暂停直播并加强未成年人保护。",
        "sum_en": "BBC says Brazil's ANPD ordered Discord to suspend livestreams after a 13-year-old girl's death on the platform.",
        "src_cn": "BBC", "src_en": "BBC", "url": "https://www.bbc.com/news/articles/cgewpqxyrddo",
    },
]

CAT_ORDER = [
    ("国内", "China Mainland"),
    ("科技", "Technology"),
    ("财经", "Finance & Business"),
    ("社会", "Society"),
    ("国际", "World"),
    ("香港本地", "Hong Kong"),
    ("其他", "Other"),
]

SRC_COLORS = {
    "新华社": "#c0392b", "Xinhua": "#c0392b",
    "财新": "#8e44ad", "Caixin": "#8e44ad",
    "澎湃新闻": "#2980b9", "The Paper": "#2980b9",
    "路透": "#27ae60", "Reuters": "#27ae60",
    "彭博社": "#2c3e50", "Bloomberg": "#2c3e50",
    "商业时报": "#16a085",
    "海峡时报": "#d35400",
    "南华早报": "#e67e22", "SCMP": "#e67e22",
    "香港电台": "#1abc9c", "RTHK": "#1abc9c",
    "美联社": "#3498db", "AP": "#3498db",
    "BBC": "#c0392b",
    "ABC": "#9b59b6",
    "Arab News": "#27ae60",
    "香港政府新闻网": "#34495e", "news.gov.hk": "#34495e",
    "法新社": "#7f8c8d", "AFP": "#7f8c8d",
}


def item_html(n, it):
    src = it["src_cn"].split(" / ")[0]
    color = SRC_COLORS.get(src, "#555")
    pub_line = f'发布时间 Published: {it["pub"]}'
    return f'''
<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
<div style="color:#888;font-size:11px;font-weight:bold;margin-bottom:4px;">{n:02d}</div>
<div style="font-size:16px;font-weight:bold;margin-bottom:4px;"><a href="{it['url']}" style="color:#1a5276;text-decoration:none;">{it['title_cn']}</a></div>
<div style="font-size:14px;color:#555;font-style:italic;margin-bottom:4px;">{it['title_en']}</div>
<div style="font-size:12px;color:#999;margin-bottom:8px;">{pub_line}</div>
<div style="font-size:14px;color:#333;line-height:1.6;margin-bottom:4px;">{it['sum_cn']}</div>
<div style="font-size:13px;color:#666;line-height:1.5;margin-bottom:8px;">{it['sum_en']}</div>
<div><span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:6px;">{it['src_cn']}</span><span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;margin-right:8px;">{it['src_en']}</span><a href="{it['url']}" style="color:#2471a3;font-size:12px;text-decoration:none;">查看全文 Read more →</a></div>
</div>'''


def build_html():
    n = 0
    body = ""
    for cat_cn, cat_en in CAT_ORDER:
        body += f'<h2 style="background:#f0f3f5;padding:10px 14px;margin:28px 0 16px;border-left:4px solid #2471a3;font-size:17px;color:#2c3e50;">{cat_cn} · {cat_en}</h2>\n'
        for it in ITEMS:
            if it["cat_cn"] == cat_cn:
                n += 1
                body += item_html(n, it)
    total = n
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 Evening Briefing - 2026-08-13</title></head>
<body style="margin:0;padding:0;background:#eef0f2;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;padding:16px 12px;">
<div style="background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.08);overflow:hidden;">
<div style="background:linear-gradient(135deg,#1a252f,#2c3e50);color:#fff;padding:24px 20px;text-align:center;">
<div style="font-size:22px;font-weight:bold;margin-bottom:6px;">每日热点晚报</div>
<div style="font-size:14px;opacity:.9;margin-bottom:4px;">Evening News Briefing · 2026-08-13</div>
<div style="font-size:13px;opacity:.75;">共 {total} 条 · {total} stories</div>
</div>
<div style="padding:20px 18px;background:#fafbfc;border-bottom:1px solid #eee;">
<div style="font-size:14px;color:#333;margin-bottom:6px;">汇总今日全日要闻，涵盖国内外时政、财经、科技与社会热点。</div>
<div style="font-size:13px;color:#666;font-style:italic;">Today's main stories across politics, business, technology and society.</div>
</div>
<div style="padding:8px 18px 24px;">
{body}
<div style="margin-top:28px;padding-top:16px;border-top:1px solid #ddd;font-size:11px;color:#999;line-height:1.6;">
<div>本简报由公开新闻来源自动整理，仅供参考，不构成任何投资或决策建议。</div>
<div style="margin-top:4px;">Compiled from public sources for reference only. Not investment or legal advice.</div>
</div>
</div>
</div>
</div>
</body>
</html>'''
    return html, total


def main():
    html, total = build_html()
    assert total == 28, f"Expected 28 items, got {total}"
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-13",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out} ({len(html)} chars, {total} items)")


if __name__ == "__main__":
    main()
