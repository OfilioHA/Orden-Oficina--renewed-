<script>
  export let personal;
</script>

<tr>
  <td>{personal.firstnames} {personal.lastnames}</td>
  {#each personal.task_accomplished as accomplished (accomplished.id)}
    <td>{accomplished.id}</td>
  {/each}
</tr>
