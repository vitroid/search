<script>
    import { _ } from 'svelte-i18n';
    // import SessionTable from "./Components/SessionTable/sessiontable.svelte";
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import PosterTables2 from "./PosterTables2.svelte";
    import ShortCut from "./Components/shortcut.svelte";
    import {all_talks} from "./all_talks.js"

    const rooms_day3am = ["3Aa", "3Ab", "3Ac", "3Ad", "3B", "3C", "3D", "3E", "3Fa", "3Fb", "3Fc"]
    // let bins_am = ["9:00", "9:20", "9:40", "10:00", "10:20", "10:30", "10:50", "11:10", "11:30"]
    // let slots_am = ["1", "2", "3", "4", "", "5", "6", "7", "8"]

    const am_shortcuts = [
        ["3Aa", "^3Aa-", "工100", "1F"],
        ["3Ab", "^3Ab-", "工101", "1F"],
        ["3Ac", "^3Ac-", "工102", "1F"],
        ["3Ad", "^3Ad-", "工103", "1F"],
        ["3B",  "^3B-",  "工104", "1F"],
        ["3C",  "^3C-",  "工105", "1F"],
        ["3D",  "^3D-",  "工201", "2F"],
        ["3E",  "^3E-",  "工204", "2F"],
        ["3Fa", "^3Fa-", "全共102", "1F"],
        ["3Fb", "^3Fb-", "全共103", "1F"],
        ["3Fc", "^3Fc-", "工106", "1F"],
]

