import { GridModel, TurnResult } from './GridModel';

export type GamePhase = 'playing' | 'gameover' | 'reviving';

export interface GameSnapshot {
    score: number;
    bestScore: number;
    turns: number;
    phase: GamePhase;
    grid: number[][];
    canRevive: boolean;
}

const STORAGE_KEY = 'merge_blocks_best_score';

/** Manages score, persistence, and game flow */
export class GameState {
    readonly grid: GridModel;
    score = 0;
    bestScore = 0;
    turns = 0;
    phase: GamePhase = 'playing';
    canRevive = true;

    constructor() {
        this.grid = new GridModel();
        this.bestScore = this.loadBestScore();
    }

    private loadBestScore(): number {
        try {
            if (typeof wx !== 'undefined' && wx.getStorageSync) {
                return wx.getStorageSync(STORAGE_KEY) || 0;
            }
            if (typeof localStorage !== 'undefined') {
                return parseInt(localStorage.getItem(STORAGE_KEY) || '0', 10);
            }
        } catch { /* ignore */ }
        return 0;
    }

    saveBestScore(): void {
        if (this.score <= this.bestScore) return;
        this.bestScore = this.score;
        try {
            if (typeof wx !== 'undefined' && wx.setStorageSync) {
                wx.setStorageSync(STORAGE_KEY, this.bestScore);
            } else if (typeof localStorage !== 'undefined') {
                localStorage.setItem(STORAGE_KEY, String(this.bestScore));
            }
        } catch { /* ignore */ }
    }

    reset(): void {
        this.grid.reset();
        this.score = 0;
        this.turns = 0;
        this.phase = 'playing';
        this.canRevive = true;
    }

    /** Player taps "投放" button */
    spawn(): TurnResult | null {
        if (this.phase !== 'playing') return null;

        const result = this.grid.playTurn();
        this.turns++;

        if (result.spawn) {
            this.score += result.totalScore;
            if (this.score > this.bestScore) {
                this.bestScore = this.score;
            }
        }

        if (result.gameOver) {
            this.phase = 'gameover';
            this.saveBestScore();
        }

        return result;
    }

    /** After watching rewarded video ad */
    revive(): boolean {
        if (this.phase !== 'gameover' || !this.canRevive) return false;

        this.grid.clearLowestBlocks();
        this.phase = 'playing';
        this.canRevive = false;
        return true;
    }

    restart(): void {
        this.reset();
    }

    snapshot(): GameSnapshot {
        return {
            score: this.score,
            bestScore: this.bestScore,
            turns: this.turns,
            phase: this.phase,
            grid: this.grid.cloneLevels(),
            canRevive: this.canRevive,
        };
    }
}

/** WeChat global type stub for non-WeChat environments */
declare const wx: {
    getStorageSync(key: string): number;
    setStorageSync(key: string, value: number): void;
} | undefined;
