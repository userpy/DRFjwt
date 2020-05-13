<template>
  <div class="home">
    <b-container class="bv-example-row shadow-lg rounded-bottomh">
      <b-row style="background-color: #23aff2;" class="text-center" >
        <b-col ><b>Выберете тест</b><b-icon icon="filter"></b-icon></b-col>
        <b-col cols="9"><h2>система тестирования <b-icon icon="list" ></b-icon></h2></b-col>
      </b-row>
      <b-row>
        <b-col class="shadow-sm">
          <div class="m-1" >
            <b-button :disabled="MenubuttonDisabled" v-for="item in tests_names_menu" :key="item.test_name" block variant="primary" @click="loadTest(item.test_name)">{{item.test_name}}</b-button>
          </div>
        </b-col>
        <b-col class="shadow-sm" style="background-color: #9bd7ff" cols="9" > <test-component :MenubuttonDisabled.sync="MenubuttonDisabled" :questions="test"></test-component></b-col>
      </b-row>
      <b-row  class="text-center shadow-sm p-3 mb-5 bg-white">
        <b-col>2020   </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import TestComponent from "../components/TestComponent";
export default {
  name: 'Home',
  data: function() {
    return {
      tests_names_menu:[],
      test:[],
      MenubuttonDisabled: false,
    }
  },
  components: {
    TestComponent
  },
  methods: {
      loadTest: function (test_name) {

        this.axios.get('/api/tests/name/questions/',{params:{test_name: test_name}}).then(response => {
          this.test = response.data[0]
        }).catch().finally(this)
      }
  },
  created() {
    this.axios.get('/api/tests/name/').then(response => {
      this.tests_names_menu = response.data
    })
  }

}
</script>
