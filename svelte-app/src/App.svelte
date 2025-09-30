<script>
    import { _, locale } from 'svelte-i18n';
    import Schedule from "./schedule.svelte";
    import SearchBox from "./Components/Search/searchbox.svelte";
	import {id, generateId} from "./Components/directory"
    import Banner from "./Banner.svelte"
    import { data } from "./index.js"
    import VotingInfoModal from "./VotingInfoModal.svelte"
    import PullToRefresh from "./Components/PullToRefresh.svelte"

    // Set the current locale to en-US
    // locale.set('ja')
    // setupI18n({ withLocale: 'en' });

    let search = "";
    let showVotingModal = false;
    let pullToRefreshComponent;
    
    function searchHandler(event){
        search = event.detail.text;
    }
    
    function openVotingModal() {
        showVotingModal = true;
    }

    function handleRefresh() {
        console.log('🔄 Pull-to-refresh triggered!');
        // ページをリロード
        setTimeout(() => {
            window.location.reload();
        }, 500);
    }

	$: {
		// 統計のためのunique id.
		if ($id == ""){
			$id = generateId();
		}
	}

</script>

<PullToRefresh bind:this={pullToRefreshComponent} on:refresh={handleRefresh}>
	<body>
		<div class="wrap">
			<Banner />
			<h2>{$_("SEARCH")}</h2>
			<div class="search">
				<!-- <ShortCuts on:search={searchHandler} /> -->
				{#if $locale === 'ja'}
					<ul>
						<li>発表番号、題目、研究場所、発表者名にて検索が可能です。</li>
						<li>正規表現が使えます。</li>
						<li>画像クリックでPDFが開きます。</li>
						<li>表示は申込データに基づいており、表示のタイトルおよび著者の一部が要旨とは異なる場合があります。</li>
					</ul>
				{:else if $locale === 'cn'}
					<ul>
						<li>你可以通过演讲编号，标题，关键词，研究地点和演讲者姓名进行搜索。</li>
						<li>可以使用正则表达式。</li>
						<li>点击图片，打开PDF。</li>
						<li>该显示基于应用数据，显示的一些标题和作者可能与摘要不同。</li>
					</ul>
				{:else}
					<ul>
						<li>You can search by presentation number, title, keywords, research location, or presenter name.</li>
						<li>Regular expressions can be used.</li>
						<li>Click on the image to open the PDF file.</li>
						<li>The data shown is based on the application data, and some of the titles and authors shown may be different from the abstract.</li>
					</ul>
				{/if}

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
</PullToRefresh>

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
