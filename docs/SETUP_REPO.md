# 推送到新仓库

Cloud Agent 无法直接在 GitHub 上创建新仓库，请按以下步骤操作（约 2 分钟）。

## 第一步：在 GitHub 创建空仓库

1. 打开 https://github.com/new
2. 仓库名填：**`wechat-mini-games`**
3. 选 **Public** 或 Private
4. **不要**勾选 "Add a README"（保持空仓库）
5. 点 Create repository

## 第二步：推送代码

在本机或 Cloud 终端执行：

```bash
# 克隆当前已重构的代码（若你还没有）
git clone https://github.com/liuguolai/AI-Test.git
cd AI-Test
git checkout cursor/monorepo-wechat-mini-games-6011

# 添加新仓库远程地址
git remote add mini-games https://github.com/liuguolai/wechat-mini-games.git

# 推送到新仓库 main 分支
git push mini-games cursor/monorepo-wechat-mini-games-6011:main
```

## 第三步（可选）：切换默认远程

若以后只维护新仓库：

```bash
git remote rename origin ai-test-old
git remote rename mini-games origin
git branch -M main
git push -u origin main
```

## 新仓库地址

推送成功后访问：

**https://github.com/liuguolai/wechat-mini-games**

## 验证

```bash
git clone https://github.com/liuguolai/wechat-mini-games.git
cd wechat-mini-games
npm install
npm test
```

应看到 7 个测试全部通过。
