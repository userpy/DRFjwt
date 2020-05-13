<template>
    <div>
          <b-form-group class="text-left" label="">
              <div v-if="showAnswers">
                   <div v-if="multiple_choice">
                      <b-form-checkbox  v-for="i in answers" :key="i" v-model="selected" name="some-radios"  :value="i.answer">{{i.answer}}</b-form-checkbox>
                    </div>
                   <div v-else>
                     <b-form-radio      v-for="i in answers" :key="i" v-model="selected" name="some-radios"  :value="i.answer">{{i.answer}}</b-form-radio>
                   </div>
              </div>
              <div v-else>
                  <h3>Варианты ответов не добавлены</h3>
              </div>
          </b-form-group>
    </div>
</template>

<script>
    export default {
        name: "AnswersComponent",
        props:{
            answers:[],
            multiple_choice:null,
            button_next_disabled:null,
            selected_answer:null,
            current_question:null
        },
        computed:{
            showAnswers: function () {
                return this.answers.length > 0? true: false;
            }
        },
        methods:{
            OnlyTrue: function() {
                let arrOnlyTrue = this.answers.map((item) => {
                    if (item.сorrect_answer == true) {
                        return item
                    }
                }).filter(item => item != undefined);
                return arrOnlyTrue
            },
            OnlyTrueAndSelect: function(select) {
                let arrOnlyTrue = this.answers.map((item) => {
                    if (item.сorrect_answer == true && item.answer === select) {
                        return item
                    }
                }).filter(item => item != undefined);
                return arrOnlyTrue
            },
            TrueАnswer: function (select) {
            let arr = this.answers.map((item) => {
                    if (select === item.answer) {
                        return item
                    }
                }).filter(item => item != undefined);
             return arr[0];
            },
            TrueАnswerMyltiplee: function (select) {
                let onlyTrueElement = this.OnlyTrue();
                let elements = [];
                select.forEach(item => {
                    let T = this.OnlyTrueAndSelect(item);
                    if (T.length > 0){
                        elements.push(T);
                    }
                });
                if (elements.length === onlyTrueElement.length && elements.length === select.length){
                     return { answer: select, сorrect_answer: true}
                } else {
                     return { answer: select, сorrect_answer: false}
                }

            }
        },
        data: function(){
            return{
                selected: [],
            }
        },
        watch: {
            selected: function () {
                     if (this.selected.length > 0){
                     this.$emit('update:button_next_disabled', false);
                     if (this.multiple_choice){
                         let answer  = this.TrueАnswerMyltiplee(this.selected);
                         answer.current_question = this.current_question;
                         this.$emit('update:selected_answer', answer);
                     } else {
                         let answer  = this.TrueАnswer(this.selected);
                         answer.current_question = this.current_question;
                         this.$emit('update:selected_answer', answer);
                     }
                     } else {
                     this.$emit('update:selected_answer', this.TrueAnswer);
                     this.$emit('update:button_next_disabled', true);
                    }
            },
            answers: function () {
                this.selected = [];
            }
        }
    }
</script>

<style scoped>

</style>