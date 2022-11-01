<template>
  <NavbarComp @logout="logout" />
  <section class="section">
    <my-message
      @closeMessage="closeMessage"
      :messages="error_messages"
      v-if="showErrors"
      class="is-danger"
    />
				<div class="box">
						<p class="title is-size-6">Текущие игры:</p>	
				</div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import NavbarComp from "@/components/NavbarComp.vue";
import axios from "axios";
export default defineComponent({
  components: {
    NavbarComp,
  },
  setup() {
    //Tools
    const store = useStore();
    const router = useRouter();

				// Game sessions

    // Player interaction
    const logout = () => {
      const form = {
        username: store.state.username,
      };
      axios
        .post("api/v1/player_logout/", form)
        .then((res) => {
          console.log(res);
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

    return { logout, error_messages, showErrors, toggleErrors, closeMessage };
  },
});
</script>

<style scoped></style>
