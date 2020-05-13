import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
Vue.use(VueRouter)

  const routes = [
      {
       path:'*',
       name: 'NotFound',
       component: () => import('../views/NotFound.vue')
      },
      {
          path:'/403',
          name: '403',
          component: () => import('../views/403.vue')
      },
      {
        path:'/login',
        name:'Login',
        component: () => import('../views/Login.vue')
      },
      {
        path: '/registration',
        name: 'Registration',
        component: () => import('../views/Registration.vue'),
      },
      {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {'rolereq':'any'},
      },
      {
        path:'/results',
        name:'resultsComponent',
        component: () => import('../views/resultsComponent.vue'),
        meta: {'rolereq':'any'},
      },
      {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
    if (to.meta.rolereq !== undefined) {
        if (to.meta.rolereq === 'any') {
            if (localStorage.getItem('jwt-access') != null) {
                next()
            } else {
                next('/403')
            }
        } else {
            next('/403')
        }
    } else {
        next()
    }
})
export default router
