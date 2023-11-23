<script>
  import { NativeSelect } from "@svelteuidev/core";
  import { onMount } from "svelte";
  import { tasksPersonal } from "@/stores/tasks";
  import { activeRound } from "@/stores/tasks";
  import fetcher from "@/hooks/useFetch";

  let tasks = [];
  let selectedTask = null;

  onMount(async () => {
    const response = await fetcher.get("/task");
    tasks = response.data.map(({ id, name }) => ({
      label: name,
      value: id,
    }));
    selectedTask = tasks[0]?.value;
  });

  $: {
    (async function () {
      if (!selectedTask) return;
      const response = await fetcher.get(`/task/${selectedTask}/personal`);
      tasksPersonal.set(response.data.list);
      activeRound.set(response.data.round);
    })();
  }
</script>

<NativeSelect
  data={tasks}
  bind:value={selectedTask}
  placeholder="Pick one"
  label="Select your favorite framework/library"
/>
