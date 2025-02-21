<script setup>
import { onMounted, computed } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { ref } from "vue";
import Pagination from "../Pagination/Pagination.vue";
import { storeToRefs } from "pinia";

const plantsStore = usePlantsStore();
const { currentCategory, currentGenus, isTableMode } = storeToRefs(plantsStore);
const visibleGenusesCount = ref(12);
const currentGenusPage = ref(1);


const toggleCategory = (id) => {
  if (currentCategory.value === id) {
    currentCategory.value = "";
    visibleGenusesCount.value = 12;
  } else {
    currentCategory.value = id;
    visibleGenusesCount.value = 12;
    currentGenus.value = ""
    plantsStore.getPlants()
    currentGenusPage.value = 1
    // localStorage.setItem("currentCategory", id);
  }
};
const toggleGenus = (id) => {
  if (currentGenus.value === id) {
    currentGenus.value = "";
  } else {
    currentGenus.value = id;
    plantsStore.getPlants()
    // localStorage.setItem("currentGenus", id);
  }
};


//подсчитываем кол-во элементов в родов в категории
const totalGenusCount = computed(() => {
  if (!currentCategory.value) return plantsStore.genuses.length;
  return plantsStore.genuses.filter(
    (genus) => genus.category_id === currentCategory.value
  ).length;
});

//фильтруем список родов исходя из выбранной категории, отображаем только первые 12
const filteredGenuses = computed(() => {
  if (!currentCategory.value) return plantsStore.genuses;
  const filtered = plantsStore.genuses.filter(
    (genus) => genus.category_id === currentCategory.value
  );
  const start = (currentGenusPage.value - 1) * visibleGenusesCount.value;
  const end = start + visibleGenusesCount.value;
  return filtered.slice(start, end);
});

const totalGenusPages = computed(() => {
  return Math.ceil(totalGenusCount.value / visibleGenusesCount.value);
});


const changeGenusPage = (page) => {
  currentGenusPage.value = page;
};

const toggleSwitch = () => {
  isTableMode.value = !isTableMode.value
  console.log(isTableMode.value)
}

onMounted(() => {
  plantsStore.getCategories();
  plantsStore.getGenuses();
  plantsStore.getPlants();
});

</script>

<template>
  <div class="filter">
    <p class="filter__title title">Фильтры</p>
    <div class="form-check form-switch">
      <input
        class="form-check-input"
        type="checkbox"
        role="switch"
        :checked="isTableMode"
        @change="toggleSwitch"
        id="flexSwitchCheckChecked"
      />
      <label :class="isTableMode ? 'form-check-label form-check-label--active' : 'form-check-label'" for="flexSwitchCheckChecked">Режим таблицы</label>
    </div>
    <div
      class="filter__inner"
      v-for="category in plantsStore.categories"
      :key="category.id"
    >
      <div class="filter__box">
        <h3
          :class="
            currentCategory === category.id
              ? 'filter__category--active filter__category'
              : 'filter__category'
          "
          @click="toggleCategory(category.id)"
        >
          {{ category.name }}
        </h3>
        <div class="filter__genus-box" v-if="currentCategory === category.id">
          <div
            class="filter__genuses"
            v-for="genus in filteredGenuses"
            :key="genus.id"
          >
            <p
              :class="
                currentGenus === genus.id
                  ? 'filter__genus--active filter__genus'
                  : 'filter__genus'
              "
              @click="toggleGenus(genus.id)"
            >
              {{ genus.name }}
            </p>
          </div>
          <Pagination
            :currentPage="currentGenusPage"
            :totalPages="totalGenusPages"
            @changePage="changeGenusPage"
            v-if="totalGenusPages > 1"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style src="./Filters.scss" scoped />
