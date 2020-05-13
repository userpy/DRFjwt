<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand to="/" href="#"><font-awesome-icon icon="user-secret" /></b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
         <b-nav-item class="nav-item" ><router-link style="color: #e6f5e9;" to="/">Главная</router-link></b-nav-item>
        <b-nav-item class="nav-item" ><router-link style="color: #e6f5e9;" to="/about">О нас</router-link></b-nav-item>
      </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto" v-if='isAuth'>
          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <em>{{userName}} <b-icon icon="person-fill"></b-icon></em>
            </template>
            <b-dropdown-item ><b-link @click="logOutAndRoute">Выход</b-link></b-dropdown-item>
            <b-dropdown-item ><b-link @click="$router.push({'path':'/results'})" >Личный кабинет</b-link></b-dropdown-item>
          </b-nav-item-dropdown>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-else>
          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <em><b-icon icon="person-fill"></b-icon></em>
            </template>
            <b-dropdown-item ><b-link @click="$router.push({'path':'/login'})">Вход</b-link></b-dropdown-item>
            <b-dropdown-item ><b-link @click="$router.push({'path':'/registration'})">Регистрация</b-link></b-dropdown-item>
          </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    {{jwtDet}}
    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>
<script>
  import {mapGetters, mapActions} from 'vuex'
  export default {
    name:'App',
    computed:{
      ...mapGetters([
              'isAuth',
              'userName'
      ])
    },
    methods:{
      ...mapActions([
              'Logout'
      ]),
      logOutAndRoute: function () {
        this.Logout();
        this.$router.push({'path':'/login'});
      }
    }
  }
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
