<template>
    <div id="app">
        <div class="header">
            <div class="container">
                <a href="http://gvozdika.perm.ru"><div class="logo"></div></a>
            </div>
            <div  class="container" id="nav">
                <router-link to="/" exact> Каталог</router-link> |
                <router-link to="/price_xls/" exact>Прайсы</router-link> |
                <router-link to="/offer/" exact v-if="user.username">Коммерческие предложения</router-link> |
            </div>
        </div>
        <div class="container">
            <router-view/>
        </div>
    </div>

</template>

<script>

export default {
    name: 'App',
    computed:{
        user(){
            return this.$store.state.user
        }
    },
    mounted(){
        this.$store.dispatch('getUser')
        console.log('mount')
        console.log(this.$store)
    },
    components: {
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
.logo {
    padding: 0px;
    width: 275px;
    height: 91px;
    background: url("/logo.png") no-repeat;
}
</style>
