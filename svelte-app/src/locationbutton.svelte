<script>
    import { _ } from 'svelte-i18n';
    import { bdgA_url, bdgC_url, bdgG_url, bdgP_url, hall_url } from './common.js';
    export let label;
</script>

{#if label === "C"}
<a class="buttonC" href={bdgC_url}>{label}</a>
{:else if label === "G"}
<a class="buttonG" href={bdgG_url}>{label}</a>
{:else if label === "P"}
<a class="buttonP" href={bdgP_url}>{label}</a>
{:else if label === "A"}
<a class="buttonA" href={bdgA_url}>{label}</a>
{:else if label === "H"}
<a class="buttonH" href={hall_url}>{label}</a>
{/if}

<style>
    .buttonA {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(0, 100%, 50%);
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
        background-color: hsl(320, 100%, 50%);
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
        background-color: hsl(30, 100%, 50%);
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
        background-color: hsl(200, 100%, 50%);
    }  
    .buttonP {
        border-radius: 5px 5px 5px;
        border: none;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: white;
        background-color: hsl(120, 100%, 40%);
    }
</style>