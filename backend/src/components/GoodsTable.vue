<template lang="pug">
table(class="table table-bordered")
    thead
        tr
            th Высота
            th Контейнер
            th цена

    tbody
        tr(v-for="item in value")
            template(v-if="!edit" )
                td {{item.height}}
                td {{item.pot_size}}
                td 
                    b {{formatNumber(item.price)}}
            template(v-else)
               td {{item.height}}
               td {{item.pot_size}}
               td 
                   input(v-model="item.price" class="form-control") 
        tr(v-if='edit')
            td
            td
            td()
                button(class="btn btn-primary mr-2" @click="save") сохранить
                button(class="btn btn-danger" @click="cancel") отмена
        tr(v-else-if='user.permissions.indexOf("change_plant")>=0')
            td
            td
            td
                button(class="btn btn-primary float-right" @click="edit=true" ) Изменить




</template>
<script>
import {Goods} from "@/api"
import {formatNumber} from "@/tools"
export default {
    name:'goods-table',
    props:['value'],
    data(){
        return{
            edit:false
        }
    },
    computed:{
        user(){
            return this.$store.state.user
        }
    },
    methods:{
        formatNumber,
       async save(){
            let new_list = []
           for (let x of this.value){
               new_list.push(await Goods.objects.save(x))
            }
           this.$emit('update',new_list)
            this.edit =false
        },
        async cancel(){
            let new_list = []
           for (let x of this.value){
               new_list.push(await Goods.objects.get(x.id))
            }
            this.edit =false

           this.$emit('update',new_list)
        }

    }
}
</script>
