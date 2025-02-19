<script setup>
import { ref, computed, watch } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import Skeleton from "../Skeleton/Skeleton.vue";
import Empty from "../Empty/Empty.vue";
import Card from "../Card/Card.vue";
import Pagination from "../Pagination/Pagination.vue";
const plantsStore = usePlantsStore();
import { storeToRefs } from "pinia";

const { currentGenus, searchPlants } = storeToRefs(plantsStore);

const currentPage = ref(1);
const visiblePlantsCount = ref(8);


const totalPLantsCount = computed(() => {
  if (!plantsStore.plants) return 0;
  else if(searchPlants.value){
    return searchPlants.value.length
  }
  return plantsStore.plants.length;
});
const totalPlantsPages = computed(() => {
  return Math.ceil(totalPLantsCount.value / visiblePlantsCount.value);
});

const filteredPlants = computed(() => {
  if (searchPlants.value) {
    const filtered = searchPlants.value;
    const start = (currentPage.value - 1) * visiblePlantsCount.value;
    const end = start + visiblePlantsCount.value;
    return filtered.slice(start, end);
  } else if(!searchPlants.value){
    const filtered = plantsStore.plants;
    const start = (currentPage.value - 1) * visiblePlantsCount.value;
    const end = start + visiblePlantsCount.value;
    return filtered.slice(start, end);
  } else{
    return []
  }
});

const changeCardsPage = (page) => {
  currentPage.value = page;
};

watch(currentGenus, () => {
  currentPage.value = 1;
})


</script>

<template>
  <div class="container text-center">
    <div class="row row-cols-1 row-cols-md-4 g-4" v-auto-animate>
      <Skeleton v-if="plantsStore.isLoading" v-for="i in 4" :key="i" />
      <Empty
        v-if="
          (!plantsStore.isLoading && !plantsStore.plants) ||
          (plantsStore.plants.length === 0 && !plantsStore.isLoading) ||
          (!plantsStore.isLoading && filteredPlants.length === 0)
        "
      />
      <div
        v-if="!plantsStore.isLoading"
        class="col"
        v-for="plant in filteredPlants"
      >
        <Card
          :img="plant.img !== null ? plant.img : ''"
          :id="plant.id"
          :pot="plant.goods_set[0].pot_size"
          :height="plant.goods_set[0].height"
          :descr="plant.description"
          :sort="plant.sort"
          :name="plant.species.name"
          :name-latin="plant.species.name_latin"
        />
      </div>
    </div>
    <Pagination
      :currentPage
      :totalPages="totalPlantsPages"
      @changePage="changeCardsPage"
      class="pagination"
      v-if="!plantsStore.isLoading && totalPlantsPages > 1"
    />
  </div>
</template>

<style lang="scss" scoped>
.container {
  margin-top: 50px;
  margin-bottom: 50px;
}
.pagination {
  margin-top: 30px !important;
}
</style>
