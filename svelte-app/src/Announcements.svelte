<script lang="ts">
    import { _ } from 'svelte-i18n';

    let abstract_book =       "pdf/abstract74_240903.pdf"
    let abstract_book_light = "https://www.dropbox.com/scl/fi/msur441jgze37f3hygkw2/AbstractBook0915_light.pdf?rlkey=bzcftf0mjydejhn5o0dk8u3bm&dl=0"
    let program_book =        "pdf/program74_240903.pdf"
    let program_book_light =  "https://www.dropbox.com/scl/fi/1p8zlvdfgrdlwhv7pin9j/Program0915_light.pdf?rlkey=j3bdwtuy521oivkmu4nngfk3q&dl=0"
    // let seat = "http://www.chem.okayama-u.ac.jp/~reg/seat73/"

</script>

<div class="textbox">
    <h2>{$_("Program book")}</h2>
    <ul>
        <li>
            <a href={program_book}>{$_("Program book")} (Sep. 3, 20 MBytes)</a>
        </li>
        <!-- <li>
            <a href={program_book_light}>{$_("Program book")} {$_("(lightweight)")} (Sep. 15, 8 MBytes)</a>
        </li> -->
    </ul>
    <h2>{$_("Abstract book")}</h2>
    <!-- {$_("msg1")} -->
    <ul>
        <li>
            <a href={abstract_book}>{$_("Abstract book")} (Sep. 3, 241 MBytes)</a>
        </li>
        <!-- <li>
            <a href={abstract_book_light}>{$_("Abstract book")} {$_("(lightweight)")} (Sep. 15, 376 MBytes)</a>
        </li> -->
    </ul>


    <!-- <h2>{$_("Seat reservation for the banquet")}</h2>
    {$_("msg2")}
    <ul>
        <li>
            <a href={seat}>{$_("Seat reservation for the banquet")}</a>
        </li>
    </ul> -->
</div>


<style>
    .textbox {
        padding: 10px;

        /* for children */
        display: block;
        flex-flow: row;
        flex-wrap: wrap;
        justify-content: left;
    }
</style>
