<script>
    import { _ } from 'svelte-i18n';
    import Schedule from "./schedule.svelte";
    import SearchBox from "./Components/Search/searchbox.svelte";
	import {id, generateId} from "./Components/directory"
    import Banner from "./Banner.svelte"
    import { data } from "./index.js"
    import VotingInfoModal from "./Components/VotingInfoModal.svelte"

    // Set the current locale to en-US
    // locale.set('ja')
    // setupI18n({ withLocale: 'en' });

    let search = "";
    let showVotingModal = false;
    
    function searchHandler(event){
        search = event.detail.text;
    }
    
    function openVotingModal() {
        showVotingModal = true;
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

			<div class="voting-info-section">
				<button class="voting-info-btn" on:click={openVotingModal}>
					{$_("Statistics feature")}
				</button>
			</div>

			<SearchBox {search} {data}/>
            <p>{$_("hint5")}</p>
		</div>
		<Schedule on:search={searchHandler} />
		<noscript>
			<p>{$_("usingjs")}</p>
		</noscript>

	</div>
</body>

<!-- 投票機能説明モーダル -->
<VotingInfoModal bind:show={showVotingModal} />

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
	
	.voting-info-section {
		text-align: center;
		margin: 1rem 0;
		padding: 0.5rem;
		background: linear-gradient(135deg, #f8f9fa, #e9ecef);
		border-radius: 8px;
		border: 1px solid #dee2e6;
	}
	
	.voting-info-btn {
		background: linear-gradient(135deg, #007bff, #0056b3);
		color: white;
		border: none;
		padding: 0.75rem 1.5rem;
		border-radius: 25px;
		font-size: 0.9rem;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.3s ease;
		box-shadow: 0 3px 10px rgba(0, 123, 255, 0.3);
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
	}
	
	.voting-info-btn:hover {
		background: linear-gradient(135deg, #0056b3, #004085);
		transform: translateY(-2px);
		box-shadow: 0 5px 15px rgba(0, 123, 255, 0.4);
	}
	
	.voting-info-btn:active {
		transform: translateY(0);
		box-shadow: 0 2px 8px rgba(0, 123, 255, 0.3);
	}
	
	/* モバイル対応 */
	@media (max-width: 768px) {
		.voting-info-btn {
			padding: 0.6rem 1.2rem;
			font-size: 0.8rem;
		}
	}
</style>
