
 <template>

  <div class="container" >
    <h3>АВТОРИЗАЦИЯ</h3>
    <b-form style="width: 20em;padding: 0.4em;  margin: auto" v-if="isAuth" class="border rounded shadow-lg p-3 mb-5 bg-white rounded">
                <b-form-success-feedback class="" :state="validation">
                    <b style="color: #34ce57">Вы авторизованы<b-icon icon="check" variant="success"></b-icon> </b>
                </b-form-success-feedback>
             </b-form>
    <b-form  class="login_form border  rounded shadow-lg p-3 mb-5 bg-white rounded" v-else>
      <b-form-group class="login_form_label"  id="input-group-2" label="Логин:" label-for="input-2">
        <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0" >
           <b-form-input
          id="input-2"
          v-model="username"
          placeholder="Login"
        ></b-form-input >
        </b-input-group>
      </b-form-group>
      <b-form-group class="login_form_label"  id="input-group-3" label="Пароль:" label-for="input-3">
        <b-input-group prepend="'*'" class="mb-2 mr-sm-2 mb-sm-0" >
        <b-form-input
          id="input-3"
          v-model="password"
          type="password"
          placeholder="Password"
        ></b-form-input>
          </b-input-group>
        <b-form-invalid-feedback :state="validation">
         {{validation_message}}
        </b-form-invalid-feedback>
      </b-form-group>
      <b-button  @click="login" @keydown.enter="login" :disabled="ButtonDisable" variant="primary">Войти</b-button>
    </b-form>
    <b-form-group>
      <router-link to="/registration" style="width: 18em;padding: 0.3em;  margin: auto;" block variant="link"><span style="font-weight: 100;">Регистрация</span> <b-icon icon="person-plus"   aria-hidden="true"></b-icon>   </router-link>
    </b-form-group>
    <p></p>
    </div>

</template>
<script>
    import { mapActions, mapGetters } from 'vuex'
    export default {
        name: "Login",
         computed:{
            ...mapGetters(['isAuth']),
            IsfieldsValidation: function() {
              return (this.password.length >= 3 && this.username.length >= 3)
            },
            ButtonDisable: function() {
             if (!this.IsfieldsValidation || !this.validation) {
               return true
             } else {
               return false
             }
           }
         },
         data: function () {
            return {
              username: '',
              password: '',
              jwt:null,
              validation: true,
              validation_message:null,
            }
          },
          methods: {
            ...mapActions(['Login']),
            login: function () {
              this.validation = true;
              this.axios.post('/api/auth/login/', {username: this.username, password: this.password}).then((response) => {
                  this.Login(response.data);
                  setTimeout(() => {this.$router.push({'path':'/'});}, 500);
              }).catch((err) => {
                  if (err == 'Error: Network Error') {
                    this.validation_message = err
                  } else {
                    this.validation_message = 'Не верные данные, проверте правильность ввода логина или пароля'
                  }
                  this.validation = false;
              }).finally(() => {
                  setTimeout(() =>{this.validation = true;  this.password = '';}, 5000);
              })
            },
          },
    }
</script>

<style scoped>
  .login_form {
    width: 18em;
    padding: 0.4em;
    margin: auto;
  }
  .login_form_label {
    text-align: left
  }

</style>