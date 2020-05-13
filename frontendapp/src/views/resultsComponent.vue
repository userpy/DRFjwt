<template>
    <div>
        <b-table striped hover :items="result"></b-table>
    </div>
</template>

<script>
    export default {
        name: "resultsComponent",
        data() {
            return {
                result:''
            }
        },
        mounted() {
            this.result = '';
            this.axios.get('/api/tests/results/').then(response => {
                this.result = response.data
            }).catch().finally()
        }
    }
</script>

<style scoped>

</style>