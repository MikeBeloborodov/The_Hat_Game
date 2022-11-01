import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    username: "",
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("username")) {
        const username = localStorage.getItem("username");
        state.username = username ? username : "";
        state.isAuthenticated = true;
      } else {
        state.username = "";
        state.isAuthenticated = false;
      }
    },
    setUsername(state, username) {
      state.isAuthenticated = true;
      state.username = username;
    },
    removeUsername(state) {
      state.isAuthenticated = false;
      state.username = "";
    },
  },
  actions: {},
  modules: {},
});
