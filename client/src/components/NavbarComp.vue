<template>
  <div class="navbar is-info">
    <div class="navbar-brand">
      <div class="navbar-item">
        <p class="is-size-4">Шляпа</p>
      </div>
      <a
        class="navbar-burger"
        :class="{ 'is-active': showBurger }"
        @click="toggleBurger"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" :class="{ 'is-active': showBurger }">
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary" @click="logout">Выйти</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore } from "vuex";
export default defineComponent({
  setup(props, { emit }) {
    // Tools
    const store = useStore();

    // Navbar burger
    const showBurger = ref(false);
    const toggleBurger = () => {
      showBurger.value = !showBurger.value;
    };

    // Logout
    const logout = () => {
      emit("logout");
      toggleBurger();
    };

    return { store, showBurger, toggleBurger, logout };
  },
});
</script>

<style scoped></style>
