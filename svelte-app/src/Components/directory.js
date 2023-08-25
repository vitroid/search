export let directory = {};

// directory辞書は、タブ内のボタンへの参照を保持している。これを操作することで、遠隔で状態を変えられる。
// 操作の方法はcheckbox.svelteを見よ

// シグナル伝達方式もsearchで使っている。本当はこういう直接結合は避けて、シグナル伝達に統一すべきだと思う。

// browser内メモリー
import { localStorageStore } from "@babichjacob/svelte-localstorage/browser";
export const marks = localStorageStore("marks", new Set());
