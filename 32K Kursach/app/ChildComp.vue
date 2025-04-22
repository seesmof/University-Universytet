<script setup>
const props = defineProps({
  message: String,
});

const emit = defineEmits(["msg"]);

function emitEvent() {
  emit("msg", message.value);
  console.log(message);
}
</script>

<template>
  <h2>Amen</h2>
  <p>{{ message }}</p>
  <button @click="emitEvent">Send</button>
</template>
