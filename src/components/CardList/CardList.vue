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
import { useRouter, useRoute } from "vue-router";
const router = useRouter();


const { currentGenus, searchPlants, searchQuery, currentCategory, currentPage, totalPages, currentPot, isTableMode } = storeToRefs(plantsStore);

const updateQuery = () => {
  const query = {
    search: searchQuery.value || "",
  };
  if (currentCategory.value) query.category = currentCategory.value;
  if (currentGenus.value) query.genus = currentGenus.value;
  if (currentPot.value) query.pot = currentPot.value;
  if (searchQuery.value) query.search = searchQuery.value;
  if (isTableMode.value) query.tableMode = isTableMode.value.toString();
  if (currentPage.value) query.page = currentPage.value;

  router.push({
    path: "/catalog",
    query,
  });
};

// const visiblePlantsCount = ref(50);

// const totalPLantsCount = computed(() => {
//   if (!plantsStore.plants) return 0;
//   else if (searchPlants.value) {
//     return searchPlants.value.length;
//   }
//   return plantsStore.plants.length;
// });
// const totalPlantsPages = computed(() => {
//   return Math.ceil(totalPLantsCount.value / visiblePlantsCount.value);
// });

// const filteredPlants = computed(() => {
//   if (searchPlants.value) {
//     const filtered = searchPlants.value;
//     const start = (currentPage.value - 1) * visiblePlantsCount.value;
//     const end = start + visiblePlantsCount.value;
//     return filtered.slice(start, end);
//   } else if (!searchPlants.value) {
//     const filtered = plantsStore.plants;
//     const start = (currentPage.value - 1) * visiblePlantsCount.value;
//     const end = start + visiblePlantsCount.value;
//     return filtered.slice(start, end);
//   } else {
//     return [];
//   }
// });
const filteredPlants = computed(() => {
  if (searchPlants.value) {
    const filtered = searchPlants.value;
    return filtered;
  } else if (!searchPlants.value) {
    const filtered = plantsStore.plants;
    return filtered;
  } else {
    return [];
  }
})

const changeCardsPage = (page) => {
  currentPage.value = page;
  plantsStore.getPlants();
  updateQuery();
};

watch(currentGenus, () => {
  currentPage.value = 1;
});
watch(currentCategory, () => {
  currentPage.value = 1;
});

watch(searchQuery, () => {
  currentPage.value = 1;
});

</script>

<template>
  <div class="container text-center">
    <div class="row row-cols-1 row-cols-md-4" v-auto-animate>
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
    <Table
      v-if="plantsStore.isTableMode && filteredPlants.length > 0"
      :head="[
        'Название',
        'Латинское название',
        'Контейнер',
        'Высота',
        'Цена',
        'Описание',
      ]"
      :body="filteredPlants"
    />
    <Pagination
      :currentPage
      :totalPages="totalPages"
      @changePage="changeCardsPage"
      v-if="!plantsStore.isLoading && totalPages > 1"
    />
  </div>
</template>

<style src="./CardList.scss" scoped/>

