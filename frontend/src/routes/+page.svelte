<script>
  import TaskList from "../components/task/list.svelte";
  import { Button } from "@svelteuidev/core";
  import { Container } from "@svelteuidev/core";
  import { Grid } from "@svelteuidev/core";

  let clicked = false;
</script>

<Container>
  <Grid>
    <Grid.Col md={8}>
      <h1>Welcome to SvelteKit</h1>
      <p>
        Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
      </p>
      <TaskList />
      <Button on:click={() => (clicked = !clicked)} class="animation-bounce">
        {clicked ? "Don't click me anymore" : "Click me"}
      </Button>
    </Grid.Col>
  </Grid>
</Container>
