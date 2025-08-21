<script>
    import { _ } from 'svelte-i18n';
    // import SessionTable from "./Components/SessionTable/sessiontable.svelte";
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import PosterTables from "./PosterTables.svelte";
    import ShortCut from "./Components/shortcut.svelte";
    import {all_talks} from "./all_talks.js"
    let sessions=["Time", "1Aa", "1Ab", "1Ac", "1Ad", "1B","1C", "1D", "1E", "1Fa", "1Fb", "1Fc","1Fd",]
    // let bins_am = ["9:00", "9:20", "9:40", "10:00", "10:20", "10:30", "10:50", "11:10", "11:30"]
    // let slots_am = ["1", "2", "3", "4", "", "5", "6", "7", "8"]

    const am_shortcuts = [
        ["1Aa", "^1Aa-", "工100", "1F"],
        ["1Ab", "^1Ab-", "工101", "1F"],
        ["1Ac", "^1Ac-", "工102", "1F"],
        ["1Ad", "^1Ad-", "工103", "1F"],
        ["1B", "^1B-", "工104", "1F"],
        ["1C", "^1C-", "工105", "1F"],
        ["1D", "^1D-", "工201", "2F"],
        ["1E", "^1E-", "工204", "2F"],
        ["1Fa", "^1Fa-", "全共102", "1F"],
        ["1Fb", "^1Fb-", "全共103", "1F"],
        ["1Fc", "^1Fc-", "工106", "1F"],
        ["1Fd", "^1Fd-", "工103", "1F"],
    ]

    const sy_shortcuts = [
        ["S1", "^S1-", "Ibiden", "1F"],
        ["S2", "^S2-", "全共102", "1F"],
        ["S3", "^S3-", "全共103", "1F"],
    ]

    const day1am = [
        [
            {bin:[9,0,60], id: "", label:"9:00"},
            {bin:[,,60],   id: "", label:"10:00"},
            {bin:[,,60],   id: "", label:"11:00"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1Aa-02", label:"02"},
            {bin:[,,20],   id: "1Aa-03", label:"03"},
            {bin:[,,20],   id: "1Aa-04", label:"04"},
            // {bin:[,,10],   id: "", label:""},
            {bin:[10,30,20],   id: "1Aa-05", label:"05"},
            {bin:[,,20],   id: "1Aa-06", label:"06"},
            {bin:[,,20],   id: "1Aa-07", label:"07"},
            {bin:[,,20],   id: "1Aa-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1Ab-02", label:"02"},
            {bin:[,,20],   id: "1Ab-03", label:"03"},
            {bin:[,,20],   id: "1Ab-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Ab-05", label:"05"},
            {bin:[,,20],   id: "1Ab-06", label:"06"},
            {bin:[,,20],   id: "1Ab-07", label:"07"},
            {bin:[,,20],   id: "1Ab-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1Ac-02", label:"02"},
            {bin:[,,20],   id: "1Ac-03", label:"03"},
            {bin:[,,20],   id: "1Ac-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Ac-05", label:"05"},
            {bin:[,,20],   id: "1Ac-06", label:"06"},
            {bin:[,,20],   id: "1Ac-07", label:"07"},
            // {bin:[,,20],   id: "1Ac-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "", label:""},
            {bin:[,,20],   id: "", label:""},
            {bin:[,,20],   id: "", label:""},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Ad-05", label:"05"},
            {bin:[,,20],   id: "1Ad-06", label:"06"},
            {bin:[,,20],   id: "1Ad-07", label:"07"},
            {bin:[,,20],   id: "1Ad-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1B-02", label:"02"},
            {bin:[,,20],   id: "1B-03", label:"03"},
            {bin:[,,20],   id: "1B-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1B-05", label:"05"},
            {bin:[,,20],   id: "1B-06", label:"06"},
            {bin:[,,20],   id: "1B-07", label:"07"},
            // {bin:[,,20],   id: "1C-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1C-02", label:"02"},
            {bin:[,,20],   id: "1C-03", label:"03"},
            {bin:[,,20],   id: "1C-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1C-05", label:"05"},
            {bin:[,,20],   id: "1C-06", label:"06"},
            {bin:[,,20],   id: "1C-07", label:"07"},
            {bin:[,,20],   id: "1C-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1D-02", label:"02"},
            {bin:[,,20],   id: "1D-03", label:"03"},
            {bin:[,,20],   id: "1D-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1D-05", label:"05"},
            {bin:[,,20],   id: "1D-06", label:"06"},
            {bin:[,,20],   id: "1D-07", label:"07"},
            // {bin:[,,20],   id: "", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "1E-02", label:"02"},
            {bin:[,,20],   id: "1E-03", label:"03"},
            {bin:[,,20],   id: "1E-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1E-05", label:"05"},
            {bin:[,,20],   id: "1E-06", label:"06"},
            {bin:[,,20],   id: "1E-07", label:"07"},
            // {bin:[,,20],   id: "1Fb-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Fa-01", label:"01"},
            {bin:[,,20],   id: "1Fa-02", label:"02"},
            {bin:[,,20],   id: "1Fa-03", label:"03"},
            {bin:[,,20],   id: "1Fa-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Fa-05", label:"05"},
            {bin:[,,20],   id: "1Fa-06", label:"06"},
            {bin:[,,20],   id: "1Fa-07", label:"07"},
            {bin:[,,20],   id: "1Fa-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Fb-01", label:"01"},
            {bin:[,,20],   id: "1Fb-02", label:"02"},
            {bin:[,,20],   id: "1Fb-03", label:"03"},
            {bin:[,,20],   id: "1Fb-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Fb-05", label:"05"},
            {bin:[,,20],   id: "1Fb-06", label:"06"},
            {bin:[,,20],   id: "1Fb-07", label:"07"},
            {bin:[,,20],   id: "1Fb-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Fc-01", label:"01"},
            {bin:[,,20],   id: "1Fc-02", label:"02"},
            {bin:[,,20],   id: "1Fc-03", label:"03"},
            {bin:[,,20],   id: "1Fc-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Fc-05", label:"05"},
            {bin:[,,20],   id: "1Fc-06", label:"06"},
            {bin:[,,20],   id: "1Fc-07", label:"07"},
            {bin:[,,20],   id: "1Fc-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Fd-01", label:"01"},
            {bin:[,,20],   id: "1Fd-02", label:"02"},
            {bin:[,,20],   id: "1Fd-03", label:"03"},
            {bin:[,,20],   id: "1Fd-04", label:"04"},
        ],
    ]



    let rooms_sy = ["Time", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]

    let symposia = [
        [
            {bin:[15,0,60], id:"", label:"15:00"},
            {bin:[,,60],    id:"", label:"16:00"},
            {bin:[,,60],    id:"", label:"17:00"},
            {bin:[,,60],    id:"", label:"18:00"},
        ],
        [
            {bin:[15,0,5],  id:"", label:""},
            {bin:[,,25],    id:"S1-01", label:"01"},
            {bin:[,,25],    id:"S1-02", label:"02"},
            {bin:[,,25],    id:"S1-03", label:"03"},
            {bin:[,,25],    id:"S1-04", label:"04"},
            {bin:[,,15],    id:"", label:""},
            {bin:[,,25],    id:"S1-05", label:"05"},
            {bin:[,,25],    id:"S1-06", label:"06"},
            {bin:[,,25],    id:"S1-07", label:"07"},
            {bin:[,,5],     id:"", label:""}
        ],
        [
            {bin:[15,0,5],  id:"", label:""},
            {bin:[,,25],    id:"S2-01", label:"01"},
            {bin:[,,25],    id:"S2-02", label:"02"},
            {bin:[,,25],    id:"S2-03", label:"03"},
            {bin:[,,25],    id:"S2-04", label:"04"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,25],    id:"S2-05", label:"05"},
            {bin:[,,25],    id:"S2-06", label:"06"},
            {bin:[,,5],     id:"", label:""}
        ],
        [
            {bin:[15,0,5],  id:"", label:""},
            {bin:[,,25],    id:"S3-01", label:"01"},
            {bin:[,,25],    id:"S3-02", label:"02"},
            {bin:[,,25],    id:"S3-03", label:"03"},
            {bin:[,,20],    id:"", label:""},
            {bin:[,,25],    id:"S3-04", label:"04"},
            {bin:[,,25],    id:"S3-05", label:"05"},
            {bin:[,,25],    id:"S3-06", label:"06"},
            {bin:[,,5],     id:"", label:""}
        ],

    ]

