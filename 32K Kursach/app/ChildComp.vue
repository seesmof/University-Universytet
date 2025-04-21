<script setup>
const props = defineProps({
  message: String,
});
</script>

<template>
  <h2>Amen</h2>
  <p>{{ message }}</p>
</template>
