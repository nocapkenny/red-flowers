<script setup>
import { onMounted, watch, computed } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { ref } from "vue";
const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false,
    required: true,
  },
});

const plantsStore = usePlantsStore();
const currentCategory = ref("");
const currentGenus = ref("");
const filters = ref({category_id: 1, genus_id: 2});

const filteredGenuses = computed(() => {
  if (!currentCategory.value) return plantsStore.genuses;
  return plantsStore.genuses.filter(
    (genus) => genus.category_id === currentCategory.value
  );
});

const resetFilters = () => {
  currentCategory.value = "";
  currentGenus.value = "";
  plantsStore.plants = null;
};

const emit = defineEmits(["update:isBigCard"]);

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
  <div class="container">
    <div class="card mb-4">
      <div class="card-header bg-light">
        <h5 class="mb-0">Фильтры</h5>
      </div>
      <div class="card-body">
        <div class="mb-3">
          <label class="form-label">Категория</label>
          <select
            class="form-select"
            v-model="currentCategory"
            @change="currentGenus = ''"
          >
            <option value="" selected>Любая категория</option>
            <option
              :value="category.id"
              :key="category.id"
              v-for="category in plantsStore.categories"
            >
              {{ category.name }}
            </option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Род</label>
          <select class="form-select" v-model="currentGenus">
            <option value="" selected>Любой род</option>
            <option
              :value="genus.id"
              v-for="genus in filteredGenuses"
              :key="genus.id"
            >
              {{ genus.name }}
            </option>
          </select>
        </div>

        <div class="mb-3 form-check form-switch">
          <input
            class="form-check-input"
            id="flexSwitchCheckDefault"
            type="checkbox"
            :checked="isBigCard"
            @change="$emit('update:isBigCard', !isBigCard)"
          />
          <label class="form-check-label" for="flexSwitchCheckDefault">
            Больше информации
          </label>
        </div>

        <button class="btn btn-secondary w-100" @click="resetFilters">
          Сбросить фильтры
        </button>
      </div>
    </div>
  </div>
</template>

<style src="./Filters.scss" scoped />
