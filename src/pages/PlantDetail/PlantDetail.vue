<script setup>
import { ref, computed } from "vue";
import Header from "../../components/Header/Header.vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import Loader from "../../components/Loader/Loader.vue";
import Table from "@/components/Table/Table.vue";
import { useHead } from "@vueuse/head";
const plantsStore = usePlantsStore();
const $route = useRoute();

const isLoading = ref(true);

const headData = computed(() => {
  const defaultTitle = "Красная Гвоздика";
  const defaultMeta = [
    { name: "Растение", content: "Загрузка..." },
    {
      name: "keywords",
      content:
        "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
    },
  ];

  if (!isLoading.value && plantsStore.plant && plantsStore.plant.species) {
    return {
      title: `Красная Гвоздика. ${plantsStore.plant.species.name}`,
      meta: [
        { name: "Растение", content: plantsStore.plant.species.name },
        {
          name: "keywords",
          content:
            "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
        },
      ],
    };
  }

  return {
    title: defaultTitle,
    meta: defaultMeta,
  };
});

useHead(headData);

onMounted(async () => {
  try {
    isLoading.value = false;
    await plantsStore.getPlantById($route.params.id);
  } catch (e) {
    console.log(e);
  }
});
</script>

<template>
  <Header />
  <div class="plant">
    <div class="plant__inner">
      <Loader v-if="isLoading" />
      <div class="plant__box" v-if="!isLoading">
        <div class="plant__img-wrapper">
          <img
            :src="plantsStore.plant.img"
            alt=""
            class="plant__img"
            v-if="plantsStore.plant.img"
          />
          <img
            src="../../assets/images/sample.png"
            class="plant__img--sample"
            alt="cardImg"
            v-else
          />
        </div>
        <div class="plant__info">
          <h5 class="plant__title title">
            {{ plantsStore.plant.species.name }}
          </h5>
          <p class="plant__text">
            {{ plantsStore.plant.species.description }}
          </p>
          <p class="plant__text" >
            {{ plantsStore.plant.description }}
          </p>
          <p class="plant__text" v-if="plantsStore.plant.technology">
          <h2 class="plant__title title"> Агротехника </h2>
            {{ plantsStore.plant.technology }}
          </p>
          <p class="plant__text" v-if="plantsStore.plant.usage">
          <h2 class="plant__title title"> Использование </h2>
            {{ plantsStore.plant.usage }}
          </p>
        </div>
        <div class="plant__table">
          <Table
            :head="['Высота', 'Контейнер', 'Цена']"
            :body="plantsStore.plant.goods_set"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style src="./PlantDetail.scss" scoped />
