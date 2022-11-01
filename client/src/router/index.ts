import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SessionView from "@/views/SessionView.vue";
import GameView from "@/views/GameView.vue";
import store from "@/store";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/sessions",
    name: "sessions",
    component: SessionView,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/game",
    name: "game",
    component: GameView,
    meta: {
      requireLogin: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  to.matched.some((record) => {
    if (record.meta.requireLogin && !store.state.isAuthenticated) {
      next("/");
    } else {
      next();
    }
  });
});

export default router;
