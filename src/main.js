import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import { createRouter, createWebHistory } from 'vue-router'

// Import components for routing
import Home from './components/Home.vue'

// Define routes
const routes = [
  { path: '/', component: Home }
]

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes
})

// Create and mount the Vue application
const app = createApp(App)
app.use(router)
app.mount('#app')