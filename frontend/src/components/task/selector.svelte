<script>
  import { onMount } from "svelte";
  import { NativeSelect } from "@svelteuidev/core";
  import { tasksPersonal } from "@/stores/tasks";
  import { taskSelected } from "@/stores/tasks";
  import fetcher from "@/hooks/useFetch";

  let tasks = [];

  onMount(async () => {
    const response = await fetcher.get("/task");
    tasks = response.data.map(({ id, name }) => ({
      label: name,
      value: id,
    }));
    taskSelected.set(tasks[0]?.value);
  });

  $: {
    (async function () {
      if (!$taskSelected) return;
      const response = await fetcher.get(`/task/${$taskSelected}/personal`);
      tasksPersonal.set(response.data);
    })();
  }
</script>

<NativeSelect
  data={tasks}
  bind:value={$taskSelected}
  placeholder="Pick one"
  label="Select your favorite framework/library"
/>
