<script setup>
import { ref, computed, watch } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import Skeleton from "../Skeleton/Skeleton.vue";
import Empty from "../Empty/Empty.vue";
import Card from "../Card/Card.vue";
import Pagination from "../Pagination/Pagination.vue";
import Table from "../Table/Table.vue";
const plantsStore = usePlantsStore();
import { storeToRefs } from "pinia";

const { currentGenus, searchPlants, searchQuery } = storeToRefs(plantsStore);

const currentPage = ref(1);
const visiblePlantsCount = ref(8);

const totalPLantsCount = computed(() => {
  if (!plantsStore.plants) return 0;
  else if (searchPlants.value) {
    return searchPlants.value.length;
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
  } else if (!searchPlants.value) {
    const filtered = plantsStore.plants;
    const start = (currentPage.value - 1) * visiblePlantsCount.value;
    const end = start + visiblePlantsCount.value;
    return filtered.slice(start, end);
  } else {
    return [];
  }
});

const changeCardsPage = (page) => {
  currentPage.value = page;
};

watch(currentGenus, () => {
  currentPage.value = 1;
});

watch(searchQuery, () => {
  currentPage.value = 1;
});
</script>

<template>
  <div class="container text-center">
    <div class="row row-cols-1 row-cols-md-4 g-4" v-auto-animate>
      <Skeleton
        v-if="plantsStore.isLoading && !plantsStore.isTableMode"
        v-for="i in 4"
        :key="i"
      />
      <Empty
        v-if="
          (!plantsStore.isLoading && !plantsStore.plants) ||
          (plantsStore.plants.length === 0 && !plantsStore.isLoading) ||
          (!plantsStore.isLoading && filteredPlants.length === 0)
        "
      />
      <div
        v-if="!plantsStore.isLoading && !plantsStore.isTableMode"
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
          :key="plant.id"
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
    <Table
      v-if="plantsStore.isTableMode && plantsStore.plants.length > 0"
      :head="['Название', 'Описание', 'Цена']"
      :body="filteredPlants"
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
.row > * {
  flex: 1 0 25%;
  max-width: 25%;
  padding: 0 15px;
}

@media (max-width: 1024px) {
  .row > * {
    flex: 1 0 33.333%;
    max-width: 33.333%;
  }
}
@media (max-width: 840px) {
  .row > * {
    flex: 1 0 50%;
    max-width: 50%;
  }
}
@media (max-width: 670px) {
  .row > * {
    flex: 1 0 100%;
    max-width: 100%;
  }
}
</style>
