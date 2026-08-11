#!/usr/bin/env python3
"""Build evening briefing HTML and email_payload.json for 2026-08-11."""
import json
import os

DATE = "2026-08-11"
BRIEFING_EDITION = "晚报"
TOTAL = 28

CATEGORIES = [
    ("国内 China Mainland", [
        {
            "zh_title": "长征七号改火箭发射失败，中星4B卫星丢失",
            "en_title": "Long March 7A rocket fails, ChinaSat-4B satellite lost",
            "published": "00:09 2026年8月11日",
            "zh_summary": "海南文昌发射的长征七号改火箭升空约90秒后爆炸，中星4B通信卫星随箭体坠入南海，新华社确认任务失败。",
            "en_summary": "A Long March 7A rocket exploded about 90 seconds after liftoff from Hainan, losing the ChinaSat-4B satellite over the South China Sea.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/china/military/article/3363574/chinas-long-march-7a-rocket-explodes-after-launch-satellite-lost",
            "tag": "#c0392b",
        },
        {
            "zh_title": "河南启动防汛四级响应应对台风“白海豚”",
            "en_title": "Henan activates Level IV flood response as Typhoon Bebinca nears",
            "published": "07:53 2026年8月11日",
            "zh_summary": "河南省防指召开台风防范会议，预置5400余名救援人员，8月10日13时启动省级防汛四级应急响应。",
            "en_summary": "Henan held emergency typhoon meetings, pre-positioned over 5,400 rescuers and activated a provincial Level IV flood response.",
            "source_zh": "新华社", "source_en": "Xinhua",
            "url": "http://www.ha.xinhuanet.com/20260811/703d92e6c6b345e7a3cb5e199a9b4c91/c.html",
            "tag": "#e67e22",
        },
        {
            "zh_title": "7月高频数据显示新质生产力动能增强",
            "en_title": "July high-frequency data show new growth drivers strengthening",
            "published": "00:00 2026年8月10日",
            "zh_summary": "国家发改委国家信息中心称，7月先进制造投资同比增73.1%，AI相关专利授权量同比增60%。",
            "en_summary": "NDRC data show July advanced manufacturing investment up 73.1% and AI patent grants up 60% year on year.",
            "source_zh": "新华社《经济参考报》", "source_en": "Xinhua / Economic Information",
            "url": "http://jjckb.xinhuanet.com/20260810/d04e79fc79da464f9b195f0bf9b8c473/c.html",
            "tag": "#e67e22",
        },
        {
            "zh_title": "华恒生物创始人郭恒华因涉嫌非法吸收公众存款被批捕",
            "en_title": "Huahine Biotech founder Guo Henghua arrested over deposit case",
            "published": "08:00 2026年8月11日",
            "zh_summary": "科创板上市公司华恒生物公告称，实控人郭恒华因涉嫌非法吸收公众存款被检察机关批准逮捕并辞去职务。",
            "en_summary": "Huahine Biotech said founder Guo Henghua was arrested on alleged illegal deposit-taking charges and resigned all posts.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-11/102473013.html",
            "tag": "#8e44ad",
        },
    ]),
    ("科技 / 互联网 Technology", [
        {
            "zh_title": "OpenAI、Anthropic与Meta接连披露AI越界行为",
            "en_title": "OpenAI, Anthropic and Meta report AI models going out of bounds",
            "published": "00:00 2026年8月6日",
            "zh_summary": "多家AI公司披露模型在测试中突破沙箱或误配网络权限，英国AI安全研究所亦发现潜在欺骗性行为。",
            "en_summary": "Several AI firms disclosed models breaching test sandboxes or gaining web access, raising scrutiny of agent safety.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cp30989ee1wo",
            "tag": "#2980b9",
        },
        {
            "zh_title": "宇树科技科创板IPO网上中签率仅0.018%",
            "en_title": "Unitree Robotics IPO draw rate just 0.018% on STAR Market",
            "published": "09:22 2026年8月11日",
            "zh_summary": "人形机器人企业宇树科技发行价150.80元，网上发行最终中签率约0.018%，申购热度极高。",
            "en_summary": "Humanoid robot maker Unitree priced its STAR Market IPO at 150.80 yuan with a 0.018% online allotment rate.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-11/102473044.html",
            "tag": "#8e44ad",
        },
        {
            "zh_title": "特朗普对进口多晶硅产品加征15%关税",
            "en_title": "Trump imposes 15% tariff on imported polysilicon products",
            "published": "08:44 2026年8月7日",
            "zh_summary": "美国签署行政令对多晶硅及相关产品设最低进口价并加征15%关税，12月4日生效以扶持本土半导体供应链。",
            "en_summary": "The US set minimum import prices and a 15% polysilicon tariff, effective December 4, to shield domestic chip supply chains.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cdrvn686dljo",
            "tag": "#2980b9",
        },
        {
            "zh_title": "科技领袖称AI将减工时，员工却常周工作90小时",
            "en_title": "Tech leaders tout shorter weeks while staff report 90-hour sprints",
            "published": "17:30 2026年8月10日",
            "zh_summary": "BBC调查称OpenAI、Anthropic等AI公司员工在冲刺期常周工作超90小时，与高管减工时承诺形成反差。",
            "en_summary": "BBC reporting says AI firm staff often work 90-hour weeks during sprints, contradicting executives' shorter-week claims.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cvgx4yd1gl2o",
            "tag": "#2980b9",
        },
    ]),
    ("财经 / 商业 Finance & Business", [
        {
            "zh_title": "特朗普新索赔令霍尔木兹协议前景黯淡，油价持稳高位",
            "en_title": "Oil holds gains as Trump's new Iran demands cloud Hormuz deal",
            "published": "00:00 2026年8月11日",
            "zh_summary": "特朗普要求伊朗赔偿冲突伤亡后，布伦特原油维持在约88美元，年内涨幅近45%，市场担忧供应持续紧张。",
            "en_summary": "Brent held near $88 after Trump demanded Iranian compensation, with crude up nearly 45% this year on supply fears.",
            "source_zh": "彭博社", "source_en": "Bloomberg",
            "url": "https://www.energyconnects.com/news/oil/2026/august/oil-holds-advance-as-fresh-trump-demands-cloud-hormuz-outlook/",
            "tag": "#27ae60",
        },
        {
            "zh_title": "美国债市下跌，投资者权衡通胀与中东风险",
            "en_title": "US bonds fall as markets weigh inflation and Middle East risks",
            "published": "02:37 2026年8月11日",
            "zh_summary": "10年期美债收益率升至4.694%，投资者关注本周CPI数据及霍尔木兹僵局对油价和通胀的影响。",
            "en_summary": "The 10-year Treasury yield rose to 4.694% as investors eyed CPI data and Hormuz risks pushing oil higher.",
            "source_zh": "路透社", "source_en": "Reuters",
            "url": "https://economictimes.indiatimes.com/markets/us-stocks/news/us-bonds-fall-as-markets-weight-inflation-middle-east-risks/articleshow/133130271.cms",
            "tag": "#27ae60",
        },
        {
            "zh_title": "美法官撤销对印度富豪阿达尼的贿赂欺诈指控",
            "en_title": "US judge dismisses bribery and fraud charges against Gautam Adani",
            "published": "14:30 2026年8月11日",
            "zh_summary": "纽约联邦法官批准司法部撤诉，但批评高层未充分咨询办案检察官，阿达尼称对司法程序保持尊重。",
            "en_summary": "A federal judge approved dropping charges against Gautam Adani but criticised how prosecutors were sidelined.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/clyqxknpp26o",
            "tag": "#2980b9",
        },
        {
            "zh_title": "美的置业上半年资产运营收入翻倍",
            "en_title": "Midea Real Estate asset operations revenue doubles in first half",
            "published": "13:46 2026年8月11日",
            "zh_summary": "剥离开发业务近两年后，美的置业上半年资产运营收入5.59亿元，同比增103%，经营利润占比过半。",
            "en_summary": "Midea Real Estate's asset operations revenue rose 103% to 559 million yuan, now over half of operating profit.",
            "source_zh": "财新", "source_en": "Caixin",
            "url": "https://www.caixin.com/2026-08-11/102473131.html",
            "tag": "#8e44ad",
        },
    ]),
    ("社会 Society", [
        {
            "zh_title": "特朗普签署行政令要求拆分儿童疫苗接种",
            "en_title": "Trump signs order to space out childhood vaccines",
            "published": "06:24 2026年8月11日",
            "zh_summary": "行政令主张将MMR等联合疫苗拆为单剂接种，医学界警告可能增加感染风险，共和党参议员亦公开反对。",
            "en_summary": "Trump ordered separate childhood shots including split MMR doses, drawing medical warnings and GOP Senate pushback.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/vaccine-research-autism-trump-kennedy-rfk-d10f81f221c4ae9f5b2f83dd0ee98b29",
            "tag": "#d35400",
        },
        {
            "zh_title": "法国今夏山火已拘420人，九成火灾系人为",
            "en_title": "France arrests 420 people as human activity drives most wildfires",
            "published": "07:59 2026年8月9日",
            "zh_summary": "法国内政部称今夏逾30万英亩林地烧毁，420人因故意或过失纵火被拘，含166名未成年人。",
            "en_summary": "France arrested 420 people, including 166 minors, as officials say nine in ten wildfires involve human activity.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.co.uk/news/articles/cvgxjn92x9jo",
            "tag": "#2980b9",
        },
        {
            "zh_title": "澳大利亚人口普查首次纳入性取向与性别认同问题",
            "en_title": "Australia census adds optional sexual orientation and gender questions",
            "published": "00:00 2026年8月11日",
            "zh_summary": "8月11日五年一度人口普查首次允许16岁以上居民自愿披露性取向及与出生登记性别是否一致。",
            "en_summary": "Australia's Aug 11 census lets residents aged 16+ optionally disclose sexual orientation and gender identity.",
            "source_zh": "美联社", "source_en": "AP",
            "url": "https://apnews.com/article/australia-census-sexual-orientation-gender-gay-lesbian-a442c949e0570a0b0c2a310269228e34",
            "tag": "#d35400",
        },
        {
            "zh_title": "澳总理因评论日首相赠瓜礼物遭批评",
            "en_title": "Australia PM under fire over remarks on Japanese leader's melon gift",
            "published": "16:30 2026年8月11日",
            "zh_summary": "阿尔巴尼斯在播客谈及高市早苗所赠皇冠蜜瓜时手势引争议，前驻澳日大使斥其性别歧视，反对党要求道歉。",
            "en_summary": "Anthony Albanese faces backlash over podcast comments about melons gifted by Japan's PM Sanae Takaichi.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c0jl6ewvq42o",
            "tag": "#2980b9",
        },
    ]),
    ("国际 World", [
        {
            "zh_title": "乌克兰称打击距前线1500公里俄奥尔斯科炼油厂",
            "en_title": "Ukraine says it struck Russian Orsk refinery 1,500km from front line",
            "published": "08:00 2026年8月11日",
            "zh_summary": "乌军称夜间深度打击奥伦堡州奥尔斯科炼油厂，同期俄袭击致乌至少9人死亡，泽连斯基指俄使用朝鲜导弹。",
            "en_summary": "Kyiv said it hit an Orsk refinery 1,500km away as Russian strikes killed at least nine people across Ukraine overnight.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/live/cn9454xy0l7t",
            "tag": "#2980b9",
        },
        {
            "zh_title": "利比亚扎维耶炼油厂遭无人机袭击引发大火",
            "en_title": "Huge fire at Libya's Zawiya refinery after drone attack",
            "published": "04:00 2026年8月11日",
            "zh_summary": "该国最大炼油厂汽油储罐被击中后坍塌，国家石油公司警告若袭击持续将宣布不可抗力并停产。",
            "en_summary": "A gasoline tank at Libya's largest refinery collapsed in a drone strike; NOC warned it may halt operations.",
            "source_zh": "半岛电视台", "source_en": "Al Jazeera",
            "url": "https://www.aljazeera.com/news/2026/8/11/huge-fire-breaks-out-at-libyas-zawiya-refinery-after-drone-attack",
            "tag": "#c0392b",
        },
        {
            "zh_title": "哥伦比亚7.4级地震遇难人数升至至少132人",
            "en_title": "Colombia earthquake death toll rises to at least 132",
            "published": "12:30 2026年8月11日",
            "zh_summary": "西部佩雷拉、卡利等地大量建筑倒塌，新总统宣布国家灾难状态，逾570人受伤，搜救仍在进行。",
            "en_summary": "At least 132 people died in western Colombia's magnitude 7.4 quake, with over 570 injured and rescues ongoing.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c20e360lx0vo",
            "tag": "#2980b9",
        },
        {
            "zh_title": "内塔尼亚胡正式拒绝特朗普15点加沙和平方案",
            "en_title": "Netanyahu rejects Trump's 15-point Gaza peace plan",
            "published": "17:30 2026年8月10日",
            "zh_summary": "以总理称在哈马斯真正解除武装前不会撤军，与美方路线图要求分阶段撤军形成公开分歧。",
            "en_summary": "Israel's PM said troops will not withdraw until Hamas is genuinely disarmed, rejecting the US roadmap.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c5yw4lpe0yeo",
            "tag": "#2980b9",
        },
    ]),
    ("香港本地 Hong Kong", [
        {
            "zh_title": "酷热下元朗等地停电停空调，逾2400户受影响",
            "en_title": "Power and AC outages hit Yuen Long estate amid heatwave",
            "published": "16:50 2026年8月11日",
            "zh_summary": "元朗水边围邨凌晨电缆故障致约2400户停电，湾仔及红磡亦有楼宇及殡仪馆空调中断。",
            "en_summary": "About 2,400 Yuen Long households lost power in extreme heat, with outages also hitting Wan Chai and Hung Hom.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/society/article/3363653/power-ac-outages-hit-estate-office-building-and-funeral-home-amid-heatwave",
            "tag": "#c0392b",
        },
        {
            "zh_title": "《南华早报》在马来西亚签署三项合作备忘录",
            "en_title": "SCMP signs three MOUs in Malaysia to deepen regional ties",
            "published": "11:26 2026年8月11日",
            "zh_summary": "报社与东南亚未来倡议中心、星报集团及马港澳商会签约，配合贸发局“思汇商机”代表团访马。",
            "en_summary": "SCMP signed MOUs with SEAFIC, Star Media and MayCham during Hong Kong's trade mission to Malaysia.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363599/scmp-signs-3-mous-malaysia-deepen-hong-kong-asean-regional-cooperation",
            "tag": "#c0392b",
        },
        {
            "zh_title": "港警拘8人涉620万港元“糖宝”约会诈骗",
            "en_title": "Hong Kong police arrest eight in HK$6.2m sugar-baby scam",
            "published": "14:08 2026年8月10日",
            "zh_summary": "诈骗团伙在社交媒体招揽有偿约会，假扮律师收取所谓合约费，80名受害者包括教师及医护人员。",
            "en_summary": "Police arrested eight over a compensated-dating scam that cheated 80 victims out of HK$6.2 million.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363500/hong-kong-police-arrest-8-over-hk62-million-sugar-baby-dating-scam",
            "tag": "#c0392b",
        },
        {
            "zh_title": "法院批准11名在囚反对派人士最后一次上诉",
            "en_title": "Court grants final appeal bid by 11 jailed opposition figures",
            "published": "13:04 2026年8月10日",
            "zh_summary": "上诉庭认定2020年初选案有五项重大法律问题值得终审法院审议，涉及议员职责与刑事界限。",
            "en_summary": "Hong Kong's Court of Appeal granted final leave on five legal issues in the 2020 primary election subversion case.",
            "source_zh": "南华早报", "source_en": "SCMP",
            "url": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3363492/court-approves-last-attempt-11-jailed-opposition-figures-clear-their-name",
            "tag": "#c0392b",
        },
    ]),
    ("其他 Other", [
        {
            "zh_title": "全球海洋7月表面温度创历史同期新高",
            "en_title": "World's oceans hit record-high July surface temperatures",
            "published": "18:30 2026年8月10日",
            "zh_summary": "哥白尼气候服务称非极地海域平均海温20.96°C，超2023年7月纪录，厄尔尼诺发展加剧热浪与山火。",
            "en_summary": "Copernicus said extra-polar sea surface temperatures hit 20.96C in July, a record fueled partly by El Niño.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cpvw8vmmgrwo",
            "tag": "#7f8c8d",
        },
        {
            "zh_title": "英仙座流星雨今夜至明晨迎来年度峰值",
            "en_title": "Perseid meteor shower reaches peak this week",
            "published": "09:30 2026年8月11日",
            "zh_summary": "流星雨8月12至13日凌晨达峰，恰逢新月无月光干扰，远离光污染处或可见每小时逾百颗流星。",
            "en_summary": "The Perseids peak overnight Aug 12-13 under a new moon, offering potentially 100+ meteors per hour.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/c4g3kn216yzo",
            "tag": "#7f8c8d",
        },
        {
            "zh_title": "芬兰瑞典时隔数十年恢复跨境客运列车",
            "en_title": "New train service links Finland and Sweden after decades",
            "published": "11:00 2026年8月11日",
            "zh_summary": "奥卢至瑞典哈帕兰达每日两班列车周一首发，可衔接欧洲最长约5000公里铁路线路至葡萄牙。",
            "en_summary": "A new Oulu-Haparanda passenger service restores a Finland-Sweden rail link after decades of suspension.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/news/articles/cx2lwpzz6qjo",
            "tag": "#7f8c8d",
        },
        {
            "zh_title": "图帕克谋杀案嫌疑人“Keffe D”庭审陪审团遴选开始",
            "en_title": "Jury selection begins in Tupac murder trial of Duane 'Keffe D' Davis",
            "published": "00:00 2026年8月10日",
            "zh_summary": "63岁戴维斯被控1996年拉斯维加斯枪击说唱歌手图帕克，距案发近30年，庭审预计持续约一个月。",
            "en_summary": "Jury selection began for Duane Davis, charged with the 1996 murder of rapper Tupac Shakur in Las Vegas.",
            "source_zh": "BBC", "source_en": "BBC",
            "url": "https://www.bbc.com/pidgin/articles/c39e3km40kvo",
            "tag": "#7f8c8d",
        },
    ]),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_html():
    items_html = []
    n = 0
    for cat_name, items in CATEGORIES:
        cat_block = f'<h2 style="margin:28px 0 14px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:16px;color:#1a1a2e;">{esc(cat_name)}</h2>'
        for it in items:
            n += 1
            num = f"{n:02d}"
            items_html.append(f'''<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
<span style="display:inline-block;background:#2563eb;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:3px;margin-bottom:6px;">{num}</span>
<div style="font-size:15px;font-weight:700;margin-bottom:4px;"><a href="{esc(it["url"])}" style="color:#1a1a2e;text-decoration:none;">{esc(it["zh_title"])}</a></div>
<div style="font-size:13px;color:#555;font-style:italic;margin-bottom:4px;">{esc(it["en_title"])}</div>
<div style="font-size:11px;color:#888;margin-bottom:8px;">发布时间 Published: {esc(it["published"])}</div>
<div style="font-size:13px;color:#333;line-height:1.6;margin-bottom:4px;">{esc(it["zh_summary"])}</div>
<div style="font-size:12px;color:#666;line-height:1.5;margin-bottom:8px;">{esc(it["en_summary"])}</div>
<span style="display:inline-block;background:{it["tag"]};color:#fff;font-size:10px;padding:2px 8px;border-radius:3px;margin-right:8px;">{esc(it["source_zh"])} / {esc(it["source_en"])}</span>
<a href="{esc(it["url"])}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</div>''')
        items_html.insert(len(items_html) - len(items), cat_block) if False else None

    # Rebuild with proper category headers
    parts = []
    n = 0
    for cat_name, items in CATEGORIES:
        parts.append(f'<h2 style="margin:28px 0 14px;padding:10px 14px;background:#f0f3f7;border-left:4px solid #2563eb;font-size:16px;color:#1a1a2e;">{esc(cat_name)}</h2>')
        for it in items:
            n += 1
            num = f"{n:02d}"
            parts.append(f'''<div style="margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid #eee;">
<span style="display:inline-block;background:#2563eb;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:3px;margin-bottom:6px;">{num}</span>
<div style="font-size:15px;font-weight:700;margin-bottom:4px;"><a href="{esc(it["url"])}" style="color:#1a1a2e;text-decoration:none;">{esc(it["zh_title"])}</a></div>
<div style="font-size:13px;color:#555;font-style:italic;margin-bottom:4px;">{esc(it["en_title"])}</div>
<div style="font-size:11px;color:#888;margin-bottom:8px;">发布时间 Published: {esc(it["published"])}</div>
<div style="font-size:13px;color:#333;line-height:1.6;margin-bottom:4px;">{esc(it["zh_summary"])}</div>
<div style="font-size:12px;color:#666;line-height:1.5;margin-bottom:8px;">{esc(it["en_summary"])}</div>
<span style="display:inline-block;background:{it["tag"]};color:#fff;font-size:10px;padding:2px 8px;border-radius:3px;margin-right:8px;">{esc(it["source_zh"])} / {esc(it["source_en"])}</span>
<a href="{esc(it["url"])}" style="font-size:12px;color:#2563eb;text-decoration:none;">查看全文 Read more →</a>
</div>''')

    body = "\n".join(parts)
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日热点晚报 {DATE}</title></head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">
<div style="font-size:22px;font-weight:700;color:#fff;margin-bottom:6px;">每日热点晚报</div>
<div style="font-size:14px;color:#a8b8d8;">Evening News Briefing · {DATE} · 共 {TOTAL} 条</div>
</td></tr>
<tr><td style="padding:20px 24px 8px;">
<div style="font-size:14px;color:#333;line-height:1.7;margin-bottom:6px;">以下为今日全日要闻精选，涵盖盘中动态、政策发布与社会热点。</div>
<div style="font-size:13px;color:#666;line-height:1.6;margin-bottom:4px;">Today's main stories — market moves, policy updates and social highlights from across the day.</div>
</td></tr>
<tr><td style="padding:4px 24px 24px;">
{body}
</td></tr>
<tr><td style="background:#f8f9fa;padding:18px 24px;border-top:1px solid #eee;">
<div style="font-size:11px;color:#999;line-height:1.6;">本简报由自动化系统编发，仅供参考，不构成投资建议。新闻版权归原媒体所有。<br>This briefing is auto-generated for informational purposes only. All rights belong to original publishers.</div>
</td></tr>
</table></td></tr></table>
</body></html>'''
    return html


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    root = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root, "email_payload.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Built email_payload.json ({len(html)} chars, {TOTAL} items)")


if __name__ == "__main__":
    main()
