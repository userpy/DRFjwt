import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import router from "../router";
Vue.use(axios);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
      status: '',
      tokenAccess: localStorage.getItem('jwt-access'),
      tokenResfrash: localStorage.getItem('jwt-refresh'),
      user : {}
  },
  getters: {
      isAuth: state => {
          return state.tokenAccess != null? true: false;
      },
      userName: state => {
          if (state.tokenAccess != null) {
              let token = state.tokenAccess;
              let decode = jwtDecode(token).user_name;
              return decode;
          } else {
              return ''
          }

      },
      tokenRefrash: state => {
          return state.tokenResfrash
      }
  },
  mutations: {
        updateAccessToken (state, newAccessToken) {
            localStorage.setItem('jwt-access', newAccessToken);
            state.tokenAccess = newAccessToken;
            return true
        },
        updateRefrashToken (state, newRefrashToken) {
            localStorage.setItem('jwt-refrash', newRefrashToken);
            state.tokenResfrash = newRefrashToken;
            return true
        },
        removeAccessToken(state){
            localStorage.removeItem('jwt-access');
            state.tokenAccess = null;
            return true
        },
        removeRefrashToken(state){
            localStorage.removeItem('jwt-refrash');
            state.tokenResfrash=null;
            return true;
        }
  },
  actions: {
      Login ({commit}, response ) {
          commit('updateAccessToken', response.access);
          commit('updateRefrashToken', response.refresh);

      },
      Logout ({commit}) {
          commit('removeAccessToken');
          commit('removeRefrashToken');

      },
  },
  modules: {
  }
});

export default store

let authTokenRequest = null;

axios.interceptors.request.use(function (config) {
  const token = store.state.tokenAccess;
  if (token != null) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, function (err) {
  return Promise.reject(err)
});


axios.interceptors.response.use(function (response) {
  return response
}, function (err) {
  const originalRequest = err.config;
  if (err.response.data.code === "token_not_valid") {
    if (!authTokenRequest) {
      authTokenRequest = axios.post('/api/auth/refresh/', {refrash: store.getters.tokenResfrash}).then((response) => {
        store.dispatch('Login', response.data);
        const retryOriginalRequest = new Promise((resolve) => {
          originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
          resolve(axios(originalRequest))
        });
        resetAuthTokenRequest();
        return retryOriginalRequest
      }).catch(() => {
        store.dispatch('Logout');
        router.push('/login/');
        resetAuthTokenRequest();
        return Promise.reject(err)
      })
    }
    return authTokenRequest
  } else {
    return Promise.reject(err)
  }
});

function resetAuthTokenRequest () {
  authTokenRequest = null
}