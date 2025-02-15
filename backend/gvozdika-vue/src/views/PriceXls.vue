<template lang="pug">
div
    div(v-for="item in  categoryList")
        div
            a(:href="getHref(item)") {{item.name}}
</template>
<script>
import {Category,categoryUrl} from "@/api"
export default {
    name:'print-xls',
    data(){
        return {
            categoryList:[]
        }
    },
    methods:{
        async  getCategory(){
            this.categoryList = (await Category.objects.filter()).results
        },
        getHref(item){
            return categoryUrl + `${item.id}/price_xls`
        }
    },
    mounted(){
        this.getCategory()

    }
}
</script>
