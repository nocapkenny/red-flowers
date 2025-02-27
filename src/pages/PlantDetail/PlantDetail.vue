<script setup>
import { ref } from "vue";
import Header from "../../components/Header/Header.vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import Loader from "../../components/Loader/Loader.vue";
import Table from "@/components/Table/Table.vue";
const plantsStore = usePlantsStore();
const $route = useRoute();

const isLoading = ref(true);

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
