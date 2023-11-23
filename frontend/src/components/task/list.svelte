<script>
  import { onMount } from "svelte";
  import fetcher from "@/hooks/useFetch";

  let tasks = [];

  onMount(async () => {
    const response = await fetcher.get("/task");
    tasks = response.data;
  });
</script>

<ul>
  {#each tasks as task (task.id)}
    <li>{task.name}</li>
  {/each}
</ul>
