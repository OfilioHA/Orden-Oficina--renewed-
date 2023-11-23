<script>
  import { tasksPersonal } from "@/stores/tasks";
  import TaskPersonalItem from "./item.svelte";
</script>

<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th colspan="3">Rondas</th>
    </tr>
  </thead>
  <tbody>
    {#each $tasksPersonal as personal (personal.id)}
      <TaskPersonalItem {personal} />
    {/each}
  </tbody>
</table>
