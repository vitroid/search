<script lang="ts">
    import { _ } from 'svelte-i18n';
    import LocationButton from './locationbutton.svelte';

    let abstract_book = $_("abstract_book_url");
    let program_book = $_("program_book_url");

</script>

<div class="textbox">
    <h2>{$_("Announcements")}</h2>
    <ul>
        <li>
            9月14日(前日)に<a href="https://www.cms.nagasaki-u.ac.jp/sakuto75/events.html#event3">市民公開講座「サクタイってなに　―どこで役に立ってるの―」</a>があります。(会場: 中部講堂<LocationButton label="H" />)
        </li>
    </ul>

    <h2>{$_("Program book")}</h2>
    <ul>
        <li>
            <a href={program_book} target="_blank" rel="noopener noreferrer">
                {$_("Program book")} (Sep. 4, 33 MBytes)
            </a>
        </li>
    </ul>
    <h2>{$_("Abstract book")}</h2>
    <ul>
        <li>
            <a href={abstract_book} target="_blank" rel="noopener noreferrer">
                {$_("Abstract book")} (Sep. 4, 330 MBytes)
            </a>
        </li>
    </ul>
</div>

<style>
    /* .textbox {
        display: block;
        flex-flow: row;
        flex-wrap: wrap;
        justify-content: left;
    } */
</style>
