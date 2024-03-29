import Vue from "vue";
import VueRouter from "vue-router";
import Games from '../views/Games.vue'

Vue.use(VueRouter);

const routes = [
  {
    path : '/games',
    name : 'Games',
    component : Games,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
