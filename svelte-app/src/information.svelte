<script lang="ts">
    import { _ } from 'svelte-i18n';
    import SmartTable from './Components/smarttable.svelte';

    let table
    _.subscribe(t=>{

        const venue = "<a href='"+t("venue_url")+"'>"+t("venue")+"</a>"
        const awardvenue    = "<a href='"+t("awardvenue_url")+"'>"+t("awardvenue")+"</a>"
        const banquetvenue  = "<a href='"+t("banquetvenue_url")+"'>"+t("banquetvenue")+"</a>"
        const luncheonvenue = "<a href='"+t("venue_url")+"'>"+t("luncheonvenue")+"</a>"
        const hcvenue    = "<a href='"+t("hcvenue_url")+"'>"+t("hcvenue")+"</a>"

        table=[
            [t("Date"), t("Time"), t("Event"), t("Access")],
            [t("day1"), "9:00-11:30", t("Morning sessions"), venue],
            [t("day1"), "12:50-14:50", t("Poster sessions"), venue],

            [t("day2"), "9:00-11:55", t("Award lectures"), awardvenue],
            [t("day2"), "14:00-16:40", t("Award lectures"), awardvenue],
            [t("day2"), "16:50-18:15", t("JSCC General Meeting"), awardvenue],
            [t("day2"), "16:50-18:20", t("Homecoming Day"), hcvenue],
            [t("day2"), "18:30-20:30", t("Banquet"), banquetvenue],

            [t("day3"), "9:00-11:30", t("Morning sessions"), venue],
            [t("day3"), "11:40-12:50", t("Luncheon seminars"), luncheonvenue],
            [t("day3"), "12:55-14:55", t("Poster sessions"), venue],
            [t("day3"), "15:40-18:10", t("Afternoon sessions"), venue],
        ];
    })

</script>

<div class="post">
    <SmartTable {table} />
</div>

<style>
    div.post {
        margin: 2px;
    }
</style>
