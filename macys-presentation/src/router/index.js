import { createRouter, createWebHistory } from 'vue-router'

// Import page components
const SubscribePage = () => import('../views/SubscribePage.vue')
const SigninPage = () => import('../views/SigninPage.vue')
const WelcomePage = () => import('../views/WelcomePage.vue')
const RegisterPage = () => import('../views/Register.vue')

const routes = [
  {
    path: '/',
    redirect: '/register'
  },
  {
    path: '/subscribe',
    name: 'Subscribe',
    component: SubscribePage
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },
  {
    path: '/signin',
    name: 'Signin',
    component: SigninPage
  },
  {
    path: '/welcome',
    name: 'Welcome',
    component: WelcomePage,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard for protected routes
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('user') !== null
  
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    // If route requires auth and user is not authenticated, redirect to signin
    next({ name: 'Signin' })
  } else if (to.path === '/signin' && isAuthenticated) {
    // If user is already authenticated and tries to access signin, redirect to welcome
    next({ name: 'Welcome' })
  } else {
    next()
  }
})

export default router
