<script setup>
import { ref, watch } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import Skeleton from "../Skeleton/Skeleton.vue";
import Card from "../Card/Card.vue";
const plantsStore = usePlantsStore();
const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false, 
    required: true
  },
})



</script>

<template>
  <div class="container text-center">
    <div class="row row-cols-1 row-cols-md-4 g-4" v-auto-animate>
      <Skeleton v-if="plantsStore.isLoading" v-for="i in 4" :key="i" />
      <div v-if="!plantsStore.isLoading" class="col" v-for="plant in plantsStore.plants">
        <Card :id="plant.id" :pot="plant.goods_set[0].pot_size" :height="plant.goods_set[0].height" :descr="plant.description" :sort="plant.sort" :name="plant.species.name" :name-latin="plant.species.name_latin" :isBigCard="isBigCard"/>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
