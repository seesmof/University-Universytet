<script setup>
import ChildComp from "./ChildComp.vue";
import { ref } from "vue";

const greets = ref("Allelujah");
</script>

<template>
  <input type="text" name="message" id="message" v-model="greets" />
  <ChildComp :message="greets" />
</template>
