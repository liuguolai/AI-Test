# 合成方块记

6×6 格子合成类微信小游戏。点击「投放」生成方块，相邻相同等级自动合并升级。

> 本目录是 monorepo 中的第一款游戏。公共代码（广告、存储）在 `packages/shared/`。

## 玩法

1. 点击 **投放** → 随机空位出现 1 级方块
2. 相邻相同等级自动合并升级，可连锁
3. 格子满 → 游戏结束
4. 看激励视频 → 清除 3 个最低级方块（每局 1 次）

## 目录

```
games/merge-blocks/
├── assets/scripts/
│   ├── core/           # 游戏逻辑
│   ├── components/     # Cocos 组件
│   └── config/         # 广告位 ID 等配置
├── docs/               # 开发计划、软著说明
└── tests/              # 单元测试
```

## Cocos 场景搭建

```
Canvas
├── GridContainer       → GameManager.gridContainer
├── ScoreLabel          → GameManager.scoreLabel
├── BestLabel           → GameManager.bestLabel
├── SpawnButton         → GameManager.spawnButton
├── GameOverPanel       → GameManager.gameOverPanel
│   ├── StatusLabel
│   ├── ReviveButton
│   └── RestartButton
├── Bootstrap           → 挂载 Bootstrap 组件（初始化广告）
└── GameManager         → 挂载 GameManager 组件
```

## 构建

1. Cocos Creator 新建 2D 项目
2. 将整个 `wechat-mini-games` 仓库克隆到本地
3. 把 `games/merge-blocks/assets/` 和 `packages/shared/` 都放进 Cocos 项目的 `assets/` 下（保持相对路径），或在 Cocos 项目中用文件夹引用
4. **推荐**：在 Cocos 项目中创建软链接或直接把仓库作为项目根目录的子集

### 推荐 Cocos 项目布局

```
MyCocosProject/
└── assets/
    ├── packages/shared/     ← 从 monorepo 复制或软链
    └── games/merge-blocks/  ← 从 monorepo 复制或软链
```

## 配置广告

编辑 `assets/scripts/config/GameAds.ts`，填入微信流量主广告位 ID。

## 测试

```bash
# 在仓库根目录
npm test
```

## 上线

详见 `docs/DEV_PLAN.md` 和仓库根目录 `docs/PUBLISH_CHECKLIST.md`。
