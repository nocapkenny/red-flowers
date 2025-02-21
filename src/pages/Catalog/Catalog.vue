<script setup>
import { computed } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";
import Search from "@/components/Search/Search.vue";
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();

const catalogClasses = computed(() => {
  return {
    "container catalog__inner catalog__inner--table": plantsStore.isTableMode,
    "container catalog__inner": !plantsStore.isTableMode,
  };
});

</script>

<template>
  <Header />
  <div class="catalog">
    <div :class="catalogClasses">
      <Filters />
      <div class="catalog__box">
        <Search />
        <CardList />
      </div>
    </div>
  </div>
</template>

<style src="./Catalog.scss" lang="scss" />