const pm_shortcuts = [
        ["3Aa", "^3Aa-", "工100", "1F"],
        ["3Ab", "^3Ab-", "工101", "1F"],
        ["3Ac", "^3Ac-", "工102", "1F"],
        ["3C",  "^3C-",  "工105", "1F"],
        ["3D",  "^3D-",  "工201", "2F"],
        ["3E",  "^3E-",  "工204", "2F"],
        ["3Fa", "^3Fa-", "全共102", "1F"],
        ["3Fb", "^3Fb-", "全共103", "1F"],
        ["3Fc", "^3Fc-", "工106", "1F"],
        ["3Fd", "^3Fd-", "工103", "1F"],
        ["Aw",  "^Aw-",  "Ibiden", "1F"],
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
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Aa-05", label:"05"},
            {bin:[,,20],   id: "3Aa-06", label:"06"},
            {bin:[,,20],   id: "3Aa-07", label:"07"},
        ],
        [
            {bin:[9,0,20], id: "3Ab-01", label:"01"},
            {bin:[,,20],   id: "3Ab-02", label:"02"},
            {bin:[,,20],   id: "3Ab-03", label:"03"},
            {bin:[,,20],   id: "3Ab-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Ab-05", label:"05"},
            {bin:[,,20],   id: "3Ab-06", label:"06"},
            // {bin:[,,20],   id: "2Ab-07", label:"07"},
            // {bin:[,,20],   id: "2Ab-08", label:"08"},
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
            // {bin:[,,20],   id: "2Ac-08", label:"08"},
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
            // {bin:[,,20],   id: "2Ac-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3B-02", label:"02"},
            {bin:[,,20],   id: "3B-03", label:"03"},
            {bin:[,,20],   id: "3B-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3B-05", label:"05"},
            {bin:[,,20],   id: "3B-06", label:"06"},
            {bin:[,,20],   id: "3B-07", label:"07"},
            // {bin:[,,20],   id: "2B-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3C-02", label:"02"},
            {bin:[,,20],   id: "3C-03", label:"03"},
            {bin:[,,20],   id: "3C-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3C-05", label:"05"},
            {bin:[,,20],   id: "3C-06", label:"06"},
            {bin:[,,20],   id: "3C-07", label:"07"},
            // {bin:[,,20],   id: "2C-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3D-02", label:"02"},
            {bin:[,,20],   id: "3D-03", label:"03"},
            {bin:[,,20],   id: "3D-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3D-05", label:"05"},
            {bin:[,,20],   id: "3D-06", label:"06"},
            {bin:[,,20],   id: "3D-07", label:"07"},
            // {bin:[,,20],   id: "2D-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3E-02", label:"02"},
            {bin:[,,20],   id: "3E-03", label:"03"},
            {bin:[,,20],   id: "3E-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3E-05", label:"05"},
            {bin:[,,20],   id: "3E-06", label:"06"},
            {bin:[,,20],   id: "3E-07", label:"07"},
            // {bin:[,,20],   id: "2E-08", label:"08"},
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
            // {bin:[,,20],   id: "2Fa-08", label:"08"},
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
            // {bin:[,,20],   id: "2Fb-08", label:"08"},
        ],
        [
            {bin:[9,0,20], id: "", label:""},
            {bin:[,,20],   id: "3Fc-02", label:"02"},
            {bin:[,,20],   id: "3Fc-03", label:"03"},
            {bin:[,,20],   id: "3Fc-04", label:"04"},
            {bin:[,,10],   id: "", label:""},
            {bin:[,,20],   id: "3Fc-05", label:"05"},
            {bin:[,,20],   id: "3Fc-06", label:"06"},
            {bin:[,,20],   id: "3Fc-07", label:"07"},
            // {bin:[,,20],   id: "2Fc-08", label:"08"},
        ],
    ]

    let rooms_day3pm = ["3Aa", "3Ab", "3Ac", "3Fd", "2C", "2D", "2E", "2Fa", "2Fb", "2Fc", "Aw"]

    let day3pm = [
        [
            {bin:[15,0,60],  id:"", label:"15:00"},
            {bin:[,,60],  id:"", label:"16:00"},
            {bin:[,,60],  id:"", label:"17:00"},
            {bin:[,,10],  id:"", label:"18:00"},
        ],
        [ // Aa 
            // {bin:[15,0,30], id:"Aw-07", label:$_("JSCC Research Encouragement Award")},
            // {bin:[,,10],    id:"", label:""},
            {bin:[15,40,20],    id:"3Aa-09", label:"09"},
            {bin:[,,20],    id:"3Aa-10", label:"10"},
            {bin:[,,20],    id:"3Aa-11", label:"11"},
            {bin:[,,20],    id:"3Aa-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Aa-13", label:"13"},
            {bin:[,,20],    id:"3Aa-14", label:"14"},
            {bin:[,,20],    id:"3Aa-15", label:"15"},
            // {bin:[,,20],  id:"2Aa-16", label:"16"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3Ab-09", label:"09"},
            {bin:[,,20],    id:"3Ab-10", label:"10"},
            {bin:[,,20],    id:"3Ab-11", label:"11"},
            {bin:[,,20],    id:"3Ab-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Ab-13", label:"13"},
            {bin:[,,20],    id:"3Ab-14", label:"14"},
            {bin:[,,20],    id:"3Ab-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3Ac-09", label:"09"},
            {bin:[,,20],    id:"3Ac-10", label:"10"},
            {bin:[,,20],    id:"3Ac-11", label:"11"},
            {bin:[,,20],    id:"3Ac-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Ac-13", label:"13"},
            {bin:[,,20],    id:"3Ac-14", label:"14"},
            {bin:[,,20],    id:"3Ac-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3C-09", label:"09"},
            {bin:[,,20],    id:"3C-10", label:"10"},
            {bin:[,,20],    id:"3C-11", label:"11"},
            {bin:[,,20],    id:"3C-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3C-13", label:"13"},
            {bin:[,,20],    id:"3C-14", label:"14"},
            {bin:[,,20],    id:"3C-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3D-09", label:"09"},
            {bin:[,,20],    id:"3D-10", label:"10"},
            {bin:[,,20],    id:"3D-11", label:"11"},
            {bin:[,,20],    id:"3D-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3D-13", label:"13"},
            {bin:[,,20],    id:"3D-14", label:"14"},
            {bin:[,,20],    id:"3D-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3E-09", label:"09"},
            {bin:[,,20],    id:"3E-10", label:"10"},
            {bin:[,,20],    id:"3E-11", label:"11"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,5,30], id:"Aw-08", label:$_("JSCC Research Encouragement Award")},
            {bin:[15,40,20],    id:"3Fa-09", label:"09"},
            {bin:[,,20],    id:"3Fa-10", label:"10"},
            {bin:[,,20],    id:"3Fa-11", label:"11"},
            {bin:[,,20],    id:"3Fa-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Fa-13", label:"13"},
            {bin:[,,20],    id:"3Fa-14", label:"14"},
            {bin:[,,20],    id:"3Fa-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3Fb-09", label:"09"},
            {bin:[,,20],    id:"3Fb-10", label:"10"},
            {bin:[,,20],    id:"3Fb-11", label:"11"},
            {bin:[,,20],    id:"3Fb-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Fb-13", label:"13"},
            {bin:[,,20],    id:"3Fb-14", label:"14"},
            // {bin:[,,20],    id:"3Fb-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"3Fc-09", label:"09"},
            {bin:[,,20],    id:"3Fc-10", label:"10"},
            {bin:[,,20],    id:"3Fc-11", label:"11"},
            {bin:[,,20],    id:"3Fc-12", label:"12"},
            {bin:[,,10],    id:"", label:""},
            {bin:[,,20],    id:"3Fc-13", label:"13"},
            {bin:[,,20],    id:"3Fc-14", label:"14"},
            {bin:[,,20],    id:"3Fc-15", label:"15"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,40,20],    id:"", label:""},
            {bin:[,,20],    id:"3Fd-10", label:"10"},
            {bin:[,,20],    id:"3Fd-11", label:"11"},
            {bin:[,,20],    id:"3Fd-12", label:"12"},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
        ],
        [
            // {bin:[15,4,40], id:"", label:""},
            {bin:[15,5,30], id:"Aw-07", label:$_("JSCC Research Encouragement Award")},
            // {bin:[,,20],    id:"2Ab-14", label:"14"},
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
    <h2>{$_("venue")} <a class="button" href="pdf/venue1.pdf">{$_("layout")}</a></h2>
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
                <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />{shortcut[2]}<br />{shortcut[3]}
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

</style>
