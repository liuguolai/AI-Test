import json

items = [
    ("国内 Domestic", [
        ("庆祝中国共产党成立105周年大会在京举行", "China marks CPC founding with ceremony in Beijing",
         "7月1日上午，庆祝中国共产党成立105周年大会在人民大会堂举行，习近平将颁授七一勋章并发表讲话。",
         "新华网", "https://www.news.cn/politics/leaders/20260629/20a12f3db5c64225b957ec918d10bf5c/c.html"),
        ("小型飞机撞击北京最高楼「中国尊」", "Small plane crashes into Beijing's tallest tower",
         "6月26日一架轻型飞机撞上中信大厦，飞行员死亡、13人受伤，官方信息披露有限。",
         "BBC", "https://www.bbc.com/news/articles/crlwe28dz44o"),
        ("香港各界启动庆祝回归祖国29周年系列活动", "Hong Kong launches handover anniversary events",
         "6月30日启动礼在红馆举行，李家超称香港经济提速、民生改善，GDP增约5%。",
         "新华网", "https://www.news.cn/gangao/20260701/072b3fba415048b690765388407accab/c.html"),
    ]),
    ("科技 Tech", [
        ("美国解除Anthropic先进AI工具出口禁令", "US lifts export ban on Anthropic AI tools",
         "商务部撤销对Claude Fable 5与Mythos 5的出口管制，Anthropic将于7月2日起恢复访问。",
         "BBC", "https://www.bbc.com/news/articles/cdr42623e1do"),
        ("SpaceX完成750亿美元史上最大规模IPO", "SpaceX completes record $75bn IPO",
         "SpaceX以约1.8万亿美元估值上市，刷新全球IPO融资纪录，引发市场高度关注。",
         "Reuters", "https://www.reuters.com/graphics/SPACEX-IPO/byprdokrkpe/"),
    ]),
    ("财经 Finance", [
        ("特朗普披露逾12亿美元加密货币收入", "Trump reports $1.2bn crypto income in filing",
         "2025年财务披露显示，其加密货币相关收入主要来自World Liberty与$TRUMP代币。",
         "AP", "https://apnews.com/article/trump-financial-disclosure-crypto-060c15062b8fedc6104159ea13775463"),
        ("欧美贸易协议欧盟侧承诺7月1日起生效", "EU side of US trade deal takes effect July 1",
         "欧盟按计划取消对美工业品关税并给予农产品优惠准入，以避免美国加征更高关税。",
         "Reuters", "https://www.reuters.com/business/eu-governments-clear-us-trade-deal-legislation-says-eu-source-2026-05-27/"),
        ("市场预期香港或获「Reit Connect」惠港政策", "Hong Kong eyes possible Reit Connect scheme",
         "市场关注回归纪念日是否推出房地产信托跨境互联互通，以深化两地资本市场联系。",
         "SCMP", "https://www.scmp.com/business/banking-finance/article/3358638/beijings-handover-anniversary-policy-gift-hong-kong-it-could-be-reit-connect"),
    ]),
    ("社会 Society", [
        ("巴基斯坦拉合尔补习班屋顶坍塌14名学童遇难", "Roof collapse kills 14 children at Lahore tuition centre",
         "7月1日卡赫纳区一补习班屋顶坍塌，遇难者多为7至11岁儿童，两人被拘。",
         "BBC", "https://www.bbc.com/news/articles/cr7x38lle1jo"),
        ("波兰7月7日起对德国立陶宛边境实施临时管控", "Poland to impose temporary border controls",
         "图斯克称将加强边境管控以应对非法移民，德国总理称需共同保护欧盟外部边界。",
         "Reuters", "https://www.reuters.com/world/europe/poland-introduce-controls-borders-with-germany-lithuania-pm-says-2025-07-01/"),
        ("委内瑞拉地震官方死难者升至1943人", "Venezuela quake death toll rises to 1,943",
         "救援窗口收窄，医疗系统承压，援助组织警告实际伤亡可能被低估。",
         "AP", "https://apnews.com/article/venezuela-earthquakes-survivors-rescue-healthcare-aid-workers-de59847a5afb28f799d693501f2385aa"),
    ]),
    ("国际 International", [
        ("美特使在多哈仅与调解方会面未直接接触伊朗", "US envoys in Doha meet mediators, not Iranians",
         "卡塔尔称暂无美伊高层直接会谈安排，伊朗代表团将讨论冻结资产与谅解备忘录执行。",
         "BBC", "https://www.bbc.com/news/articles/cpd38x1dy4no"),
        ("美最高法院裁定维护出生公民权", "US Supreme Court upholds birthright citizenship",
         "6比3裁决认定宪法第十四修正案保障境内出生者公民身份，驳回特朗普行政令限制。",
         "BBC", "https://www.bbc.com/news/articles/cgmepnx1wzzo"),
        ("阿富汗塔利班跨境打击巴基斯坦边界", "Afghan Taliban launch strikes on Pakistan border",
         "巴方称击落四架简易无人机并警告将回击，地区紧张在停火后再度升级。",
         "BBC", "https://www.bbc.com/news/articles/c621g086ek4o"),
        ("美方称伊朗曾在霍尔木兹海峡附近部署水雷", "US says Iran prepared mines near Strait of Hormuz",
         "两名美国官员称情报显示伊方曾装载水雷但未布设，全球能源运输风险仍受关注。",
         "Reuters", "https://www.reuters.com/world/middle-east/iran-made-preparations-mine-strait-hormuz-us-sources-say-2025-07-01/"),
    ]),
    ("香港本地 Hong Kong", [
        ("香港举行七一升旗仪式庆祝回归29周年", "Hong Kong marks July 1 handover anniversary",
         "金紫荆广场举行升旗礼，李家超将出席酒并发表施政回顾，逾千家商户推出优惠。",
         "SCMP", "https://www.scmp.com/news/hong-kong/society/article/3358962/hong-kong-mark-july-1-anniversary-flag-raising-ceremony-citywide-deals"),
        ("逾千家商户推七一折扣及免费电车等活动", "Citywide July 1 shopping and dining deals",
         "多家餐饮零售品牌推出29折或特价套餐，市民可免费乘电车及使用部分康体设施。",
         "SCMP", "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3358838/no-plans-handover-day-scmp-breaks-down-hong-kongs-biggest-july-1-deals"),
        ("香港7月推出措施强化离岸人民币交易", "Hong Kong to boost offshore yuan trading in July",
         "陈茂波称将推动更多上市公司以人民币交易，并配合打击非法跨境证券交易。",
         "SCMP", "https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3357804/hong-kong-roll-out-measures-boosting-offshore-yuan-trading-july-finance-chief"),
    ]),
    ("其他 Other", [
        ("联邦法官推翻特朗普政府学生贷款减免新规", "Judge strikes down student loan forgiveness overhaul",
         "法院认定教育部越权且新规可能侵犯言论自由，逾百万人公共贷款减免计划得以保留。",
         "AP", "https://apnews.com/article/public-service-loan-forgiveness-trump-debt-5cbe13349bff45bea6ae5fc330d7b617"),
        ("美最高法院维持各州禁止跨性别者参加女子体育赛事", "Court upholds bans on trans athletes in women's sports",
         "裁决认为爱达荷与西弗吉尼亚州禁令不违宪，亦未违反教育法第九条反性别歧视规定。",
         "AP", "https://apnews.com/article/supreme-court-transgender-athletes-school-teams-e01548be1fc0f574d9c274e077414075"),
        ("美国中西部至东岸将迎Independence Day极端高温", "Dangerous US heatwave ahead of July 4 holiday",
         "气象部门警告热指数可达100至115华氏度，费城等地宣布高温紧急并开放避暑中心。",
         "AP", "https://apnews.com/article/weather-heat-great-lakes-midwest-73e11e920b8835aeedd0cad33c4db803"),
    ]),
]

