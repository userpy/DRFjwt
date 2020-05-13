<template>
    <div>
      <div v-if="questions.questions.length > 0? true: false">

          <div v-if="start_question < questions.questions.length">
              <p>{{questions.test_name}}</p>
               <div v-if="!testStarted">
                   <b-btn class="m-2 text-left" variant="success" @click="startTest"> Начать тестирование </b-btn>
               </div>
               <div v-else>
                   <h3 class="text-left"><b>Вопрос {{start_question}}: </b>{{current_question}}</h3>
                    <answers-component :multiple_choice="questions.questions[start_question].multiple_choice"
                                       :answers="questions.questions[start_question].answers"
                                       :button_next_disabled.sync="button_next_disabled"
                                       :selected_answer.sync="selected_answer"
                                       :current_question="current_question"  >

                    </answers-component>
                    <b-btn class="m-2 text-left" variant="success" :disabled="button_next_disabled" @click="nextQuestin"> >> </b-btn>
               </div>
          </div>
          <div v-else class="m-4">
              <b-alert variant="success" show>  Тестирование <b>{{questions.test_name}}</b> окончено
                <ul>
                    <li v-for="i in answers" :key="i">{{i.current_question}} - {{i.answer}} <span v-if="i.сorrect_answer">Верно</span><span v-else >Не верно</span></li>
                </ul>
              </b-alert>
          </div>
      </div>
      <div class="p-2" v-else>Вопросы не добавлены <b-icon icon="exclamation-circle-fill" variant="danger"></b-icon> </div>
    </div>
</template>

<script>
    import AnswersComponent from "../views/AnswersComponent";

    export default {
        name: "TestComponent",
        components: {
            AnswersComponent,
        },
        props: {
            questions: [],
            statr: null,
            MenubuttonDisabled: null,
        },
        data:function(){
            return{
                start_question: 0,
                testStarted: false,
                button_next_disabled: true,
                selected_answer:null,
                answers:[],
            }
        },
        computed:{
            current_question: function () {
                return this.questions.questions[this.start_question].question
            }
        },
        methods:{
            nextQuestin: function () {
                this.answers.push(this.selected_answer);
                this.start_question++;

            },
            startTest: function () {
                this.button_next_disabled = true;
                this.testStarted = true;
                this.$emit('update:MenubuttonDisabled', true);
                this.answers = [];
            }
        },
        watch:{
            questions: function () {
                this.start_question = 0;
                this.testStarted = false;

            },
            start_question: function () {
                if (this.start_question >= this.questions.questions.length) {
                        this.$emit('update:MenubuttonDisabled', false);
                        let tryeAnswers = 0;
                        this.answers.forEach(item => {
                            if(item.сorrect_answer) {
                                tryeAnswers++;
                            }
                        });
                        let result = 'Правильных ответо:'+ tryeAnswers +' из ' + this.answers.length;
                        this.axios.post('/api/tests/results/',{testname: this.questions.test_name, result: result})
                       
                }
            }
        }

    }
</script>

<style scoped>

</style>