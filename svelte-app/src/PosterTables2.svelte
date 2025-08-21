<script lang="ts">
    import PosterTable from "./Components/PosterTable2/postertable.svelte";

    function range(a,b){
        let c = new Set();
        for(let i=a; i<=b; i++){
            c.add(i);
        }
        return c;
    }
    function array(a,b){
        let c = []
        for(let i=a; i<=b; i++){
            c.push(i)
        }
        return c
    }
</script>

<PosterTable title={""}
    sessions={[
        {prefix:"3PA-", items:array(1,93)},
        {prefix:"3PB-", items:array(1,11)},
        {prefix:"3PC-", items:array(1,15)},
        {prefix:"3PD-", items:array(1,13)},
        {prefix:"3PE-", items:array(1,11)},
        {prefix:"3PF-", items:array(1,40)},
    ]}
    on:search />
