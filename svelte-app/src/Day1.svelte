<script>
    import { _ } from 'svelte-i18n';
    // import SessionTable from "./Components/SessionTable/sessiontable.svelte";
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import PosterTables from "./PosterTables.svelte";
    import ShortCut from "./Components/shortcut.svelte";
    import LocationButton from "./locationbutton.svelte";
    import {all_talks} from "./all_talks.js"
    let sessions=["Time", "1Aa", "1Ab", "1Ac", "1Ad", "1B","1C", "1Da", "1Db", "1Fa", "1Fb", "1Fc","1Fd",]
    // let bins_am = ["9:00", "9:20", "9:40", "10:00", "10:20", "10:30", "10:50", "11:10", "11:30"]
    // let slots_am = ["1", "2", "3", "4", "", "5", "6", "7", "8"]

    // btnCはbdgC_urlへのリンクの丸型ボタン。背景色はHSB(240,1,0.8)、文字"C"は白抜き太字で。
    const am_shortcuts = [
        ["1Aa", "^1Aa-", "141", "1F", "C"],
        ["1Ab", "^1Ab-", "C-16", "1F", "C"],
        ["1Ac", "^1Ac-", "A-12", "1F", "A"],
        ["1Ad", "^1Ad-", "A-13", "1F", "A"],
        ["1B", "^1B-", "A-32", "3F", "A"],
        ["1C", "^1C-", "A-33", "3F", "A"],
        ["1Da", "^1Da-", "A-41", "4F", "A"],
        ["1Db", "^1Db-", "A-43", "4F", "A"],
        ["1Fa", "^1Fa-", "A-21", "2F", "A"],
        ["1Fb", "^1Fb-", "A-22", "2F", "A"],
        ["1Fc", "^1Fc-", "A-24", "2F", "A"],
        ["1Fd", "^1Fd-", "A-31", "3F", "A"],
    ]


    const day1am = [
        [
            {bin:[9,0,60], id: "", label:"9:00"},
            {bin:[,,60],   id: "", label:"10:00"},
            {bin:[,,60],   id: "", label:"11:00"},
        ],
        [
            {bin:[9,0,20], id: "1Aa-01", label:"01"},
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
            {bin:[9,0,20], id: "1Ab-01", label:"01"},
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
            {bin:[9,0,20], id: "1Ac-01", label:"01"},
            {bin:[,,20],   id: "1Ac-02", label:"02"},
            {bin:[,,20],   id: "1Ac-03", label:"03"},
            {bin:[,,20],   id: "1Ac-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Ac-05", label:"05"},
            {bin:[,,20],   id: "1Ac-06", label:"06"},
            {bin:[,,20],   id: "1Ac-07", label:"07"},
            {bin:[,,20],   id: "1Ac-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Ad-01", label:"01"},
            {bin:[,,20],   id: "1Ad-02", label:"02"},
            {bin:[,,20],   id: "1Ad-03", label:"03"},
            {bin:[,,20],   id: "1Ad-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Ad-05", label:"05"},
            {bin:[,,20],   id: "1Ad-06", label:"06"},
            {bin:[,,20],   id: "1Ad-07", label:"07"},
            {bin:[,,20],   id: "1Ad-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1B-01", label:"01"},
            {bin:[,,20],   id: "1B-02", label:"02"},
            {bin:[,,20],   id: "1B-03", label:"03"},
            {bin:[,,20],   id: "1B-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1B-05", label:"05"},
            {bin:[,,20],   id: "1B-06", label:"06"},
            {bin:[,,20],   id: "1B-07", label:"07"},
            {bin:[,,20],   id: "1B-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1C-01", label:"01"},
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
            {bin:[9,0,20], id: "1Da-01", label:"01"},
            {bin:[,,20],   id: "1Da-02", label:"02"},
            {bin:[,,20],   id: "1Da-03", label:"03"},
            {bin:[,,20],   id: "1Da-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Da-05", label:"05"},
            {bin:[,,20],   id: "1Da-06", label:"06"},
            {bin:[,,20],   id: "1Da-07", label:"07"},
            {bin:[,,20],   id: "1Da-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "1Db-01", label:"01"},
            {bin:[,,20],   id: "1Db-02", label:"02"},
            {bin:[,,20],   id: "1Db-03", label:"03"},
            {bin:[,,20],   id: "1Db-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Db-05", label:"05"},
            {bin:[,,20],   id: "1Db-06", label:"06"},
            {bin:[,,20],   id: "1Db-07", label:"07"},
            {bin:[,,20],   id: "1Db-08", label:"08"},
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
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "1Fd-05", label:"05"},
            {bin:[,,20],   id: "1Fd-06", label:"06"},
            {bin:[,,20],   id: "1Fd-07", label:"07"},
            {bin:[,,20],   id: "1Fd-08", label:"08"},
        ],
    ]


    const noon_shortcuts = [
        ["LS", "^1LS", "G-38", "3F", "G"],
    ]


    const day1noon = [
        [
            {bin:[12,0,60], id: "", label:"12:00"},
        ],
        [
            {bin:[12,0,50], id: "1LS", label:"LS"},
        ],
    ]

    const pm_shortcuts = [
        ["1Aa", "^1Aa-", "141", "1F", "C"],
        ["1Ab", "^1Ab-", "C-16", "1F", "C"],
        ["1Ac", "^1Ac-", "A-12", "1F", "A"],
        ["1Ad", "^1Ad-", "A-13", "1F", "A"],
        ["1B", "^1B-", "A-32", "3F", "A"],
        ["1C", "^1C-", "A-33", "3F", "A"],
        ["1Da", "^1Da-", "A-41", "4F", "A"],
        ["1E", "^1E-", "A-43", "4F", "A"],
        ["1Fa", "^1Fa-", "A-21", "2F", "A"],
        ["1Fb", "^1Fb-", "A-22", "2F", "A"],
        ["1Fc", "^1Fc-", "A-24", "2F", "A"],
        ["1Fd", "^1Fd-", "A-31", "3F", "A"],
    ]

    const day1pm = [
        [
            {bin:[15,0,60], id: "", label:"15:00"},
            {bin:[,,60],   id: "", label:"16:00"},
        ],
        [
            {bin:[15,10,20], id: "1Aa-09", label:"09"},
            {bin:[,,20],   id: "1Aa-10", label:"10"},
            {bin:[,,20],   id: "1Aa-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Ab-09", label:"09"},
            {bin:[,,20],   id: "1Ab-10", label:"10"},
            {bin:[,,20],   id: "1Ab-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Ac-09", label:"09"},
            {bin:[,,20],   id: "1Ac-10", label:"10"},
            {bin:[,,20],   id: "1Ac-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Ad-09", label:"09"},
            {bin:[,,20],   id: "1Ad-10", label:"10"},
            {bin:[,,20],   id: "1Ad-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1B-09", label:"09"},
            {bin:[,,20],   id: "1B-10", label:"10"},
            {bin:[,,20],   id: "1B-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1C-09", label:"09"},
            {bin:[,,20],   id: "1C-10", label:"10"},
            {bin:[,,20],   id: "1C-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Da-09", label:"09"},
            {bin:[,,20],   id: "1Da-10", label:"10"},
            {bin:[,,20],   id: "1Da-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1E-09", label:"09"},
            {bin:[,,20],   id: "1E-10", label:"10"},
            {bin:[,,20],   id: "1E-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Fa-09", label:"09"},
            {bin:[,,20],   id: "1Fa-10", label:"10"},
            {bin:[,,20],   id: "1Fa-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Fb-09", label:"09"},
            {bin:[,,20],   id: "1Fb-10", label:"10"},
            {bin:[,,20],   id: "1Fb-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Fc-09", label:"09"},
            {bin:[,,20],   id: "1Fc-10", label:"10"},
            {bin:[,,20],   id: "1Fc-11", label:"11"},
        ],
        [
            {bin:[15,10,20], id: "1Fd-09", label:"09"},
            {bin:[,,20],   id: "1Fd-10", label:"10"},
            {bin:[,,20],   id: "1Fd-11", label:"11"},
        ],
    ]

    const sy_shortcuts = [
        ["S1", "^S1-", "A-21", "2F", "A"],
        ["S2", "^S2-", "C-16", "1F", "C"],
        ["S3", "^S3-", "141", "1F", "C"],
        ["S4", "^S4-", "A-12", "1F", "A"],
        ["S5", "^S5-", "A-13", "1F", "A"],
        ["S6", "^S6-", "A-32", "3F", "A"],
    ]

    const symposia = [
        [
            {bin:[16,0,60], id:"", label:"16:00"},
            {bin:[,,60],    id:"", label:"17:00"},
            {bin:[,,60],    id:"", label:"18:00"},
            {bin:[,,60],    id:"", label:"19:00"},
        ],
        [
            {bin:[16,20,5],  id:"", label:"OR"},
            {bin:[,,25],    id:"S1-01", label:"01"},
            {bin:[,,25],    id:"S1-02", label:"02"},
            {bin:[,,25],    id:"S1-03", label:"03"},
            {bin:[,,25],    id:"S1-04", label:"04"},
            {bin:[,,25],    id:"S1-05", label:"05"},
            {bin:[,,25],    id:"S1-06", label:"06"},
            {bin:[,,25],    id:"S1-07", label:"07"},
            {bin:[,,5],     id:"", label:"CR"}
        ],
        [
            {bin:[16,20,5],  id:"", label:"OR"},
            {bin:[,,25],    id:"S2-01", label:"01"},
            {bin:[,,25],    id:"S2-02", label:"02"},
            {bin:[,,25],    id:"S2-03", label:"03"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,25],    id:"S2-04", label:"04"},
            {bin:[,,25],    id:"S2-05", label:"05"},
            {bin:[,,25],    id:"S2-06", label:"06"},
            {bin:[,,25],    id:"S2-07", label:"07"},
            {bin:[,,5],     id:"", label:"CR"}
        ],
        [
            {bin:[16,20,5],  id:"", label:"OR"},
            {bin:[,,15],    id:"S3-01", label:"01"},
            {bin:[,,25],    id:"S3-02", label:"02"},
            {bin:[,,25],    id:"S3-03", label:"03"},
            {bin:[,,25],    id:"S3-04", label:"04"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,25],    id:"S3-05", label:"05"},
            {bin:[,,25],    id:"S3-06", label:"06"},
            {bin:[,,25],    id:"S3-07", label:"07"},
        ],
        [
            {bin:[16,20,5],  id:"", label:"OR"},
            {bin:[,,30],    id:"S4-01", label:"01"},
            {bin:[,,30],    id:"S4-02", label:"02"},
            {bin:[,,30],    id:"S4-03", label:"03"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,30],    id:"S4-04", label:"04"},
            {bin:[,,30],    id:"S4-05", label:"05"},
            {bin:[,,5],    id:"", label:"CR"},
        ],
        [
            {bin:[16,30,5],  id:"", label:"OR"},
            {bin:[,,20],    id:"S5", label:"01"},
            {bin:[,,20],    id:"S5", label:"02"},
            {bin:[,,20],    id:"S5", label:"03"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"S5", label:"04"},
            {bin:[,,20],    id:"S5", label:"05"},
            {bin:[,,20],    id:"S5", label:"06"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,30],    id:"S5", label:"PD"},
            {bin:[,,5],    id:"", label:"CR"},
        ],
        [
            {bin:[16,20,5],  id:"", label:"OR"},
            {bin:[,,40],    id:"S6-01", label:"01"},
            {bin:[,,40],    id:"S6-02", label:"02"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,40],    id:"S6-03", label:"03"},
            {bin:[,,40],    id:"S6-04", label:"04"},
            {bin:[,,5],    id:"", label:"CR"},
        ],

    ]

