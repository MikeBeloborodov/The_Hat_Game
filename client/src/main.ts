import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

const app = createApp(App)

axios.defaults.baseURL = process.env.VUE_APP_DJANGO_HOST

app.use(store).use(router, axios).mount('#app')
