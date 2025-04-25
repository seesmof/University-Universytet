<template>
  <div class="flex flex-col items-center justify-center gap-4 h-screen">
    <h1 class="font-bold text-2xl text-(--ui-primary)">Nuxt UI - Starter</h1>

    <div class="flex items-center gap-2">
      <UButton
        label="Documentation"
        icon="i-lucide-square-play"
        to="https://ui.nuxt.com/getting-started/installation/nuxt"
        target="_blank"
      />

      <UButton
        label="GitHub"
        color="neutral"
        variant="outline"
        icon="i-simple-icons-github"
        to="https://github.com/nuxt/ui"
        target="_blank"
      />
    </div>
  </div>

  <div class="bg-green-50 p-3">
    <button
      class="font-bold text-(--color)-[colorValue]"
      @click="
        colorValue.value =
          colorOptions[colorValueIndex + (1 % colorOptions.length)]
      "
    >
      Help
    </button>
  </div>
</template>

<script setup>
const colorOptions = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900];
const color = "green";
const colorValueIndex = ref(0);
const colorValue = ref(colorOptions[colorValueIndex]);
</script>
