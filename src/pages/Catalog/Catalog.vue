<script setup>
import { computed } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";
import Search from "@/components/Search/Search.vue";
import Breadcrumbs from "@/components/Breadcrumbs/Breadcrumbs.vue";
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();
import { useHead } from "@vueuse/head";

useHead({
  title: 'Питомник "Красная Гвоздика"',
  meta: [
    { name: "description", content: 'питомник растений "Красная Гвоздика"' },
    {
      name: "keywords",
      content:
        "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
    },
  ],
});

const catalogClasses = computed(() => {
  return {
    "container catalog__inner catalog__inner--table": plantsStore.isTableMode,
    "container catalog__inner": !plantsStore.isTableMode,
  };
});
</script>

<template>
  <Header />
  <section class="catalog">
    <div :class="catalogClasses">
      <div class="catalog__row">
        <Breadcrumbs />
      </div>
      <div class="catalog__row">
        <Filters />
        <div class="catalog__box">
          <Search />
          <CardList />
        </div>
      </div>
    </div>
  </section>
</template>

<style src="./Catalog.scss" lang="scss" />
