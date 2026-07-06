# 合成方块记

6×6 格子合成类微信小游戏 starter 项目。点击「投放」生成方块，相邻相同等级自动合并升级，格子满则游戏结束，可看激励视频复活。

## 玩法

1. 点击 **投放** → 随机空位出现 1 级方块
2. 上下左右相邻的 **相同等级** 方块自动合并为高一级
3. 合并产生连锁反应，获得分数
4. 格子满 → 游戏结束
5. 看激励视频 → 清除 3 个最低级方块，继续游戏（每局 1 次）

## 等级表

| 等级 | 名称 | 颜色 |
|------|------|------|
| 1 | 碎块 | 蓝 |
| 2 | 石块 | 绿 |
| 3 | 铁块 | 橙 |
| ... | ... | ... |
| 10 | 皇冠 | 红 |

## 技术栈

- **引擎**: Cocos Creator 3.8+
- **语言**: TypeScript
- **平台**: 微信小游戏（IAA 广告变现）
- **架构**: 核心逻辑与 UI 分离，方便测试和迭代

## 项目结构

```
merge-game/
├── assets/scripts/
│   ├── core/           # 纯逻辑，无 UI 依赖
│   │   ├── GameConfig.ts
│   │   ├── GridModel.ts
│   │   └── GameState.ts
│   └── components/     # Cocos 组件
│       ├── GameManager.ts
│       ├── AdManager.ts
│       └── Bootstrap.ts
├── tests/
│   └── grid.test.ts    # 核心逻辑单元测试
├── docs/
│   ├── DEV_PLAN.md     # 7 天开发计划
│   └── SOFT_COPYRIGHT.md  # 软著操作说明模板
└── package.json
```

## 快速开始

### 1. 安装 Cocos Creator

下载 [Cocos Creator 3.8+](https://www.cocos.com/creator-download)，安装微信小游戏构建支持。

### 2. 导入项目

1. 打开 Cocos Creator → 新建空项目（2D）
2. 将 `assets/scripts/` 下的文件复制到项目的 `assets/scripts/`
3. 创建场景 `Game.scene`，按下方「场景搭建」配置节点

### 3. 场景搭建

```
Canvas
├── Background          (Sprite, 深色背景)
├── Header
│   ├── ScoreLabel      (Label → GameManager.scoreLabel)
│   └── BestLabel       (Label → GameManager.bestLabel)
├── GridContainer       (空节点 → GameManager.gridContainer)
├── SpawnButton         (Button "投放" → GameManager.spawnButton)
├── GameOverPanel       (默认隐藏 → GameManager.gameOverPanel)
│   ├── StatusLabel     (Label → GameManager.statusLabel)
│   ├── ReviveButton    (Button "看广告复活" → GameManager.reviveButton)
│   └── RestartButton   (Button "重新开始" → GameManager.restartButton)
└── GameManager         (挂载 GameManager 组件)
```

### 4. 构建微信小游戏

1. 菜单 → 项目 → 构建发布 → 微信小游戏
2. 填入你的 AppID
3. 构建后用微信开发者工具打开 `build/wechatgame/`

### 5. 接广告

1. 微信公众平台开通 **流量主**（需 1000 独立访问用户）
2. 创建 **激励视频广告位**，复制 adUnitId
3. 修改 `assets/scripts/components/AdManager.ts` 中的 `AD_UNIT_ID`

### 6. 跑测试

```bash
cd merge-game
npm install
npm test
```

## 上线 Checklist

- [ ] 注册微信小游戏账号（个人/企业）
- [ ] 申请软著（名称：合成方块记V1.0）
- [ ] 完成小游戏备案 + 小程序备案
- [ ] 选择 IAA 资质（不开通虚拟支付）
- [ ] 版本审核通过
- [ ] 开通流量主 → 配置广告位
- [ ] 发布

## 软著与命名

- **软著名称**: 合成方块记V1.0
- **小游戏名称**: 合成方块记
- 详见 `docs/SOFT_COPYRIGHT.md`

## 后续迭代方向

- [ ] 方块上显示等级数字/名称
- [ ] 合并音效和粒子特效
- [ ] 分享得复活次数
- [ ] 每日挑战模式
- [ ] 排行榜（需开放数据域）
