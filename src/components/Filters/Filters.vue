<script setup>
import { onMounted, computed, watch, watchEffect } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { ref } from "vue";
import Pagination from "../Pagination/Pagination.vue";
import Arrow from "../../assets/images/arrow-down.svg";
import { storeToRefs } from "pinia";
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
const route = useRoute();

const plantsStore = usePlantsStore();
const {
  currentCategory,
  currentGenus,
  isTableMode,
  currentPot,
  searchQuery,
  currentPage,
} = storeToRefs(plantsStore);
const visibleGenusesCount = ref(12);
const visiblePotsCount = ref(30);
const currentGenusPage = ref(1);
const currentPotsPage = ref(1);

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

const toggleCategory = (id) => {
  if (currentCategory.value === id) {
    currentCategory.value = "";
    visibleGenusesCount.value = 12;
  } else {
    currentCategory.value = id;
    visibleGenusesCount.value = 12;
    currentGenus.value = "";
    currentPot.value = "";
    currentPage.value = 1;
    searchQuery.value = "";
    currentGenusPage.value = 1;
  }
  plantsStore.getPlants();
  updateQuery();
};
const toggleGenus = (id) => {
  if (currentGenus.value === id) {
    currentGenus.value = "";
  } else {
    currentGenus.value = id;
    currentPot.value = "";
    searchQuery.value = "";
    currentPage.value = 1;
  }
  plantsStore.getPlants();
  updateQuery();
};
const togglePot = (size) => {
  if (currentPot.value === size) {
    currentPot.value = "";
  } else {
    currentPot.value = size;
    searchQuery.value = "";
    currentPage.value = 1;
  }
  plantsStore.getPlants();
  updateQuery();
};

//подсчитываем кол-во элементов в родов в категории
const totalGenusCount = computed(() => {
  if (!currentCategory.value) return plantsStore.genuses.length;
  return plantsStore.genuses.filter(
    (genus) => genus.category_id === currentCategory.value
  ).length;
});
const totalPotsCount = computed(() => {
  if (plantsStore.pots) return plantsStore.pots.length;
  else return 0;
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

const filteredPots = computed(() => {
  if (plantsStore.pots) {
    // Сортируем массив по полю pot_size по возрастанию
    const sortedPots = [...plantsStore.pots].sort(
      (a, b) => parseInt(a.pot_size) - parseInt(b.pot_size)
    );

    const start = (currentPotsPage.value - 1) * visiblePotsCount.value;
    const end = start + visiblePotsCount.value;
    return sortedPots.slice(start, end);
  }
  return [];
});

const totalGenusPages = computed(() => {
  return Math.ceil(totalGenusCount.value / visibleGenusesCount.value);
});
const totalPotsPages = computed(() => {
  return Math.ceil(totalPotsCount.value / visiblePotsCount.value);
});
const isDisabled = computed(() => window.innerWidth <= 993);

const changeGenusPage = (page) => {
  currentGenusPage.value = page;
};
const changePotsPage = (page) => {
  currentPotsPage.value = page;
};

const toggleSwitch = () => {
  isTableMode.value = !isTableMode.value;
  updateQuery();
};

const resetFilters = () => {
  currentCategory.value = "";
  currentGenus.value = "";
  currentPot.value = "";
  searchQuery.value = "";
  currentPage.value = 1;
  plantsStore.getPlants();
  updateQuery();
};

// onMounted(() => {
//   const storedCategory = localStorage.getItem("currentCategory");
//   const storedGenus = localStorage.getItem("currentGenus");

//   if (storedCategory) {
//     currentCategory.value = storedCategory;
//   }
//   if (storedGenus) {
//     currentGenus.value = storedGenus;
//   }
//   plantsStore.getCategories();
//   plantsStore.getGenuses();
//   plantsStore.getPots();
//   plantsStore.getPlants();
// });

watch(searchQuery, (newValue) => {
  console.log(newValue);
  updateQuery();
});
// watchEffect(async () => {
//     if (window.innerWidth <= 993) {
//       isTableMode.value = false;
//       updateQuery()
//     }
// });

onMounted(async () => {
  await Promise.all([
    plantsStore.getCategories(),
    plantsStore.getGenuses(),
    plantsStore.getPots(),
    plantsStore.getPlants(),
  ]);

  if (route.query.category) {
    currentCategory.value = Number(route.query.category);
  }
  if (route.query.genus) {
    currentGenus.value = Number(route.query.genus);
  }
  if (route.query.pot) {
    currentPot.value = route.query.pot;
  }
  if (route.query.search) {
    searchQuery.value = route.query.search;
  }
  if (route.query.tableMode) {
    if(window.innerWidth <= 993){
      isTableMode.value = route.query.tableMode === "false";
    } else{
      isTableMode.value = route.query.tableMode === "true";
    }
  }
  if (route.query.page) {
    currentPage.value = Number(route.query.page);
  }

  await plantsStore.getPlants();
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
        :disabled="isDisabled"
        @change="toggleSwitch"
        
        id="flexSwitchCheckChecked"
      />
      <label
        :class="
          isTableMode
            ? 'form-check-label form-check-label--active'
            : 'form-check-label'
        "
        for="flexSwitchCheckChecked"
        >Режим таблицы</label
      >
    </div>
    <div
      class="filter__inner"
      v-for="category in plantsStore.categories"
      :key="category.id"
    >
      <div class="filter__box">
        <div
          class="filter__box-categories"
          @click="toggleCategory(category.id)"
        >
          <button class="filter__box-btn">
            <Arrow
              :class="
                currentCategory === category.id
                  ? 'filter__box-arrow filter__box-arrow--active'
                  : 'filter__box-arrow'
              "
            />
          </button>
          <h3
            :class="
              currentCategory === category.id
                ? 'filter__category--active filter__category'
                : 'filter__category'
            "
          >
            {{ category.name }}
          </h3>
        </div>
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
    <p class="filter__pots-title title">Контейнеры</p>
    <div class="filter__pots">
      <div class="form-check" v-for="pot in filteredPots" :key="pot.pot_size">
        <input
          :value="pot.pot_size"
          class="form-check-input"
          type="checkbox"
          :checked="currentPot === pot.pot_size"
          :id="'checkbox-' + pot.pot_size"
          @change="togglePot(pot.pot_size)"
        />
        <label class="form-check-label" :for="'checkbox-' + pot.pot_size">{{
          pot.pot_size
        }}</label>
      </div>
    </div>
    <Pagination
      :currentPage="currentPotsPage"
      :totalPages="totalPotsPages"
      @changePage="changePotsPage"
    />
    <button @click="resetFilters" class="filter__btn btn">
      Сбросить фильтры
    </button>
  </div>
</template>

<style src="./Filters.scss" scoped />
