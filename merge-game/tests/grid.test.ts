/**
 * Standalone test runner for core game logic.
 * Run: npx tsx tests/grid.test.ts
 */
import { GridModel } from '../assets/scripts/core/GridModel';
import { GameState } from '../assets/scripts/core/GameState';

let passed = 0;
let failed = 0;

function assert(condition: boolean, msg: string) {
    if (condition) {
        passed++;
        console.log(`  ✓ ${msg}`);
    } else {
        failed++;
        console.error(`  ✗ ${msg}`);
    }
}

console.log('=== GridModel tests ===');

const grid = new GridModel(4);
grid.loadLevels([
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]);

const pair = grid.findMergePair();
assert(pair !== null, 'finds adjacent same-level pair');
assert(pair!.r1 === 0 && pair!.c1 === 0, 'pair starts at (0,0)');

const merges = grid.resolveAllMerges();
assert(merges.length === 1, 'one merge happens');
assert(grid.getLevel(0, 0) === 2, 'merged cell becomes level 2');
assert(grid.getLevel(0, 1) === 0, 'source cell cleared');

console.log('\n=== GameState tests ===');

const game = new GameState();
let turns = 0;
let gameOver = false;

while (!gameOver && turns < 200) {
    const result = game.spawn();
    if (!result) break;
    gameOver = result.gameOver;
    turns++;
}

assert(turns > 0, 'game runs at least one turn');
assert(game.score >= 0, 'score is non-negative');
console.log(`  ℹ game ended after ${turns} turns, score=${game.score}`);

console.log(`\n=== Results: ${passed} passed, ${failed} failed ===`);
process.exit(failed > 0 ? 1 : 0);
