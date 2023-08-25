<script>
    import { _ } from 'svelte-i18n';
    import SessionTable from "./Components/SessionTable/sessiontable.svelte";
    import AsyncTable from "./Components/TimeTable/asynctable.svelte";
    import PosterTables2 from "./Components/PosterTable/PosterTables2.svelte";

    let sessions = ["2Aa", "2Ab", "2Ac", "2B", "2C", "2D", "2E", "2Fa", "2Fb", "2Fc"]
    let bins_am = ["9:00", "9:20", "9:40", "10:00", "10:20", "10:30", "10:50", "11:10", "11:30"]
    let slots_am = ["1", "2", "3", "4", "", "5", "6", "7", "8"]

    let rooms_day2pm = ["Time", "2Aa", "2Ab", "2Ac", "2B", "2C", "2D/S7", "2E", "2Fa", "2Fb", "2Fc"]

    let day2pm = [
        [
            {"bin":[15,0,60],  "id":"", "label":"15:00"},
            {"bin":[,,60],  "id":"", "label":"16:00"},
            {"bin":[,,60],  "id":"", "label":"17:00"},
            {"bin":[,,60],  "id":"", "label":"18:00"},
            {"bin":[,,60],  "id":"", "label":"19:00"},
            {"bin":[,,60],  "id":"", "label":"20:00"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Aa-09", "label":"09"},
            {"bin":[,,20],  "id":"2Aa-10", "label":"10"},
            {"bin":[,,20],  "id":"2Aa-11", "label":"11"},
            {"bin":[,,20],  "id":"2Aa-12", "label":"12"},
            {"bin":[,,10],  "id":"", "label":""},
            {"bin":[,,20],  "id":"2Aa-13", "label":"13"},
            {"bin":[,,20],  "id":"2Aa-14", "label":"14"},
            {"bin":[,,20],  "id":"2Aa-15", "label":"15"},
            // {"bin":[,,20],  "id":"2Aa-16", "label":"16"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Ab-07", "label":"07"},
            {"bin":[,,20],  "id":"2Ab-08", "label":"08"},
            {"bin":[,,20],  "id":"2Ab-09", "label":"09"},
            {"bin":[,,20],  "id":"2Ab-10", "label":"10"},
            {"bin":[,,10],  "id":"", "label":""},
            {"bin":[,,20],  "id":"2Ab-11", "label":"11"},
            {"bin":[,,20],  "id":"2Ab-12", "label":"12"},
            {"bin":[,,20],  "id":"2Ab-13", "label":"13"},
            {"bin":[,,20],  "id":"2Ab-14", "label":"14"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Ac-09", "label":"09"},
            {"bin":[,,20],   "id":"2Ac-10", "label":"10"},
            {"bin":[,,20],  "id":"2Ac-11", "label":"11"},
            {"bin":[,,20],  "id":"2Ac-12", "label":"12"},
            {"bin":[,,10],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Ac-13", "label":"13"},
            {"bin":[,,20],  "id":"2Ac-14", "label":"14"},
            {"bin":[,,20],  "id":"2Ac-15", "label":"15"},
            // {"bin":[,,20],  "id":"2Ac-16", "label":"16"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2B-08", "label":"08"},
            {"bin":[,,20],   "id":"2B-09", "label":"09"},
            {"bin":[,,20],  "id":"2B-10", "label":"10"},
            {"bin":[,,20],  "id":"2B-11", "label":"11"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2C-08", "label":"08"},
            {"bin":[,,20],  "id":"2C-09", "label":"09"},
            {"bin":[,,20],  "id":"2C-10", "label":"10"},
        ],
        [
            {"bin":[15,0,30],   "id":"Aw-06", "label":$_("JSCC International Award for Creative Work")},
            {"bin":[,,10],       "id":"", "label":""},
            {"bin":[,,20],      "id":"2D-09", "label":"09"},
            {"bin":[,,20],      "id":"2D-10", "label":"10"},
            {"bin":[,,20],      "id":"2D-11", "label":"11"},
            {"bin":[,,80],     "id":"", "label":""},
            {"bin":[,,10],      "id":"", "label":$_("Explanation")+" 1"},
            {"bin":[,,20],      "id":"S7-01", "label":"S7-01"},
            {"bin":[,,20],      "id":"S7-02", "label":"S7-02"},
            {"bin":[,,5],       "id":"", "label":""},
            {"bin":[,,10],      "id":"", "label":$_("Explanation")+" 2"},
            {"bin":[,,20],      "id":"S7-03", "label":"S7-03"},
            {"bin":[,,20],      "id":"S7-04", "label":"S7-04"},
            {"bin":[,,5],       "id":"", "label":""},
            {"bin":[,,10],      "id":"", "label":$_("Explanation")+" 3"},
            {"bin":[,,20],      "id":"S7-05", "label":"S7-05"},
            {"bin":[,,10],      "id":"", "label":$_("Closing Remark")},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2E-08", "label":"08"},
            {"bin":[,,20],   "id":"2E-09", "label":"09"},
            {"bin":[,,20],  "id":"2E-10", "label":"10"},
            {"bin":[,,20],  "id":"2E-11", "label":"11"},
        ],
        [
            {"bin":[15,0,30],   "id":"Aw-07", "label":$_("JSCC Research Encouragement Award")},
            {"bin":[,,10],      "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fa-09", "label":"09"},
            {"bin":[,,20],   "id":"2Fa-10", "label":"10"},
            {"bin":[,,20],  "id":"2Fa-11", "label":"11"},
            {"bin":[,,20],  "id":"2Fa-12", "label":"12"},
            {"bin":[,,10],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fa-13", "label":"13"},
            {"bin":[,,20],  "id":"2Fa-14", "label":"14"},
            {"bin":[,,20],  "id":"2Fa-15", "label":"15"},
        ],
        [
            {"bin":[15,0,30],   "id":"Aw-07", "label":$_("JSCC Research Encouragement Award")},
            {"bin":[,,10],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fb-09", "label":"09"},
            {"bin":[,,20],   "id":"2Fb-10", "label":"10"},
            {"bin":[,,20],  "id":"2Fb-11", "label":"11"},
            {"bin":[,,20],  "id":"2Fb-12", "label":"12"},
            {"bin":[,,10],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fb-13", "label":"13"},
            {"bin":[,,20],  "id":"2Fb-14", "label":"14"},
            {"bin":[,,20],  "id":"2Fb-15", "label":"15"},
        ],
        [
            {"bin":[15,0,40],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fc-09", "label":"09"},
            {"bin":[,,20],   "id":"2Fc-10", "label":"10"},
            {"bin":[,,20],  "id":"2Fc-11", "label":"11"},
            {"bin":[,,20],  "id":"2Fc-12", "label":"12"},
            {"bin":[,,10],   "id":"", "label":""},
            {"bin":[,,20],  "id":"2Fc-13", "label":"13"},
            {"bin":[,,20],  "id":"2Fc-14", "label":"14"},
            {"bin":[,,20],  "id":"2Fc-15", "label":"15"},
            {"bin":[,,20],  "id":"2Fc-16", "label":"16"},
        ]        
    ]

</script>

<div class="panel">
    <h1>
        {$_("Oral sessions")}
    </h1>
    <SessionTable title={$_("Morning sessions")}
        sessions={sessions}
        timebins={bins_am}
        slots={slots_am}
        on:search />
    <!-- <AwardTable title={$_("Award lectures")}
        rooms={project.rooms_aw2}
        timebins={project.bins_aw2}
        button_titles={project.titles_aw2}
        ids={project.ids_aw2}
        on:search/> -->
    <!-- <SessionTable title={$_("Afternoon sessions")}
        sessions={project.sessions_day2}
        timebins={project.bins_pm}
        slots={project.slots_pm}
        on:search /> -->
    <AsyncTable 
        table={day2pm} 
        colnames={rooms_day2pm} 
        title={$_("Afternoon sessions")} 
        on:search />
</div>

<div class="panel">
    <h1>
        {$_("Poster sessions")}
    </h1>
    <PosterTables2 on:search />
</div>


<style>
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
</style>
