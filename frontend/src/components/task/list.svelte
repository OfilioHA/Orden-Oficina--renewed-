<script>
  import { NativeSelect } from "@svelteuidev/core";
  import { onMount } from "svelte";
  import fetcher from "@/hooks/useFetch";

  let tasks = [];
  let selectedTask = null;
  let personal = [];
  let roundActive = 0;

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
      personal = response.data.list;
      roundActive = response.data.round;
    })();
  }
</script>

<div>
  <NativeSelect
    data={tasks}
    bind:value={selectedTask}
    placeholder="Pick one"
    label="Select your favorite framework/library"
  />

  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th colspan="3">Rondas</th>
      </tr>
    </thead>
    <tbody>
      {#each personal as task (task.id)}
        <tr>
          <td>{task.firstnames} {task.lastnames}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
