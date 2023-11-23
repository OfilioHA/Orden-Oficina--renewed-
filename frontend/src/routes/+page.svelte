<script>
  /** @type {import('./$types').PageData} */
  export let data;

  import TaskSelector from "@/components/task/selector.svelte";
  import TaskPersonal from "@/components/task/personal/index.svelte"
  import TaskList from "@/components/task/list.svelte"
  import TaskRoundSelector from "@/components/task/round_selector.svelte"
  import { Container } from "@svelteuidev/core"
  import { Grid } from "@svelteuidev/core";
</script>

<Container>
  <Grid>
    <Grid.Col md={8}>
      <h1>Welcome to SvelteKit</h1>
      <p>
        Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
      </p>
      <h1>{data.post.title}</h1>
      <div>{data.post.content}</div>
      <TaskList />
      <TaskSelector />
      <TaskRoundSelector />
      <TaskPersonal />
    </Grid.Col>
  </Grid>
</Container>
