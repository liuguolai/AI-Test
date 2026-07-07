export interface AdCallbacks {
    onSuccess: () => void;
    onFail: () => void;
}

let adUnitId = '';
let rewardedAd: WechatMinigame.RewardedVideoAd | null = null;

/** Call once at game launch with your ad unit ID */
export function configureAds(unitId: string): void {
    adUnitId = unitId;
    rewardedAd = null;
}

function getRewardedAd(): WechatMinigame.RewardedVideoAd | null {
    if (!adUnitId || typeof wx === 'undefined') return null;

    if (!rewardedAd) {
        rewardedAd = wx.createRewardedVideoAd({ adUnitId });
        rewardedAd.onError((err) => {
            console.warn('[AdManager] ad error:', err);
        });
    }

    return rewardedAd;
}

export const AdManager = {
    preload(): void {
        getRewardedAd()?.load().catch(() => {});
    },

    showRewardedVideo(callbacks: AdCallbacks): void {
        const ad = getRewardedAd();

        if (!ad) {
            console.log('[AdManager] no wx env, simulating ad success');
            callbacks.onSuccess();
            return;
        }

        const onClose = (res: { isEnded: boolean }) => {
            ad.offClose(onClose);
            res.isEnded ? callbacks.onSuccess() : callbacks.onFail();
        };

        ad.onClose(onClose);

        ad.show().catch(() => {
            ad.load()
                .then(() => ad.show())
                .catch(() => {
                    ad.offClose(onClose);
                    callbacks.onFail();
                });
        });
    },
};

declare const wx: WechatMinigame.Wx | undefined;
