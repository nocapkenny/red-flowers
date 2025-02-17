<script setup>
import { onMounted, watch, computed } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { ref } from "vue";

const plantsStore = usePlantsStore();
const currentCategory = ref("");
const currentGenus = ref("");
const filters = ref({ category_id: "", genus_id: "" });
const visibleGenusesCount = ref(12);

const toggleCategory = (id) => {
  if (currentCategory.value === id) {
    currentCategory.value = "";
    visibleGenusesCount.value = 12;
  } else {
    currentCategory.value = id;
    visibleGenusesCount.value = 12;
  }
};
const toggleGenus = (id) => {
  if (currentGenus.value === id) {
    currentGenus.value = "";
  } else {
    currentGenus.value = id;
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
  return filtered.slice(0, visibleGenusesCount.value);
});

const showMoreBtn = computed(() => {
  return filteredGenuses.value.length < totalGenusCount.value;
})
const showCloseBtn = computed(() => {
  return filteredGenuses.value.length === totalGenusCount.value && filteredGenuses.value.length !== visibleGenusesCount.value;
})

const showMoreGenuses = () => {
  visibleGenusesCount.value += 12;
};
const closeGenuses = () => {
  visibleGenusesCount.value = 12;
}

onMounted(() => {
  plantsStore.getCategories();
  plantsStore.getGenuses();
  plantsStore.getPlants(filters.value);
});
watch(currentGenus, () => {
  if (currentGenus.value && currentGenus.value !== "") {
    filters.value = {
      category_id: currentCategory.value,
      genus_id: currentGenus.value,
    };
    plantsStore.getPlants(filters.value);
  }
});
</script>

<template>
  <div class="filter">
    <p class="filter__title title">Фильтры</p>
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
          <button
            @click="showMoreGenuses"
            class="filter__btn btn"
            v-if="showMoreBtn"
          >
            Показать больше
          </button>
          <button
            @click="closeGenuses"
            class="filter__btn btn"
            v-if="showCloseBtn"
          >
            Свернуть
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style src="./Filters.scss" scoped />
