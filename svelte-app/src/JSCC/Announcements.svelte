<script lang="ts">
    import { _ } from 'svelte-i18n';

    let program_book = "#" // "http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCProgramBook.pdf"
    let program_book_light = "#" // "http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCProgramBook_low.pdf"
    let abstract_book = "#" // "http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCAnnualSympoAbstract.pdf"
    let abstract_book_light = "#" // "http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCAnnualSympoAbstract_low.pdf"
    let seat = "#" // "http://www.chem.okayama-u.ac.jp/~reg/seat73/"

</script>

<div class="textbox">
    <h2>{$_("Program book")}</h2>
    <ul>
        <!-- これらのファイルは別の場所(/Users/matto/Unison/00Priority/2022錯討/AbstBook)からインストール。 -->
        <li>
            <a href={program_book}>{$_("Program book")} (32 MBytes)</a>
        </li>
        <li>
            <a href={program_book_light}>{$_("Program book")} {$_("(lightweight)")} (9 MBytes)</a>
        </li>
    </ul>
    <h2>{$_("Abstract book")}</h2>
    {$_("msg1")}
    <ul>
        <li>
            <a href={abstract_book}>{$_("Abstract book")} (206 MBytes)</a>
        </li>
        <li>
            <a href={abstract_book_light}>{$_("Abstract book")} {$_("(lightweight)")} (47 MBytes)</a>
        </li>
    </ul>
    <h2>{$_("Seat reservation for the banquet")}</h2>
    {$_("msg2")}
    <ul>
        <li>
            <a href={seat}>{$_("Seat reservation for the banquet")}</a>
        </li>
    </ul>
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
