<template>
  <div class="container">
    <form action="" @submit.prevent>
      <div class="field">
        <label class="label">Команда #1</label>
        <my-input v-model="session_form.team1" placeholder="Введите название" />
      </div>
      <div class="field">
        <label class="label">Команда #2</label>
        <my-input v-model="session_form.team2" placeholder="Введите название" />
      </div>
      <div class="field">
        <label class="label">Кол-во слов на каждого</label>
        <my-input
          v-model="session_form.words_per_player"
          placeholder="Введите число"
        />
      </div>
      <div class="field">
        <div class="buttons is-right">
          <my-button @click="submitForm" class="is-info">Создать</my-button>
        </div>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore } from "vuex";
export default defineComponent({
  setup(props, { emit }) {
    // Tools
    const store = useStore();

    // New session
    const session_form = ref({
      username: store.state.username,
      team1: "",
      team2: "",
      words_per_player: 10,
    });
    const submitForm = () => {
      const form = {
        username: session_form.value.username,
        team1: session_form.value.team1,
        team2: session_form.value.team2,
        words_per_player: session_form.value.words_per_player,
      };
      emit("submitForm", form);
      session_form.value.team1 = "";
      session_form.value.team2 = "";
      session_form.value.words_per_player = 0;
    };

    return { session_form, submitForm };
  },
});
</script>

<style></style>
