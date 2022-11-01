import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import components from "@/components/UI";

const app = createApp(App);

axios.defaults.baseURL = process.env.VUE_APP_DJANGO_HOST;

components.forEach((component) => app.component(component.name, component));

app.use(store).use(router, axios).mount("#app");
