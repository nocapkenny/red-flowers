import './assets/sytles/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import { createHead } from "@vueuse/head";

import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(createHead())
app.use(autoAnimatePlugin)

app.mount('#app')
