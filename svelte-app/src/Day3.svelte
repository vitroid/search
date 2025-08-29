<script>
    import { _ } from 'svelte-i18n';
    // import SessionTable from "./Components/SessionTable/sessiontable.svelte";
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import PosterTables2 from "./PosterTables2.svelte";
    import ShortCut from "./Components/shortcut.svelte";
    import {all_talks} from "./all_talks.js"
    import LocationButton from "./locationbutton.svelte";

    const am_shortcuts = [
        ["3Aa", "^3Aa-", "141", "1F", "C"],
        ["3Ab", "^3Ab-", "C-16", "1F", "C"],
        ["3Ac", "^3Ac-", "A-12", "1F", "A"],
        ["3Ad", "^3Ad-", "A-13", "1F", "A"],
        ["3B",  "^3B-",  "A-32", "3F", "A"],
        ["3C",  "^3C-",  "A-33", "3F", "A"],
        ["3Da",  "^3Da-",  "A-41", "4F", "A"],
        ["3E",  "^3E-",  "A-43", "4F", "A"],
        ["3Fa", "^3Fa-", "A-21", "2F", "A"],
        ["3Fb", "^3Fb-", "A-22", "2F", "A"],
        ["3Fc", "^3Fc-", "A-24", "2F", "A"],
        ["3Fc", "^3Fc-", "A-31", "3F", "A"],
]

const pm_shortcuts = [
        ["3B", "^3B-", "A-32", "3F", "A"],
        ["3C",  "^3C-",  "A-33", "3F", "A"],
        ["3Fa",  "^3Fa-",  "A-21", "2F", "A"],
        ["3Fb",  "^3Fb-",  "A-22", "2F", "A"],
        ["3Fc", "^3Fc-", "A-24", "2F", "A"],
        ["3Fd", "^3Fd-", "A-31", "3F", "A"],
]

