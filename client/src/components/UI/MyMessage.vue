<template>
  <div class="message">
    <div class="message-header">
      <p>Error</p>
      <button @click="$emit('closeMessage')" class="delete"></button>
    </div>
    <div class="message-body">
      <div class="content">
        <ul>
          <li
            class="has-text-left pb-2"
            v-for="message in messages"
            :key="message"
          >
            <p>{{ message }}</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
export default defineComponent({
  name: "my-message",
  props: {
    messages: {
      required: true,
      type: Array as PropType<string[]>,
    },
  },
});
</script>

<style scoped></style>
