<template>
    <div>
            <h3>РЕГИСТРАЦИЯ </h3>
             <b-form style="width: 20em;padding: 0.4em;  margin: auto" v-if="isAuth" class="border rounded shadow-lg p-3 mb-5 bg-white rounded">
                <b-form-success-feedback class="" :state="validation">
                    <b style="color: #34ce57">Регистрация прошла успешно  <b-icon icon="check" variant="success"></b-icon> </b>
                </b-form-success-feedback>
             </b-form>
            <b-form style="width: 20em;padding: 0.4em;  margin: auto" v-else class="border rounded shadow-lg p-3 mb-5 bg-white rounded">
                <b-form-invalid-feedback class="border rounded  mb-3 p-1 bg-warning" :state="validation">
                    <b>{{validationMessage}}</b>
                </b-form-invalid-feedback>
              <b-form-group style="text-align: left"  id="input-group-2" label="Логин:" label-for="input-1">
                <b-form-input
                  v-model="username"
                  id="input-1"
                  placeholder="Login"
                ></b-form-input>
                   <b-form-invalid-feedback :state="isValidationErrorInField.username">
                        {{validationMessageInField}}
                   </b-form-invalid-feedback>
                   <b-form-text id="input-text-2">
                        Логин не должен совпадасть с сущесвующем
                   </b-form-text>
              </b-form-group>
              <b-form-group style="text-align: left"  id="input-group-2" label="e-mail" label-for="input-2">
                <b-form-input
                  v-model="email"
                  id="input-2"
                  placeholder="e-mail"
                ></b-form-input>
                  <b-form-invalid-feedback :state="isValidationErrorInField.email">
                        {{validationMessageInField}}
                   </b-form-invalid-feedback>
                  <b-form-text id="input-text-2">
                  username@example.com
                </b-form-text>
              </b-form-group>
              <b-form-group style="text-align: left" id="input-group-3" label="Пароль:" label-for="input-3">
                <b-form-input
                  v-model="password"
                  id="input-3"
                  type="password"
                  placeholder="Password"
                ></b-form-input>
                <b-form-invalid-feedback :state="isValidationErrorInField.password">
                        {{validationMessageInField}}
                   </b-form-invalid-feedback>
                <b-form-text  id="input-text-3">
                  Паль должен иметь длину от 8-20, и не состоять только из цифр
                </b-form-text>
              </b-form-group>

              <b-button  @click="createUser" :disabled="ButtonDisable"  class="m-1" variant="success">Создать </b-button>
            </b-form>
            <b-form-group >
                <router-link to="/login" style="width: 18em;padding: 0.3em;  margin: auto;" block variant="link">Вход <b-icon icon="person-fill"   aria-hidden="true"></b-icon> </router-link>
            </b-form-group>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'
    export default {
        name: "Registration",
        data: function () {
            return {
                email: '',
                username: '',
                password: '',
                isRegistration:false,
                validation: true,
                validationMessage: '',
                validationMessageInField:'',
                isValidationErrorInField: {},
            }
        },
        computed: {
            ...mapGetters(['isAuth']),
            // eslint-disable-next-line vue/return-in-computed-property
            isUsernameValidation: function () {
                return this.username.length >= 3 ? true : null
            },
            isEmailValidation: function () {
                return this.email.match('^\\w{2,20}@\\w{2,20}\\.\\w{2,3}$') ? true : null
            },
            isPasswordValidation: function () {
                return !this.password.match('^\\d*$') && this.password.length >= 8 ? true : null
            },
            isValidationAllForm: function () {
                return this.isEmailValidation && this.isPasswordValidation && this.isUsernameValidation
            },
            ButtonDisable: function () {
               return (!this.isValidationAllForm || !this.validation)
            }
        },
        methods: {
            ...mapActions(['Login']),
            login: function () {
              this.validation = true;
              this.axios.post('/api/auth/login/', {username: this.username, password: this.password}).then((response) => {
                  this.Login(response.data)
                  setTimeout(()=>{this.$router.push({'path':'/'})},1000);

              }).catch((err) => {
                  if (err == 'Error: Network Error') {
                    this.validationMessage = err
                  } else {
                    this.validationMessage = 'Не верные данные, проверте правильность ввода логина или пароля'
                  }
                  this.validation = false;
              }).finally(() => {
                  setTimeout(() =>{this.validation = true;  this.password = '';}, 5000);
              })
            },
            createUser: function () {
                this.validation = true;
                this.axios.post('/api/auth/users/', {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }).then(() => {
                    this.login();
                }).catch((err) => {
                    this.errorHandler(err)
                }).finally(() => {
                    setTimeout(() => {
                        this.validation = true;
                        this.isValidationErrorInField= {};
                    }, 5000);
                })
            },
            errorHandler: function (err) {
                this.validation = false;
                if (err == 'Error: Network Error') {
                    this.validationMessage = err
                } else {
                    if (err.response.status >= 500) {
                        this.validationMessage = 'Неизвестная ошибка'
                    } else {
                        this.validationMessage = 'Исправте ошибки';
                        let errMessage = err.response.data.username ||
                            err.response.data.email ||
                            err.response.data.password;
                        this.validationMessageInField = errMessage.join();
                        this.isValidationErrorInField.username = (err.response.data.username)? false: null;
                        this.isValidationErrorInField.email = (err.response.data.email)? false: null;
                        this.isValidationErrorInField.password = (err.response.data.password)? false: null;

                    }
                }
            },
        }
    }
</script>

<style scoped>

</style>