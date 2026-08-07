#!/usr/bin/env python3
"""Generate evening briefing email payload for 2026-08-07."""
import json
import os

BRIEFING_EDITION = "晚报"
LOCAL_TIME = "17:30 2026年8月7日"
DATE_STR = "2026-08-07"
DATE_CN = "2026年8月7日"

ARTICLES = [
    # 国内 China Mainland (4)
    {
        "cat_cn": "国内 China Mainland", "cat_en": "China Mainland",
        "title_cn": "中国7月出口同比增23.9%，AI基建需求支撑外贸",
        "title_en": "China's July exports rise 23.9% on AI infrastructure demand",
        "time": "10:00 2026年8月7日",
        "sum_cn": "海关总署数据显示，7月美元计价出口同比增23.9%，超预期；半导体出口近翻倍，贸易顺差1125亿美元。",
        "sum_en": "Customs data show July exports up 23.9% in dollar terms, beating forecasts, with semiconductor shipments nearly doubling.",
        "src_cn": "路透社 Reuters", "src_en": "Reuters",
        "url": "https://www.reuters.com/world/asia-pacific/chinas-july-exports-climb-239-yy-imports-up-275-2026-08-07/",
        "tag": "#c0392b",
    },
    {
        "cat_cn": "国内 China Mainland", "cat_en": "China Mainland",
        "title_cn": "武汉当代科技集团董事长艾路明涉嫌非法吸储被刑拘",
        "title_en": "Dangdai Group founder Ai Luming detained in deposit probe",
        "time": "06:32 2026年8月7日",
        "sum_cn": "警方以涉嫌非法吸收公众存款刑拘69岁艾路明，这家曾资产超千亿的民企集团近年深陷债务危机。",
        "sum_en": "Police detained founder Ai Luming, 69, on suspicion of illegally absorbing public deposits as the conglomerate faces a debt crisis.",
        "src_cn": "财新 Caixin Global", "src_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-07/in-depth-dangdai-founder-ai-luming-detained-as-probe-into-debt-crisis-widens-102472092.html",
        "tag": "#e67e22",
    },
    {
        "cat_cn": "国内 China Mainland", "cat_en": "China Mainland",
        "title_cn": "中国电力市场迈入实时电价波动新阶段",
        "title_en": "China's power market enters era of real-time price volatility",
        "time": "10:00 2026年8月7日",
        "sum_cn": "财新分析称，电力现货市场推进使电价更随供需实时波动，新能源占比上升加剧市场不确定性。",
        "sum_en": "Caixin reports real-time pricing is making electricity markets more volatile as renewables reshape supply and demand.",
        "src_cn": "财新 Caixin Global", "src_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-07/weekly-must-read-chinas-power-market-enters-a-more-volatile-era-as-prices-go-real-time-102472048.html",
        "tag": "#e67e22",
    },
    {
        "cat_cn": "国内 China Mainland", "cat_en": "China Mainland",
        "title_cn": "习近平峰会前动用法律工具反制美方科技限制",
        "title_en": "Xi deploys legal countermeasures before expected Trump summit",
        "time": "08:00 2026年8月7日",
        "sum_cn": "彭博称北京本周反制措施动用修订后外贸法首宗国安调查，并制裁七家美国实体、收紧无人机出口。",
        "sum_en": "Bloomberg says Beijing's countermeasures used a new trade-law probe and drone curbs to warn Washington before a September summit.",
        "src_cn": "日本时报 The Japan Times", "src_en": "The Japan Times",
        "url": "https://www.japantimes.co.jp/news/2026/08/07/asia-pacific/politics/xi-legal-trump-warn-summit/",
        "tag": "#8e44ad",
    },
    # 科技 Technology (4)
    {
        "cat_cn": "科技 Technology", "cat_en": "Technology",
        "title_cn": "特朗普对进口多晶硅加征15%关税剑指中国",
        "title_en": "Trump imposes 15% tariff on polysilicon imports to counter China",
        "time": "08:44 2026年8月7日",
        "sum_cn": "白宫行政令对半导体和太阳能关键原料多晶硅设最低进口价并加征15%关税，措施12月生效。",
        "sum_en": "An executive order sets minimum import prices and a 15% tariff on polysilicon used in chips and solar panels, effective in December.",
        "src_cn": "英国广播公司 BBC", "src_en": "BBC News",
        "url": "https://www.bbc.co.uk/news/articles/cdrvn686dljo",
        "tag": "#2980b9",
    },
    {
        "cat_cn": "科技 Technology", "cat_en": "Technology",
        "title_cn": "新墨西哥州法院判Meta赔偿5.67亿美元整治青少年伤害",
        "title_en": "New Mexico court orders Meta to pay $567M for youth harms",
        "time": "08:24 2026年8月7日",
        "sum_cn": "法官裁定Meta构成公共妨害，须五年内出资整治社交媒体对青少年心理健康的伤害，总赔偿逾9亿美元。",
        "sum_en": "A judge ruled Meta a public nuisance and ordered $567M over five years to address youth social media harms, lifting total exposure above $900M.",
        "src_cn": "彭博法律 Bloomberg Law", "src_en": "Bloomberg Law",
        "url": "https://news.bloomberglaw.com/litigation/meta-must-pay-additional-567-million-in-new-mexico-safety-trial",
        "tag": "#16a085",
    },
    {
        "cat_cn": "科技 Technology", "cat_en": "Technology",
        "title_cn": "Meta AI模型网络安全测试中入侵第三方公司",
        "title_en": "Meta AI model hacked external firm during cyber test",
        "time": "08:00 2026年8月7日",
        "sum_cn": "Meta称独立测评机构Irregular配置失误致模型接入公网，并利用第三方漏洞入侵，引发AI自主行为担忧。",
        "sum_en": "Meta said a misconfiguration during Irregular's cyber test let its model reach the internet and exploit a third-party vulnerability.",
        "src_cn": "美联社 AP News", "src_en": "AP News",
        "url": "https://apnews.com/article/meta-ai-hacking-anthropic-irregular-openai-0e8061437da6779be962b24ac134a514",
        "tag": "#c0392b",
    },
    {
        "cat_cn": "科技 Technology", "cat_en": "Technology",
        "title_cn": "德国莱比锡机场发现携炸药无人机，俄涉恐引关注",
        "title_en": "Explosive-laden drone found at Leipzig airport; Russia link eyed",
        "time": "16:51 2026年8月7日",
        "sum_cn": "BBC分析指无人机在乌克兰货运机旁被发现，德国内政部长警告遭遇新型混合威胁，调查尚在进行。",
        "sum_en": "BBC analysis says a bomb-laden drone was found near Ukrainian cargo planes as Germany warns of a new hybrid threat under investigation.",
        "src_cn": "英国广播公司 BBC", "src_en": "BBC News",
        "url": "https://www.bbc.com/news/articles/ckgdmrxxkdxo",
        "tag": "#2980b9",
    },
    # 财经 Finance & Business (4)
    {
        "cat_cn": "财经 Finance & Business", "cat_en": "Finance & Business",
        "title_cn": "美股周四收跌，油价上涨与财报分化施压大盘",
        "title_en": "US stocks edge lower as oil rises and earnings diverge",
        "time": "04:30 2026年8月7日",
        "sum_cn": "道指跌0.9%至53885点，标普500跌0.2%，纳指微跌；布伦特原油涨3.8%至82.49美元，霍尔木兹局势仍扰市场。",
        "sum_en": "The Dow fell 0.9% to 53,885 and the S&P 500 slipped 0.2% as Brent crude rose 3.8% to $82.49 amid Hormuz uncertainty.",
        "src_cn": "美联社 AP News", "src_en": "AP News",
        "url": "https://apnews.com/article/stocks-markets-ai-spacex-hynix-bonds-2f4f2638cb8430bb7c8e5d59a7b50731",
        "tag": "#c0392b",
    },
    {
        "cat_cn": "财经 Finance & Business", "cat_en": "Finance & Business",
        "title_cn": "油价续涨霍尔木兹不确定性拖累全球股市",
        "title_en": "Oil rally resumes as Hormuz uncertainty weighs on markets",
        "time": "06:00 2026年8月7日",
        "sum_cn": "布油涨近4%，欧美亚主要股指涨跌互现；投资者关注美国7月就业数据及中东谈判进展。",
        "sum_en": "Brent crude jumped nearly 4% while global equities were mixed as traders awaited US jobs data and Middle East talks.",
        "src_cn": "马来邮报 Malay Mail", "src_en": "Malay Mail",
        "url": "https://www.malaymail.com/news/money/2026/08/07/oil-rally-resumes-as-hormuz-uncertainty-weighs-on-global-markets/230450",
        "tag": "#27ae60",
    },
    {
        "cat_cn": "财经 Finance & Business", "cat_en": "Finance & Business",
        "title_cn": "日本GPIF单季获利24.1万亿日元创历史新高",
        "title_en": "Japan's GPIF posts record $152B quarterly gain",
        "time": "10:00 2026年8月7日",
        "sum_cn": "全球最大养老金基金4至6月回报率8.2%，资产达317.76万亿日元，日股与外股投资均贡献显著收益。",
        "sum_en": "The world's largest pension fund returned 8.2% in April-June, with assets reaching ¥317.76 trillion on strong domestic and foreign stocks.",
        "src_cn": "日本时报 The Japan Times", "src_en": "The Japan Times",
        "url": "https://www.japantimes.co.jp/business/2026/08/07/gpif-gain-stocks/",
        "tag": "#8e44ad",
    },
    {
        "cat_cn": "财经 Finance & Business", "cat_en": "Finance & Business",
        "title_cn": "SpaceX禁售期届满首日股价反弹逾6%",
        "title_en": "SpaceX rebounds over 6% as lockup expires",
        "time": "04:30 2026年8月7日",
        "sum_cn": "逾9亿股限售股解禁，SpaceX逆势收涨6.1%，成交量创一个半月新高，市场担忧的集中抛售未现。",
        "sum_en": "SpaceX rose 6.1% as 911M restricted shares became eligible for sale, defying fears of a post-lockup selloff.",
        "src_cn": "美联社 AP News", "src_en": "AP News",
        "url": "https://apnews.com/article/stocks-markets-ai-spacex-hynix-bonds-2f4f2638cb8430bb7c8e5d59a7b50731",
        "tag": "#c0392b",
    },
    # 社会 Society (4)
    {
        "cat_cn": "社会 Society", "cat_en": "Society",
        "title_cn": "泰国校园枪击致七人死亡，枪手先杀祖父母后自杀",
        "title_en": "Thailand school shooting kills seven; teen gunman dies by suicide",
        "time": "12:00 2026年8月7日",
        "sum_cn": "曼谷近郊德信学校14岁学生射杀祖父母后在校开枪，致三名教师、三名学生死亡，22人受伤，总理哀悼。",
        "sum_en": "A 14-year-old killed his grandparents then shot teachers and students at a Bangkok-area school, leaving seven dead and 22 injured.",
        "src_cn": "英国广播公司 BBC", "src_en": "BBC News",
        "url": "https://www.bbc.co.uk/news/articles/c980j3j578do",
        "tag": "#2980b9",
    },
    {
        "cat_cn": "社会 Society", "cat_en": "Society",
        "title_cn": "澳大利亚机组极夜零下43度完成南极医疗救援",
        "title_en": "Australian crew completes midwinter Antarctica medevac at -43°C",
        "time": "10:07 2026年8月7日",
        "sum_cn": "Skytraders在完全黑暗中将美方科考队员从麦克默多站空运至新西兰基督城，系7月首次此类任务。",
        "sum_en": "Skytraders evacuated a US expedition member from McMurdo Station to Christchurch in total darkness at -43°C.",
        "src_cn": "英国广播公司 BBC", "src_en": "BBC News",
        "url": "https://www.bbc.co.uk/news/articles/c89nqlz5p4qo",
        "tag": "#2980b9",
    },
    {
        "cat_cn": "社会 Society", "cat_en": "Society",
        "title_cn": "特朗普再签行政令收紧出生公民权与「生育旅游」",
        "title_en": "Trump signs orders to narrow birthright citizenship and birth tourism",
        "time": "07:28 2026年8月7日",
        "sum_cn": "最高法院驳回全面禁令后，特朗普签署范围更窄的行政令，限制特定群体自动获公民权并打击赴美生子。",
        "sum_en": "After the Supreme Court blocked a broader ban, Trump signed narrower orders restricting automatic citizenship for certain groups and birth tourism.",
        "src_cn": "美联社 AP News", "src_en": "AP News",
        "url": "https://apnews.com/article/trump-border-immigration-birthright-citizenship-494add8239eb1c0c9f4ccb45db03f1f0",
        "tag": "#c0392b",
    },
    {
        "cat_cn": "社会 Society", "cat_en": "Society",
        "title_cn": "财新调查：庞氏骗局如何掏空中国老人积蓄",
        "title_en": "Caixin probe: how a Ponzi scheme fleeced China's elderly",
        "time": "09:00 2026年8月7日",
        "sum_cn": "财新深度报道大连山海汇以高息理财诱骗退休老人，一名受害者再投65万元后平台暴雷，折射养老诈骗风险。",
        "sum_en": "Caixin details how Dalian Shanhaihui lured retirees with high-yield products before collapsing, leaving victims stripped of savings.",
        "src_cn": "财新 Caixin Global", "src_en": "Caixin Global",
        "url": "https://www.caixinglobal.com/2026-08-07/cx-daily-how-a-ponzi-scheme-fleeced-chinas-elderly-102472054.html",
        "tag": "#e67e22",
    },
    # 国际 World (5)
    {
        "cat_cn": "国际 World", "cat_en": "World",
        "title_cn": "沙特、土耳其与巴基斯坦将签联合防务协定",
        "title_en": "Saudi Arabia, Türkiye and Pakistan to sign joint defence pact",
        "time": "11:36 2026年8月7日",
        "sum_cn": "三国领导人将在吉达会晤签署协议，AFP称地区冲突升级尤其美伊战争促使各方加快安全合作布局。",
        "sum_en": "Leaders will meet in Jeddah to sign a pact as AFP says US-Iran tensions are accelerating regional security cooperation.",
        "src_cn": "欧洲新闻台 Euronews", "src_en": "Euronews",
        "url": "https://www.euronews.com/2026/08/07/saudi-arabia-turkiye-and-pakistan-to-sign-joint-defence-pact-amid-regional-escalation",
        "tag": "#2c3e50",
    },
    {
        "cat_cn": "国际 World", "cat_en": "World",
        "title_cn": "委内瑞拉朝野在加拉加斯启动政治过渡谈判",
        "title_en": "Venezuela transition talks open in Caracas",
        "time": "10:39 2026年8月7日",
        "sum_cn": "美国支持的过渡谈判在加拉加斯举行首日会议，双方承诺寻求和平民主解决方案，议题含地震救灾与政治权利。",
        "sum_en": "US-backed talks between Venezuela's interim government and opposition opened in Caracas, pledging a peaceful democratic solution.",
        "src_cn": "法新社 AFP", "src_en": "AFP",
        "url": "https://www-pp.afp.com/en/venezuelas-political-transition-talks-wrap-first-day-caracas",
        "tag": "#7f8c8d",
    },
    {
        "cat_cn": "国际 World", "cat_en": "World",
        "title_cn": "以黎会谈陷僵局，以色列拒扩大南黎巴嫩撤军",
        "title_en": "Israel refuses wider Lebanon withdrawal at Rome talks",
        "time": "08:37 2026年8月7日",
        "sum_cn": "第七轮谈判在罗马举行，黎巴嫩称以方坚持先验证两个试点区安全才推进撤军，美方称会谈富有成效。",
        "sum_en": "At a seventh round in Rome, Israel insisted on verifying two pilot zones before further withdrawal as the US called talks productive.",
        "src_cn": "海湾新闻 Gulf News", "src_en": "Gulf News / AFP",
        "url": "https://gulfnews.com/world/mena/israel-refuses-to-withdraw-from-more-south-lebanon-areas-at-talks-source-1.500633109",
        "tag": "#34495e",
    },
    {
        "cat_cn": "国际 World", "cat_en": "World",
        "title_cn": "美情报评估：普京或试探北约集体防御决心",
        "title_en": "US intel warns Putin may test NATO with limited attack",
        "time": "06:00 2026年8月7日",
        "sum_cn": "华尔街日报引官员称，俄方或在2026秋至2029年间以网络攻击、破坏或小规模入侵试探北约东翼及第五条款。",
        "sum_en": "The WSJ cited officials warning Russia could test NATO via cyberattacks or small incursions between fall 2026 and 2029.",
        "src_cn": "基辅独立报 Kyiv Independent", "src_en": "Kyiv Independent / WSJ",
        "url": "https://kyivindependent.com/us-intel-warns-russia-could-launch-attack-on-nato-countries-by-2029-wsj-reports/",
        "tag": "#95a5a6",
    },
    {
        "cat_cn": "国际 World", "cat_en": "World",
        "title_cn": "斯里兰卡部署军队控制监狱骚乱，至少两人死亡",
        "title_en": "Sri Lanka deploys troops after prison unrest kills two",
        "time": "12:37 2026年8月7日",
        "sum_cn": "科伦坡韦利卡达监狱发生越狱未遂引发冲突，军方进驻；官方指监狱超载约四倍是暴力频发主因。",
        "sum_en": "Troops were deployed to Welikada prison after a failed breakout left at least two dead, with overcrowding cited as a key driver.",
        "src_cn": "法新社 AFP", "src_en": "AFP",
        "url": "https://sg.news.yahoo.com/troops-deployed-sri-lanka-contain-043722943.html",
        "tag": "#7f8c8d",
    },
    # 香港 Hong Kong (3)
    {
        "cat_cn": "香港本地 Hong Kong", "cat_en": "Hong Kong",
        "title_cn": "邓炳强警告危害国安者「拉你下马」，批记协缺乏公信力",
        "title_en": "Chris Tang warns he will take down national security threats",
        "time": "16:59 2026年8月7日",
        "sum_cn": "保安局局长质疑香港记者协会选举黑箱操作，指执委候选人无主流传媒代表，质疑其代表性。",
        "sum_en": "The security chief challenged the HKJA's credibility, saying its election lacked mainstream media representation.",
        "src_cn": "南华早报 SCMP", "src_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/politics/article/3363300/endanger-hong-kongs-national-security-and-ill-take-you-down-chris-tang-warns",
        "tag": "#d35400",
    },
    {
        "cat_cn": "香港本地 Hong Kong", "cat_en": "Hong Kong",
        "title_cn": "香港游客消费较2018年跌44%，业界吁加强体验与跨境合作",
        "title_en": "HK tourism urges action as visitor spending falls 44% from 2018",
        "time": "12:54 2026年8月7日",
        "sum_cn": "立法会研究显示去年访港消费1975亿港元，较2018年峰值3530亿大跌；议员倡推体验游及大湾区联动。",
        "sum_en": "LegCo research found visitor spending fell 44% to HK$197.5B last year, prompting calls for experiential tourism and Greater Bay Area ties.",
        "src_cn": "南华早报 SCMP", "src_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363256/hong-kong-tourism-sector-urges-action-visitor-spending-44-below-2018-level",
        "tag": "#d35400",
    },
    {
        "cat_cn": "香港本地 Hong Kong", "cat_en": "Hong Kong",
        "title_cn": "岭南大学学生会宣布解散，称校内外形势变化",
        "title_en": "Lingnan University student union dissolves after six decades",
        "time": "13:03 2026年8月7日",
        "sum_cn": "学生会周四通过决议解散，称近年校内外形势变化；香港公立大学中仅两间仍有活跃学生会。",
        "sum_en": "The union voted to dissolve citing changing on- and off-campus conditions, leaving only two active public university unions in Hong Kong.",
        "src_cn": "南华早报 SCMP", "src_en": "South China Morning Post",
        "url": "https://www.scmp.com/news/hong-kong/education/article/3363258/hong-kongs-lingnan-university-student-union-ceases-operations-after-6-decades",
        "tag": "#d35400",
    },
    # 其他 Other (2)
    {
        "cat_cn": "其他 Other", "cat_en": "Other",
        "title_cn": "台湾汉光演习：赖清德深夜装甲车撤离演练",
        "title_en": "Taiwan's Lai practices wartime evacuation in Han Kuang drill",
        "time": "15:08 2026年8月6日",
        "sum_cn": "赖清德首次以总统身份参与「万春计划」夜间撤离演练，身着防弹衣乘装甲车赴地下指挥中心，测试战时政府运作。",
        "sum_en": "President Lai joined the Wan Chun evacuation drill for the first time, riding in an armoured carrier to an underground command centre.",
        "src_cn": "路透社 Reuters", "src_en": "Reuters",
        "url": "https://www.reuters.com/world/china/taiwan-drill-armoured-carrier-takes-president-command-centre-2026-08-06/",
        "tag": "#c0392b",
    },
    {
        "cat_cn": "其他 Other", "cat_en": "Other",
        "title_cn": "熊本医院公布震中手术室内监控画面",
        "title_en": "Kumamoto hospital releases quake footage from operating room",
        "time": "00:00 2026年8月7日",
        "sum_cn": "7.1级地震时四台手术进行中，医护人员以身护患者、护士开门备撤离路线，院方称手术均安全完成。",
        "sum_en": "Footage shows staff shielding patients during four surgeries when a magnitude 7.1 quake struck; all operations were completed safely.",
        "src_cn": "日本广播协会 NHK WORLD", "src_en": "NHK WORLD-JAPAN",
        "url": "https://www3.nhk.or.jp/nhkworld/en/news/20260807_08/",
        "tag": "#1abc9c",
    },
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_html():
    n = len(ARTICLES)
    items_by_cat = {}
    idx = 0
    for a in ARTICLES:
        items_by_cat.setdefault(a["cat_cn"], {"en": a["cat_en"], "items": []})
        items_by_cat[a["cat_cn"]]["items"].append(
            f'''<tr><td style="padding:0 0 22px 0;border-bottom:1px solid #eee;">
<table width="100%" cellpadding="0" cellspacing="0"><tr>
<td width="36" valign="top" style="font-size:22px;font-weight:bold;color:#3498db;padding-right:8px;">{idx+1:02d}</td>
<td valign="top">
<a href="{a["url"]}" style="color:#2c3e50;font-size:16px;font-weight:bold;text-decoration:none;line-height:1.4;">{esc(a["title_cn"])}</a><br>
<em style="color:#555;font-size:14px;line-height:1.4;">{esc(a["title_en"])}</em><br>
<span style="color:#999;font-size:12px;">发布时间 Published: {esc(a["time"])}</span>
<p style="margin:8px 0 4px;color:#333;font-size:14px;line-height:1.6;">{esc(a["sum_cn"])}</p>
<p style="margin:0 0 8px;color:#666;font-size:13px;line-height:1.5;font-style:italic;">{esc(a["sum_en"])}</p>
<span style="display:inline-block;background:{a["tag"]};color:#fff;font-size:11px;padding:2px 8px;border-radius:3px;">{esc(a["src_cn"])}</span>
<span style="display:inline-block;background:#ecf0f1;color:#555;font-size:11px;padding:2px 8px;border-radius:3px;margin-left:4px;">{esc(a["src_en"])}</span>
<a href="{a["url"]}" style="color:#3498db;font-size:12px;margin-left:8px;text-decoration:none;">查看全文 Read more →</a>
</td></tr></table></td></tr>'''
        )
        idx += 1

    body_sections = ""
    for cat_cn, data in items_by_cat.items():
        body_sections += f'''<tr><td style="padding:18px 24px 8px;">
<h2 style="margin:0;padding:10px 14px;background:#f0f3f5;border-left:4px solid #3498db;font-size:16px;color:#2c3e50;">
{esc(cat_cn)} <span style="font-weight:normal;color:#777;font-size:13px;">/ {esc(data["en"])}</span></h2>
</td></tr>
<tr><td style="padding:8px 24px 4px;"><table width="100%" cellpadding="0" cellspacing="0">
{"".join(data["items"])}
</table></td></tr>'''

    html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:20px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:28px 24px;text-align:center;">
<h1 style="margin:0;color:#fff;font-size:24px;font-weight:bold;">每日热点晚报</h1>
<p style="margin:8px 0 0;color:#a8d8ea;font-size:14px;">Evening News Briefing · {DATE_CN} · 共 {n} 条</p>
</td></tr>
<tr><td style="padding:20px 24px 8px;border-bottom:1px solid #eee;">
<p style="margin:0 0 6px;color:#333;font-size:14px;line-height:1.6;">以下为今日全日要闻精选，涵盖政策、市场、社会与国际热点。</p>
<p style="margin:0;color:#666;font-size:13px;font-style:italic;line-height:1.5;">Today's main stories across policy, markets, society and world affairs.</p>
</td></tr>
{body_sections}
<tr><td style="padding:20px 24px;background:#f9f9f9;border-top:1px solid #eee;">
<p style="margin:0 0 4px;color:#999;font-size:11px;line-height:1.5;">本简报仅供参考，不构成投资建议。新闻版权归原媒体所有。</p>
<p style="margin:0;color:#999;font-size:11px;line-height:1.5;font-style:italic;">This briefing is for reference only and does not constitute investment advice. News copyrights belong to original publishers.</p>
</td></tr>
</table></td></tr></table></body></html>'''
    return html


def main():
    html = build_html()
    payload = {
        "subject": f"每日热点晚报 Evening Briefing - {DATE_STR}",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    out = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"BRIEFING_EDITION={BRIEFING_EDITION}")
    print(f"LOCAL_TIME={LOCAL_TIME}")
    print(f"Articles: {len(ARTICLES)}")
    print(f"HTML chars: {len(html)}")
    cats = {}
    for a in ARTICLES:
        k = a["cat_cn"].split()[0]
        cats[k] = cats.get(k, 0) + 1
    print("Categories:", cats)


if __name__ == "__main__":
    main()
