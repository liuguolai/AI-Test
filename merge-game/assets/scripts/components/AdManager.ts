/**
 * WeChat rewarded video ad wrapper.
 * Replace AD_UNIT_ID with your real ad unit from WeChat MP backend.
 */

const AD_UNIT_ID = 'adunit-xxxxxxxxxxxxxxxx'; // TODO: replace after开通流量主

export interface AdCallbacks {
    onSuccess: () => void;
    onFail: () => void;
}

let rewardedAd: WechatMinigame.RewardedVideoAd | null = null;

function getRewardedAd(): WechatMinigame.RewardedVideoAd | null {
    if (typeof wx === 'undefined') return null;

    if (!rewardedAd) {
        rewardedAd = wx.createRewardedVideoAd({ adUnitId: AD_UNIT_ID });

        rewardedAd.onError((err) => {
            console.warn('[AdManager] ad error:', err);
        });
    }

    return rewardedAd;
}

export const AdManager = {
    /** Preload ad on game start */
    preload(): void {
        const ad = getRewardedAd();
        ad?.load().catch(() => {});
    },

    /** Show rewarded video — grants reward only if user watches fully */
    showRewardedVideo(callbacks: AdCallbacks): void {
        const ad = getRewardedAd();

        // Dev / browser fallback: grant reward directly
        if (!ad) {
            console.log('[AdManager] no wx env, simulating ad success');
            callbacks.onSuccess();
            return;
        }

        const onClose = (res: { isEnded: boolean }) => {
            ad.offClose(onClose);
            if (res.isEnded) {
                callbacks.onSuccess();
            } else {
                callbacks.onFail();
            }
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
