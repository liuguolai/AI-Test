import { _decorator, Component, Node, Label, Color, UITransform, Graphics, EventTouch, tween, Vec3 } from 'cc';
import { GameState } from '../core/GameState';
import { GameConfig } from '../core/GameConfig';
import { AdManager } from './AdManager';

const { ccclass, property } = _decorator;

/**
 * Main game controller — attach to Canvas root node.
 * Wires UI buttons to game logic and refreshes the grid display.
 */
@ccclass('GameManager')
export class GameManager extends Component {
    @property(Node)
    gridContainer: Node | null = null;

    @property(Label)
    scoreLabel: Label | null = null;

    @property(Label)
    bestLabel: Label | null = null;

    @property(Label)
    statusLabel: Label | null = null;

    @property(Node)
    spawnButton: Node | null = null;

    @property(Node)
    gameOverPanel: Node | null = null;

    @property(Node)
    reviveButton: Node | null = null;

    @property(Node)
    restartButton: Node | null = null;

    private state = new GameState();
    private cellSize = 80;
    private cellGap = 6;
    private blockNodes: Node[][] = [];

    onLoad() {
        this.setupButtons();
        this.buildGrid();
        this.refreshUI();
    }

    private setupButtons() {
        this.spawnButton?.on(Node.EventType.TOUCH_END, this.onSpawn, this);
        this.reviveButton?.on(Node.EventType.TOUCH_END, this.onRevive, this);
        this.restartButton?.on(Node.EventType.TOUCH_END, this.onRestart, this);
    }

    private buildGrid() {
        if (!this.gridContainer) return;

        const size = GameConfig.GRID_SIZE;
        const total = this.cellSize + this.cellGap;
        const offset = -(size - 1) * total / 2;

        this.blockNodes = [];
        for (let r = 0; r < size; r++) {
            this.blockNodes[r] = [];
            for (let c = 0; c < size; c++) {
                const node = new Node(`cell_${r}_${c}`);
                node.parent = this.gridContainer;

                const transform = node.addComponent(UITransform);
                transform.setContentSize(this.cellSize, this.cellSize);

                node.setPosition(
                    offset + c * total,
                    offset + (size - 1 - r) * total,
                    0
                );

                node.addComponent(Graphics);
                this.blockNodes[r][c] = node;
            }
        }
    }

    private onSpawn() {
        const result = this.state.spawn();
        if (!result) return;

        this.refreshUI();

        if (result.spawn) {
            this.animateSpawn(result.spawn.row, result.spawn.col);
        }

        for (const merge of result.merges) {
            this.animateMerge(merge.toRow, merge.toCol);
        }
    }

    private onRevive() {
        AdManager.showRewardedVideo({
            onSuccess: () => {
                if (this.state.revive()) {
                    this.gameOverPanel && (this.gameOverPanel.active = false);
                    this.refreshUI();
                }
            },
            onFail: () => {
                if (this.statusLabel) {
                    this.statusLabel.string = '广告加载失败，请稍后再试';
                }
            },
        });
    }

    private onRestart() {
        this.state.restart();
        if (this.gameOverPanel) this.gameOverPanel.active = false;
        this.refreshUI();
    }

    private animateSpawn(row: number, col: number) {
        const node = this.blockNodes[row]?.[col];
        if (!node) return;
        node.setScale(0.3, 0.3, 1);
        tween(node).to(0.15, { scale: new Vec3(1, 1, 1) }).start();
    }

    private animateMerge(row: number, col: number) {
        const node = this.blockNodes[row]?.[col];
        if (!node) return;
        tween(node)
            .to(0.08, { scale: new Vec3(1.2, 1.2, 1) })
            .to(0.08, { scale: new Vec3(1, 1, 1) })
            .start();
    }

    private refreshUI() {
        const snap = this.state.snapshot();

        if (this.scoreLabel) this.scoreLabel.string = `分数: ${snap.score}`;
        if (this.bestLabel) this.bestLabel.string = `最高: ${snap.bestScore}`;

        const size = GameConfig.GRID_SIZE;
        for (let r = 0; r < size; r++) {
            for (let c = 0; c < size; c++) {
                this.drawCell(r, c, snap.grid[r][c]);
            }
        }

        if (snap.phase === 'gameover') {
            if (this.gameOverPanel) this.gameOverPanel.active = true;
            if (this.statusLabel) {
                const highest = GameConfig.LEVEL_NAMES[snap.grid.flat().reduce((a, b) => Math.max(a, b), 0)] || '';
                this.statusLabel.string = `游戏结束！最高合成: ${highest}`;
            }
            if (this.reviveButton) {
                this.reviveButton.active = snap.canRevive;
            }
        }
    }

    private drawCell(row: number, col: number, level: number) {
        const node = this.blockNodes[row]?.[col];
        if (!node) return;

        const g = node.getComponent(Graphics);
        if (!g) return;

        g.clear();
        const half = this.cellSize / 2;

        // Empty cell background
        g.fillColor = new Color(60, 60, 80, 255);
        g.roundRect(-half, -half, this.cellSize, this.cellSize, 8);
        g.fill();

        if (level <= 0) return;

        const colorHex = GameConfig.LEVEL_COLORS[Math.min(level - 1, GameConfig.LEVEL_COLORS.length - 1)];
        const color = Color.fromHEX(new Color(), colorHex);

        g.fillColor = color;
        g.roundRect(-half + 2, -half + 2, this.cellSize - 4, this.cellSize - 4, 6);
        g.fill();
    }
}
