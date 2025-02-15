<script setup>
<<<<<<< HEAD
import { onMounted, watch, computed } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { ref } from "vue";
=======

>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false,
<<<<<<< HEAD
    required: true,
  },
});

const plantsStore = usePlantsStore();
const currentCategory = ref("");
const currentGenus = ref("");

const filteredGenuses = computed(() => {
  if (!currentCategory.value) return plantsStore.genuses; // Если категория не выбрана, показываем все роды
  return plantsStore.genuses.filter(
    (genus) => genus.category_id === currentCategory.value
  );
});

const resetFilters = () => {
  currentCategory.value = "";
  currentGenus.value = "";
};


const emit = defineEmits(["update:isBigCard"]);

onMounted(() => {
  plantsStore.getCategories();
  plantsStore.getGenuses();
});
watch(currentCategory, () => {
  console.log(currentCategory.value);
});
=======
    required: true
  },
})

const emit = defineEmits(['update:isBigCard'])

>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
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
<<<<<<< HEAD
          <select class="form-select" v-model="currentCategory" @change="currentGenus = ''">
            <option value="" selected>Любая категория</option>
            <option
              :value="category.id"
              :key="category.id"
              v-for="category in plantsStore.categories"
            >
              {{ category.name }}
            </option>
=======
          <select class="form-select">
            <option value="">Все категории</option>
            <option value="flowers">Цветы</option>
            <option value="bushes">Кустарники</option>
            <option value="trees">Деревья</option>
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
          </select>
        </div>

        <div class="mb-3">
<<<<<<< HEAD
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

=======
          <label class="form-label">Размер</label>
          <select class="form-select">
            <option value="">Любой размер</option>
            <option value="small">Маленький</option>
            <option value="medium">Средний</option>
            <option value="large">Большой</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Зависимость от солнца</label>
          <select class="form-select">
            <option value="">Любое освещение</option>
            <option value="full-sun">Полное солнце</option>
            <option value="partial-shade">Частичная тень</option>
            <option value="full-shade">Полная тень</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Необходимость воды</label>
          <select class="form-select">
            <option value="">Любой режим полива</option>
            <option value="low">Низкая</option>
            <option value="moderate">Умеренная</option>
            <option value="high">Высокая</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Сезон</label>
          <select class="form-select">
            <option value="">Любой сезон</option>
            <option value="spring">Весна</option>
            <option value="summer">Лето</option>
            <option value="autumn">Осень</option>
            <option value="winter">Зима</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Скорость роста</label>
          <select class="form-select">
            <option value="">Любая скорость</option>
            <option value="slow">Медленная</option>
            <option value="moderate">Умеренная</option>
            <option value="fast">Быстрая</option>
          </select>
        </div>
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
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

<<<<<<< HEAD
        <button class="btn btn-secondary w-100" @click="resetFilters">Сбросить фильтры</button>
=======
        <button class="btn btn-secondary w-100">Сбросить фильтры</button>
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
      </div>
    </div>
  </div>
</template>

<style src="./Filters.scss" scoped />
