<script>
    import { _ } from 'svelte-i18n';
    import Schedule from "./schedule.svelte";
    import SearchBox from "./Components/Search/searchbox.svelte";
	import {id, generateId} from "./Components/directory"
    import Banner from "./Banner.svelte"
    import { data } from "./index.js"

    // Set the current locale to en-US
    // locale.set('ja')
    // setupI18n({ withLocale: 'en' });

    let search = "";
    function searchHandler(event){
        search = event.detail.text;
    }

	$: {
		// 統計のためのunique id.
		if ($id == ""){
			$id = generateId();
		}
	}

</script>

<body>
	<div class="wrap">
        <Banner />
		<h2>{$_("SEARCH")}</h2>
		<div class="search">
			<!-- <ShortCuts on:search={searchHandler} /> -->
			<ul>
				<li>{$_("hint1")}</li>
				<li>{$_("hint2")}</li>
				<li>{$_("hint3")}</li>
				<li>{$_("hint4")}</li>
			</ul>

			<SearchBox {search} {data}/>
            <p>{$_("hint5")}</p>
		</div>
		<Schedule on:search={searchHandler} />
		<noscript>
			<p>{$_("usingjs")}</p>
		</noscript>

	</div>
</body>

<style>
	body{
		font-family: Helvetica, Ariel, sans-serif;
		font-size: 10pt;
	}
	div.wrap{
		max-width: 750px;
		background-color:#f0f0f0;
		margin: 0 auto;
	}
	h2 {
		padding: 10px;
        margin: 0;
		text-align: center;
		background-color: #fff;
	}
	div.search {
		margin: 10px;
	}
</style>
