<template>
  <my-modal
    class=""
    title="Создать игру"
    @closeModal="toggleModal"
    :showModal="showModal"
  >
    <NewSession @submitForm="submitForm" />
  </my-modal>
  <NavbarComp @logout="logout" />
  <section class="section">
    <my-message
      @closeMessage="closeMessage"
      :messages="error_messages"
      v-if="showErrors"
      class="is-danger"
    />
    <div class="box">
      <p class="title is-size-4">Текущие игры:</p>
      <div v-if="game_sessions">
        <div
          style="
            display: flex;
            align-items: center;
            justify-content: space-between;
          "
          class="mb-3"
          v-for="game in game_sessions"
          :key="game.id"
        >
          <p class="is-size-5" v-if="game.owner.username.length > 16">
            {{ game.owner.username.slice(0, 17) + "..." }}
          </p>
          <p class="is-size-5" v-else>
            {{ game.owner.username }}
          </p>
          <my-button @click="openSession(game.id)" class="is-primary"
            >Зайти</my-button
          >
        </div>
      </div>
      <div v-else>
        <p>В данный момент игр нет.</p>
      </div>
      <div class="buttons is-centered mt-5">
        <my-button class="is-info" @click="createSession">Создать</my-button>
        <my-button
          :class="{ 'is-loading': refreshLoading }"
          @click="refreshSessions"
          >Обновить</my-button
        >
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, onBeforeMount, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import NavbarComp from "@/components/NavbarComp.vue";
import NewSession from "@/components/NewSession.vue";
import NewSessionInterface from "@/interfaces/NewSessionInterface";
import axios from "axios";

function sleep(time: number) {
  return new Promise((r) => setTimeout(r, time));
}

export default defineComponent({
  components: {
    NavbarComp,
    NewSession,
  },
  setup() {
    //Tools
    const store = useStore();
    const router = useRouter();

    // Before mount hook
    onBeforeMount(() => {
      // load game sessions
      axios
        .get("api/v1/game_session/")
        .then((res) => {
          game_sessions.value = res.data.game_sessions;
        })
        .catch((error) => {
          console.log(error);
          toggleErrors([error.message]);
        });
    });

    // Game sessions
    const game_sessions = ref([]);
    const createSession = () => {
      showModal.value = true;
    };
    const showModal = ref(false);
    const toggleModal = () => {
      showModal.value = !showModal.value;
    };
    const refreshLoading = ref(false);
    const refreshSessions = async () => {
      refreshLoading.value = true;
      await sleep(500);
      axios
        .get("api/v1/game_session/")
        .then((res) => {
          game_sessions.value = res.data.game_sessions;
        })
        .catch((error) => {
          console.log(error);
          toggleErrors([error.message]);
        })
        .finally(() => {
          refreshLoading.value = false;
        });
    };
    const submitForm = (form: NewSessionInterface) => {
      showModal.value = false;
      axios
        .post("api/v1/game_session/", form)
        .then((res) => {
          refreshSessions();
        })
        .catch((error) => {
          console.log(error);
          toggleErrors([error.message]);
        });
    };
    const openSession = (game_id: number) => {
      router.push({ name: "game", params: { id: game_id } });
    };

    // Player interaction
    const logout = () => {
      const form = {
        username: store.state.username,
      };
      axios
        .post("api/v1/player_logout/", form)
        .then((res) => {
          localStorage.removeItem("username");
          router.push("/");
        })
        .catch((error) => {
          console.log(error);
          try {
            const error_payload = error.response.data.error_message;
            toggleErrors([error_payload]);
          } catch (err) {
            console.log(err);
            toggleErrors(["Network error"]);
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
      logout,
      error_messages,
      showErrors,
      toggleErrors,
      closeMessage,
      game_sessions,
      showModal,
      toggleModal,
      createSession,
      refreshSessions,
      refreshLoading,
      submitForm,
      openSession,
    };
  },
});
</script>

<style scoped></style>
