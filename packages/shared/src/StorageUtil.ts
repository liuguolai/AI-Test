/** Cross-platform storage: WeChat mini game or browser localStorage */
export const StorageUtil = {
    getNumber(key: string, defaultValue = 0): number {
        try {
            if (typeof wx !== 'undefined' && wx.getStorageSync) {
                const val = wx.getStorageSync(key);
                return typeof val === 'number' ? val : defaultValue;
            }
            if (typeof localStorage !== 'undefined') {
                return parseInt(localStorage.getItem(key) || String(defaultValue), 10);
            }
        } catch { /* ignore */ }
        return defaultValue;
    },

    setNumber(key: string, value: number): void {
        try {
            if (typeof wx !== 'undefined' && wx.setStorageSync) {
                wx.setStorageSync(key, value);
            } else if (typeof localStorage !== 'undefined') {
                localStorage.setItem(key, String(value));
            }
        } catch { /* ignore */ }
    },
};

declare const wx: {
    getStorageSync(key: string): unknown;
    setStorageSync(key: string, value: unknown): void;
} | undefined;