const day3am = [
        [
            {bin:[9,0,60], id: "", label:"9:00"},
            {bin:[,,60],   id: "", label:"10:00"},
            {bin:[,,60],   id: "", label:"11:00"},
        ],
        [
            {bin:[9,0,20], id: "3Aa-01", label:"01"},
            {bin:[,,20],   id: "3Aa-02", label:"02"},
            {bin:[,,20],   id: "3Aa-03", label:"03"},
            {bin:[,,20],   id: "3Aa-04", label:"04"},
            // {bin:[,,10],   id: "", label:""},
            {bin:[10,30,20],   id: "3Aa-05", label:"05"},
            {bin:[,,20],   id: "3Aa-06", label:"06"},
            {bin:[,,20],   id: "3Aa-07", label:"07"},
            {bin:[,,20],   id: "3Aa-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Ab-01", label:"01"},
            {bin:[,,20],   id: "3Ab-02", label:"02"},
            {bin:[,,20],   id: "3Ab-03", label:"03"},
            {bin:[,,20],   id: "3Ab-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Ab-05", label:"05"},
            {bin:[,,20],   id: "3Ab-06", label:"06"},
            {bin:[,,20],   id: "3Ab-07", label:"07"},
            {bin:[,,20],   id: "3Ab-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Ac-01", label:"01"},
            {bin:[,,20],   id: "3Ac-02", label:"02"},
            {bin:[,,20],   id: "3Ac-03", label:"03"},
            {bin:[,,20],   id: "3Ac-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Ac-05", label:"05"},
            {bin:[,,20],   id: "3Ac-06", label:"06"},
            {bin:[,,20],   id: "3Ac-07", label:"07"},
            {bin:[,,20],   id: "3Ac-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3Ad-02", label:"02"},
            {bin:[,,20],   id: "3Ad-03", label:"03"},
            {bin:[,,20],   id: "3Ad-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Ad-05", label:"05"},
            {bin:[,,20],   id: "3Ad-06", label:"06"},
            {bin:[,,20],   id: "3Ad-07", label:"07"},
            {bin:[,,20],   id: "3Ad-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3B-01", label:"01"},
            {bin:[,,20],   id: "3B-02", label:"02"},
            {bin:[,,20],   id: "3B-03", label:"03"},
            {bin:[,,20],   id: "3B-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3B-05", label:"05"},
            {bin:[,,20],   id: "3B-06", label:"06"},
            {bin:[,,20],   id: "3B-07", label:"07"},
            {bin:[,,20],   id: "3B-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "", label:""},
            {bin:[,,20],   id: "3C-03", label:"03"},
            {bin:[,,20],   id: "3C-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3C-05", label:"05"},
            {bin:[,,20],   id: "3C-06", label:"06"},
            {bin:[,,20],   id: "3C-07", label:"07"},
            {bin:[,,20],   id: "3C-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Da-01", label:"01"},
            {bin:[,,20],   id: "3Da-02", label:"02"},
            {bin:[,,20],   id: "3Da-03", label:"03"},
            {bin:[,,20],   id: "3Da-04", label:"04"},
        ],
        [
            {bin:[9,0,20], id: "3E-01", label:"01"},
            {bin:[,,20],   id: "3E-02", label:"02"},
            {bin:[,,20],   id: "3E-03", label:"03"},
            {bin:[,,20],   id: "3E-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3E-05", label:"05"},
            {bin:[,,20],   id: "3E-06", label:"06"},
            {bin:[,,20],   id: "3E-07", label:"07"},
            {bin:[,,20],   id: "3E-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Fa-01", label:"01"},
            {bin:[,,20],   id: "3Fa-02", label:"02"},
            {bin:[,,20],   id: "3Fa-03", label:"03"},
            {bin:[,,20],   id: "3Fa-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Fa-05", label:"05"},
            {bin:[,,20],   id: "3Fa-06", label:"06"},
            {bin:[,,20],   id: "3Fa-07", label:"07"},
            {bin:[,,20],   id: "3Fa-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Fb-01", label:"01"},
            {bin:[,,20],   id: "3Fb-02", label:"02"},
            {bin:[,,20],   id: "3Fb-03", label:"03"},
            {bin:[,,20],   id: "3Fb-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Fb-05", label:"05"},
            {bin:[,,20],   id: "3Fb-06", label:"06"},
            {bin:[,,20],   id: "3Fb-07", label:"07"},
            {bin:[,,20],   id: "3Fb-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "3Fc-01", label:"01"},
            {bin:[,,20],   id: "3Fc-02", label:"02"},
            {bin:[,,20],   id: "3Fc-03", label:"03"},
            {bin:[,,20],   id: "3Fc-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Fc-05", label:"05"},
            {bin:[,,20],   id: "3Fc-06", label:"06"},
            {bin:[,,20],   id: "3Fc-07", label:"07"},
            {bin:[,,20],   id: "3Fc-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3Fd-02", label:"02"},
            {bin:[,,20],   id: "3Fd-03", label:"03"},
            {bin:[,,20],   id: "3Fd-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Fd-05", label:"05"},
            {bin:[,,20],   id: "3Fd-06", label:"06"},
            {bin:[,,20],   id: "3Fd-07", label:"07"},
            {bin:[,,20],   id: "3Fd-08", label:"08"},
        ],
    ]






    const day3pm = [
        [
            {bin:[15,0,60], id: "", label:"15:00"},
            {bin:[,,60],   id: "", label:"16:00"},
            {bin:[,,60],   id: "", label:"17:00"},
        ],
        [
            {bin:[15,0,20], id: "3B-09", label:"09"},
            {bin:[,,20],   id: "3B-10", label:"10"},
            {bin:[,,20],   id: "3B-11", label:"11"},
        ],
        [
            {bin:[15,0,20], id: "3C-09", label:"09"},
            {bin:[,,20],   id: "3C-10", label:"10"},
            {bin:[,,20],   id: "3C-11", label:"11"},
        ],
        [
            {bin:[15,0,20], id: "3Fa-09", label:"09"},
            {bin:[,,20],   id: "3Fa-10", label:"10"},
            {bin:[,,20],   id: "3Fa-11", label:"11"},
        ],
        [
            {bin:[15,0,20], id: "3Fb-09", label:"09"},
            {bin:[,,20],   id: "3Fb-10", label:"10"},
            {bin:[,,20],   id: "3Fb-11", label:"11"},
        ],
        [
            {bin:[15,0,20], id: "3Fc-09", label:"09"},
            {bin:[,,20],   id: "3Fc-10", label:"10"},
            {bin:[,,20],   id: "3Fc-11", label:"11"},
        ],
        [
            {bin:[15,0,20], id: "3Fd-09", label:"09"},
            {bin:[,,20],   id: "3Fd-10", label:"10"},
            {bin:[,,20],   id: "3Fd-11", label:"11"},
        ],
    ]

    // {#each rooms_day3am as room}
    //         <td>
    //             <ShortCut label={room} query={shortcuts[room]} on:search />
    //         </td>
    //         {/each}
    // {#each rooms_day3pm as room}
    //         <td>
    //             <ShortCut label={room} query={shortcuts[room]} on:search />
    //         </td>
    //         {/each}

</script>

<div class="panel">
    <h1>
        {$_("Oral sessions")}
    </h1>
    <h2>{$_("venue")} <a class="button" href={$_("venue_url")}>{$_("Map")}</a></h2>
    <div class="container">
        <AsyncTable 
            table={day3am} 
            title={$_("Morning sessions")}
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
            table={day3pm} 
            title={$_("Afternoon sessions")} 
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
    </div>
</div>

<div class="panel">
    <h1>
        {$_("Poster sessions")}
    </h1>
    <div class="hbox">
    <h2>{$_("venue")} <a class="button" href={$_("postervenue_url")}>{$_("Layout")}</a></h2>
    <p><LocationButton label="P" />2F, 3F</p>
    </div>
    <PosterTables2 
        on:search />
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
    .hbox {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

</style>