n = sum(len(g[1]) for g in items)
parts = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>Daily Briefing</title></head><body style="margin:0;padding:0;background:#f5f5f5;font-family:Georgia,serif;color:#222;">']
parts.append('<div style="max-width:600px;margin:0 auto;background:#fff;padding:20px 18px;">')
parts.append('<h1 style="margin:0 0 6px;font-size:22px;color:#1a1a1a;">每日热点简报 Daily Briefing</h1>')
parts.append('<p style="margin:0 0 18px;font-size:13px;color:#666;">2026-07-01 · 共 %d 条</p>' % n)
num = 1
for cat, rows in items:
    parts.append('<h2 style="margin:22px 0 10px;padding-bottom:4px;border-bottom:2px solid #c41e3a;font-size:16px;color:#c41e3a;">%s</h2>' % cat)
    for zh, en, summary, source, url in rows:
        parts.append('<div style="margin:0 0 14px;padding-bottom:12px;border-bottom:1px solid #eee;">')
        parts.append('<p style="margin:0 0 4px;font-size:15px;line-height:1.45;"><strong>%d.</strong> <a href="%s" style="color:#1a5490;text-decoration:none;">%s</a></p>' % (num, url, zh))
        parts.append('<p style="margin:0 0 4px;font-size:13px;color:#555;font-style:italic;">%s</p>' % en)
        parts.append('<p style="margin:0 0 6px;font-size:13px;color:#444;line-height:1.5;">%s</p>' % summary)
        parts.append('<p style="margin:0;font-size:11px;color:#888;">[%s] <a href="%s" style="color:#888;">Read more →</a></p>' % (source, url))
        parts.append('</div>')
        num += 1
parts.append('<p style="margin:24px 0 0;font-size:11px;color:#999;line-height:1.5;">免责声明：本简报由自动化系统汇编公开报道，仅供信息参考，不构成投资或法律建议。链接指向第三方网站，请以原文为准。</p>')
parts.append('</div></body></html>')
html = ''.join(parts)
payload = {
    "subject": "每日热点简报 Daily Briefing - 2026-07-01",
    "htmlContent": html,
    "recipients": ["maymay_xia@163.com", "459729983@qq.com"]
}
with open("email_payload.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False)
print("items", n, "html_chars", len(html))
