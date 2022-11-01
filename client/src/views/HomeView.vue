<template>
  <section class="section">
    <div class="container has-text-centered pt-6">
      <div class="title is-size-4">The Шляпа</div>
      <my-message
        @closeMessage="closeMessage"
        :messages="error_messages"
        v-if="showErrors"
        class="is-danger"
      />
    </div>
  </section>
  <section class="section">
    <div class="container">
      <form action="" @submit.prevent>
        <label class="label"> Введите имя, чтобы начать играть </label>
        <my-input v-model="username" />
        <div class="buttons is-right">
          <my-button @click="registerUser" class="is-primary mt-3"
            >Принять</my-button
          >
        </div>
      </form>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import axios from "axios";

export default defineComponent({
  name: "HomeView",
  components: {},
  setup() {
    // Tools
    const store = useStore();
    const router = useRouter();

    // User interaction
    const username = ref("");
    const registerUser = () => {
      closeMessage();
      if (!username.value) {
        toggleErrors(["Заполните поле."]);
        return;
      }
      const form = {
        username: username.value,
      };
      axios
        .post("api/v1/player/", form)
        .then((res) => {
          store.commit("setUsername", form.username);
          router.push("/game");
        })
        .catch((error) => {
          if (
            error.response.data.error_message.username[0] ==
            "player with this username already exists."
          ) {
            toggleErrors(["Такое имя уже занято."]);
          } else {
            toggleErrors(error.message);
          }
        });
      username.value = "";
    };

    // Error messages
    const error_messages = ref([""]);
    const showErrors = ref(false);
    const toggleErrors = (errors: Array<string>) => {
      error_messages.value = [];
      error_messages.value = [...errors];
      showErrors.value = true;
    };
    const closeMessage = () => {
      error_messages.value = [];
      showErrors.value = false;
    };

    return {
      username,
      registerUser,
      error_messages,
      showErrors,
      toggleErrors,
      closeMessage,
    };
  },
});
</script>

<style scoped></style>
