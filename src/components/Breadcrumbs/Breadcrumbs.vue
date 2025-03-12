<script setup>
import { computed } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { storeToRefs } from "pinia";
import { useRouter, useRoute } from "vue-router";

const plantsStore = usePlantsStore();
const { currentCategory, currentGenus, genusName, categoryName, searchQuery, currentPage, currentPot, isTableMode } = storeToRefs(plantsStore);

const router = useRouter();
const route = useRoute();


const breadcrumbs = computed(() => {
  const crumbs = [
    { name: "Главная", path: "/" },
    { name: "Каталог", path: "/catalog" },
  ];
  if (currentCategory.value) {
    crumbs.push({
      name: `${categoryName.value}`,
      path: `/catalog?search=${searchQuery.value}&category=${currentCategory.value}&tableMode=${isTableMode.value}&page=${currentPage.value}`,
    });
  }
  if (currentGenus.value) {
    crumbs.push({
      name: `${genusName.value}`,
      path: `/catalog?category=${currentCategory.value}&genus=${currentGenus.value}&tableMode=${isTableMode.value}&page=${currentPage.value}`,
    });
  }
  return crumbs
});

const navigate = (path) => {
    currentGenus.value = ""
    currentPot.value = ""
    currentPage.value = 1
    router.push(path)
    plantsStore.getPlants()
}
</script>

<template>
    <nav :class="isTableMode ? 'breadcrumbs--table' : 'breadcrumbs'">
    <span v-for="(crumb, index) in breadcrumbs" :key="index" class="breadcrumbs__item">
      <span
        v-if="index < breadcrumbs.length - 1"
        class="breadcrumbs__link"
        @click="navigate(crumb.path)"
      >
        {{ crumb.name }}
      </span>
      <span v-else class="breadcrumbs__current">
        {{ crumb.name }}
      </span>
      <span v-if="index < breadcrumbs.length - 1" class="breadcrumbs__separator"> > </span>
    </span>
  </nav>
</template>

<style src="./Breadcrumbs.scss" scoped />
