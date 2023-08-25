<script>
    import { _ } from 'svelte-i18n';
    import SessionTable from "../sessiontable.svelte";
    import AsyncTable from "../asynctable.svelte";
    import PosterTables from "../PosterTables.svelte";

    let sessions=["1Aa", "1Ab", "1Ac", "1Ad", "1C", "1D", "1Fa", "1Fb", "1Fc", "1Fd"]
    let bins_am = ["9:00", "9:20", "9:40", "10:00", "10:20", "10:30", "10:50", "11:10", "11:30"]
    let slots_am = ["1", "2", "3", "4", "", "5", "6", "7", "8"]
    let rooms_sy = ["Time", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]

    let symposia = [
        [
            {"bin":[15,0,60], "id":"", "label":"15:00"},
            {"bin":[,,60],    "id":"", "label":"16:00"},
            {"bin":[,,60],    "id":"", "label":"17:00"},
            {"bin":[,,60],    "id":"", "label":"18:00"},
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,25],    "id":"S1-01", "label":"01"},
            {"bin":[,,25],    "id":"S1-02", "label":"02"},
            {"bin":[,,25],    "id":"S1-03", "label":"03"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,25],    "id":"S1-04", "label":"04"},
            {"bin":[,,25],    "id":"S1-05", "label":"05"},
            {"bin":[,,25],    "id":"S1-06", "label":"06"},
            {"bin":[,,25],    "id":"S1-07", "label":"07"}
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,25],    "id":"S2-01", "label":"01"},
            {"bin":[,,25],    "id":"S2-02", "label":"02"},
            {"bin":[,,25],    "id":"S2-03", "label":"03"},
            {"bin":[,,25],    "id":"S2-04", "label":"04"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,25],    "id":"S2-05", "label":"05"},
            {"bin":[,,25],    "id":"S2-06", "label":"06"},
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,35],    "id":"S3-01", "label":"01"},
            {"bin":[,,25],    "id":"S3-02", "label":"02"},
            {"bin":[,,25],    "id":"S3-03", "label":"03"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,25],    "id":"S3-04", "label":"04"},
            {"bin":[,,25],    "id":"S3-05", "label":"05"},
            {"bin":[,,25],    "id":"S3-06", "label":"06"},
            {"bin":[,,25],    "id":"S3-07", "label":"07"},
            {"bin":[,,25],    "id":"S3-07", "label":"08"}
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,30],    "id":"S4-01", "label":"01"},
            {"bin":[,,25],    "id":"S4-02", "label":"02"},
            {"bin":[,,30],    "id":"S4-03", "label":"03"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,30],    "id":"S4-04", "label":"04"},
            {"bin":[,,25],    "id":"S4-05", "label":"05"},
            {"bin":[,,30],    "id":"S4-06", "label":"06"},
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,25],    "id":"S5-01", "label":"01"},
            {"bin":[,,25],    "id":"S5-02", "label":"02"},
            {"bin":[,,25],    "id":"S5-03", "label":"03"},
            {"bin":[,,30],    "id":"S5-04", "label":"04"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,25],    "id":"S5-05", "label":"05"},
            {"bin":[,,25],    "id":"S5-06", "label":"06"},
            {"bin":[,,30],    "id":"S5-07", "label":"07"}
        ],
        [
            {"bin":[15,0,5],  "id":"", "label":""},
            {"bin":[,,30],    "id":"S6-01", "label":"01"},
            {"bin":[,,30],    "id":"S6-02", "label":"02"},
            {"bin":[,,10],    "id":"", "label":""},
            {"bin":[,,30],    "id":"S6-03", "label":"03"},
            {"bin":[,,30],    "id":"S6-04", "label":"04"},
            {"bin":[,,30],    "id":"S6-05", "label":"05"},
            {"bin":[,,30],    "id":"S6-06", "label":"06"},
        ],
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
    <AsyncTable 
        table={symposia} 
        colnames={rooms_sy} 
        title={$_("Symposia")} 
        on:search/>
</div>
<div class="panel">
    <h1>
        {$_("Poster sessions")}
    </h1>
    <PosterTables on:search/>
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
