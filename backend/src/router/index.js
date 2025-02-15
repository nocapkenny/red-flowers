import { createRouter,createWebHashHistory} from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
      component: () => import('../views/home.vue')
  },
  {
    path: '/plant/:id/',
    name: 'plant-detail',
      component: () => import('../views/PlantDetail.vue')
  },
  {
    path: '/offer/',
    name: 'offer-list',
      component: () => import('../views/OfferList.vue')
  },
  {
      path: '/offer/:id/',
    name: 'offer-detail',
      component: () => import('../views/OfferDetail.vue')
  },
]

const router = createRouter({
    // mode: 'history',
    //history: createWebHistory(),
  history: createWebHashHistory(),
  base: process.env.BASE_URL,
  routes
})

export default router
