<template lang="pug">
div
    h2 Коммерческое предложение  {{offer.id}}
    .row
        .col-2 Контрагент:
        .col-10
            v-select(v-model="offer.counterparty" :options="counterpartyList"
            label="name"
            @search="getCounterpartyList")
    div Дата: {{offer.date}}
    a(class="btn btn-primary" :href="'/offer/'+id+'/pdf'" v-if="id!='new'") PDF

    table(class="table table-hover")
        thead 
            tr
                th
                th Наименование
                th Кол-во
                th цена
                th итого
        tbody
            tr(v-for="item in item_list")
                td {{item.id}}
                td
                    v-select(:options="goodsList" :filterable="false"
                    v-model="item.goods"
                    label="species_name"
                    @search="getPlanList")
                        template(v-slot:option="option")
                            span(:class="option.icon") {{option.species_name}} 
                            span 
                                b v {{option.pot_size}}
                td 
                    input(v-model="item.count" class="form-control")
                td {{+item.goods.price}}
                td {{item.count*(+item.goods.price)}}
        button(class="btn btn-primary" @click="addItem") Добавтиь
        hr
        button(class="btn btn-primary" @click="save") Сохранить
</template>
<script>
import {Offer,OfferItem,Goods,Counterparty} from '@/api'
import {debounce} from "lodash"
export default {
    name:'offer-detail',
    data(){
        return {
            offer:{},
            item_list:[],
            goodsList:[],
            counterpartyList:[]
        }
    },
    computed:{
        id(){
            return this.$route.params.id
        }
    },
    methods:{
        addItem(){
            this.item_list.push({'offer':this.id,count:1,goods:{}})
        },
        async save(){
            this.offer = await Offer.objects.save(this.offer)
            if (this.id=='new')
                this.$router.replace({params:{id:this.offer.id}})
            for (let x in this.item_list){
                let item = this.item_list[x]
                if (item.goods){
                    item = await OfferItem.objects.save(item)
                    this.item_list[x]=item
                }
            }
        },
        async getObject(){
            this.offer = await Offer.objects.get(this.id)
        },
        async getList(){
            if (this.id){
                this.item_list = (await OfferItem.objects.filter({offer:this.id})).results
            }
        },
        getCounterpartyList:debounce(async function(search){
                this.counterpartyList = (await Counterparty.objects.filter({search})).results
        },300),

        getPlanList:debounce(async function(search){
            if (search!=''){
                this.goodsList = (await Goods.objects.filter({search})).results
            }
        },300)
    },
    mounted(){
        this.getObject()
        this.getList()
        this.getPlanList()
    }
}
</script>
