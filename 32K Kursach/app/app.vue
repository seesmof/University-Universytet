<script setup>
import ChildComp from "./ChildComp";
import { ref } from "vue";
const message = ref("");
</script>

<template>
  <input type="text" name="message" id="messageInput" v-model="message" />
  <ChildComp>{{ message || "No message" }}</ChildComp>
</template>
