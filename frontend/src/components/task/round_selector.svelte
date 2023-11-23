<script>
  import { NativeSelect } from "@svelteuidev/core";
  import { activeRound } from "@/stores/tasks";
  import { tasksPersonal } from "@/stores/tasks";
  import fetcher from "@/hooks/useFetch";
  import { onMount } from "svelte";

  let needFetch = false;
  let rounds = [];

  onMount(async ()=>{

  })

  $: (async function () {
    needFetch = !needFetch || !$activeRound;
    if (needFetch) return;
    const { data } = await fetcher.get(`/round/${$activeRound}/personal`);
    tasksPersonal.set(data.active);
  })();
</script>

<NativeSelect
  data={rounds}
  bind:value={$activeRound}
  placeholder="Pick one"
  label="Select your favorite framework/library"
/>
