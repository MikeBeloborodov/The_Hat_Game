<template>
  <NavbarComp @logout="logout" />
  <my-message
    @closeMessage="closeMessage"
    :messages="error_messages"
    v-if="showErrors"
    class="is-danger"
  />
  <section class="section">
    <div class="columns" v-if="game_session.team1">
      <div class="column">
        <div class="box">
          <p class="title is-size-5 has-text-centered">Команда #1</p>
          <div
            style="
              display: flex;
              align-items: center;
              justify-content: space-between;
            "
            class="mb-3"
          >
            <div>
              <p v-if="game_session.team1.name.length > 17" class="is-size-5">
                <strong>{{
                  game_session.team1.name.slice(0, 15) + "..."
                }}</strong>
              </p>
              <p v-else class="is-size-5">
                <strong>{{ game_session.team1.name }}</strong>
              </p>
              <p class="is-size-5">Очки: {{ game_session.team1.points }}</p>
              <div class="content">
                <p class="is-size-5">Игроки:</p>
                <ul>
                  <li
                    class="has-text-info is-size-5"
                    v-for="player in game_session.team1.players"
                    :key="player.username"
                  >
                    {{
                      player.username.length > 15
                        ? player.username.slice(0, 15) + "..."
                        : player.username
                    }}
                  </li>
                </ul>
              </div>
            </div>
            <my-button
              v-if="game_session.team1.id == playerData.team_id"
              @click="exitTeam(game_session.team1.name)"
              >Выйти</my-button
            >
            <my-button
              v-else
              @click="joinTeam(game_session.team1.name, 'team1')"
              class="is-primary"
              >Войти</my-button
            >
          </div>
        </div>
      </div>
      <div class="column">
        <div class="box">
          <p class="title is-size-5 has-text-centered">Команда #2</p>
          <div
            style="
              display: flex;
              align-items: center;
              justify-content: space-between;
            "
            class="mb-3"
          >
            <div>
              <p v-if="game_session.team2.name.length > 17" class="is-size-5">
                <strong>{{
                  game_session.team2.name.slice(0, 15) + "..."
                }}</strong>
              </p>
              <p v-else class="is-size-5">
                <strong>{{ game_session.team2.name }}</strong>
              </p>
              <p class="is-size-5">Очки: {{ game_session.team2.points }}</p>
              <div class="content">
                <p class="is-size-5">Игроки:</p>
                <ul>
                  <li
                    class="has-text-info is-size-5"
                    v-for="player in game_session.team2.players"
                    :key="player.username"
                  >
                    {{
                      player.username.length > 15
                        ? player.username.slice(0, 15) + "..."
                        : player.username
                    }}
                  </li>
                </ul>
              </div>
            </div>
            <my-button
              v-if="game_session.team2.id == playerData.team_id"
              @click="exitTeam(game_session.team2.name)"
              >Выйти</my-button
            >
            <my-button
              v-else
              @click="joinTeam(game_session.team2.name, 'team2')"
              class="is-primary"
              >Войти</my-button
            >
          </div>
        </div>
      </div>
      <div class="buttons is-centered mt-4">
        <my-button class="is-info">Начать</my-button>
        <my-button
          :class="{ 'is-loading': refreshLoading }"
          @click="refreshSession"
          >Обновить</my-button
        >
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, onBeforeMount, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";
import NavbarComp from "@/components/NavbarComp.vue";
import SessionDetails from "@/interfaces/SessionDetails";

function sleep(time: number) {
  return new Promise((r) => setTimeout(r, time));
}

export default defineComponent({
  props: ["id"],
  components: {
    NavbarComp,
  },
  setup(props) {
    // Tools
    const router = useRouter();
    const store = useStore();

    // Before mount
    onBeforeMount(() => {
      axios
        .get("api/v1/game_session/" + props.id + "/")
        .then((res) => {
          console.log(res);
          game_session.value = res.data.game_session as SessionDetails;
        })
        .catch((error) => {
          console.log(error);
        });

      axios
        .get("api/v1/player/?q=" + localStorage.getItem("username"))
        .then((res) => {
          playerData.value.username = res.data.player.username;
          playerData.value.team_id = res.data.player.team;
        })
        .catch((error) => {
          console.log(error);
        });
    });

    // Game session
    const game_session = ref<SessionDetails>({} as SessionDetails);
    const joinTeam = (team_name: string, team_type: string) => {
      const form = {
        username: localStorage.getItem("username"),
        team_name: team_name,
        method: "join",
      };
      axios
        .post("api/v1/teams/", form)
        .then((res) => {
          playerData.value.team_id = res.data.team.id;
          refreshSession();
        })
        .catch((error) => {
          console.log(error);
          if (error.response.status === 400) {
            toggleErrors([error.response.data.error_message]);
          }
        });
    };
    const exitTeam = (team_name: string) => {
      const form = {
        username: localStorage.getItem("username"),
        team_name: team_name,
        method: "exit",
      };
      axios
        .post("api/v1/teams/", form)
        .then((res) => {
          playerData.value.team_id = 0;
          refreshSession();
        })
        .catch((error) => {
          console.log(error);
        });
    };

    // Refresh
    const refreshLoading = ref(false);
    const refreshSession = async () => {
      refreshLoading.value = true;
      await sleep(500);
      axios
        .get("api/v1/game_session/" + props.id + "/")
        .then((res) => {
          game_session.value = res.data.game_session;
        })
        .catch((error) => {
          console.log(error);
          toggleErrors([error.message]);
        })
        .finally(() => {
          refreshLoading.value = false;
        });
    };

    // Player interaction
    const playerData = ref({
      team_id: 0,
      username: "",
    });
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
      router,
      props,
      logout,
      closeMessage,
      showErrors,
      game_session,
      joinTeam,
      refreshSession,
      refreshLoading,
      exitTeam,
      playerData,
      error_messages,
    };
  },
});
</script>

<style scoped></style>
