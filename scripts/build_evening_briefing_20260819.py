#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 2026-08-19 evening briefing HTML and email_payload.json."""
import json
import os
import re

OUT_HTML = os.path.join(os.path.dirname(__file__), "..", "briefing_evening_20260819.html")
OUT_JSON = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")

# Colors for source pills
SRC = {
    "xinhua": ("#c0392b", "新华社 Xinhua"),
    "caixin": ("#1a5276", "财新 Caixin"),
    "chinanews": ("#b03a2e", "中国新闻社 China News Service"),
    "scmp": ("#1e8449", "南华早报 SCMP"),
    "bbc": ("#922b21", "BBC"),
    "rthk": ("#6c3483", "香港电台 RTHK"),
    "st": ("#1b4f72", "海峡时报 The Straits Times"),
    "aj": ("#935116", "半岛电视台 Al Jazeera"),
    "ap": ("#2e4053", "美联社 AP"),
    "reuters": ("#ff6f00", "路透社 Reuters"),
}

ITEMS = [
    # 国内 01-04
    dict(cat="国内 China Mainland", n="01",
         zh="王毅将访问韩国、印尼并出席中印尼外长防长对话",
         en="Wang Yi to visit South Korea and Indonesia",
         pub="10:33 2026年8月19日",
         zhs="外交部称，王毅应邀于19日至22日访韩、印尼，并将与董军出席中印尼外长防长“2+2”第二次会议。",
         ens="China's foreign minister will visit South Korea and Indonesia from Aug. 19-22 and join a 2+2 ministerial meeting in Jakarta.",
         src="xinhua",
         url="https://english.news.cn/20260819/570e847abd11488a866a47894334be86/c.html"),
    dict(cat="国内 China Mainland", n="02",
         zh="医保局规划提出大力推动商业医疗保险",
         en="NHSA plan elevates support for private health insurance",
         pub="15:13 2026年8月19日",
         zhs="国家医保局印发全民医保“十五五”规划，将商保支持力度提升为大力推动，并支持数据共享与快赔直赔。",
         ens="China's medical insurance regulator issued a 2026-30 plan backing private health cover more strongly, including data sharing and faster payouts.",
         src="caixin",
         url="https://finance.caixin.com/2026-08-19/102475666.html"),
    dict(cat="国内 China Mainland", n="03",
         zh="朱雀三号完成中国首次入轨火箭陆地回收",
         en="China completes first land recovery of an orbital booster",
         pub="07:58 2026年8月19日",
         zhs="蓝箭航天朱雀三号遥二7时35分升空，一子级按计划在甘肃民勤着陆，飞行任务取得圆满成功。",
         ens="LandSpace's Zhuque-3 first stage landed in Gansu after a 7:35 a.m. launch, China's first land recovery of an orbital booster.",
         src="xinhua",
         url="http://www.xinhuanet.com/politics/20260819/1a901f63eb2c43fd9793eaf6849bce47/c.html"),
    dict(cat="国内 China Mainland", n="04",
         zh="2026世界机器人大会在北京开幕",
         en="World Robot Conference opens in Beijing",
         pub="15:32 2026年8月19日",
         zhs="大会以“人机共生，产需共融”为主题在北京开幕，300余家企业携3000余件展品亮相，为期五天。",
         ens="The 2026 World Robot Conference opened in Beijing, with more than 300 firms showing over 3,000 exhibits across five days.",
         src="chinanews",
         url="https://www.chinanews.com.cn/cj/2026/08-19/10680358.shtml"),
    # 科技 05-08
    dict(cat="科技 Technology", n="05",
         zh="宇树科技科创板上市开盘大涨629%",
         en="Unitree soars 629% on Shanghai Star Market debut",
         pub="09:45 2026年8月19日",
         zhs="人形机器人公司宇树科技开盘报1100元，较发行价150.80元上涨629.44%，为今年开盘涨幅最高新股。",
         ens="Unitree Robotics opened at 1,100 yuan, up 629% from its 150.80 yuan issue price, the year's largest opening gain.",
         src="caixin",
         url="https://finance.caixin.com/2026-08-19/102475557.html"),
    dict(cat="科技 Technology", n="06",
         zh="港金交所合资搭建黄金交易清算平台",
         en="Hong Kong Gold Exchange launches tech joint venture",
         pub="11:28 2026年8月19日",
         zhs="香港黄金交易所与TGX成立合资公司，联合阿里云等建设交易清算平台，拟于2027年一季度试运行。",
         ens="Hong Kong's gold bourse and TGX, backed by Alibaba Cloud, formed a venture to build a trading and clearing platform for a 2027 pilot.",
         src="scmp",
         url="https://www.scmp.com/business/china-business/article/3364508/hong-kong-gold-exchange-taps-tech-strength-joint-venture-power-gold-settlement"),
    dict(cat="科技 Technology", n="07",
         zh="电商法修改需回应人工智能与平台变革",
         en="E-commerce law seen due for an AI-era update",
         pub="14:05 2026年8月19日",
         zhs="有法律界人士指出，正在讨论的电商法修改应回应平台竞争、直播带货与人工智能带来的新挑战。",
         ens="A legal commentary said pending e-commerce law revisions should address platform rivalry, livestream selling and artificial intelligence.",
         src="caixin",
         url="https://opinion.caixin.com/2026-08-19/102475642.html"),
    dict(cat="科技 Technology", n="08",
         zh="贝恩资本竺稼：AI能否兑现落地预期是关键",
         en="Bain Capital's Zhu Jia: AI bets hinge on real-world payoff",
         pub="13:55 2026年8月19日",
         zhs="竺稼对财新表示，市场是否存在泡沫，核心要看企业能否兑现AI落地预期，软硬件仍有新应用空间。",
         ens="Bain Capital's Zhu Jia told Caixin that talk of an AI bubble hinges on whether firms can deliver, with new application tracks still open.",
         src="caixin",
         url="https://www.caixin.com/2026-08-19/102475635.html"),
    # 财经 09-13
    dict(cat="财经 Finance & Business", n="09",
         zh="港股科指收跌、恒指微升，A股科技股重挫",
         en="Hong Kong tech falls as mainland growth boards slump",
         pub="17:10 2026年8月19日",
         zhs="恒生科技指数收跌1.2%，恒指微升0.1%报25495点；内地科创50与创业板指分别下跌约6.9%和6.3%。",
         ens="Hang Seng Tech fell 1.2% while the Hang Seng Index rose 0.1% to 25,495.07; China's STAR 50 and ChiNext dropped about 6.9% and 6.3%.",
         src="scmp",
         url="https://www.scmp.com/business/china-business/article/3364498/hong-kong-stocks-decline-rising-bond-yields-and-stalemate-iran-war-dent-sentiment"),
    dict(cat="财经 Finance & Business", n="10",
         zh="港交所第二季盈利再创新高",
         en="HKEX posts record second-quarter profit",
         pub="12:13 2026年8月19日",
         zhs="港交所第二季净利同比升21%至53.8亿港元，上半年盈利105.7亿港元，均高于预期，拟派中期息7.43港元。",
         ens="HKEX's second-quarter net profit rose 21% to HK$5.38 billion, a record, as first-half earnings also beat analyst estimates.",
         src="scmp",
         url="https://www.scmp.com/business/banking-finance/article/3364515/hkex-profit-jumps-record-high-surging-ipos-and-turnover-beating-market-estimates"),
    dict(cat="财经 Finance & Business", n="11",
         zh="特朗普宣布推迟对加拿大加征50%关税",
         en="Trump pauses 50% tariffs on Canada for three days",
         pub="10:41 2026年8月19日",
         zhs="特朗普称美加已有协议、待文件敲定，将原定生效的50%关税推迟三日；加总理卡尼称谈判取得重大进展。",
         ens="Trump delayed 50% tariffs on Canadian goods for three days, saying a deal awaits paperwork; Ottawa cited substantial progress.",
         src="bbc",
         url="https://www.bbc.co.uk/news/articles/cy9wz79ze29o"),
    dict(cat="财经 Finance & Business", n="12",
         zh="油价升至三周高位，霍尔木兹前景未明",
         en="Oil hits a three-week high on Hormuz uncertainty",
         pub="15:54 2026年8月19日",
         zhs="布伦特原油一度升至约91.5美元。特朗普称海峡畅通，伊朗则称水道仍关闭，多数船东选择绕行。",
         ens="Brent rose toward $91.5 a barrel as Trump said Hormuz was open while Iran said it remained shut, keeping shipowners wary.",
         src="reuters",
         url="https://www.marketscreener.com/news/oil-extends-climb-on-prolonged-hormuz-export-uncertainty-ce7859ddde80f72d"),
    dict(cat="财经 Finance & Business", n="13",
         zh="香港人民币快速支付额升至六个月高位",
         en="Yuan FPS transfers in Hong Kong hit a six-month high",
         pub="08:00 2026年8月19日",
         zhs="7月香港FPS人民币交易额达350.3亿元，较2月升34%；分析指“支付通”扩大了跨境小额转账应用。",
         ens="Hong Kong's yuan FPS volume reached 35.03 billion yuan in July, up 34% from February, aided by the Payment Connect link.",
         src="scmp",
         url="https://www.scmp.com/business/banking-finance/article/3364413/use-yuan-hits-6-month-high-hong-kongs-fast-payment-system"),
    # 社会 14-17
    dict(cat="社会 Society", n="14",
         zh="元朗咬死两只宠物的大型犬或被人道处理",
         en="Yuen Long dog that killed two pets may be put down",
         pub="10:36 2026年8月19日",
         zhs="渔护署称，若饲主交出动物理应考虑人道处理；若自行饲养，或列为已知危险犬只，外出须佩口罩并限绳长。",
         ens="Hong Kong officials said a large dog that killed two pets in Yuen Long could be euthanised if surrendered, or listed as dangerous.",
         src="rthk",
         url="https://news.rthk.hk/rthk/en/component/k2/1866687-20260819.htm"),
    dict(cat="社会 Society", n="15",
         zh="罗湖海关检获200只涉嫌非法进口活鸟",
         en="Customs seize 200 live birds at Lo Wu",
         pub="13:00 2026年8月19日",
         zhs="海关在罗湖截获两名旅客行李中的200只涉嫌非法进口活鸟，估值约2万港元，两人已被捕。",
         ens="Hong Kong Customs seized 200 suspected illegal live birds worth about HK$20,000 from two passengers at Lo Wu; both were arrested.",
         src="rthk",
         url="https://news.rthk.hk/rthk/en/component/k2/1866707-20260819.htm"),
    dict(cat="社会 Society", n="16",
         zh="津巴布韦渡轮事故死亡人数升至94人",
         en="Zimbabwe ferry death toll rises to 94",
         pub="01:31 2026年8月19日",
         zhs="政府称卡里巴湖倾覆渡轮载客约180人，约为核定人数两倍，死亡94人，已救出77人，搜救工作尚未结束。",
         ens="Zimbabwe said a Lake Kariba ferry carried about 180 people, double its listed capacity, as the death toll rose to 94.",
         src="st",
         url="https://www.straitstimes.com/world/zimbabwe-ferry-death-toll-reaches-94-as-government-confirms-it-was-over-capacity"),
    dict(cat="社会 Society", n="17",
         zh="福奇前顾问承认隐瞒新冠研究相关记录",
         en="Ex-Fauci adviser pleads guilty over COVID research records",
         pub="00:00 2026年8月18日",
         zhs="福奇前高级顾问莫伦斯承认共谋欺诈美国政府，检方指其用私人邮箱规避公开记录法，最高可判五年。",
         ens="David Morens, a former senior adviser to Anthony Fauci, pleaded guilty to conspiring to hide federal COVID research records.",
         src="ap",
         url="https://www.wral.com/news/ap/f0a02-ex-fauci-adviser-pleads-guilty-to-plotting-to-conceal-covid-19-research-records-during-pandemic/"),
    # 国际 18-21
    dict(cat="国际 World", n="18",
         zh="阿联酋暂停与伊朗一切贸易和金融往来",
         en="UAE suspends all trade and financial ties with Iran",
         pub="05:45 2026年8月19日",
         zhs="阿联酋外交部凌晨宣布，因地区局势升级，暂停与伊朗一切贸易、商业往来和金融交易；伊朗否认发射导弹。",
         ens="The UAE halted all trade and financial dealings with Iran after reporting two ballistic missiles; Tehran called the claim baseless.",
         src="xinhua",
         url="https://www.news.cn/20260819/bd858d234d934442b466571a61e50934/c.html"),
    dict(cat="国际 World", n="19",
         zh="韩美联合军演应美方要求提前六日结束",
         en="US-South Korea drills cut short after Washington request",
         pub="11:39 2026年8月19日",
         zhs="韩国国防部称，“乙支自由之盾”演习将于21日而非27日结束，野外训练规模亦将部分缩减。",
         ens="Seoul said Ulchi Freedom Shield will end Aug. 21 instead of Aug. 27, after a US request to shorten and scale back the drills.",
         src="bbc",
         url="https://www.bbc.co.uk/news/articles/cnvn0j31qj8o"),
    dict(cat="国际 World", n="20",
         zh="乌克兰前防长呼吁战时举行总统选举",
         en="Sacked Ukraine defence minister calls for wartime election",
         pub="09:31 2026年8月19日",
         zhs="被解职的费多罗夫发视频称民主不能被俄罗斯挟持，呼吁建立战时亦可恢复选举的机制，泽连斯基尚未回应。",
         ens="Mykhailo Fedorov called for a legal way to hold elections under martial law, the strongest challenge yet to Zelensky's wartime rule.",
         src="bbc",
         url="https://www.bbc.co.uk/news/articles/cdew8n9erlwo"),
    dict(cat="国际 World", n="21",
         zh="美国谴责以色列空袭叙利亚空军基地",
         en="US rebukes Israeli strikes on a Syrian airbase",
         pub="00:00 2026年8月19日",
         zhs="美特使称以色列空袭阿布杜胡尔基地属不必要升级；以方指叙利亚正允许土军进驻，叙土予以否认。",
         ens="A US envoy called Israeli strikes on Syria's Abu Duhur airbase an unnecessary escalation; Israel cited a possible Turkish deployment.",
         src="bbc",
         url="https://www.bbc.co.uk/news/articles/c62vy3wl31lo"),
    # 香港 22-24
    dict(cat="香港本地 Hong Kong", n="22",
         zh="邓炳强与深圳官员视察新皇岗口岸",
         en="Hong Kong and Shenzhen inspect new Huanggang port",
         pub="16:43 2026年8月19日",
         zhs="保安局局长邓炳强与深圳代表团视察新皇岗口岸，称系统完备并通过跨境负荷检验后，目标是尽早开通。",
         ens="Security chief Chris Tang and Shenzhen officials inspected the new Huanggang port, aiming to open it after systems pass cross-border load checks.",
         src="rthk",
         url="https://news.rthk.hk/rthk/en/component/k2/1866732-20260819.htm"),
    dict(cat="香港本地 Hong Kong", n="23",
         zh="香港单车节将新增56公里非竞赛路线",
         en="Hong Kong Cyclothon to add a 56km fun-ride route",
         pub="16:32 2026年8月19日",
         zhs="旅发局宣布10月11日单车节非竞赛路线延至56公里，途经五隧三桥，职业赛将有约100名车手参赛。",
         ens="Hong Kong's Oct. 11 cyclothon will extend its main fun ride to 56km across five tunnels and three bridges; a UCI race also returns.",
         src="rthk",
         url="https://news.rthk.hk/rthk/en/component/k2/1866730-20260819.htm"),
    dict(cat="香港本地 Hong Kong", n="24",
         zh="逾2600人演练国际刑警大会安保",
         en="Hong Kong stages a mass drill for the INTERPOL assembly",
         pub="15:46 2026年8月19日",
         zhs="警务处等部门逾2600人在会展中心及西九模拟人流、海陆交通及袭击情景，为11月国际刑警大会做准备。",
         ens="More than 2,600 personnel drilled crowd control and attack scenarios at the convention centre and West Kowloon ahead of November's INTERPOL assembly.",
         src="rthk",
         url="https://news.rthk.hk/rthk/en/component/k2/1866723-20260819.htm"),
    # 其他 25-26
    dict(cat="其他 Other", n="25",
         zh="佛州初选预计唐纳兹与乔利对决州长",
         en="Donalds and Jolly projected to win Florida governor primaries",
         pub="08:50 2026年8月19日",
         zhs="美媒预计共和党众议员唐纳兹与民主党乔利赢得佛州州长初选，将在11月对决，以接替任期届满的德桑蒂斯。",
         ens="US media projected Republican Byron Donalds and Democrat David Jolly to win Florida's gubernatorial primaries and meet in November.",
         src="bbc",
         url="https://www.bbc.co.uk/news/articles/cpvwgym9xl9o"),
    dict(cat="其他 Other", n="26",
         zh="泰国寻求以南疆治理改革推动和谈",
         en="Thailand seeks a new path in the southern insurgency",
         pub="14:01 2026年8月19日",
         zhs="泰国首席谈判代表称将告别以交易换降暴力的旧思路，探讨分权等治理安排，以重启南部和平进程。",
         ens="Thailand's peace envoy said Bangkok wants to shift from swapping concessions for fewer attacks toward talks on governance in the deep south.",
         src="st",
         url="https://www.straitstimes.com/asia/thailand-seeks-new-path-to-end-deadly-southern-insurgency-negotiator-says"),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def build_html():
    cats = []
    for it in ITEMS:
        if not cats or cats[-1][0] != it["cat"]:
            cats.append((it["cat"], []))
        cats[-1][1].append(it)

    parts = []
    parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>每日热点晚报 Morning News Briefing</title>
</head>
<body style="margin:0;padding:0;background:#eef2f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Noto Sans SC',sans-serif;color:#1c2430;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f6;">
<tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="width:600px;max-width:600px;background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 8px 24px rgba(16,24,40,.08);">
<tr><td style="background:#1a2332;color:#fff;padding:28px 24px 22px;">
<div style="font-size:12px;letter-spacing:.12em;color:#9fb0c8;text-transform:uppercase;">Asia/Shanghai</div>
<div style="font-size:26px;font-weight:700;margin-top:6px;line-height:1.3;">每日热点晚报</div>
<div style="font-size:16px;color:#d5def0;margin-top:4px;">Evening News Briefing · 2026年8月19日 · 共 26 条</div>
</td></tr>
<tr><td style="padding:18px 24px 8px;font-size:14px;line-height:1.7;color:#344054;">
汇总今日全日要闻，覆盖内地政策与开盘后市场、科技产业、社会热点及已发酵的国际局势。<br>
<span style="color:#667085;">Today’s main stories across China, markets, technology, society and world affairs as they stood this afternoon.</span>
</td></tr>
""")
    # Fix accidental Morning in title - I put wrong title. Fix below after build.
    for cat, items in cats:
        parts.append(
            f'<tr><td style="padding:14px 24px 6px;"><h2 style="margin:0;padding:10px 12px;background:#f2f4f8;'
            f'border-left:4px solid #2f6fed;border-radius:0 8px 8px 0;font-size:16px;color:#1a2332;">{esc(cat)}</h2></td></tr>'
        )
        for it in items:
            color, srcname = SRC[it["src"]]
            parts.append(f"""<tr><td style="padding:10px 24px 14px;border-bottom:1px solid #eef2f6;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0">
<tr><td style="width:36px;vertical-align:top;font-weight:700;color:#2f6fed;font-size:15px;">{it["n"]}</td>
<td style="vertical-align:top;">
<a href="{esc(it["url"])}" style="color:#1a365d;font-size:16px;font-weight:700;text-decoration:none;line-height:1.4;">{esc(it["zh"])}</a>
<div style="font-size:13px;font-style:italic;color:#4a5568;margin-top:4px;">{esc(it["en"])}</div>
<div style="font-size:12px;color:#98a2b3;margin-top:4px;">发布时间 Published: {esc(it["pub"])}</div>
<div style="font-size:14px;line-height:1.65;color:#344054;margin-top:8px;">{esc(it["zhs"])}</div>
<div style="font-size:13px;line-height:1.6;color:#667085;margin-top:4px;">{esc(it["ens"])}</div>
<div style="margin-top:10px;">
<span style="display:inline-block;background:{color};color:#fff;font-size:11px;padding:3px 8px;border-radius:12px;">{esc(srcname)}</span>
<a href="{esc(it["url"])}" style="margin-left:10px;font-size:13px;color:#2f6fed;text-decoration:none;">查看全文 Read more →</a>
</div>
</td></tr></table>
</td></tr>""")

    parts.append("""<tr><td style="padding:20px 24px 28px;font-size:11px;line-height:1.6;color:#98a2b3;">
本邮件由公开报道汇编，仅供读者了解当日要闻，不构成投资、法律或政策建议。摘要力求客观中立，细节以原文为准。<br>
This briefing compiles publicly reported headlines for general information only. It is not investment, legal or policy advice. Please refer to the original articles for full detail.
</td></tr>
</table>
</td></tr></table>
</body></html>""")
    html = "".join(parts)
    html = html.replace(
        "<title>每日热点晚报 Morning News Briefing</title>",
        "<title>每日热点晚报 Evening News Briefing</title>",
    )
    return html


def validate(html):
    banned = ["测试", "TEST", "Draft", "draft", "预览", "Part", "续"]
    hits = []
    for w in banned:
        if w in html:
            # allow 南华早报 (contains 早报, not 续). 续 is the issue.
            if w == "续":
                for m in re.finditer("续", html):
                    start = max(0, m.start() - 8)
                    end = min(len(html), m.end() + 8)
                    ctx = html[start:end]
                    hits.append(("续", ctx))
            else:
                hits.append((w, "found"))
    assert html.count("</a>") >= 52
    assert "每日热点晚报" in html and "Evening News Briefing" in html
    assert "Morning Briefing" not in html and "每日热点早报" not in html
    assert "汇总今日全日要闻" in html
    assert len(ITEMS) == 26
    for it in ITEMS:
        assert len(it["zhs"]) <= 55, (it["n"], len(it["zhs"]), it["zhs"])
        wc = len(it["ens"].split())
        assert wc <= 30, (it["n"], wc, it["ens"])
    return hits


def main():
    html = build_html()
    hits = validate(html)
    if hits:
        raise SystemExit(f"banned hits: {hits}")
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    payload = {
        "subject": "每日热点晚报 Evening Briefing - 2026-08-19",
        "htmlContent": html,
        "recipients": ["maymay_xia@163.com", "459729983@qq.com"],
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print("items", len(ITEMS), "chars", len(html))
    print("wrote", OUT_HTML, OUT_JSON)


if __name__ == "__main__":
    main()
