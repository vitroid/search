export let directory = {};

// directory辞書は、タブ内のボタンへの参照を保持している。これを操作することで、遠隔で状態を変えられる。
// 操作の方法はcheckbox.svelteを見よ

// シグナル伝達方式もsearchで使っている。本当はこういう直接結合は避けて、シグナル伝達に統一すべきだと思う。


// https://stackoverflow.com/questions/1349404/generate-random-string-characters-in-javascript

// dec2hex :: Integer -> String
// i.e. 0-255 -> '00'-'ff'
function dec2hex (dec) {
    return dec.toString(16).padStart(2, "0")
}
  
  // generateId :: Integer -> String
export function generateId (len) {
    var arr = new Uint8Array((len || 40) / 2)
    window.crypto.getRandomValues(arr)
    return Array.from(arr, dec2hex).join('')
}

// browser内メモリー
import { localStorageStore } from "@babichjacob/svelte-localstorage/browser";
// 青い印をつけた講演の表
export const marks = localStorageStore("marks", new Set());
// identity
export let id = localStorageStore("id", "");
