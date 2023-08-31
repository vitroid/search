<script lang="ts">
    import VButton from "./vbutton.svelte";
    export let column
    export let available

    $: {

    }
</script>

<div class="container">
    {#each column as button, i}
    <VButton id={button.id} label={button.label} height={button.bin[2]} {available} on:search />
    {/each}
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: start;
    }
</style>
