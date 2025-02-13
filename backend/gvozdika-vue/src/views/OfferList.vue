<template lang="pug">
div 
    input(class='form-control' v-model="filter.name" placeholder="Поиск")
    .row
        .col-2
            button(class="btn btn-primary" @click="toDetail({id:'new'})") Создать
        .col-10
            table(class="table table-hover")
                thead
                    tr
                        th id
                        th Дата
                        th Контрагент
                tbody
                    template(v-for="item in list ") 
                        tr(@click="toDetail(item)")
                            td {{item.id}}
                            td {{item.date}}
                            td {{item.counterparty}}

                    
</template>
<script>
import {Offer,} from "@/api"
import {formatNumber} from "@/tools.js"
export default {
    data(){
        return {
            list:[],
            filter:{name:'',genus:''}
        }
    },
    components:{
    },
    methods:{
        formatNumber,
        toDetail(item){
            this.$router.push({name:'offer-detail',params:{id:item.id}})
        },
        async getList(){
            this.list =  (await Offer.objects.filter(this.filter)).results
        },  
    },
    watch:{
        filter:{
            deep:true,
            handler(){
                let query = this.$route.query
                query = {...query,...this.filter}
                this.$router.replace({query})
                return this.getList()}
        }
    },
     mounted(){
        this.filter =this.$route.query
        this.getList()
    }
}
</script>
<style>
.plant-list__name-genus{
    font-weight:600;
    line-height:1.1;
    text-align:left
}
.plant-list__name-species{
    margin-top:5px;
    text-align:left;
    line-height:1.1
}
.parent-list__description{
    font-size:0.8rem
}

.plant-list__img{
    height:120px
}

</style>
