<script lang="ts">
    import { _ } from 'svelte-i18n';

    let abstract_book =       $_("abstract_book_url")
    // let abstract_book_light = "https://www.dropbox.com/scl/fi/msur441jgze37f3hygkw2/AbstractBook0915_light.pdf?rlkey=bzcftf0mjydejhn5o0dk8u3bm&dl=0"
    let program_book =        $_("program_book_url")
    // let program_book_light =  "https://www.dropbox.com/scl/fi/1p8zlvdfgrdlwhv7pin9j/Program0915_light.pdf?rlkey=j3bdwtuy521oivkmu4nngfk3q&dl=0"
    // let seat = "http://www.chem.okayama-u.ac.jp/~reg/seat73/"

</script>

<div class="textbox">
    <h2>{$_("Announcements")}</h2>
    <ul>
        <li>
            9月14日(前日)に<a href="https://www.cms.nagasaki-u.ac.jp/sakuto75/events.html#event3">市民公開講座「サクタイってなに　―どこで役に立ってるの―」</a>があります。
        </li>
    </ul>
</div>

<!--    <h2>{$_("Program book")}</h2>
    <ul>
        <li>
            <a href={program_book}>{$_("Program book")} (Sep. 3, 20 MBytes)</a>
        </li>
    </ul>
    <h2>{$_("Abstract book")}</h2>
    <ul>
        <li>
            <a href={abstract_book}>{$_("Abstract book")} (Sep. 3, 241 MBytes)</a>
        </li>
    </ul>
</div> -->


<style>
    /* .textbox {
        display: block;
        flex-flow: row;
        flex-wrap: wrap;
        justify-content: left;
    } */
</style>
