# 如何创建第二款游戏

## 1. 复制模板

```bash
cp -r games/merge-blocks games/color-sort
```

## 2. 修改游戏标识

| 文件 | 改什么 |
|------|--------|
| `games/color-sort/package.json` | `"name": "@mini-games/color-sort"` |
| `games/color-sort/project.config.json` | `projectname`, `appid` |
| `games/color-sort/assets/scripts/config/GameAds.ts` | 新广告位 ID |
| `games/color-sort/README.md` | 游戏名、玩法说明 |
| `games/color-sort/docs/SOFT_COPYRIGHT.md` | 软著名称 |

## 3. 替换游戏逻辑

删除或重写 `assets/scripts/core/` 下的逻辑文件，保留目录结构：

```
assets/scripts/
├── core/           ← 你的新玩法逻辑
├── components/     ← 改 GameManager 适配新 UI
├── config/         ← 广告、游戏配置
```

`components/Bootstrap.ts` 通常只需改 `GameAds.ts` 的 import，不用动。

## 4. 公共模块（不用重写）

以下直接用 `packages/shared/`：

- `AdManager.ts` — 激励视频广告
- `StorageUtil.ts` — 本地存储

## 5. 注册与合规（每款独立做）

1. 注册新的微信小游戏账号 → 新 AppID
2. 申请新软著（名称与新游戏一致）
3. 小游戏备案 + 小程序备案
4. 资质审核（IAA / 情况二）

## 6. 添加测试

```bash
# 在新游戏目录下写 tests/
games/color-sort/tests/game.test.ts
```

在根 `package.json` 加 script：

```json
"test:color-sort": "npm test -w @mini-games/color-sort"
```

## 7. 时间预估

| 步骤 | 时间 |
|------|------|
| 复制 + 改名 | 30 分钟 |
| 新玩法逻辑 | 2～5 天 |
| UI + 广告 | 1～2 天 |
| 软著申请 | 2～3 个月等待 |
| 备案提审 | 1～2 周 |

## 命名规范

- 目录名：`kebab-case`（如 `color-sort`）
- npm 包名：`@mini-games/color-sort`
- 软著名：`颜色排序记V1.0`
- 微信小游戏名：`颜色排序记`
