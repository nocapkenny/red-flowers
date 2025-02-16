<template lang="pug">
div 
    input(class='form-control' v-model="filter.name" placeholder="Поиск")
    .row
        .col-md-2
            category-tree(:value="filter" @input="filter=$event")
        .col-md-10
            table(class="table table-hover")
                thead
                    tr
                        th
                        th Фото
                        th Нзавание
                        th Описание
                        th cорт
                        th Цена
                tbody
                    template(v-for="item in list ") 
                        tr(@click="toDetail(item)")
                            td {{item.id}}
                            td
                                img(class="plant-list__img" :src="item.preview")
                            td
                                div(class="plant-list__name-genus")  {{item.species.genus.name}}
                                div(class="plant-list__name-species") {{item.species.name}}
                            td  {{item.species.description}}
                            td {{item.sort}}
                            td  
                                b(class="text-nowrap") от {{formatNumber(item.min_price)}}
            PaginationNav(:modelValue="page",:maxPage='maxPage' @update:modelValue="changePage")

                    
</template>
<script>
import {Plant,} from "@/api"
import CategoryTree from "@/components/CategoryTree.vue"
import {formatNumber} from "@/tools.js"
import PaginationNav from "@/components/PaginationNav"
export default {
    data(){
        return {
            list:[],
            page:1,
            maxPage:0,
            filter:{name:'1',genus:'2'}
        }
    },
    components:{
        CategoryTree,
        PaginationNav,
    },
    methods:{
        formatNumber,
        changePage(event){
            this.page=event
            let query = this.$route.query
            query = {...query,...this.filter,page:this.page}
            this.$router.replace({query})
            this.getList()
        },
        toDetail(item){
            this.$router.push({name:'plant-detail',params:{id:item.id}})
        },
        async getList(){
            let filter = {...this.filter,page:this.page}
            const responce = await Plant.objects.filter(filter)
            this.list =  responce.results
            this.maxPage = responce.total_pages
        },  
    },
    watch:{
        filter:{
            deep:true,
            handler(){
                let query = this.$route.query
                this.page=1
                query = {...query,...this.filter,page:this.page}
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
