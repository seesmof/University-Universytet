<script setup>
import { RouterLink, RouterView } from "vue-router";
import { watch, ref, created } from "vue";

const bunches = ref([]);

created(){
  fetch("http://127.0.0.1:8000/bunches", {
    mode: "no-cors"
  }).then((response) => response.json()).then((data) => (bunches.value = data));
};
</script>

<template>
  <div class="h-screen flex flex-row overflow-hidden">
    <div class="flex-1/5 bg-green-700 text-white sticky top-0">
      <RouterLink
        to="/"
        class="p-3 block font-medium w-full hover:bg-green-800 bg-green-800"
        >Grapes</RouterLink
      >
      <RouterLink to="/" class="p-3 block font-medium w-full hover:bg-green-800"
        >New</RouterLink
      >
    </div>
    <div class="flex-4/5 p-3 overflow-y-scroll">
      <p v-if="bunches.length > 0">{{ bunches }}</p>
      <p v-else>No bunches yet</p>
    </div>
  </div>
</template>
