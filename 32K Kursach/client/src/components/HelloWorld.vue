<script setup>
import { onMounted } from "vue";

defineProps({
  msg: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="h-screen flex flex-row">
    <div class="flex-2/5 bg-green-700 text-white">
      <p class="p-5">This is example</p>
    </div>
    <div class="flex-3/5 p-3"></div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
