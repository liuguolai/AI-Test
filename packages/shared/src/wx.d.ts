/** Minimal WeChat mini game type stubs for non-WeChat dev environments */
declare namespace WechatMinigame {
    interface Wx {
        createRewardedVideoAd(opts: { adUnitId: string }): RewardedVideoAd;
        getStorageSync(key: string): unknown;
        setStorageSync(key: string, value: unknown): void;
    }

    interface RewardedVideoAd {
        load(): Promise<void>;
        show(): Promise<void>;
        onClose(cb: (res: { isEnded: boolean }) => void): void;
        offClose(cb: (res: { isEnded: boolean }) => void): void;
        onError(cb: (err: unknown) => void): void;
    }
}
