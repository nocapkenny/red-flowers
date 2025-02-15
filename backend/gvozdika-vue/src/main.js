import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "@/store"

//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
//import '@/style.css'


import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

import axios from "axios"
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'
// Make BootstrapVue available throughout your project
// Optionally install the BootstrapVue icon components plugin


const app = createApp(App)
app.use(router)
app.use(store)
//app.use(vSelect)
app.component("v-select", vSelect);

//app.use(BootstrapVue)
//app.use(IconsPlugin)

//app.component('v-select', vSelect)
app.mount('#app')
