<template>
  <div class="about">


    <h1>{{data_about.header}}</h1>
    <div v-if="edit? false: true">
      <p v-html="data_about.about_info">
      </p>
      <b-button variant="outline-primary" @click="edit = true">Редактировать</b-button>
    </div>

    <div v-else>
      <p>
        <b-form-textarea
      id="textarea"
      v-model="data_about.about_info"
      placeholder="Редактировать..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
      </p>

      <b-button variant="outline-primary" class="m-1" @click="edit = false">Отмена</b-button>
      <b-button variant="success" class="m-1" @click="updated">Обновить</b-button>
    </div>


  </div>
</template>
<script>
  export default {
        name: "resultsComponent",
        data() {
            return {
                edit: false,
                data_about:[]
            }
        },
        methods:{
          updated:function () {
            this.axios.put('/api/about/',this.data_about).then(response => {
                this.about_info = response.data[0];

            }).catch().finally(() => {this.edit = false})
          }
        },
        mounted() {
            this.result = '';
            this.axios.get('/api/about/').then(response => {
                this.data_about = response.data[0];

            }).catch().finally()
        }
    }
</script>
