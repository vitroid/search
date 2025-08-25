<script>
    import { _ } from 'svelte-i18n';
    export let label;
</script>

{#if label === "C"}
<a class="buttonC" href={$_("bdgC_url")}>{label}</a>
{:else if label === "G"}
<a class="buttonG" href={$_("bdgG_url")}>{label}</a>
{:else if label === "S"}
<a class="buttonS" href={$_("bdgS_url")}>{label}</a>
{:else if label === "A"}
<a class="buttonA" href={$_("bdgA_url")}>{label}</a>
{:else if label === "H"}
<a class="buttonH" href={$_("hall_url")}>{label}</a>
{/if}

<style>
    .buttonA {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(0, 100%, 80%);
        text-decoration: none;
        margin-right: 3px;

    }
    .buttonG {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(320, 100%, 80%);
        text-decoration: none;
        margin-right: 3px;
    }
    .buttonC {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(280, 100%, 80%);
        text-decoration: none;
        margin-right: 3px;
        /* line-height: 150%; */
    }
    .buttonH {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(200, 100%, 80%);
    }
    .buttonS {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(120, 100%, 40%);
    }
</style>