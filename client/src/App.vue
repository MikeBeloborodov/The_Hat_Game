<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent, onBeforeMount } from "vue";
import { useStore } from "vuex";
export default defineComponent({
  setup() {
    // Tools
    const store = useStore();
    onBeforeMount(() => {
      store.commit("initializeStore");
    });

    return { store };
  },
});
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
