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
          <my-button @click="registerUser" class="is-info mt-3"
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
          username.value = "";
        })
        .catch((error) => {
          console.log(error);
          try {
            const error_payload = error.response.data.error_message;
            toggleErrors([error_payload]);
          } catch (err) {
            console.log(err);
            toggleErrors(["Network error"]);
          } finally {
            username.value = "";
          }
        });
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
