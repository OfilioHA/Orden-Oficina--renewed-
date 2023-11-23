<script>
  /** @type {import('./$types').PageData} */
  export let data;

  import TaskSelector from "@/components/task/selector.svelte";
  import TaskPersonal from "@/components/task/personal/index.svelte";
  import { Container } from "@svelteuidev/core";
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
      <TaskSelector />
      <TaskPersonal />
    </Grid.Col>
  </Grid>
</Container>
