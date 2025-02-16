import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import("../pages/Home/Home.vue"),
    },
    {
      path:"/about",
      name:"about",
      component: () => import("../pages/About/About.vue"),
    },
    {
      path:"/catalog",
      name:"catalog",
      component: () => import("../pages/Catalog/Catalog.vue"),
    },
    {
      path:"/prices",
      name:"prices",
      component: () => import("../pages/Prices/Prices.vue"),
    },
    {
      path:"/gallery",
      name:"gallery",
      component: () => import("../pages/Gallery/Gallery.vue"),
    },
    {
      path:"/vacancies",
      name:"vacancies",
      component: () => import("../pages/Vacancies/Vacancies.vue"),
    },
    {
      path:"/articles",
      name:"articles",
      component: () => import("../pages/Articles.vue"),
    },
    {
      path:"/contacts",
      name:"contacts",
      component: () => import("../pages/Contacts/Contacts.vue"),
    },
    {
      path:"/plant/:id",
      name: "plant-detail",
      component: () => import("../pages/PlantDetail/PlantDetail.vue"),
    }
  ],
});

export default router;
