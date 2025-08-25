<script>
    import { _ } from 'svelte-i18n';
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import ShortCut from "./Components/shortcut.svelte";
    import {all_talks} from "./all_talks.js"
    import LocationButton from "./locationbutton.svelte";


    const day2_shortcuts = [
        ["Aw", "^Aw-", "中部講堂", "", "H"],
        ["2HC", "^2HC", "A-12", "1F", "A"],
        ["2HC", "^2HC", "A-13", "1F", "A"],
        ["2HC", "^2HC", "A-22", "2F", "A"],
        ["2HC", "^2HC", "A-24", "2F", "A"],
    ]
    
    let day2 = [
        [
            {bin:[9,0,60],   id:"", label:"9:00"},
            {bin:[10,0,60],  id:"", label:"10:00"},
            {bin:[11,0,60],  id:"", label:"11:00"},
            {bin:[12,0,60],  id:"", label:"12:00"},
            {bin:[13,0,60],  id:"", label:"13:00"},
            {bin:[14,0,60],  id:"", label:"14:00"},
            {bin:[15,0,60],  id:"", label:"15:00"},
            {bin:[16,0,60],  id:"", label:"16:00"},
            {bin:[17,0,60],  id:"", label:"17:00"},
        ],   
        [
            {bin:[9,0,60],   id:"Aw-01", label:$_("JSCC International Award")},
            {bin:[10,5,30],  id:"Aw-02", label:$_("JSCC International Award for Creative Work")},
            {bin:[10,40,30], id:"Aw-03", label:$_("JSCC Award for Creative Work")},
            {bin:[11,15,30], id:"Aw-04", label:$_("JSCC Award for Creative Work")},
            {bin:[13,45,60], id:"Aw-05", label:$_("JSCC Award")},
            {bin:[14,50,60], id:"Aw-06", label:$_("JSCC Contribution Award")},
            {bin:[16,0,90], id:"", label:$_("JSCC General Meeting")},
        ],
        [
            {bin:[16,0,90], id:"2HC", label:$_("Homecoming Day")},
        ],
        [
            {bin:[16,0,90], id:"2HC", label:$_("Homecoming Day")},
        ],
        [
            {bin:[16,0,90], id:"2HC", label:$_("Homecoming Day")},
        ],
        [
            {bin:[16,0,90], id:"2HC", label:$_("Homecoming Day")},
        ]
    ]

    let banquet = [
        [
            {bin:[18,0,60],  id:"", label:"18:00"},
            {bin:[19,0,60],  id:"", label:"19:00"},
            {bin:[20,0,60],  id:"", label:"20:00"},
        ],   
        [
            {bin:[18,30,120],   id:"", label:$_("Banquet")},
        ],
    ]

</script>

<div class="panel">
    <h1>
        {$_("Award lectures")} | {$_("Homecoming Day")} | {$_("Banquet")}
    </h1>
    <h2>{$_("venue")} <a class="button" href={$_("venue_url")}>{$_("layout")}</a></h2>

    <div class="container">
    <AsyncTable
        table={day2} 
        title=""
        available={all_talks}
        startminute={9*60+0}
        date={"2025-09-16"}
        on:search>
        <td>Time</td>
        {#each day2_shortcuts as shortcut}
        <td>
            <ShortCut label={shortcut[0]} query={shortcut[1]} on:search /><br />
            {shortcut[2]}<br />
            <LocationButton label={shortcut[4]} />{shortcut[3]}
        </td>
        {/each}
        <!-- <td>
            <ShortCut label={$_("Award lectures")} query={"^Aw-"} on:search /><br />
            {$_("awardvenue")}
        </td>
        <td>
            <br />
            {$_("hcvenue")}
        </td> -->
    </AsyncTable>
    <!-- <h2>{$_("banquetvenue")}</h2> -->
    <AsyncTable 
        table={banquet} 
        title={$_("banquetvenue")} 
        available={all_talks}
        startminute={18*60+0}
        date={"2023-09-23"}
        on:search>
        <td>Time</td>
    </AsyncTable>
    </div>
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
    }

</style>
