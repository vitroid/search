<script lang="ts">
    import { _ } from 'svelte-i18n';
</script>

<div class="textbox">
    <h2>{$_("Program book")}</h2>
    <ul>
        <!-- これらのファイルは別の場所(/Users/matto/Unison/00Priority/2022錯討/AbstBook)からインストール。 -->
        <li>
            <a href="http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCProgramBook.pdf">{$_("Program book")} (32 MBytes)</a>
        </li>
        <li>
            <a href="http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCProgramBook_low.pdf">{$_("Program book")} {$_("(lightweight)")} (9 MBytes)</a>
        </li>
    </ul>
    <h2>{$_("Abstract book")}</h2>
    <ul>
        {$_("msg1")}
        <ul>
            <li>
                <a href="http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCAnnualSympoAbstract.pdf">{$_("Abstract book")} (206 MBytes)</a>
            </li>
            <li>
                <a href="http://www.chem.okayama-u.ac.jp/~reg/jscc72/72JSCCAnnualSympoAbstract_low.pdf">{$_("Abstract book")} {$_("(lightweight)")} (47 MBytes)</a>
            </li>
        </ul>
    </ul>
    <h2>{$_("Seat reservation for the banquet")}</h2>
    <ul>
        <li>
            {$_("msg2")}
        </li>
        <li>
            <a href="http://www.chem.okayama-u.ac.jp/~reg/seat72/">http://www.chem.okayama-u.ac.jp/~reg/seat72/</a>
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
