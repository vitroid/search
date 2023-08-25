<script>
    import { _ } from 'svelte-i18n';
    import LocaleSelector from './Components/localeselector.svelte';

    let conf_url = "https://sites.google.com/g.ibaraki.ac.jp/sakuto73"

</script>



<div class="banner">
    <div>
        <a href={conf_url} target="_blank" >
            {$_("JSCCAS")}
        </a>
    </div>
    <div class="right">
        <LocaleSelector />
    </div>
</div>


<style>
	a {
		padding: 0px 5;
        font-size: 150%;
        color: white;
        text-decoration: none;
    }
    a:link, a:visited {
        color: white;
    }
    a:hover {
        opacity: 75%;
        transition-duration: 500ms;
    }
    .banner {
        background-color: #4169E1;
        display: flex;
        justify-content: space-between;
        padding: 10px;
    }
</style>