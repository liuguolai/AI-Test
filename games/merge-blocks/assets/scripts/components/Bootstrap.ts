import { _decorator, Component } from 'cc';
import { configureAds, AdManager } from '../../../../../packages/shared/src/AdManager';
import { MERGE_BLOCKS_AD_UNIT_ID } from '../config/GameAds';

const { ccclass } = _decorator;

@ccclass('Bootstrap')
export class Bootstrap extends Component {
    onLoad() {
        configureAds(MERGE_BLOCKS_AD_UNIT_ID);
        AdManager.preload();
    }
}
