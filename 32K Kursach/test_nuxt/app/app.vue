<script setup>
import { reactive, computed } from "vue";

const authors = reactive(
  {
    name: "John Doe",
    books: [
      "Vue 2 - Advanced Guide",
      "Vue 3 - Basic Guide",
      "Vue 4 - The Mystery",
    ],
  },
  {
    name: "Some",
    books: [],
  }
);

// a computed ref
const publishedBooksMessage = computed((author) => {
  return author.books.length > 0 ? "Yes" : "No";
});
</script>

<template>
  <ul v-for="author of authors">
    <span>{{ publishedBooksMessage(author) }}</span>
  </ul>
</template>
