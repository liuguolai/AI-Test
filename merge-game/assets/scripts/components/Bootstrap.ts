import { _decorator, Component } from 'cc';
import { AdManager } from './AdManager';

const { ccclass } = _decorator;

/** Attach to a persistent node to preload ads on launch */
@ccclass('Bootstrap')
export class Bootstrap extends Component {
    onLoad() {
        AdManager.preload();
    }
}
