import { GridModel, TurnResult } from './GridModel';
import { StorageUtil } from '../../../../../packages/shared/src/StorageUtil';

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
        this.bestScore = StorageUtil.getNumber(STORAGE_KEY);
    }

    reset(): void {
        this.grid.reset();
        this.score = 0;
        this.turns = 0;
        this.phase = 'playing';
        this.canRevive = true;
    }

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

    private saveBestScore(): void {
        if (this.score > this.bestScore) {
            this.bestScore = this.score;
        }
        StorageUtil.setNumber(STORAGE_KEY, this.bestScore);
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