</script>

<div class="panel">
    <h1>
        {$_("Oral sessions")}
    </h1>
    <h2>{$_("venue")} <a class="button" href="pdf/venue1.pdf">{$_("layout")}</a></h2>
    <div class="container">
    <AsyncTable 
        title={$_("Morning sessions")}
        table={day1am}
        available={all_talks}
        startminute={9*60+0}
        on:search>
        <td>Time</td>
        {#each am_shortcuts as shortcut}
        <td>
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />{shortcut[2]}<br />{shortcut[3]}
        </td>
        {/each}
    </AsyncTable>
    <AsyncTable 
        table={symposia} 
        title={$_("Symposia")} 
        available={all_talks}
        startminute={15*60+0}
        on:search>
        <td>Time</td>
        {#each sy_shortcuts as shortcut}
        <td>
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />{shortcut[2]}<br />{shortcut[3]}
        </td>
        {/each}
    </AsyncTable>
    </div>
</div>
<div class="panel">
    <h1>
        {$_("Poster sessions")}
    </h1>
    <h2>{$_("venue")} <a class="button" href="pdf/venue1.pdf">{$_("layout")}</a></h2>
    <PosterTables 
        on:search/>
</div>

<style>
    td {
        text-align: center;
        margin: auto;
    }
    .panel {
        background-color: #fff;
        border: 4px solid #fff;
        border-radius: 15px;

        /* for children */
        display: flex;
        flex-flow: row;
        flex-wrap: wrap;
        margin: 5px;
        justify-content: center;
    }
    h1 {
        background-color: #4169E1c0;
        /* #5ab4bd; */
        width: 100%;
        padding: 10px;
        margin: 0px;
        font-size: 120%;
        border-radius: 15px 15px 0px 0px;
        color: white;
    }
    .container {
        display: flex;
        justify-content: start;
        flex-direction: row;
        flex-wrap: wrap;
        margin: 5px;
    }

    .button {
        border-radius: 5px 5px 5px;
        border: 1px solid #ccc;
        font-size: 90%;
        font-weight: bold;
        padding: 4px;
        color: black;
        background-color: white;
        text-decoration: none;
        margin-right: 3px;
        /* line-height: 150%; */
    }

</style>
