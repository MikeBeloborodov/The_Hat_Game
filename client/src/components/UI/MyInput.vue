<template>
  <input
    class="input"
    :value="modelValue"
    placeholder="Введите текст"
    @input="update"
  />
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "my-input",
  props: {
    modelValue: [String, Number],
  },
  setup(props, { emit }) {
    const update = (event: Event) => {
      emit("update:modelValue", (event.target as HTMLInputElement).value);
    };

    return { update };
  },
});
</script>

<style scoped></style>
