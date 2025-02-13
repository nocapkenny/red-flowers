<template lang="pug">
div(class="category-tree")
    h2 Саженцы
    div()
        div(class="category-tree__category" v-for="category,index in category_list" @click="selectCategory(index)")
            div(class="category-tee__name" ) {{category.name}}
            div(v-for="genus in category.genus_set" class="category-tree__genus" @click.stop="selectGenus(genus)" :class="genus.id==value.genus?'active':''") {{genus.name}}


</template>
<script>
import {Genus,Category} from "@/api.js"
export default{
    name:'category-tree',
    props:['value'],
    data(){
        return {
            genus_list:[],
            category_list:[],
            open_catetory:[]
        }
    },
    methods:{
        selectGenus(genus){
            this.$emit('input',{...this.value,genus:genus.id})
        },
        async selectCategory(index){
            if (this.category_list[index].genus_set){
                this.category_list[index].genus_set = undefined
                let idx = this.open_catetory.indexOf(this.category_list[index].id)
                if (idx>=0){
                    this.open_catetory.splice(idx,1)
                    this.$emit('input',{...this.value,genus:undefined,genus__category:undefined})
                }
            }else{
                const category = this.category_list[index]
                const response =await Genus.objects.filter({category})
                this.category_list[index].genus_set = response.results
                const id = this.category_list[index].id
                if (this.open_catetory.indexOf(id)<0) {
                    this.open_catetory.push(id)
                    this.$emit('input',{...this.value,genus__category:id})
                }
            }

            let query = this.$route.query
            this.$router.replace({query:{...query,open_catetory:this.open_catetory}})
        },
        async getGenus(){
            this.genus_list =  await Genus.objects.filter(this.filter)
        }, 
        async getCategory(){
            this.category_list=  (await Category.objects.filter(this.filter)).results
            for(let x in this.category_list){
                console.log(this.open_catetory.includes(this.category_list[x].id))
                if ( this.open_catetory.includes(this.category_list[x].id)){
                    console.log(x)
                    this.selectCategory(x)
                }
            }
        }  
    },
    mounted(){
        let open_catetory = this.$route.query.open_catetory
        if (open_catetory){
            if (typeof open_catetory === 'string'){

                this.open_catetory=[+open_catetory]
            } 
            else{
                for(let x in open_catetory){
                    open_catetory[x] = +open_catetory[x]
                }
                this.open_catetory=open_catetory

            }
        }
        this.getCategory()
    }

}
</script>
<style>
.category-tree__genus{
    padding-left:20px
}

.category-tee__name{
    cursor:pointer;
}
.category-tree__genus.active{
    font-weight:600
}
</style>

