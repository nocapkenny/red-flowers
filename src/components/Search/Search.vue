<script setup>
import { ref, computed, onMounted } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { storeToRefs } from "pinia";
const plantsStore = usePlantsStore();

const { searchQuery, searchPlants } = storeToRefs(plantsStore)


const selectOption = (option) => {
  searchQuery.value = option.species.name;
};

onMounted(()=>{
  console.log(searchPlants.value)
})
</script>

<template>
  <div class="search">
    <input
      v-model="searchQuery"
      placeholder="Поиск растений..."
      class="search__input"
    />
    <ul v-if="searchQuery.length > 0" class="search__suggestions" >
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

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
.search {
  position: relative;
  width: 100%;
  &__input {
    outline: none;
    width: 100%;
    padding: 10px;
    border-radius: 10px;
  }
  &__suggestions {
    list-style: none;
    padding: 0;
    margin: 0;
    position: absolute;
    width: 100%;
    background: $white;
    border-left: 3px solid $black;
    border-bottom: 3px solid $black;
    max-height: 150px;
    overflow-y: auto;
    z-index: 1000;
    border-radius: 15px;
  }
  &__suggestions-item {
    padding: 5px 10px !important;
    
    cursor: pointer;
  }
  &__suggestions-item:hover {
    background: #f0f0f0;
  }
}

</style>
