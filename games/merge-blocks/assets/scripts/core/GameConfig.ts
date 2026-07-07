/** Game balance and layout constants for 合成方块记 */
export const GameConfig = {
    /** Grid dimensions */
    GRID_SIZE: 6,

    /** Block level range: 1..MAX_LEVEL */
    MAX_LEVEL: 10,

    /** Starting level when spawning */
    SPAWN_LEVEL: 1,

    /** Score per merge: level * SCORE_PER_LEVEL */
    SCORE_PER_LEVEL: 10,

    /** Ad revive: how many lowest blocks to remove */
    AD_CLEAR_COUNT: 3,

    /** Block colors by level (hex) */
    LEVEL_COLORS: [
        '#4A90D9', // 1
        '#50C878', // 2
        '#F5A623', // 3
        '#E94B3C', // 4
        '#9B59B6', // 5
        '#1ABC9C', // 6
        '#E67E22', // 7
        '#3498DB', // 8
        '#2ECC71', // 9
        '#E74C3C', // 10
    ] as const,

    /** Display names for levels */
    LEVEL_NAMES: [
        '', '碎块', '石块', '铁块', '铜块',
        '银块', '金块', '水晶', '宝石', '钻石', '皇冠',
    ] as const,
};
