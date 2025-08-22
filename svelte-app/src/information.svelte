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

            [t("day0"), "15:00-17:30", t("Public lectures"), venue],

            [t("day1"), "9:00-11:50", t("Morning sessions"), venue],
            [t("day1"), "12:00-12:50", t("Luncheon seminars"), venue], //luncheonvenue],
            [t("day1"), "13:00-15:00", t("Poster sessions"), venue],
            [t("day1"), "15:10-16:10", t("Afternoon sessions"), venue],
            [t("day1"), "16:20-19:30", t("Symposia"), venue],

            [t("day2"), "9:00-11:45", t("Award lectures"), awardvenue], // old
            [t("day2"), "13:45-15:50", t("Award lectures"), awardvenue], // old
            [t("day2"), "16:00-17:30", t("JSCC General Meeting"), awardvenue], // old

            [t("day2"), "16:00-17:30", t("Homecoming Day"), hcvenue],

            [t("day2"), "18:30-20:30", t("Banquet"), banquetvenue], //old

            [t("day3"), "9:00-11:50", t("Morning sessions"), venue],
            [t("day3"), "12:50-14:50", t("Poster sessions"), venue],
            [t("day3"), "15:00-16:00", t("Afternoon sessions"), venue],
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
