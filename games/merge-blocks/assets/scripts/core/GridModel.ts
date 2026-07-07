import { GameConfig } from './GameConfig';

export interface Cell {
    level: number; // 0 = empty
}

export interface MergeStep {
    fromRow: number;
    fromCol: number;
    toRow: number;
    toCol: number;
    newLevel: number;
    scoreGained: number;
}

export interface SpawnResult {
    row: number;
    col: number;
    level: number;
}

export interface TurnResult {
    spawn: SpawnResult | null;
    merges: MergeStep[];
    totalScore: number;
    gameOver: boolean;
}

/** Pure grid logic — no UI dependencies, easy to unit test */
export class GridModel {
    readonly size: number;
    private cells: Cell[][];

    constructor(size = GameConfig.GRID_SIZE) {
        this.size = size;
        this.cells = this.createEmptyGrid();
    }

    private createEmptyGrid(): Cell[][] {
        return Array.from({ length: this.size }, () =>
            Array.from({ length: this.size }, () => ({ level: 0 }))
        );
    }

    reset(): void {
        this.cells = this.createEmptyGrid();
    }

    getCell(row: number, col: number): Cell {
        return this.cells[row][col];
    }

    getLevel(row: number, col: number): number {
        return this.cells[row][col].level;
    }

    /** Deep copy for snapshots */
    cloneLevels(): number[][] {
        return this.cells.map(row => row.map(c => c.level));
    }

    loadLevels(levels: number[][]): void {
        for (let r = 0; r < this.size; r++) {
            for (let c = 0; c < this.size; c++) {
                this.cells[r][c].level = levels[r]?.[c] ?? 0;
            }
        }
    }

    getEmptyCells(): Array<{ row: number; col: number }> {
        const empty: Array<{ row: number; col: number }> = [];
        for (let r = 0; r < this.size; r++) {
            for (let c = 0; c < this.size; c++) {
                if (this.cells[r][c].level === 0) {
                    empty.push({ row: r, col: c });
                }
            }
        }
        return empty;
    }

    isFull(): boolean {
        return this.getEmptyCells().length === 0;
    }

    /** Spawn a block on a random empty cell */
    spawnRandom(level = GameConfig.SPAWN_LEVEL): SpawnResult | null {
        const empty = this.getEmptyCells();
        if (empty.length === 0) return null;

        const pick = empty[Math.floor(Math.random() * empty.length)];
        this.cells[pick.row][pick.col].level = level;
        return { row: pick.row, col: pick.col, level };
    }

    /** Find first mergeable adjacent pair (top-to-bottom, left-to-right) */
    findMergePair(): { r1: number; c1: number; r2: number; c2: number } | null {
        const dirs = [
            [0, 1],  // right
            [1, 0],  // down
        ];

        for (let r = 0; r < this.size; r++) {
            for (let c = 0; c < this.size; c++) {
                const level = this.cells[r][c].level;
                if (level === 0 || level >= GameConfig.MAX_LEVEL) continue;

                for (const [dr, dc] of dirs) {
                    const nr = r + dr;
                    const nc = c + dc;
                    if (nr >= this.size || nc >= this.size) continue;
                    if (this.cells[nr][nc].level === level) {
                        return { r1: r, c1: c, r2: nr, c2: nc };
                    }
                }
            }
        }
        return null;
    }

    /** Execute one merge between two adjacent same-level cells */
    executeMerge(r1: number, c1: number, r2: number, c2: number): MergeStep {
        const level = this.cells[r1][c1].level;
        const newLevel = Math.min(level + 1, GameConfig.MAX_LEVEL);

        // Keep upper-left cell, clear the other
        this.cells[r1][c1].level = newLevel;
        this.cells[r2][c2].level = 0;

        return {
            fromRow: r2,
            fromCol: c2,
            toRow: r1,
            toCol: c1,
            newLevel,
            scoreGained: newLevel * GameConfig.SCORE_PER_LEVEL,
        };
    }

    /** Resolve all chain merges after a spawn */
    resolveAllMerges(): MergeStep[] {
        const steps: MergeStep[] = [];
        let pair = this.findMergePair();
        while (pair) {
            const step = this.executeMerge(pair.r1, pair.c1, pair.r2, pair.c2);
            steps.push(step);
            pair = this.findMergePair();
        }
        return steps;
    }

    /** Full turn: spawn → merge chain → check game over */
    playTurn(): TurnResult {
        const spawn = this.spawnRandom();
        if (!spawn) {
            return { spawn: null, merges: [], totalScore: 0, gameOver: true };
        }

        const merges = this.resolveAllMerges();
        const totalScore = merges.reduce((sum, m) => sum + m.scoreGained, 0);
        const gameOver = this.isFull();

        return { spawn, merges, totalScore, gameOver };
    }

    /** Ad revive: remove N lowest-level blocks */
    clearLowestBlocks(count = GameConfig.AD_CLEAR_COUNT): Array<{ row: number; col: number }> {
        const blocks: Array<{ row: number; col: number; level: number }> = [];
        for (let r = 0; r < this.size; r++) {
            for (let c = 0; c < this.size; c++) {
                if (this.cells[r][c].level > 0) {
                    blocks.push({ row: r, col: c, level: this.cells[r][c].level });
                }
            }
        }

        blocks.sort((a, b) => a.level - b.level);
        const cleared: Array<{ row: number; col: number }> = [];

        for (let i = 0; i < Math.min(count, blocks.length); i++) {
            const { row, col } = blocks[i];
            this.cells[row][col].level = 0;
            cleared.push({ row, col });
        }

        return cleared;
    }

    getHighestLevel(): number {
        let max = 0;
        for (let r = 0; r < this.size; r++) {
            for (let c = 0; c < this.size; c++) {
                max = Math.max(max, this.cells[r][c].level);
            }
        }
        return max;
    }
}
