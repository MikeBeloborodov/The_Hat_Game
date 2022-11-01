<template>
  <div class="modal" :class="{ 'is-active': showModal }">
    <div @click="$emit('closeModal')" class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ title }}</p>
        <button @click="$emit('closeModal')" class="delete"></button>
      </header>
      <section class="modal-card-body">
        <slot></slot>
      </section>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "my-modal",
  props: {
    title: String,
    showModal: Boolean,
  },
});
</script>

<style scoped></style>
