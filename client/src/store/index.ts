import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    username: "",
  },
  getters: {},
  mutations: {
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
