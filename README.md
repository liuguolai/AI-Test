# WeChat Mini Games

微信小游戏 Monorepo — 多款 IAA 休闲游戏，公共代码复用，快速铺量试错。

## 仓库结构

```
wechat-mini-games/
├── packages/
│   └── shared/              # 公共模块：广告、存储、微信 SDK 封装
│       └── src/
│           ├── AdManager.ts
│           ├── StorageUtil.ts
│           └── index.ts
├── games/
│   └── merge-blocks/        # 第一款：合成方块记
│       ├── assets/scripts/
│       ├── docs/
│       └── tests/
└── docs/
    ├── PUBLISH_CHECKLIST.md # 通用上线清单
    └── NEW_GAME.md           # 新游戏创建指南
```

## 游戏列表

| 游戏 | 目录 | 状态 | 变现 |
|------|------|------|------|
| 合成方块记 | `games/merge-blocks` | 开发中 | IAA |

## 快速开始

```bash
git clone https://github.com/liuguolai/mini-games.git
cd mini-games
npm install
npm test
```

## 开发第二款游戏

```bash
cp -r games/merge-blocks games/your-game-name
# 然后按 docs/NEW_GAME.md 修改
```

## 技术栈

- Cocos Creator 3.8+
- TypeScript
- 微信小游戏 IAA（激励视频广告）

## 公共模块用法

```typescript
import { configureAds, AdManager } from '../../../../../packages/shared/src/AdManager';
import { StorageUtil } from '../../../../../packages/shared/src/StorageUtil';

configureAds('adunit-xxxx');
AdManager.showRewardedVideo({ onSuccess: () => {}, onFail: () => {} });
StorageUtil.setNumber('key', 100);
```

## 许可证

Private — 副业项目
