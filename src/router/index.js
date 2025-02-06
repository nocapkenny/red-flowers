import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import("../pages/Home.vue"),
    },
    {
      path:"/about",
      name:"about",
      component: () => import("../pages/About.vue"),
    },
    {
      path:"/catalog",
      name:"catalog",
      component: () => import("../pages/Catalog.vue"),
    },
    {
      path:"/prices",
      name:"prices",
      component: () => import("../pages/Prices.vue"),
    },
    {
      path:"/gallery",
      name:"gallery",
      component: () => import("../pages/Gallery.vue"),
    },
    {
      path:"/vacancies",
      name:"vacancies",
      component: () => import("../pages/Vacancies.vue"),
    },
    {
      path:"/articles",
      name:"articles",
      component: () => import("../pages/Articles.vue"),
    },
    {
      path:"/contacts",
      name:"contacts",
      component: () => import("../pages/Contacts.vue"),
    },
  ],
});

export default router;
