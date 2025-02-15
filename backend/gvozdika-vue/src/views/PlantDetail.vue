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
            .col-md-5
                img(:src="activeImage? activeImage.detail:''")
                .row
                    .col-12
                        img(@click="activeImage=img" :src="img.preview" v-for="img in photoList")
                        input(type="file" id="file" ref="file_img" @input="sendFile" v-if="user.permissions.indexOf('change_plant')>=0")

            .col-md-7
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
import {Plant,Photo} from "@/api.js"
import GoodsTable from "@/components/GoodsTable"
import axios from "axios"
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
            photoList:[],
            activeImage:{},
        }
    },
    methods:{

      async sendFile(){
        let formData = new FormData();
          if (this.$refs.file_img.files[0]){
              formData.append('img', this.$refs.file_img.files[0]);
              if (!this.plant.detail){
                this.plant = (await axios.patch(Plant.url+this.plant.id+'/', formData)).data
             }else{
                    formData.append('plant', this.plant.id);
                    let photo = await Photo.objects.save(formData)
                 this.photoList.push(photo)
             }
          }
      },

        updateGoods(value){
            this.plant.goods_set=value
        },
        async getPlant(){
            this.plant = await Plant.objects.get(this.id)
            this.activeImage = {detail:this.plant.detail}
            this.photoList = (await Photo.objects.filter({plant:this.id})).results
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
