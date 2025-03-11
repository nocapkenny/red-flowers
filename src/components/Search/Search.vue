<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { storeToRefs } from "pinia";
const plantsStore = usePlantsStore();

const { searchQuery, searchPlants, searchGenuses, categories, currentCategory, currentGenus } = storeToRefs(plantsStore)

const isSelected = ref(true)


const selectOption = (option) => {
  searchQuery.value = option.species.name;
  isSelected.value = true
};

const selectGenus = (genus) => {
  searchQuery.value = genus.name
  currentCategory.value = genus.category_id
  currentGenus.value = genus.id
  plantsStore.getPlants()
  searchQuery.value = ""
}

watch(searchQuery, () => {
  if (searchQuery.value.length > 0) {
    isSelected.value = false
  } else if(searchQuery.value.length === 0) {
    isSelected.value = true
  }
})

</script>

<template>
  <div class="search">
    <input
      v-model="searchQuery"
      placeholder="Поиск растений..."
      class="search__input"
    />
    <ul v-if="!isSelected" class="search__suggestions" >
      <li
        v-for="option in searchGenuses"
        :key="option.id"
        class="search__suggestions-item"
        @click="selectGenus(option)"
      >
        {{ categories[option.category_id - 1].name }} -> {{ option.name }} ->
      </li>
      <li
        v-for="option in searchPlants"
        :key="option.id"
        @click="selectOption(option)"
        class="search__suggestions-item"
      >
        {{ option.species.genus.category.name }} -> {{ option.species.genus.name }} -> {{ option.species.name }}
      </li>
    </ul>
  </div>
</template>

<style src="./Search.scss" scoped/>

