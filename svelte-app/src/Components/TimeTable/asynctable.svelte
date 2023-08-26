<script>
    import AsyncTableColumn from "./asynctablecolumn.svelte";
    // import AsyncTableHeader from "./asynctableheader.svelte";

    export let table
    // export let colnames
    export let title
    // a list of available (pushable, active) buttons.
    // ボタンを作るのは自由だが、availableに含まれていなければ押せない。
    export let available

</script>



<table>
    <tbody>
        <tr class='header'>
            <th colspan=99 class='corner'>
                {title}
            </th>
        </tr>
        <tr class='header'>
            <slot></slot>
        </tr>
        <tr class='top'>
            {#each table as column, i}
            <td class="column">
                <AsyncTableColumn {column} {available} on:search/>
            </td>
            {/each}
        </tr>
    </tbody>
</table>

<style>
    .top {
        vertical-align: top;
        background: repeating-linear-gradient(
  0deg,
  #ffffff,
  #ffffff 120px,
  #e0e0ff 120px,
  #e0e0ff 240px
);    }
    /* .container2 {
        display: flex;
        justify-content: start;
        flex-direction: column;
        margin: 5px;
    }
    h3 {
        text-align: center;
    }*/
    table {
        display: flex;
        justify-content: start;
        flex-direction: row;
        border: 0px;
        cellspacing: 0px;
    }
</style>
