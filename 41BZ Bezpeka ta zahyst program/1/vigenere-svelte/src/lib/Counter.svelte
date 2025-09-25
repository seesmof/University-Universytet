<script lang="ts">
  import { fade } from "svelte/transition";

  let count: number = $state(0)
</script>

<button onclick={() => count++}>
  count is {count}
</button>
<p transition:fade>Jesus Christ is the LORD</p>
