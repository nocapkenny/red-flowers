<template lang="pug">
div
    div(v-if="plant.species")
        .row
            .col-8
                h2 {{plant.species.genus.name}} 
                    small {{plant.species_name}}
                h4 {{plant.sort}}
            .col-4
        .row
            .col-5
                img(:src="plant.detail")
            .col-7
                h2 Описание
                div {{plant.species.description}}
                div {{plant.description}}
                hr
                goods-table(:value="plant.goods_set" @update="updateGoods")
        hr
        div(class="mb-2" v-if="user.permissions.indexOf('change_plant')>=0")
                button(v-if="!edit" class="btn btn-primary right" @click="edit=true") изменить
                button(v-else class="btn btn-primary right" @click="save()") сохранить
        .row
            .col-12
                h2 Использование 
                div(v-if='!edit') {{plant.usage}}
                div(v-else) 
                    textarea(v-model="plant.usage" class="form-control")
        .row
            .col-12
                h2 Агротехника
                div(v-if='!edit') {{plant.technology}}
                div(v-else)
                    textarea(v-model="plant.technology" class="form-control")
</template>
<script>
import {Plant} from "@/api.js"
import GoodsTable from "@/components/GoodsTable"
export default{
    name:'plant-detail',
    components:{
        GoodsTable,
    },
    computed:{
        user(){
            return this.$store.state.user
        },
        id(){
            return this.$route.params.id
        }
    },
    data(){
        return{
            plant:{},
            edit:false,
        }
    },
    methods:{
        updateGoods(value){
            this.plant.goods_set=value
        },
        async getPlant(){
            this.plant = await Plant.objects.get(this.id)
        },
        async save(){
            const {id,description,usage,technology} = this.plant
            const plant = {
                id,description,usage,technology
            }
            this.plant = await  Plant.objects.save(plant)
            this.edit=false
        }
    },
    mounted(){
        this.getPlant()
    }
}
</script>