</script>

<div class="panel">
    <h1>
        {$_("Oral sessions")}
    </h1>
    <h2>{$_("venue")}<br /><a class="button" href={$_("venue_url")}>{$_("Map")}</a><a class="button" href={$_("oralvenue_url")}>{$_("Layout")}</a></h2>
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
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />
            {shortcut[2]}<br />
            <LocationButton label={shortcut[4]} />{shortcut[3]}
        </td>
        {/each}
    </AsyncTable>
    <AsyncTable 
        title={$_("Luncheon Seminar")}
        table={day1noon}
        available={all_talks}
        startminute={12*60+0}
        on:search>
        <td>Time</td>
        {#each noon_shortcuts as shortcut}
        <td>
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />
            {shortcut[2]}<br />
            <LocationButton label={shortcut[4]} />{shortcut[3]}
        </td>
        {/each}
    </AsyncTable>
    <AsyncTable 
        title={$_("Afternoon sessions")}
        table={day1pm}
        available={all_talks}
        startminute={15*60+0}
        on:search>
        <td>Time</td>
        {#each pm_shortcuts as shortcut}
        <td>
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />
            {shortcut[2]}<br />
            <LocationButton label={shortcut[4]} />{shortcut[3]}
        </td>
        {/each}
    </AsyncTable>
    <div class="vbox">
        <div>
        <AsyncTable 
            table={symposia} 
            title={$_("Symposia")} 
            available={all_talks}
            startminute={16*60+0}
            on:search>
            <td>Time</td>
            {#each sy_shortcuts as shortcut}
            <td>
                <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />
                {shortcut[2]}<br />
                <LocationButton label={shortcut[4]} />{shortcut[3]}
            </td>
            {/each}
        </AsyncTable>
        </div>
        <div>PD: {$_("Panel discussion")}</div>
        <div>OR & CR: {$_("Opening and closing remarks")}</div>
    </div>
    </div>
</div>
<div class="panel">
    <h1>
        {$_("Poster sessions")}
    </h1>
    <div class="hbox">
        <h2>{$_("venue")}<br /><a class="button" href={$_("venue_url")}>{$_("Map")}</a><a class="button" href={$_("postervenue_url")}>{$_("Layout")}</a></h2>
        <p><LocationButton label="P" />2F, 3F</p>
</div>
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
    .vbox { /* only for vbox in container */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .hbox { /* only for vbox in container */
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }
</style>
